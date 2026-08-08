# RevOps Leader Playbook

For RevOps and sales leaders: you own the system — process, pipeline truth, forecast credibility, territory fairness, and the learning loop. These skills treat CRM stage, probability, and seller confidence as inputs to interrogate, not facts to aggregate.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context --skill design-sales-process --skill review-pipeline --skill forecast-sales --skill plan-territories --skill analyze-win-loss --skill coach-sales-rep
```

## Week 1 — Establish shared context and inspect the pipeline

Create the team-wide context once with [`gtm-context`](../../skills/gtm-context/); every artifact your team produces afterward starts from the same facts.

Then run the flagship loop on a real export:

```text
Use $review-pipeline on this CRM export. Do not silently fix the source. Surface duplicates, currency mixes, stale next steps, stage-date contradictions, and deals with no buyer-verified evidence. Then use $forecast-sales for downside, expected, and upside scenarios with every assumption stated.
```

[`review-pipeline`](../../skills/review-pipeline/) finds what dashboard rollups hide, and [`forecast-sales`](../../skills/forecast-sales/) produces a forecast whose assumptions are listed and challengeable — the difference between a number you present and a number you defend. Map your export safely with the [generic CRM handoff pack](../../reference-packs/generic-crm/); the raw snapshot stays immutable, so lineage survives audits.

## Week 2 — Fix the process the pipeline revealed

```text
Use $design-sales-process to audit our stages against buyer decision states. Where do stages measure seller activity instead of buyer commitment? Propose exit evidence per stage and a rollout plan the team will actually adopt.
```

[`design-sales-process`](../../skills/design-sales-process/) designs buyer-state stages with evidence gates — so "Stage 4" starts meaning something again.

## Week 3 — Coverage and capacity

```text
Use $plan-territories with this account universe and current team roster. Show capacity scenarios, fairness tradeoffs, and the assignment rules behind each option.
```

[`plan-territories`](../../skills/plan-territories/) makes the tradeoffs explicit, which is most of what a territory fight actually needs.

## Week 4 — Close the learning loop

```text
Use $analyze-win-loss on last quarter's closed opportunities and decision notes. Separate what buyers said from what reps recorded. What patterns distinguish wins from no-decisions, and what evidence would confirm them?
```

Feed confirmed patterns back into your ICP and process. For individual reps, [`coach-sales-rep`](../../skills/coach-sales-rep/) turns call evidence into one narrow developmental experiment at a time — observable behavior in, focused experiment out, no personality reviews.

## The operating cadence

- **Weekly**: pipeline review before the forecast call, never after.
- **Monthly**: win/loss pass over the month's closed deals.
- **Quarterly**: process audit and territory capacity check.

Every artifact keeps facts, inferences, and unknowns separate, so when the board asks "why do you believe this number?", the answer is in the document — with lineage. See the [evidence contract](../evidence-contract.md) for the vocabulary that makes the artifacts auditable, and the [evidence ledger pack](../../reference-packs/evidence-ledger/) for moving claims between tools without losing provenance.
