# Shortlist de postes ciblés: Data Scientist (industrie / R&D)

Date de vérification (Europe/Paris): `2026-04-25` (dernière vérification: `09:36` CEST)

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit/Send/Envoyer” visible).

## Positionnement & logique de tri (rappel)

- Angle candidat (preuves dans ce repo, notamment `cv.md` / `resume.html`): `modélisation probabiliste`, `calibration/correction`, `validation sous bruit/biais`, `domain shift`, pipelines `Python/C++` + discipline de reproductibilité.
- Cible: Data Scientist *industrial/R&D ou physical-systems-adjacent* quand possible (énergie, monitoring, séries temporelles, optimisation, capteurs), en évitant BI/reporting pur.
- Déprioriser: BI/dashboards sans contenu modèle/validation; DS “marketing/CRM”; rôles purement consulting génériques sans ownership technique.

### Priorités

- `A` = DS orienté systèmes/monitoring/industrial + transfert direct
- `B` = DS intéressant mais plus éloigné / plus produit / moins “physical systems”
- `C` = stretch (niveau/seniority/management) ou domaine très éloigné

---

## Bucket A — priorité haute

### A1. Kayrros — Senior Data Scientist F/H (Paris, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre + candidature (formulaire “Send” visible sur la page): https://kayrros1.recruitee.com/o/senior-data-scientist-fh
- Pourquoi c’est un fit:
  - “Monitoring / risk & environmental” sur données imparfaites (mesures indirectes, peu de vérité terrain) → bon terrain pour ton axe `validation/robustesse/calibration`.
  - Pipeline complet (scoping → features → modèles → tests) compatible avec ton expérience de workflows reproductibles et de diagnostic.
- Risque/gap principal:
  - Domaine remote-sensing / computer vision possible + attentes “Senior” → cadrer honnêtement l’expérience; mettre l’accent sur rigueur de validation + interprétation de signaux bruités.

#### CV title (tailored)

`Data Scientist — Validation & calibration under uncertainty (monitoring, Python/C++)`

#### Summary (tailored)

Data scientist orientée crédibilité modèle, avec un background en physique expérimentale: je construis et valide des modèles sur des données bruitées/biaisées (peu de vérité terrain), via calibration/correction, stress tests et diagnostics reproductibles.
Je vise des sujets monitoring/risque/environnement où l’incertitude et la qualité des mesures sont centrales.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
2. Implemented likelihood-based models and joint fits to estimate latent parameters under mismatch, finite resolution, and biased observations.
3. Developed calibration/correction workflows to reduce structured bias and compare before/after performance across operating conditions.
4. Built monitoring/validation pipelines that surfaced anomalies and supported root-cause diagnosis; drove concrete follow-up actions.
5. Aligned simulated and observed datasets through reweighting / control-sample calibration to mitigate dataset shift before decisions.
6. Ran sensitivity analyses and robustness checks; communicated uncertainty and limitations clearly to stakeholders.

### A2. Bigblue — Senior Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre (Lever): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a/apply
- Pourquoi c’est un fit:
  - Problèmes “ops / décision sous contraintes” (ETA, optimisation logistique, monitoring near-real-time) → valorise ton axe “validation robuste + monitoring + biais/shift”.
  - Place pour une posture “rigueur scientifique + diagnostic” plutôt que BI/reporting.
- Risque/gap principal:
  - Poste affiché “Senior (5–10y)” → cadrer l’ownership sur rigueur validation + expérimentation, et être claire sur la séniorité.

#### CV title (tailored)

`Data Scientist — Robust validation & monitoring for real-world ops (Python/C++)`

#### Summary (tailored)

Data scientist orientée production/ops, spécialisée dans la validation et la calibration de modèles sur données réelles imparfaites (bruit, biais, shift), avec des workflows `Python/C++` reproductibles.
Je transforme des écarts observés en diagnostics et garde-fous (monitoring, stress tests, corrections) pour des décisions fiables.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Implemented robustness checks under bias and dataset shift; quantified sensitivity to assumptions and failure modes.
2. Built monitoring/validation workflows that exposed anomalies and supported root-cause diagnosis (system vs software vs data).
3. Developed calibration/correction workflows to reduce structured bias; quantified before/after improvements.
4. Delivered reproducible pipelines with traceable outputs and documented checks for reliable comparisons across iterations.
5. Designed feature selection / stability strategies to improve signal-to-noise ratio and prevent brittle models.
6. Communicated uncertainty and trade-offs clearly to keep operational decisions aligned with evidence.

---

## Bucket B — bon fit avec gap réel

### B1. BlaBlaCar — Data Scientist - Entry Level (Paris, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre (Lever): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d/apply
- Pourquoi c’est potentiellement intéressant:
  - Place pour ton axe “validation + monitoring + diagnostic” sur systèmes ML en prod (garde-fous, robustesse sous données imparfaites).
- Risque/gap principal:
  - Domaine plutôt “trust / fraude / content moderation / GenAI” (moins industrial/physical-systems-adjacent) → candidature seulement si tu acceptes cet éloignement.

#### CV title (tailored)

`Data Scientist — Robust validation & monitoring for real-world ML (Python/C++)`

#### Summary (tailored)

Data scientist issue de la physique expérimentale: j’apporte une rigueur de validation et de calibration sur données imparfaites, avec monitoring et diagnostics reproductibles pour réduire les erreurs silencieuses en production.
Je peux contribuer sur la partie “model credibility” et la boucle d’amélioration continue.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation workflows that surfaced anomalies and supported root-cause diagnosis (system vs software vs data).
2. Implemented robustness checks under bias and dataset shift; quantified failure modes and limitations.
3. Developed calibration/correction workflows to reduce structured bias and compare before/after performance.
4. Delivered reproducible pipelines (versioned code, documented checks) enabling reliable comparisons across iterations.
5. Implemented probabilistic modeling (likelihood-based inference) when uncertainty and imperfect observation dominated.
6. Communicated uncertainty and trade-offs clearly to prevent overconfident decisions.

---

## Bucket C — stretch assumé

### C1. Octopus Energy France — Lead Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre (Lever): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429/apply
- Pourquoi c’est intéressant:
  - Secteur énergie + sujets data → possibilité de valoriser validation, expérimentation, et “impact mesuré”.
- Risque/gap principal:
  - Poste “Lead” (management d’équipe + pod commercial/marketing) + prérequis affichés “5+ ans + 2 ans de management” → candidature seulement si tu acceptes un stretch management/seniority.

#### CV title (tailored)

`Data Scientist — Model credibility & validation under uncertainty (energy context)`

#### Summary (tailored)

Profil data orienté crédibilité: je rends des modèles exploitables sur données réelles via calibration/correction, validation robuste, diagnostics et monitoring.
Je vise des équipes où la rigueur de validation compte autant que la performance nominale — tout en assumant que ce rôle est un stretch “Lead/management”.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Designed robust validation under mismatch/shift; prevented overconfident conclusions in noisy regimes.
2. Developed calibration/correction workflows with quantified before/after improvements across operating conditions.
3. Built monitoring pipelines that surfaced anomalies and drove corrective actions (data, model, or software fixes).
4. Implemented probabilistic inference (likelihood-based models, joint fits) under imperfect observations.
5. Delivered reproducible workflows in shared codebases with review discipline and documented checks.
6. Communicated uncertainty and trade-offs clearly to keep decisions aligned with evidence.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — fermés / page indisponible

- Cognite — Senior Data Scientist (Pau / France): la page offre + le chemin “apply” renvoient `404` au moment de la vérification (`2026-04-25`) → **exclu**.
  - Offre (404 au check): https://jobs.lever.co/cognite/a8a52bd2-15b2-45ec-b365-88659119beb0

### Exclus — statut “apply” non vérifiable

- Kraken — Data Scientist in Power Electrical Systems (Paris): offre repérée précédemment mais impossible de vérifier la page / le chemin “apply” au moment du check (`2026-04-25`) → **exclu** (“apply” non vérifiable).
  - Offre repérée: https://jobs.lever.co/kraken123/ba4edb2f-7417-42b3-b09d-07ed92d869b9

### Exclus — hors-cible (exemples)

- Ekimetrics — Junior business data scientist (Marketing & commercial effectiveness): orientation marketing/commercial → hors-track.
  - Offre: https://jobs.lever.co/ekimetrics/6b4c0434-5e26-45c6-94a3-ab9946ab2485

- Veepee — Data Scientist / Senior Data Scientist: recommandation/pricing e-commerce (moins industrial/R&D / physical-systems-adjacent) → hors-track.
  - Offre: https://jobs.lever.co/veepee/1490a34b-351a-4bfb-8b80-97419e9d2dcb

