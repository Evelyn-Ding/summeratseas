# Week 7 — 7/20–7/26

---

## Monday, 7/20
- *similar pipeline/workflow to [TORGO jupyter notebook](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_analysis.ipynb)

  1. display first few cols of csv
  2. check the shape and print out rows + cols, verify this against what you expected
  3. visualize feature distributions, pca
  4. train a random forest model and plot confusion matrix, and the top 20 features

- feature extraction (1) eGeMAPS features - required separate [script](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/extract_egemaps_features_free.py), run separately in the terminal to generate:
  - summary csv [here](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_free_egemaps_summary.csv)
  - extracted features (corr to each audio, makes up an entire folder) [here](https://github.com/Evelyn-Ding/summeratseas/tree/main/week-07/neurovoz_free_csvs) - this time I COULD put them in the github repo instead of hiding in gitignore (like for TORGO) bc only 76 of them total -> 76 rows (df.shape[0] or len returns # of rows w/o counting title) 
- -> egemaps -> train RF classifier -> results analysis [neurovoz_free_egemaps_features.ipynb](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_free_egemaps_features.ipynb).
- *insert write up on analysis on results* 

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
- IRB trainings -> document the training process -> finish by wknd
---

## Week Summary

**What I did:**
- 
- (ARNI) papers read:
- huntington's disease
- annotations project report

**Questions:**
- 

**Plan for next week:**


- thai's rec'd paper [attention is all you need](https://arxiv.org/pdf/1703.01365) -> SHAP try to fix dependencies and properly implement it; look for multimodal dataset and update arni group next wk
