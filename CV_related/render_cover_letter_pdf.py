#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

try:
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
except ImportError as exc:  # pragma: no cover - runtime dependency guard
    raise SystemExit("Install reportlab before rendering cover letters.") from exc


def clean_markdown(text: str) -> str:
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text).strip()


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    safe_text = html.escape(clean_markdown(text)).replace("\n", "<br/>")
    return Paragraph(safe_text, style)


def build_letter(input_path: Path, output_path: Path) -> None:
    raw = input_path.read_text(encoding="utf-8").replace("  \n", "\n")
    blocks = [block.strip() for block in re.split(r"\n\s*\n", raw) if block.strip()]
    if len(blocks) < 7:
        raise SystemExit(f"Unexpected cover-letter structure in {input_path}")

    base = getSampleStyleSheet()
    styles = {
        "sender": ParagraphStyle(
            "LetterSender",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            alignment=2,
            textColor=HexColor("#30343f"),
        ),
        "body": ParagraphStyle(
            "LetterBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.2,
            leading=14.2,
            textColor=HexColor("#202124"),
            spaceAfter=8,
        ),
        "subject": ParagraphStyle(
            "LetterSubject",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.4,
            leading=13,
            textColor=HexColor("#1d3557"),
            spaceAfter=10,
        ),
    }

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=input_path.stem.replace("_", " "),
        author="Yingrui Hou",
    )

    sender_lines = [line.strip() for line in blocks[0].splitlines() if line.strip()]
    story = [paragraph("\n".join(sender_lines), styles["sender"]), Spacer(1, 10)]
    story.append(paragraph(blocks[1], styles["body"]))
    story.append(Spacer(1, 4))
    story.append(paragraph("\n".join(blocks[2].splitlines()), styles["body"]))
    story.append(Spacer(1, 5))
    story.append(paragraph(blocks[3], styles["subject"]))

    for block in blocks[4:]:
        story.append(paragraph("\n".join(block.splitlines()), styles["body"]))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render an editable Markdown cover letter as PDF.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build_letter(args.input, args.output)
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
