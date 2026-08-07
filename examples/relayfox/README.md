# RelayFox Example Workspace

RelayFox and every account, person, opportunity, claim, and amount in this folder are fictional. The files are designed to exercise the skills without using customer or personal data.

## Scenario

RelayFox sells a workflow-approval product to operations teams. The example includes:

- [shared GTM context](gtm-context.md) with verified facts and active hypotheses;
- [a discovery transcript](discovery-transcript.md) with ambiguous budget, timing, and authority;
- [a pipeline export](pipeline.csv) containing duplicates, mixed currency, stale dates, and contradictory milestones.

## Try The Conversation Workflow

```text
Use $analyze-sales-call to analyze examples/relayfox/discovery-transcript.md with examples/relayfox/gtm-context.md as shared context. Then use $qualify-opportunity to create an evidence-based qualification update.
```

Inspect whether the output keeps reported budget, authority, urgency, and proposed next steps distinct from verified facts and accepted actions.

## Try The Management Workflow

```text
Use $review-pipeline to review examples/relayfox/pipeline.csv using examples/relayfox/gtm-context.md. Do not silently fix the source. Then use $forecast-sales to produce supportable downside, expected, and upside scenarios.
```

Inspect whether duplicate records, currency uncertainty, stale dates, missing buyer actions, and the security-timing contradiction survive the handoff into forecasting.

## Try The Learning Workflow

```text
Treat the outcome notes in examples/relayfox/pipeline.csv as seller-entered evidence. Use $analyze-win-loss to explain what can and cannot be learned, then propose the smallest buyer-evidence collection plan.
```

The example has too little outcome evidence for causal conclusions. A useful response should say so.

## Use Your Own Data Safely

Replace fictional records with approved, minimally necessary fields. Remove credentials, sensitive personal data, confidential free text, and any information the agent or intended audience should not access. Preserve source identifiers and access restrictions so conclusions remain auditable.
