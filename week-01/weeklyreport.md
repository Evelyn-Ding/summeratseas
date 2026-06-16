# Week 1 — 6/8–6/14

---

## Monday, 6/8
- I read and annotated a [literature review on mental health datasets](./Mental_Health_Dataset_and_Resources_Review_speechweb.pdf) for any potential datasets that would be relevant for my project. I also noted which disorders have the most potential for being detected through acoustic features in speech (such as depression), paying particular attention to disorders that could be related to pronunciation specifically.
## Tuesday, 6/9
- Yu-Wen, Parmida, and I had our first meeting! Meeting notes linked [here](https://docs.google.com/document/d/1sG3M2QBKsiHNJ0RDA9XdGqiWv_AwBW7fA1HkksWMjiQ/edit?tab=t.0). We discussed Project 1: Voice-Quality-Aware Audio Enhancement (Parmida) and Project 2: Medical Speech / Pronunciation for Disease Detection (Evelyn).
- I set up this github repo and figured out the structure for how I want to document my research this summer. There will be weekly folders with papers I read and code that I worked on, as well as an overall progress report for the week.
## Wednesday, 6/10
- Summer@SEAS Orientation
- The program has weekly meetings on Wednesday from 12:30-2pm.
## Thursday, 6/11
- Parmida and I had a meeting where we had a more in-depth discussion on my automatic pronunciation assessment project that I worked on during the school year. Then we talked about her work on denoising and voice quality and I asked questions about some really cool concepts from the paper, like how the data is synthetically overlapped, the target-absent problem when the model is supposed to output silence but fails to do so, and enrollment clips which are given to the model so it knows what the target speaker is supposed to sound like. Meeting notes linked [here](https://docs.google.com/document/d/1Ck0IveANDh7lTpOJTzxSc6t_qOwUIrXAt2ZvtHgcOHM/edit?tab=t.0#heading=h.aji1stbje3r2).
## Friday, 6/12
- I was really interested in exploring Voice Quality (VQ)! I felt like it could be a promising area to explore for the intersection between my work and Parmida's work. This is because I'm trying to develop interpretable models for detecting disorders from speech signals, and Parmida's paper noted that patients with depression were more likely to have VQ labels like soft, hesitant, and stammering; this was relevant to her work because she noticed the RE-USE model was altering VQ labels and changing them from depressed to confident (e.g. authoritative, singsong, loud).
- I read papers on VQ to understand it better. I realized that a common set of 25 labels across 5 categories (Pitch, Texture, Volume, Clarity, Rhythm) was first identified by the [Paraspeechcaps dataset](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-01/paraspeechcaps_dataset.pdf). The creators of the [VoxProfile](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-01/voxprofile.pdf) benchmark used these VQ labels for their benchmark, and they released a whisper large model that was fine-tuned to these VQ labels.
- I requested access to datasets that are relevant for my project.
  - DAIC-WOZ & extended (depression / clinical voice data) - requested from USC
  - bridge2AI voice pediatric (Yu-Wen recommended this one) - requested via Physionet and emailed authors for raw audio 
  - <https://www.ldc.upenn.edu/> (recommended by Parmida - this is where the DIHARD dataset came from, which is speaker diarization in real settings)

---

## Week Summary

**What I did:**
- This week, I read papers to understand the field of medical speech / pronunciation and brainstorm ideas for my project.
- After some discussion about the direction of my project, this is my current direction: instead of making model do a binary classification, use intermediate model to predict voice quality of waveform (e.g. high pitch, timbre) → use these features to make a prediction for depression or no depression → that way the final prediction is more explainable

**Questions:**
- Which datasets does VoxProfile use? It gets voice quality metrics from ParaSpeechCorps but seems to be tested on the VCTK and MSP-Podcast datasets.
- What is the difference between the voice quality biomarkers used in the [Briganti paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-01/voicequality_biomarker_depression.pdf) (e.g. prosody (frequency, speech rate, voice intensity), spectral features (MFCCs and spectral jilt), voice pertubation (jitter and shimmer), pause duration, harmonic-to-noise ratio) and the voice quality labels used in [VoxProfile](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-01/voxprofile.pdf) (e.g. shrill, silky, booming, crisp, singsong)?

**Plan for next week:**
- Narrow the scope of my project by identifying which disorders I can focus on (within the broad realm of mental health disorders) and key datasets. Once I have access to them, I can start analyzing audio signals!
