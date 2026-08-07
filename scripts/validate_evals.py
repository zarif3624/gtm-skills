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
JOURNEYS = ROOT / "evals" / "journeys"
ROUTING = ROOT / "evals" / "routing" / "cases.json"
SKILLS = ROOT / "skills"
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TOP_LEVEL_FIELDS = {"schema_version", "id", "skill", "risk", "prompt", "context", "assertions"}
ASSERTION_FIELDS = {"must_demonstrate", "must_avoid", "human_review"}
JOURNEY_FIELDS = {"schema_version", "id", "skills", "prompt", "context", "assertions"}
JOURNEY_ASSERTION_FIELDS = {"must_preserve", "must_not_transform", "human_review"}
ROUTING_TOP_FIELDS = {"schema_version", "cases"}
ROUTING_CASE_FIELDS = {"id", "prompt", "expected_skills", "excluded_skills"}


def nonempty_strings(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and bool(item.strip()) for item in value
    )


def validate_case(path: Path, skill_names: set[str]) -> tuple[str | None, list[str]]:
    errors: list[str] = []
    if path.is_symlink():
        return None, ["evaluation case must not be a symbolic link"]
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


def validate_journey(path: Path, skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    if path.is_symlink():
        return ["journey case must not be a symbolic link"]
    try:
        journey = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"invalid JSON: {error}"]
    if not isinstance(journey, dict):
        return ["journey must be a JSON object"]
    if set(journey) != JOURNEY_FIELDS:
        errors.append(f"journey fields must be exactly: {', '.join(sorted(JOURNEY_FIELDS))}")

    journey_id = journey.get("id")
    if not isinstance(journey_id, str) or not ID_RE.fullmatch(journey_id):
        errors.append("id must use lowercase letters, digits, and hyphens")
    elif journey_id != path.stem:
        errors.append("id must match the journey filename")
    if journey.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    skills = journey.get("skills")
    if not nonempty_strings(skills) or len(skills) < 2:
        errors.append("skills must contain at least two skill names")
    else:
        unknown = sorted(set(skills) - skill_names)
        if unknown:
            errors.append(f"unknown skills: {', '.join(unknown)}")
        if len(skills) != len(set(skills)):
            errors.append("skills must not contain duplicates")
    for field in ("prompt",):
        if not isinstance(journey.get(field), str) or not journey[field].strip():
            errors.append(f"{field} must be a non-empty string")
    if not nonempty_strings(journey.get("context")):
        errors.append("context must be a non-empty list of strings")

    assertions = journey.get("assertions")
    if not isinstance(assertions, dict) or set(assertions) != JOURNEY_ASSERTION_FIELDS:
        errors.append(
            f"assertions must contain exactly: {', '.join(sorted(JOURNEY_ASSERTION_FIELDS))}"
        )
    else:
        for field in sorted(JOURNEY_ASSERTION_FIELDS):
            if not nonempty_strings(assertions.get(field)):
                errors.append(f"assertions.{field} must be a non-empty list of strings")
    return errors


def validate_routing(path: Path, skill_names: set[str]) -> tuple[set[str], list[str]]:
    if path.is_symlink():
        return set(), ["routing corpus must not be a symbolic link"]
    try:
        corpus = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return set(), [f"invalid JSON: {error}"]
    if not isinstance(corpus, dict):
        return set(), ["routing corpus must be a JSON object"]
    errors: list[str] = []
    if set(corpus) != ROUTING_TOP_FIELDS:
        errors.append(f"routing fields must be exactly: {', '.join(sorted(ROUTING_TOP_FIELDS))}")
    if corpus.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    cases = corpus.get("cases")
    if not isinstance(cases, list) or not cases:
        return set(), errors + ["cases must be a non-empty list"]

    covered: set[str] = set()
    seen_ids: set[str] = set()
    for index, case in enumerate(cases, start=1):
        prefix = f"cases[{index}]"
        if not isinstance(case, dict) or set(case) != ROUTING_CASE_FIELDS:
            errors.append(f"{prefix} fields must be exactly: {', '.join(sorted(ROUTING_CASE_FIELDS))}")
            continue
        case_id = case["id"]
        if not isinstance(case_id, str) or not ID_RE.fullmatch(case_id):
            errors.append(f"{prefix}.id must use lowercase letters, digits, and hyphens")
        elif case_id in seen_ids:
            errors.append(f"duplicate routing id: {case_id}")
        else:
            seen_ids.add(case_id)
        if not isinstance(case["prompt"], str) or not case["prompt"].strip():
            errors.append(f"{prefix}.prompt must be a non-empty string")
        expected = case["expected_skills"]
        excluded = case["excluded_skills"]
        for field, value in (("expected_skills", expected), ("excluded_skills", excluded)):
            if not nonempty_strings(value) or len(value) != len(set(value)):
                errors.append(f"{prefix}.{field} must be a non-empty unique list of skills")
            elif unknown := sorted(set(value) - skill_names):
                errors.append(f"{prefix}.{field} has unknown skills: {', '.join(unknown)}")
        if isinstance(expected, list) and isinstance(excluded, list):
            overlap = sorted(set(expected) & set(excluded))
            if overlap:
                errors.append(f"{prefix} expects and excludes: {', '.join(overlap)}")
            if all(isinstance(item, str) for item in expected):
                covered.update(set(expected) & skill_names)
    return covered, errors


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
        results[f"cases/{case_file.name}"] = errors
        if skill and not errors:
            covered.add(skill)
        if case_file.stem in seen_ids:
            errors.append(f"duplicate case id: {case_file.stem}")
        seen_ids.add(case_file.stem)

    missing = sorted(skill_names - covered)
    if missing:
        repository_errors.append(f"skills without a valid eval case: {', '.join(missing)}")

    if not JOURNEYS.is_dir():
        repository_errors.append("evals/journeys directory is missing")
    else:
        journey_files = sorted(JOURNEYS.glob("*.json"))
        if not journey_files:
            repository_errors.append("no journey evaluation cases found")
        for journey_file in journey_files:
            results[f"journeys/{journey_file.name}"] = validate_journey(
                journey_file, skill_names
            )
    if not ROUTING.is_file():
        repository_errors.append("evals/routing/cases.json is missing")
    else:
        routing_coverage, routing_errors = validate_routing(ROUTING, skill_names)
        results["routing/cases.json"] = routing_errors
        missing_routing = sorted(skill_names - routing_coverage)
        if missing_routing:
            repository_errors.append(
                f"skills without a routing case: {', '.join(missing_routing)}"
            )
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
    print(f"\nValidated {len(results)} eval definition files; {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
