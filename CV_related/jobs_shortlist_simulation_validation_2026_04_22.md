# Shortlist de postes ciblés: Simulation / Validation / R&D systèmes physiques

Date de vérification (Europe/Paris): `2026-04-22`

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit/Send/Envoyer” visible).

## Positionnement & logique de tri (rappel)

- Cible: `ingénierie simulation/validation` + `scientific software` pour systèmes physiques instrumentés (calibration, validation, corrélation essai↔modèle, root-cause).
- Angle candidat (preuves dans le repo): workflows `Python/C++` réutilisables, validation sous bruit/biais, calibration/correction, simulation↔mesure, diagnostics menant à actions (fix logiciel, update calibration).
- Déprioriser: `meshing/SALOME/geometry-kernel`, “FEA/maillage” centré construction du modèle mécanique, et backend générique sans angle systèmes physiques.

### Priorités

- `A` = fit direct + transfert très clair
- `B` = bon fit mais gap (stack/domaine/seniority)
- `C` = stretch assumé (domaine très différent / prérequis manquants)

---

## Bucket A — priorité haute

### A1. Outsight — Customer Validation Engineer (Paris, Hybrid)

- Liens (vérifiés le `2026-04-22`):
  - Offre (Lever): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3/apply
- Pourquoi c’est un fit:
  - Rôle “validation terrain” (acceptance criteria, test plan, analyse résultats) directement aligné avec ton axe `validation/diagnostic` sur systèmes réels.
  - Python scripting + métriques + traduction d’exigences en critères mesurables: bon mapping de tes workflows de validation/calibration.
- Risque/gap principal:
  - Forte composante client/delivery + déplacements + coordination multi-équipes: il faut cadrer ta capacité à “faire tourner un plan de validation” de bout en bout.

#### CV title (tailored)

`Ingénieure validation & acceptance testing (Python/C++) — systèmes physiques / capteurs`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la **validation** et la **calibration** de modèles/outils sur données de mesure bruitées, via des pipelines reproductibles en `Python/C++`.
Je transforme des écarts observés (mismatch, biais, anomalies) en diagnostics et actions concrètes (corrections, critères d’acceptation, monitoring), avec une approche orientée résultats et traçabilité.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Defined measurable validation criteria and produced decision-facing test outputs under noise, bias, and limited ground truth.
2. Built reusable `Python/C++/ROOT` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
3. Developed calibration/correction workflows (`ROOT/C++`) to reduce structured bias and quantify before/after improvements across operating conditions.
4. Built monitoring/validation pipelines that exposed anomalies and supported root-cause diagnosis (system vs software vs data), triggering concrete follow-up actions.
5. Aligned simulated and observed datasets via control-sample calibration and gradient-boosting reweighting to mitigate mismatch.
6. Communicated limitations and uncertainty clearly to technical stakeholders to keep decisions aligned with evidence (traceability, stress checks).

### A2. MaiaSpace — Flight Engineering Software Development and Validation Engineer (Paris — La Défense, On-site)

- Liens (vérifiés le `2026-04-22`):
  - Offre (ATS MaiaSpace): https://careers.maia-space.com/o/flight-engineering-software-development-and-validation-engineer?lang=en
  - Candidature (formulaire + bouton “Send”, sur la même page): https://careers.maia-space.com/o/flight-engineering-software-development-and-validation-engineer?lang=en
- Pourquoi c’est un fit:
  - “6DoF flight simulation” + intégration de modèles physiques + campagnes de simulation + validation = coeur simulation/validation.
  - Stack mentionnée `Matlab`, `C/C++`, `Python`: ton angle “scientific software + validation” est crédible.
- Risque/gap principal:
  - Pré-requis affiché “5–7 years experience” + domaine spatial/GNC: c’est un vrai gap (à assumer) → candidature seulement si tu es OK de te positionner en “adjacent”.

#### CV title (tailored)

`Ingénieure simulation & validation (Python/C++) — corrélation modèle↔mesure, diagnostics`

#### Summary (tailored)

Ingénieure simulation/validation issue de la physique expérimentale: je construis des workflows `Python/C++` qui relient simulation et données de mesure via calibration/correction, stress tests et diagnostics reproductibles.
Je peux contribuer sur des suites de simulation et des campagnes de validation en structurant critères, métriques, et boucles “écart → hypothèse → test → correction”.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` scientific workflows to run simulation studies, validation checks, and sensitivity analyses with traceable outputs.
2. Aligned simulated and observed datasets via calibration and reweighting to mitigate mismatch; quantified impact on downstream conclusions.
3. Developed calibration/correction tooling to reduce structured bias and compare performance before/after across operating conditions.
4. Implemented likelihood-based models and joint fits under finite resolution and biased observations; added robustness/stress checks.
5. Built monitoring/validation that surfaced anomalies and supported root-cause diagnosis (model vs data vs software).
6. Delivered reusable components in shared codebases with reproducible runs and documented validation procedures.

### A3. Alice & Bob — Workflow Engineer - Calibration (H/F) (Paris, Hybrid)

- Liens (vérifiés le `2026-04-22`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070/apply
- Pourquoi c’est un fit:
  - Orchestration DAG + idempotence/retries + HIL + “recalibration” = mapping direct vers validation/calibration en boucle fermée.
  - Rôle orienté fiabilité et diagnostics plutôt que “juste coder”.
- Risque/gap principal:
  - Attentes “workflow systems” + production/fault-tolerance + 5+ ans: il faut cadrer ce que tu as réellement fait côté robustesse/monitoring.

#### CV title (tailored)

`Ingénieure workflows de calibration & validation (Python/C++) — systèmes physiques instrumentés`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la conception de workflows `Python/C++` pour calibration, validation et diagnostics sur données de mesure bruitées (sans vérité terrain directe).
J’apporte une culture “pipeline credibility” (métriques, stress tests, traçabilité) et des boucles de correction qui transforment des écarts en actions (calibration updates, bug fixes).

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built benchmark-based monitoring workflows to validate reconstruction/calibration quality and traced anomalies to detector behaviour or software issues.
2. Developed robust calibration & correction workflows (`ROOT/C++`) to reduce structured bias and compare performance before/after across operating conditions.
3. Built reusable `C++/Python/ROOT` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
4. Implemented uncertainty stress checks and sensitivity analyses to prevent overconfident conclusions under mismatch/shift.
5. Aligned simulation and observed datasets via control-sample calibration and gradient-boosting reweighting to avoid mismatch-driven bias.
6. Worked in large technical collaborations with shared codebases and review discipline; delivered reusable components and documented validation procedures.

---

## Bucket B — bon fit avec gap réel

### B1. Outsight — Unity Software Engineer (Paris, Hybrid)

- Liens (vérifiés le `2026-04-22`):
  - Offre (Lever): https://jobs.lever.co/outsight/b47fb2d1-376e-43eb-843a-ce580c053042
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/outsight/b47fb2d1-376e-43eb-843a-ce580c053042/apply
- Pourquoi c’est intéressant:
  - Simulation pour systèmes physiques (LiDAR) + focus performance + debugging = cohérent “validation/systèmes”, même si l’outil est Unity.
- Risque/gap principal:
  - Stack principale `Unity/C#` (et crowd simulation) vs ton cœur `C++/Python` + validation scientifique: risque de mismatch fort.

#### CV title (tailored)

`Scientific software engineer — simulation & validation workflows (Python/C++)`

#### Summary (tailored)

Scientific software engineer orientée simulation/validation: je conçois des pipelines reproductibles et des diagnostics qui relient modèles et données réelles, avec une approche rigoureuse de la performance, des tests et de la traçabilité.
Je reste factuelle sur un gap `Unity/C#` et je me positionne surtout sur la partie “validation + outils + métriques + debugging”.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation tooling to surface anomalies and support root-cause diagnosis (system vs software vs data).
2. Developed reproducible pipelines and documented checks in shared environments (versioned code, repeatable runs).
3. Implemented calibration/correction workflows with quantified before/after performance.
4. Produced decision-facing validation outputs with traceability (metrics, comparisons, failure modes → corrective actions).
5. Optimized scientific workflows to be reliable and reusable across many runs/conditions (automation, sanity checks).
6. Communicated technical findings clearly to cross-functional teams.

### B2. MaiaSpace — Modeling, Simulation, HIL & Embedded Code Generation Engineer (MATLAB/Simulink) (Paris — La Défense, On-site)

- Liens (vérifiés le `2026-04-22`):
  - Offre (ATS MaiaSpace): https://careers.maia-space.com/l/fr/o/modeling-simulation-hil-embedded-code-generation-engineer-matlabsimulink-expert?lang=fr
  - Candidature (formulaire + bouton “Envoyer”, sur la même page): https://careers.maia-space.com/l/fr/o/modeling-simulation-hil-embedded-code-generation-engineer-matlabsimulink-expert?lang=fr
- Pourquoi c’est intéressant:
  - MIL/SIL/PIL/HIL + validation + CI/CD + C/C++/Python: très proche des patterns “validation & workflows robustes”.
- Risque/gap principal:
  - Rôle “expert MATLAB/Simulink/Stateflow + codegen + HIL” et `5–10 ans` affichés: gap seniority/stack à assumer.

#### CV title (tailored)

`Ingénieure validation & calibration — workflows robustes (Python/C++)`

#### Summary (tailored)

Ingénieure orientée crédibilité modèle: je construis des workflows `Python/C++` de calibration/validation, avec stress tests, métriques et diagnostics reproductibles pour rendre des modèles exploitables sur données réelles.
Je peux contribuer sur la partie “plan de validation + outillage + checks”, tout en restant factuelle sur un gap `Simulink/HIL`.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built robust validation workflows and monitoring that turned discrepancies into concrete corrective actions.
2. Developed calibration/correction tooling with quantified before/after improvements across regimes.
3. Implemented reproducible scientific pipelines with documented checks, enabling reliable reruns and comparisons.
4. Performed sensitivity/robustness analyses under finite resolution, bias, and dataset mismatch.
5. Aligned simulation and measurement via control-sample calibration and reweighting to mitigate mismatch.
6. Delivered reusable components in shared codebases with review discipline.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — “apply” non vérifiable (bloqué / dynamique / erreur)

- MBDA France — RMO Simulation Intégration et Test Combat Collaboratif F/H (via WelcomeToTheJungle): lien “Postuler” redirigeant vers un intermédiaire (`jobstats.robopost.com`) dont le chemin vers l’ATS MBDA n’a pas pu être ouvert de façon fiable → **exclu**.
  - Offre: https://www.welcometothejungle.com/fr/companies/mbda-france-fr/jobs/rmo-simulation-integration-et-test-combat-collaboratif-f-h_le-plessis-robinson_MF_KeyGZJj
- Outsight — Senior System Integration Engineer (Lever): page offre OK, mais la page `/apply` n’a pas pu être ouverte de façon fiable (erreur/cache du fetch) → **exclu**.
  - Offre: https://jobs.lever.co/outsight/26f37bc5-b59b-42e8-80a1-117d59bec989

### Exclus — fermés

- Alice & Bob — Scientific Computational Engineer: page offre renvoyait une erreur (introuvable) au moment de la vérification → **exclu**.
  - Offre (non accessible): https://jobs.lever.co/alice-bob/35835b5e-c279-43de-b704-5bf038077d62

