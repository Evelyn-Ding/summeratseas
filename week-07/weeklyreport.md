# Week 7 — 7/20–7/26

---

## Monday, 7/20
- Out of the three Parkinson's Disease (PD) datasets to explore, I chose to start with the Neurovoz dataset because it had the cleanest audio and largest sample sizes. The first step of my analysis was feature extraction. There were a couple options for which features to extract: ```(1) eGeMAPS (2) NeuroSpeech (3) MDVP (Multidimensional Voice Program)```.
- I started with (1) the [eGeMAPS](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/gemapsconvention_acousticfeatures.pdf) features, so I wrote a [script](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/extract_egemaps_features_free.py) that generates a csv for each audio file that contains the values for all 88 eGeMAPS features, stored in this [folder](https://github.com/Evelyn-Ding/summeratseas/tree/main/week-07/neurovoz_free_csvs). I directly uploaded the folder because there's only 76 files total, whereas TORGO had 8,000+ files (so I had to .gitignore the folder)! After all the audio files have been processed, a [summary csv](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_free_egemaps_summary.csv) is generated, containing the values of extracted features for all files.
- To perform analysis on the Neurovoz dataset, I followed a similar approach to my [TORGO analysis](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-04/torgo_analysis.ipynb), where I wrote code in Jupyter Notebook to do the following:
```
    1. display first few cols of csv
    2. check the shape and print out rows + cols, verify this against what is expected
    3. visualize feature distributions using histograms, pca graphs
    4. train a random forest model, plot confusion matrix and feature importances (top 20 features)
    *bonus: generate feature distribution histograms for top 4 most important features
```
- In my [analysis on Neurovoz with eGeMAPS features](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_free_egemaps_features.ipynb), I found that the most important features are related to the rate and rhythm of speech (e.g. mean unvoiced segment length, voiced segment length, voiced segments per second). This makes sense, since Parkinson's patients are known to speak slower, especially in monologue settings where they don't have a script to read off of.
  - I was wondering: if Parkinson's causes a form of dysarthria, and loudness is the most important feature for the TORGO (dysarthria) dataset, then why isn't loudness a very important feature for Parkinson's? This could be because the patients in TORGO had dysarthria caused by cerebral palsy, ALS, or even Huntington's disease, which manifests differently than the kind of hypokinetic dysarthria that Parkinson's causes. Or it could simply be due to the microphone settings for the Neurovoz dataset!

## Tuesday, 7/21
- We had our weekly meeting, where I presented my [Week 7 slides](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/Meeting%20%237_%20July%2021%2C%202026.pdf).
- For the IRB review process, I set up an account on the Rascal platform and began filling out the forms. I emailed the IRB team to help clarify my questions about category 4 exemption and required trainings for listed personnel.
- I also had a meeting with Chengtao from the ARNI group on the project for mental health dialogue scoring using LLMs. We discussed the manual annotation part of the project, which I will be helping with!

## Wednesday, 7/22
- Summer@SEAS Meeting — End of Summer Celebration
- I got to work on feature extraction approach (2) [Neurospeech toolkit](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/Neurospeech%20paper%20full%20print.pdf) / [DisVoice library](https://github.com/jcvasquezc/disvoice).
  - I realized that Neurospeech was built for Windows computers (I have a Mac). The good news is that the creator of Neurospeech also released a Python library called DisVoice. What's great is that DisVoice has an even larger feature set than Neurospeech (even though it's missing a couple cool features), with a feature extraction pipeline built for machine learning! I summarized the differences between the two softwares [here](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurospeech.md).
- After installing the Python library, I got stuck on resolving dependency conflicts. Once I am able to get the extracted features for Neurospeech/DisVoice, I'll work on performing the same analysis I did earlier with the eGeMAPS features.

## Thursday, 7/23
- The final set of features I wanted to explore was (3) [MDVP (Multidimensional Voice Program)](https://pubmed.ncbi.nlm.nih.gov/15952683/). This set of features have already been extracted and are directly provided in the Neurovoz dataset in the ```audio_features``` folder; MDVP features are also native to the SVD (German) dataset, which stores its data in .nsp files. Thus, I thought it would be useful to compare the performance of using MDVP features!
- After performing the same [analysis](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_mdvp_features.ipynb) that I did for the other feature sets, I found that the most important features were related to tremor frequency. Then I did the additional step of solving the speaker leakage problem, which I first dealt with when I was working with the TORGO dataset (due to its very limited number of speakers). This lowered the accuracy from around 70% to 55%.

## Friday, 7/24

- I looked into the Parmida's [slides](https://docs.google.com/presentation/d/1oyXigbFfhRBsFg8MrF26cupQdxAif-MA/edit?rtpof=true) on voice quality labels from the VoxProfile benchmark. My goal is identify which VQ features are the most helpful. The underlying VoxProfile model can be found at: https://huggingface.co/tiantiaf/whisper-large-v3-voice-quality. Then, I believe I can directly prompt the ALM on the most useful VQ features, which fall into 5 categories: ```pitch, rhythm, clarity, voice texture, volume```.
- I attended the weekly ARNI meeting. We discussed the mentalBERT project, and how the scope is focused on text-based Reddit (social media) datasets for depression, with potential for expanding the scope to blog posts and clinical interviews and even other modalities + mental health disorders.
- I also had a one-on-one meeting with Thai from the ARNI group to discuss the mentalBERT project, which focuses on text-based mental health analysis—with strong parallels to my speech-based analysis. We talked about the project's focus on interpretability (via methods like SHAP) as well as the differences between Machine Learning (e.g. Random Forest) and Deep Learning (e.g. BERT, Llama) approaches. I plan on reading more about encoder/decoder models to understand the model architectures used in the mentalBERT project!
---

## Week Summary

**What I did:**
- My goal this week was to fully explore the Parkinson's datasets! After last week's meeting, where we listened to a few audio files from each of the three datasets, we agreed that I should start with the Neurovoz dataset (Spanish).
  - Despite having audio recordings that were pretty short in length, Neurovoz had the cleanest data and the largest sample size; the MDVR-KCL (English) dataset had noise (i.e. conversations between the moderator and speaker) and the SVD (German) dataset only had data for 1 Parkinson's patient. 
  - When I start working with the MDVR-KCL data, I'll have to remove the noise in the data pre-processing stage, which may be a bit involved. While the SVD dataset is too small for a train set, it could be a good way to verify our results on a test sample.
- I had a couple ideas for which set of features to extract: ```(1) eGeMAPS (2) NeuroSpeech (3) MDVP (Multidimensional Voice Program)```. The reason why I want to try extracting feature sets is that I plan on comparing the accuracies of the various approaches!
  - (1) eGeMAPS: https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_free_egemaps_features.ipynb
  - (2) NeuroSpeech / DisVoice: https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurospeech_disvoice.md
  - (3) MDVP: https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/neurovoz_mdvp_features.ipynb
- After performing analysis on all three feature sets, I saw that eGeMAPS was the most successful approach. Perhaps it's because there are a larger number of features, or the specific features are better at capturing the voice quality of PD.
- I read the following papers from the ARNI group: [Huntington's Disease vocal biomarkers](https://arxiv.org/pdf/2603.11168v1) (since PD results in hypokinetic dysarthria and HD results in hyperkinetic dysarthria, it could be interesting to explore contrastive learning approach that assumes the features for the two classes are opposites!); Chengtao's project report on LLM-as-a-judge for PsychEval Dialogues.

**Questions:**
- What are the steps for implementing a concept bottleneck framework, or an SSL embeddings model?
- If I train multiple different (ML) classifiers in one Jupyter Notebook, can I directly compare "benchmark" accuracies?
- For the MDVR-KCL English dataset, how can I train a voice activity detection model to trim silence + denoise?

**Plan for next week:**
- Now that I've trained classifiers on three standard feature sets, the next step is to try implementing the concept bottleneck framework. This will generate features that are super interpretable, baked directly into the prompt to the ALM ([Flamingo-Audio from HuggingFace](https://huggingface.co/nvidia/audio-flamingo-next-think-hf), fine tuned on Clinical Voice Quality (CVQ) dimensions). I'll also try implementing an SSL-based model, which generates abstract, uninterpretable features that may result in a higher accuracy. This method will use a feature extraction approach built on VoxProfile (which produces 25 voice quality labels), using the [Whisper large v3 VQ model](https://huggingface.co/openai/whisper-large-v3) as the backbone.
- For the ARNI project, Thai recommended that I read the paper [Attention is all you need](https://arxiv.org/pdf/1703.01365) to better understand encoder/decoder models (& classification heads). I'm also eager to learn more about the architectures like BERT, HuBERT (BERT fine-tuned for Automatic Speech Recognition), Transformers, RNNs. I can also work on properly implementing SHAP, which will require me to try fixing dependencies. Finally, I'll look for multimodal dataset on mental health disorders that offers both text and speech data.
- I am working on the IRB trainings: TC0019 - HIPAA: Health Insurance Portability Accountability Act Research Training Course; TC0087 - Human Subjects Protection Training (includes Minors and FDA where applicable). I'll document the training process as I complete them.
