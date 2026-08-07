from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "build_release_manifest.py"
SPEC = importlib.util.spec_from_file_location("build_release_manifest", MODULE_PATH)
assert SPEC and SPEC.loader
MANIFEST = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MANIFEST)


class ReleaseManifestTests(unittest.TestCase):
    def test_repository_file_rejects_escape(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            with self.assertRaisesRegex(ValueError, "must stay in the repository"):
                MANIFEST.repository_file(root, "../outside.json", "response")

    def test_manifest_indexes_packages_and_only_latest_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            behavior = root / "evals" / "results"
            routing = root / "evals" / "routing" / "results"
            behavior.mkdir(parents=True)
            routing.mkdir(parents=True)
            (root / "catalog.json").write_text(
                json.dumps(
                    {
                        "skills": [
                            {
                                "name": "test-skill",
                                "path": "skills/test-skill",
                                "package_sha256": "a" * 64,
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            (root / "quality-summary.json").write_text("{}\n", encoding="utf-8")
            prior = behavior / "prior.json"
            prior.write_text(
                json.dumps(
                    {
                        "case_id": "test-case",
                        "case_type": "case",
                        "supersedes": None,
                        "run": {
                            "lineage": "test-lineage",
                            "repository_commit": "abcdef1",
                            "response_path": "evals/results/prior.md",
                        },
                        "summary": {"verdict": "fail"},
                    }
                ),
                encoding="utf-8",
            )
            current = behavior / "current.json"
            (behavior / "current.md").write_text("Current response.\n", encoding="utf-8")
            current.write_text(
                json.dumps(
                    {
                        "case_id": "test-case",
                        "case_type": "case",
                        "supersedes": "evals/results/prior.json",
                        "run": {
                            "lineage": "test-lineage",
                            "repository_commit": "abcdef2",
                            "response_path": "evals/results/current.md",
                        },
                        "summary": {"verdict": "pass"},
                    }
                ),
                encoding="utf-8",
            )
            route = routing / "route.json"
            (routing / "route.response.json").write_text("{}\n", encoding="utf-8")
            corpus = root / "evals" / "routing" / "corpora" / "test.json"
            corpus.parent.mkdir(parents=True)
            corpus.write_text("{}\n", encoding="utf-8")
            route.write_text(
                json.dumps(
                    {
                        "corpus_path": "evals/routing/corpora/test.json",
                        "supersedes": None,
                        "run": {
                            "lineage": "test-lineage",
                            "repository_commit": "abcdef2",
                            "response_path": "evals/routing/results/route.response.json",
                        },
                        "summary": {
                            "verdict": "pass",
                            "total_cases": 2,
                            "exact_matches": 2,
                        },
                    }
                ),
                encoding="utf-8",
            )

            result = MANIFEST.build_manifest(root)
            self.assertEqual(result["skill_packages"][0]["name"], "test-skill")
            self.assertEqual(len(result["current_evidence"]["behavioral"]), 1)
            self.assertEqual(
                result["current_evidence"]["behavioral"][0]["verdict"], "pass"
            )
            self.assertEqual(len(result["current_evidence"]["routing"]), 1)
            self.assertEqual(
                len(result["generated_artifacts"]["catalog"]["sha256"]), 64
            )
            self.assertEqual(
                len(result["current_evidence"]["behavioral"][0]["response_sha256"]),
                64,
            )
            self.assertEqual(
                len(result["current_evidence"]["routing"][0]["corpus_sha256"]), 64
            )


if __name__ == "__main__":
    unittest.main()
