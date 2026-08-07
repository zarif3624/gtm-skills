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


if __name__ == "__main__":
    unittest.main()
