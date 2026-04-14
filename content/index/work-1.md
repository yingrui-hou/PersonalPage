---
number: 01
homepage_order: 8
homepage_group: secondary
collapsible: true
title: Weak-Signal Inference
tags: Mixture Models | Maximum Likelihood | Feature Selection | Statistical Validation
methods: likelihood fitting, control-sample validation, production yield workflows
impact: turned rare-signal extraction into a reproducible workflow with stability checks and auditable validation logic.
industry: Rare Event Analytics | Anomaly Detection | Weakly Labeled Systems
---
**Built a reusable C++/Python/ROOT workflow for weak-signal extraction in data where background dominates and event-level truth is unavailable.**

![Weak-signal mass fit case 2](assets/selected-work/work-1/BToVG.png "A narrow signal peak is recovered from dominant background through an explicit signal-plus-background fit.")

### Problem
The analysis problem was to recover a weak signal from dominant combinatorial background without having reliable event-level truth labels. That makes simple cut-based counting fragile and forces the extraction logic to carry its own validation.

### Workflow
- Implemented signal-plus-background likelihood fits to separate rare signal from background and extract stable yields under low signal-to-noise conditions.
- Automated yield extraction, preselection, and branching-ratio cross-checks through analysis-production scripts and structured inputs rather than relying on one-off notebooks.
- Validated the strategy against a higher-yield control decay and monitored yield, width, and fit stability across runs and selection settings.

### Result
- Turned the mass-fit strategy into reusable production tooling rather than a one-off fit tuned to a single dataset.
- Demonstrated that the extraction logic was robust enough to support a dedicated branching-ratio measurement, which is a stronger validation than simply showing a visible peak.
