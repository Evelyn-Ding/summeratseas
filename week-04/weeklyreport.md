# Week 4 — 6/29–7/5

---

## Monday, 6/29
- After getting familiar with how to use the [openSMILE toolkit](https://audeering.github.io/opensmile/get-started.html#obtaining-and-installing-opensmile), I was ready to start extracting features! Last week, I followed the documentation to extract features like energy and chroma. For this project, the most relevant features belong to the set of 88 features called [eGeMAPS](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/gemapsconvention_acousticfeatures.pdf). I wrote a [script](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/extract_egemaps_features_all.py) that cycles through all 8,000+ audio files inside the TORGO dataset and runs the egemaps/v02/eGeMAPSv02.conf config from openSMILE, successfully generating a csv for each file that contains the extracted eGeMAPS features.
- I compiled the csvs into the [torgo egemaps summary csv](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_egemaps_summary.csv). The csv has around 8,000 rows (representing audio files) and 88 columns (reprenting eGeMAPS features).

## Tuesday, 6/30
- The next step is creating visualizations for the extracted eGeMAPS features from the TORGO data. I set up Jupyter Notebook with the libraries: matplotlib, seaborn, scikit-learn. My code and results are linked [here](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_analysis.ipynb)!
- Step (1) was to check if the csv file was read in successfully. The rows represent audio files and the columns represent eGeMAPS features.
- Step (2) was to see if the output matched my expectations. I wanted to make sure the csv had the correct dimensions, which it did. I also looked at the data distribution - slightly imbalanced by a 2:1 ratio, with more control than dysarthic labels. I confirmed that there were 0 missing values.
- Step (3) was to generate the feature distributions! I plotted histograms for four features: average pitch, average loudness, jitter, and harmonics to noise ratio. Then I checked to see if the feature graphs aligned with my intuition - some of them didn't (like for loudness)! My next step is to directly listen to some audio samples to see what dysarthria sounds like at different stages, and try to understand why the graphs differ from what I expected.
- I presented these findings in our Tuesday meeting :) During the meeting, we also discussed the Bridge2AI form and identified who we could reach out to for the Authorized Institutional Official signature. We also finalized the list of people for the approved recipients list. 

## Wednesday, 7/1
- Summer@SEAS Meeting on Library Resources
- I updated the proposal for the Bridge2AI-Voice dataset to reflect the most updated direction for the project:
> **Investigating Vocal Biomarkers for Health Assessment:** This project investigates whether interpretable models trained on acoustic features in voice recordings can be used to detect various health conditions. Specifically, we aim to (1) identify acoustic features that could act as vocal biomarkers for various health disorders, and (2) evaluate the performance of models at detecting health disorders and providing clinically interpretable feedback. We plan on using the Bridge2AI-Voice dataset to analyze voice recordings collected from patients with a wide range of disorders. We will extract feature sets (e.g., GeMAPS) and train interpretable feature-based classifiers. We will also train deep learning neural networks on both handcrafted features and self-supervised learning (SSL) embeddings, and we will use post hoc explanation techniques (e.g., SHAP) to explore model interpretability. All data processing and model training will be conducted in a secure environment, minimizing any risks to patient privacy. The expected duration of this project is two years.
- We finalized the Data Transfer and Use Agreement for the Bridge2AI-Voice dataset and sent it off to the Columbia contracts team for signatures! Once we have all the signatures, Dr. Hisrchberg will submit our forms to request access to the dataset through Synapse.

## Thursday, 7/2
- While we wait for the approval process for the Bridge2AI-Voice dataset, we are looking for other interesting datasets to explore.
  - *Dementia:* DementiaBank (Pitt).
  - *Parkinson's Disease:* Mobile Device Voice Recordings recorded by King’s College London (MDVR-KCL), NeuroVoz: a Castillian Spanish corpus of parkinsonian speech.
  - *Other conditions:* TalkBank, Speech Accessibility Project, Zenodo.
- I got approved for access to the Linguistic Data Consortium (LDC)! After browsing through some datasets, I also looked through recent papers published by members of the LDC. I have linked some interesting papers I read from a researcher who has done a lot of work on training ML models to analyze acoustic features through tools like [OpenSMILE and Praat](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/Opensmile_Praat_Librosa_Comparison_Schizophrenia.pdf) and detect disorders like [Schizophrenia](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/Prosody_schizophrenia.pdf) or [Alzheimer's Disease / dementia](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/Acoustic_features_Alzheimers_Disease.pdf). They even combined [speech data with text-based approaches](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/Combining_acoustic_and_linguistic_features_for_AD_Dementia.pdf).
## Friday, 7/3
- I attended the ARNI meeting and got to share what I was working on!
- I am learning a lot by exploring how to apply various feature extraction and machine learning techniques to the TORGO dataset.
  -  First, I listened to some audio files and noticed patterns in people with dysarthria versus people who are in the control group.
  - Then, I explored features using Principal Component Analysis (PCA), which effectively compresses all 88 eGeMAPS features into 2 numbers that capture the variance in the data. Through this visualization, you can actually see and judge whether or not distinct clusters form for dysarthic versus control group patients!
  - Finally, I trained a simple speech classifier to perform classification of dysarthria. I chose Random Forest because it is an interpretable feature-based model, and the algorithm allows you to rank the features by importance in terms of their significance in the final predictions.
- All of my results are explained [here](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_analysis.ipynb).

---

## Week Summary

**What I did:**
- I explored the [TORGO dataset](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/TORGO%20Webpage%20Info.pdf), which contains data for dysarthria (a vocal disorder). It includes 8,000+ audio files plus tongue movement data (not being used for now), with total size under 1GB.
- After extracting acoustic features from the data, I created visualizations to interpret these features, such as histograms and PCA graphs. Then, I trained the Random Forest classifier to predict dysarthria with 99% accuracy! In addition, I performed analysis on feature importance rankings, which may shed light on which features are the most important indicators of dysarthria in a quantifiable way. 
- I found new datasets we could look into, including conditions like Alzheimer's, Parkinson's, and more. I have downloaded data for MDVR-KCL and requested access to NeuroVoz. I also got access to the LDC and read some papers from their authors.
- For the Bridge2AI-Voice dataset, we are now in the stage of waiting on signatures and approval!

**Questions:**
- My model initially reached 99% accuracy, although this number may be skewed high due to data leakage (i.e. the model is teaching itself a shortcut of what the speakers *with dysarthria* sound like, rather than what dysarthria sounds like). As Yu-Wen suggested, I will split the training and test data so that speakers are isolated. I am curious to see how that affects the accuracy!

**Plan for next week:**
- Read about [SHAP](https://shap.readthedocs.io/en/latest/) and [LIME](https://interpret.ml/docs/lime.html) from the API documentations. I will practice implementing them on the TORGO dataset. Once I have a solid grasp of these techniques, I will be able to apply them to future work on the Bridge2AI-Voice and other datasets.


