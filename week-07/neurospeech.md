──────────────────┬──────────────────────────────────────────────────┬──────────────────────────────────────────────────────┐
│ DisVoice module  │                DisVoice features                 │          NeuroSpeech equivalent (per paper)          │
├──────────────────┼──────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│                  │ 7 descriptors (F0 1st/2nd deriv, jitter,         │                                                      │
│ Phonation        │ shimmer, APQ, PPQ, log energy) × 4 functionals = │ phonVowels.py — 5 features only: jitter, shimmer,    │
│                  │  28 features. Works on vowels + continuous       │ APQ, PPQ, %unvoiced. Vowels only, no functionals.    │
│                  │ speech.                                          │                                                      │
├──────────────────┼──────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│                  │ 122 descriptors (BBE, MFCCs + derivatives at     │ artCont.py — BBE onset/offset only (no MFCCs).       │
│ Articulation     │ onset/offset, F1/F2 + derivatives) × 4           │ Separately, artVowels.py adds VSA/VPA/FCR            │
│                  │ functionals                                      │ (vowel-triangle geometry) — DisVoice has no          │
│                  │                                                  │ equivalent for this part.                            │
├──────────────────┼──────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│                  │ 103 features: F0 + energy contour stats (incl.   │ prosody.py — 12 features: voiced/silence rate,       │
│ Prosody          │ per-segment linear-fit tilt/MSE, first/last      │ duration stats, F0 avg/std/max, energy avg/std/max   │
│                  │ segment), duration stats                         │                                                      │
├──────────────────┼──────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│ Glottal          │ 9 descriptors (GCI variability, OQ, NAQ, H1-H2,  │ Not present in NeuroSpeech.                          │
│                  │ HRF) × 4 functionals = 36 features               │                                                      │
├──────────────────┼──────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│ Phonological     │ 18 phonet-based class log-likelihoods × 6        │ Not present in NeuroSpeech.                          │
│                  │ functionals = 108 features                       │                                                      │
├──────────────────┼──────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│ Representation   │ Autoencoder-based embeddings                     │ Not present in NeuroSpeech.                          │
│ learning         │                                                  │                                                      │
└──────────────────┴──────────────────────────────────────────────────┴──────────────────────────────────────────────────────┘

NeuroSpeech-only — no DisVoice module covers these at all:

┌───────────────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│   NeuroSpeech     │                                            What it measures                                            │
│      module       │                                                                                                        │
├───────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ DDK               │ 11 features: F0/energy variability, DDK rate/regularity/duration, pause rate/duration/regularity —     │
│                   │ from repeated-syllable tasks (e.g. "pa-ta-ka")                                                         │
├───────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Intelligibility   │ Word Accuracy + DTW similarity, via Google ASR on read sentences vs. reference text                    │
├───────────────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Clinical          │ Pretrained SVM/SVR predicting per-articulator dysarthria scores (respiration, lips, palate, larynx,    │
│ prediction        │ tongue) + UPDRS-III severity                                                                           │
└───────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────┘

