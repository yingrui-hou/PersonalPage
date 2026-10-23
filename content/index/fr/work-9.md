---
number: 09
homepage_order: 2
collapsible: true
title: Calibration de la confiance d’un classificateur
tags: Calibration | Écarts de distribution | Validation sur données
methods: contrôles sur données réelles, calibration du marquage de saveur, revue collaborative
impact: calibration et validation d’un modèle de marquage de saveur pour l’analyse physique.
industry: ML appliqué | Validation de modèles | Analyse scientifique
---
Calibration des probabilités d’erreur estimées par un classificateur à partir de mesures de référence, puis vérification par simulation.

### Problème
Le classificateur était entraîné sur une simulation dont les distributions différaient des données réelles. Ses probabilités d’erreur devaient être calibrées pour l’analyse cible.

### Ma contribution
- Choix de processus de référence dont les classes sont identifiables et contrôle de leur pertinence pour les données cibles.
- Alignement des distributions d’entrée importantes par repondération lorsque nécessaire.
- Ajustement de la relation entre probabilités d’erreur prédites et observées, puis application de la correction à l’analyse cible.

### Validation et résultat
Vérification de la calibration par une simulation cible repondérée : les estimations d’erreur concordaient dans les incertitudes. Ma contribution portait sur la calibration et la validation, avec participation aux discussions sur l’entraînement. Je n’ai pas entraîné ce modèle. La calibration reste propre au processus cible et aux conditions des données de référence.
