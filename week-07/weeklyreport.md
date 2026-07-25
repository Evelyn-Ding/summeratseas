# Week 7 — 7/20–7/26

---

## Monday, 7/20
- My goal this week was to fully explore the Parkinson's datasets! After last week's meeting, where we listened to a few audio files from each of the three datasets, we agreed that I should start with the Neurovoz dataset (Spanish).
  - Despite each audio recording being pretty short in length, Neurovoz had the cleanest data and the largest sample size; the MDVR-KCL (English) dataset had noise (i.e. conversations between the moderator and speaker) and the SVD (German) dataset only had data for 1 Parkinson's patient. 
  - When I start working with the MDVR-KCL data, I'll have to remove the noise in the data pre-processing stage, which may a bit involved. While the SVD dataset is too small for a train set, it could be a good way to verify our results on a test sample.
- The first step was feature extraction. I had a couple ideas last week for which set of features to extract: ```(1) eGeMAPS (2) NeuroSpeech (3) MDVP (Multidimensional Voice Program)```.
  - I started with (1) the eGeMAPS features, so I wrote a [script](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/extract_egemaps_features_free.py) that generates a csv for each audio file that contains the values for all 88 eGeMAPS features, stored in this [folder](https://github.com/Evelyn-Ding/summeratseas/tree/main/week-07/neurovoz_free_csvs). There's only 76 files total, whereas TORGO had 8,000+ files (so I had to .gitignore the folder)! After all the audio files have been processed, a [summary csv](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_free_egemaps_summary.csv) is generated, containing the values of extracted features for all the audio files.
- To perform analysis on the Neurovoz dataset, I followed a similar approach to my [TORGO analysis](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_analysis.ipynb), where I wrote code in Jupyter Notebook to do the following:
```
    1. display first few cols of csv
    2. check the shape and print out rows + cols, verify this against what is expected
    3. visualize feature distributions using histograms, pca graphs
    4. train a random forest model, plot confusion matrix and feature importances (top 20 features)
```
- In my [analysis on Neurovoz with eGeMAPS features](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_free_egemaps_features.ipynb), I found that the most important features are related to the rate and rhythm of speech (e.g. mean unvoiced segment length, voiced segment length, voiced segments per second). This makes sense, since Parkinson's patients are known to speak slower, especially in monologue settings where they don't have a script to read off of.
  - I was wondering: if Parkinson's causes a form of dysarthria, and loudness is the most important feature for the TORGO (dysarthria) dataset, then why loudness isn't a very important feature for Parkinson's? This could be because the patients in TORGO had dysarthria caused by cerebral palsy, ALS, or even Huntington's disease, which manifests differently than the kind of hypokinetic dysarthria that Parkinson's causes. Or it could simply be due to the microphone settings for the Neurovoz dataset!

## Tuesday, 7/21
- Meeting
- IRB review process - set up account on rascal platform, category 4 exemption, required personnel + trainings
- another meeting with chengtao dai on annotations !

## Wednesday, 7/22
- Summer@SEAS Final Meeting / Social Event
- (2) Neurospeech / disvoice set of features - read up a lot about the toolkit vs library and their differences
  - reading the neurospeech [paper]() and the disvoice [github](https://github.com/jcvasquezc/disvoice) which also has a lot of its own useful read.me's for each feature type -> wrote this [summary of comparisons btwn the two](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurospeech.md)
- *still working on resolving dependencies -> thursday


## Thursday, 7/23
- (3) [MDVP set of features](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_mdvp_features.ipynb)
- *additionally, i added the same speaker leakage problem i did for torgo. i also generated 4 most important features' histograms as well like i did for the egemaps feature set.

## Friday, 7/24

- look into the parmida's [slides](https://docs.google.com/presentation/d/1oyXigbFfhRBsFg8MrF26cupQdxAif-MA/edit?rtpof=true) -> VQ analysis
  ```
   this is the voxprofile model
   https://huggingface.co/tiantiaf/whisper-large-v3-voice-quality
   parmida should be familiar with it
   maybe you can collaborate with her seeing what features from this model are more accurate or helpful?
  ```
- meeting w/thai - interpretability (SHAP); ML (RF) vs DL (bert, mentalbert, llama -> encoder/decoder ?)
- IRB trainings -> document the training process -> finish by wknd
---

## Week Summary

**What I did:**
- 
- (ARNI) papers read:
- huntington's disease
- annotations project report

**Questions:**
- how does one train a concept bottleneck fw, or an ssl embeddings model?
- how to train multiple dif (ML) classifiers in one jupyter notebook - compare "benchmark" accuracies?
- voice activity detection model on the english dataset ?

**Plan for next week:**


- thai's rec'd paper [attention is all you need](https://arxiv.org/pdf/1703.01365) -> SHAP try to fix dependencies and properly implement it; look for multimodal dataset and update arni group next wk
