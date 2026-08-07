#!/usr/bin/env python3
"""Validate realistic evaluation cases and ensure every skill is covered."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evals" / "cases"
SKILLS = ROOT / "skills"
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TOP_LEVEL_FIELDS = {"schema_version", "id", "skill", "risk", "prompt", "context", "assertions"}
ASSERTION_FIELDS = {"must_demonstrate", "must_avoid", "human_review"}


def nonempty_strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and bool(item.strip()) for item in value
    )


def validate_case(path: Path, skill_names: set[str]) -> tuple[str | None, list[str]]:
    errors: list[str] = []
    try:
        case = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return None, [f"invalid JSON: {error}"]

    if not isinstance(case, dict):
        return None, ["case must be a JSON object"]
    if set(case) != TOP_LEVEL_FIELDS:
        errors.append(f"case fields must be exactly: {', '.join(sorted(TOP_LEVEL_FIELDS))}")

    case_id = case.get("id")
    if not isinstance(case_id, str) or not ID_RE.fullmatch(case_id):
        errors.append("id must use lowercase letters, digits, and hyphens")
    elif case_id != path.stem:
        errors.append("id must match the case filename")

    if case.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    skill = case.get("skill")
    if skill not in skill_names:
        errors.append(f"unknown skill: {skill}")
    for field in ("risk", "prompt"):
        if not isinstance(case.get(field), str) or not case[field].strip():
            errors.append(f"{field} must be a non-empty string")
    if not nonempty_strings(case.get("context")):
        errors.append("context must be a non-empty list of strings")

    assertions = case.get("assertions")
    if not isinstance(assertions, dict) or set(assertions) != ASSERTION_FIELDS:
        errors.append(f"assertions must contain exactly: {', '.join(sorted(ASSERTION_FIELDS))}")
    else:
        for field in sorted(ASSERTION_FIELDS):
            if not nonempty_strings(assertions.get(field)):
                errors.append(f"assertions.{field} must be a non-empty list of strings")

    return skill if isinstance(skill, str) else None, errors


def run_validation() -> tuple[dict[str, list[str]], list[str]]:
    repository_errors: list[str] = []
    if not CASES.is_dir():
        return {}, ["evals/cases directory is missing"]
    skill_names = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    case_files = sorted(CASES.glob("*.json"))
    if not case_files:
        return {}, ["no evaluation cases found"]

    results: dict[str, list[str]] = {}
    covered: set[str] = set()
    seen_ids: set[str] = set()
    for case_file in case_files:
        skill, errors = validate_case(case_file, skill_names)
        results[case_file.name] = errors
        if skill and not errors:
            covered.add(skill)
        if case_file.stem in seen_ids:
            errors.append(f"duplicate case id: {case_file.stem}")
        seen_ids.add(case_file.stem)

    missing = sorted(skill_names - covered)
    if missing:
        repository_errors.append(f"skills without a valid eval case: {', '.join(missing)}")
    return results, repository_errors


def main() -> int:
    results, repository_errors = run_validation()
    failed = sum(bool(errors) for errors in results.values()) + bool(repository_errors)
    for name, errors in results.items():
        print(f"{'FAIL' if errors else 'PASS'} {name}")
        for error in errors:
            print(f"  - {error}")
    if repository_errors:
        print("FAIL eval coverage")
        for error in repository_errors:
            print(f"  - {error}")
    print(f"\nValidated {len(results)} eval cases; {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
