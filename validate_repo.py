#!/usr/bin/env python3
"""Offline structural checks for the instruction-only humanize-en repository."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
required = ["README.md", "SKILL.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "REFERENCES.md", "CHANGELOG.md", "CONTRIBUTING.md", "profiles/korean-founder.md", "references/founder-trust-audit.md", "references/founder-structure-atlas.md"]
errors = []
for relative in required:
    if not (root / relative).is_file():
        errors.append(f"Missing: {relative}")
skill = (root / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    errors.append("SKILL.md must start with YAML front matter")
if not re.search(r"(?m)^name: humanize-en$", skill):
    errors.append("SKILL.md missing skill name")
for rel in re.findall(r"`((?:references|profiles)/[A-Za-z0-9_.-]+\.md)`", skill):
    if not (root / rel).exists():
        errors.append(f"Broken instruction reference: {rel}")
notices=(root/"THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
for expected in ("Siqi Chen", "Hardik Pandya", "MIT License"):
    if expected not in notices:
        errors.append(f"Missing notice: {expected}")
if errors:
    print("FAILED\n" + "\n".join(errors))
    raise SystemExit(1)
print(f"PASS: {len(required)} required paths; skill links and notices checked")
