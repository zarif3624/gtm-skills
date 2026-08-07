#!/usr/bin/env python3
"""Validate the portable structure and basic quality rules for every skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\((references|assets)/([^)]+)\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening YAML delimiter"]
    try:
        raw, _body = text[4:].split("\n---\n", 1)
    except ValueError:
        return {}, ["missing closing YAML delimiter"]

    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_file = path / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    fields, frontmatter_errors = parse_frontmatter(text)
    errors.extend(frontmatter_errors)

    if set(fields) != {"name", "description"}:
        errors.append("frontmatter must contain exactly name and description")
    if fields.get("name") != path.name:
        errors.append("name must match its directory")
    if not NAME_RE.fullmatch(fields.get("name", "")):
        errors.append("name must use lowercase letters, digits, and hyphens")
    description = fields.get("description", "")
    if not 20 <= len(description) <= 1024:
        errors.append("description must contain 20-1024 characters")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md must remain below 500 lines")
    if "TODO" in text or "[TODO" in text:
        errors.append("unresolved TODO marker")

    for folder, relative in LINK_RE.findall(text):
        target = path / folder / relative.split("#", 1)[0]
        if not target.exists():
            errors.append(f"broken local resource link: {folder}/{relative}")
    return errors


def main() -> int:
    failures = 0
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failures += 1
            print(f"FAIL {skill_dir.name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {skill_dir.name}")

    print(f"\nValidated {len(skill_dirs)} skills; {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
