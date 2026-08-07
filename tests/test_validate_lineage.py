from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_lineage.py"
SPEC = importlib.util.spec_from_file_location("validate_lineage", MODULE_PATH)
assert SPEC and SPEC.loader
LINEAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LINEAGE)


def report(lineage: str, supersedes: str | None = None) -> dict[str, object]:
    return {"supersedes": supersedes, "run": {"lineage": lineage}}


class LineageValidatorTests(unittest.TestCase):
    def test_linear_history_has_one_latest_report(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            first = (root / "first.json").resolve()
            second = (root / "second.json").resolve()
            reports = {
                first: report("lane"),
                second: report("lane", "first.json"),
            }
            self.assertEqual(
                LINEAGE.validate_lineage_graph(
                    reports, root, identity_fields=("run.lineage",)
                ),
                [],
            )

    def test_branching_history_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            first = (root / "first.json").resolve()
            reports = {
                first: report("lane"),
                (root / "second.json").resolve(): report("lane", "first.json"),
                (root / "third.json").resolve(): report("lane", "first.json"),
            }
            errors = LINEAGE.validate_lineage_graph(
                reports, root, identity_fields=("run.lineage",)
            )
            self.assertTrue(any("multiple successors" in error for error in errors))
            self.assertTrue(any("exactly one latest report" in error for error in errors))

    def test_cycle_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            reports = {
                (root / "first.json").resolve(): report("lane", "second.json"),
                (root / "second.json").resolve(): report("lane", "first.json"),
            }
            errors = LINEAGE.validate_lineage_graph(
                reports, root, identity_fields=("run.lineage",)
            )
            self.assertTrue(any("supersession cycle" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
