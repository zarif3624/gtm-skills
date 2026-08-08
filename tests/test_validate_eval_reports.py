from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_eval_reports.py"
SPEC = importlib.util.spec_from_file_location("validate_eval_reports", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def source_case() -> dict[str, object]:
    return {
        "id": "test-case",
        "assertions": {
            "must_demonstrate": ["Label uncertainty."],
            "must_avoid": ["Invent facts."],
            "human_review": ["Surface approval."],
        },
    }


class EvalReportValidatorTests(unittest.TestCase):
    def make_report(self, root: Path) -> Path:
        case_path = root / "evals" / "cases" / "test-case.json"
        case_path.parent.mkdir(parents=True)
        case_path.write_text(json.dumps(source_case()), encoding="utf-8")
        response_path = root / "evals" / "results" / "run" / "response.md"
        response_path.parent.mkdir(parents=True)
        response_path.write_text("The response labels uncertainty.", encoding="utf-8")
        report = {
            "schema_version": 1,
            "case_id": "test-case",
            "case_type": "case",
            "case_path": "evals/cases/test-case.json",
            "supersedes": None,
            "run": {
                "agent": "Test agent",
                "model": "test-model",
                "lineage": "test-lineage",
                "tested_at": "2026-08-08",
                "repository_commit": "abcdef1",
                "response_path": "evals/results/run/response.md",
            },
            "scores": {
                category: [
                    {"assertion": assertion, "verdict": "pass", "evidence": "Paragraph 1"}
                    for assertion in assertions
                ]
                for category, assertions in source_case()["assertions"].items()  # type: ignore[union-attr]
            },
            "summary": {"verdict": "pass", "critical_failure": False, "notes": ""},
        }
        report_path = response_path.parent / "report.json"
        report_path.write_text(json.dumps(report), encoding="utf-8")
        return report_path

    def test_valid_final_report_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = self.make_report(root)
            self.assertEqual(VALIDATOR.validate_report(report, root), [])

    def test_boolean_schema_version_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = self.make_report(root)
            value = json.loads(report.read_text(encoding="utf-8"))
            value["schema_version"] = True
            report.write_text(json.dumps(value), encoding="utf-8")
            self.assertIn(
                "schema_version must be 1", VALIDATOR.validate_report(report, root)
            )

    def test_unscored_draft_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = self.make_report(root)
            value = json.loads(report.read_text(encoding="utf-8"))
            value["scores"]["must_demonstrate"][0]["verdict"] = "unscored"
            value["scores"]["must_demonstrate"][0]["evidence"] = ""
            value["summary"]["verdict"] = "partial"
            report.write_text(json.dumps(value), encoding="utf-8")
            errors = VALIDATOR.validate_report(report, root)
            self.assertIn(
                "scores.must_demonstrate[1].verdict must be pass, partial, or fail", errors
            )
            self.assertIn(
                "scores.must_demonstrate[1].evidence must cite response evidence", errors
            )

    def test_prohibited_failure_requires_critical_flag(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = self.make_report(root)
            value = json.loads(report.read_text(encoding="utf-8"))
            value["scores"]["must_avoid"][0]["verdict"] = "fail"
            value["summary"]["verdict"] = "fail"
            report.write_text(json.dumps(value), encoding="utf-8")
            errors = VALIDATOR.validate_report(report, root)
            self.assertIn(
                "summary.critical_failure must be true exactly when a prohibited-behavior "
                "assertion fails",
                errors,
            )

    def test_assertion_text_cannot_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = self.make_report(root)
            value = json.loads(report.read_text(encoding="utf-8"))
            value["scores"]["must_demonstrate"][0]["assertion"] = "A weaker assertion."
            report.write_text(json.dumps(value), encoding="utf-8")
            errors = VALIDATOR.validate_report(report, root)
            self.assertIn(
                "scores.must_demonstrate[1].assertion must exactly match the source", errors
            )

    def test_malformed_scores_fail_without_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = self.make_report(root)
            value = json.loads(report.read_text(encoding="utf-8"))
            value["scores"]["must_demonstrate"] = "not a score list"
            report.write_text(json.dumps(value), encoding="utf-8")
            errors = VALIDATOR.validate_report(report, root)
            self.assertIn(
                "scores.must_demonstrate must score every source assertion once", errors
            )

    def test_superseded_report_must_match_case(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = self.make_report(root)
            prior = report.parent / "prior.json"
            prior.write_text(
                json.dumps({
                    "case_id": "other-case",
                    "case_type": "case",
                    "case_path": "x",
                    "run": {"lineage": "test-lineage"},
                }),
                encoding="utf-8",
            )
            value = json.loads(report.read_text(encoding="utf-8"))
            value["supersedes"] = "evals/results/run/prior.json"
            report.write_text(json.dumps(value), encoding="utf-8")
            errors = VALIDATOR.validate_report(report, root)
            self.assertIn("superseded report must have the same case_id", errors)


if __name__ == "__main__":
    unittest.main()
