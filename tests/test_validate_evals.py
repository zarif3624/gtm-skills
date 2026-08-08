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


def valid_journey() -> dict[str, object]:
    return {
        "schema_version": 1,
        "id": "test-journey",
        "skills": ["first-skill", "second-skill"],
        "prompt": "Complete the fictional workflow.",
        "context": ["A material claim remains unknown."],
        "assertions": {
            "must_preserve": ["Keep the claim unknown across both artifacts."],
            "must_not_transform": ["Do not turn the claim into a verified fact."],
            "human_review": ["Ask the responsible owner to verify the claim."],
        },
    }


def valid_routing() -> dict[str, object]:
    return {
        "schema_version": 1,
        "cases": [
            {
                "id": "choose-first-skill",
                "prompt": "Complete the first workflow.",
                "expected_skills": ["first-skill"],
                "excluded_skills": ["second-skill"],
            },
            {
                "id": "choose-second-skill",
                "prompt": "Complete the second workflow.",
                "expected_skills": ["second-skill"],
                "excluded_skills": ["first-skill"],
            },
        ],
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

    def test_boolean_schema_version_fails_all_definition_types(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            case = valid_case()
            case["schema_version"] = True
            _skill, case_errors = VALIDATOR.validate_case(
                self.write_case(root, case), {"test-skill"}
            )
            journey = valid_journey()
            journey["schema_version"] = True
            journey_path = root / "test-journey.json"
            journey_path.write_text(json.dumps(journey), encoding="utf-8")
            journey_errors = VALIDATOR.validate_journey(
                journey_path, {"first-skill", "second-skill"}
            )
            routing = valid_routing()
            routing["schema_version"] = True
            routing_path = root / "routing.json"
            routing_path.write_text(json.dumps(routing), encoding="utf-8")
            _covered, routing_errors = VALIDATOR.validate_routing(
                routing_path, {"first-skill", "second-skill"}
            )
            self.assertIn("schema_version must be 1", case_errors)
            self.assertIn("schema_version must be 1", journey_errors)
            self.assertIn("schema_version must be 1", routing_errors)

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

    def test_valid_journey_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "test-journey.json"
            path.write_text(json.dumps(valid_journey()), encoding="utf-8")
            errors = VALIDATOR.validate_journey(path, {"first-skill", "second-skill"})
            self.assertEqual(errors, [])

    def test_journey_requires_two_distinct_skills(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            journey = valid_journey()
            journey["skills"] = ["first-skill", "first-skill"]
            path = Path(temp) / "test-journey.json"
            path.write_text(json.dumps(journey), encoding="utf-8")
            errors = VALIDATOR.validate_journey(path, {"first-skill"})
            self.assertIn("skills must not contain duplicates", errors)

    def test_valid_routing_corpus_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "routing.json"
            path.write_text(json.dumps(valid_routing()), encoding="utf-8")
            covered, errors = VALIDATOR.validate_routing(
                path, {"first-skill", "second-skill"}
            )
            self.assertEqual(errors, [])
            self.assertEqual(covered, {"first-skill", "second-skill"})

    def test_routing_expected_and_excluded_must_not_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            routing = valid_routing()
            routing["cases"][0]["excluded_skills"] = ["first-skill"]  # type: ignore[index]
            path = Path(temp) / "routing.json"
            path.write_text(json.dumps(routing), encoding="utf-8")
            _covered, errors = VALIDATOR.validate_routing(
                path, {"first-skill", "second-skill"}
            )
            self.assertIn("cases[1] expects and excludes: first-skill", errors)

    def test_every_journey_topology_requires_a_routing_case(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            journey_path = root / "test-journey.json"
            journey_path.write_text(json.dumps(valid_journey()), encoding="utf-8")
            routing_path = root / "routing.json"
            routing = valid_routing()
            routing_path.write_text(json.dumps(routing), encoding="utf-8")
            self.assertEqual(
                VALIDATOR.uncovered_journey_routes([journey_path], routing_path),
                ["test-journey"],
            )
            routing["cases"].append(
                {
                    "id": "run-journey",
                    "prompt": "Complete both workflows.",
                    "expected_skills": ["first-skill", "second-skill"],
                    "excluded_skills": ["third-skill"],
                }
            )
            routing_path.write_text(json.dumps(routing), encoding="utf-8")
            self.assertEqual(
                VALIDATOR.uncovered_journey_routes([journey_path], routing_path), []
            )


if __name__ == "__main__":
    unittest.main()
