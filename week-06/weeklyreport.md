# Week 6 — 7/13–7/19

---

## Monday, 7/13
- I emailed the IRB, requesting a consultation for our Bridge2AI-Voice Dataset application. The IRB replied that a protocol needs to be submitted for IRB review. I will start the IRB process, completing the training and filling out forms through the Rascal platform.
- After obtaining access to three Parkinson's datasets (SVD, Neurovoz, MVDR-KCL), I am currently focusing on Parkinson's detection using vocal biomarkers. To understand what kind of research has been done in this area, I read several papers by the same author:
  - In particular, the paper on [Parkinson's disease detection from speech across three languages (Spanish, German, Czech)](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/Parkinsons_across_three_languages.pdf) really stood out to me. I also happen to be exploring three PD datasets in different languages (German, Spanish, English), although my datasets differ from theirs. Specifically, they used datasets in [Spanish](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/PD_Spanish_Dataset.pdf), [German](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/PD_German_Dataset.pdf), and [Czech](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/PD_Czech_Dataset.pdf) that are not publicly accessible (except for the Spanish one, which is called PC-GITA). The same questions of cross-language generalizability are present in both of our research though.
  - I also found an interesting link between dysarthria and Parkinson's disease from reading [this paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/PD%20and%20Dysarthria%20Link.pdf), which explains that PD causes extreme slowness of movement that affects a patient's vocal tract and thus speech. The paper states that "The main symptoms of the impaired speech of PD patients include reduced loudness, monopitch, monoloudness, hypotonicity, breathy, hoarse voice quality, and imprecise articulation. These symptoms are typically grouped and called *hypokinetic dysarthria*." This helps connect my previous work on exploring the TORGO (dysarthria) dataset to my current focus on PD, as my analysis on which features are important to detecting dysarthria and the techniques I used to extract those features can be cross-applied.
## Tuesday, 7/14
- I read Yu-Wen's paper on an ALM-based voice concept bottleneck framework. The goal of model interpretability is really important in medical contexts, as you want a model's predictions to be understood by clinicians and patients. I spent some time reading about the ideas in the paper to gain a deeper understanding of how I could achieve model interpretability in my research project. Currently, there are three main approaches:
  - (1) Self-Supervised Learning (SSL) embeddings: Black box models, Generating complex numbers, Can only achieve interpretability using post-hoc interpretability methods that fit explainable features over them (LIME, SHAP)
  - (2) Feature Extraction using openSMILE toolkit: Uses a standard set of 88 features (eGeMAPS), Low-level descriptors (Some are human interpretable: jitter, shimmer, harmonics to noise ratio. Some are less interpretable: MFCCs)
  - (3) Concept Bottleneck Framework using Audio Language Model (ALM): High-level descriptors (Clinical Voice Quality: breathiness, roughness, loudness. Speech Behavior: slow speech tempo, low intensity, reduced prosodic expression)
- I listed these in order of least to most interpretable. The idea is that with the concept bottleneck framework, you have high-level concepts that are very understandable by humans. You come up with a list of these concepts, plug them into the model prompt, and force the model to predict scores each of these concepts that influence its final decision. The concept bottleneck framework, when combined with ALM, goes one step beyond the approach in the original [concept bottleneck framework paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/concept%20bottleneck%20models.pdf). By using adaptable concepts rather than predefined concept sets, the ALM adds much more flexibility. You still have to decide which concepts matter, but you can simply update the prompt to reflect a new set of concepts, without having to change any underlying architecture (like the number of neurons in certain layers).

## Wednesday, 7/15
- listen to audio files, summarize content, and copy over datasets to speechlab serveer (~70k)
## Thursday, 7/16
- MATLAB -> idea to train a simple speech classifier with a click of a button !
## Friday, 7/17
- discuss ARNI project
- huntington's (hyper vs hypo) (hypo- prefix indicating that the speech is slower and quieter in nature)
---

## Week Summary

**What I did:**
- listened to dataset audio files
- copied over to speechlab server
- direction of project

- The high-level concepts are more interpretable than the low-level features used in the feature extraction approach because most people wouldn't know how to interpret their jitter score, much less a MFCC. 
- However, I hypothesize that these approaches may also be listed in order from most to least accurate, due to the expected trade-off between interpretability and accuracy. 

**Questions:**
- how to best clean messy datasets
- how would b2ai dataset come in - how is it related to huntington's disease

**Plan for next week:**
- i have a lot of ideas!!
  - train simple speech classifier
3 ideas in parallel now:
(1) keep working on TORGO - b/c directly relevant to PD
- severity based scores vs binary classification
- SHAP vs LIME
(2) ARNI [mentalbert paper] - interpretability -> same methodlogy but applied to speech instead of text: feature extraction (eGeMAPS instead of LIWCS), SHAP, k-means clustering
(3) 
START WORKING ON DATASET (spanish → identify spontaneous speech OR english spontaneous speech → clean it first using voice activity detection models)

*start IRB application process for Bridge2AI-Voice dataset
