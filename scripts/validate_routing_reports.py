#!/usr/bin/env python3
"""Validate blind routing run responses and their computed reports."""

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

from create_routing_report import calculate_summary
from validate_lineage import validate_lineage_graph


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "evals" / "routing" / "results"
REPORT_FIELDS = {"schema_version", "corpus_path", "supersedes", "run", "summary"}
RUN_FIELDS = {"agent", "model", "lineage", "tested_at", "repository_commit", "response_path"}
SUMMARY_FIELDS = {"total_cases", "exact_matches", "expected_covered", "excluded_selected", "verdict"}
RESPONSE_FIELDS = {"selections"}
SELECTION_FIELDS = {"id", "selected_skills", "rationale"}
COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$", re.IGNORECASE)


def load_json(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return None, [f"invalid JSON: {error}"]
    return (value, []) if isinstance(value, dict) else (None, ["must be a JSON object"])


def resolve_path(raw: Any, field: str, root: Path) -> tuple[Path | None, list[str]]:
    if not isinstance(raw, str) or not raw.strip():
        return None, [f"{field} must be a non-empty repository-relative path"]
    path = (root / raw).resolve()
    if not path.is_relative_to(root.resolve()):
        return None, [f"{field} escapes the repository"]
    if not path.is_file():
        return None, [f"{field} does not exist: {raw}"]
    return path, []


def validate_response(
    response: dict[str, Any], corpus: dict[str, Any], skill_names: set[str]
) -> list[str]:
    errors: list[str] = []
    if set(response) != RESPONSE_FIELDS or not isinstance(response.get("selections"), list):
        return ["response must contain exactly one selections array"]
    case_ids = [case["id"] for case in corpus["cases"]]
    seen: list[str] = []
    for index, selection in enumerate(response["selections"], start=1):
        prefix = f"selections[{index}]"
        if not isinstance(selection, dict) or set(selection) != SELECTION_FIELDS:
            errors.append(f"{prefix} must contain exactly id, selected_skills, and rationale")
            continue
        case_id = selection["id"]
        if not isinstance(case_id, str):
            errors.append(f"{prefix}.id must be a string")
        else:
            seen.append(case_id)
        selected = selection["selected_skills"]
        if not isinstance(selected, list) or not all(isinstance(item, str) for item in selected):
            errors.append(f"{prefix}.selected_skills must be a list of skill names")
        else:
            if len(selected) != len(set(selected)):
                errors.append(f"{prefix}.selected_skills must not contain duplicates")
            unknown = sorted(set(selected) - skill_names)
            if unknown:
                errors.append(f"{prefix}.selected_skills has unknown skills: {', '.join(unknown)}")
        if not isinstance(selection["rationale"], str) or not selection["rationale"].strip():
            errors.append(f"{prefix}.rationale must be a non-empty string")
    if seen != case_ids:
        errors.append("response must select every corpus case exactly once in corpus order")
    return errors


def validate_report(path: Path, root: Path = ROOT) -> list[str]:
    if path.is_symlink():
        return ["routing report must not be a symbolic link"]
    report, errors = load_json(path)
    if report is None:
        return errors
    if set(report) != REPORT_FIELDS:
        errors.append(f"report fields must be exactly: {', '.join(sorted(REPORT_FIELDS))}")
    if type(report.get("schema_version")) is not int or report["schema_version"] != 1:
        errors.append("schema_version must be 1")
    corpus_path, path_errors = resolve_path(report.get("corpus_path"), "corpus_path", root)
    errors.extend(path_errors)
    corpus = None
    if corpus_path:
        corpora = (root / "evals" / "routing" / "corpora").resolve()
        if corpus_path.parent != corpora:
            errors.append("corpus_path must point directly into evals/routing/corpora")
        corpus, corpus_errors = load_json(corpus_path)
        errors.extend(f"corpus {error}" for error in corpus_errors)

    run = report.get("run")
    response = None
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
        if not isinstance(run["repository_commit"], str) or not COMMIT_RE.fullmatch(run["repository_commit"]):
            errors.append("run.repository_commit must be a 7-40 character Git commit")
        response_path, response_errors = resolve_path(run["response_path"], "run.response_path", root)
        errors.extend(response_errors)
        if response_path:
            if not response_path.is_relative_to((root / "evals" / "routing" / "results").resolve()):
                errors.append("run.response_path must stay under evals/routing/results")
            response, load_errors = load_json(response_path)
            errors.extend(f"response {error}" for error in load_errors)

    supersedes = report.get("supersedes")
    if supersedes is not None:
        prior_path, prior_errors = resolve_path(supersedes, "supersedes", root)
        errors.extend(prior_errors)
        if prior_path:
            if not prior_path.is_relative_to(
                (root / "evals" / "routing" / "results").resolve()
            ):
                errors.append("supersedes must stay under evals/routing/results")
            if prior_path == path.resolve():
                errors.append("a routing report cannot supersede itself")
            prior, prior_load_errors = load_json(prior_path)
            errors.extend(f"superseded report {error}" for error in prior_load_errors)
            if prior:
                prior_run = prior.get("run")
                if not isinstance(prior_run, dict) or not isinstance(run, dict) or prior_run.get("lineage") != run.get("lineage"):
                    errors.append("superseded report must have the same run.lineage")

    summary = report.get("summary")
    if not isinstance(summary, dict) or set(summary) != SUMMARY_FIELDS:
        errors.append(f"summary must contain exactly: {', '.join(sorted(SUMMARY_FIELDS))}")
    else:
        for field in (
            "total_cases",
            "exact_matches",
            "expected_covered",
            "excluded_selected",
        ):
            if type(summary[field]) is not int or summary[field] < 0:
                errors.append(f"summary.{field} must be a non-negative integer")
        if summary["verdict"] not in {"pass", "partial", "fail"}:
            errors.append("summary.verdict must be pass, partial, or fail")
    if corpus and response:
        skill_names = {item.name for item in (root / "skills").iterdir() if item.is_dir()}
        errors.extend(validate_response(response, corpus, skill_names))
        calculated = calculate_summary(corpus, response)
        if isinstance(summary, dict) and set(summary) == SUMMARY_FIELDS and summary != calculated:
            errors.append(f"summary must match computed routing result: {calculated}")
    return errors


def main() -> int:
    reports = sorted(RESULTS.glob("*.json")) if RESULTS.is_dir() else []
    reports = [path for path in reports if not path.name.endswith(".response.json")]
    failures = 0
    valid_reports: dict[Path, dict[str, Any]] = {}
    for path in reports:
        errors = validate_report(path)
        failures += bool(errors)
        print(f"{'FAIL' if errors else 'PASS'} {path.relative_to(RESULTS)}")
        for error in errors:
            print(f"  - {error}")
        if not errors:
            report, _ = load_json(path)
            if report:
                valid_reports[path.resolve()] = report
    print(f"\nValidated {len(reports)} routing reports; {failures} invalid.")
    lineage_errors = validate_lineage_graph(
        valid_reports, ROOT, identity_fields=("run.lineage",)
    )
    if lineage_errors:
        failures += 1
        print("FAIL routing report lineages")
        for error in lineage_errors:
            print(f"  - {error}")
    superseded = {
        (ROOT / report["supersedes"]).resolve()
        for report in valid_reports.values()
        if report.get("supersedes")
    }
    latest = [report for path, report in valid_reports.items() if path not in superseded]
    verdicts = {"pass": 0, "partial": 0, "fail": 0}
    for report in latest:
        verdicts[report["summary"]["verdict"]] += 1
    print(
        f"Latest by lineage: {len(latest)} reports; {verdicts['pass']} pass, "
        f"{verdicts['partial']} partial, {verdicts['fail']} fail."
    )
    print(f"Historical routing runs retained: {len(valid_reports) - len(latest)}.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
