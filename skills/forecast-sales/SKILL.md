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

## Build The Forecast

Use the simplest method supported by the data. Read [forecast methods](references/methods.md).

1. Establish closed revenue.
2. Inspect seller commit deal by deal; seller category is evidence, not certainty.
3. Estimate likely in-period outcomes from verified buyer progress and historical behavior.
4. Build at least downside, expected, and upside scenarios.
5. Identify concentration, slip, and timing risk.
6. Reconcile the forecast with the target without changing assumptions to close the gap.
7. Record assumptions so the forecast can be compared with the eventual outcome.

## Output

Provide:

- as-of date and scope;
- forecast range and central estimate;
- closed, commit, expected, upside, and excluded values;
- deal-level contribution with method and evidence;
- scenario assumptions;
- gap to target;
- top risks and sensitivities;
- data-quality limitations;
- actions that improve outcomes separated from actions that improve forecast accuracy.

Never present a stage-weighted total as precise truth. Never infer missing historical rates. Use ranges when uncertainty is material.
