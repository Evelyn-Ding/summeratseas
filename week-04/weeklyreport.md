# Week 4 — 6/29–7/5

---

## Monday, 6/29
- After getting familiar with how to use the [openSMILE toolkit](https://audeering.github.io/opensmile/get-started.html#obtaining-and-installing-opensmile), I was ready to start extracting features! Last week, I followed the documentation to extract features like energy and chroma. For this project, the most relevant features belong to the set of 88 features called [eGeMAPS](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/gemapsconvention_acousticfeatures.pdf). I wrote a [script](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/extract_egemaps_features_all.py) that cycles through all 8,000+ audio files inside the TORGO dataset and runs the egemaps/v02/eGeMAPSv02.conf config from openSMILE, successfully generating a csv for each file that contains the extracted eGeMAPS features.
- I compiled the csvs into the [torgo egemaps summary csv](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_egemaps_summary.csv). The csv has around 8,000 rows (representing audio files) and 88 columns (reprenting eGeMAPS features).

## Tuesday, 6/30
- visualizations
- install jupyter matplotlib seaborn scikit-learn
- https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_analysis.ipynb
- explain steps 1, 2, and 3

## Wednesday, 7/1
- b2ai proposal
- hand-crafted features vs SSL embeddings 
## Thursday, 7/2
- ldc access; new datasets found!
## Friday, 7/3
- TORGO
- listen to audio
- explore features more!
- train a simple speech classifier!!
- learn about + try implementing SHAP and LIME!!!

  
---

## Week Summary

**What I did:**
- Reminder: What is in the TORGO dataset? -> What kind of data was collected? (read here: https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/TORGO%20Webpage%20Info.pdf)

**Questions:**
- 

**Plan for next week:**
- 

Summary for now (from bridge2AI proposal):
**Investigating Vocal Biomarkers for Health Assessment:** This project investigates whether interpretable models trained on acoustic features in voice recordings can be used to detect various health conditions. Specifically, we aim to (1) identify acoustic features that could act as vocal biomarkers for various health disorders, and (2) evaluate the performance of models at detecting health disorders and providing clinically interpretable feedback. We plan on using the Bridge2AI-Voice dataset to analyze voice recordings collected from patients with a wide range of disorders. We will extract feature sets (e.g., GeMAPS) and train interpretable feature-based classifiers. We will also train deep learning neural networks on both handcrafted features and self-supervised learning (SSL) embeddings, and we will use post hoc explanation techniques (e.g., SHAP) to explore model interpretability. All data processing and model training will be conducted in a secure environment, minimizing any risks to patient privacy. The expected duration of this project is two years.
