from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_workflows.py"
SPEC = importlib.util.spec_from_file_location("validate_workflows", MODULE_PATH)
assert SPEC and SPEC.loader
WORKFLOWS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WORKFLOWS)


class WorkflowValidatorTests(unittest.TestCase):
    def write(self, root: Path, text: str) -> Path:
        path = root / "test.yml"
        path.write_text(text, encoding="utf-8")
        return path

    def test_commit_pinned_action_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = self.write(
                Path(temp),
                "steps:\n  - uses: actions/checkout@" + "a" * 40 + " # v4\n",
            )
            self.assertEqual(WORKFLOWS.validate_workflow(path), [])

    def test_moving_tag_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = self.write(Path(temp), "steps:\n  - uses: actions/checkout@v4\n")
            self.assertEqual(
                WORKFLOWS.validate_workflow(path),
                ["remote action must use a full commit SHA: actions/checkout@v4"],
            )

    def test_pull_request_target_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = self.write(Path(temp), "on:\n  pull_request_target:\n")
            self.assertEqual(
                WORKFLOWS.validate_workflow(path),
                ["pull_request_target requires an explicit security review"],
            )


if __name__ == "__main__":
    unittest.main()
