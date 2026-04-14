---
number: 07
homepage_order: 3
collapsible: true
title: Model Correction Workflow
tags: Scientific Software | Event Filtering | Simulation Correction | Framework Integration
methods: Gaudi-package development, event-level correction, framework integration
impact: turned measured constraints into a reusable event-level correction package for improving simplified simulation realism.
industry: Simulation Platforms | Scientific Computing | Model Correction
---
**Developed simulation-correction tooling that turns measured physics constraints into an event-level resampling workflow.**

### Problem
The simplified fast simulation was good enough for most kinematic behaviour, but it could not reproduce one paired-particle correlation effect needed downstream. A full first-principles simulation of the multi-body process was not practical, so measured constraints had to be folded back into the event distribution in an operational and auditable way rather than through ad hoc post-processing.

### Workflow
- Built a framework-integrated C++ package to correct inclusive fast-simulation samples event by event so that the missing correlation effect was restored.
- Encoded correction factors from measured inputs into a filtering workflow that keeps or rejects events to match the corrected distribution.
- Designed the package with headers, source files, job options, and framework integration points so the correction logic is reusable beyond a single analysis or software stack.

### Result
- Turned measured constraints into a reusable event-level correction package for improving simplified simulation realism.
- Kept the event-level behaviour explicit and auditable: each event receives a correction factor and is accepted or rejected through a simple stochastic rule, which makes the method portable, reviewable, and suitable for shared technical environments.
