# Structured GTM Context Pack

This vendor-neutral pack is an optional machine-readable companion to `.agents/gtm-context.md`. It helps agents, internal tools, and data pipelines exchange shared GTM context without promoting hypotheses into facts or dropping ownership, approval, access, and source restrictions.

## Files

- [context template](gtm-context-template.json) — an empty safe starting point;
- [closed JSON Schema](gtm-context.schema.json) — the interchange contract for claims, buying roles, and governance.

## Minimum Safe Workflow

1. Keep the human-readable `.agents/gtm-context.md` as the working narrative and preserve its version and as-of date.
2. Export only the smallest context needed by the receiving workflow. Do not include credentials, unnecessary personal data, confidential free text, or inaccessible sources.
3. Create one scoped claim per record and use `Verified`, `Reported`, `Inferred`, `Hypothesis`, `Unknown`, or `Contradicted` exactly as defined in the evidence contract.
4. Include a source locator, observation date, scope, and limitation whenever a material claim is not `Unknown`.
5. Keep evidence status separate from `Approved`, `Proposed`, `Rejected`, or `Unknown` publication or operating approval.
6. Treat empty arrays and null values as missing context, never as false, zero, disqualified, approved, or not applicable.
7. Preserve access classification and source restrictions at every handoff.
8. Require new authoritative evidence before strengthening a status; repetition or import success does not verify a claim.

The schema validates shape and vocabulary. It does not establish truth, grant source access, authorize publication, or replace responsible product, commercial, privacy, security, legal, and regional review.
