from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_docs.py"
SPEC = importlib.util.spec_from_file_location("validate_docs", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class DocumentationLinkTests(unittest.TestCase):
    def test_valid_relative_and_external_links_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "docs").mkdir()
            (root / "target.md").write_text("# Target\n", encoding="utf-8")
            source = root / "docs" / "source.md"
            source.write_text(
                "[local](../target.md#section) [web](https://example.com)\n",
                encoding="utf-8",
            )
            self.assertEqual(VALIDATOR.validate_file(source, root), [])

    def test_missing_and_escaping_links_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source.md"
            source.write_text("[missing](no.md) [escape](../outside.md)\n", encoding="utf-8")
            errors = VALIDATOR.validate_file(source, root)
            self.assertIn("repository link target does not exist: no.md", errors)
            self.assertIn("repository link escapes the repository: ../outside.md", errors)

    def test_symlink_target_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            outside = root.parent / "doc-link-outside.md"
            outside.write_text("# Outside\n", encoding="utf-8")
            try:
                (root / "linked.md").symlink_to(outside)
                source = root / "source.md"
                source.write_text("[linked](linked.md)\n", encoding="utf-8")
                errors = VALIDATOR.validate_file(source, root)
                self.assertTrue(any("symbolic link" in error for error in errors))
            finally:
                outside.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
