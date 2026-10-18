---
number: 02
homepage_order: 5
collapsible: true
title: Inférence temporelle et correction des biais
tags: Inférence temporelle | Calibration | Ajustements conjoints
methods: Modélisation de l’acceptance, calibration de résolution, repondération
impact: Corrections propres aux jeux de données et propagation des incertitudes résiduelles.
industry: Estimation de paramètres | Modèles dynamiques latents
---
**Construction d’une chaîne d’inférence temporelle corrigée des effets de sélection, de résolution et des écarts simulation-données.**

![Effets de reconstruction sur la distribution temporelle](assets/selected-work/work-2/time_rec_eff.png "La reconstruction modifie la sensibilité à la structure temporelle.")

### Réalisation personnelle
- Modélisation explicite de l’acceptance et de la résolution ; corrections distinctes pour Run 1 et Run 2.
- Alignement des échantillons de signal et de contrôle par repondération avec gradient boosting.
- Composants d’ajustement réutilisables pour la masse, le temps de vie, l’efficacité et la résolution.

![Chaîne d’analyse](assets/selected-work/work-2/workflow.png "Des données aux observables latentes.")

### Résultat
Les écarts de modélisation résiduels sont traités comme des incertitudes quantifiées, avec des hypothèses explicites et vérifiables. Ces méthodes apportent des compétences transférables en estimation ; elles ne constituent pas une expérience de prévision industrielle.
