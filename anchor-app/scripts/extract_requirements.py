#!/usr/bin/env python3
import json
import sys
import uuid
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("Missing dependency 'python-docx'. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
OUTPUT_JSON = ROOT / "Resources" / "requirements.json"

PRD_DOC = DOCS_DIR / "Anchor_App_PRD.docx"
PLAN_DOC = DOCS_DIR / "Anchor_App_Execution_Plan.docx"


def extract_paragraphs(doc_path: Path) -> list[str]:
    if not doc_path.exists():
        return []
    doc = Document(str(doc_path))
    items: list[str] = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            items.append(text)
    return items


def build_requirements() -> list[dict]:
    prd_items = extract_paragraphs(PRD_DOC)
    plan_items = extract_paragraphs(PLAN_DOC)

    combined: list[str] = []
    if prd_items:
        combined.extend(prd_items)
    if plan_items:
        combined.extend(plan_items)

    requirements: list[dict] = []
    for idx, text in enumerate(combined, start=1):
        # Heuristic: first sentence as title, rest as details
        parts = text.split(". ", 1)
        if len(parts) == 2:
            title, details = parts[0].strip(), parts[1].strip()
        else:
            title, details = text.strip(), ""
        requirements.append({
            "id": str(uuid.uuid4()),
            "title": title,
            "details": details,
        })
    return requirements


def main() -> int:
    requirements = build_requirements()
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(requirements, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(requirements)} requirements to {OUTPUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())