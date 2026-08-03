# Week 8 — 7/27–8/2

---

## Monday, 7/27
- I looked into which set of concepts should be used to prompt the Audio Language Model (ALM) in the concept bottleneck framework.
  - In Yu-Wen's paper, a Clinical Voice Quality (CVQ) feature set was defined to consist of scores from CAPE-V (overall severity, roughness, breathiness, strain, pitch abnormality, loudness abnormality) + GRBAS (overall severity, roughness, breathiness, asthenia, strain) were used. Values for these scores came from the human annotations in the Perceptual Voice Qualities Database (PVQD). For the four concepts that overlapped, an average was taken of the two values.
  - For my project, I am currently working with the Neurovoz PD dataset. Since Neurovoz provides a complete folder with GRBAS annotations, I may focus on the five concepts in the GRBAS feature set.
- I also thought about which ALM to train for the concept extractor step. Flamingo-Audio was used in Yu-Wen's paper (from NVIDIA, available via Hugging Face). For my project, Gemini may be a better fit because it doesn't require the fine-tuning setup that is necessary for Flamingo-Audio in order to achieve a reasonably high accuracy. Using Gemini, I can test out this approach of zero-shot concept extraction to see if it generates strong enough correlations between model output and human annotator GRBAS ratings.

## Tuesday, 7/28
- I read and annotated the [concept bottleneck framework paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/concept%20bottleneck%20models.pdf). My understanding is that models are given input x, which has ground truth annotations of concept c (an intermediate step to the final prediction) and target y (the final prediction). Given an input x, the models are trained to predict a concept c-hat and must directly use these concept scores to predict the target y-hat.
- This sparked a new idea for the direction of the project: to achieve not just interpretability (“why”), but also test-time interventions where I see how changing a concept's value will affect the final prediction. In Yu-Wen's paper, the ALM was fine-tuned on a PVQD dataset (separate from the depression and dysarthria datasets they were applied to) to assess CAPE-V + GRBAS scores. The analysis on concepts was focused on the correlation the ALM output and ground truth annotations, and did not test whether adjusting certain concept values would change the downstream prediction. Since my Neurovoz dataset happens to contain GRBAS scores, I can go the extra step of changing the predicted concept values and seeing how that affects the final prediction result (i.e. I’m not just predicting the alignment between c-hat and c, but I can actually change c-hat to become c).

## Wednesday, 7/29
- I completed all of my IRB trainings and wrote a [document](https://docs.google.com/document/d/1M2-xi_zimDJckRlHCPVxGVST6vWSkIB_DMAjFbQKIso/edit?usp=sharing) with instructions for how to complete the trainings. This document also contains the scientific and lay abstracts for the research project.
- We had our weekly meeting in-person!

## Thursday, 7/30
- For the ALM, Yu-Wen recommended that I start with on [VoxProfile](https://huggingface.co/tiantiaf/whisper-large-v3-voice-quality] (instead of [Flamingo-Audio](https://huggingface.co/nvidia/audio-flamingo-next-think-hf)) to generate scores for the 25 voice quality labels, resulting in a different feature set than the CVQ prompt. This model is already pre-trained, so there's no need to fine-tune it! It will help me get familiar with running models the speechlab server.
- I connected to speechlab server and setup the directory ```/proj/speech/users/esd2154```. Also, I was able to check the status of speechlab's GPUs using ```watch nvidia-smi```, which was pretty cool!

## Friday, 7/31
- For the ARNI project (mentalBERT), I read the [Attention Is All You Need paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-07/Attention%20is%20all%20you%20need%20Encoders%20and%20Decoders.pdf) on encoders/decoders. I also looked into multimodal datasets that we could run side-by-side comparisons of text and speech analysis on.
- While searching for a multimodal dataset, I came across a relevant [paper](https://github.com/Evelyn-Ding/summeratseas/blob/main/week-08/Automated_Depression_Detection_From_Text_and_Audio_A_Systematic_Review.pdf) that systematically reviews 65 studies from 2008-2024, benchmarking the performance of various feature sets and classifiers for depression detection, comparing across audio speech vs text vs both taken together (multi-modal).
  - The paper explains that social media datasets contain text only, because they're scraped from the internet posts. On the other hand, conversation-based datasets contain both raw audio (speech recordings) and text (transcripts extracted from speech recordings). These categories are quite separate; the ARNI group has been working with social media data (specifically this [Reddit mental health dataset](https://zenodo.org/records/3941387), but bringing in speech analysis may require conversation at a instead.
  - If we were to use a multimodal (text + speech) dataset, I believe DAIC-WOZ would be the best bet. We already have it available for download in the speechlab server. However, it is conversation based instead of social media data. Also, it's been used in a large number of studies (64% of all studies that used conversational data!), which have already covered a lot of ground in extracting features (like LIWC) and training a variety of different classifiers and models—so we may have to look for a different angle. 
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
