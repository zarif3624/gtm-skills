from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_examples.py"
SPEC = importlib.util.spec_from_file_location("validate_examples", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ExampleValidatorTests(unittest.TestCase):
    def make_pack(self, root: Path) -> Path:
        pack = root / "sample"
        pack.mkdir()
        (pack / "README.md").write_text("# Fictional example\n", encoding="utf-8")
        (pack / "gtm-context.md").write_text("# Context\n", encoding="utf-8")
        (pack / "discovery-transcript.md").write_text(
            "[00:01] Seller: Hello.\n\n[00:05] Buyer: Hello.\n", encoding="utf-8"
        )
        header = ",".join(sorted(VALIDATOR.REQUIRED_PIPELINE_FIELDS))
        values = {
            "opportunity_id": "OP-1",
            "account_name": "Fictional Co",
            "stage": "Discovery",
            "amount": "100",
            "currency": "USD",
            "close_date": "2026-09-30",
            "last_buyer_action": "",
            "next_step": "",
            "next_step_owner": "",
            "next_step_date": "",
            "forecast_category": "Pipeline",
            "notes": "",
        }
        row = ",".join(values[field] for field in sorted(VALIDATOR.REQUIRED_PIPELINE_FIELDS))
        (pack / "pipeline.csv").write_text(f"{header}\n{row}\n", encoding="utf-8")
        return pack

    def test_valid_pack_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            pack = self.make_pack(Path(temp))
            self.assertEqual(VALIDATOR.validate_pack(pack), [])

    def test_email_like_identifier_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            pack = self.make_pack(Path(temp))
            readme = pack / "README.md"
            readme.write_text("# Fictional\nContact person@example.com\n", encoding="utf-8")
            errors = VALIDATOR.validate_pack(pack)
            self.assertIn("example contains an email-like identifier: README.md", errors)


if __name__ == "__main__":
    unittest.main()
