import html
import runpy
from pathlib import Path

import pypdfium2 as pdfium
from pypdf import PdfReader
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

HERE = Path(__file__).resolve().parent
OUT = HERE / 'informatis_3214'
OUT.mkdir(exist_ok=True)
base = runpy.run_path(str(HERE / 'build_deliverables.py'))
b = base['b']
CONTACT = [b('contact', 'Clermont-Ferrand, France | +33 (0)7 85 39 63 32 | yingrui.hou@outlook.com'),
           b('contact', 'Portfolio: yingrui-hou.github.io/PersonalPage/ | LinkedIn: linkedin.com/in/yingrui-hou'),
           b('orcid', '0000-0001-6454-278X')]

CV = [
    b('name', 'Yingrui Hou'),
    b('headline', 'Data Scientist | Exploratory Modelling, Machine Learning & Validation'),
    *CONTACT, b('rule'),
    b('section', 'PROFESSIONAL SUMMARY'),
    b('body', 'PhD-trained data scientist with four years of postdoctoral research at CNRS, developing Python/C++ analytical workflows, machine learning models and statistical validation methods. Experienced in turning open research questions into reproducible studies, evaluating methods under noisy measurements and distribution shifts, and communicating assumptions and limitations to international collaborators. Interested in exploratory data and AI projects connecting technical feasibility with practical decisions.'),
    b('section', 'CORE SKILLS'),
    b('bullet', 'Scientific programming: Python, NumPy, pandas, scikit-learn, statsmodels; C++, ROOT/RooFit, Linux and Git.'),
    b('bullet', 'Machine learning: supervised classification, feature studies, train/test diagnostics, threshold selection, sample reweighting and validation under distribution shift.'),
    b('bullet', 'Statistical modelling: likelihood estimation, mixture models, time-dependent inference, joint fitting, uncertainty quantification and sensitivity studies.'),
    b('bullet', 'Exploration and validation: proof-of-principle studies, control samples, calibration, monitoring, anomaly diagnosis and comparison of modelling assumptions.'),
    b('bullet', 'Technical delivery: reusable analysis components, reproducible configurations, collaborative review, documented findings and scientific presentations.'),
    b('section', 'PROFESSIONAL EXPERIENCE'),
    b('job', 'Postdoctoral Researcher | CNRS - LPCA, Clermont-Ferrand | 2023-2025'),
    b('bullet', 'Developed a measurement-to-simulation workflow for GRAiNITA, translating prototype observations into response maps and Geant4 performance studies.'),
    b('bullet', 'Built calibration and signal-extraction methods using noise correction, channel equalisation and statistical fitting to produce comparable, position-resolved measurements.'),
    b('bullet', 'Integrated measured response maps into a simplified full-size model to estimate performance limits, including a non-uniformity constant term below 1% in the studied configuration.'),
    b('bullet', 'Developed time-profile fitting and correction methods for scintillation simulations, improving energy resolution by about a factor of 2 in a representative study.'),
    b('bullet', 'Compared material-dependent signal separation and communicated model assumptions, limitations and results to guide collaborative R&D discussions.'),
    b('job', 'Postdoctoral Researcher | CNRS - LAPP, Annecy | 2021-2023'),
    b('bullet', 'Developed reusable Python/C++ workflows for weak-signal extraction and time-dependent inference on noisy datasets without direct event-level ground truth.'),
    b('bullet', 'Built machine learning classifiers with feature studies, train/test diagnostics and threshold scans to assess overfitting and validate event selection.'),
    b('bullet', 'Aligned control and simulation samples through machine learning reweighting to address distribution differences before downstream inference.'),
    b('bullet', 'Built monitoring and reconstruction checks that traced discrepancies to calibration, sensor or software causes, including a missing-energy software issue subsequently corrected downstream.'),
    b('page'),
    b('section', 'SELECTED TECHNICAL PROJECTS'),
    b('job', 'Proof-of-principle validation | Advanced statistical inference, LHCb'),
    b('bullet', 'Contributed to testing a novel unbinned inference method under background, efficiency and resolution effects, using pseudoexperiments and covariance-aware checks.'),
    b('bullet', 'Prepared real-data inputs through reconstruction, selection and statistical background subtraction to assess whether the method remained usable beyond idealised conditions.'),
    b('job', 'Machine learning validation | LHCb'),
    b('bullet', 'Combined feature assessment, score validation, threshold scans and sample alignment into reproducible workflows to evaluate model reliability under dataset mismatch.'),
    b('job', 'Latent-parameter estimation | Time-dependent and weak-signal analyses'),
    b('bullet', 'Modelled acceptance and resolution with dataset-specific corrections and joint fits to infer latent behaviour while accounting for measurement bias.'),
    b('bullet', 'Implemented signal-plus-background likelihood fits and automated yield, width and stability checks across datasets and selections.'),
    b('job', 'Sensor modelling and signal decomposition | GRAiNITA and PSD studies'),
    b('bullet', 'Extracted spatial response maps from a 16-channel CERN test-beam prototype to constrain a physics-based model with measured inputs.'),
    b('bullet', 'Compared ZnWO4 and BGO simulations from 1 to 20 GeV, using fitted timing components to assess reconstruction performance and limits of signal separation.'),
    b('job', 'Reusable scientific software | QCFilter / STCF studies'),
    b('bullet', 'Developed a C++ package integrated into Gaudi, converting measured constraints into stochastic event filtering to restore missing correlations in a fast simulation.'),
    b('section', 'EARLIER EXPERIENCE'),
    b('job', 'Doctoral Research | University of Chinese Academy of Sciences | 2016-2021'),
    b('bullet', 'Developed analyses combining simulation, statistical modelling and calibration to validate models against experimental data.'),
    b('section', 'EDUCATION'),
    b('body', 'Joint Master and PhD in Particle Physics | University of Chinese Academy of Sciences | 2016-2021'),
    b('body', 'BSc in Applied Physics | China University of Mining and Technology | 2010-2014'),
    b('section', 'LANGUAGES'),
    b('body', 'English: C1 | French: B1 progressing towards B2 | Chinese: native'),
]

LETTER = [
    b('name', 'Yingrui Hou'), *CONTACT, b('rule'),
    b('body', '10 September 2026'),
    b('body', 'Mr Marc Sorel\nInformatis-TS\n26 rue Daubenton\n75005 Paris, France'),
    b('headline', 'Application - Data Scientist / AI Engineer - Reference 3214'),
    b('body', 'Dear Mr Sorel,'),
    b('body', 'I am applying for the Data Scientist / AI Engineer position in Paris or Clermont-Ferrand. The opportunity to explore new use cases, develop proofs of concept and help teams assess technical feasibility is particularly appealing to me. Based in Clermont-Ferrand, I would welcome the opportunity to bring my experience in scientific data analysis and model validation to your client’s innovation team.'),
    b('body', 'I hold a PhD in particle physics and have four years of postdoctoral research experience at CNRS. At LAPP, I developed Python and C++ workflows for machine learning, statistical inference and validation on complex measurement data. This included feature studies, train/test diagnostics and sample reweighting to address differences between datasets. I also developed monitoring methods that traced discrepancies to calibration and software causes, including a reconstruction issue that was subsequently corrected.'),
    b('body', 'At LPCA, my work connected experimental measurements with simulation to evaluate the behaviour of an instrumented prototype. I developed calibration, response-mapping and signal-analysis workflows, then used their outputs to assess model assumptions and performance limits. In a separate collaborative study, I contributed to proof-of-principle validation of a new inference method under realistic measurement effects. These projects required me to turn open questions into testable approaches and communicate what the evidence did and did not support.'),
    b('body', 'I would bring scientific Python skills, rigorous machine learning validation and experience developing reusable analytical components in shared Linux and Git environments. My professional platform experience has mainly been in scientific computing rather than Azure or Databricks, so I would need to build practical familiarity with your client’s environment. My immediate contribution would be in modelling, experimental design, validation and clear technical recommendations.'),
    b('body', 'I work comfortably in English within international collaborations and value close discussion with domain experts when defining a useful analysis. I would be pleased to discuss how my background could support your client’s exploratory projects and the transition from a tested idea to a documented solution.'),
    b('body', 'Kind regards,\nYingrui Hou'),
]

ROWS = [
    ['Assessment area', 'Weight', 'Credit', 'Evidence and limitation'],
    ['Python and analytical modelling', '20', '18', 'Strong Python/C++ and statistical work; no evidence of enterprise Python service ownership.'],
    ['Exploration, machine learning and validation', '20', '17', 'Research autonomy, classifiers, robustness checks and proof-of-principle validation.'],
    ['Databricks and Azure / Azure ML', '25', '2', 'No documented practical experience; small credit for transferable computing workflows only.'],
    ['NLP and API / web data acquisition', '10', '3', 'Complex-data analysis transfers partly; NLP, crawling and API ingestion are unproven.'],
    ['Business workshops and IT architecture', '10', '4', 'Technical communication transfers; DSI reporting and enterprise architecture are unproven.'],
    ['Seniority and delivery context', '10', '5', 'Four postdoctoral years plus doctoral research; equivalence to five required years is uncertain.'],
    ['English and location', '5', '5', 'C1 English and Clermont-Ferrand residence are directly aligned.'],
    ['TOTAL', '100', '54', 'Approximately 55% overall documented fit.'],
]

REPORT = [
    b('name', 'Job Fit Analysis'),
    b('headline', 'Informatis-TS | Data Scientist / AI Engineer | Offer 3214'),
    b('contact', 'Prepared for Yingrui Hou | 10 September 2026 | Decision support, not a hiring prediction'),
    b('rule'),
    b('section', 'RECOMMENDATION'),
    b('body', 'Apply selectively, with medium-to-low priority. Your analytical background makes a recruiter conversation worthwhile, especially given the Clermont-Ferrand option. However, this is a stretch application: strong research methods do not establish the requested cloud-platform experience. Do not invest in a substantial take-home exercise before checking whether those requirements are negotiable.'),
    b('body', 'Estimated documented fit: 54/100, rounded to about 55%. The strongest overlap is exploratory modelling and validation; the weakest is immediate readiness for the specified platform and enterprise IT context. This is a transparent judgement rubric, not an ATS result or an interview probability. A strict platform filter could reject the application regardless of the aggregate score.'),
    b('section', 'ROLE AND LISTING STATUS'),
    b('body', 'The role combines early-stage data/AI exploration, prototypes, technical choices and stakeholder communication within an IT department. Python, Databricks and Azure are central; the advertised seniority is at least five years. It offers a permanent contract and Paris or Clermont-Ferrand with flexible remote work. [1]'),
    b('body', 'The indexed employer page is dated 9 April 2026; the matching Hellowork listing carries reference 3214 and a 14 August 2026 publication date. This suggests republication, not proof of a new vacancy. Direct employer-page retrieval returned an error; indexed content and the accessible matching listing were cross-checked. Confirm that recruitment remains active. [1][2]'),
    b('section', 'WEIGHTED MATCH MATRIX'),
    ('table', ROWS),
    b('body', 'Weights reflect this specific posting, especially its platform emphasis. Undocumented skills are treated as unproven, not as proof that you cannot learn them. The scoring should change if you can supply concrete Azure, Databricks or NLP work.'),
    b('page'),
    b('section', 'YOUR STRONGEST MATCH POINTS'),
    b('job', '1. Converting uncertain questions into validated analyses'),
    b('body', 'The LHCb inference-method study provides a credible proof-of-principle example: you tested measurement effects, prepared realistic inputs and checked robustness. Explain the initial uncertainty, the simplest baseline, the acceptance criteria and the finding that changed the next step.'),
    b('job', '2. Machine learning and statistical judgement'),
    b('body', 'Your classifier validation, sample reweighting, joint fits and uncertainty studies show more than model training. The strongest interview story is how you detected a misleading result, identified its cause and changed the evaluation or correction strategy.'),
    b('job', '3. Reusable work and technical communication'),
    b('body', 'Shared C++/Python workflows, Git collaboration, QCFilter and scientific presentations support a claim of reusable technical delivery. They provide transferable evidence for explaining feasibility and limitations. They do not establish commercial product ownership or enterprise architecture expertise.'),
    b('section', 'GAPS THAT MAY DETERMINE THE OUTCOME'),
    b('bullet', 'Azure and Databricks: the current CV and project evidence do not support proficiency. Scientific computing and reproducibility are useful foundations, but should not be presented as platform equivalence.'),
    b('bullet', 'NLP and unstructured information: sensor signals and complex event data do not demonstrate language-processing experience. API integration, scraping and crawling also need concrete examples before being claimed.'),
    b('bullet', 'Enterprise decisions: no documented build-versus-buy evaluation, business workshop leadership, IT urbanisation or reporting to a CIO. Scientific review experience is relevant but only partially transferable.'),
    b('bullet', 'Seniority: state four postdoctoral years plus doctoral research. Do not describe this as five or more years of commercial AI engineering. The recruiter must clarify how doctoral work is counted.'),
    b('bullet', 'French and stakeholder work: your documented level is B1 towards B2. Although professional English is specified, the language used for business workshops is unknown; test this early rather than assuming English-only delivery.'),
    b('section', 'CONDITIONS FOR APPLYING'),
    b('body', 'Proceed if the team can support platform onboarding and values analytical experimentation. Deprioritise if it needs an autonomous Azure/Databricks specialist immediately, or if most assignments require established NLP delivery and enterprise architecture ownership. The current profile is better supported for scientific/R&D data roles and model-validation positions.'),
    b('body', 'The client and domain are not identified in the posting. Clermont-Ferrand alone does not identify the employer. The application therefore addresses Informatis and its client without naming a presumed end customer.'),
    b('page'),
    b('section', 'QUESTIONS FOR THE RECRUITER'),
    b('bullet', 'Is offer 3214 still funded and open, and is the contract with Informatis or directly with the end client?'),
    b('bullet', 'Are Azure and Databricks screening prerequisites, or can a strong Python/modelling profile learn the platform with support?'),
    b('bullet', 'What are the first two use cases, and how much work involves language data versus structured or measurement data?'),
    b('bullet', 'Who owns architecture, deployment and operational support after a prototype is accepted?'),
    b('bullet', 'Does the five-year threshold include doctoral research? What evidence would establish the expected seniority?'),
    b('bullet', 'What language is used in business workshops, and what presence or travel is required from Clermont-Ferrand?'),
    b('bullet', 'What is the actual salary budget, start date and expected outcome in the first three months?'),
    b('section', 'APPLICATION AND INTERVIEW STRATEGY'),
    b('body', 'Position yourself as a Data Scientist specialising in exploratory modelling, machine learning and validation. Lead with problem framing, evaluation design and reusable results. Explain the physical context in one sentence, then focus on data, method, decision and limitations.'),
    b('body', 'Prepare three examples: an inference proof of principle; a machine learning workflow under dataset mismatch; and monitoring that found a software issue. For each, distinguish your own contribution from the collaboration’s result. Explain the handover artefacts and what another team would need to reproduce the work.'),
    b('body', 'A useful next learning project, if the recruiter confirms flexibility, would reproduce one existing analysis in the requested environment with documented data, a baseline, an evaluation and a reproducible run. Label it as a personal learning project only after completing it. Do not add Azure/Databricks proficiency to the current CV on the basis of a plan.'),
    b('section', 'COMPENSATION AND PRACTICAL UNCERTAINTIES'),
    b('body', 'The employer gives no numerical salary budget. Hellowork shows EUR 40,000-67,500 annually as its own estimate, not an employer commitment. Use this only as background for asking the recruiter; it is not a justified salary target for your profile. Exact remote arrangements and client identity also remain unresolved. [1][2]'),
    b('section', 'SOURCES AND EVIDENCE BOUNDARIES'),
    b('body', '[1] Informatis-TS, offer 3214, indexed employer posting; accessed 10 September 2026. Direct page retrieval failed; indexed content was available.'),
    b('link', 'Employer posting|https://www.informatis-ts.fr/offre_detail.php?id_offre=3214'),
    b('body', '[2] Hellowork, matching Informatis vacancy, reference 3214; accessed 10 September 2026. Used to corroborate scope and distinguish a platform salary estimate from an employer budget.'),
    b('link', 'Matching Hellowork posting|https://www.hellowork.com/fr-fr/emplois/77803130.html'),
    b('body', 'Candidate evidence: current CV Markdown; content/shared/profile.md; content/resume/en/skills.md, experience.md and education.md; portfolio projects work-1 through work-8; prior LPCA/LAPP experience descriptions and the GRAiNITA guide. These are candidate-provided records, not independent employment verification. No new cloud, NLP, business-impact or deployment claims have been added.'),
]


def render(name, blocks, label, expected_pages):
    styles = base['template'].make_styles(modern=True)
    styles['job'].keepWithNext = True
    styles['job'].spaceBefore = 5
    styles['section'].keepWithNext = True
    if name.startswith('Motivation'):
        styles['body'].fontSize = 10.3
        styles['body'].leading = 13.6
        styles['body'].spaceAfter = 8
    story, markdown, expected = [], [], []
    for kind, value in blocks:
        if kind == 'page':
            story.append(PageBreak())
            markdown.append('<!-- page break -->')
        elif kind == 'rule':
            story.append(HRFlowable(width='100%', thickness=1.2, color=HexColor('#246B78'), spaceBefore=5, spaceAfter=6))
        elif kind == 'table':
            rows = [[Paragraph(html.escape(cell), styles['compact_note']) for cell in row] for row in value]
            table = Table(rows, colWidths=[46*mm, 14*mm, 14*mm, 100*mm], repeatRows=1)
            table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),HexColor('#E7EFF0')),('LINEBELOW',(0,0),(-1,-1),0.3,HexColor('#CBD4D7')),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            story.append(table)
            markdown.append('\n'.join(['| '+' | '.join(value[0])+' |', '|---|---:|---:|---|']+['| '+' | '.join(row)+' |' for row in value[1:]]))
            expected.extend(cell for row in value for cell in row)
        elif kind in ('orcid','link'):
            title, url = ('ORCID: '+value, 'https://orcid.org/'+value) if kind == 'orcid' else value.split('|',1)
            story.append(Paragraph(f'<link href="{html.escape(url, quote=True)}" color="#246B78">{html.escape(title)}</link>',styles['contact']))
            markdown.append(f'[{title}]({url})')
            expected.append(title)
        elif kind == 'section':
            base['template'].add_section_heading(story,value,styles,True)
            markdown.append('## '+value)
            expected.append(value)
        else:
            text = ('- ' if kind=='bullet' else '') + value
            story.append(Paragraph(html.escape(text).replace('\n','<br/>'),styles[kind]))
            markdown.append({'name':'# ','headline':'## ','job':'### ','bullet':'- '}.get(kind,'')+value)
            expected.append(value)
    md = '\n\n'.join(markdown)+'\n'
    assert not any(term in md.lower() for term in ['catboost','bdt','gradient boost'])
    (OUT/f'{name}.md').write_text(md,encoding='utf-8')
    doc = SimpleDocTemplate(str(OUT/f'{name}.pdf'),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=13*mm,bottomMargin=15*mm,title=label,author='Yingrui Hou' if name != 'Job_Analysis_Informatis_3214' else 'Prepared for Yingrui Hou')
    doc.short_label = label
    doc.build(story,onFirstPage=base['footer'],onLaterPages=base['footer'])
    pdf=PdfReader(OUT/f'{name}.pdf')
    normalise=lambda text: ''.join(text.split())
    extracted=normalise(''.join(page.extract_text() for page in pdf.pages))
    assert all(normalise(text) in extracted for text in expected), name
    assert len(pdf.pages)==expected_pages,(name,len(pdf.pages))
    render_pdf=pdfium.PdfDocument(OUT/f'{name}.pdf')
    for i in range(len(render_pdf)):
        render_pdf[i].render(scale=1.25).to_pil().save(HERE/'qa'/f'{name}-{i+1}.png')
    print(name, len(pdf.pages),'pages; text complete')


render('CV_Yingrui_Hou_Informatis_3214', CV, 'Yingrui Hou | Informatis 3214', 2)
render('Motivation_Letter_Informatis_3214', LETTER, 'Yingrui Hou | Application 3214', 1)
render('Job_Analysis_Informatis_3214', REPORT, 'Job fit assessment | Informatis 3214', 3)
