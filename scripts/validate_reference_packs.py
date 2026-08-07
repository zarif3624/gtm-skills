#!/usr/bin/env python3
"""Validate operational reference packs and their machine-readable contracts."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "reference-packs"
GENERIC = PACKS / "generic-crm"
EVIDENCE = PACKS / "evidence-ledger"
OPPORTUNITY_FIELDS = (
    "record_id", "opportunity_id", "account_id", "account_name", "opportunity_name",
    "opportunity_owner_id", "stage", "stage_entered_at", "forecast_category", "amount",
    "currency", "close_date", "created_at", "last_buyer_action", "last_buyer_action_at",
    "next_step", "next_step_owner_id", "next_step_status", "next_step_due_at",
    "required_milestone", "required_milestone_status", "required_milestone_due_at", "outcome",
    "outcome_reason", "outcome_evidence_status", "source_system", "source_updated_at",
)
FIELD_MAP_FIELDS = (
    "source_field", "canonical_field", "transformation", "transformation_status",
    "approver_status", "notes",
)
REQUIRED_FILES = {
    "README.md", "opportunities-template.csv", "field-map-template.csv",
    "currency-policy-template.md", "pipeline-opportunity.schema.json",
}
EVIDENCE_FIELDS = (
    "claim_id", "subject_id", "claim", "claim_type", "evidence_status", "source_locator",
    "source_date", "as_of_date", "scope", "attribution", "transformation",
    "transformation_status", "validation_owner_id", "validation_status",
    "access_classification", "notes",
)
ACTION_FIELDS = (
    "action_id", "subject_id", "action", "actor_id", "actor_status", "timing",
    "timing_status", "buyer_status", "approval_status", "completion_status",
    "source_locator", "source_date", "access_classification", "notes",
)
EVIDENCE_REQUIRED_FILES = {
    "README.md", "evidence-ledger-template.csv", "evidence-record.schema.json",
    "action-ledger-template.csv", "action-record.schema.json", "status-vocabulary.md",
}


def read_csv_header(path: Path) -> tuple[tuple[str, ...], list[list[str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    return (tuple(rows[0]) if rows else ()), rows[1:]


def validate_schema(schema: Any) -> list[str]:
    if not isinstance(schema, dict):
        return ["pipeline-opportunity.schema.json must contain a JSON object"]
    errors: list[str] = []
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append("opportunity schema must use JSON Schema draft 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        errors.append("opportunity schema must define a closed object")
    properties = schema.get("properties")
    if not isinstance(properties, dict) or tuple(properties) != OPPORTUNITY_FIELDS:
        errors.append("opportunity schema property order must match the CSV contract")
    required = schema.get("required")
    minimum = {"record_id", "opportunity_id", "amount", "currency", "source_system", "source_updated_at"}
    if not isinstance(required, list) or set(required) != minimum:
        errors.append("opportunity schema required fields do not match the minimum contract")
    return errors


def validate_record_schema(
    schema: Any, *, label: str, fields: tuple[str, ...], required: set[str]
) -> list[str]:
    if not isinstance(schema, dict):
        return [f"{label} must contain a JSON object"]
    errors: list[str] = []
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append(f"{label} must use JSON Schema draft 2020-12")
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        errors.append(f"{label} must define a closed object")
    properties = schema.get("properties")
    if not isinstance(properties, dict) or tuple(properties) != fields:
        errors.append(f"{label} property order must match its CSV contract")
    schema_required = schema.get("required")
    if not isinstance(schema_required, list) or set(schema_required) != required:
        errors.append(f"{label} required fields do not match the minimum contract")
    return errors


def validate_generic_pack(path: Path = GENERIC) -> list[str]:
    errors: list[str] = []
    if not path.is_dir():
        return ["generic-crm reference pack is missing"]
    symlinks = sorted(item.relative_to(path).as_posix() for item in path.rglob("*") if item.is_symlink())
    if symlinks:
        return [f"reference-pack path must not be a symbolic link: {item}" for item in symlinks]
    present = {item.name for item in path.iterdir() if item.is_file()}
    missing = sorted(REQUIRED_FILES - present)
    if missing:
        return [f"missing required files: {', '.join(missing)}"]

    opportunities_header, opportunity_rows = read_csv_header(path / "opportunities-template.csv")
    if opportunities_header != OPPORTUNITY_FIELDS:
        errors.append("opportunities-template.csv header does not match the canonical contract")
    if opportunity_rows:
        errors.append("opportunities-template.csv must remain header-only")
    field_map_header, field_map_rows = read_csv_header(path / "field-map-template.csv")
    if field_map_header != FIELD_MAP_FIELDS:
        errors.append("field-map-template.csv header does not match the mapping contract")
    if field_map_rows:
        errors.append("field-map-template.csv must remain header-only")

    try:
        schema = json.loads((path / "pipeline-opportunity.schema.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"invalid opportunity schema JSON: {error}")
    else:
        errors.extend(validate_schema(schema))
    currency_text = (path / "currency-policy-template.md").read_text(encoding="utf-8")
    for phrase in ("Preserve original amount", "Approval status", "Proposed / Approved / Unknown"):
        if phrase not in currency_text:
            errors.append(f"currency policy is missing required guidance: {phrase}")
    return errors


def validate_evidence_pack(path: Path = EVIDENCE) -> list[str]:
    if not path.is_dir():
        return ["evidence-ledger reference pack is missing"]
    symlinks = sorted(
        item.relative_to(path).as_posix() for item in path.rglob("*") if item.is_symlink()
    )
    if symlinks:
        return [f"reference-pack path must not be a symbolic link: {item}" for item in symlinks]
    present = {item.name for item in path.iterdir() if item.is_file()}
    missing = sorted(EVIDENCE_REQUIRED_FILES - present)
    if missing:
        return [f"missing required files: {', '.join(missing)}"]

    errors: list[str] = []
    for filename, expected in (
        ("evidence-ledger-template.csv", EVIDENCE_FIELDS),
        ("action-ledger-template.csv", ACTION_FIELDS),
    ):
        header, rows = read_csv_header(path / filename)
        if header != expected:
            errors.append(f"{filename} header does not match its canonical contract")
        if rows:
            errors.append(f"{filename} must remain header-only")

    schema_specs = (
        (
            "evidence-record.schema.json",
            EVIDENCE_FIELDS,
            {"claim_id", "subject_id", "claim", "claim_type", "evidence_status"},
        ),
        (
            "action-record.schema.json",
            ACTION_FIELDS,
            {
                "action_id", "subject_id", "action", "actor_status", "timing_status",
                "buyer_status", "approval_status", "completion_status",
            },
        ),
    )
    for filename, fields, required in schema_specs:
        try:
            schema = json.loads((path / filename).read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"invalid {filename} JSON: {error}")
        else:
            errors.extend(
                validate_record_schema(
                    schema, label=filename, fields=fields, required=required
                )
            )
    vocabulary = (path / "status-vocabulary.md").read_text(encoding="utf-8")
    for phrase in (
        "Repetition never upgrades evidence",
        "buyer acceptance does not prove approval or completion",
        "Preserve the original claim",
    ):
        if phrase not in vocabulary:
            errors.append(f"status vocabulary is missing required guidance: {phrase}")
    return errors


def main() -> int:
    packs = (
        ("evidence-ledger", validate_evidence_pack()),
        ("generic-crm", validate_generic_pack()),
    )
    failures = 0
    for name, errors in packs:
        failures += bool(errors)
        print(f"{'FAIL' if errors else 'PASS'} {name}")
        for error in errors:
            print(f"  - {error}")
    print(f"\nValidated {len(packs)} reference packs; {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
