# Week 8 — 7/27–8/2

---

## Monday, 7/27
- I looked into which set of concepts should be used to prompt the Audio Language Model (ALM) in the concept bottleneck framework.
  - In Yu-Wen's paper, a Clinical Voice Quality (CVQ) feature set was defined to consist of scores from CAPE-V (overall severity, roughness, breathiness, strain, pitch abnormality, loudness abnormality) + GRBAS (overall severity, roughness, breathiness, asthenia, strain) were used. Values for these scores came from the human annotations in the Perceptual Voice Qualities Database (PVQD). For the four concepts that overlapped, an average was taken of the two values.
  - For my project, I am currently working with the Neurovoz PD dataset. Since Neurovoz provides a complete folder with GRBAS annotations, I may focus on the five concepts in the GRBAS feature set.
- I also thought about which ALM to train for the concept extractor step. Flamingo-Audio was used in Yu-Wen's paper (from NVIDIA, available via Hugging Face). For my project, Gemini may be a better fit because it doesn't require the fine-tuning setup that is necessary for Flamingo-Audio in order to achieve a reasonably high accuracy. Using Gemini, I can test out this approach of zero-shot concept extraction to see if it generates strong enough correlations between model output and human annotator GRBAS ratings.

## Tuesday, 7/28
- I read and annotated the [concept bottleneck framework paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/concept%20bottleneck%20models.pdf). My understanding is that models are given input x, which has ground truth annotations of concept c (an intermediate step to the final prediction) and target y (the final prediction). Given an input x, the models are trained to predict a concept c-hat and must directly use these concept scores to predict the target y-hat.
- This sparked a new idea for the direction of the project: to achieve not just interpretability (“why”), but also test-time interventions where I see how changing a concept's value will affect the final prediction. In Yu-Wen's paper, the ALM was fine-tuned on a PVQD dataset (separate from the depression and dysarthria datasets they were applied to) to assess CAPE-V + GRBAS scores. The analysis on concepts was focused on the correlation the ALM output and ground truth annotations, and did not test whether adjusting certain concept values would change the downstream prediction. Since my Neurovoz dataset happens to contain GRBAS scores, I can go the extra step of changing the predicted concept values and seeing how that affects the final prediction result (i.e. I’m not just predicting the alignment between c-hat and c, but I can actually change c-hat to become c…)


## Wednesday, 7/29
- Finished all IRB trainings - waiting for others to complete
- Meeting -> focusing on voxprofile would definitely change feature set AND ALM
  - use voxprofile first to generate scores for the 25 VQ labels instead of fine-tuning ALM (FlamingoAudio from Hugging Face)
  - this will help me get familiar with running on speechlab server
## Thursday, 7/30
- Finished IRB abstracts - waiting for review
- Connected to speechlab server GPU access
- Setup folder ```/proj/speech/users/esd2154```
## Friday, 7/31
- Read and annotate encoder/decoder paper for mentalBERT project -> i'll write up the report / summary of it
- also find a multimodal dataset 
- ARNI Meeting
- found a paper that does exactly what we're looking for: benchmarks extracted features + performance of classifier for depression datasets across audio/speech vs text vs taken together (multi-modal) - systematically reviews 65 studies from 2008-2024
  - social media datasets (text only, bc scraped from the internet) are quite separate from conversation-based datasets (which have both speech / raw audio and text / transcripts)
  - ```As shown in Table V, in the early years, pre-defined text embeddings extracted from Word2Vec [92] and LIWC features were commonly used in ADD. Recently, with the advancement of Transformer-based models like BERT [93] and RoBERTa [94] leverage bidirectional encoding and optimized training techniques, producing context-sensitive embeddings that capture sentence-level semantics. These improvements enhance robustness and applicability in NLP tasks```
  - interesting enough, it mentions LIWC features (text) but not eGeMAPS features (in the audio section)...but it does hint at it b/c it categorizes spectral, cepstral, and prosodic features
- based on what i've read, i believe daic-woz would be the best bet for a multimodal (text+speech) dataset but it lacks social media data. also, it's overused (fig 5b: 64% of conversational data!) and thus highly oversaturated in # of studies. the current mentalbert project uses reddit mental health dataset https://zenodo.org/records/3941387 which is not cited explicitly but many many similar datasets are featured in the paper (table II)
---

## Week Summary

**What I did:**
- I finalized the IRB application! After completing the training process and writing the abstracts, I sent out emails for everyone on the Personnel list to approve the protocol.
- I explored the big idea of training a concept bottleneck model to achieve interpretability. This involved setting up a directory in the speechlab server for me to train models using the lab's GPU machines.

**Questions:**
- I ran into some issues when trying to create a Python virtual environment inside the speechserver. How do I resolve the issues from trying to set up conda and venv?
- To continue accessing the speechlab GPU machines, how should I setup a VPN?

**Plan for next week:**
- Starting next week, I will be taking the weekly meetings from Zoom! I'll keep working on the project from home for the rest of the summer, and I'm really excited to continue the project into the school year too.
- I hope to present poster at the Columbia undergraduate research symposium in October. Looking forward to writing up a final report and making a poster to summarize my findings :)

**Overall reflections:** It's been a great summer of research! I learned a lot about the research process, from IRB proposals to audio language models. At the beginning of the summer, I wasn't familiar with how I should approach the process of identifying vocal biomarkers for health disorders. I read many papers to understand the existing work done by researchers to extract features from speech audio and train detection models, and I learned about techniques like post hoc interpretability and concept bottleneck frameworks. Now, I feel like I have a much more solid understanding of the speech processing field (and in particular, its application to detection of health disorders).
