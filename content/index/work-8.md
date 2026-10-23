---
number: 08
homepage_order: 7
homepage_group: secondary
collapsible: true
title: TensorFlow migration and numerical verification
tags: TensorFlow | GPU | Numerical Testing
methods: basis expansion, covariance-aware joint fitting, pseudoexperiment validation, statistical background subtraction
impact: helped move a novel inference method into a realistic workflow by testing robustness against background, efficiency, and resolution effects and by preparing purified real-data inputs.
industry: Advanced Modelling | Inverse Problems | Signal Analytics | Collaborative Method Development
---
Learned TensorFlow through an existing project, extended its numerical models and verified the calculations against a mature C++ implementation.

### Problem
A collaborative measurement required new model components, realistic measurement effects and a working shared GPU environment.

### My contribution
- Started without TensorFlow knowledge, studied the inherited code and implemented new amplitude models plus efficiency, resolution and measurement-bias components.
- Configured a shared GPU workstation in half a day; migrated the code to a successful GPU run in a further half-day. These timings cover setup and migration only.
- Agreed component interfaces, reviewed GitLab merge requests and helped adjust weekly priorities. A collaborator developed the fitting component; I contributed to its testing.

### Validation and result
Compared calculations at identical inputs against C++, traced discrepancies to variable types and obtained agreement at the required decimal precision. Used large simulated samples for stability checks and compared observable distributions with real data. During review, identified a sign error in the fitting component’s mathematical definition; we verified and corrected it together.

The software supported a joint BESIII–LHCb measurement. Repeated simulated experiments compared inference methods on the same fixed-size samples. The publications report about 5% lower statistical uncertainty for the LHCb result: a collaborative method outcome, not a software-speed gain.

### Figures

![Sensitivity maps for the weighted inference method](assets/selected-work/work-8/fourier-weights.png "The weighting maps show how the method concentrates statistical sensitivity in the most informative regions while accounting for real measurement effects.")

### Publications

- Publication: *Measurement of the CKM angle γ in B± → D(→ KS0h′+h′−)h± decays with a novel approach*. DOI: [10.48550/arXiv.2604.05701](https://doi.org/10.48550/arXiv.2604.05701)
- Publication: *Precise measurement of the CKM angle γ with a novel approach*. DOI: [10.48550/arXiv.2604.05712](https://doi.org/10.48550/arXiv.2604.05712)
