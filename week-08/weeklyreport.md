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
- Read and annotate encoder/decoder paper for mentalBERT project and also find a multimodal dataset
- ARNI Meeting
- found a paper that does exactly what we're looking for: benchmarks extracted features + performance of classifier for depression datasets across audio/speech vs text vs taken together (multi-modal) - systematically reviews 65 studies from 2008-2024
  - social media datasets (text only, bc scraped from the internet) are quite separate from conversation-based datasets (which have both speech / raw audio and text / transcripts)
  - ```As shown in Table V, in the early years, pre-defined text embeddings extracted from Word2Vec [92] and LIWC features were commonly used in ADD. Recently, with the advancement of Transformer-based models like BERT [93] and RoBERTa [94] leverage bidirectional encoding and optimized training techniques, producing context-sensitive embeddings that capture sentence-level semantics. These improvements enhance robustness and applicability in NLP tasks```
  - interesting enough, it mentions LIWC features (text) but not eGeMAPS features (in the audio section)...but it does hint at it b/c it categorizes spectral, cepstral, and prosodic features
---

## Week Summary

**What I did:**
- wrapping up irb process and getting ready to submit by EOW
- started exploring direction of training a concept bottleneck models (big for interpretability)

**Questions:**
- looking forward to learning more about this process - can also train models from home via vpn!

**Plan for next week:**
- notes: will be taking meetings zoom @ home
- cont. work into the fall sem
- hope to present poster at fall showcase in oct.! :)
