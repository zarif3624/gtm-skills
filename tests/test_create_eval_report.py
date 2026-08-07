from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "create_eval_report.py"
SPEC = importlib.util.spec_from_file_location("create_eval_report", MODULE_PATH)
assert SPEC and SPEC.loader
CREATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CREATOR)


class EvalReportCreatorTests(unittest.TestCase):
    def test_build_report_preserves_assertions_as_unscored(self) -> None:
        case_path = CREATOR.ROOT / "evals" / "cases" / "test-case.json"
        case = {
            "id": "test-case",
            "assertions": {"must_demonstrate": ["Label uncertainty."]},
        }
        report = CREATOR.build_report(
            case_path,
            case,
            agent="Test agent",
            model="test-model",
            tested_at="2026-08-08",
            repository_commit="abcdef1",
            response_path="evals/results/run/response.md",
        )
        self.assertEqual(report["case_type"], "case")
        self.assertEqual(
            report["scores"]["must_demonstrate"],
            [{"assertion": "Label uncertainty.", "verdict": "unscored", "evidence": ""}],
        )
        self.assertEqual(report["summary"]["verdict"], "unscored")


if __name__ == "__main__":
    unittest.main()
