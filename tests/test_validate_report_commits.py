from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_report_commits.py"
SPEC = importlib.util.spec_from_file_location("validate_report_commits", MODULE_PATH)
assert SPEC and SPEC.loader
COMMITS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COMMITS)


class ReportCommitTests(unittest.TestCase):
    def make_repository(self, root: Path) -> str:
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(
            ["git", "config", "user.email", "test.invalid@example.invalid"],
            cwd=root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Test Runner"], cwd=root, check=True
        )
        (root / "tracked.txt").write_text("test\n", encoding="utf-8")
        subprocess.run(["git", "add", "tracked.txt"], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "test"], cwd=root, check=True)
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()

    def test_existing_ancestor_commit_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            commit = self.make_repository(root)
            self.assertIsNone(COMMITS.commit_error(commit, root))

    def test_unknown_commit_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_repository(root)
            self.assertEqual(
                COMMITS.commit_error("a" * 40, root),
                "commit is not available in the repository",
            )

    def make_behavioral_repository(self, root: Path) -> str:
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(
            ["git", "config", "user.email", "test.invalid@example.invalid"],
            cwd=root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Test Runner"], cwd=root, check=True
        )
        skill = root / "skills" / "test-skill"
        case = root / "evals" / "cases"
        results = root / "evals" / "results"
        skill.mkdir(parents=True)
        case.mkdir(parents=True)
        results.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            '---\nname: test-skill\ndescription: "Use when testing evidence."\n---\n\n# Test\n',
            encoding="utf-8",
        )
        (case / "test-case.json").write_text(
            '{"id":"test-case","skill":"test-skill"}\n', encoding="utf-8"
        )
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "tested state"], cwd=root, check=True)
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        report = (
            '{"case_id":"test-case","case_type":"case",'
            '"case_path":"evals/cases/test-case.json","supersedes":null,'
            f'"run":{{"repository_commit":"{commit}"}}}}\n'
        )
        (results / "test-case.json").write_text(report, encoding="utf-8")
        return commit

    def test_current_behavioral_report_matches_unchanged_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_behavioral_repository(root)
            count, errors = COMMITS.validate_current_behavioral_freshness(root)
            self.assertEqual(count, 1)
            self.assertEqual(errors, [])

    def test_tracked_skill_change_makes_current_report_stale(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_behavioral_repository(root)
            (root / "skills" / "test-skill" / "SKILL.md").write_text(
                "# Changed\n", encoding="utf-8"
            )
            _, errors = COMMITS.validate_current_behavioral_freshness(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("is stale", errors[0])

    def test_untracked_skill_resource_makes_current_report_stale(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_behavioral_repository(root)
            resource = root / "skills" / "test-skill" / "references" / "new.md"
            resource.parent.mkdir()
            resource.write_text("new\n", encoding="utf-8")
            _, errors = COMMITS.validate_current_behavioral_freshness(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("is stale", errors[0])

    def test_definition_change_makes_current_report_stale(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_behavioral_repository(root)
            (root / "evals" / "cases" / "test-case.json").write_text(
                '{"id":"test-case","skill":"test-skill","prompt":"Changed"}\n',
                encoding="utf-8",
            )
            _, errors = COMMITS.validate_current_behavioral_freshness(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("evals/cases/test-case.json differs", errors[0])

    def test_unrelated_change_does_not_stale_skill_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_behavioral_repository(root)
            (root / "README.md").write_text("unrelated\n", encoding="utf-8")
            _, errors = COMMITS.validate_current_behavioral_freshness(root)
            self.assertEqual(errors, [])

    def test_fresh_successor_replaces_stale_prior_report(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_behavioral_repository(root)
            (root / "skills" / "test-skill" / "SKILL.md").write_text(
                "# Changed\n", encoding="utf-8"
            )
            subprocess.run(
                ["git", "add", "skills/test-skill/SKILL.md"], cwd=root, check=True
            )
            subprocess.run(
                ["git", "commit", "-qm", "change skill"], cwd=root, check=True
            )
            commit = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            successor = (
                '{"case_id":"test-case","case_type":"case",'
                '"case_path":"evals/cases/test-case.json",'
                '"supersedes":"evals/results/test-case.json",'
                f'"run":{{"repository_commit":"{commit}"}}}}\n'
            )
            (root / "evals" / "results" / "test-case.retest.json").write_text(
                successor, encoding="utf-8"
            )
            count, errors = COMMITS.validate_current_behavioral_freshness(root)
            self.assertEqual(count, 1)
            self.assertEqual(errors, [])

    def make_routing_repository(self, root: Path) -> str:
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(
            ["git", "config", "user.email", "test.invalid@example.invalid"],
            cwd=root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Test Runner"], cwd=root, check=True
        )
        skill = root / "skills" / "test-skill"
        corpus = root / "evals" / "routing" / "corpora" / "current.json"
        results = root / "evals" / "routing" / "results"
        skill.mkdir(parents=True)
        corpus.parent.mkdir(parents=True)
        results.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            '---\nname: test-skill\ndescription: "Use when testing routing."\n---\n\n# Body\n',
            encoding="utf-8",
        )
        corpus.write_text('{"schema_version":1,"cases":[]}\n', encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "routing inputs"], cwd=root, check=True)
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        report = (
            '{"corpus_path":"evals/routing/corpora/current.json",'
            '"supersedes":null,'
            f'"run":{{"repository_commit":"{commit}"}}}}\n'
        )
        (results / "current.json").write_text(report, encoding="utf-8")
        return commit

    def test_current_routing_report_matches_corpus_and_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_routing_repository(root)
            count, errors = COMMITS.validate_current_routing_freshness(root)
            self.assertEqual(count, 1)
            self.assertEqual(errors, [])

    def test_routing_body_only_change_stays_fresh(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_routing_repository(root)
            (root / "skills" / "test-skill" / "SKILL.md").write_text(
                '---\nname: test-skill\ndescription: "Use when testing routing."\n---\n\n# Changed body\n',
                encoding="utf-8",
            )
            _, errors = COMMITS.validate_current_routing_freshness(root)
            self.assertEqual(errors, [])

    def test_routing_description_change_makes_report_stale(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_routing_repository(root)
            (root / "skills" / "test-skill" / "SKILL.md").write_text(
                '---\nname: test-skill\ndescription: "Changed routing trigger."\n---\n\n# Body\n',
                encoding="utf-8",
            )
            _, errors = COMMITS.validate_current_routing_freshness(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("names or descriptions differ", errors[0])

    def test_routing_corpus_change_makes_report_stale(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_routing_repository(root)
            (root / "evals" / "routing" / "corpora" / "current.json").write_text(
                '{"schema_version":1,"cases":[{"id":"changed"}]}\n',
                encoding="utf-8",
            )
            _, errors = COMMITS.validate_current_routing_freshness(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("corpora/current.json differs", errors[0])


if __name__ == "__main__":
    unittest.main()
