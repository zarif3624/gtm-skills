#!/usr/bin/env python3
"""Create an evidence-scoring draft for one behavioral evaluation case."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"


def find_case(case_id: str) -> tuple[Path, dict[str, Any]]:
    matches = sorted((EVALS / "cases").glob(f"{case_id}.json"))
    matches.extend(sorted((EVALS / "journeys").glob(f"{case_id}.json")))
    if len(matches) != 1:
        raise ValueError(f"expected one evaluation case named {case_id}; found {len(matches)}")
    path = matches[0]
    return path, json.loads(path.read_text(encoding="utf-8"))


def current_commit() -> str:
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip() if completed.returncode == 0 else "unknown"


def build_report(
    case_path: Path,
    case: dict[str, Any],
    *,
    agent: str,
    model: str,
    lineage: str,
    tested_at: str,
    repository_commit: str,
    response_path: str,
    supersedes: str | None = None,
) -> dict[str, Any]:
    case_type = "case" if case_path.parent.name == "cases" else "journey"
    scores = {
        category: [
            {"assertion": assertion, "verdict": "unscored", "evidence": ""}
            for assertion in assertions
        ]
        for category, assertions in case["assertions"].items()
    }
    return {
        "schema_version": 1,
        "case_id": case["id"],
        "case_type": case_type,
        "case_path": case_path.relative_to(ROOT).as_posix(),
        "supersedes": supersedes,
        "run": {
            "agent": agent,
            "model": model,
            "lineage": lineage,
            "tested_at": tested_at,
            "repository_commit": repository_commit,
            "response_path": response_path,
        },
        "scores": scores,
        "summary": {
            "verdict": "unscored",
            "critical_failure": False,
            "notes": "",
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_id", help="evaluation case or journey id")
    parser.add_argument("--agent", required=True, help="agent or runtime name")
    parser.add_argument("--model", required=True, help="model identifier")
    parser.add_argument(
        "--lineage", required=True, help="stable comparison lane, such as codex-gpt-5"
    )
    parser.add_argument("--response", required=True, help="repository-relative raw response path")
    parser.add_argument("--output", required=True, type=Path, help="draft report path")
    parser.add_argument(
        "--supersedes", help="repository-relative prior report replaced by this run"
    )
    parser.add_argument("--tested-at", default=date.today().isoformat(), help="ISO test date")
    parser.add_argument("--commit", default=current_commit(), help="tested repository commit")
    args = parser.parse_args(argv)

    try:
        case_path, case = find_case(args.case_id)
        report = build_report(
            case_path,
            case,
            agent=args.agent,
            model=args.model,
            lineage=args.lineage,
            tested_at=args.tested_at,
            repository_commit=args.commit,
            response_path=args.response,
            supersedes=args.supersedes,
        )
    except (OSError, ValueError, json.JSONDecodeError, KeyError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Created unscored draft: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
