from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_evals.py"
SPEC = importlib.util.spec_from_file_location("validate_evals", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def valid_case() -> dict[str, object]:
    return {
        "schema_version": 1,
        "id": "test-case",
        "skill": "test-skill",
        "risk": "The behavior is not tested.",
        "prompt": "Complete the fictional task.",
        "context": ["Only partial evidence is available."],
        "assertions": {
            "must_demonstrate": ["Make uncertainty visible."],
            "must_avoid": ["Invent missing facts."],
            "human_review": ["Ask a responsible owner to approve the claim."],
        },
    }


class EvalValidatorTests(unittest.TestCase):
    def write_case(self, root: Path, case: dict[str, object]) -> Path:
        path = root / "test-case.json"
        path.write_text(json.dumps(case), encoding="utf-8")
        return path

    def test_valid_case_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = self.write_case(Path(temp), valid_case())
            skill, errors = VALIDATOR.validate_case(path, {"test-skill"})
            self.assertEqual(skill, "test-skill")
            self.assertEqual(errors, [])

    def test_unknown_skill_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = self.write_case(Path(temp), valid_case())
            _skill, errors = VALIDATOR.validate_case(path, {"other-skill"})
            self.assertIn("unknown skill: test-skill", errors)

    def test_empty_assertion_list_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            case = valid_case()
            case["assertions"]["must_avoid"] = []  # type: ignore[index]
            path = self.write_case(Path(temp), case)
            _skill, errors = VALIDATOR.validate_case(path, {"test-skill"})
            self.assertIn("assertions.must_avoid must be a non-empty list of strings", errors)

    def test_filename_must_match_id(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            case = valid_case()
            case["id"] = "different-id"
            path = self.write_case(Path(temp), case)
            _skill, errors = VALIDATOR.validate_case(path, {"test-skill"})
            self.assertIn("id must match the case filename", errors)


if __name__ == "__main__":
    unittest.main()
