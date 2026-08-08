# Ten-Minute Quickstart

Start with the artifact you need. Shared GTM context improves repeated work, but it is not required for a first useful result.

Prefer a role-based path? The [playbooks](docs/playbooks/README.md) give founders, AEs, SDRs, and RevOps leaders a first-week skill sequence. In a hurry? Grab one prompt from the [prompt cookbook](docs/prompt-cookbook.md), or preview artifacts in the [output gallery](docs/gallery.md) before installing anything.

## 1. Preview And Install

```bash
npx skills add zarif3624/gtm-skills --list
npx skills add zarif3624/gtm-skills --skill analyze-sales-call --skill qualify-opportunity --skill review-pipeline --skill forecast-sales
```

Use your agent's normal skill directory when installing manually. The repository itself remains vendor-neutral.

## 2. Try A Safe End-To-End Example

Clone the repository, then ask:

```text
Use $review-pipeline to review examples/relayfox/pipeline.csv with examples/relayfox/gtm-context.md as context. Do not silently fix the source. Then use $forecast-sales to build downside, expected, and upside scenarios.
```

A useful response should keep the duplicate opportunity, mixed currency, stale next step, and security-after-close contradiction visible. It should not invent a conversion rate or a precise central forecast.

## 3. Use Your Own Transcript

Provide an approved transcript or notes and ask:

```text
Use $analyze-sales-call to separate customer evidence, seller claims, decisions, objections, and next steps. Then use $qualify-opportunity to show what changed and what remains unknown.
```

Remove credentials, sensitive personal data, and confidential content the agent or audience should not access. Preserve timestamps or section locators so conclusions remain auditable.

## 4. Use Your Own Pipeline

Map the smallest approved export with the [generic CRM handoff pack](reference-packs/generic-crm/). Keep the raw snapshot immutable. Ask for pipeline review before forecasting so duplicates, currencies, date contradictions, and missing buyer evidence survive the handoff.

## 5. Review Customer Outcomes Without Overclaiming

Try the fictional post-sale snapshot:

```text
Use $review-customer-outcomes to review examples/relayfox/customer-outcomes.csv. Keep activity, adoption, outcomes, realized value, renewal readiness, and expansion readiness separate.
```

A useful result will not call an account healthy from login count alone or transform an internal seat-growth target into customer demand. It will identify the smallest customer, measurement, support, sponsor, and contract checks needed next.

## 6. Improve The Process Prospectively

When stages or CRM rules are unreliable, ask for a proposed design rather than retroactive certainty:

```text
Use $design-sales-process to audit our current stages and propose buyer-state entry and exit evidence, valid stop paths, minimum fields, measurement definitions, and a bounded pilot. Do not backfill stage history or import generic benchmarks.
```

Keep process design separate from live CRM configuration, migration, compensation, and personnel decisions until their authorized owners review and approve the change.

## What Good Looks Like

- Material claims point to evidence or are labeled `Reported`, `Inferred`, `Hypothesis`, `Unknown`, or `Contradicted`.
- Proposed owners, dates, approvals, and customer actions do not appear as confirmed.
- Missing data narrows the answer but does not cause a bare refusal.
- Exact supported values, theoretical ceilings, and plausible forecast scenarios are distinct.
- Actions that improve an outcome are separate from data cleanup and forecast-governance actions.
- A clear no, loss, disqualification, or revised date remains a valid outcome.

See the [evidence and status contract](docs/evidence-contract.md) for the shared vocabulary and handoff rules.

## If The Result Is Weak

- Name the skill explicitly, such as `$forecast-sales`.
- State the decision or artifact you need, not only the data you have.
- Add source locators, the as-of date, scope, currency, and definitions when available.
- Ask the agent to list exclusions and transformations rather than silently cleaning the data.
- Treat unknowns as a signal to collect the next smallest evidence, not as permission to fill gaps.
