# Shortlist de postes ciblés: Data Scientist (industrie / R&D)

Date de vérification (Europe/Paris): `2026-04-24` (dernière vérification: `11:34` CEST)

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit/Send/Envoyer” visible).

## Positionnement & logique de tri (rappel)

- Angle candidat (preuves dans ce repo, notamment `resume.html`): `modélisation probabiliste`, `calibration/correction`, `validation sous bruit/biais`, `domain shift`, pipelines `Python/C++/ROOT` + discipline de reproductibilité.
- Cible: Data Scientist *industrial/ops/physical-systems adjacent* quand possible (énergie, monitoring, séries temporelles, optimisation, capteurs), en évitant BI/reporting pur.
- Déprioriser: BI/dashboards sans contenu modèle/validation; DS “marketing/CRM”; rôles purement consulting “génériques” sans ownership technique.

### Priorités

- `A` = DS orienté systèmes/monitoring/industrial + transfert direct
- `B` = DS intéressant mais plus senior / plus “business” / management
- `C` = DS OK mais moins “industrial/physical systems” (fallback)

---

## Bucket A — priorité haute

### A1. Kayrros — Senior Data Scientist F/H (Paris, Hybrid)

- Liens (vérifiés le `2026-04-24`):
  - Offre + candidature (formulaire “Send” visible sur la page): https://kayrros1.recruitee.com/o/senior-data-scientist-fh
- Pourquoi c’est un fit:
  - “Monitoring / risk & environmental” sur données imparfaites (satellite imagery + signaux) → bon terrain pour ton axe `validation/robustesse/calibration` sur systèmes de mesure.
  - “Full pipeline” (scoping → features → modèles → tests → produit) compatible avec ton expérience de workflows reproductibles.
- Risque/gap principal:
  - Domaine remote-sensing/computer vision (selon missions) + attentes “Senior” → cadrer honnêtement l’expérience, mettre l’accent sur rigueur de validation + interprétation de signaux bruités.

#### CV title (tailored)

`Data Scientist — Validation & calibration under uncertainty (industrial monitoring, Python/C++)`

#### Summary (tailored)

Data scientist orientée crédibilité modèle, avec un background en physique expérimentale: je construis et valide des modèles sur des données bruitées/biaisées (peu de vérité terrain), via calibration/correction, stress tests et diagnostics reproductibles.
Je vise des sujets monitoring/risque/environnement où l’incertitude et la qualité des mesures sont centrales.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python/ROOT` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
2. Implemented likelihood-based models and joint fits to estimate latent parameters under mismatch, finite resolution, and biased observations.
3. Developed calibration/correction workflows to reduce structured bias and compare before/after performance across operating conditions.
4. Built monitoring/validation pipelines that surfaced anomalies and supported root-cause diagnosis; drove concrete follow-up actions.
5. Aligned simulated and observed datasets through gradient-boosting reweighting and control-sample calibration before downstream decisions.
6. Ran sensitivity analyses and robustness checks; communicated uncertainty and limitations clearly to stakeholders.

---

## Bucket B — bon fit avec gap réel

### B1. Bigblue — Senior Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-24`):
  - Offre (Lever): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a/apply
- Pourquoi c’est un fit:
  - Problèmes ops/qualité de décision sous données imparfaites → valorise ton axe “validation robuste + monitoring + biais/shift”.
  - Place pour une posture “rigueur scientifique + diagnostic” plutôt que BI.
- Risque/gap principal:
  - Poste affiché “Senior” → cadrer l’ownership sur la rigueur validation + expérimentation + métriques, et être claire sur la séniorité.

#### CV title (tailored)

`Data Scientist — Robust validation & monitoring for real-world ops (Python/C++)`

#### Summary (tailored)

Data scientist orientée production/ops, spécialisée dans la validation et la calibration de modèles sur données réelles imparfaites (bruit, biais, shift), avec des workflows `Python/C++` reproductibles.
Je transforme des écarts observés en diagnostics et garde-fous (monitoring, stress tests, corrections).

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Implemented robustness checks under bias and dataset shift; quantified sensitivity to modeling assumptions and failure modes.
2. Built monitoring/validation workflows that exposed anomalies and supported root-cause diagnosis (system vs software vs data).
3. Developed calibration/correction workflows to reduce structured bias; quantified before/after improvements.
4. Built reproducible pipelines with traceable outputs and documented checks for reliable comparisons across iterations.
5. Aligned simulated and observed datasets via reweighting and control-sample calibration to mitigate mismatch.
6. Communicated uncertainty and limitations clearly to keep decisions aligned with evidence.

### B2. Octopus Energy France — Lead Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-24`):
  - Offre (Lever): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429/apply
- Pourquoi c’est intéressant:
  - Secteur énergie + contexte data → possibilité de valoriser validation, expérimentation, et “impact mesuré”.
  - Formulaire de candidature très explicite (motivation/forces/mobilité/salaire) → candidature actionnable.
- Risque/gap principal:
  - Poste “Lead” (management) + orientation potentiellement “commercial/customer” → vérifier la proportion de travail technique vs leadership.

#### CV title (tailored)

`Data Scientist — Model credibility & validation under uncertainty (energy context)`

#### Summary (tailored)

Profil data orienté crédibilité: je rends des modèles exploitables sur données réelles via calibration/correction, validation robuste, diagnostics et monitoring.
Je vise des équipes où la rigueur de validation compte autant que la performance nominale, idéalement en contexte énergie/systèmes.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Designed robust validation under mismatch/shift; prevented overconfident conclusions in noisy regimes.
2. Developed calibration/correction workflows with quantified before/after improvements across operating conditions.
3. Built monitoring pipelines that surfaced anomalies and drove corrective actions (data, model, or software fixes).
4. Implemented probabilistic inference (likelihood-based models, joint fits) under imperfect observations.
5. Delivered reproducible workflows in shared codebases with review discipline and documented checks.
6. Communicated uncertainty and trade-offs clearly to stakeholders to keep decisions aligned with evidence.

---

## Bucket C — fallback (moins “industrial/physical systems”)

### C1. BlaBlaCar — Data Scientist - Entry Level (Paris, Hybrid)

- Liens (vérifiés le `2026-04-24`):
  - Offre (Lever): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d/apply
- Pourquoi c’est potentiellement intéressant:
  - Place pour ton axe “validation + monitoring + diagnostic” sur systèmes ML en prod.
- Risque/gap principal:
  - Domaine plutôt “trust/content moderation/GenAI” (moins industrial/physical systems) → candidature seulement si tu acceptes cet éloignement.

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
5. Communicated uncertainty and trade-offs clearly to prevent overconfident decisions.
6. Built reusable `Python/C++` tooling that made iterative debugging and validation faster and safer.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — fermés / page indisponible

- Cognite — Senior Data Scientist (Pau / France): le chemin officiel de candidature renvoie `404` au moment de la vérification (`2026-04-24`) → **exclu** (statut “apply” non vérifiable).
  - Offre: https://jobs.lever.co/cognite/a8a52bd2-15b2-45ec-b365-88659119beb0
  - Candidature (404 au check): https://jobs.lever.co/cognite/a8a52bd2-15b2-45ec-b365-88659119beb0/apply

### Exclus — “apply” non vérifiable (erreur tool / statut ambigu)

- Kraken — Data Scientist in Power Electrical Systems (Paris): offre repérée mais impossible d’ouvrir de façon fiable la page / le chemin “apply” au moment de la vérification (`2026-04-24`) → **exclu**.
  - Offre (repérée): https://jobs.lever.co/kraken123/ba4edb2f-7417-42b3-b09d-07ed92d869b9

### Exclus — hors-cible (exemples)

- Veepee — Data Scientist / Senior Data Scientist: rôle centré recommandation/pricing e-commerce (moins industrial/R&D / physical-systems adjacent) → exclu.
  - Offres: https://jobs.lever.co/veepee/1490a34b-351a-4bfb-8b80-97419e9d2dcb

- Ekimetrics — Junior business data scientist (Marketing & commercial effectiveness): orientation marketing/commercial → hors-track.
  - Offre: https://jobs.lever.co/ekimetrics/6b4c0434-5e26-45c6-94a3-ab9946ab2485

- Valeuriad — Data Scientist Expérimenté (Nantes, hybride): ESN/mission générique (IA générative/chatbot + “LLM as a judge”) sans ancrage systèmes physiques → hors-track.
  - Offre: https://valeuriad.recruitee.com/o/data-scientist-experimente-1?lang=fr

- Theodo Data — Lead Data Engineer (Paris, hybride): rôle data engineering/consulting plutôt que data scientist → hors-track.
  - Offre: https://jobs.lever.co/theodo/05e18476-381b-4fd9-bc8a-11a6741e16a3
