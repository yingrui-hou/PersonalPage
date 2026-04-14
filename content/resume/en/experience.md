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
