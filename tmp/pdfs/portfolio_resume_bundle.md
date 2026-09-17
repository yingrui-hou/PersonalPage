# Yingrui Hou - Portfolio and Resume
Clermont-Ferrand, France | yingrui.hou@outlook.com | +33(0)785396332
LinkedIn: https://www.linkedin.com/in/yingrui-hou | ORCID: https://orcid.org/0000-0001-6454-278X | Personal GitLab: https://gitlab.com/hyrsophie | CERN GitLab: https://gitlab.cern.ch/yihou

## Positioning
Simulation & Data Science Engineer for Physical Systems

Best fit for **industrial R&D teams working on physical systems**, especially where **simulation-to-measurement alignment**, **calibration**, **model validation**, and **uncertainty-aware analysis** are central to the work. Strongest value comes when the goal is not generic analytics, but making models trustworthy enough to support engineering decisions.

## Personal Introduction
From noisy measurements to reliable model decisions

I build calibrated models from noisy measurements and imperfect simulations for physical systems.

I build calibrated models from noisy measurements and imperfect simulations. My core strength is designing modelling, calibration, and validation strategies that extract reliable conclusions when the true state is only indirectly observed.

In postdoctoral work, that meant building reusable C++/Python/ROOT/Geant4 workflows for simulation-to-test alignment, calibration, monitoring, time-dependent inference, and model correction in large shared technical environments. The value came from turning validation results into calibration updates, software follow-up actions, and more credible modelling decisions.

This profile is strongest in industrial R&D environments working on complex physical systems, where instrumented tests, imperfect models, and engineering decisions must stay aligned under uncertainty.

## Seeking
**Simulation & Data Science Engineer for Physical Systems**, with strongest fit in **model validation**, **test-data analytics**, and **simulation-to-measurement alignment** roles where calibrated models and robust technical decisions matter.

## Overview
What this work supports in industrial R&D

Across these projects, the recurring pattern is consistent: build the workflow, correct mismatch between simulation and measurement, validate aggressively before trusting the result, and make the final model usable for decisions rather than just analysis. That is the same pattern behind industrial R&D teams working on physical systems, test-data interpretation, monitoring, calibration, model credibility, and simulation-informed design iteration.

The strongest proof repeats across multiple cases: test data used to calibrate model response, structured bias removed through reusable correction logic, anomalies traced to instrument behaviour or software rather than left unexplained, and quantified performance changes used to support calibration choices, software fixes, and simulation updates before a result is trusted for engineering decisions.

## Selected Outcomes
- Quantified response non-uniformity contribution to resolution below `1%` in a detailed detector study
- Improved reconstructed-energy resolution by about `2x` in representative PSD-based studies
- Built validation workflows that exposed detector and software issues, including a missing-energy bug later fixed downstream

## Selected Work
### Sensor Simulation & Reconstruction
Tags: Signal Processing, Simulation Calibration, Digital Twins

**Built a simulation-and-measurement workflow to quantify how detector non-uniformity affects energy resolution, using beam-test data to constrain the model instead of assuming ideal sensor response.**

Methods: Geant4 simulation, beam-test analysis, response-map reconstruction
Impact: linked measured non-uniformity to system-level resolution through both simulation code and experimental validation.
Industry relevance: Sensor Analytics | Measurement Systems | Simulation-Assisted Design

### Pulse-Shape Discrimination for Energy Reconstruction
Tags: Pulse Shape Discrimination, Detector Simulation, Time-Resolved Signal Analysis, Resolution Optimisation

**Built a PSD-oriented simulation and analysis workflow to extract shower composition from scintillation time profiles and use it to improve reconstructed energy.**

Methods: particle-dependent timing models, component fitting, correlation-based correction
Impact: showed that PSD-derived shower fractions can improve reconstructed energy and help judge which detector materials remain usable for timing-based separation.
Industry relevance: Time-Resolved Sensing | Signal Decomposition | Measurement-System Design

### Model Correction Workflow
Tags: Scientific Software, Event Filtering, Simulation Correction, Framework Integration

**Developed simulation-correction tooling that turns measured physics constraints into an event-level resampling workflow.**

Methods: Gaudi-package development, event-level correction, framework integration
Impact: turned measured constraints into a reusable event-level correction package for improving simplified simulation realism.
Industry relevance: Simulation Platforms | Scientific Computing | Model Correction

### Test-Data Validation & Root-Cause Analysis
Tags: Monitoring, Data Validation, Performance Diagnostics, Root-Cause Analysis

**Built a production-style validation workflow for early Run 3 photon reconstruction, focused on finding actionable detector and software issues.**

Methods: benchmark-channel checks, MC-data comparison, detector-level diagnostics
Impact: translated validation discrepancies into concrete calibration, detector, and software follow-ups before they became accepted bias.
Industry relevance: Production Monitoring | Model Validation | Observability | Quality Assurance

### Time-Series Inference
Tags: Time-Series Modelling, Bias Correction, Calibration, Joint Fitting

**Built a bias-corrected time-series inference workflow for data affected by selection effects, detector resolution, and sample mismatch.**

Methods: acceptance modelling, resolution calibration, custom fit components, joint fitting
Impact: converted a bias-sensitive latent-dynamics problem into a controlled inference workflow with dataset-specific corrections.
Industry relevance: Durability Modelling | State Estimation | Latent-Dynamics Inference

### Domain Adaptation for ML
Tags: GBDT, CatBoost, Reweighting, Feature Validation

**Built an ML validation and sample-alignment workflow in a shared analysis environment for noisy selection problems under dataset shift.**

Methods: CatBoost training, train-test diagnostics, gradient-boosting reweighting
Impact: improved downstream model reliability by treating dataset mismatch and overtraining checks as part of the production workflow.
Industry relevance: Domain Adaptation | Applied ML | Dataset Shift

## Additional Statistical Methods
These cases show deeper statistical-method development alongside the more immediately industry-facing simulation, calibration, and test-data workflows above.

### Advanced Inference Workflow Validation
Tags: Advanced Statistical Modelling, Basis-Function Methods, Latent-Parameter Estimation, Collaborative R&D

**Contributed the proof-of-principle validation needed to move a new basis-expansion inference idea from theory toward a usable workflow under realistic measurement conditions.**

Methods: basis expansion, covariance-aware joint fitting, pseudoexperiment validation, statistical background subtraction
Impact: helped move a novel inference method into a realistic workflow by testing robustness against background, efficiency, and resolution effects and by preparing purified real-data inputs.
Industry relevance: Advanced Modelling | Inverse Problems | Signal Analytics | Collaborative Method Development

### Weak-Signal Inference
Tags: Mixture Models, Maximum Likelihood, Feature Selection, Statistical Validation

**Built a reusable C++/Python/ROOT workflow for weak-signal extraction in data where background dominates and event-level truth is unavailable.**

Methods: likelihood fitting, control-sample validation, production yield workflows
Impact: turned rare-signal extraction into a reproducible workflow with stability checks and auditable validation logic.
Industry relevance: Rare Event Analytics | Anomaly Detection | Weakly Labeled Systems

## Resume
### Summary
R&D-oriented simulation and data scientist with a background in experimental physics and several years of experience building reusable Python/C++ workflows for calibration, validation, and inference on noisy measurement systems.

Core strength: turning imperfect simulations and biased measurements into decision-ready models through simulation-to-data alignment, correction workflows, uncertainty handling, and robust validation.

**Best fit:** industrial R&D teams working on physical systems, instrumented tests, sensor data, model credibility, and simulation-informed engineering decisions.

**Track record:** delivered validation and correction workflows that fed calibration updates, software fixes, and quantified model improvements under uncertainty.

### Selected Outcomes
- Quantified response non-uniformity contribution to resolution below `1%` in a detailed detector study
- Improved reconstructed-energy resolution by about `2x` in representative PSD-based studies
- Built validation workflows that exposed detector and software issues, including a missing-energy bug later fixed downstream

### Skills
- Python
- C/C++
- ROOT / RooFit
- Geant4
- CatBoost / Gradient Boosting
- Probabilistic Modelling
- Statistical Inference
- Maximum Likelihood Estimation
- Model Validation
- Calibration & Bias Correction
- Simulation-to-Data Alignment
- Signal Processing
- Domain Adaptation
- Workflow Automation (YAML / Shell / CMake)
- Large-Scale Data Analysis

### Technical Highlights
- Model validation and uncertainty quantification for noisy measurement systems
- Simulation-to-measurement alignment through calibration, reweighting, and correction workflows
- Sensor and system modelling with Geant4, ROOT, Python, and C++
- Test-data analytics, anomaly tracing, and root-cause diagnosis
- ML validation under dataset shift for decision-facing pipelines

### Professional Experience [Postdoctoral Researcher (2021 - 2025)]
### Inference, Validation & Analysis Workflows
CNRS / CERN / LHCb Collaboration + GRAiNITA Collaboration
- Built reusable C++/Python/ROOT workflows for weak-signal extraction, time-dependent inference, and validation on noisy datasets where direct event-level truth was unavailable.
- Implemented likelihood-based models and joint fits to estimate latent parameters under sample mismatch, finite resolution, and biased observation conditions.
- Developed CatBoost-based selection and validation pipelines, including train/test diagnostics, scan studies, and reproducible model application.
- Aligned simulated and observed datasets through gradient-boosting reweighting and control-sample calibration before downstream inference and selection decisions.
- Contributed reusable fit components and uncertainty-stress checks for advanced weighted and unbinned inference workflows.
- Worked in large technical collaborations with shared codebases and review discipline, with validation outputs feeding calibration and model decisions.

### Simulation, Calibration & Test-Data Interpretation
CNRS / CERN / LHCb Collaboration + GRAiNITA Collaboration
- Built and adapted Geant4/C++ simulation code for optical-response and detector studies, including geometry, stepping, and analysis outputs.
- Combined beam-test data, simulation, and response maps to model measurement-chain behaviour and quantify non-uniformity effects on system resolution, including a quantified constant-term contribution below `1%`.
- Built time-resolved signal-analysis workflows that recovered component fractions from scintillation timing and improved reconstructed-energy resolution by about a factor of `2` in representative PSD studies.
- Developed ROOT/C++ calibration and correction workflows to reduce structured bias and compare performance before and after correction across operating conditions.
- Built benchmark-based monitoring workflows to validate reconstruction and calibration quality, then traced anomalies to detector behaviour or software issues instead of stopping at descriptive analysis.
- Identified concrete issues that led to follow-up actions, including detector-specific anomalies and a missing-energy software problem later fixed in reconstruction software.
- Implemented event-level model-correction tooling inside collaboration frameworks to improve fast-model realism using measured constraints.

### Education
### PhD in Particle Physics
University of Chinese Academy of Sciences

### BSc in Applied Physics
China University of Mining and Technology

### Languages
- Chinese: Native speaker
- English: C1
- French: B1 to B2
