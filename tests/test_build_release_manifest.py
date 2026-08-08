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

    def test_directory_digest_includes_paths_and_contents(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            asset = root / "assets" / "one"
            asset.mkdir(parents=True)
            (asset / "a.txt").write_text("first\n", encoding="utf-8")
            initial = MANIFEST.directory_sha256(asset, root)
            (asset / "a.txt").write_text("second\n", encoding="utf-8")
            changed_content = MANIFEST.directory_sha256(asset, root)
            (asset / "a.txt").rename(asset / "b.txt")
            changed_path = MANIFEST.directory_sha256(asset, root)

            self.assertNotEqual(initial, changed_content)
            self.assertNotEqual(changed_content, changed_path)

    def test_directory_digest_ignores_python_cache_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            asset = root / "scripts"
            asset.mkdir()
            (asset / "check.py").write_text("print('ok')\n", encoding="utf-8")
            initial = MANIFEST.directory_sha256(asset, root)
            cache = asset / "__pycache__"
            cache.mkdir()
            (cache / "check.cpython-310.pyc").write_bytes(b"generated")
            self.assertEqual(MANIFEST.directory_sha256(asset, root), initial)

    def test_manifest_indexes_packages_and_only_latest_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            behavior = root / "evals" / "results"
            routing = root / "evals" / "routing" / "results"
            behavior.mkdir(parents=True)
            routing.mkdir(parents=True)
            for path in (
                root / "evals" / "cases",
                root / "evals" / "journeys",
                root / "examples" / "example-one",
                root / "reference-packs" / "pack-one",
                root / "scripts",
                root / "tests",
            ):
                path.mkdir(parents=True)
                (path / "asset.txt").write_text("asset\n", encoding="utf-8")
            workflow = root / ".github" / "workflows" / "validate.yml"
            workflow.parent.mkdir(parents=True)
            workflow.write_text("name: Validate\n", encoding="utf-8")
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
            (root / "quality-policy.json").write_text("{}\n", encoding="utf-8")
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
            self.assertEqual(result["schema_version"], 3)
            self.assertEqual(result["skill_packages"][0]["name"], "test-skill")
            self.assertEqual(len(result["current_evidence"]["behavioral"]), 1)
            self.assertEqual(
                result["current_evidence"]["behavioral"][0]["verdict"], "pass"
            )
            self.assertEqual(len(result["current_evidence"]["routing"]), 1)
            self.assertEqual(
                len(result["generated_artifacts"]["catalog"]["sha256"]), 64
            )
            self.assertEqual(len(result["quality_policy"]["sha256"]), 64)
            self.assertEqual(
                len(result["supporting_assets"]["evaluation_definitions"]), 2
            )
            self.assertEqual(
                result["supporting_assets"]["example_workspaces"][0]["name"],
                "example-one",
            )
            self.assertEqual(
                result["supporting_assets"]["reference_packs"][0]["name"],
                "pack-one",
            )
            self.assertEqual(
                len(
                    result["supporting_assets"]["quality_tooling"]["scripts"][
                        "tree_sha256"
                    ]
                ),
                64,
            )
            self.assertEqual(
                len(
                    result["supporting_assets"]["quality_tooling"][
                        "validation_workflow"
                    ]["sha256"]
                ),
                64,
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
