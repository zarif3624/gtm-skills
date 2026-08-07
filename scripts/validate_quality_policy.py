#!/usr/bin/env python3
"""Enforce the reviewed quality ratchet against the generated summary."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "quality-policy.json"
SUMMARY_PATH = ROOT / "quality-summary.json"
MINIMUM_FIELDS = {
    "isolated_cases",
    "journey_cases",
    "current_routing_cases",
    "behavioral_definitions_with_latest_result",
    "behavioral_definitions_with_latest_pass",
    "current_corpus_passing_lineages",
}
MAXIMUM_FIELDS = {
    "behavioral_definitions_missing_latest_result",
    "latest_behavioral_partial",
    "latest_behavioral_fail",
    "latest_routing_partial",
    "latest_routing_fail",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def observed_values(summary: dict[str, Any]) -> dict[str, int]:
    catalog = summary["catalog"]
    behavioral = summary["evidence"]["behavioral"]
    routing = summary["evidence"]["routing"]
    coverage = behavioral["definition_coverage"]
    return {
        "isolated_cases": catalog["isolated_cases"],
        "journey_cases": catalog["journey_cases"],
        "current_routing_cases": catalog["current_routing_cases"],
        "behavioral_definitions_with_latest_result": coverage[
            "definitions_with_latest_result"
        ],
        "behavioral_definitions_with_latest_pass": coverage[
            "definitions_with_latest_pass"
        ],
        "current_corpus_passing_lineages": routing[
            "current_corpus_passing_lineages"
        ],
        "behavioral_definitions_missing_latest_result": len(
            coverage["missing_latest_result_ids"]
        ),
        "latest_behavioral_partial": behavioral["latest_verdicts"]["partial"],
        "latest_behavioral_fail": behavioral["latest_verdicts"]["fail"],
        "latest_routing_partial": routing["latest_verdicts"]["partial"],
        "latest_routing_fail": routing["latest_verdicts"]["fail"],
    }


def validate_policy(policy: dict[str, Any], summary: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(policy) != {"schema_version", "minimums", "maximums"}:
        return ["quality policy must contain exactly schema_version, minimums, and maximums"]
    if policy["schema_version"] != 1:
        errors.append("quality policy schema_version must be 1")
    minimums = policy["minimums"]
    maximums = policy["maximums"]
    if not isinstance(minimums, dict) or set(minimums) != MINIMUM_FIELDS:
        errors.append("quality policy minimum fields do not match the contract")
    if not isinstance(maximums, dict) or set(maximums) != MAXIMUM_FIELDS:
        errors.append("quality policy maximum fields do not match the contract")
    if errors:
        return errors
    if any(not isinstance(value, int) or value < 0 for value in minimums.values()):
        errors.append("quality policy minimums must be non-negative integers")
    if any(not isinstance(value, int) or value < 0 for value in maximums.values()):
        errors.append("quality policy maximums must be non-negative integers")
    if errors:
        return errors
    observed = observed_values(summary)
    for field, threshold in minimums.items():
        if observed[field] < threshold:
            errors.append(f"{field} fell below the reviewed minimum: {observed[field]} < {threshold}")
    for field, threshold in maximums.items():
        if observed[field] > threshold:
            errors.append(f"{field} exceeded the reviewed maximum: {observed[field]} > {threshold}")
    return errors


def main() -> int:
    try:
        errors = validate_policy(load_json(POLICY_PATH), load_json(SUMMARY_PATH))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"FAIL {error}")
        return 1
    if errors:
        print("FAIL quality-policy.json")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("PASS quality-policy.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
