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
**Calibration du risque d’erreur prédit par un classifieur à partir de données réelles, avant son utilisation dans une mesure physique. Le modèle effectuait le marquage de saveur.**

### Problème et domaine d’application
Le modèle fournissait une décision de saveur (−1, 0 ou +1) et une probabilité estimée de mauvais marquage comprise entre 0 et 0,5. Son entraînement reposait sur des échantillons simulés d’un processus particulier. Les écarts entre simulation et données de collision réelles nécessitaient une calibration de cette probabilité.

Ces écarts dépendent du processus cible : la calibration ne peut pas être supposée universelle pour d’autres signaux.

### Contribution personnelle
- Utilisation d’un processus de référence dont la saveur était identifiable dans les données reconstruites ; comparaison avec la décision du modèle pour calibrer la probabilité estimée de mauvais marquage.
- Calibration à partir des données pour l’analyse du signal, afin de traiter l’influence d’estimations mal calibrées sur la mesure finale.
- Participation aux discussions de construction et d’entraînement pour préparer la calibration et la validation ; sans réalisation de l’entraînement du modèle.

### Transfert vers l’ingénierie
Calibrer la confiance d’un modèle à partir d’observations, reconnaître les écarts simulation-données et vérifier le domaine d’application d’une calibration avant son transfert. Cette expérience porte sur la calibration des sorties d’un modèle pour l’analyse scientifique.
