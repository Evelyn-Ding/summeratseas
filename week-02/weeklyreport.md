# Week 2 — 6/15–6/21

---

## Monday, 6/15
- I went back to [Sara's literature review paper](../week-01/Mental_Health_Dataset_and_Resources_Review_speechweb.pdf) and the accompanying [website](https://ziweig.github.io/mental-health-datasets-resources-review/) to figure out which datasets are most relevant to the direction of my project. First, I used the website's sorting tool to filter the [spreadsheet](./sara_mentalhealthdatasetspaper_spreadsheet.csv) for datasets that were speech audio (because we are trying to examine acoustic signals directly from the raw audio, and this information would be lost in a text transcript or extracted textual features); clinical interview data; publicly available.
- Unfortunately, there is a trade-off between having abundant publicly available data and clinically accurate data. Many of the studies with clinician-verified data are small-scale, interview-based, and keep their data protected, in contrast to the large open-source data scraped from social media platforms that rely on self-diagnosis labels (which are less accurate).
- Based on the findings of Sara's paper, I also considered whether it's worth exploring if the data is a single snapshot or collected longitudinally (so we could measure the progression of the disease), severity based annotations (shows progression of disease over time, with nuance) rather than binary classifications (black-and-white), and comorbidities in mental health disorders (which is commonly glossed over and ignored). 
- Overall, I noticed that the primary mental health disorders that fit my criteria (speech data; publicily available; clinically acucrate) were schizophrenia/bipolar and depression/MDD. I generated this [brief report](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/publicspeechdata.md) where I went through Section 2. For each disorder, I looked at the references to see if the dataset (either proposed/given by the paper or used/accessed by the authors) was publicly available. I found the most potential in the dementia/Alzheimer's datasets.

## Tuesday, 6/16
- We had our first in person meeting! This was also my first day seeing the new lab space in person :)
- Meeting notes [here](https://docs.google.com/document/d/1sG3M2QBKsiHNJ0RDA9XdGqiWv_AwBW7fA1HkksWMjiQ/edit?tab=t.0#heading=h.13b7f5t5mgpx). Parmida presented on her findings for her reserach (we listened to a couple audio files to see the impact of RE-USE on voice quality, which was really interesting!), and we discussed ways that I could build off the work. One idea is that if voice quality labels are preserved (as opposed to masking depressive features with changed labels) after denoising, then I could take the de-noised audio file and perform the mental health disorder detection on it.
- For my project, the focus is on obtaining access to datasets with speech audio. The (paper)[https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/2022EMNLP_2025CLPsych_bipolarschizophreniadata.pdf] I found with publicly available for schiphrenia/bipolar had features that were text-focused rather than multimodal. Furthermore, the depression datasets should not be the primary area of interest since there is previous lab work done on that.
- We could pivot to looking at diseases that change how a person speaks (e.g., Parkinson's, Alzheimer's/dementia, dysarthria). For now, the goal is to find a dataset with raw audio and clear clinical labels (Bridge2AI, DAIC-WOZ), and narrow down on which disorders to explore afterward.

## Wednesday, 6/17
## Thursday, 6/18

## Friday, 6/19

---

## Week Summary

**What I did:**
- I got approved for the DAIC-Woz dataset!
- Bridge2AI application

**Questions:**
- what KINDS of linguistic markers to look at? dif measures of VQ depending on the paper you read
- do we want to focus on severity-based datasets (as suggested by sara’s paper)? or can we look at binary classification (more data available) but focus on making the results more interpretable?
- 

**Plan for next week:**
- I will revise the application for the Bridge2AI-Voice dataset (for both adult and pediatric)
