# Week 3 — 6/22–6/28

---

## Monday, 6/22
- I wanted to deepen my understanding on what model interpretability meant, so I watched an MIT Opencourseware video on [Interpretability in ML for Healthcare](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-03/MIT%20Opencourseware%20-%20ML%20for%20Healthcare%20-%20Interpretability.pdf). This was really informative on how even if you ask the model to continually justify its reasoning, it might not give you a faithful answer; this is where techniques like LIME come in. It's also hard to generalize your results from training on clean data to the real world.
- The tradeoff between accuracy and complexity of models is worth exploring. Usually more complex models are less interpretable. Interestingly enough, models that have high accuracy sometimes are looking at nonsense features, while models looking at the "right" features (aligned with human knowledge) may end up performing worse.
- The difference between training a model from scratch and fine-tuning a model is that the former starts with randomly initialized weights that you train on massive datasets to obtain a generalist model, and the latter requires optimizing pre-trained weights using a small dataset and specialized use case.

## Tuesday, 6/23
- In our meeting, we discussed the next steps for the Bridge2AI-Voice dataset access request. I emailed the dataset providers with our questions about the Authorized Institutional Official and requirements for the people we add to the authorized recipients list.
- We also discussed how we can take this summer project in a different direction from the ongoing ARNI project; two main directions in this project's proposal (mapping features across disorders; building an interpretable diagnostic model) are related to ongoing work in the Arni project.
- I also met with Parmida one-on-one about how I could approach the next steps of the project: access audio data (she sent me a few Google Drive links to DAIC-WOZ, DI-HARD, and Librimix), extract acoustic features using the openSMILE toolkit (and look into PRAAT software as well), and train a simple speech classifier.
- Meeting notes [here](https://docs.google.com/document/d/1sG3M2QBKsiHNJ0RDA9XdGqiWv_AwBW7fA1HkksWMjiQ/edit?tab=t.0) and [here](https://docs.google.com/document/d/1Ck0IveANDh7lTpOJTzxSc6t_qOwUIrXAt2ZvtHgcOHM/edit?tab=t.0).
## Wednesday, 6/24
- Summer@SEAS Meeting on Engineering Wellness
- I successfully logged into the speechlab server! This gives me the ability to directly download large corpora that the Speech Lab has access to. For example, [TORGO](https://www.cs.toronto.edu/~complingweb/data/TORGO/torgo.html) - a dysarthria dataset - and DAIC-WOZ. Now, I have downloaded all of the data for TORGO (797MB) and listened to sample audio files. If I don't have enough storage to download the entire dataset (DAIC-WOZ is 39 GB), my access to the speechlab server allows me to write scripts in my home folder to access the data and generate outputs, without me needing to download the data locally!
## Thursday, 6/25
- I read and annotated the ARNI project report to catch up on their work. Their research builds on the prior language models [BERT](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-03/BERTmodel.pdf) (released by researchers at Google) and [MentalBERT](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-03/MentalBERT_paper.pdf).
- Here is my understanding of BERT and its significance in the advancements of the Natural Language Processing (NLP) field.
```
                  ┌─► Understanding/classifying text: BERT ──► RoBERTa (Decoders)
                  │
Word2Vec ──► LSTM ┼   (transformers kinda helped with both of these advancements)
                  │
                  └─► Generating text: GPT-1 ──► GPT-2 ──► GPT-3 (Encoders)
                      (by predicting the next word/token in the sequence)
```
- The ARNI project delves into the concept of interpretability in four main ways: (1) integrated gradients and SHAP (2) masking to verify predictions (3) linear probing by layer (4) k-means clustering and CPA. I can take inspiration from their project by using some of these techniques to achieve interpretability in the models that I train.
- My project differs from the ARNI project in the modality of the data. While ARNI uses text-based data (e.g. Reddit datasets) to analyze patterns in language, I'm looking for raw audio data (e.g. speech recordings) that I'll extract acoustic features from. Thus, instead of using psycholinguistic features from [Linguistic Inquiry and Word Count (LIWC)](https://www.liwc.app/help/howitworks), I'm looking at features from the [Geneva Minimalistic Acoustic Parameter Set (GeMAPS)](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-02/gemapsconvention_acousticfeatures.pdf). Then, similarly to the ARNI project, I will compare the results of training the models on these human-influenced features with model-learned features and try to make conclusions about the interpretability of the models.

## Friday, 6/26
- I attended the first ARNI meeting and got to hear about what everyone was working on :)
- I extracted acoustic features using the openSMILE toolkit! I followed the [tutorial](https://audeering.github.io/opensmile/get-started.html#obtaining-and-installing-opensmile) to install openSMILE, learn how to use and set up configs, extract features to a csv file, install gnuplot, and visualize data using gnuplot.
- I was able to recreate the process of extracting the energy feature and the chroma fft feature from the sample audio provided by openSMILE and generate a gnuplot for the chroma csv file!
- I took one sample audio (FC03-Session2-wav_headMic-0211.wav) and extracted the 88 features from the eGeMAPS (extended GeMAPS) feature set. I uploaded the results to [this csv](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-03/torgo1.csv).
---

## Week Summary

**What I did:**
- I worked on obtaining data for Bridge2AI-Voice pediatric and adult datasets, and I successfully downloaded the data for the TORGO dataset. I also got access to DAIC-WOZ, DI-HARD, and Librimix!
- Now that I have access to the audio data, I have started learning how to use the openSMILE toolkit to extract features and generate useful plots. I was able to extract eGeMAPS features for audio files in the TORGO dataset. I am also working on training speech classifiers to perform binary prediction and severity assessments for the speakers based on these extracted features.

**Questions:**
- Who should I list on recipients for the Bridge2AI-Voice dataset? (Everyone on the list must digitally sign the form.)
- Which speech classifiers have a more "interpretable" design - are all of them interpretable as long as I'm using a feature-based approach? How do I choose the optimal model to train?
- Do I shift away from looking at Voice Quality (VQ) labels and toward GeMAPS features, or try to keep both directions?

**Plan for next week:**
- I can train (more complex) black box models, then use techniques like LIME and SHAP to probe the models to achieve post-hoc interpretability. I also want to compare the performance of the GeMAPS (human-crafted) features approach to the SSL embeddings  (which are machine-generated) approach, allowing me to explore the trade-off between accuracy and interpretability.
