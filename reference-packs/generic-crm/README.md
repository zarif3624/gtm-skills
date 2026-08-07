# Generic CRM Handoff Pack

This vendor-neutral pack defines a minimal, auditable pipeline snapshot for `$review-pipeline` and `$forecast-sales`. It is an interchange contract, not a required CRM model. Keep the raw export immutable and map source fields into a separate working copy.

## Files

- [opportunities template](opportunities-template.csv) — canonical CSV header for one snapshot row per source record;
- [opportunity JSON Schema](pipeline-opportunity.schema.json) — the same record contract for APIs and structured workflows;
- [field-map template](field-map-template.csv) — records source-to-canonical transformations and their approval state;
- [currency-policy template](currency-policy-template.md) — makes any cross-currency treatment explicit and dated.

## Minimum Safe Workflow

1. Export the smallest approved field set needed for the decision.
2. Save the untouched source snapshot with its extraction time and access controls.
3. Map source fields without overwriting source values.
4. Preserve one `record_id` per exported row and one `opportunity_id` per intended buying decision. Duplicate opportunity IDs are evidence to investigate, not permission to merge silently.
5. Leave unavailable values blank. Do not turn blanks into zero, `false`, a default stage, or a default probability.
6. Use ISO 8601 dates and timestamps. Keep the source timezone when it matters.
7. Retain original currency and amount. Convert only under an approved, dated currency policy.
8. Label next steps and milestones as `Accepted`, `Proposed`, `Completed`, or `Unknown`; seller-entered activity alone is not buyer acceptance.
9. Have responsible data and forecast owners approve material transformations before operating use.

## Field Groups

| Group | Purpose |
| --- | --- |
| Identity | Preserve source rows, buying decisions, accounts, and ownership without inferring duplicates |
| Commercial | Preserve stage, forecast category, amount, currency, and close date as reported inputs |
| Buyer evidence | Distinguish meaningful buyer actions from seller activity |
| Next action | Keep action, owner, timing, and acceptance status separate |
| Required milestone | Expose dependencies that contradict an entered close date |
| Outcome | Keep outcome state separate from seller-entered reason and evidence strength |
| Lineage | Record source system and source update time for auditability |

Identifiers may be pseudonymous when names are unnecessary. Do not export credentials, sensitive personal data, confidential free text, or fields the agent and intended audience are not authorized to access.
