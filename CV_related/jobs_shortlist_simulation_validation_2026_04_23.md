# Shortlist de postes ciblés: Simulation / Validation / R&D systèmes physiques

Date de vérification (Europe/Paris): `2026-04-23`

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit/Send/Envoyer” visible).

## Positionnement & logique de tri (rappel)

- Cible: `ingénierie simulation/validation` + `scientific software` pour systèmes physiques instrumentés (calibration, validation, corrélation essai↔modèle, root-cause).
- Angle candidat (preuves dans le repo): workflows `Python/C++` réutilisables, validation sous bruit/biais, calibration/correction, simulation↔mesure, diagnostics menant à actions.
- Déprioriser: `meshing/SALOME/geometry-kernel`, “FEA/maillage” centré construction du modèle mécanique, et backend générique sans angle systèmes physiques.

### Priorités

- `A` = fit direct + transfert très clair
- `B` = bon fit mais gap (stack/domaine/seniority)
- `C` = stretch assumé (domaine très différent / prérequis manquants)

---

## Bucket A — priorité haute

### A1. Outsight — Customer Validation Engineer (Paris, Hybrid)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3/apply
- Pourquoi c’est un fit:
  - Validation “terrain” et critères d’acceptation (requirements → acceptance criteria, test plan) + analyse de résultats: mapping direct vers ton axe `validation/calibration/diagnostic`.
  - Python scripting + métriques + traçabilité = très cohérent avec tes workflows reproductibles sur données bruitées/biaisées.
- Risque/gap principal:
  - Composante delivery/client + déplacements + coordination multi-équipes: il faut cadrer ton “ownership” sur plan de validation, reporting, et clôture d’actions.

#### CV title (tailored)

`Ingénieure validation & acceptance testing (Python/C++) — systèmes physiques / capteurs`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la **validation** et la **calibration/correction** de modèles/outils sur données de mesure bruitées, via des pipelines reproductibles en `Python/C++`.
Je transforme des écarts observés (mismatch, biais, anomalies) en diagnostics et actions concrètes (corrections, critères d’acceptation, monitoring), avec une approche orientée résultats et traçabilité.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Defined measurable validation criteria and produced decision-facing test outputs under noise, bias, and limited ground truth.
2. Built reusable `Python/C++/ROOT` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
3. Developed calibration/correction workflows (`ROOT/C++`) to reduce structured bias and quantify before/after improvements across regimes.
4. Built monitoring/validation pipelines that surfaced anomalies and supported root-cause diagnosis (system vs software vs data), triggering follow-up actions.
5. Aligned simulated and observed datasets via control-sample calibration and gradient-boosting reweighting to mitigate mismatch.
6. Communicated limitations and uncertainty clearly to technical stakeholders to keep decisions aligned with evidence (traceability, stress checks).

---

## Bucket B — bon fit avec gap réel

### B1. Fairmat — Software Engineer - Robotics (Paris ou Bouguenais, Hybrid)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091/apply
- Pourquoi c’est intéressant:
  - “C++/Python + tests + validation sur cellules robotiques industrielles” = très proche d’un rôle systèmes physiques (software + terrain + non-régression).
  - Le job mentionne explicitement mise en place de tests unitaires/fonctionnels + test en labo/usine + analyse des données pour correctifs: aligné avec ton axe `validation/diagnostic`.
- Risque/gap principal:
  - Pré-requis forts en `ROS`/robotique (Gazebo/RViz) + 3 ans d’expérience: il faut assumer un gap et te positionner sur “validation/robustesse + intégration capteurs + investigation de défauts”.

#### CV title (tailored)

`Scientific software / validation engineer (C++/Python) — tests, diagnostic, systèmes instrumentés`

#### Summary (tailored)

Ingénieure orientée fiabilité des systèmes: je construis des workflows `C++/Python` testables et traçables pour relier modèles/logiciels et comportements observés via mesures, puis transformer les écarts en actions (correctifs, garde-fous, tests).
Je peux contribuer sur la partie “validation & diagnostic” et sur l’outillage de non-régression, tout en restant factuelle sur un gap `ROS`.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation workflows that surfaced anomalies and supported root-cause diagnosis (system vs software vs data).
2. Delivered reproducible pipelines with documented checks enabling reliable reruns and comparisons (traceability, sanity checks).
3. Developed calibration/correction tooling with quantified before/after improvements across operating conditions.
4. Produced decision-facing validation outputs (metrics, acceptance criteria, failure modes → corrective actions).
5. Implemented robust testing mindset: isolate failure modes, add regression guards, and prevent overconfident conclusions under noise/shift.
6. Worked in shared codebases (Git/review discipline) and shipped reusable components used by other teams.

### B2. Alice & Bob — Workflow Engineer - Calibration (H/F) (Paris, Hybrid)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070/apply
- Pourquoi c’est intéressant:
  - Sujet “calibration workflow / DAG orchestration / recovery / HIL” = très proche de ton axe “rendre un système mesuré exploitable via validation + correction + boucles d’investigation”.
  - Leur besoin explicite de robustesse (idempotence, retries, observability) + tests = bon terrain pour ton approche “validation crédible”.
- Risque/gap principal:
  - Seniority affichée (>= 5 ans) + exigence workflow/DAG framework: tu dois cadrer ton niveau d’expérience sur l’ownership logiciel et la discipline de validation (sans sur-vendre).

#### CV title (tailored)

`Ingénieure calibration & validation — workflows robustes (Python/C++)`

#### Summary (tailored)

Scientific software engineer orientée calibration/validation: je construis des pipelines `Python/C++` reproductibles qui relient mesures bruitées et modèles via calibration/correction, stress tests et diagnostics.
Je peux contribuer à transformer des procédures “fragiles” en workflows robustes (checks, métriques, traceabilité), tout en restant factuelle sur un gap “orchestration DAG” si nécessaire.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` workflows to validate and calibrate models on noisy measurements with limited ground truth.
2. Implemented robustness checks and stress tests under mismatch/shift; quantified sensitivity to assumptions.
3. Developed calibration/correction tooling to reduce structured bias and compare before/after performance across regimes.
4. Built monitoring/validation that surfaced anomalies and supported root-cause diagnosis; drove concrete follow-up actions.
5. Delivered traceable outputs (config/versioning, repeatable runs) to support audits, reruns, and reliable comparisons.
6. Collaborated in large shared codebases with review discipline; documented procedures and validation criteria for reuse.

---

## Bucket C — stretch assumé

### C1. MaiaSpace — Flight Engineering Software Development and Validation Engineer (Paris — La Défense, On-site)

- Liens (vérifiés le `2026-04-23`):
  - Offre + candidature (ATS MaiaSpace, bouton “Send” visible sur la page): https://careers.maia-space.com/o/flight-engineering-software-development-and-validation-engineer?lang=en
- Pourquoi c’est un fit “technique”:
  - 6DoF flight simulation + intégration modèles physiques + campagnes de simulation + validation GNC: coeur simulation/validation.
  - Stack affichée `Matlab`, `C/C++`, `Python`: ton angle “scientific software + validation” reste crédible.
- Risque/gap principal:
  - Pré-requis “5–7 years experience” + domaine spatial/GNC: vrai gap seniorité/domaine → candidature seulement si tu acceptes une posture “adjacent / learning curve”.

#### CV title (tailored)

`Ingénieure simulation & validation (Python/C++) — corrélation modèle↔mesure, diagnostics`

#### Summary (tailored)

Ingénieure simulation/validation issue de la physique expérimentale: je construis des workflows `Python/C++` qui relient simulation et données de mesure via calibration/correction, stress tests et diagnostics reproductibles.
Je peux contribuer à structurer des suites de simulation et des campagnes de validation (critères, métriques, exploitation des écarts), tout en restant factuelle sur un gap GNC.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` scientific workflows to run simulation studies, validation checks, and sensitivity analyses with traceable outputs.
2. Aligned simulated and observed datasets via calibration and reweighting to mitigate mismatch; quantified impact on conclusions.
3. Developed calibration/correction tooling to reduce structured bias and compare performance before/after across operating conditions.
4. Implemented likelihood-based models and joint fits under finite resolution and biased observations; added robustness/stress checks.
5. Built monitoring/validation that surfaced anomalies and supported root-cause diagnosis (model vs data vs software).
6. Communicated uncertainty and limitations clearly to keep engineering decisions aligned with evidence.

### C2. Alice & Bob — Senior Software Engineer - Calibration Software (Paris, Hybrid)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/b7386caa-70dd-4670-bb69-a5c97322332f
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/alice-bob/b7386caa-70dd-4670-bb69-a5c97322332f/apply
- Pourquoi c’est intéressant:
  - Sujet “calibration automatique + CI/CD + integration avec hardware control” = cohérent avec ton axe “calibration/validation sous contraintes réelles”.
- Risque/gap principal:
  - Poste explicitement “Senior” + attentes architecture/CI/CD ownership: à candidater si tu acceptes un risque de séniorité et peux cadrer ton impact sur la partie validation/outillage.

#### CV title (tailored)

`Scientific software engineer — calibration/validation pipelines (Python/C++)`

#### Summary (tailored)

Scientific software engineer orientée crédibilité modèle: je rends des pipelines de calibration/validation robustes et traçables sur des données imparfaites, en intégrant stress tests, checks et diagnostics reproductibles.
Je me positionne sur la partie “qualité, validation, outillage, correction” et je reste factuelle sur un gap potentiel “senior architecture”.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `Python/C++` workflows for calibration and validation under noisy measurements and imperfect observability.
2. Developed calibration/correction tooling with quantified before/after improvements across conditions.
3. Implemented monitoring/validation that surfaced anomalies and supported root-cause diagnosis; closed the loop with corrective actions.
4. Designed robustness checks under mismatch/shift to prevent overconfident conclusions.
5. Delivered reproducible pipelines with configuration/versioning and documented checks for reliable reruns.
6. Collaborated in shared codebases with review discipline and delivered reusable components.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — non-France-first

- Hypersonica — Software Verification Test Engineer (GNC): poste localisé **Munich** (On-site) → non “France-first” → exclu.
  - Offre: https://jobs.lever.co/hypersonica-prod/dad56d98-7693-4c47-b954-5b3bf8e45f0e

### Exclus — “apply” non vérifiable (erreur tool / statut ambigu)

- Alice & Bob — Calibration API Software Engineer: page offre accessible, mais le chemin `/apply` n’a pas pu être ouvert de façon fiable (erreur “cache miss” au moment de la vérification) → **exclu**.
  - Offre: https://jobs.lever.co/alice-bob/b40a5281-ac51-439f-b690-0a30b0e9ced2

### Exclus — hors-cible (exemples)

- Postes “simulation mécanique / maillage / CFD” (SmartRecruiters/ESN) axés ANSA/StarCCM+/Abaqus/maillage → hors-axe `validation/calibration/simulation↔mesure` → exclus.

