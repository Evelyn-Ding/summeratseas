# Bridge2AI Voice Dataset — Feature Notes

## Access Status

### PhysioNet (Adult + Pediatric)
- **Status: Approved** — downloaded 13.0 GB of pre-extracted features
- No raw audio is included; only the derived features listed below

### Synapse
- **Status: Application in progress** — currently completing forms including abstract section
- **Bottleneck: Institutional Signing Official (ISO)** — need one to complete the application

---

## Feature Files

```
features
├── audio_quality_metrics.json
├── audio_quality_metrics.tsv
├── ppgs.parquet
├── sparc_ema.parquet
├── sparc_loudness.parquet
├── sparc_periodicity.parquet
├── sparc_pitch.parquet
├── static_features.json        ← contains full eGeMAPS + more (see below)
├── static_features.tsv
├── torchaudio_mel_spectrogram.parquet
├── torchaudio_mfcc.parquet
├── torchaudio_pitch.parquet
└── torchaudio_spectrogram.parquet
```

---

## GeMAPS Overlap

GeMAPS (Geneva Minimalistic Acoustic Parameter Set, Eyben et al. 2015) defines **62 parameters** across:
- **Frequency**: Pitch (F0), Jitter, Formants 1–3 frequency + bandwidth
- **Energy/Amplitude**: Shimmer, Loudness, HNR (Harmonics-to-Noise Ratio)
- **Spectral**: Alpha Ratio, Hammarberg Index, Spectral Slope (0–500 Hz, 500–1500 Hz), Formant relative energies, H1–H2, H1–A3
- **Temporal**: Rate of loudness peaks, mean/SD of voiced/unvoiced region lengths, voiced regions per second

eGeMAPS extends to **88 parameters**, adding MFCC 1–4, Spectral Flux, and Formant 2–3 bandwidths.

| File | What it is | GeMAPS overlap? | Notes |
|---|---|---|---|
| `static_features` | **Full eGeMAPS + extra features** | **Yes — complete eGeMAPS** | Extracted via openSMILE (confirmed by `sma3nz`/`sma3` naming). See breakdown below. |
| `sparc_pitch.parquet` | F0/pitch features | Yes — GeMAPS | Redundant with static_features F0; different extractor |
| `sparc_loudness.parquet` | Loudness/energy | Yes — GeMAPS | Redundant with static_features loudness |
| `sparc_periodicity.parquet` | Voiced/unvoiced + HNR-like | Yes — GeMAPS | Relates to HNR and temporal features |
| `torchaudio_mfcc.parquet` | MFCCs (frame-level) | Yes — eGeMAPS | Frame-level; static_features has summary stats (mean, CoV) |
| `torchaudio_pitch.parquet` | F0 (frame-level) | Yes — GeMAPS | Frame-level version |
| `torchaudio_mel_spectrogram.parquet` | Mel spectrogram (2D) | No | Dense frame-level representation |
| `torchaudio_spectrogram.parquet` | Raw spectrogram (2D) | No | Dense frame-level representation |
| `ppgs.parquet` | Phonetic Posteriorgrams | No | SSL-derived soft phoneme labels |
| `sparc_ema.parquet` | Articulatory features | No | Not in GeMAPS; relevant for pronunciation work |
| `audio_quality_metrics` | SNR, clipping, etc. | No | Recording quality metrics |

---

## static_features Breakdown

### eGeMAPS features (extracted via openSMILE)
All of the following are confirmed present and match the eGeMAPS 88-parameter spec exactly:

| Feature group | Fields present |
|---|---|
| **F0 (pitch)** | mean, CoV, 20th/50th/80th percentile, percentile range, mean/SD rising+falling slope |
| **Loudness** | mean, CoV, 20th/50th/80th percentile, percentile range, mean/SD rising+falling slope |
| **Jitter** | mean, CoV |
| **Shimmer (dB)** | mean, CoV |
| **HNR** | mean, CoV |
| **H1–H2, H1–A3** | mean, CoV |
| **F1, F2, F3** | frequency mean/CoV, bandwidth mean/CoV, amplitude relative to F0 mean/CoV |
| **Alpha Ratio** | voiced mean/CoV, unvoiced mean |
| **Hammarberg Index** | voiced mean/CoV, unvoiced mean |
| **Spectral Slope 0–500 Hz, 500–1500 Hz** | voiced mean/CoV, unvoiced mean |
| **Spectral Flux** | overall mean/CoV, voiced mean/CoV, unvoiced mean |
| **MFCC 1–4** | overall mean/CoV, voiced mean/CoV |
| **Temporal** | loudness peaks/sec, voiced segments/sec, mean/SD voiced segment length, mean/SD unvoiced segment length |
| **Equivalent sound level** | dBp |

### Extra features beyond eGeMAPS
These are additional features present in static_features that are NOT part of GeMAPS/eGeMAPS:

| Feature group | Fields | Notes |
|---|---|---|
| **Speech timing / rhythm** | speaking_rate, articulation_rate, phonation_ratio, pause_rate, mean_pause_duration | Clinically very relevant for depression (psychomotor retardation) |
| **F0 in Hz** | mean_f0_hertz, std_f0_hertz | Duplicate of eGeMAPS F0 but in Hz instead of semitones |
| **Intensity** | mean_intensity_db, std_intensity_db, range_ratio_intensity_db | Not in GeMAPS explicitly |
| **HNR (Praat)** | mean_hnr_db, std_hnr_db | Second HNR extraction via Praat alongside openSMILE |
| **Spectral shape** | spectral_slope, spectral_tilt, spectral_gravity, spectral_std_dev, spectral_skewness, spectral_kurtosis | Richer spectral description beyond GeMAPS |
| **CPP** | cepstral_peak_prominence_mean, cepstral_peak_prominence_std | Cepstral Peak Prominence — strong voice quality marker, not in GeMAPS |
| **Formants (Praat)** | mean/std F1, F2 location + bandwidth | Second formant extraction via Praat alongside openSMILE |
| **Jitter variants (Praat)** | local, localabsolute, rap, ppq5, ddp | Multiple jitter measures beyond GeMAPS's single jitter |
| **Shimmer variants (Praat)** | local, localDB, apq3, apq5, apq11, dda | Multiple shimmer measures beyond GeMAPS's single shimmer |
| **Signal quality** | stoi, pesq, si_sdr | Recording quality metrics (intelligibility, perceptual quality, distortion ratio) |

---

## Summary

The Bridge2AI dataset provides a very rich hand-crafted feature set. `static_features` alone covers the entire eGeMAPS standard plus Praat-based jitter/shimmer variants, speech timing features, spectral shape descriptors, and CPP — all of which are interpretable and clinically grounded. The SPARC and torchaudio files provide frame-level versions of a subset of these same features, useful if temporal dynamics (not just summary statistics) are needed.
