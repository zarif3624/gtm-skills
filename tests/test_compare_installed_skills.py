from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "compare_installed_skills.py"
SPEC = importlib.util.spec_from_file_location("compare_installed_skills", MODULE_PATH)
assert SPEC and SPEC.loader
COMPARATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(COMPARATOR)


class InstalledSkillComparatorTests(unittest.TestCase):
    def make_trees(self, root: Path) -> tuple[Path, Path]:
        source = root / "source"
        installed = root / "installed"
        for tree in (source, installed):
            package = tree / "test-skill"
            (package / "references").mkdir(parents=True)
            (package / "SKILL.md").write_text("# Test\n", encoding="utf-8")
            (package / "references" / "method.md").write_text(
                "Method.\n", encoding="utf-8"
            )
        return source, installed

    def test_matching_install_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source, installed = self.make_trees(Path(temp))
            skills, files, errors = COMPARATOR.compare(source, installed)
            self.assertEqual((skills, files, errors), (1, 2, []))

    def test_missing_extra_and_changed_files_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source, installed = self.make_trees(Path(temp))
            (installed / "test-skill" / "SKILL.md").write_text(
                "Changed.\n", encoding="utf-8"
            )
            (installed / "test-skill" / "references" / "method.md").unlink()
            (installed / "test-skill" / "extra.txt").write_text(
                "Extra.\n", encoding="utf-8"
            )
            _skills, _files, errors = COMPARATOR.compare(source, installed)
            self.assertTrue(any("differs from source" in error for error in errors))
            self.assertTrue(any("is missing" in error for error in errors))
            self.assertTrue(any("extra file" in error for error in errors))

    def test_symlinked_install_path_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source, installed = self.make_trees(Path(temp))
            link = installed / "test-skill" / "linked.md"
            link.symlink_to(source / "test-skill" / "SKILL.md")
            _skills, _files, errors = COMPARATOR.compare(source, installed)
            self.assertTrue(any("symbolic link" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
