# Notes de préparation et messages d’approche

Version du 3 septembre 2026. Les deux CV et la fiche de mission sont fournis en Markdown éditable et en PDF.

## Modèle repris

Le dernier CV effectivement généré dans la tâche « Assess CV for ATS fit » est `CV_YingruiHou_ResilienceCare_MLDataScientist.pdf`. Les échanges ultérieurs portent sur la préparation d’entretien et le profil Malt.

Les nouveaux PDF réutilisent les styles de ce CV : format A4, colonne unique, nom aligné à gauche, police Helvetica, titres de section bleu-vert et filets horizontaux. Le contenu est réorganisé suivant le guide GRAiNITA ; chaque CV fait deux pages. Le Markdown conserve le contenu et la hiérarchie éditables ; le PDF porte la mise en page.

## Sources et périmètre des affirmations

- **Positionnement et vocabulaire :** `GRAiNITA_CV_Reframing_Codex_Guide.md`, sans la contrainte d’une page. Les deux profils visent respectivement la simulation / digital twin et la data science R&D.
- **GRAiNITA :** `sources/GRAiNITA.pdf`, `sources/GRAiNITA_FCC_DRD.pdf`, le guide et `content/index/work-4.md`. Prototype 16 voies, campagne CERN de juin 2024, calibration, cartes spatiales et simulation Geant4. Le terme constant inférieur à 1 % est une estimation dans la configuration étudiée. La statistique de photo-électrons proche de 1 %/sqrt(E) est distincte de ce terme constant.
- **PSD :** `content/index/work-5.md`. Le gain d’environ un facteur 2 concerne une étude simulée représentative ; il ne décrit pas une amélioration industrielle ni un résultat mesuré du prototype GRAiNITA.
- **LHCb :** `content/index/work-1.md`, `work-2.md`, `work-3.md` et `work-6.md`, ainsi que le CV précédent et `content/resume/fr/experience.md`. Extraction de signaux faibles, inférence temporelle, CatBoost, repondération, validation et diagnostic logiciel.
- **Projets complémentaires :** `content/index/work-7.md` pour QCFilter/Gaudi et `work-8.md` pour la validation d’inférence non binée. Ils sont conservés séparément, sans leur attribuer de dates ou d’employeur non documentés.
- **Parcours :** le CV précédent, `CV_related/Malt_Profile_FR_DS_Simulation.md` et `content/resume/fr/education.md`. LPCA 2023-2025, LAPP 2021-2023, master-doctorat intégrés 2016-2021, licence 2010-2014. Aucune activité après 2025 n’a été ajoutée.
- **Coordonnées et langues :** `content/shared/profile.md`, le CV précédent et les sources du CV. La publication de 2026 indique explicitement Yingrui Hou dans la liste des auteurs.

Les deux CV couvrent les huit ensembles de projets documentés. Le machine learning est attribué aux analyses LHCb. Le digital twin figure comme cible professionnelle, sans revendication de déploiement. Aucun outil FEM/CFD, environnement cloud, MLOps ou résultat commercial non documenté n’est ajouté.

## Message d’approche - Simulation

Bonjour [nom], votre équipe [équipe] travaille sur [activité de simulation vérifiée dans l’entreprise]. Mon expérience GRAiNITA relie modélisation physique, mesures expérimentales, calibration et validation : j’ai transformé des cartes de réponse mesurées en entrées de simulation Geant4 pour estimer les performances d’un système. Je recherche une immersion de 2 à 4 semaines à Clermont-Ferrand pour découvrir votre workflow de simulation et permettre une évaluation de mon adéquation technique. Une mise en situation encadrée autour de [modèle / comparaison simulation-essais] pourrait-elle correspondre aux possibilités de votre équipe ?

## Message d’approche - Data Science R&D

Bonjour [nom], les activités de votre équipe sur [données de mesure / qualité / R&D vérifiées dans l’entreprise] m’intéressent. Mon expérience comprend la correction du bruit, la calibration, les ajustements statistiques, les cartes de réponse et la comparaison simulation-données ; mes analyses LHCb incluent également CatBoost et la validation sous changement de distribution. Je recherche une immersion de 2 à 4 semaines pour découvrir votre métier et appliquer cette démarche, sous tutorat, à un cas limité de [analyse / calibration / validation]. Pourrions-nous échanger sur un périmètre adapté ?

## Utilisation de la fiche de mission

Compléter les champs entre crochets, retenir l’option A ou B, puis fixer les semaines, les activités et les critères d’observation avec le tuteur. Le calendrier comporte une restitution finale à la semaine 2, 3 ou 4 selon la durée convenue.

Le document est une fiche de cadrage, pas une convention PMSMP. Le cadre de l’immersion, l’objet principal et la convention sont décrits par [Immersion Facilitée](https://aide.immersion-facile.beta.gouv.fr/fr/article/quest-ce-quune-immersion-professionnelle-xeml36/). Les activités proposées sont des mises en situation encadrées, conformément aux [obligations de l’immersion](https://aide.immersion-facile.beta.gouv.fr/fr/article/quelles-sont-les-obligations-a-respecter-pour-une-immersion-1bl944v/).

## Vérification effectuée

Les sept pages PDF ont été inspectées visuellement. Le contenu extrait des PDF a été comparé aux textes sources des livrables. Les fichiers Markdown et PDF proviennent du même contenu structuré.
