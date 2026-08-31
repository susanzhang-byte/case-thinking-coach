#!/usr/bin/env python3
"""Dependency-free structural checks for the bundled case bank."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
REQUIRED_KEYS = {
    "id", "title", "category", "industry", "difficulty", "target_roles",
    "duration_minutes", "provenance", "safety_reviewed", "calculation_checked",
}
ALLOWED_DIFFICULTIES = {"introductory", "intermediate", "advanced"}
PROHIBITED_REVIEW_TERMS = {
    "terrorism", "self-harm", "sexual misconduct", "mass casualty",
    "active shooter", "graphic injury", "visa cancellation",
}


def parse_simple_yaml(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors: list[str] = []
    case_dirs = sorted(p for p in CASES.iterdir() if p.is_dir())
    ids: set[str] = set()
    for case_dir in case_dirs:
        for filename in ("metadata.yaml", "case.md", "solution.md"):
            if not (case_dir / filename).is_file():
                errors.append(f"{case_dir.name}: missing {filename}")
        metadata_path = case_dir / "metadata.yaml"
        if not metadata_path.exists():
            continue
        data = parse_simple_yaml(metadata_path)
        missing = REQUIRED_KEYS - data.keys()
        if missing:
            errors.append(f"{case_dir.name}: missing metadata {sorted(missing)}")
        case_id = data.get("id", "")
        if case_id != case_dir.name or not re.fullmatch(r"[a-z0-9-]+", case_id):
            errors.append(f"{case_dir.name}: invalid or mismatched id {case_id!r}")
        if case_id in ids:
            errors.append(f"{case_dir.name}: duplicate id")
        ids.add(case_id)
        if data.get("difficulty") not in ALLOWED_DIFFICULTIES:
            errors.append(f"{case_dir.name}: invalid difficulty")
        for flag in ("safety_reviewed", "calculation_checked"):
            if data.get(flag) != "true":
                errors.append(f"{case_dir.name}: {flag} must be true")
        combined = " ".join(
            p.read_text(encoding="utf-8").lower()
            for p in (case_dir / "case.md", case_dir / "solution.md") if p.exists()
        )
        for term in PROHIBITED_REVIEW_TERMS:
            if term in combined:
                errors.append(f"{case_dir.name}: prohibited review term {term!r}")
        if "you may ask 1–2 clarifying questions" not in combined:
            errors.append(f"{case_dir.name}: missing clarifying-question invitation")
        if "## reference framework" not in combined:
            errors.append(f"{case_dir.name}: missing reference framework")
        if "## math to disclose after framework submission" not in combined:
            errors.append(f"{case_dir.name}: missing formula checkpoint")

    if not case_dirs:
        errors.append("no case directories found")
    if errors:
        print("Case validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(case_dirs)} case directories.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
