#!/usr/bin/env python3
"""Check repository-level invariants beyond the standard skill validator."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "agents/openai.yaml", "README.md", "LICENSE", "CONTRIBUTING.md",
    "references/safety.md", "references/rubric.md", "references/formulas.md",
    "references/frameworks.md", "references/curriculum.md",
    "references/case-generation.md", "references/case-metadata.schema.json",
    "references/public-standards.md",
]

missing = [item for item in REQUIRED if not (ROOT / item).exists()]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
for pointer in ["safety.md", "rubric.md", "formulas.md", "case-generation.md"]:
    if pointer not in skill:
        missing.append(f"SKILL.md pointer to {pointer}")

for onboarding_rule in [
    "Are you new to case interviews?",
    "Would you like me to teach you anything from the learning section before we begin?",
    "What level would you like: easy, intermediate, or advanced?",
]:
    if onboarding_rule not in skill:
        missing.append(f"SKILL.md onboarding rule: {onboarding_rule}")

frameworks = (ROOT / "references/frameworks.md").read_text(encoding="utf-8")
for framework_name in [
    "Profitability",
    "The 3 Cs",
    "Porter’s Five Forces",
    "The 4 Ps",
    "Mergers and acquisitions (M&A)",
]:
    if framework_name not in frameworks:
        missing.append(f"framework reference: {framework_name}")

if missing:
    print("Repository checks failed:")
    for item in missing:
        print(f"- {item}")
    sys.exit(1)
print("Repository checks passed.")
