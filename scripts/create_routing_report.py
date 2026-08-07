#!/usr/bin/env python3
"""Create a finalized routing report from one blind run response."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def current_commit() -> str:
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=False, capture_output=True, text=True
    )
    return completed.stdout.strip() if completed.returncode == 0 else "unknown"


def calculate_summary(corpus: dict[str, Any], response: dict[str, Any]) -> dict[str, Any]:
    cases = {case["id"]: case for case in corpus["cases"]}
    selections = {
        selection["id"]: set(selection["selected_skills"])
        for selection in response["selections"]
        if selection.get("id") in cases
    }
    exact_matches = 0
    expected_covered = 0
    excluded_selected = 0
    for case_id, case in cases.items():
        selected = selections.get(case_id, set())
        expected = set(case["expected_skills"])
        excluded = set(case["excluded_skills"])
        exact_matches += selected == expected
        expected_covered += expected.issubset(selected)
        excluded_selected += bool(selected & excluded)
    total = len(cases)
    if exact_matches == total and not excluded_selected:
        verdict = "pass"
    elif expected_covered < total or excluded_selected:
        verdict = "fail"
    else:
        verdict = "partial"
    return {
        "total_cases": total,
        "exact_matches": exact_matches,
        "expected_covered": expected_covered,
        "excluded_selected": excluded_selected,
        "verdict": verdict,
    }


def build_report(
    corpus: dict[str, Any], *, corpus_path: str, agent: str, model: str,
    lineage: str, tested_at: str, repository_commit: str, response_path: str,
    supersedes: str | None = None
) -> dict[str, Any]:
    response = json.loads((ROOT / response_path).read_text(encoding="utf-8"))
    return {
        "schema_version": 1,
        "corpus_path": corpus_path,
        "supersedes": supersedes,
        "run": {
            "agent": agent,
            "model": model,
            "lineage": lineage,
            "tested_at": tested_at,
            "repository_commit": repository_commit,
            "response_path": response_path,
        },
        "summary": calculate_summary(corpus, response),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--lineage", required=True)
    parser.add_argument(
        "--corpus", type=Path, required=True,
        help="repository-relative immutable corpus snapshot",
    )
    parser.add_argument("--response", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--supersedes")
    parser.add_argument("--tested-at", default=date.today().isoformat())
    parser.add_argument("--commit", default=current_commit())
    args = parser.parse_args(argv)
    try:
        corpus_path = (ROOT / args.corpus).resolve()
        if corpus_path.parent != (ROOT / "evals" / "routing" / "corpora").resolve():
            raise ValueError("--corpus must point directly into evals/routing/corpora")
        response_path = (ROOT / args.response).resolve()
        if not response_path.is_relative_to(
            (ROOT / "evals" / "routing" / "results").resolve()
        ):
            raise ValueError("--response must stay under evals/routing/results")
        corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
        report = build_report(
            corpus,
            corpus_path=corpus_path.relative_to(ROOT).as_posix(),
            agent=args.agent,
            model=args.model,
            lineage=args.lineage,
            tested_at=args.tested_at,
            repository_commit=args.commit,
            response_path=response_path.relative_to(ROOT).as_posix(),
            supersedes=args.supersedes,
        )
    except (OSError, ValueError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Created routing report: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
