from __future__ import annotations

import html
import importlib.util
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer
from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT = Path('/Users/hou/Projects/PersonalPage')
OUT = ROOT / 'work/pmsmp/staged'
QA = ROOT / 'work/pmsmp/qa'
spec = importlib.util.spec_from_file_location('cv_template', ROOT / 'CV_related/generate_resume_pdfs.py')
template = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = template
spec.loader.exec_module(template)


def b(kind, text=''):
    return (kind, text)


CONTACT = [
    b('contact', 'Clermont-Ferrand, France | +33 (0)7 85 39 63 32 | yingrui.hou@outlook.com'),
    b('contact', 'Portfolio : yingrui-hou.github.io/PersonalPage/ | LinkedIn : linkedin.com/in/yingrui-hou'),
    b('orcid', '0000-0001-6454-278X'),
]

EDUCATION = [
    b('section', 'FORMATION'),
    b('body', 'Master + doctorat intégrés en physique des particules | University of Chinese Academy of Sciences | 2016-2021'),
    b('body', 'Licence en physique appliquée | China University of Mining and Technology | 2010-2014'),
    b('section', 'LANGUES'),
    b('body', 'Chinois : langue maternelle | Anglais : C1 | Français : B1 vers B2'),
]

SIM = [
    b('name', 'Yingrui Hou'),
    b('headline', 'Ingénieure Simulation Numérique / Digital Twin - Modélisation physique, validation expérimentale, analyse de données'),
    *CONTACT,
    b('rule'),
    b('section', 'PROFIL'),
    b('body', 'Titulaire d’un doctorat en physique, avec quatre années de recherche postdoctorale au CNRS. Expérience en simulation Geant4, modélisation de réponse et validation expérimentale : relier mesures, calibration et prototype virtuel pour estimer les performances. Recherche d’une PMSMP de 2 à 4 semaines en simulation numérique, digital twin ou prototypage virtuel pour la R&D autour de Clermont-Ferrand.'),
    b('section', 'COMPÉTENCES CLÉS'),
    b('bullet', 'Simulation numérique : Geant4, Monte Carlo, C++ ; géométrie, interactions physiques et réponse de systèmes instrumentés.'),
    b('bullet', 'Modélisation physique : réponse optique, matériaux scintillants, décomposition temporelle du signal et budget de résolution.'),
    b('bullet', 'Validation expérimentale : essais CERN, calibration, cartes d’uniformité, comparaison simulation-mesures et analyse des écarts.'),
    b('bullet', 'Analyse et calcul scientifique : Python, ROOT/RooFit, fitting, maximum de vraisemblance, correction de biais et incertitudes.'),
    b('bullet', 'Développement et collaboration : Linux, Git, workflows reproductibles, logiciels partagés et communication scientifique internationale.'),
    b('section', 'PROFESSIONAL EXPERIENCE'),
    b('job', 'Postdoctoral Researcher | CNRS - LPCA, Clermont-Ferrand | 2023-2025'),
    b('job', 'GRAiNITA | Physics-based simulation and instrumented prototype validation'),
    b('bullet', 'Modelled the response of a scintillating-grain prototype by linking June 2024 CERN SPS H9 measurements with Geant4 performance simulations.'),
    b('bullet', 'Extracted response-uniformity maps from a 16-channel prototype using track reconstruction, channel corrections and 2D spatial analysis.'),
    b('bullet', 'Integrated measured maps into a simplified full-size module simulation to estimate the impact of non-uniformity on resolution.'),
    b('bullet', 'Evaluated the resolution budget: photo-electron statistics near 1%/sqrt(E) and a non-uniformity constant term estimated below 1% in the studied configuration, with E in GeV.'),
    b('bullet', 'Contributed to experimental validation using WLS fibres, SiPMs and DWC beam tracking to connect measured response with simulation assumptions.'),
    b('job', 'PSD studies | Time-resolved signals and energy reconstruction'),
    b('bullet', 'Developed ZnWO4/BGO scintillation simulations from 1 to 20 GeV with particle-dependent time constants to assess signal-separation capabilities.'),
    b('bullet', 'Extracted time-profile components through fitting and applied a correlation-based correction, improving resolution by about a factor of 2 in a representative simulation study.'),
    b('bullet', 'Compared material timing signatures and identified insufficient separation in BGO to guide the interpretation of PSD studies.'),
    b('page'),
    b('section', 'PROFESSIONAL EXPERIENCE - CONTINUED'),
    b('job', 'Postdoctoral Researcher | CNRS - LAPP, Annecy | 2021-2023'),
    b('job', 'LHCb | Calibration, validation and data analysis'),
    b('bullet', 'Built reconstruction checks on reference channels through Monte Carlo-to-data comparisons to isolate calibration, sensor and software discrepancies.'),
    b('bullet', 'Identified a missing-energy software anomaly through reconstruction-chain diagnostics; the issue was subsequently corrected downstream.'),
    b('bullet', 'Modelled time-dependent observations with acceptance and resolution corrections and joint fits to estimate latent parameters and their uncertainties.'),
    b('bullet', 'Aligned control and simulation samples through Gradient Boosting reweighting to reduce bias from distribution differences.'),
    b('bullet', 'Developed machine learning classifiers with train/test diagnostics and threshold scans to validate event selection before inference.'),
    b('bullet', 'Extracted weak signals using signal-plus-background models and maximum-likelihood estimation, with stability checks across datasets and selections.'),
    b('job', 'Doctoral Research | University of Chinese Academy of Sciences | 2016-2021'),
    b('bullet', 'Developed analyses combining simulation, statistical modelling and calibration to validate models against experimental data.'),
    b('section', 'PROJETS COMPLÉMENTAIRES'),
    b('job', 'Correction de simulation | QCFilter / études STCF'),
    b('bullet', 'Développé un package C++ intégré à Gaudi utilisant des contraintes mesurées et un filtrage stochastique événement par événement pour rétablir des corrélations absentes d’une simulation rapide.'),
    b('job', 'Validation de méthodes d’inférence | Collaboration LHCb'),
    b('bullet', 'Contribué à la validation d’une méthode non binée par fonctions de base, avec pseudo-expériences et traitement des covariances pour tester les effets du fond, de l’efficacité et de la résolution.'),
    b('bullet', 'Préparé des entrées de données avec reconstruction, sélection et soustraction statistique du fond pour confronter la méthode à des conditions de mesure réalistes.'),
    *EDUCATION,
]

DATA = [
    b('name', 'Yingrui Hou'),
    b('headline', 'Data Scientist R&D - Données expérimentales, calibration, modélisation et validation'),
    *CONTACT,
    b('rule'),
    b('section', 'PROFIL'),
    b('body', 'Titulaire d’un doctorat en physique, avec quatre années de recherche postdoctorale au CNRS en analyse de données expérimentales, modélisation statistique et validation. Expérience de la calibration, du fitting et de la comparaison simulation-données, complétée par le machine learning sur les analyses LHCb. Recherche d’une PMSMP de 2 à 4 semaines en data science industrielle ou analyse de données R&D autour de Clermont-Ferrand.'),
    b('section', 'COMPÉTENCES CLÉS'),
    b('bullet', 'Analyse de données : modélisation statistique, fitting, maximum de vraisemblance, modèles de mélange et inférence dépendant du temps.'),
    b('bullet', 'Calibration et qualité des mesures : correction du bruit, égalisation des canaux, cartographie de réponse, correction des biais et estimation des incertitudes.'),
    b('bullet', 'Outils : Python, C++, NumPy, pandas, scikit-learn, statsmodels, ROOT/RooFit ; Linux et Git pour les analyses reproductibles.'),
    b('bullet', 'Simulation et validation : Geant4, Monte Carlo, comparaison simulation-données, échantillons de contrôle et études de robustesse.'),
    b('bullet', 'Machine learning LHCb : classification supervisée, Gradient Boosting, études de variables, diagnostics train/test, scans de seuils et repondération.'),
    b('bullet', 'Communication : visualisations et notes techniques, restitution des hypothèses et limites, revues au sein de collaborations internationales.'),
    b('section', 'PROFESSIONAL EXPERIENCE'),
    b('job', 'Postdoctoral Researcher | CNRS - LPCA, Clermont-Ferrand | 2023-2025'),
    b('job', 'GRAiNITA | Measurement data, calibration and validation'),
    b('bullet', 'Analysed muon/pion data from the 16-channel prototype tested at CERN SPS H9 in June 2024 to quantify response, noise and spatial uniformity.'),
    b('bullet', 'Built a calibration workflow with dark-noise subtraction, fibre-response equalisation and position-resolved mapping to make measurements comparable.'),
    b('bullet', 'Developed signal-extraction models using a Landau distribution convolved with a Gaussian for muons, supplemented by a Crystal Ball component for pions.'),
    b('bullet', 'Produced uniformity maps from reconstructed tracks and photo-electron yields to support Geant4 performance studies.'),
    b('bullet', 'Compared measured maps with simulations to isolate position-dependent effects, with a non-uniformity constant term estimated below 1% in the studied configuration.'),
    b('job', 'PSD studies | Signal decomposition and performance metrics'),
    b('bullet', 'Fitted simulated time profiles with electromagnetic, hadronic and proton-like components to extract signal composition and correct reconstructed energy.'),
    b('bullet', 'Validated extracted fractions against simulated values and compared resolution before and after correction, obtaining about a factor-of-2 improvement in a representative study.'),
    b('bullet', 'Compared ZnWO4 and BGO simulations from 1 to 20 GeV to identify limits in timing separation and the reliability of extracted parameters.'),
    b('page'),
    b('section', 'PROFESSIONAL EXPERIENCE - CONTINUED'),
    b('job', 'Postdoctoral Researcher | CNRS - LAPP, Annecy | 2021-2023'),
    b('job', 'LHCb | Machine learning, inference and monitoring'),
    b('bullet', 'Developed machine learning classifiers with feature studies, train/test diagnostics and threshold scans to check for overfitting and improve selection reliability.'),
    b('bullet', 'Corrected distribution differences through Gradient Boosting reweighting of control and calibration samples before statistical inference.'),
    b('bullet', 'Built time-dependent models and joint fits with dataset-specific acceptance and resolution corrections to estimate latent parameters.'),
    b('bullet', 'Extracted weak signals using signal-plus-background models and maximum-likelihood estimation, then automated yield, width and fit-stability checks.'),
    b('bullet', 'Developed monitoring that compared observations and simulations across reconstruction stages to identify calibration, sensor and software anomalies.'),
    b('bullet', 'Identified a missing-energy software issue through discrepancy analysis; the issue was subsequently corrected in the reconstruction chain.'),
    b('job', 'Doctoral Research | University of Chinese Academy of Sciences | 2016-2021'),
    b('bullet', 'Developed analyses combining simulation and probabilistic modelling to calibrate measurements and validate results against experimental data.'),
    b('section', 'PROJETS COMPLÉMENTAIRES'),
    b('job', 'Inférence avancée | Validation d’une méthode non binée, LHCb'),
    b('bullet', 'Évalué les effets du fond, de l’efficacité et de la résolution avec pseudo-expériences et contrôles tenant compte des covariances pour valider une inférence par fonctions de base.'),
    b('bullet', 'Préparé un échantillon réel par reconstruction, sélection et soustraction statistique du fond pour fournir des entrées exploitables dans les ajustements conjoints.'),
    b('job', 'Correction de modèles | QCFilter / études STCF'),
    b('bullet', 'Implémenté un package C++/Gaudi transformant des contraintes mesurées en filtrage stochastique d’événements pour corriger les distributions d’une simulation rapide.'),
    *EDUCATION,
]

MISSION = [
    b('name', 'Mission d’immersion professionnelle'),
    b('headline', 'Modèle éditable | Simulation numérique ou Data Science R&D | 2 à 4 semaines'),
    b('contact', 'Candidat : Yingrui Hou | Clermont-Ferrand | yingrui.hou@outlook.com'),
    b('rule'),
    b('body', 'Fiche de cadrage à compléter avec l’entreprise et le prescripteur. Elle accompagne la préparation d’une PMSMP et ne remplace pas la convention officielle. Les activités, dates et horaires retenus sont ceux validés dans cette convention.'),
    b('section', '1. IDENTIFICATION ET ORGANISATION'),
    b('body', 'Entreprise / établissement : [nom, adresse, site]'),
    b('body', 'Équipe d’accueil et métier observé : [service, intitulé du métier]'),
    b('body', 'Tuteur / tutrice : [nom, fonction, téléphone, courriel]'),
    b('body', 'Prescripteur et référent : [organisme, nom, coordonnées]'),
    b('body', 'Période : du [date] au [date] | Durée choisie : [2 / 3 / 4] semaines'),
    b('body', 'Jours, horaires, pauses et volume total : [à préciser] | Lieu(x) : [à préciser]'),
    b('body', 'Disponibilité du tutorat : [créneaux] | Points de suivi : [dates]'),
    b('body', 'Objet principal retenu avec le prescripteur : [découvrir un métier / confirmer un projet professionnel / initier une démarche de recrutement]. Choisir un seul objet.'),
    b('section', '2. OBJECTIFS À OBSERVER ET À ÉVALUER'),
    b('bullet', 'Comprendre le workflow de l’équipe, les données utilisées, les outils et les critères de validation du métier ciblé.'),
    b('bullet', 'Mettre en pratique, sous tutorat, une démarche limitée de modélisation ou d’analyse sur un cas convenu.'),
    b('bullet', 'Évaluer la transférabilité des compétences de simulation, calibration, fitting et validation vers ce contexte industriel.'),
    b('bullet', 'Identifier les connaissances métier et outils à approfondir, puis préciser la suite du projet professionnel.'),
    b('body', 'Question technique retenue : [une question mesurable, adaptée à la durée et aux accès disponibles]'),
    b('body', 'Critères d’observation : [compréhension du problème, rigueur, reproductibilité, communication, autonomie sous tutorat]'),
    b('section', '3. PÉRIMÈTRE ET MOYENS'),
    b('body', 'Cas support : [système / phénomène / mesure] | Données ou modèle de référence : [description et version]'),
    b('body', 'Outils accessibles : [logiciels, environnement de calcul, documentation] | Accès et accueil prévus : [date]'),
    b('body', 'Confidentialité, stockage, restitution et suppression des données : [règles de l’entreprise]'),
    b('body', 'Consignes du site, équipements et accompagnement : [à préciser selon les activités]'),
    b('body', 'Périmètre exclu : exploitation en production, engagement de performance ou tâche régulière correspondant à un poste permanent. La mise en situation sert les objectifs de l’immersion sous tutorat.'),
    b('page'),
    b('section', '4. OPTION DE MISSION À RETENIR'),
    b('body', 'Option choisie : [A / B]. Conserver l’option pertinente et adapter le cas support avec le tuteur.'),
    b('job', 'Option A | Corrélation simulation-mesures et validation d’un modèle physique'),
    b('body', 'Question type : dans quelles conditions un modèle existant reproduit-il les mesures de référence et quelles hypothèses expliquent les principaux écarts ?'),
    b('bullet', 'Observer la construction du modèle et la définition des hypothèses, paramètres, entrées et critères de validation.'),
    b('bullet', 'Reproduire un cas de référence ; vérifier unités, conditions initiales et cohérence entre mesures et sorties simulées.'),
    b('bullet', 'Comparer simulation et mesures ; examiner un paramètre de calibration ou une source de non-uniformité avec le tuteur.'),
    b('bullet', 'Tester quelques variations justifiées et documenter les limites d’interprétation des écarts.'),
    b('body', 'Indicateurs à choisir : [biais, résidus, RMSE, dispersion, sensibilité d’un indicateur physique]. Référence : [cas]. Tolérance discutée : [valeur et justification].'),
    b('body', 'Traces de mise en situation : comparaison de référence, figures de résidus, tableau des hypothèses et courte note de validation.'),
    b('job', 'Option B | Analyse, calibration et validation de données de mesure'),
    b('body', 'Question type : les données permettent-elles de mesurer un comportement stable et quelles corrections ou vérifications sont nécessaires avant la modélisation ?'),
    b('bullet', 'Observer le cycle de collecte et d’utilisation des données ; repérer unités, valeurs manquantes, bruit et conditions d’acquisition.'),
    b('bullet', 'Réaliser une analyse exploratoire et construire un indicateur ou modèle statistique de référence sur un périmètre limité.'),
    b('bullet', 'Étudier une correction de calibration, un ajustement ou une différence de distribution ; comparer avant/après avec une validation adaptée.'),
    b('bullet', 'Si le besoin et les données le justifient, comparer un modèle ML simple au modèle de référence avec séparation des données adaptée au temps, aux lots ou aux équipements.'),
    b('body', 'Indicateurs à choisir : [taux de données exploitables, biais, résidus, stabilité par lot, erreur sur un jeu réservé]. Référence : [cas]. Critère discuté : [à préciser].'),
    b('body', 'Traces de mise en situation : fiche qualité des données, analyse reproductible, figures de diagnostic et note sur les limites du résultat.'),
    b('section', '5. NIVEAU DE COMPLEXITÉ ET SOLUTION DE REPLI'),
    b('body', 'Périmètre minimal : un cas, un jeu de données ou modèle de référence, une question et un petit nombre d’indicateurs. Une amélioration chiffrée n’est pas un résultat garanti.'),
    b('body', 'Si les accès ou données ne sont pas prêts : [observation d’un cas existant / données anonymisées / exemple public ou synthétique validé par le tuteur].'),
    b('body', 'Décision de réduction du périmètre : [qui, quand] | Activité de remplacement : [à préciser]'),
    b('page'),
    b('section', '6. CALENDRIER MODULABLE'),
    b('job', 'Semaine 1 | Découverte et cas de référence'),
    b('bullet', 'Début de semaine : accueil, observation du métier, présentation des outils et cadrage de la question avec le tuteur.'),
    b('bullet', 'Milieu de semaine : lecture du modèle ou des données, vérifications de cohérence et reproduction d’un cas de référence.'),
    b('bullet', 'Fin de semaine : revue du diagnostic initial et validation du périmètre de la mise en situation.'),
    b('body', 'Trace attendue : fiche du cas et premier diagnostic. Point tuteur : [date].'),
    b('job', 'Semaine 2 | Mise en situation encadrée et premier bilan'),
    b('bullet', 'Réaliser une comparaison, une calibration ou un ajustement limité ; vérifier les résultats sur le cas convenu.'),
    b('bullet', 'Documenter la méthode, les hypothèses et les limites ; présenter les observations et les compétences mobilisées.'),
    b('body', 'Trace attendue : analyse ou modèle de travail, figures et synthèse. Pour une immersion de 2 semaines : restitution finale et bilan professionnel à ce stade.'),
    b('job', 'Semaine 3, si prévue | Robustesse et deuxième cas'),
    b('bullet', 'Étendre la démarche à un second cas ou à quelques variations contrôlées pour distinguer un résultat local d’un comportement stable.'),
    b('bullet', 'Examiner les écarts avec le tuteur et préciser les compétences ou connaissances métier à développer.'),
    b('body', 'Trace attendue : comparaison complémentaire et limites mises à jour. Pour 3 semaines : restitution finale en fin de semaine 3.'),
    b('job', 'Semaine 4, si prévue | Consolidation et restitution'),
    b('bullet', 'Reprendre un cas à partir de la documentation, clarifier les résultats et consolider les observations sur le métier.'),
    b('bullet', 'Présenter la synthèse au tuteur et convenir des suites avec le référent du parcours.'),
    b('body', 'Trace attendue : dossier de restitution et bilan final. Toute semaine optionnelle doit être comprise dans les dates convenues.'),
    b('section', '7. RESTITUTION ET BILAN'),
    b('body', 'Format proposé : note de 2 à 4 pages et échange de 15 à 20 minutes, à adapter. Date : [date] | Participants : [noms].'),
    b('bullet', 'Restituer la question, la méthode, le résultat observé, les limites et les étapes qui permettraient de poursuivre l’étude.'),
    b('bullet', 'Décrire les activités du métier observées, les compétences transférables et les besoins de formation identifiés.'),
    b('body', 'Retour du tuteur : [points solides, accompagnement nécessaire, exemples observés]'),
    b('body', 'Retour du candidat : [intérêt pour le métier, conditions de travail, difficultés, apprentissages]'),
    b('body', 'Suite convenue : [projet confirmé / exploration complémentaire / formation / échange recrutement]'),
    b('body', 'Action suivante : [action] | Responsable : [nom] | Échéance : [date]'),
    b('body', 'Fiche relue le [date] par [candidat], [tuteur] et [référent]. Référence de convention : [à compléter].'),
    b('section', 'RÉFÉRENCES DU CADRE PMSMP'),
    b('body', 'Immersion Facilitée : objectifs, convention et obligations. Liens officiels dans la version Markdown. Consultés le 3 septembre 2026.'),
]

DOCS = {
    'CV-SIM_Yingrui_Hou': SIM,
    'CV-DATA_Yingrui_Hou': DATA,
    'Mission_Immersion_2-4_semaines': MISSION,
}


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(HexColor('#59636B'))
    canvas.drawString(18 * mm, 8 * mm, doc.short_label)
    canvas.drawRightString(A4[0] - 18 * mm, 8 * mm, str(doc.page))
    canvas.restoreState()


def build(name, blocks):
    styles = template.make_styles(modern=True)
    styles['job'].keepWithNext = True
    styles['job'].spaceBefore = 5
    styles['section'].keepWithNext = True
    story, md = [], []
    for kind, text in blocks:
        if kind == 'page':
            story.append(PageBreak())
            md.append('<!-- Saut de page dans le PDF -->')
        elif kind == 'rule':
            story.append(HRFlowable(width='100%', thickness=1.2, color=HexColor('#246B78'), spaceBefore=5, spaceAfter=2))
        elif kind == 'section':
            template.add_section_heading(story, text, styles, True)
            md.append('## ' + text)
        elif kind == 'orcid':
            url = 'https://orcid.org/' + text
            story.append(Paragraph(f'ORCID : <link href="{url}" color="#246B78">{text}</link>', styles['contact']))
            md.append(f'ORCID : [{text}]({url})')
        else:
            label = '- ' + text if kind == 'bullet' else text
            story.append(Paragraph(html.escape(label), styles[kind]))
            prefix = {'name': '# ', 'headline': '## ', 'job': '### ', 'bullet': '- '}.get(kind, '')
            md.append(prefix + text)
    if name.startswith('Mission'):
        md.extend([
            '- [Présentation et convention](https://aide.immersion-facile.beta.gouv.fr/fr/article/quest-ce-quune-immersion-professionnelle-xeml36/)',
            '- [Objets de l’immersion](https://aide.immersion-facile.beta.gouv.fr/fr/article/quels-sont-les-objectifs-dune-immersion-pmsmp-125axdq/)',
            '- [Obligations](https://aide.immersion-facile.beta.gouv.fr/fr/article/quelles-sont-les-obligations-a-respecter-pour-une-immersion-1bl944v/)',
        ])
    (OUT / f'{name}.md').write_text('\n\n'.join(md) + '\n', encoding='utf-8')
    doc = SimpleDocTemplate(str(OUT / f'{name}.pdf'), pagesize=A4, leftMargin=18*mm,
                            rightMargin=18*mm, topMargin=13*mm, bottomMargin=14*mm,
                            title=blocks[1][1], author='Yingrui Hou')
    doc.short_label = 'Yingrui Hou | ' + ('Mission d’immersion' if name.startswith('Mission') else name.split('_')[0])
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    pdf = PdfReader(OUT / f'{name}.pdf')
    print(f'{name}: {len(pdf.pages)} pages; ' + ', '.join(str(len(p.extract_text())) + ' chars' for p in pdf.pages))
    render = pdfium.PdfDocument(OUT / f'{name}.pdf')
    for i in range(len(render)):
        render[i].render(scale=1.4).to_pil().save(QA / f'{name}-{i+1}.png')


if __name__ == '__main__':
    for name, blocks in DOCS.items():
        build(name, blocks)
