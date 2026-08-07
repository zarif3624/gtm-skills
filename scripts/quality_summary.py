#!/usr/bin/env python3
"""Build or verify the repository's machine-readable quality summary."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "quality-summary.json"
VERDICTS = ("pass", "partial", "fail")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def count_directories(path: Path) -> int:
    return sum(item.is_dir() for item in path.iterdir()) if path.is_dir() else 0


def evidence_summary(
    reports: dict[Path, dict[str, Any]], root: Path, *, include_case_counts: bool = False
) -> dict[str, Any]:
    superseded = {
        (root / report["supersedes"]).resolve()
        for report in reports.values()
        if report.get("supersedes")
    }
    latest = [report for path, report in reports.items() if path not in superseded]
    counts = {verdict: 0 for verdict in VERDICTS}
    for report in latest:
        counts[report["summary"]["verdict"]] += 1
    summary = {
        "reports_total": len(reports),
        "latest_total": len(latest),
        "latest_verdicts": counts,
        "historical_runs": len(reports) - len(latest),
    }
    if include_case_counts:
        summary["latest_case_counts"] = sorted(
            {report["summary"]["total_cases"] for report in latest}
        )
    return summary


def latest_reports(
    reports: dict[Path, dict[str, Any]], root: Path
) -> list[dict[str, Any]]:
    superseded = {
        (root / report["supersedes"]).resolve()
        for report in reports.values()
        if report.get("supersedes")
    }
    return [report for path, report in reports.items() if path not in superseded]


def build_summary(root: Path = ROOT) -> dict[str, Any]:
    routing = load_json(root / "evals" / "routing" / "cases.json")
    definition_paths = sorted((root / "evals" / "cases").glob("*.json")) + sorted(
        (root / "evals" / "journeys").glob("*.json")
    )
    definition_ids = {load_json(path)["id"] for path in definition_paths}
    behavior_paths = sorted((root / "evals" / "results").rglob("*.json"))
    behavior_reports = {path.resolve(): load_json(path) for path in behavior_paths}
    routing_paths = sorted((root / "evals" / "routing" / "results").glob("*.json"))
    routing_reports = {
        path.resolve(): load_json(path)
        for path in routing_paths
        if not path.name.endswith(".response.json")
    }
    current_behavior = latest_reports(behavior_reports, root)
    behavior_with_result = {
        report["case_id"] for report in current_behavior if report.get("case_id")
    }
    behavior_with_pass = {
        report["case_id"]
        for report in current_behavior
        if report.get("case_id") and report["summary"]["verdict"] == "pass"
    }
    current_routing = []
    for report in latest_reports(routing_reports, root):
        corpus_value = report.get("corpus_path")
        if not isinstance(corpus_value, str):
            continue
        corpus_path = root / corpus_value
        if load_json(corpus_path) == routing:
            current_routing.append(report)
    behavioral = evidence_summary(behavior_reports, root)
    behavioral["definition_coverage"] = {
        "definitions_total": len(definition_ids),
        "definitions_with_latest_result": len(behavior_with_result),
        "definitions_with_latest_pass": len(behavior_with_pass),
        "definition_ids": sorted(definition_ids),
        "latest_result_ids": sorted(behavior_with_result),
        "latest_pass_ids": sorted(behavior_with_pass),
        "latest_nonpass_ids": sorted(behavior_with_result - behavior_with_pass),
        "missing_latest_result_ids": sorted(definition_ids - behavior_with_result),
    }
    routing_evidence = evidence_summary(
        routing_reports, root, include_case_counts=True
    )
    routing_evidence["current_corpus_lineages"] = len(current_routing)
    routing_evidence["current_corpus_passing_lineages"] = sum(
        report["summary"]["verdict"] == "pass" for report in current_routing
    )
    return {
        "schema_version": 1,
        "catalog": {
            "skills": count_directories(root / "skills"),
            "isolated_cases": len(list((root / "evals" / "cases").glob("*.json"))),
            "journey_cases": len(list((root / "evals" / "journeys").glob("*.json"))),
            "current_routing_cases": len(routing["cases"]),
            "example_workspaces": count_directories(root / "examples"),
            "reference_packs": count_directories(root / "reference-packs"),
        },
        "evidence": {
            "behavioral": behavioral,
            "routing": routing_evidence,
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", action="store_true", help="update quality-summary.json")
    action.add_argument("--check", action="store_true", help="fail when the summary is stale")
    args = parser.parse_args(argv)
    try:
        summary = build_summary()
        rendered = json.dumps(summary, indent=2) + "\n"
        if args.write:
            SUMMARY_PATH.write_text(rendered, encoding="utf-8")
            print(f"Updated {SUMMARY_PATH.relative_to(ROOT)}")
        elif args.check:
            current = SUMMARY_PATH.read_text(encoding="utf-8")
            if current != rendered:
                print("FAIL quality-summary.json is stale; run scripts/quality_summary.py --write")
                return 1
            print("PASS quality-summary.json")
        else:
            print(rendered, end="")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
