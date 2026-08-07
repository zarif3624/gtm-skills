#!/usr/bin/env python3
"""Verify that every recorded evaluation commit exists in current repository history."""

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
    except OSError as error:
        print(f"FAIL cannot inspect Git history: {error}")
        return 1
    for error in errors:
        print(f"FAIL {error}")
    print(f"\nVerified {count} unique evaluation commits; {len(errors)} invalid references.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
