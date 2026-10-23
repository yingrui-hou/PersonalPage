---
number: 02
homepage_order: 5
collapsible: true
title: Modélisation temporelle
tags: Correction des biais | Calibration | Ajustement
methods: Modélisation de l’acceptance, calibration de résolution, repondération
impact: Corrections propres aux jeux de données et propagation des incertitudes résiduelles.
industry: Estimation de paramètres | Modèles dynamiques latents
---
Construction d’un workflow statistique pour estimer un comportement temporel à partir de mesures affectées par la sélection et la résolution des capteurs.

### Problème
Les distributions temporelles observées étaient modifiées par la sélection des données, la résolution de mesure et les écarts entre simulation et données.

### Ma contribution
- Modélisation explicite de l’efficacité de sélection et de la résolution de mesure.
- Estimation séparée des corrections pour des jeux de données acquis dans des conditions différentes.
- Alignement des échantillons de référence et cibles par repondération ; développement de composants réutilisables pour l’ajustement conjoint de modèles.

### Validation et résultat
Comparaison des simulations corrigées aux mesures et intégration des écarts résiduels dans l’évaluation des incertitudes. Le workflow permet la revue des hypothèses et des corrections propres à chaque jeu de données.

### Illustrations

![Effets de reconstruction sur la distribution temporelle](assets/selected-work/work-2/time_rec_eff.png "La reconstruction modifie la sensibilité à la structure temporelle.")
![Chaîne d’analyse](assets/selected-work/work-2/workflow.png "Des données aux observables latentes.")
