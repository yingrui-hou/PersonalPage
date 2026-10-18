---
number: 03
homepage_order: 1
collapsible: true
title: Validation ML et adaptation de domaine
tags: CatBoost | Repondération | Validation des variables
methods: Entraînement CatBoost, diagnostics entraînement/test, gradient boosting
impact: Contrôle du surapprentissage et des différences de distribution dans une chaîne d’analyse reproductible.
industry: Machine learning appliqué | Décalage de distribution
---
**Construction d’une chaîne de validation ML et d’alignement d’échantillons pour des problèmes de sélection bruités.**

![Performance de sélection](assets/selected-work/work-3/bkg_veto_performance.png "Réduction du bruit de fond après sélection GBDT.")

### Réalisation personnelle
- Entraînement de classifieurs CatBoost et comparaison des réponses entraînement/test avant optimisation des seuils.
- Repondération des échantillons de calibration et de contrôle pour mieux représenter la cible.
- Intégration de la validation des scores, des études de seuils, des configurations et des modèles sauvegardés dans une chaîne cohérente.

![Validation entraînement/test](assets/selected-work/work-3/train-test.png "Comparaison des réponses pour les deux classes.")
![Importance des variables](assets/selected-work/work-3/feature_importance.png "Classement des variables après affinage du modèle.")

### Résultat
Les comparaisons entraînement/test et les contrôles de distribution étayent l’utilisation du classifieur dans l’analyse. L’expérience concerne une chaîne de recherche partagée.
