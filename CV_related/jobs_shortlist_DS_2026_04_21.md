# Shortlist de postes ciblés: Data Scientist (industrie / R&D)

Date de vérification (Europe/Paris): `2026-04-21`

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit application” visible).

## Positionnement & logique de tri (rappel)

- Angle candidat (preuves dans le repo): `modélisation probabiliste`, `calibration/correction`, `validation sous bruit/biais`, `domain shift`, pipelines `Python/C++` + discipline de reproductibilité.
- Cible: Data Scientist *industrial/ops/physical-systems adjacent* quand possible (capteurs, systèmes, séries temporelles, monitoring, optimisation opérationnelle), en évitant BI/reporting pur.
- Déprioriser: BI/dashboards sans contenu modèle/validation; DS “marketing/CRM” non technique; rôles nécessitant une expertise forte en optimisation/MPC si non justifiable.

### Priorités

- `A` = DS orienté problèmes “terrain” (ops/énergie/systèmes) + transfert direct
- `B` = DS intéressant mais plus “business”/plus senior
- `C` = stretch (seniority fort ou domaine trop éloigné)

---

## Bucket A — priorité haute

### A1. Bigblue — Senior Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-21`):
  - Offre (Lever): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a/apply
- Pourquoi c’est un fit:
  - Problèmes “ops” (ETA, algos logistiques, optimisation réseau, monitoring) → plus proche d’un contexte systèmes/contraintes qu’un DS purement marketing.
  - Python/SQL + expérimentation + modèles “utilisables” en production: bon terrain pour ton angle “validation/robustesse”.
- Risque/gap principal:
  - Rôle “Senior” (ils indiquent 5–10 ans): à traiter franchement; cadrer ta séniorité sur “ownership technique + rigueur de validation”.

#### CV title (tailored)

`Data Scientist — Validation & robust pipelines for real-world operations (Python/C++)`

#### Summary (tailored)

Data scientist orientée R&D/ops avec un background en physique expérimentale, spécialisée dans la validation et la calibration de modèles sur données bruitées et biaisées, sans vérité terrain directe.
Je construis des pipelines `Python/C++` reproductibles et des diagnostics qui transforment les écarts en actions (corrections, monitoring, garde-fous).
Je vise des équipes où l’enjeu est de rendre des modèles fiables sur données réelles (shift, drift, mismatch) et de mesurer l’impact.

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

- Liens (vérifiés le `2026-04-21`):
  - Offre (Lever): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429/apply
- Pourquoi c’est intéressant:
  - Secteur énergie + rôle data central. Même si le poste est “commercial/expérience client”, il peut permettre de valoriser rigueur de validation + industrialisation (selon mission réelle).
- Risque/gap principal:
  - Poste “Lead” avec management (≥5 ans, encadrement d’équipe) + contenu potentiellement très “commercial dashboards”: risque d’écart avec ton axe “industrial R&D / physical systems”.

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

## Bucket C — stretch / à tenter si tu veux élargir

(aucun rôle “C” retenu aujourd’hui: les autres pistes vérifiées n’avaient pas un statut “apply” confirmable au `2026-04-21`.)

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — fermés

- Kraken — Data Scientist in Power Electrical Systems (via Welcome to the Jungle en): page indiquant “This position is no longer available.” → exclu.
  - Offre: https://www.welcometothejungle.com/en/companies/kraken/jobs/data-scientist-in-power-electrical-systems_paris

### Exclus — “apply” non vérifiable (bloqué / dynamique / erreur)

- Safran Analytics — Data Scientist Health Monitoring: la page offre est accessible mais le chemin de candidature n’a pas pu être ouvert de façon fiable (erreur/cache) → exclu.
  - Offre: https://www.safran-group.com/fr/offres/france/chateaufort/data-scientist-health-monitoring-fh-164168
- Safran Engineering Services — Technical leader Data scientist F/H: page offre accessible, mais statut candidature non vérifiable (erreur/cache) → exclu.
  - Offre: https://www.safran-group.com/fr/offres/france/magny-hameaux/technical-leader-data-scientist-fh-115980
- Elax Energie — Data Scientist (CDI) (via Welcome to the Jungle): bouton “Postuler” visible mais pas de lien statique exploitable (flow dynamique) → statut dépôt non vérifiable → exclu.
  - Offre: https://www.welcometothejungle.com/fr/companies/elax-energie/jobs/data-scientist-cdi_paris
- Beamy — Data Scientist Junior: page offre accessible, mais la page `/apply` n’a pas pu être ouverte de façon fiable (erreur/cache) → exclu.
  - Offre: https://jobs.lever.co/Beamy/d186057b-3a20-4dfc-9cb3-a0e4f88ec3ac

### Exclus — hors-cible (exemples)

- DS assurance / tarification (non industriel/R&D): https://recrutement.axa.fr/nos-offres-emploi/19390
