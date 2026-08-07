from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_quality_policy.py"
SPEC = importlib.util.spec_from_file_location("validate_quality_policy", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def summary(passes: int = 3, partial: int = 0) -> dict[str, object]:
    return {
        "catalog": {"isolated_cases": 3, "journey_cases": 2, "current_routing_cases": 4},
        "evidence": {
            "behavioral": {
                "definition_coverage": {
                    "definitions_with_latest_result": 3,
                    "definitions_with_latest_pass": passes,
                    "missing_latest_result_ids": [],
                },
                "latest_verdicts": {"pass": passes, "partial": partial, "fail": 0},
            },
            "routing": {
                "current_corpus_passing_lineages": 1,
                "latest_verdicts": {"pass": 1, "partial": 0, "fail": 0},
            },
        },
    }


def policy() -> dict[str, object]:
    return {
        "schema_version": 1,
        "minimums": {
            "isolated_cases": 3,
            "journey_cases": 2,
            "current_routing_cases": 4,
            "behavioral_definitions_with_latest_result": 3,
            "behavioral_definitions_with_latest_pass": 3,
            "current_corpus_passing_lineages": 1,
        },
        "maximums": {
            "behavioral_definitions_missing_latest_result": 0,
            "latest_behavioral_partial": 0,
            "latest_behavioral_fail": 0,
            "latest_routing_partial": 0,
            "latest_routing_fail": 0,
        },
    }


class QualityPolicyTests(unittest.TestCase):
    def test_policy_passes_at_threshold(self) -> None:
        self.assertEqual(VALIDATOR.validate_policy(policy(), summary()), [])

    def test_regressed_pass_coverage_fails(self) -> None:
        errors = VALIDATOR.validate_policy(policy(), summary(passes=2))
        self.assertTrue(any("fell below the reviewed minimum" in error for error in errors))

    def test_new_partial_fails(self) -> None:
        errors = VALIDATOR.validate_policy(policy(), summary(partial=1))
        self.assertTrue(any("exceeded the reviewed maximum" in error for error in errors))

    def test_uncovered_definition_fails_even_when_absolute_floor_passes(self) -> None:
        observed = summary()
        observed["evidence"]["behavioral"]["definition_coverage"][
            "missing_latest_result_ids"
        ] = ["new-definition"]
        errors = VALIDATOR.validate_policy(policy(), observed)
        self.assertTrue(any("missing_latest_result" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
