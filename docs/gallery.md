# What You Actually Get

Sample excerpts of the artifacts these skills produce, so you can judge the output before installing anything. All examples below use the fictional [RelayFox workspace](../examples/relayfox/) — every account, amount, and quote is invented, and the excerpts are illustrative renderings of what a correct run surfaces, condensed for reading. Your agent's exact wording will differ; the evidence behavior should not.

The RelayFox pipeline export is deliberately dirty: a duplicate opportunity with conflicting stages, mixed currencies with no conversion policy, a past-due next step, a security milestone scheduled after the close date, and a "Closed Lost — Price" with no buyer evidence. A useful pipeline review keeps every one of those problems visible. That is the test.

## Pipeline review (`review-pipeline`)

> ### Portfolio integrity findings
>
> | Finding | Records | Status | Why it matters |
> | --- | --- | --- | --- |
> | Duplicate opportunity ID with conflicting stage (Validation vs Proposal), amount (€95k vs €105k), and forecast category | RF-102 | **Verified** (source rows conflict) | The same deal is counted twice; Commit total is unreliable until one record is authoritative |
> | Mixed USD/EUR amounts with no stated conversion policy | RF-102 | **Verified** | Any single-currency pipeline total silently invents an exchange-rate decision |
> | Required security review scheduled 2026-09-10, after the entered close date 2026-08-31 | RF-103 | **Verified** | The close date cannot hold; Commit categorization is contradicted by the deal's own milestones |
> | Next-step date in the past (2026-08-01) with no recorded buyer action since 2026-07-20 | RF-102 | **Verified** | "Best Case" rests on a stalled thread |
> | Twelve seller emails, no meaningful buyer action | RF-104 | **Verified** | Activity is seller-generated; no evidence of buyer engagement |
> | Loss reason "Price" entered by seller with no buyer interview or decision artifact | RF-106 | **Unverified** | Feeds a false "we lose on price" narrative if aggregated |
>
> ### What was *not* done
>
> The source file was not modified. No currency conversion was applied. No duplicate was deleted — resolving RF-102 requires an owner decision, proposed below.

## Forecast (`forecast-sales`)

> ### Scenario summary
>
> Amounts are stated per currency; no conversion policy exists in context, so no blended total is offered.
>
> | Scenario | Basis | USD | EUR |
> | --- | --- | --- | --- |
> | Downside | Only deals with buyer-verified next steps and no unresolved contradictions (RF-105) | $150k | — |
> | Expected | Downside + RF-101 if validation outline is accepted by 2026-08-10 | $270k | — |
> | Upside | Expected + RF-102 (single record, lower amount) and RF-103 if security timing is renegotiated | $480k | €95k |
>
> **Assumptions you can challenge:** RF-102 is counted once at the more conservative €95k/Validation record pending owner resolution. RF-103 is excluded from Expected because its close date is contradicted by its own security milestone. RF-104 is excluded from all scenarios: there is no recorded buyer action. No historical conversion rates were applied — none exist in the provided context.

## Qualification update (`qualify-opportunity`)

> ### Alder Manufacturing — after discovery call
>
> | Dimension | Status | Evidence |
> | --- | --- | --- |
> | Problem | **Verified** | Ops lead described approval backlog and rework cost in their own words (transcript, lines 41–58) |
> | Budget | **Unknown** | "We'd have to look at budget in the fall" — timing signal, not a budget confirmation |
> | Authority | **Inferred** | Ops lead references a VP sign-off; VP has not been engaged |
> | Timeline | **Unknown** | September mentioned once, by the seller, not confirmed by the buyer |
>
> **Biggest unknown:** whether the VP sees this problem as worth funding. **Next validation step (proposed):** buyer-accepted validation outline by 2026-08-10, which tests authority and timing in one move.

---

None of these excerpts contains a number the source data could not support. No invented conversion rates, no fabricated close probabilities, no "industry benchmark" filler. If your current AI sales workflow can't show you where its numbers came from, that's the gap this project exists to close.

**Run it yourself:** clone the repo and use the prompts in the [RelayFox workspace](../examples/relayfox/), or start from the [quickstart](../QUICKSTART.md). Scoring criteria for correct behavior live in the [evaluation guide](../evals/README.md).
