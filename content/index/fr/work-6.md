---
number: 06
homepage_order: 3
collapsible: true
title: Validation de modèles de reconnaissance d’images et performance ECAL
tags: Reconnaissance d’images | Données réelles | Optimisation | Diagnostic
methods: Canaux de référence, comparaison données-simulation, analyse instrumentale
impact: Transformation d’écarts de validation en actions de calibration et de correction.
industry: Qualité des données | Validation de modèles | Diagnostic
---
**Investigation d’écarts de performance sur données réelles et identification de pistes pour la calibration et le suivi logiciel. Le travail comprend l’évaluation et l’optimisation d’un modèle de reconnaissance d’images pour le clustering de l’ECAL de LHCb au Run 3.**

### Réalisation personnelle
- Utilisation de plusieurs canaux de référence à différentes impulsions.
- Comparaison de la simulation et des données selon les sélections et les flux de déclenchement.
- Investigation des causes instrumentales et logicielles pour orienter les actions correctives.
- Contrôles et optimisation des performances du modèle de reconnaissance d’images utilisé pour le clustering, à partir de données réelles.
- Participation aux discussions de construction et d’entraînement du modèle pour préparer sa validation ultérieure ; sans réalisation de son entraînement.

![Validation des données](assets/selected-work/work-6/data_validation.png "Mise en évidence d’un défaut de calibration en énergie et suivi après correction.")

### Résultat
Identification d’une anomalie liée à une cellule du calorimètre, d’asymétries spatiales, de défauts de calibration et d’un problème d’énergie manquante corrigé ensuite dans le logiciel. La contribution est le diagnostic et la validation ; les corrections en aval sont attribuées aux équipes concernées.
### Association à la vérité simulée : du diagnostic à une modification intégrée
Dans les événements simulés à forte occupation, les candidats photons reconstruits de haute énergie présentaient une résolution anormale. La comparaison des énergies reconstruites et simulées et de l’identité des particules associées a permis de remonter à des associations incorrectes, notamment à des particules mères de plus haute énergie.

J’ai modifié l’algorithme pour comparer les dépôts d’énergie individuels des particules de vérité dans le cluster du photon reconstruit, normalisés par l’énergie totale déposée par ces particules dans ce cluster. Le matching sélectionne la particule contribuant le plus.

J’ai contrôlé la méthode sur plusieurs processus de désintégration simulés : identités des particules associées aux photons signal, énergies vraies et reconstruites, chaînes de désintégration et dépôts d’énergie de certains événements. J’ai aussi amélioré la sûreté multithread du code suivant les remarques du reviewer. **La merge request a été intégrée et la modification utilisée pour les analyses Run 3 et les contrôles de performance de reconstruction.** Cette contribution concerne l’association à la vérité simulée, distincte de l’évaluation du clustering sur données réelles et de son entraînement.

### Publication associée
*Monitoring reconstruction software in LHCb*, [DOI](https://doi.org/10.1051/epjconf/202125103044).
