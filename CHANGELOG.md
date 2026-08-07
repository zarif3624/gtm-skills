# Changelog

All notable project changes are documented here. The project uses semantic version tags when a release is published; entries under `Unreleased` are not yet a compatibility promise.

## Unreleased

### Added

- Sales-call analysis, win/loss analysis, positioning development, territory planning, sales-process design, negotiation preparation, strategic account planning, partner-channel planning, evidence-based sales coaching, customer-outcome review, and buyer business-case skills.
- One adversarial behavioral case per skill, twelve cross-skill journey cases, and a contrastive routing corpus covering every skill.
- Reproducible forward-test reports with raw responses, assertion evidence, critical-failure handling, lineage-aware retests, and historical result retention.
- Self-contained blind routing packets with installed metadata, plus computed reports that keep expected and excluded labels hidden until scoring.
- A drift-checked machine-readable quality summary for catalog, coverage, and current evidence counts.
- A generated machine-readable skill catalog with interface metadata, resource inventory, and deterministic package digests.
- A schema-versioned deterministic release manifest binding skill packages, eval definitions, examples, reference packs, quality artifacts, and current raw evidence by SHA-256.
- A validated RelayFox end-to-end fictional workspace for positioning, outbound, transcript, qualification, process, pipeline, forecast, customer-outcome, and learning workflows.
- A vendor-neutral CRM handoff pack with CSV templates, transformation governance, currency policy, and a matching JSON Schema.
- A vendor-neutral evidence and action ledger pack with matching CSV and JSON contracts for portable claim and commitment status.
- A vendor-neutral structured GTM context pack with a closed JSON contract for portable claims, buyer roles, proof, governance, and source restrictions.
- Ten-minute quickstart, evidence/status contract, compatibility evidence matrix, product roadmap, contribution templates, and expanded security policy.

### Changed

- Every skill now defines a concrete output artifact, partial-input behavior, human-review boundaries, source-instruction safety, and UI metadata.
- Owners, dates, approvals, buyer actions, and milestones distinguish confirmed, proposed, accepted, approved, and unknown states.
- Forecasting now keeps uncalibrated central estimates and ranges unknown, separates theoretical ceilings, and exposes governance decisions.
- Templates use evidence semantics instead of vague confidence labels.
- README catalog and workflow guidance now cover the full 25-skill collection.

### Security

- Repository checks reject symbolic links, escaped or orphaned resources, broken documentation links, common live-credential shapes, and unsafe example identifiers.
- Source instructions in webpages, CRM fields, transcripts, and quoted material are treated as untrusted data across every portable skill.

### Validation

- One dependency-free command now runs unit tests, supply-chain scanning, skill/package checks, eval and routing validation, behavioral-report validation, example validation, and reference-pack validation.
- A reviewed quality policy enforces zero current partials or failures and zero uncovered behavioral definitions, so new definitions cannot ship without current evidence.
- Current behavioral evidence is now rejected when any target skill directory differs from the report's tested commit, including untracked resources.
- The current recorded Codex lineage has all 37 behavioral definitions passing: 25 isolated skill cases and 12 cross-skill journeys. Earlier partial and failed runs remain available as regression history.
- The latest recorded metadata-only routing run selected the exact minimal skill set for all 28 requests with zero excluded-neighbor selections; the earlier 25-, 26-, and 27-request runs remain available as history.

## 0.1.0

- Initial evidence-first GTM skill collection.
