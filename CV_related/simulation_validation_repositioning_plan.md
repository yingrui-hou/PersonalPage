# CV Repositioning Plan: Simulation / Validation / Physical-Systems R&D

## Summary

Use one primary narrative: `Simulation/Validation Engineer for Physical Systems`, with `data science` kept as a supporting capability rather than the headline.

Primary artifacts and defaults:

- One main CV for France-first industrial/R&D applications, in French when the ad is in French.
- One English backup CV with the same positioning.
- Keep the current data-science-oriented version only as a secondary variant for clearly DS-heavy roles; do not lead with it.

Core message to carry across the CV:

- You build `C++/Python` workflows that make imperfect simulations and noisy measurements usable for engineering decisions.
- Your value is `simulation-to-measurement alignment`, `calibration`, `validation`, `correction workflows`, and `root-cause diagnosis`.
- You are not selling yourself as a generic analyst or generic ML profile.

## Key CV Changes

### 1. Headline and summary

Replace the current mixed `simulation + data science` framing with a clearer main title.

Recommended main title:

- French: `Ingénieure simulation & validation pour systèmes physiques`
- English: `Simulation & Validation Engineer for Physical Systems`

Summary structure:

- Line 1: background in experimental physics + reusable scientific workflows in `C++/Python`
- Line 2: strongest value = calibration, validation, simulation/measurement alignment, uncertainty-aware decisions
- Line 3: environments = physical systems, instrumented tests, simulation-informed engineering
- Line 4: data science appears only as an enabling toolset, not the role identity

### 2. Skills ordering

Reorder the skills section so the first screenful says “scientific software + simulation + validation,” not “analytics.”

Recommended order:

- `C++`, `Python`, `Geant4`, `ROOT / RooFit`, `Shell / CMake / YAML`
- `Model validation`, `Calibration & bias correction`, `Simulation-to-measurement alignment`, `Signal processing`
- `Probabilistic modelling`, `Statistical inference`, `Maximum likelihood`
- `CatBoost / gradient boosting`, `domain adaptation`, large-scale data analysis

Remove from the top layer:

- Any wording that makes you look like a broad business/data candidate first
- Overuse of `ML`, `data scientist`, `analytics`, `scikit-learn` before the simulation/validation story is established

### 3. Experience rewrite

Restructure experience around capability blocks, not around academic analysis categories.

Use two main blocks:

- `Scientific software, simulation & correction workflows`
- `Validation, calibration & test-data interpretation`

Within those bullets, prioritize evidence that signals industrial transfer:

- reusable `C++/Python` workflows
- framework integration
- shared codebases / review discipline
- calibration feeding software or model updates
- anomaly tracing leading to concrete fixes
- quantified outcomes

Downplay or compress:

- niche physics-goal wording
- publication-style problem framing
- rare-event or particle-physics-specific language when it does not help transferability

### 4. Evidence selection

Keep the proof points that best map to industrial R&D:

- Geant4/C++ simulation code with geometry/response logic
- beam-test + simulation + response-map integration
- ROOT/C++ correction/calibration workflows
- monitoring that exposed software and detector issues
- event-level correction tooling inside collaboration frameworks
- quantified outcomes: `<1%` non-uniformity contribution, `~2x` resolution improvement, downstream bug exposed and fixed

Do not invent or imply:

- meshing / computational geometry expertise
- HPC depth if not directly evidenced
- formal industrial employment if the evidence is really academic-collaboration work

## Application Strategy

### 1. Roles to target

Prioritize jobs with titles or content such as:

- `Ingénieur simulation`
- `Ingénieur validation / corrélation essai-simulation`
- `Ingénieur R&D systèmes physiques`
- `Scientific software engineer`
- `Model validation engineer`
- `Simulation & test-data analysis`
- `Calibration / measurement / model credibility` roles

Deprioritize or skip:

- pure meshing / SALOME / geometry-kernel roles
- pure commercial analytics / BI / dashboard data science
- pure MLOps / software backend jobs with no physical-systems angle

### 2. Company/team filter

Best-fit employers are teams working on:

- energy, nuclear, defense, aerospace testing, industrial instrumentation, sensors, medtech devices
- physical modelling, digital twins, test/simulation correlation, scientific software, advanced validation
- environments where simulation does not perfectly match measured behavior

### 3. Tailoring rule for each application

For each target ad, adapt only three elements:

- headline
- first 4-5 lines of summary
- top 6-8 bullets / skills ordering

Keep the base CV stable; do not rewrite the whole document each time.

Keyword rule:

- mirror the employer’s own wording for `validation`, `calibration`, `simulation`, `measurement`, `scientific software`, `test data`, or `model credibility`
- never mirror keywords you cannot substantiate

### 4. Funnel and prioritization

Use a three-bucket funnel:

- `70%` direct-fit simulation/validation roles
- `20%` adjacent scientific software roles
- `10%` stretch roles where your transfer story is strong but not obvious

When a role is more software-heavy:

- move `C++/Python`, workflow integration, and reusable tooling upward

When a role is more model/validation-heavy:

- move calibration, test-data interpretation, simulation-measurement alignment, and quantified outcomes upward

## Test Plan / Acceptance Criteria

A revised CV is acceptable only if all checks pass:

- In 10 seconds, a recruiter can classify you as `simulation/validation for physical systems`, not generic data science.
- The first half page contains `C++/Python + simulation + calibration/validation` before ML/analytics details.
- At least 3 bullets clearly show software implementation ownership, not only analysis ownership.
- At least 2 bullets show simulation tied to measured/test data.
- No top-section claim depends on meshing, SALOME, VTK, HPC, or formal industry experience you have not proven.
- For a French industrial recruiter, the document reads as `transferable to industry now`, not `excellent academic physicist looking for anything`.

## Assumptions and Defaults

- Main market is France-based industrial/R&D teams.
- Main identity is `Simulation/Validation Engineer`; `data science` remains a secondary strength.
- The primary deliverable is CV direction plus application strategy, not a homepage or cover-letter rewrite yet.
- Existing DS-oriented materials remain available but are not the default package.
