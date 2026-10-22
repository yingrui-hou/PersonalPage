---
number: 07
homepage_order: 6
collapsible: true
title: QCFilter : évolution d’un logiciel de simulation partagé
tags: C++ | Logiciel scientifique | Gaudi/BOSS | Correction de simulation
methods: extension de code existant, conception de méthodes, intégration, tests
impact: livraison d’une version utilisée pour les simulations suivantes du projet et enrichie par les collaborateurs.
industry: Plateformes de simulation | Calcul scientifique | Intégration logicielle
---
**Évolution d’un outil QCFilter existant, partagé au sein de la collaboration expérimentale, destiné à la simulation de systèmes D⁰D̄⁰ quantiquement corrélés dans les environnements fondés sur Gaudi. Conception des méthodes, implémentation C++, intégration Gaudi/BOSS et tests réalisés personnellement.**

### Contexte
QCFilter applique des contraintes physiques par filtrage événementiel pour représenter les corrélations quantiques dans les systèmes D⁰D̄⁰ simulés. Le code ancien présentait quelques bugs connus et ne prenait en charge que le cas de corrélation antisymétrique sous C. L’évolution a porté sur le code et sur la facilité d’ajout de processus personnalisés.

### Contribution personnelle
- Réécriture du code existant selon une norme C++ plus récente, dans le framework Gaudi.
- Ajout d’une **interface générique de modèles d’amplitude**, pour permettre aux utilisateurs d’intégrer leurs propres processus physiques.
- Intégration dans Gaudi/BOSS et réalisation des tests finaux.
- Ajout de plusieurs processus physiques majeurs et livraison du package QCFilter mis à jour.

### Vérification
- Comparaison des résultats simulés avec l’outil initial et sa nouvelle version : concordance dans les comparaisons réalisées.
- Comparaison avec les données réelles des principales variables cinématiques et des observables liées aux amplitudes : accord global, avec des écarts résiduels attribués aux limites du modèle.

### Utilisation et collaboration
Cette version a servi aux échantillons simulés suivants du projet. D’autres collaborateurs l’ont ensuite enrichie avec les processus de signal de leurs propres études.

Cette expérience illustre la reprise d’un code existant, la livraison d’un outil intégré et sa réutilisation par des collègues. Le domaine visé est la simulation de systèmes D⁰D̄⁰ quantiquement corrélés sous Gaudi.

### Publication associée
*CP violation studies at Super Tau-Charm Facility*, [DOI](https://doi.org/10.48550/arXiv.2502.08907).
