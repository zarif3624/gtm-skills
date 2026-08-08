#!/usr/bin/env python3
"""Verify evaluation commits and current behavioral evidence freshness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("report must be a JSON object")
    return value


def commit_error(commit: str, root: Path) -> str | None:
    exists = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if exists.returncode:
        return "commit is not available in the repository"
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit, "HEAD"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if ancestor.returncode:
        return "commit is not an ancestor of HEAD"
    return None


def report_paths(root: Path) -> list[Path]:
    paths = sorted((root / "evals" / "results").rglob("*.json"))
    routing = sorted((root / "evals" / "routing" / "results").glob("*.json"))
    paths.extend(path for path in routing if not path.name.endswith(".response.json"))
    return paths


def current_behavioral_reports(root: Path) -> list[tuple[Path, dict[str, Any]]]:
    """Return the unsuperseded behavioral report in every case/lineage chain."""
    reports: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / "evals" / "results").rglob("*.json")):
        reports.append((path.resolve(), load_json(path)))
    superseded = {
        (root / report["supersedes"]).resolve()
        for _, report in reports
        if report.get("supersedes")
    }
    return [(path, report) for path, report in reports if path not in superseded]


def report_skills(report: dict[str, Any], root: Path) -> list[str]:
    case_path = root / report["case_path"]
    definition = load_json(case_path)
    if report.get("case_type") == "case":
        skill = definition["skill"]
        if not isinstance(skill, str):
            raise ValueError("case skill must be a string")
        return [skill]
    skills = definition["skills"]
    if not isinstance(skills, list) or not all(isinstance(item, str) for item in skills):
        raise ValueError("journey skills must be a string list")
    return skills


def repository_path_changed(
    commit: str, relative: str, root: Path
) -> tuple[bool, str | None]:
    """Compare a tested path with the current tracked and untracked tree."""
    compared = subprocess.run(
        ["git", "diff", "--quiet", commit, "--", relative],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if compared.returncode not in {0, 1}:
        return False, compared.stderr.strip() or "git diff failed"
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "--", relative],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if untracked.returncode:
        return False, untracked.stderr.strip() or "git ls-files failed"
    return compared.returncode == 1 or bool(untracked.stdout.strip()), None


def skill_content_changed(commit: str, skill: str, root: Path) -> tuple[bool, str | None]:
    return repository_path_changed(commit, f"skills/{skill}", root)


def validate_current_behavioral_freshness(root: Path = ROOT) -> tuple[int, list[str]]:
    """Require each current report to test the present contents of every target skill."""
    root = root.resolve()
    errors: list[str] = []
    current = current_behavioral_reports(root)
    for path, report in current:
        try:
            commit = report["run"]["repository_commit"]
            case_path = report["case_path"]
            skills = report_skills(report, root)
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
            errors.append(f"{path.relative_to(root)} cannot resolve tested skills: {error}")
            continue
        definition_changed, definition_error = repository_path_changed(
            commit, case_path, root
        )
        if definition_error:
            errors.append(
                f"{path.relative_to(root)} cannot compare {case_path} at {commit}: "
                f"{definition_error}"
            )
        elif definition_changed:
            errors.append(
                f"{path.relative_to(root)} is stale: {case_path} differs from tested "
                f"commit {commit}"
            )
        for skill in skills:
            changed, comparison_error = skill_content_changed(commit, skill, root)
            if comparison_error:
                errors.append(
                    f"{path.relative_to(root)} cannot compare skills/{skill} at {commit}: "
                    f"{comparison_error}"
                )
            elif changed:
                errors.append(
                    f"{path.relative_to(root)} is stale: skills/{skill} differs from "
                    f"tested commit {commit}"
                )
    return len(current), errors


def validate_report_commits(root: Path = ROOT) -> tuple[int, list[str]]:
    errors: list[str] = []
    checked: dict[str, str | None] = {}
    paths = report_paths(root)
    for path in paths:
        try:
            report = load_json(path)
            commit = report["run"]["repository_commit"]
            if not isinstance(commit, str):
                raise ValueError("run.repository_commit must be a string")
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
            errors.append(f"{path.relative_to(root)} cannot resolve commit: {error}")
            continue
        if commit not in checked:
            checked[commit] = commit_error(commit, root)
        if checked[commit]:
            errors.append(
                f"{path.relative_to(root)} references {commit}: {checked[commit]}"
            )
    return len(set(checked)), errors


def main() -> int:
    try:
        count, errors = validate_report_commits()
        current_count, freshness_errors = validate_current_behavioral_freshness()
    except OSError as error:
        print(f"FAIL cannot inspect Git history: {error}")
        return 1
    for error in errors + freshness_errors:
        print(f"FAIL {error}")
    print(f"\nVerified {count} unique evaluation commits; {len(errors)} invalid references.")
    print(
        f"Verified {current_count} current behavioral reports against present definitions "
        f"and skill content; "
        f"{len(freshness_errors)} stale."
    )
    return 1 if errors or freshness_errors else 0


if __name__ == "__main__":
    sys.exit(main())
