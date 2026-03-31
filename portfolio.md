# Data Science & Modelling Portfolio
**Yingrui Hou**

---

## Overview

My work focuses on extracting reliable signals from complex, noisy systems where direct ground truth is unavailable.
This involves probabilistic modelling, bias correction, and iterative validation under uncertainty.

---

# Case Study 1 — Weak Signal Extraction in Noisy Data

## Problem
Identify meaningful signals from datasets dominated by noise, without per-event ground truth.

## Approach
- Built probabilistic mixture models:
  - Signal (Gaussian / Crystal Ball)
  - Background (exponential / polynomial)
- Used maximum likelihood estimation
- Designed feature-based selection strategies

## Challenges
- No explicit labels
- Strong overlap between signal and background
- Sensitivity to selection bias

## Solution
- Used proxy metrics:
  - Signal yield
  - Distribution width
  - Stability across datasets
- Performed cross-checks across independent samples

## Outcome
- Robust signal extraction under low signal-to-noise conditions
- Improved stability of parameter estimation

## Industrial relevance
- Fraud detection
- Anomaly detection
- Weak supervision learning

---

# Case Study 2 — Time-Series Modelling with Bias Correction

## Problem
Infer latent dynamics from noisy temporal data with measurement bias.

## Approach
- Built time-dependent probabilistic models
- Corrected for:
  - Measurement resolution
  - Selection bias (acceptance)
  - Noise dilution
- Used control datasets for calibration

## Challenges
- Biased observations
- Noise-dominated signals
- Multi-source data integration

## Solution
- Calibration using simulation and control channels
- Joint modelling across datasets

## Outcome
- Improved stability and reliability of inferred parameters
- Reduced systematic uncertainty

## Industrial relevance
- User lifecycle modelling
- Retention / churn analysis
- Causal inference under biased data

---

# Case Study 3 — Machine Learning under Distribution Shift

## Problem
Training data distribution differs from real-world data.

## Approach
- Trained Gradient Boosted Decision Trees (GBDT)
- Compared feature distributions between datasets
- Applied reweighting using gradient boosting

## Pipeline
Train → Compare → Reweight → Retrain → Evaluate

## Challenges
- Simulation vs real data mismatch
- Model performance degradation

## Solution
- Distribution alignment via reweighting
- Feature-level validation

## Outcome
- Improved model generalisation
- Reduced bias in downstream analysis

## Industrial relevance
- Domain adaptation
- Production ML
- Dataset shift handling

---

# Case Study 4 — Sensor Signal Modelling and Reconstruction

## Problem
Transform raw sensor signals into accurate measurements and classify signal types.

## Approach
- Modelled signal chain:
  energy → photon production → electronic signal → reconstruction
- Analysed waveform characteristics
- Applied pulse shape discrimination

## Challenges
- Complex signal generation process
- Noise and overlapping signals

## Solution
- Statistical modelling of signal components
- Feature extraction from waveform shape

## Outcome
- Improved resolution and signal discrimination
- Validated detector design performance

## Industrial relevance
- Sensor data analysis
- Signal processing
- IoT / embedded systems

---

# Case Study 5 — Model Calibration and System Optimisation

## Problem
Measurement systems show bias and non-linear behaviour.

## Approach
- Analysed correlations between variables
- Applied transformations and calibration strategies
- Compared simulation and experimental data

## Challenges
- Non-linear system response
- Energy-dependent bias

## Solution
- Parameter tuning based on observed correlations
- Iterative refinement

## Outcome
- Reduced bias
- Improved measurement accuracy

## Industrial relevance
- System calibration
- Digital twin modelling
- Engineering optimisation

---

# Key Competencies Demonstrated

- Probabilistic modelling under uncertainty
- Signal extraction without labels
- Bias correction and calibration
- Handling dataset shift
- Iterative model refinement
- Large-scale data processing

---
