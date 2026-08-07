from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PACKET = load_module("create_routing_packet", "create_routing_packet.py")
CREATOR = load_module("create_routing_report", "create_routing_report.py")
VALIDATOR = load_module("validate_routing_reports", "validate_routing_reports.py")


def corpus() -> dict[str, object]:
    return {
        "schema_version": 1,
        "cases": [
            {
                "id": "first-case",
                "prompt": "Complete the first job.",
                "expected_skills": ["first-skill"],
                "excluded_skills": ["second-skill"],
            },
            {
                "id": "combined-case",
                "prompt": "Complete both jobs.",
                "expected_skills": ["first-skill", "second-skill"],
                "excluded_skills": ["third-skill"],
            },
        ],
    }


def response(second_selection: list[str] | None = None) -> dict[str, object]:
    return {
        "selections": [
            {
                "id": "first-case",
                "selected_skills": ["first-skill"],
                "rationale": "The first skill directly owns this job.",
            },
            {
                "id": "combined-case",
                "selected_skills": second_selection or ["first-skill", "second-skill"],
                "rationale": "The request explicitly combines both jobs.",
            },
        ]
    }


class RoutingReportTests(unittest.TestCase):
    def test_packet_hides_expected_and_excluded_labels(self) -> None:
        packet = PACKET.render_packet(corpus())
        self.assertIn("Complete the first job.", packet)
        self.assertNotIn("expected_skills", packet)
        self.assertNotIn("excluded_skills", packet)
        self.assertNotIn("first-skill", packet)

    def test_exact_selection_passes(self) -> None:
        self.assertEqual(
            CREATOR.calculate_summary(corpus(), response()),
            {
                "total_cases": 2,
                "exact_matches": 2,
                "expected_covered": 2,
                "excluded_selected": 0,
                "verdict": "pass",
            },
        )

    def test_extra_skill_is_partial_and_excluded_neighbor_fails(self) -> None:
        partial = CREATOR.calculate_summary(
            corpus(), response(["first-skill", "second-skill", "other-skill"])
        )
        self.assertEqual(partial["verdict"], "partial")
        failed = CREATOR.calculate_summary(
            corpus(), response(["first-skill", "second-skill", "third-skill"])
        )
        self.assertEqual(failed["verdict"], "fail")
        self.assertEqual(failed["excluded_selected"], 1)

    def make_repository(self, root: Path) -> Path:
        corpus_path = root / "evals" / "routing" / "corpora" / "test-v1.json"
        corpus_path.parent.mkdir(parents=True)
        corpus_path.write_text(json.dumps(corpus()), encoding="utf-8")
        for name in ("first-skill", "second-skill", "third-skill"):
            (root / "skills" / name).mkdir(parents=True)
        results = root / "evals" / "routing" / "results"
        results.mkdir()
        response_path = results / "run.response.json"
        response_path.write_text(json.dumps(response()), encoding="utf-8")
        report = {
            "schema_version": 1,
            "corpus_path": "evals/routing/corpora/test-v1.json",
            "supersedes": None,
            "run": {
                "agent": "Test agent",
                "model": "test-model",
                "lineage": "test-lineage",
                "tested_at": "2026-08-08",
                "repository_commit": "abcdef1",
                "response_path": "evals/routing/results/run.response.json",
            },
            "summary": CREATOR.calculate_summary(corpus(), response()),
        }
        report_path = results / "run.json"
        report_path.write_text(json.dumps(report), encoding="utf-8")
        return report_path

    def test_valid_report_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report_path = self.make_repository(root)
            self.assertEqual(VALIDATOR.validate_report(report_path, root), [])

    def test_tampered_summary_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report_path = self.make_repository(root)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["summary"]["exact_matches"] = 1
            report_path.write_text(json.dumps(report), encoding="utf-8")
            errors = VALIDATOR.validate_report(report_path, root)
            self.assertTrue(any("summary must match computed" in error for error in errors))

    def test_out_of_order_or_duplicate_response_fails(self) -> None:
        errors = VALIDATOR.validate_response(
            {"selections": list(reversed(response()["selections"]))},
            corpus(),
            {"first-skill", "second-skill", "third-skill"},
        )
        self.assertIn(
            "response must select every corpus case exactly once in corpus order", errors
        )


if __name__ == "__main__":
    unittest.main()
