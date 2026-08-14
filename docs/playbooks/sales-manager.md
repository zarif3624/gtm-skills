# Sales Manager Playbook

For frontline sales managers running weekly pipeline reviews, forecast calls, deal coaching, and one-to-ones. This playbook turns the same approved evidence into separate operating artifacts without treating CRM stage, seller confidence, activity volume, or one call as performance truth.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill analyze-sales-call --skill qualify-opportunity --skill review-pipeline --skill forecast-sales --skill plan-deal --skill coach-sales-rep
```

Use only approved CRM exports, call material, and coaching notes. Remove credentials, unnecessary personal data, and content the intended audience should not access. Confirm recording permissions and internal access rules before using transcripts.

## Before the weekly team call - inspect pipeline truth

Take an immutable snapshot with its as-of date, scope, currency, and source fields. Then run the pipeline review before the forecast call so data defects and unsupported stages remain visible instead of becoming forecast assumptions.

```text
Use $review-pipeline on this approved weekly CRM export. Preserve the source values. Surface duplicates, currency conflicts, stale next steps, stage-evidence gaps, and close-date contradictions. Separate selling actions from CRM cleanup, and keep every suggested owner or date Proposed or Unknown unless the source confirms it.
```

Use the output to choose the few deals that need inspection. Do not rank reps from raw activity, pipeline volume, or data-quality defects without checking territory, tenure, source coverage, and manager-created constraints.

## During the forecast call - challenge assumptions consistently

Use the reviewed snapshot, documented exclusions, and approved forecast definitions:

```text
Use $forecast-sales on the reviewed pipeline. Build downside, expected, and upside scenarios. Show deal-level contribution, assumptions, exclusions, concentration, and timing risk. Do not change assumptions to close the target gap or convert the all-open-pipeline ceiling into a plausible forecast.
```

Seller commit is an input, not certainty. Keep actions that could improve an outcome separate from actions that only improve forecast accuracy. Any scope, currency treatment, or provisional scenario decision stays Proposed until its authorized owner approves it.

## For a deal review - start from buyer evidence

When a deal needs help, inspect the strongest available customer evidence rather than asking the rep to defend the CRM field:

```text
Use $analyze-sales-call on the latest approved call notes or transcript. Separate customer statements, seller claims, decisions, objections, and next steps with source locators. Then use $qualify-opportunity to show what is supported, contradicted, and Unknown.
```

Follow with a bounded deal plan:

```text
Use $plan-deal for [opportunity] from the call analysis and qualification artifact. Map the verified buying group, decision path, risks, and the three actions that most reduce buyer uncertainty this week. Do not invent access, authority, urgency, or customer commitment.
```

A clear no, disqualification, revised date, or narrower next step is a valid outcome. Do not turn internal target pressure into a claim about the buyer.

## In one-to-ones - coach observable behavior

Use coaching evidence for development, not personality judgment:

```text
Use $coach-sales-rep with these approved call excerpts, manager observations, and prior coaching notes. Separate observation from interpretation and outcome. Identify one behavior experiment, counterexamples, rep and manager responsibilities, and the minimum evidence needed to review progress.
```

Ask for the rep's perspective before treating an interpretation as shared. One call supports an episode review, not a stable trait. If the request could affect compensation, discipline, promotion, termination, or another formal employment decision, use the skill only to organize evidence and route the decision to authorized HR, legal, privacy, employee-relations, and business owners.

## The operating cadence

- **Before the team call:** freeze the source snapshot and run `$review-pipeline`.
- **During the forecast call:** use `$forecast-sales` on the reviewed scope and record assumption status.
- **For selected deals:** use `$analyze-sales-call`, `$qualify-opportunity`, and `$plan-deal` to focus inspection on buyer evidence and next validation actions.
- **In one-to-ones:** use `$coach-sales-rep` for one narrow developmental experiment with rep input.
- **After the week:** compare proposed actions with what was confirmed, accepted, completed, contradicted, or remains Unknown.

Use the [evidence and status contract](../evidence-contract.md) when moving claims between call notes, deal plans, pipeline reviews, forecasts, and coaching artifacts. The [generic CRM handoff pack](../../reference-packs/generic-crm/) preserves raw values and transformation lineage; the [evidence and action ledger pack](../../reference-packs/evidence-ledger/) preserves source, owner, and status without turning proposals into facts.
