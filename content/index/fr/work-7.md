---
number: 07
homepage_order: 6
collapsible: true
title: Modernisation d’un outil C++ extensible
tags: C++ | Interfaces | Intégration logicielle
methods: extension de code existant, conception de méthodes, intégration, tests
impact: livraison d’une version utilisée pour les simulations suivantes du projet et enrichie par les collaborateurs.
industry: Plateformes de simulation | Calcul scientifique | Intégration logicielle
---
Modernisation de QCFilter, outil de simulation partagé au sein de la collaboration expérimentale, avec une interface réutilisable pour des modèles personnalisés.

### Problème
Le code existant présentait des défauts connus, une implémentation ancienne et un périmètre de modèles limité. Les nouveaux travaux exigeaient un moyen maintenable d’ajouter des modèles.

### Ma contribution
- Réécriture avec une norme C++ plus récente et le framework Gaudi.
- Conception d’une interface commune de modèles et ajout de plusieurs processus physiques.
- Prise en charge de la méthode, de l’implémentation, de l’intégration Gaudi/BOSS et des tests finaux.

### Validation et résultat
Accord entre anciennes et nouvelles simulations dans les comparaisons effectuées. Comparaison des principales distributions aux données réelles, avec des écarts résiduels liés aux limites du modèle. L’outil a servi aux simulations suivantes et a été étendu par les collaborateurs. Le code est partagé en interne dans l’expérience.

### Publications

*CP violation studies at Super Tau-Charm Facility*, [DOI](https://doi.org/10.48550/arXiv.2502.08907).
