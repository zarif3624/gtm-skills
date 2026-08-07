#!/usr/bin/env python3
"""Validate high-signal GitHub Actions supply-chain controls."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
USES_RE = re.compile(r"^\s*-\s+uses:\s+([^@\s]+)@([^\s#]+)", re.MULTILINE)
SHA_RE = re.compile(r"^[0-9a-f]{40}$", re.IGNORECASE)


def validate_workflow(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if re.search(r"^\s*pull_request_target\s*:", text, re.MULTILINE):
        errors.append("pull_request_target requires an explicit security review")
    for action, reference in USES_RE.findall(text):
        if action.startswith("./"):
            continue
        if not SHA_RE.fullmatch(reference):
            errors.append(f"remote action must use a full commit SHA: {action}@{reference}")
    return errors


def main() -> int:
    if not WORKFLOWS.is_dir():
        print("FAIL .github/workflows is missing")
        return 1
    paths = sorted((*WORKFLOWS.glob("*.yml"), *WORKFLOWS.glob("*.yaml")))
    if not paths:
        print("FAIL no GitHub Actions workflows found")
        return 1
    failures = 0
    for path in paths:
        errors = validate_workflow(path)
        failures += bool(errors)
        print(f"{'FAIL' if errors else 'PASS'} {path.name}")
        for error in errors:
            print(f"  - {error}")
    print(f"\nValidated {len(paths)} workflows; {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
