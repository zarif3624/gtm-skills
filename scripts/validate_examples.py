#!/usr/bin/env python3
"""Validate fictional example workspaces and their structured inputs."""

from __future__ import annotations

import csv
import re
import sys
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
REQUIRED_FILES = {
    "README.md",
    "gtm-context.md",
    "discovery-transcript.md",
    "positioning-brief.md",
    "outbound-plan.md",
    "pipeline.csv",
    "customer-outcomes.csv",
}
REQUIRED_PIPELINE_FIELDS = {
    "opportunity_id",
    "account_name",
    "stage",
    "amount",
    "currency",
    "close_date",
    "last_buyer_action",
    "next_step",
    "next_step_owner",
    "next_step_date",
    "forecast_category",
    "notes",
}
REQUIRED_OUTCOME_FIELDS = {
    "account_id",
    "account_name",
    "period_start",
    "period_end",
    "eligible_users",
    "active_users",
    "login_count",
    "workflow_events",
    "outcome_metric",
    "baseline_value",
    "current_value",
    "target_value",
    "support_status",
    "sponsor_status",
    "renewal_date",
    "renewal_status",
    "customer_validation",
    "expansion_signal",
    "notes",
}
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
TIMESTAMP_RE = re.compile(r"^\[\d{2}:\d{2}\]", re.MULTILINE)


def validate_date(
    value: str, field: str, row_number: int, source: str = "pipeline"
) -> list[str]:
    if not value:
        return []
    try:
        date.fromisoformat(value)
    except ValueError:
        return [f"{source} row {row_number} has invalid {field}: {value}"]
    return []


def validate_pack(path: Path) -> list[str]:
    errors: list[str] = []
    if path.is_symlink():
        return ["example workspace must not be a symbolic link"]
    symlinks = sorted(item.relative_to(path).as_posix() for item in path.rglob("*") if item.is_symlink())
    if symlinks:
        return [f"example path must not be a symbolic link: {item}" for item in symlinks]
    missing = sorted(REQUIRED_FILES - {item.name for item in path.iterdir() if item.is_file()})
    if missing:
        errors.append(f"missing required files: {', '.join(missing)}")
        return errors

    markdown_files = sorted(path.glob("*.md"))
    readme = (path / "README.md").read_text(encoding="utf-8")
    if "fictional" not in readme.lower():
        errors.append("README.md must state that the workspace is fictional")
    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        if EMAIL_RE.search(text):
            errors.append(f"example contains an email-like identifier: {markdown_file.name}")

    transcript = (path / "discovery-transcript.md").read_text(encoding="utf-8")
    if len(TIMESTAMP_RE.findall(transcript)) < 2:
        errors.append("discovery-transcript.md must contain at least two timestamped turns")

    positioning = (path / "positioning-brief.md").read_text(encoding="utf-8")
    if "artifact status:** proposed" not in positioning.lower():
        errors.append("positioning-brief.md must preserve proposed artifact status")
    if "language to hold" not in positioning.lower():
        errors.append("positioning-brief.md must identify unsupported claims to hold")

    outbound = (path / "outbound-plan.md").read_text(encoding="utf-8")
    if "artifact status:** proposed" not in outbound.lower():
        errors.append("outbound-plan.md must preserve proposed artifact status")
    if "claim handoff" not in outbound.lower() or "review before launch" not in outbound.lower():
        errors.append("outbound-plan.md must include claim handoff and launch review")

    with (path / "pipeline.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        if fields != REQUIRED_PIPELINE_FIELDS:
            errors.append("pipeline.csv fields do not match the required example schema")
            return errors
        rows = list(reader)
    if not rows:
        errors.append("pipeline.csv must contain at least one record")
    for row_number, row in enumerate(rows, start=2):
        if None in row or any(value is None for value in row.values()):
            errors.append(f"pipeline row {row_number} has the wrong number of columns")
            continue
        if not row["opportunity_id"] or not row["account_name"]:
            errors.append(f"pipeline row {row_number} is missing identity fields")
        try:
            if Decimal(row["amount"]) < 0:
                errors.append(f"pipeline row {row_number} has a negative amount")
        except InvalidOperation:
            errors.append(f"pipeline row {row_number} has an invalid amount")
        if not re.fullmatch(r"[A-Z]{3}", row["currency"]):
            errors.append(f"pipeline row {row_number} has invalid currency: {row['currency']}")
        errors.extend(validate_date(row["close_date"], "close_date", row_number))
        errors.extend(validate_date(row["next_step_date"], "next_step_date", row_number))
        if EMAIL_RE.search(" ".join(row.values())):
            errors.append(f"pipeline row {row_number} contains an email-like identifier")

    with (path / "customer-outcomes.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        if fields != REQUIRED_OUTCOME_FIELDS:
            errors.append("customer-outcomes.csv fields do not match the required example schema")
            return errors
        outcome_rows = list(reader)
    if not outcome_rows:
        errors.append("customer-outcomes.csv must contain at least one record")
    for row_number, row in enumerate(outcome_rows, start=2):
        if None in row or any(value is None for value in row.values()):
            errors.append(
                f"customer-outcomes row {row_number} has the wrong number of columns"
            )
            continue
        if not row["account_id"] or not row["account_name"]:
            errors.append(f"customer-outcomes row {row_number} is missing identity fields")
        for field in ("period_start", "period_end", "renewal_date"):
            errors.extend(validate_date(row[field], field, row_number, "customer-outcomes"))
        for field in (
            "eligible_users",
            "active_users",
            "login_count",
            "workflow_events",
            "baseline_value",
            "current_value",
            "target_value",
        ):
            if not row[field]:
                continue
            try:
                if Decimal(row[field]) < 0:
                    errors.append(
                        f"customer-outcomes row {row_number} has a negative {field}"
                    )
            except InvalidOperation:
                errors.append(f"customer-outcomes row {row_number} has an invalid {field}")
        if EMAIL_RE.search(" ".join(row.values())):
            errors.append(
                f"customer-outcomes row {row_number} contains an email-like identifier"
            )
    return errors


def main() -> int:
    if not EXAMPLES.is_dir():
        print("FAIL examples directory is missing")
        return 1
    packs = sorted(path for path in EXAMPLES.iterdir() if path.is_dir())
    failures = 0
    for pack in packs:
        errors = validate_pack(pack)
        failures += bool(errors)
        print(f"{'FAIL' if errors else 'PASS'} {pack.name}")
        for error in errors:
            print(f"  - {error}")
    print(f"\nValidated {len(packs)} example workspaces; {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
