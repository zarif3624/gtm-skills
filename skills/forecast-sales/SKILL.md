---
name: forecast-sales
description: "Create, inspect, or explain a B2B sales forecast using CRM opportunities, historical conversion, pipeline changes, seller calls, or scenario assumptions. Use for commit and best-case calls, monthly or quarterly forecasting, forecast risk, rollups, coverage, sensitivity analysis, or explaining a forecast to leadership."
---

# Forecast Sales

Produce an auditable estimate with explicit assumptions, uncertainty, and downside. A forecast is a decision tool, not a target restated as confidence.

## Inputs

Read `.agents/gtm-context.md`. Confirm:

- as-of date, forecast period, currency, and target;
- opportunity scope and ownership;
- stage and forecast-category definitions;
- historical win, slip, and cycle data available;
- treatment of renewals, expansions, usage revenue, and one-time revenue.

## Data Checks

Check duplicates, missing amounts, close dates outside the period, stale opportunities, inconsistent currencies, unsupported stages, and required milestones after the close date. Report exclusions and transformations.

## Partial Or Aggregate Data

When deal-level rows or calibrated rates are missing, do not invent an allocation or stop at a refusal.

**Minimum response contract:** Even when the user asks for one exact number, produce a compact forecast artifact rather than only a warning or formula. It must include:

- closed revenue, central estimate, supportable forecast range, theoretical ceiling, and gap to target;
- downside, expected, and upside scenarios, using `Unknown` where a value is not supportable;
- included, excluded, and unallocatable contributions plus concentration or timing limits;
- the minimum additional evidence needed; and
- the governance checkpoint from the output template.

- Calculate exact supported values such as closed revenue.
- Show the requested formula and explain why the missing fields prevent a supportable central estimate.
- Build downside, expected, and upside scenarios even when a scenario value must be `Unknown`.
- Use closed revenue as a supported floor when appropriate. Label the all-open-pipeline value as a theoretical ceiling, not an upside forecast.
- List the minimum deal-level fields or historical inputs needed to replace `Unknown` values.
- Keep timing, concentration, and milestone contradictions visible even when they cannot be quantified.

## Build The Forecast

Use the simplest method supported by the data. Read [forecast methods](references/methods.md).

1. Establish closed revenue.
2. Inspect seller commit deal by deal; seller category is evidence, not certainty.
3. Estimate likely in-period outcomes from verified buyer progress and historical behavior.
4. Build at least downside, expected, and upside scenarios.
5. Identify concentration, slip, and timing risk.
6. Reconcile the forecast with the target without changing assumptions to close the gap.
7. Record assumptions so the forecast can be compared with the eventual outcome.
8. Surface who must approve scope, currency treatment, method, exclusions, and provisional scenario assumptions before the forecast is used for an operating decision.

## Output

Use [the forecast template](assets/forecast.md). Provide:

- as-of date and scope;
- forecast range and central estimate;
- closed, commit, expected, upside, and excluded values;
- deal-level contribution with method and evidence;
- scenario assumptions;
- gap to target;
- top risks and sensitivities;
- data-quality limitations;
- governance decisions and approver status;
- actions that improve outcomes separated from actions that improve forecast accuracy.

Never present a stage-weighted total as precise truth. Never infer missing historical rates. Use ranges when uncertainty is material, and use `Unknown` when even a supportable range is not available. Do not imply that forecast scope, transformations, or provisional assumptions are approved; label each decision and approver as approved, proposed, or unknown.
