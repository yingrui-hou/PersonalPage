---
number: 09
homepage_order: 2
collapsible: true
title: Calibration de modèles d’apprentissage profond
tags: Apprentissage profond | Calibration | Données réelles
methods: contrôles sur données réelles, calibration du marquage de saveur, revue collaborative
impact: calibration et validation d’un modèle de marquage de saveur pour l’analyse physique.
industry: ML appliqué | Validation de modèles | Analyse scientifique
---
**Calibration des probabilités de mauvais marquage pour l’analyse Bs → φγ, à partir de canaux de référence dans les données et d’une vérification par simulation.**

### Problème et domaine d’application
Le modèle fournissait une décision de saveur (−1, 0 ou +1) et une probabilité estimée de mauvais marquage comprise entre 0 et 0,5. Son entraînement reposait sur des échantillons simulés d’un processus particulier. Les écarts simulation-données nécessitaient une calibration. Ces écarts dépendent du processus cible : la calibration ne peut pas être supposée universelle.

### Contribution personnelle
- Choix de **B+ → J/ψ K et Bs → Ds π** comme canaux de calibration, selon les caractéristiques du tagger et du signal cible.
- Vérification préalable des distributions cinématiques clés ; **repondération par gradient boosting** si nécessaire pour rapprocher les échantillons de référence du signal, la réponse du modèle dépendant de la cinématique.
- Utilisation des informations de saveur issues des charges et nombres quantiques de l’état final reconstruit. Comparaison avec les décisions du modèle, puis **ajustement de la relation entre probabilités prédites et taux de mauvais marquage observés**, appliquée au signal.
- **Vérification avec une simulation du signal repondérée vers la cinématique attendue dans les données. Les estimations étaient compatibles dans leurs incertitudes**, ce qui étaye la fiabilité de la calibration pour cette analyse.
- Participation aux discussions de construction et d’entraînement en vue de la calibration et de la validation ; sans réalisation de l’entraînement du modèle.

### Transfert vers l’ingénierie
Choisir des données de référence pertinentes, traiter les différences de distribution avant le transfert d’une calibration, ajuster la confiance du modèle et la confronter à la simulation. Le résultat soutient l’analyse considérée, sans établir une calibration universelle ou l’absence de tout biais résiduel.
