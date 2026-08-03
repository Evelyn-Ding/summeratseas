# Week 8 — 7/27–8/2

---

## Monday, 7/27
- which set of features to extract? combo (take avgs if overlap) of CAPE-V + GRBAS = CVQ prompt
- what kind of ALM to train for the concept extractor step - flamingo (from the paper) vs gemini (recommended) vs something else 
## Tuesday, 7/28
- read and annotated the concept bottleneck FW paper: https://github.com/Evelyn-Ding/summeratseas/blob/main/week-06/concept%20bottleneck%20models.pdf
- new direction idea: achieve not just interpretability (“why”), but also test-time interventions
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

Overall reflections: It's been a great summer of research! I learned a lot about the research process, from IRB proposals to audio language models. At the beginning of the summer, I wasn't familiar with how I should approach the process of identifying vocal biomarkers for health disorders. I read many papers to understand the existing work done by researchers to extract features and train detection models, and I learned about techniques like post hoc interpretability and concept bottleneck frameworks. Now, I feel like I have a much more solid understanding of the speech processing field (and in particular, its application to detection of health disorders).
