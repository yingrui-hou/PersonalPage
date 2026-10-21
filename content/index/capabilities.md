### Capabilities supported by project work
- **Check model reliability:** calibrated and validated a deep-learning flavour-tagging model on real data. Applicable to evaluating learned-model outputs before using them in a new analysis. [Calibration case](index.html#work-9).
- **Investigate performance problems:** used real data to assess an ECAL image-recognition model and traced reconstruction discrepancies to calibration, detector or software issues. Applicable to model evaluation and root-cause investigation. [Diagnostic case](index.html#work-6).
- **Handle sample differences:** trained CatBoost classifiers with train/test checks and aligned control and target samples through reweighting. Applicable to evaluating models when data distributions differ. [Dataset-shift case](index.html#work-3).
- **Learn and apply methods:** started with no TensorFlow knowledge, adapted inherited code with new amplitude and measurement-effect models, and verified it using generated simulations. With no prior GPU or multi-user administration experience, configured a shared GPU workstation in half a day and migrated the code to a successful GPU run in a further half-day. These timings cover setup and migration. [Learning and implementation case](index.html#work-8).
- **Coordinate and communicate:** organised connected measurement, analysis and validation tasks; contributed to shared code and technical reviews. Presented at GDR-InF 2022 and FCC/DRD France 2025, including on behalf of GRAiNITA.

- **Reliable scientific software:** compared TensorFlow amplitudes with a mature C++ reference, resolved variable-type discrepancies and used GitLab reviews to detect a fitter sign error. Weekly team planning adjusted priorities as new data issues emerged. [Verification and collaboration](index.html#work-8).

### How I would approach a new business problem
A proposed first-month sequence, with scope and timing agreed with the team once data and environment access are available:
- **Understand the decision:** identify the users, current process, success criteria and costs of different errors.
- **Establish a baseline:** review data quality and reproduce an existing result or a simple reference analysis.
- **Investigate one priority:** examine sample bias, model calibration or a specific performance discrepancy, using checks agreed with domain experts.
- **Deliver a reviewable result:** share reproducible analysis, findings, limitations and a prioritised next-step proposal.

- **Acquisition and quality automation:** Developed a Shell pipeline for beam-test acquisition, storage, quick calibration and initial quality checks, connecting detector readout, tracking and timing calibration. Participated in on-site setup and data taking; assisted subsequent fitting and measurement-effect corrections.

- **Diagnosis to code review:** Diagnosed incorrect ECAL photon truth associations; revised cluster-energy matching, tested multiple simulated decay channels and improved thread safety through review. The merged change supported subsequent Run 3 analyses and reconstruction-performance checks.

- **ML tied to the measurement objective:** Developed CatBoost selection with reweighting, feature pruning, five-fold assessment and train/test KS checks; scanned a measurement-oriented threshold using fitted yields and selection efficiencies.

- **Experimental evidence for design choices:** Compared measured PSD time profiles and used the measured parameters to generate simulations and check temporal separation. This contributed to the team’s choice of ZnWO4 for further study; engineers handled measurement setup and particle sources.
