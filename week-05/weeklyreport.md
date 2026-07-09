# Week 5 — 7/6–7/12

---

## Monday, 7/6
- I performed addition analysis to the TORGO (dysarthria) dataset, adding my code and findings to [Jupyter Notebook](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_analysis.ipynb). Last week, after extracting the eGeMAPS features from the TORGO dataset and visualizing the feature distributions, I trained a Random Forest model to perform binary classification of samples as dysarthria or control.
- While the model achieved a 99% accuracy, this number was inflated due to the issue of data leakage — the model learned to recognize the *speaker*, not *dysarthria*. To fix this, I split the training and testing data by speaker. I selected my test speakers: F03, M02 (dysarthric) + FC03, MC02 (control). Train speakers: all remaining 11 speakers. -> severity balanced AND gender balanced!!
```
- Dysarthric (8): F01, F03, F04, M01, M02, M03, M04, M05 (8 total: 3 female, 5 male)
- Control (7): FC01, FC02, FC03, MC01, MC02, MC03, MC04 (7 total: 3 female, 4 male)
```
- After training the Random Forest with the fixed train/test split, the model had a 73% accuracy rate. This lower accuracy rate is a more honest reflection of the model's performance. While the accuracy decreased, it's important to fix the data leakage issue because we want the model to be actually learning the signs of dysarthria without taking shortcuts; it should be able to generalize to new voices it hasn't heard before, which is what a real clinical tool would need to do.
- SHAP vs LIME reading
- 3 datasets summary + analysis - see md file
- future: TORGO severity annotations - if they exist? severity_level mapping
```
severity_level = {
    "F03": 1,
    "F04": 1,
    "M03": 1,
    "F01": 2,
    "M05": 2,
    "M01": 3,
    "M02": 3,
    "M04": 3,
}
//control group is 0
```
## Tuesday, 7/7
- meeting
- summarize content of slides here -> from meeting notes
- parmida slides -> Voice Quality 1:1 mapping idea
## Wednesday, 7/8
- Summer@SEAS Meeting on Innovation, Design, & Entrepreneurship (IDE)
- The Columbia Engineering social media reached out, asking me to share my summer research experience, so I filled out the form for that!
- Read paper about applicability of SHAP / LIME for audio data
## Thursday, 7/9
- look into datasets (NEW)
## Friday, 7/10
SHAP libraries didn't work oop - try again to see per-prediction feature importances ?

---

## Week Summary

**What I did:**
- 

**Questions:**
- 

**Plan for next week:**
- 
