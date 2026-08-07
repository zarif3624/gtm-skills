from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"
SPEC = importlib.util.spec_from_file_location("validate_skills", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class SkillValidatorTests(unittest.TestCase):
    def make_skill(self, root: Path, name: str = "test-skill") -> Path:
        skill = root / name
        (skill / "agents").mkdir(parents=True)
        (skill / "references").mkdir()
        (skill / "references" / "guide.md").write_text("# Guide\n", encoding="utf-8")
        (skill / "SKILL.md").write_text(
            f'''---
name: {name}
description: "Create a useful test artifact. Use when testing skill validation behavior."
---

# Test Skill

Read `.agents/gtm-context.md` when available. Read [the guide](references/guide.md).

Never invent evidence.

## Output

Produce a test artifact.
''',
            encoding="utf-8",
        )
        (skill / "agents" / "openai.yaml").write_text(
            f'''interface:
  display_name: "Test Skill"
  short_description: "Create a useful validation artifact"
  default_prompt: "Use ${name} to create a useful test artifact."
''',
            encoding="utf-8",
        )
        return skill

    def test_valid_skill_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skill = self.make_skill(Path(temp))
            self.assertEqual(VALIDATOR.validate_skill(skill), [])

    def test_duplicate_frontmatter_field_fails(self) -> None:
        text = "---\nname: one\nname: two\ndescription: Use this for tests.\n---\n# Body\n"
        _fields, _body, errors = VALIDATOR.parse_frontmatter(text)
        self.assertIn("duplicate frontmatter field: name", errors)

    def test_broken_resource_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skill = self.make_skill(Path(temp))
            skill_file = skill / "SKILL.md"
            skill_file.write_text(
                skill_file.read_text(encoding="utf-8").replace(
                    "references/guide.md", "references/missing.md"
                ),
                encoding="utf-8",
            )
            errors = VALIDATOR.validate_skill(skill)
            self.assertIn("broken local resource link: references/missing.md", errors)

    def test_escaping_resource_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skill = self.make_skill(Path(temp))
            skill_file = skill / "SKILL.md"
            skill_file.write_text(
                skill_file.read_text(encoding="utf-8").replace(
                    "references/guide.md", "../private.md"
                ),
                encoding="utf-8",
            )
            errors = VALIDATOR.validate_skill(skill)
            self.assertIn("local resource link escapes skill directory: ../private.md", errors)

    def test_unreferenced_resource_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skill = self.make_skill(Path(temp))
            (skill / "assets").mkdir()
            (skill / "assets" / "orphan.md").write_text("unused", encoding="utf-8")
            errors = VALIDATOR.validate_skill(skill)
            self.assertIn("unreferenced bundled resource: assets/orphan.md", errors)

    def test_default_prompt_must_name_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            skill = self.make_skill(Path(temp))
            metadata = skill / "agents" / "openai.yaml"
            metadata.write_text(
                metadata.read_text(encoding="utf-8").replace("$test-skill", "$other-skill"),
                encoding="utf-8",
            )
            errors = VALIDATOR.validate_skill(skill)
            self.assertIn("default_prompt must explicitly mention $test-skill", errors)


if __name__ == "__main__":
    unittest.main()
