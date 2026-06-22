# Week 2 — 6/15–6/21

---

## Monday, 6/15
- I went back to [Sara's literature review paper](../week-01/Mental_Health_Dataset_and_Resources_Review_speechweb.pdf) and the accompanying [website](https://ziweig.github.io/mental-health-datasets-resources-review/) to figure out which datasets are most relevant to the direction of my project. First, I used the website's sorting tool to filter the [spreadsheet](./sara_mentalhealthdatasetspaper_spreadsheet.csv) for datasets that were speech audio (because we are trying to examine acoustic signals directly from the raw audio, and this information would be lost in a text transcript or extracted textual features); clinical interview data; publicly available.
- Unfortunately, there is a trade-off between having abundant publicly available data and clinically accurate data. Many of the studies with clinician-verified data are small-scale, interview-based, and keep their data protected, in contrast to the large open-source data scraped from social media platforms that rely on self-diagnosis labels (which are less accurate).
- Based on the findings of Sara's paper, I also considered whether it's worth exploring if the data is a single snapshot or collected longitudinally (so we could measure the progression of the disease), severity based annotations (shows progression of disease over time, with nuance) rather than binary classifications (black-and-white), and comorbidities in mental health disorders (which is commonly glossed over and ignored). 
- Overall, I noticed that the primary mental health disorders that fit my criteria (speech data; publicly available; clinically accurate) were schizophrenia/bipolar and depression/MDD. I generated this [brief report](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/publicspeechdata.md) where I went through Section 2. For each disorder, I looked at the references to see if the dataset (either proposed/given by the paper or used/accessed by the authors) was publicly available. I found the most potential in the dementia/Alzheimer's datasets.

## Tuesday, 6/16
- We had our first in person meeting! This was also my first day seeing the new lab space in person :)
- Meeting notes [here](https://docs.google.com/document/d/1sG3M2QBKsiHNJ0RDA9XdGqiWv_AwBW7fA1HkksWMjiQ/edit?tab=t.0#heading=h.13b7f5t5mgpx). Parmida presented her findings for her research (we listened to a couple audio files to see the impact of RE-USE on voice quality, which was really interesting!), and we discussed ways that I could build off the work. One idea is that if voice quality labels are preserved (as opposed to masking depressive features with changed labels) after denoising, then I could take the de-noised audio file and perform the mental health disorder detection on it.
- For my project, the focus is on obtaining access to datasets with speech audio. The [paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/2022EMNLP_2025CLPsych_bipolarschizophreniadata.pdf) I found with publicly available data for schizophrenia/bipolar had features that were text-focused rather than multimodal. Furthermore, the depression datasets should not be the primary area of interest since there is previous lab work done on that.
- We could pivot to looking at diseases that change how a person speaks (e.g., Parkinson's, Alzheimer's/dementia, dysarthria). For now, the goal is to find a dataset with raw audio and clear clinical labels (Bridge2AI, DAIC-WOZ), and narrow down on which disorders to explore afterward.

## Wednesday, 6/17
- I downloaded the forms for requesting data for the Bridge2AI [adult dataset](https://physionet.org/content/b2ai-voice/3.1.0/) and [pediatric dataset](https://physionet.org/content/b2ai-voice-pediatric/1.1.0/). I successfully submitted a request to access the data with extracted features. However, to access the raw audio, I need to submit a separate application that requires signed forms and a research project description! I am tracking the status of my application in this [file](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/bridge2aidata.md).
- I scoured all 10+ datasets surveyed in the [Briganti depression voice quality paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-01/voicequality_biomarker_depression.pdf) and realized that all of them are basically private (e.g. [Mazur 2025](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/mazur2025evaluation.pdf).

## Thursday, 6/18
- I spent time on the research project description for the Bridge2AI forms. My [draft](https://docs.google.com/document/d/1xehvai0ZYgLnObimR-gl5rFZ1AvwvIVjh7qNh_dXwwU/edit?tab=t.0) ended up being about 650 words.
- I met with Parmida about the proposal draft.
- We identified two main directions that I could take this project:
  1. build a framework that maps disorders to acoustic features (useful as an evaluation benchmark for other models) for a wide variety of disorders (broaden the scope)
  2. build a new interpretable diagnostic model for specific disorders where acoustic features seem particularly relevant (narrow the scope).
- What kind of acoustic features to look at?
  1. Voice Quality (VQ) labels — categorical labels (pitch, texture, volume, clarity, rhythm) to describe voice, kind of like personality descriptors (e.g. soft, singsong, nasally).
  2. Acoustic features — quantifiable signal properties, standard GeMAPS features (e.g. jitter, shimmer); extractable via openSMILE or Praat software.
- Leave a note in the proposal that we are using models that are trained locally so the data does not face privacy risks.
- One key issue is model interpretability and how even if we ask the model to *explain* its reasoning, that is different from it being *interpretable* (which would require something like an open architecture with transparent weights, stress testing black-box model, etc.).

## Friday, 6/19
- I learned more about model interpretability, which I think is an important concept for me to understand going forward. The papers I read are [Rudin 2019 black box](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/rudin2019blackbox.pdf), [Kerz 2023 explainable AI in mental health](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/kerz2023explainableAImentalhealth.pdf), and [Ebraheem 2025 interpretable AI for voice/speech](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/ebraheem2025iexplainableAIvoice_bridge2a.pdf) (same authors of Bridge2AI dataset!).
- There is a distinction between making the model inherently interpretable which require models with simple designs (e.g. decision tree, linear/logistic regression on GeMAPS features) and post-hoc explainability (e.g. LIME — local linear approximation, SHAP — feature contribution scores, gradient attribution/saliency — input sensitivity, probing — what does layer X encode?).
- There is also an important trade-off between accuracy and interpretability in models. Usually models that use technically complex algorithms instead of human-crafted features perform better, despite being less interpretable. Accuracy and interpretability are both incredibly important for models in healthcare.
- I finished a draft of the Bridge2AI application and also got approved for the DAIC-Woz dataset!
---

## Week Summary

**What I did:**
- My goal is to identify and obtain access to datasets with raw audio and clear clinical labels. I did a deep dive into Sara's paper to guide me on which direction to look for datasets (in terms of the dataset design and task formulation, as well as the mental health disorders covered).
- I completed applications to access the Daic-Woz dataset and Bridge2AI data.
- For the Bridge2AI data application, I drafted a research project description, thinking through many different ideas for which direction to take the project this summer.

**Questions:**
- What kinds of linguistic markers do we look at? There are measures of voice quality depending on the paper you read (two main categories listed above in notes from Thursday's meeting)
- Do we want to focus on severity-based datasets (as suggested by Sara’s paper)? Or can we look at binary classification (because there's more data available) but focus on making the results more interpretable?

**Plan for next week:**
- Based on Yu-Wen's feedback, I will revise the application for the Bridge2AI-Voice dataset (for both adult and pediatric) and submit it!
- Since I got approved for the DAIC-Woz dataset, I can start listening to the files, which consist of interview recordings and transcripts, to see if there are any interesting ideas to explore :)





