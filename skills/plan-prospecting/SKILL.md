---
name: plan-prospecting
description: "Create a B2B prospecting strategy, account list plan, or contact coverage model from an ICP. Use when building pipeline, prioritizing territories, selecting prospect data fields and sources, defining account tiers, or deciding who to contact and why before launching outbound."
---

# Plan Prospecting

Turn an ICP into a finite, explainable prospecting plan. Optimize for learning and relevance before list size.

## Workflow

1. Read `.agents/gtm-context.md` and an existing ICP if available.
2. Confirm the goal: new logo, expansion, event follow-up, territory penetration, or hypothesis test.
3. Define hard exclusions before positive filters.
4. Translate each ICP criterion into an observable field, search filter, or research step.
5. Define account tiers and the effort allowed per tier.
6. Define buying-group coverage: user, champion, economic buyer, technical approver, and likely blocker where relevant.
7. Select data sources based on coverage, freshness, permission, and cost. Never imply a data source is complete.
8. Define validation and deduplication rules before enrichment.
9. Create a small pilot batch and learning loop before scaling.

## Data Rules

- Collect only fields needed for a clear sales purpose.
- Do not source sensitive personal data or infer protected characteristics.
- Keep company fit, contact relevance, intent, and timing as separate dimensions.
- Mark unverified emails, roles, and trigger events for validation.
- Respect applicable consent, suppression, privacy, and platform rules.

## Output

Produce a prospecting plan with:

- objective and success metric;
- target segment and exclusions;
- account-tier definitions;
- required account and contact fields;
- source plan and freshness expectations;
- buying-group coverage target;
- pilot size and selection method;
- quality checks and suppression rules;
- handoff fields for research and outreach;
- weekly learning questions.

Also provide the ordered column schema in [the list schema](assets/prospect-list-schema.csv) when the user wants a CSV-ready structure.

Do not generate a large list merely to appear productive. If fit criteria are weak, return to `define-icp`.
