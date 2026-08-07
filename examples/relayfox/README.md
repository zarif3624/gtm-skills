# RelayFox Example Workspace

RelayFox and every account, person, opportunity, claim, and amount in this folder are fictional. The files are designed to exercise the skills without using customer or personal data.

## Scenario

RelayFox sells a workflow-approval product to operations teams. The example includes:

- [shared GTM context](gtm-context.md) with verified facts and active hypotheses;
- [a discovery transcript](discovery-transcript.md) with ambiguous budget, timing, and authority;
- [a proposed positioning brief](positioning-brief.md) that maps capability, audience hypotheses, proof gaps, and claims to hold;
- [a proposed outbound plan](outbound-plan.md) that preserves those claim statuses through channel copy and launch review;
- [a pipeline export](pipeline.csv) containing duplicates, mixed currency, stale dates, and contradictory milestones;
- [a customer-outcomes snapshot](customer-outcomes.csv) that separates activity, adoption inputs, outcome evidence, support risk, and seller-generated expansion pressure.

## Try The Conversation Workflow

```text
Use $analyze-sales-call to analyze examples/relayfox/discovery-transcript.md with examples/relayfox/gtm-context.md as shared context. Then use $qualify-opportunity to create an evidence-based qualification update.
```

Inspect whether the output keeps reported budget, authority, urgency, and proposed next steps distinct from verified facts and accepted actions.

## Try The Positioning-To-Outbound Workflow

```text
Use $develop-positioning with examples/relayfox/gtm-context.md and examples/relayfox/discovery-transcript.md to create a proposed operations-leader message architecture. Then use $write-outbound to create a small message test without upgrading one buyer's statements into segment proof or reviving any held claim.
```

Compare the result with [the example positioning brief](positioning-brief.md) and [outbound plan](outbound-plan.md). Useful wording may differ. Inspect whether the same capabilities, hypotheses, limitations, approval states, held claims, and complete review boundary survive the handoff.

## Try The Management Workflow

```text
Use $review-pipeline to review examples/relayfox/pipeline.csv using examples/relayfox/gtm-context.md. Do not silently fix the source. Then use $forecast-sales to produce supportable downside, expected, and upside scenarios.
```

Inspect whether duplicate records, currency uncertainty, stale dates, missing buyer actions, and the security-timing contradiction survive the handoff into forecasting.

## Try The Sales Process Workflow

```text
Use $design-sales-process with examples/relayfox/gtm-context.md and examples/relayfox/pipeline.csv to propose the smallest evidence-based process improvement. Treat the current stages as reported inputs, not validated policy, and do not invent conversion benchmarks, service expectations, or historical stage events.
```

The example is too small and incomplete to validate a full stage model. A useful result should diagnose the present evidence gaps, propose buyer-state criteria and valid stop paths, and design a prospective pilot rather than rewriting current records.

## Try The Learning Workflow

```text
Treat the outcome notes in examples/relayfox/pipeline.csv as seller-entered evidence. Use $analyze-win-loss to explain what can and cannot be learned, then propose the smallest buyer-evidence collection plan.
```

The example has too little outcome evidence for causal conclusions. A useful response should say so.

## Try The Customer Outcomes Workflow

```text
Use $review-customer-outcomes to review examples/relayfox/customer-outcomes.csv with examples/relayfox/gtm-context.md. Separate activity, adoption, outcomes, realized value, renewal readiness, and expansion readiness. Do not turn the seller's 30% target into customer demand.
```

Inspect whether the output keeps Alder's 100 logins as activity only, surfaces its support and sponsor risks, and proposes the smallest validation plan. For Elm, it should preserve the stated measurement confirmation while keeping the test-workflow caveat and unverified baseline visible.

## Use Your Own Data Safely

Replace fictional records with approved, minimally necessary fields. Remove credentials, sensitive personal data, confidential free text, and any information the agent or intended audience should not access. Preserve source identifiers and access restrictions so conclusions remain auditable.
