---
number: 07
homepage_order: 6
collapsible: true
title: Modernising an extensible C++ toolkit
tags: C++ | Interfaces | Framework Integration
methods: existing-toolkit extension, method design, framework integration, testing
impact: delivered an upgraded toolkit used in subsequent project simulation samples and extended by collaborators.
industry: Simulation Platforms | Scientific Computing | Software Integration
---
Modernised QCFilter, a simulation toolkit shared within the experimental collaboration, and added a reusable interface for custom models.

### Problem
The legacy code had known defects, used an older implementation and supported a restricted modelling case. New studies needed a maintainable way to add models.

### My contribution
- Rewrote the toolkit using a newer C++ standard and the Gaudi framework.
- Designed a common model interface and added support for several physics processes.
- Handled method design, implementation, Gaudi/BOSS integration and final testing.

### Validation and result
Compared old and new simulation results, with agreement in the checks performed. Compared key simulated distributions with real data; residual differences reflected model limitations. The toolkit was used for subsequent project simulations and extended by collaborators. Source code is shared internally within the experiment.

### Publications

*CP violation studies at Super Tau-Charm Facility*, [DOI](https://doi.org/10.48550/arXiv.2502.08907).
