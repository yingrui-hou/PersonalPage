---
number: 08
homepage_order: 7
homepage_group: secondary
collapsible: true
title: TensorFlow/GPU Code Adaptation & Inference Validation
tags: TensorFlow | GPU Computing | Statistical Modelling | Collaborative R&D
methods: basis expansion, covariance-aware joint fitting, pseudoexperiment validation, statistical background subtraction
impact: helped move a novel inference method into a realistic workflow by testing robustness against background, efficiency, and resolution effects and by preparing purified real-data inputs.
industry: Advanced Modelling | Inverse Problems | Signal Analytics | Collaborative Method Development
---
**Starting with no TensorFlow knowledge, adapted research code with new models, verified it using simulated data and brought the calculation onto a shared GPU workstation. The joint gamma-measurement work also included inference-method validation under realistic measurement conditions.**

![Sensitivity maps for the weighted inference method](assets/selected-work/work-8/fourier-weights.png "The weighting maps show how the method concentrates statistical sensitivity in the most informative regions while accounting for real measurement effects.")

### Problem
The method problem was not only to propose a new structured inference strategy, but to show that it remained usable once real measurement effects were introduced. Background contamination, reconstruction efficiency, and detector resolution all had to be tested explicitly before the method could be trusted in a collaborative measurement.

### Workflow
- Evaluated how experimental background, reconstruction efficiency, and detector resolution affect an unbinned basis-expansion inference strategy for extracting latent parameters.
- Prepared a real-data signal sample end to end, including reconstruction, event selection, and statistical background subtraction, so the method could be tested on realistic inputs rather than idealised samples.
- Contributed within a broader collaborative method effort by connecting the weighting-function idea to fit-ready inputs, covariance-aware validation, pseudoexperiments, and robustness studies required for a full joint measurement.

### Learning TensorFlow by extending an existing codebase
- Started with no TensorFlow knowledge and reviewed code supplied from a related project to understand and adapt it for the joint gamma measurement.
- Added new physical amplitude models and numerical components for efficiency, resolution and measurement bias to describe real-data measurement effects.
- Generated simulated data with the new model and used it to verify the adapted code.

### Taking responsibility for a shared GPU workstation
- Before this project, my Linux experience was as an individual user; GPU computing and multi-user administration were new to me.
- The experiment assigned a GPU workstation for my use and management, shared with other users. Workstation setup took **half a day**.
- Migrating the TensorFlow code to the workstation and obtaining a successful GPU run took **a further half-day**.
- These two timings cover workstation setup and code migration. The TensorFlow learning, model-development and code-verification work formed a separate part of the project.

### Transferable contribution
Understanding unfamiliar software, extending it with domain-specific models, checking changes with simulated inputs and taking responsibility for a usable shared computing environment.

### Result
- Helped turn a novel inference idea into a realistic analysis workflow instead of leaving it as a purely formal method proposal.
- Anchored the method in practical validation work: weighted Fourier observables, joint fitting over latent parameters, and explicit checks under background, efficiency, resolution, and higher-order modelling variations.

### Publications & Reports
- Publication: *Measurement of the CKM angle γ in B± → D(→ KS0h′+h′−)h± decays with a novel approach*. DOI: [10.48550/arXiv.2604.05701](https://doi.org/10.48550/arXiv.2604.05701)
- Publication: *Precise measurement of the CKM angle γ with a novel approach*. DOI: [10.48550/arXiv.2604.05712](https://doi.org/10.48550/arXiv.2604.05712)
