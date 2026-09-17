# Shortlist de postes ciblés: Data Scientist (industrie / R&D)

Date de vérification (Europe/Paris): `2026-04-23`

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit” visible).

## Positionnement & logique de tri (rappel)

- Angle candidat (preuves dans le repo): `modélisation probabiliste`, `calibration/correction`, `validation sous bruit/biais`, `domain shift`, pipelines `Python/C++` + discipline de reproductibilité.
- Cible: Data Scientist *industrial/ops/physical-systems adjacent* quand possible (énergie, opérations, monitoring, séries temporelles, optimisation opérationnelle), en évitant BI/reporting pur.
- Déprioriser: BI/dashboards sans contenu modèle/validation; DS “marketing/CRM” non technique; consulting “générique” sans ownership technique.

### Priorités

- `A` = DS orienté problèmes “terrain” (ops/énergie/systèmes) + transfert direct
- `B` = DS intéressant mais plus senior / plus “business” / management
- `C` = DS OK mais moins “industrial/physical systems” (fallback)

---

## Bucket A — priorité haute

### A1. Bigblue — Senior Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a/apply
- Pourquoi c’est un fit:
  - Problèmes ops (ETA, algos logistiques, optimisation) → plus proche “systèmes/contraintes” qu’un DS purement marketing.
  - Espace pour ton angle “validation/robustesse sur données imparfaites” + itération expé → prod.
- Risque/gap principal:
  - Role “Senior” (ils affichent 5–10 ans): cadrer franchement ta séniorité sur ownership technique + rigueur de validation.

#### CV title (tailored)

`Data Scientist — Validation & robust pipelines for real-world operations (Python/C++)`

#### Summary (tailored)

Data scientist orientée R&D/ops avec un background en physique expérimentale, spécialisée dans la validation et la calibration de modèles sur données bruitées et biaisées, sans vérité terrain directe.
Je construis des pipelines `Python/C++` reproductibles et des diagnostics qui transforment les écarts en actions (corrections, monitoring, garde-fous).

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python/ROOT` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
2. Implemented robustness checks under bias, finite resolution, and dataset shift; quantified impact of modeling assumptions.
3. Built monitoring/validation workflows that exposed anomalies and supported root-cause diagnosis (system vs software vs data).
4. Developed calibration/correction workflows to reduce structured bias and compare before/after performance across operating conditions.
5. Aligned simulated and observed datasets via control-sample calibration and gradient-boosting reweighting to mitigate mismatch.
6. Produced decision-facing validation outputs that triggered concrete follow-up actions (software fixes, calibration updates, monitoring rules).

---

## Bucket B — bon fit avec gap réel

### B1. Octopus Energy France — Lead Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429/apply
- Pourquoi c’est intéressant:
  - Secteur énergie + possibilité de valoriser rigueur de validation, expérimentation, “impact mesuré”.
  - Leur formulaire demande explicitement motivations/forces/mobilité/salaire → candidature actionnable sans zone grise.
- Risque/gap principal:
  - Poste “Lead” (management) + Pod “Commercials” (ventes/marketing/expérience client): risque d’éloignement de l’axe R&D/physical-systems.

#### CV title (tailored)

`Data Scientist — Credible ML & validation under uncertainty (energy-context, Python/C++)`

#### Summary (tailored)

Profil data orienté crédibilité modèle: je rends des modèles exploitables sur des données réelles imparfaites via calibration/correction, validation robuste, et diagnostics reproductibles.
Je peux contribuer sur des sujets d’impact (prédiction, scoring, optimisation) à condition que le rôle valorise la rigueur de validation plus que le reporting.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Designed robust validation under dataset shift and mismatch; prevented overconfident results in noisy regimes.
2. Built calibration/correction workflows with quantified before/after improvements.
3. Implemented probabilistic inference (likelihood-based models, joint fits) under imperfect observations.
4. Built monitoring/validation that surfaced anomalies and drove concrete corrective actions.
5. Delivered reproducible pipelines (versioned code, documented checks) in shared environments.
6. Communicated uncertainty and limitations clearly to stakeholders to keep decisions aligned with evidence.

---

## Bucket C — fallback (moins “industrial/physical systems”)

### C1. Mistral AI — Data Scientist (Paris, On-site)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/mistral/bf5bcae2-839b-492e-a5bc-11d4427ee843
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/mistral/bf5bcae2-839b-492e-a5bc-11d4427ee843/apply
- Pourquoi c’est potentiellement intéressant:
  - Rôle “product / research / engineering” avec métriques + modèles + décisions: bon terrain pour ton axe “validation/robustesse”.
- Risque/gap principal:
  - Moins “industrie/physical systems” (plutôt produit AI). À candidater seulement si tu acceptes cette dérive.

#### CV title (tailored)

`Data Scientist — Model credibility & experimentation (Python/C++)`

#### Summary (tailored)

Data scientist orientée crédibilité modèle: je combine validation robuste, calibration/correction et diagnostics reproductibles pour rendre des modèles exploitables sur données réelles imparfaites.
Je sais structurer des métriques, des stress tests et des analyses d’écarts qui évitent des décisions sur-interprétées.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Designed robust validation checks under mismatch/shift; quantified sensitivity to assumptions.
2. Built reproducible `Python/C++` pipelines with traceable outputs and documented checks.
3. Implemented calibration/correction workflows with quantified before/after improvements.
4. Built monitoring and anomaly detection workflows that supported root-cause diagnosis.
5. Applied probabilistic inference and uncertainty-aware reporting to keep decisions aligned with evidence.
6. Communicated technical results to mixed audiences with clarity (what’s measured, what’s not, and why).

### C2. BlaBlaCar — Data Scientist - Entry Level (Paris, Hybrid)

- Liens (vérifiés le `2026-04-23`):
  - Offre (Lever): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d/apply
- Pourquoi c’est potentiellement intéressant:
  - “Ops + confiance” (automation, fraud/modération, production ML) → permet de valoriser rigueur validation + monitoring.
- Risque/gap principal:
  - Domaine plutôt NLP/modération + product growth, pas “physical systems”; à traiter en option seulement.

#### CV title (tailored)

`Data Scientist — Robust validation & monitoring for real-world ML (Python/C++)`

#### Summary (tailored)

Data scientist issue de la physique expérimentale, spécialisée dans la validation et la calibration de modèles sur données bruitées/biaisées, avec une approche “pipeline credibility” (stress tests, monitoring, diagnostics).
Je vise des équipes où la mise en production et la fiabilité des modèles comptent autant que la performance nominale.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation workflows that surfaced anomalies and supported root-cause diagnosis (system vs software vs data).
2. Implemented robustness checks under bias and dataset shift; quantified failure modes and limitations.
3. Developed calibration/correction workflows to reduce structured bias and compare before/after performance.
4. Delivered reproducible pipelines (versioned code, documented checks) enabling reliable comparisons across iterations.
5. Communicated uncertainty and trade-offs to stakeholders to prevent overconfident decisions.
6. Built reusable `Python/C++` tooling that made iterative debugging and validation faster and safer.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — fermés / page indisponible

- Cognite — Senior Data Scientist (Pau / France): la page offre renvoie `404` au moment de la vérification (`2026-04-23`) → **exclu**.
  - Offre (non accessible): https://jobs.lever.co/cognite/a8a52bd2-15b2-45ec-b365-88659119beb0

### Exclus — “apply” non vérifiable (erreur tool / statut ambigu)

- Aircall — AI Product Data Scientist: page offre accessible, mais la page `/apply` a renvoyé une erreur au moment de la vérification → **exclu** (statut “apply” non vérifiable).
  - Offre: https://jobs.lever.co/aircall/de9c770a-a7ea-4f15-a134-ea24701dcaeb

### Exclus — hors-cible (exemples)

- Veepee — Data Scientist / Senior Data Scientist: recommandation/pricing e-commerce (moins industrial/R&D / physical-systems adjacent) → exclu.

