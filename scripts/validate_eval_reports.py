#!/usr/bin/env python3
"""Validate finalized behavioral evaluation reports and their source evidence."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validate_lineage import validate_lineage_graph


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "evals" / "results"
TOP_LEVEL_FIELDS = {
    "schema_version",
    "case_id",
    "case_type",
    "case_path",
    "supersedes",
    "run",
    "scores",
    "summary",
}
RUN_FIELDS = {
    "agent", "model", "lineage", "tested_at", "repository_commit", "response_path"
}
SUMMARY_FIELDS = {"verdict", "critical_failure", "notes"}
SCORE_FIELDS = {"assertion", "verdict", "evidence"}
FINAL_VERDICTS = {"pass", "partial", "fail"}
COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$", re.IGNORECASE)


def load_json(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return None, [f"invalid JSON: {error}"]
    if not isinstance(value, dict):
        return None, ["report must be a JSON object"]
    return value, []


def resolve_repository_path(raw: Any, field: str, root: Path) -> tuple[Path | None, list[str]]:
    if not isinstance(raw, str) or not raw.strip():
        return None, [f"{field} must be a non-empty repository-relative path"]
    path = (root / raw).resolve()
    if not path.is_relative_to(root.resolve()):
        return None, [f"{field} escapes the repository"]
    if not path.is_file():
        return None, [f"{field} does not exist: {raw}"]
    return path, []


def expected_verdict(scores: dict[str, Any]) -> str | None:
    if not all(
        isinstance(items, list) and all(isinstance(item, dict) for item in items)
        for items in scores.values()
    ):
        return None
    verdicts = [item.get("verdict") for items in scores.values() for item in items]
    if not verdicts or any(verdict not in FINAL_VERDICTS for verdict in verdicts):
        return None
    if verdicts and all(verdict == "pass" for verdict in verdicts):
        return "pass"
    if "fail" in verdicts:
        return "fail"
    return "partial"


def validate_report(path: Path, root: Path = ROOT) -> list[str]:
    if path.is_symlink():
        return ["evaluation report must not be a symbolic link"]
    report, errors = load_json(path)
    if report is None:
        return errors
    if set(report) != TOP_LEVEL_FIELDS:
        errors.append(f"report fields must be exactly: {', '.join(sorted(TOP_LEVEL_FIELDS))}")
    if type(report.get("schema_version")) is not int or report["schema_version"] != 1:
        errors.append("schema_version must be 1")

    case_path, path_errors = resolve_repository_path(report.get("case_path"), "case_path", root)
    errors.extend(path_errors)
    source: dict[str, Any] | None = None
    if case_path:
        allowed_case_dirs = {
            (root / "evals" / "cases").resolve(),
            (root / "evals" / "journeys").resolve(),
        }
        if case_path.parent not in allowed_case_dirs:
            errors.append("case_path must point directly into evals/cases or evals/journeys")
        source, source_errors = load_json(case_path)
        errors.extend(f"case source {error}" for error in source_errors)
        expected_type = "case" if case_path.parent.name == "cases" else "journey"
        if report.get("case_type") != expected_type:
            errors.append(f"case_type must be {expected_type}")
        if source and report.get("case_id") != source.get("id"):
            errors.append("case_id must match the source case")
        if report.get("case_id") != case_path.stem:
            errors.append("case_id must match the source filename")

    supersedes = report.get("supersedes")
    if supersedes is not None:
        prior, prior_errors = resolve_repository_path(supersedes, "supersedes", root)
        errors.extend(prior_errors)
        if prior:
            if not prior.is_relative_to((root / "evals" / "results").resolve()):
                errors.append("supersedes must stay under evals/results")
            if prior == path.resolve():
                errors.append("a report cannot supersede itself")
            prior_report, prior_load_errors = load_json(prior)
            errors.extend(f"superseded report {error}" for error in prior_load_errors)
            if prior_report:
                for field in ("case_id", "case_type", "case_path"):
                    if prior_report.get(field) != report.get(field):
                        errors.append(f"superseded report must have the same {field}")
                prior_run = prior_report.get("run")
                current_run = report.get("run")
                if (
                    not isinstance(prior_run, dict)
                    or not isinstance(current_run, dict)
                    or prior_run.get("lineage") != current_run.get("lineage")
                ):
                    errors.append("superseded report must have the same run.lineage")

    run = report.get("run")
    if not isinstance(run, dict) or set(run) != RUN_FIELDS:
        errors.append(f"run must contain exactly: {', '.join(sorted(RUN_FIELDS))}")
    else:
        for field in ("agent", "model", "lineage"):
            if not isinstance(run[field], str) or not run[field].strip():
                errors.append(f"run.{field} must be a non-empty string")
        try:
            date.fromisoformat(run["tested_at"])
        except (TypeError, ValueError):
            errors.append("run.tested_at must be an ISO date")
        if not isinstance(run["repository_commit"], str) or not COMMIT_RE.fullmatch(
            run["repository_commit"]
        ):
            errors.append("run.repository_commit must be a 7-40 character Git commit")
        response, response_errors = resolve_repository_path(
            run["response_path"], "run.response_path", root
        )
        errors.extend(response_errors)
        if response and not response.is_relative_to((root / "evals" / "results").resolve()):
            errors.append("run.response_path must stay under evals/results")

    scores = report.get("scores")
    source_assertions = source.get("assertions") if source else None
    if not isinstance(scores, dict) or not isinstance(source_assertions, dict):
        errors.append("scores must map every source assertion category")
    elif set(scores) != set(source_assertions):
        errors.append("score categories must exactly match the source assertions")
    else:
        for category, assertions in source_assertions.items():
            items = scores[category]
            if not isinstance(items, list) or len(items) != len(assertions):
                errors.append(f"scores.{category} must score every source assertion once")
                continue
            for index, (item, assertion) in enumerate(zip(items, assertions), start=1):
                prefix = f"scores.{category}[{index}]"
                if not isinstance(item, dict) or set(item) != SCORE_FIELDS:
                    errors.append(f"{prefix} must contain assertion, verdict, and evidence")
                    continue
                if item["assertion"] != assertion:
                    errors.append(f"{prefix}.assertion must exactly match the source")
                if item["verdict"] not in FINAL_VERDICTS:
                    errors.append(f"{prefix}.verdict must be pass, partial, or fail")
                if not isinstance(item["evidence"], str) or not item["evidence"].strip():
                    errors.append(f"{prefix}.evidence must cite response evidence")

    summary = report.get("summary")
    if not isinstance(summary, dict) or set(summary) != SUMMARY_FIELDS:
        errors.append(f"summary must contain exactly: {', '.join(sorted(SUMMARY_FIELDS))}")
    elif isinstance(scores, dict):
        calculated = expected_verdict(scores)
        if calculated and summary["verdict"] != calculated:
            errors.append(f"summary.verdict must be {calculated} from assertion scores")
        if not isinstance(summary["critical_failure"], bool):
            errors.append("summary.critical_failure must be true or false")
        else:
            prohibited = scores.get("must_avoid", scores.get("must_not_transform", []))
            requires_critical = any(
                isinstance(item, dict) and item.get("verdict") == "fail" for item in prohibited
            )
            if summary["critical_failure"] != requires_critical:
                errors.append(
                    "summary.critical_failure must be true exactly when a prohibited-behavior "
                    "assertion fails"
                )
        if not isinstance(summary["notes"], str):
            errors.append("summary.notes must be a string")
    return errors


def main() -> int:
    if not RESULTS.is_dir():
        print("FAIL evals/results directory is missing")
        return 1
    reports = sorted(RESULTS.rglob("*.json"))
    failures = 0
    verdict_counts = {"pass": 0, "partial": 0, "fail": 0}
    valid_reports: dict[Path, dict[str, Any]] = {}
    for report_path in reports:
        errors = validate_report(report_path)
        failures += bool(errors)
        print(f"{'FAIL' if errors else 'PASS'} {report_path.relative_to(RESULTS)}")
        for error in errors:
            print(f"  - {error}")
        if not errors:
            report = json.loads(report_path.read_text(encoding="utf-8"))
            valid_reports[report_path.resolve()] = report
            verdict_counts[report["summary"]["verdict"]] += 1

    superseded = {
        (ROOT / report["supersedes"]).resolve()
        for report in valid_reports.values()
        if report.get("supersedes")
    }
    latest = [report for path, report in valid_reports.items() if path not in superseded]
    lineage_errors = validate_lineage_graph(
        valid_reports,
        ROOT,
        identity_fields=("case_id", "case_type", "run.lineage"),
    )
    if lineage_errors:
        failures += 1
        print("FAIL report lineages")
        for error in lineage_errors:
            print(f"  - {error}")
    latest_counts = {"pass": 0, "partial": 0, "fail": 0}
    for report in latest:
        latest_counts[report["summary"]["verdict"]] += 1
    print(f"\nValidated {len(reports)} finalized reports; {failures} invalid.")
    print(
        f"Latest by case and lineage: {len(latest)} reports; "
        f"{latest_counts['pass']} pass, "
        f"{latest_counts['partial']} partial, {latest_counts['fail']} fail."
    )
    print(
        f"Historical runs retained: {len(valid_reports) - len(latest)} "
        f"({verdict_counts['pass']} pass, {verdict_counts['partial']} partial, "
        f"{verdict_counts['fail']} fail across all runs)."
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
