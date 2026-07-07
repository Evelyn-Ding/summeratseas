# Resources

## Papers

<!-- | Title | Authors | Year | Link | Notes | -->
<!-- |-------|---------|------|------|-------| -->

## Datasets

| Name | Date | Description | Size | Speech Tasks | Naming Convention | Notes |
|------|------|--------------|------|--------------|--------------------|-------|
| [Saarbrücken Voice Database (SVD)](https://zenodo.org/records/16874898) | 2008 (v2) | German speech recordings for phonetics, speech pathology, and computer-assisted speech analysis research; one of the most widely used public repositories of voice recordings for studying vocal pathologies (e.g., hoarseness, polyps, paralysis); includes "normal" and pathological samples recorded under controlled conditions; audio stored as .nsp (needs conversion to .wav) | **Morbus Parkinson: only 1 subject** (ID 1580) in this download — not just "small N," literally N=1; **healthy: 687 recording sessions on disk** (local `overview.csv` catalogs 869 sessions / 854 unique speakers total, so this is a partial download of the full healthy set) | (1) vowel phonation [i, a, u] at normal, high, and low pitch; (2) vowel phonation [i, a, u] with rising-falling pitch; (3) recording of the sentence "Guten Morgen, wie geht es Ihnen?" ("Good morning, how are you?"); voice signal + EGG (electroglottograph) signal stored as separate files per task | Folder per subject named by `AufnahmeID` (recording session ID), with subfolders `vowels/`, `sentences/`, `remarks/`; files: `{AufnahmeID}-{a\|i\|u}_{l\|h\|n\|lhl}.nsp` (vowel at low/high/normal/rising-falling pitch), `{AufnahmeID}-iau.nsp` (combined vowel sequence), `{AufnahmeID}-phrase.nsp` (sentence), each paired with a `-egg.egg` file; `overview.csv` columns: `AufnahmeID, AufnahmeTyp, AufnahmeDatum, Diagnose, SprecherID, Geburtsdatum, Geschlecht, Pathologien` | **PD subset is a single patient (ID 1580, diagnosis "Hypotone Komponente, (vox senilis)", pathology tag "Morbus Parkinson") — not usable as a meaningful test set on its own**, only for sanity-checking a pipeline; includes a text file with full per-recording metadata — see [Appendix: SVD Pathology Term Translations](#appendix-svd-pathology-term-translations-german--english) for category names |
| [NeuroVoz](https://zenodo.org/records/10777657) | 2024 | Spanish PD vs HC dataset; 112 participants (54 PD, 58 HC), recorded in ON medication state; raw audio with phonatory, articulatory, and prosodic insights | 2,977 audio files (2,976 found in local `audios/` folder); 112 participants (54 PD, 58 HC) — confirmed via [Scientific Data paper](https://www.nature.com/articles/s41597-024-04186-z); on disk: 1,467 PD-prefixed + 1,509 HC-prefixed files | Sustained vowel phonations (5 Spanish vowels /a e i o u/, 3 reps each), DDK test (/pa-ta-ka/ repeated ≥5 sec), 16 structured listen-and-repeat utterances, spontaneous monologues | `{HC\|PD}_{TASKCODE}_{ID}.wav` — `TASKCODE` is either a vowel+rep code (`A1`/`A2`/`A3`, `E1`–`E3`, `I1`–`I3`, `O1`–`O3`, `U1`–`U3`) or a word/phrase task name (`PATAKA`, `PAN_VINO`, `CARMEN`, `BARBAS`, `BURRO`, `CALLE`, `DIABLO`, `GANGA`, `MANGA`, `PATATA_BLANDA`, `PERRO`, `PETACA_BLANCA`, `PIDIO`, `SOMBRA`, `TOMAS`, `ABLANDADA`, `ACAMPADA`, `FREE` for monologue); `ID` is a zero-padded numeric subject/recording ID | Folders: `audio_features` (10 MDVP-style features: Jitter, RAP, PPQ, Shimmer, APQ, NNE, HNR, GNE, etc.), `audios` (raw audio), `grbas` (perceptual GRBAS voice quality ratings, one CSV per task e.g. `Pan_Vino.csv`, `O1.csv`), `metadata` (`metadata_pd.csv` / `metadata_hc.csv`, 23 columns: ID, cohort, 10 clinical columns, ..., audio file path), `transcriptions` (paired `.wav` + `.txt` per utterance); recently released, not yet oversaturated; largest usable N — likely primary training set |
| [MDVR-KCL](https://zenodo.org/records/2867216) | 2017 | English PD vs HC dataset; severity labeled by human annotators using the Hoehn & Yahr (H&Y) clinical staging scale | 37 participants (16 PD, 21 HC); 73 total recordings — 37 ReadText (16 PD, 21 HC) + 36 SpontaneousDialogue (15 PD, 21 HC) | (1) Read aloud "The North Wind and the Sun"; (2) read aloud "Tech. Engin. Computer applications in geography" snippet, depending on participant's constitution; (3) spontaneous dialogue — test executor asks random questions about places of interest, local traffic, or personal interests | `ID##_{hc\|pd}_{H&Y stage}_{score}_{score}.wav` — e.g. `ID18_pd_4_3_3.wav`; all HC files end in `_0_0_0`; PD files encode H&Y stage (2–4 observed) + two additional clinical scores directly in the filename | Only dataset with both scripted and spontaneous speech — key for task-generalization testing; H&Y severity + extra scores are embedded in filenames, so ground-truth labels don't require a separate lookup table; one PD participant (ID18) is missing from SpontaneousDialogue |

<!-- | Name | Source | Description | -->
<!-- |------|--------|-------------| -->

## Tools & Libraries

<!-- | Name | Purpose | Link | -->
<!-- |------|---------|------| -->

## Useful Links

<!-- - [name](url) — description -->

## Appendix: SVD Pathology Term Translations (German → English)

| German | English |
|--------|---------|
| Funktionelle | Functional (voice disorder) |
| Hyperfunktionelle | Hyperfunctional (overuse-related voice disorder) |
| Hypofunktionelle | Hypofunctional (underuse-related voice disorder) |
| Hypotone | Hypotonic (weak/low muscle tone voice) |
| Dysplastische | Dysplastic (abnormal tissue growth) |
| Juvenile | Juvenile (childhood-onset) |
| Psychogene | Psychogenic (psychologically caused) |
| Spasmodische (Dysphonie) | Spasmodic dysphonia |
| Rekurrensparese | Recurrent laryngeal nerve palsy (vocal cord paralysis) |
| Laryngitis | Laryngitis |
| Amyotrophe Lateralsklerose | Amyotrophic lateral sclerosis (ALS) |
| Morbus Parkinson | Parkinson's disease |
| Bulbärparalyse | Bulbar palsy |
| Stimmlippenkarzinom | Vocal cord carcinoma (cancer) |
| Kehlkopftumor | Laryngeal (throat) tumor |
| Chordektomie | Chordectomy (surgical vocal cord removal) |
| Papillom | Papilloma (benign wart-like growth) |
| Fibrom | Fibroma (benign fibrous growth) |
| Balbuties | Stuttering |
| Poltersyndrom | Cluttering (rapid, disorganized speech) |
| Sigmatismus | Sigmatismus (lisping / "s"-sound speech defect) |
| Orofaciale Dyspraxie | Orofacial dyspraxia (motor planning disorder affecting mouth/face) |
| Dysarthrophonie | Dysarthrophonia (combined dysarthria + dysphonia) |
| Dysodie | Dysodia (impaired singing voice) |
| Diplophonie | Diplophonia (perception of two simultaneous pitches) |
| Rhinophonie (variants) | Rhinophonia (nasal-sounding voice; open/closed variants) |
| Kontaktpachydermie | Contact pachydermia (thickened tissue from vocal cord contact) |
| Reinke Ödem | Reinke's edema (swelling of vocal cords, often smoking-related) |
| Gesangsstimme | Singing voice |
| Sängerstimme | Singer's voice |
