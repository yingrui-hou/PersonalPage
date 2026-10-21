---
number: 05
homepage_order: 4
collapsible: true
title: Décomposition temporelle et reconstruction du signal
tags: Analyse temporelle | PSD | Correction de modèle
methods: Modèles de scintillation, ajustements de composantes, corrections par corrélation
impact: Réduction d’environ 2× d’un terme de résolution dans une étude représentative par rotation.
industry: Analyse de signaux | Caractérisation capteur | Validation de modèle
---
**Développement d’une simulation et d’une analyse PSD pour extraire les composantes de gerbe à partir de profils temporels de scintillation.**

![Résolution avant et après correction](assets/selected-work/work-5/res_compare.png "Évaluation de la correction dans les conditions étudiées.")

### Comparaison expérimentale pour choisir le matériau
L’équipe a testé ZnWO4 et BGO en mesurant les profils de décroissance temporelle de la scintillation dans plusieurs domaines d’énergie, sous excitation électromagnétique ou hadronique. Le critère de choix était la capacité à distinguer ces processus par leurs profils temporels dans les conditions étudiées.

L’équipe a retenu **ZnWO4** pour poursuivre les études PSD. À basse énergie, les profils mesurés de BGO étaient trop proches des profils d’excitation électromagnétique pour fournir la séparation recherchée. Cette comparaison expérimentale a guidé la suite de la modélisation ; elle est distincte des résultats simulés de résolution présentés ci-dessous.

### Réalisation personnelle
- Génération d’échantillons simulés électron/proton/pion pour ZnWO4 et BGO entre 1 et 20 GeV ; vérification des corrélations pertinentes.
- Extension de la simulation avec des constantes temporelles dépendant du type de particule et de dE/dx.
- Ajustement des profils temporels en composantes électromagnétique, hadronique et protonique, puis utilisation des fractions dans la correction de l’énergie.

![Ajustement temporel](assets/selected-work/work-5/time_fit.png "Comparaison d’une fraction extraite à sa référence simulée.")

### Résultat
Dans une étude représentative fondée sur une rotation, un terme de résolution est réduit d’environ un facteur 2. Une validation donne F_em = 0,740 ± 0,055 pour une référence de 0,738. L’étude identifie aussi une limite : la séparation temporelle de BGO est moins favorable que celle de ZnWO4. Ces résultats restent propres aux configurations étudiées.
