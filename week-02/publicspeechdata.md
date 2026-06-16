# Public Speech Data — Citation Review

Citation-by-citation breakdown of the speech-relevant sections (2.1, 2.2, 2.4, 2.6, 2.7) from the week-1 mental health datasets survey paper.

## 2.1 Depression

| Citation | Proposes dataset? | Public? | Summary |
|---|---|---|---|
| **Mundt et al., 2007** | No — modeling/biomarker study | N/A (clinical study, not a released corpus) | IVR-collected speech from depressed patients in a 6-week observational study; found pause time/speech rate (psychomotor retardation) track depression severity and treatment response. |
| **Gratch et al., 2014** | **Yes — DAIC/DAIC-WOZ** | **Request-only** (not freely downloadable; apply via [USC ICT](https://dcapswoz.ict.usc.edu/)) | Wizard-of-Oz clinical interviews (189–275 participants) w/ audio, video, transcripts, labeled with **PHQ-8** depression severity scores. The foundational corpus underlying most of the rest of this list. |
| **Dumpala et al., 2024** | No | Uses DAIC-WOZ | "Self-Supervised Embeddings for Detecting Individual Symptoms of Depression" (Interspeech 2024) — uses SSL speech embeddings to predict individual PHQ symptoms, not just an overall label. |
| **Lewis et al., 2025** | Partial — new longitudinal corpus, not obviously open | Unclear/likely restricted (smartphone clinical study) | "Towards the Objective Characterisation of MDD..." (Interspeech 2025) — 18-month smartphone speech study, 585 participants, biweekly samples; fluency/loudness features negatively associated with symptom severity. |
| **Maji et al., 2024** | No | Uses existing low-resource depression corpora (e.g., Androids) | Layer-wise probing of SSL models (Wav2Vec2, HuBERT, WavLM) — cross-lingual study of which SSL layers best encode depression-relevant speech info. |
| **Dumpala et al., 2025** | No | Uses DAIC-WOZ-style data | "Test-Time Training for Speech-based Depression Detection" — adapts the model at inference time to each new speaker/session to improve generalization. |
| **Campbell et al., 2023** | No | Uses AVEC/DAIC-style corpora | "Classifying depression symptom severity..." (Interspeech 2023) — compares personalized vs. generalized ML models on speech representations for **severity** classification. |
| **Fara et al., 2023a** | Inconclusive — couldn't confirm exact paper | — | Likely a multimodal (audio+video+text) depression-severity fusion paper in the AVEC/DAIC tradition; couldn't pin the exact title/dataset with confidence — flagging rather than guessing. |

## 2.2 Bipolar

| Citation | Proposes dataset? | Public? | Summary |
|---|---|---|---|
| **Gratch et al., 2014** | DAIC-WOZ (see above) | Request-only | Reused here for bipolar-adjacent distress signals. |
| **Wang et al., 2020** | **Yes — AMoSS-I** | Not stated as openly downloadable (academic dataset, likely request-based) | 50 non-clinical interviews of people with bipolar disorder (BD) or borderline personality disorder (BPD); linear classifier on language+speech features distinguishes BD vs. BPD. |
| **Erdener et al., 2019** | No — lab study, not a public corpus | N/A | Small McGurk-effect audiovisual perception experiment (12 manic, 10 depressive, 22 controls) — finds altered auditory-visual speech integration in bipolar mania/depression. |
| **Bersani et al., 2013** | No | N/A | FACS-coded facial-expression study comparing bipolar and schizophrenia patients' emotional responses — not a speech/audio dataset, more facial-affect focused. |
| **Kang et al., 2018** | No | N/A | Facial-expression recognition/intensity study in BD vs. MDD — again facial, not primarily speech. |
| **Wang et al., 2024** | No | N/A (clinical MRI data, not open) | "Enhancing Early Diagnosis of Bipolar Disorder in Adolescents through Multimodal Neuroimaging" — combines behavioral assessment + multimodal MRI, not speech/audio. |

**Note:** Several bipolar citations (Bersani, Kang, Erdener, Wang 2024) are facial/neuroimaging/perception studies, not speech-data papers — worth double-checking if the survey draft is over-attributing them to the "speech" theme.

## 2.4 PTSD

| Citation | Proposes dataset? | Public? | Summary |
|---|---|---|---|
| **Sawadogo et al., 2024** | **Yes — PTSD in the Wild** | **Yes, public** — paper explicitly states it was "prepared for public distribution" ([arXiv](https://arxiv.org/abs/2209.14085)) | Unconstrained, "in the wild" video database (high variability in pose/lighting/demographics) for automatic PTSD recognition; also proposes a deep-learning detection baseline. |
| **DeVault et al., 2014** | Describes SimSensei/DAIC | Request-only (same DAIC family) | SimSensei Kiosk — virtual human interviewer ("Ellie") that elicits verbal/nonverbal distress indicators for depression/anxiety/PTSD; produced the original DAIC corpus (167–275 participants). |

## 2.6 Schizophrenia

Mostly modeling papers working off small private clinical speech samples rather than shared corpora — none of these showed up as "public dataset" releases.

| Citation | Dataset used | Summary |
|---|---|---|
| **Iter, Yoon & Jurafsky, 2018** | Own clinical transcripts (not released) | Automatic detection of incoherent speech via semantic similarity between consecutive text chunks ("derailment" measure). |
| **Bar et al., 2019** | Own/clinical transcripts | Computational model of "reference incoherence" via ambiguous pronoun usage — strong predictive feature for schizophrenia speech. |
| **Hong et al., 2012** | Own clinical sample | Early work on repetitions in speech as a distinguishing feature of schizophrenia-spectrum speech vs. controls. |
| **Li et al., 2021 / Tang et al., 2021** | Clinical samples (Tang: Zucker Hillside/LDC-affiliated) | Tang et al. used BERT-based sentence-level coherence, found NLP measures (tangentiality, pronoun overuse, fewer adjectives/determiners) outperform clinical rating scales. |
| **Espy-Wilson, 1992** | N/A — couldn't verify this exact 1992 citation | Her broader body of work is on articulatory/acoustic modeling for mental-health speech, but no confirmed 1992 schizophrenia-specific paper turned up. Worth double-checking the year/title against the source bibliography. |
| **Shriki et al., 2022** | Own Hebrew-speaking inpatient sample (not released) | Masks specific morphosyntactic categories (nouns, verbs, etc.) when fine-tuning a classifier to find which categories are most "salient" for diagnosis — nouns mattered most. |
| **Aich et al., 2025** | Same corpus as the bipolar/schizophrenia dataset already flagged in week-02 sheet (644 subjects, [github.com/ankitaich09/EMNLP_2022](https://github.com/ankitaich09/EMNLP_2022)) | Uses LLMs to automate annotation/extraction of clinically-relevant speech/social-functioning features in bipolar & schizophrenia interviews — connects directly back to a dataset already flagged as public. |

## 2.7 Dementia / Alzheimer's

This subfield is the most consistently open of all five sections.

| Citation | Proposes dataset? | Public? | Summary |
|---|---|---|---|
| **Lanzi et al., 2023** | **Yes — DementiaBank Delaware Corpus** | **Yes, but gated** — free to access via [TalkBank](https://talkbank.org/dementia/access/) with a data-use agreement (not anonymous-download, but openly available to researchers who sign up) | 55 participants, CHAT transcripts + audio + test scores; picture description/story narrative/procedural/personal narrative tasks. |
| **Luz et al., 2021a/b** | **Yes — ADReSS / ADReSSo** | **Yes**, same TalkBank gated-access model | Standardized benchmark from spontaneous speech for AD detection, cognitive-score inference, and decline prediction; ADReSSo specifically forces models to work from raw audio (no provided manual transcripts). |
| **Peled-Cohen & Reichart, 2025** | No — it's a survey | N/A | "A Systematic Review of NLP for Dementia" (TACL 2025) — reviews 240+ papers, finds ~half focus only on detection from clinical data, and calls out the field's lack of multilingual/multimodal datasets as a major open gap. |

---

## Bottom line on public availability

- **Genuinely public/open**: PTSD in the Wild, DementiaBank corpora, ADReSS/ADReSSo (gated but accessible), and the Aich et al. bipolar/schizophrenia corpus already flagged.
- **Request/application-only**: DAIC, DAIC-WOZ (and everything downstream of it — most of the depression and PTSD modeling papers), AMoSS-I.
- **Not public at all / private clinical samples**: nearly all the schizophrenia NLP papers (Iter, Bar, Hong, Tang, Shriki) and the bipolar facial/neuroimaging studies (Bersani, Kang, Erdener, Wang 2024) — these are working off small, study-specific clinical recordings that were never released.

**Low-confidence citations to double-check against the source bibliography:** Fara et al., 2023a; Espy-Wilson, 1992.
