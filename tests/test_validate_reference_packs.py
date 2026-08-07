from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_reference_packs.py"
SPEC = importlib.util.spec_from_file_location("validate_reference_packs", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ReferencePackValidatorTests(unittest.TestCase):
    def copy_valid_pack(self, root: Path) -> Path:
        pack = root / "generic-crm"
        pack.mkdir()
        for source in VALIDATOR.GENERIC.iterdir():
            if source.is_file():
                (pack / source.name).write_bytes(source.read_bytes())
        return pack

    def test_repository_pack_passes(self) -> None:
        self.assertEqual(VALIDATOR.validate_generic_pack(), [])
        self.assertEqual(VALIDATOR.validate_evidence_pack(), [])
        self.assertEqual(VALIDATOR.validate_context_pack(), [])

    def test_header_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            pack = self.copy_valid_pack(Path(temp))
            template = pack / "opportunities-template.csv"
            template.write_text("record_id,opportunity_id\n", encoding="utf-8")
            errors = VALIDATOR.validate_generic_pack(pack)
            self.assertIn(
                "opportunities-template.csv header does not match the canonical contract", errors
            )

    def test_schema_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            pack = self.copy_valid_pack(Path(temp))
            schema_path = pack / "pipeline-opportunity.schema.json"
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            schema["additionalProperties"] = True
            schema_path.write_text(json.dumps(schema), encoding="utf-8")
            errors = VALIDATOR.validate_generic_pack(pack)
            self.assertIn("opportunity schema must define a closed object", errors)

    def test_evidence_template_and_schema_must_stay_aligned(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            pack = Path(temp) / "evidence-ledger"
            pack.mkdir()
            for source in VALIDATOR.EVIDENCE.iterdir():
                if source.is_file():
                    (pack / source.name).write_bytes(source.read_bytes())
            template = pack / "evidence-ledger-template.csv"
            template.write_text("claim_id,claim\n", encoding="utf-8")
            errors = VALIDATOR.validate_evidence_pack(pack)
            self.assertIn(
                "evidence-ledger-template.csv header does not match its canonical contract",
                errors,
            )

    def test_structured_context_template_and_schema_must_stay_aligned(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            pack = Path(temp) / "structured-gtm-context"
            pack.mkdir()
            for source in VALIDATOR.STRUCTURED_CONTEXT.iterdir():
                if source.is_file():
                    (pack / source.name).write_bytes(source.read_bytes())
            template_path = pack / "gtm-context-template.json"
            template = json.loads(template_path.read_text(encoding="utf-8"))
            template["unexpected"] = True
            template_path.write_text(json.dumps(template), encoding="utf-8")
            errors = VALIDATOR.validate_context_pack(pack)
            self.assertIn(
                "structured context template fields must match the schema contract", errors
            )


if __name__ == "__main__":
    unittest.main()
