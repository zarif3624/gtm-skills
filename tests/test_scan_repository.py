from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "scan_repository.py"
SPEC = importlib.util.spec_from_file_location("scan_repository", MODULE_PATH)
assert SPEC and SPEC.loader
SCANNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCANNER)


class RepositoryScannerTests(unittest.TestCase):
    def test_normal_text_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("No credentials here.\n", encoding="utf-8")
            count, errors = SCANNER.scan_repository(root)
            self.assertEqual(count, 1)
            self.assertEqual(errors, [])

    def test_common_credential_shape_fails_without_echoing_value(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            candidate = "AKIA" + "A" * 16
            (root / "candidate.txt").write_text(candidate, encoding="utf-8")
            _count, errors = SCANNER.scan_repository(root)
            self.assertEqual(errors, ["possible AWS access key: candidate.txt:1"])
            self.assertNotIn(candidate, errors[0])

    def test_symlink_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "target.md"
            target.write_text("safe", encoding="utf-8")
            (root / "linked.md").symlink_to(target)
            _count, errors = SCANNER.scan_repository(root)
            self.assertIn("symbolic link is not allowed: linked.md", errors)

    def test_skipped_directory_name_cannot_hide_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "target"
            target.mkdir()
            (root / "node_modules").symlink_to(target, target_is_directory=True)
            _count, errors = SCANNER.scan_repository(root)
            self.assertIn("symbolic link is not allowed: node_modules", errors)


if __name__ == "__main__":
    unittest.main()
