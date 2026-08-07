from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "quality_summary.py"
SPEC = importlib.util.spec_from_file_location("quality_summary", MODULE_PATH)
assert SPEC and SPEC.loader
SUMMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUMMARY)


class QualitySummaryTests(unittest.TestCase):
    def test_summary_counts_catalog_and_latest_lineages(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for path in (
                root / "skills" / "test-skill",
                root / "examples" / "example",
                root / "reference-packs" / "pack",
                root / "evals" / "cases",
                root / "evals" / "journeys",
                root / "evals" / "results" / "run",
                root / "evals" / "routing" / "results",
            ):
                path.mkdir(parents=True, exist_ok=True)
            (root / "evals" / "cases" / "case.json").write_text(
                json.dumps({"id": "case"}), encoding="utf-8"
            )
            (root / "evals" / "journeys" / "journey.json").write_text(
                json.dumps({"id": "journey"}), encoding="utf-8"
            )
            (root / "evals" / "routing" / "cases.json").write_text(
                json.dumps({"cases": [{"id": "one"}, {"id": "two"}]}),
                encoding="utf-8",
            )
            prior = root / "evals" / "results" / "run" / "prior.json"
            prior.write_text(
                json.dumps(
                    {
                        "case_id": "case",
                        "supersedes": None,
                        "summary": {"verdict": "fail"},
                    }
                ),
                encoding="utf-8",
            )
            current = root / "evals" / "results" / "run" / "current.json"
            current.write_text(
                json.dumps(
                    {
                        "case_id": "case",
                        "supersedes": "evals/results/run/prior.json",
                        "summary": {"verdict": "pass"},
                    }
                ),
                encoding="utf-8",
            )
            routing = root / "evals" / "routing" / "results" / "route.json"
            routing.write_text(
                json.dumps(
                    {
                        "supersedes": None,
                        "summary": {"verdict": "partial", "total_cases": 2},
                    }
                ),
                encoding="utf-8",
            )

            result = SUMMARY.build_summary(root)
            self.assertEqual(
                result["catalog"],
                {
                    "skills": 1,
                    "isolated_cases": 1,
                    "journey_cases": 1,
                    "current_routing_cases": 2,
                    "example_workspaces": 1,
                    "reference_packs": 1,
                },
            )
            self.assertEqual(result["evidence"]["behavioral"]["latest_total"], 1)
            self.assertEqual(
                result["evidence"]["behavioral"]["latest_verdicts"]["pass"], 1
            )
            self.assertEqual(result["evidence"]["behavioral"]["historical_runs"], 1)
            self.assertEqual(
                result["evidence"]["behavioral"]["definition_coverage"],
                {
                    "definitions_total": 2,
                    "definitions_with_latest_result": 1,
                    "definitions_with_latest_pass": 1,
                    "definition_ids": ["case", "journey"],
                    "latest_result_ids": ["case"],
                    "latest_pass_ids": ["case"],
                    "latest_nonpass_ids": [],
                    "missing_latest_result_ids": ["journey"],
                },
            )
            self.assertEqual(
                result["evidence"]["routing"]["latest_verdicts"]["partial"], 1
            )
            self.assertEqual(result["evidence"]["routing"]["latest_case_counts"], [2])
            self.assertEqual(result["evidence"]["routing"]["current_corpus_lineages"], 0)
            self.assertEqual(
                result["evidence"]["routing"]["current_corpus_passing_lineages"], 0
            )

    def test_definition_coverage_names_current_nonpasses(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for path in (
                root / "skills" / "test-skill",
                root / "examples",
                root / "reference-packs",
                root / "evals" / "cases",
                root / "evals" / "journeys",
                root / "evals" / "results",
                root / "evals" / "routing" / "results",
            ):
                path.mkdir(parents=True, exist_ok=True)
            (root / "evals" / "cases" / "pass.json").write_text(
                json.dumps({"id": "passing-case"}), encoding="utf-8"
            )
            (root / "evals" / "cases" / "fail.json").write_text(
                json.dumps({"id": "failing-case"}), encoding="utf-8"
            )
            (root / "evals" / "journeys" / "missing.json").write_text(
                json.dumps({"id": "missing-journey"}), encoding="utf-8"
            )
            (root / "evals" / "routing" / "cases.json").write_text(
                json.dumps({"cases": []}), encoding="utf-8"
            )
            for case_id, verdict in (("passing-case", "pass"), ("failing-case", "fail")):
                (root / "evals" / "results" / f"{case_id}.json").write_text(
                    json.dumps(
                        {
                            "case_id": case_id,
                            "supersedes": None,
                            "summary": {"verdict": verdict},
                        }
                    ),
                    encoding="utf-8",
                )

            coverage = SUMMARY.build_summary(root)["evidence"]["behavioral"][
                "definition_coverage"
            ]

            self.assertEqual(coverage["latest_result_ids"], ["failing-case", "passing-case"])
            self.assertEqual(coverage["latest_pass_ids"], ["passing-case"])
            self.assertEqual(coverage["latest_nonpass_ids"], ["failing-case"])
            self.assertEqual(coverage["missing_latest_result_ids"], ["missing-journey"])


if __name__ == "__main__":
    unittest.main()
