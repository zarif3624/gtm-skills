from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build_catalog.py"
SPEC = importlib.util.spec_from_file_location("build_catalog", MODULE_PATH)
assert SPEC and SPEC.loader
CATALOG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CATALOG)


class CatalogTests(unittest.TestCase):
    def make_skill(self, root: Path, name: str) -> Path:
        skill = root / "skills" / name
        (skill / "agents").mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            f'''---
name: {name}
description: "Create a catalog test. Use when testing generated metadata."
---

# Test
''',
            encoding="utf-8",
        )
        (skill / "agents" / "openai.yaml").write_text(
            f'''interface:
  display_name: "{name.title()}"
  short_description: "Create a catalog validation artifact"
  default_prompt: "Use ${name} for this catalog test."
''',
            encoding="utf-8",
        )
        return skill

    def test_catalog_is_sorted_and_contains_interface_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_skill(root, "second-skill")
            self.make_skill(root, "first-skill")
            catalog = CATALOG.build_catalog(root)
            self.assertEqual(
                [entry["name"] for entry in catalog["skills"]],
                ["first-skill", "second-skill"],
            )
            self.assertEqual(
                catalog["skills"][0]["default_prompt"],
                "Use $first-skill for this catalog test.",
            )

    def test_package_digest_changes_with_resource_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = self.make_skill(root, "test-skill")
            before = CATALOG.build_catalog(root)["skills"][0]["package_sha256"]
            (skill / "asset.md").write_text("changed\n", encoding="utf-8")
            after = CATALOG.build_catalog(root)["skills"][0]["package_sha256"]
            self.assertNotEqual(before, after)


if __name__ == "__main__":
    unittest.main()
