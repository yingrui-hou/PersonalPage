import hashlib
import html
import json
from pathlib import Path
import runpy
import subprocess

from pypdf import PdfReader
import pypdfium2 as pdfium
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, PageBreak, Paragraph, SimpleDocTemplate

HERE = Path(__file__).resolve().parent
SOURCE = Path('/Users/hou/Documents/Codex/2026-09-03/referenced-chatgpt-conversation-this-is-an/outputs')
RUNTIME = Path('/Users/hou/.cache/codex-runtimes/codex-primary-runtime/dependencies')
context = runpy.run_path(str(HERE / 'build_deliverables.py'))


def inline(tokens, plain=False):
    parts = []
    for token in tokens:
        kind = token['type']
        if kind in ('text', 'escape', 'codespan'):
            value = token.get('text', '')
            parts.append(value if plain else html.escape(value))
        elif kind in ('link', 'strong', 'em'):
            value = inline(token['tokens'], plain)
            if plain:
                parts.append(value)
            elif kind == 'link':
                parts.append(f'<link href="{html.escape(token["href"], quote=True)}" color="#246B78">{value}</link>')
            else:
                tag = 'b' if kind == 'strong' else 'i'
                parts.append(f'<{tag}>{value}</{tag}>')
        elif kind == 'br':
            parts.append(' ' if plain else '<br/>')
        else:
            raise ValueError(f'Unsupported inline token: {kind}')
    return ''.join(parts)


def render(name):
    source = SOURCE / f'{name}.md'
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    module = (RUNTIME / 'node/node_modules/marked/lib/marked.esm.js').as_uri()
    code = f'import {{lexer}} from {json.dumps(module)}; import fs from "node:fs"; process.stdout.write(JSON.stringify(lexer(fs.readFileSync(process.argv[1], "utf8"))));'
    tokens = json.loads(subprocess.check_output([str(RUNTIME / 'node/bin/node'), '--input-type=module', '-e', code, str(source)], text=True))
    styles = context['template'].make_styles(modern=True)
    styles['job'].keepWithNext = True
    styles['job'].spaceBefore = 5
    styles['section'].keepWithNext = True
    story, expected = [], []
    heading_count = 0
    header = True
    for token in tokens:
        kind = token['type']
        if kind == 'space':
            continue
        if kind == 'html':
            if token['text'].strip() == '<!-- Saut de page dans le PDF -->':
                story.append(PageBreak())
            else:
                raise ValueError('Unsupported HTML block')
            continue
        if kind == 'heading':
            heading_count += 1
            depth = token['depth']
            text = inline(token['tokens'])
            expected.append(inline(token['tokens'], True))
            if depth == 1:
                story.append(Paragraph(text, styles['name']))
            elif depth == 2 and heading_count == 2:
                story.append(Paragraph(text, styles['headline']))
            elif depth == 2:
                if header:
                    story.append(HRFlowable(width='100%', thickness=1.2, color=HexColor('#246B78'), spaceBefore=5, spaceAfter=2))
                    header = False
                context['template'].add_section_heading(story, inline(token['tokens'], True), styles, True)
            elif depth == 3:
                story.append(Paragraph(text, styles['job']))
            else:
                raise ValueError(f'Unsupported heading depth: {depth}')
        elif kind == 'paragraph':
            expected.append(inline(token['tokens'], True))
            story.append(Paragraph(inline(token['tokens']), styles['contact' if header else 'body']))
        elif kind == 'list':
            for item in token['items']:
                paragraphs = [t for t in item['tokens'] if t['type'] != 'space']
                assert all(t['type'] in ('text', 'paragraph') for t in paragraphs)
                text = ' '.join(inline(t['tokens']) for t in paragraphs)
                expected.append(' '.join(inline(t['tokens'], True) for t in paragraphs))
                story.append(Paragraph('- ' + text, styles['bullet']))
        else:
            raise ValueError(f'Unsupported block: {kind}')
    output = HERE / 'staged' / f'{name}.pdf'
    doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                           topMargin=13*mm, bottomMargin=14*mm, author='Yingrui Hou', title=expected[1])
    doc.short_label = 'Yingrui Hou | ' + name.split('_')[0]
    doc.build(story, onFirstPage=context['footer'], onLaterPages=context['footer'])
    pdf = PdfReader(output)
    normalise = lambda value: ''.join(value.split())
    text = normalise(''.join(page.extract_text() for page in pdf.pages))
    assert all(normalise(value) in text for value in expected), 'Missing source text'
    assert hashlib.sha256(source.read_bytes()).hexdigest() == digest, 'Source changed during conversion'
    rendered = pdfium.PdfDocument(output)
    for i in range(len(rendered)):
        rendered[i].render(scale=1.2).to_pil().save(HERE / 'qa' / f'{name}-current-{i+1}.png')
    print(f'{name}: {len(pdf.pages)} pages; source text verified; Markdown unchanged')


for name in ['CV-SIM_Yingrui_Hou', 'CV-DATA_Yingrui_Hou']:
    render(name)
