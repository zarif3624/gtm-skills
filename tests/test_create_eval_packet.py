from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "create_eval_packet.py"
SPEC = importlib.util.spec_from_file_location("create_eval_packet", MODULE_PATH)
assert SPEC and SPEC.loader
PACKET = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKET)


class EvalPacketTests(unittest.TestCase):
    def test_case_packet_contains_inputs_but_hides_scoring(self) -> None:
        definition = {
            "id": "case",
            "skill": "test-skill",
            "risk": "Hidden consequential risk.",
            "prompt": "Complete the requested artifact.",
            "context": ["Only this limited evidence is supplied."],
            "assertions": {"must_demonstrate": ["A hidden expected behavior."]},
        }
        packet = PACKET.render_packet(definition)
        self.assertIn("**Target skills:** test-skill", packet)
        self.assertIn("Complete the requested artifact.", packet)
        self.assertIn("Only this limited evidence is supplied.", packet)
        self.assertNotIn("Hidden consequential risk", packet)
        self.assertNotIn("hidden expected behavior", packet.lower())
        self.assertNotIn("must_demonstrate", packet)

    def test_journey_packet_preserves_skill_order(self) -> None:
        definition = {
            "id": "journey",
            "skills": ["first-skill", "second-skill"],
            "prompt": "Complete both jobs.",
            "context": [],
        }
        packet = PACKET.render_packet(definition)
        self.assertIn("**Target skills:** first-skill, second-skill", packet)

    def test_missing_skill_target_fails(self) -> None:
        with self.assertRaisesRegex(ValueError, "identify skill or skills"):
            PACKET.render_packet({"prompt": "Do work.", "context": []})


if __name__ == "__main__":
    unittest.main()
