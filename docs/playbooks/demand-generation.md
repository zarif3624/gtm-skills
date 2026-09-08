# Demand Generation Leader Playbook

For demand generation leaders turning market evidence into measurable acquisition experiments and inspectable pipeline learning. This playbook connects ICP, positioning, audience design, outreach, pipeline review, and outcome analysis without treating clicks, form fills, or sourced pipeline as proof of buyer progress or caused revenue.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context --skill define-icp --skill develop-positioning --skill plan-prospecting --skill write-outbound --skill review-pipeline --skill analyze-win-loss
```

Use only data approved for the intended purpose and audience. Remove credentials, unnecessary personal data, and restricted customer or account details. Confirm consent, suppression, privacy, platform, regional outreach, retention, and vendor-use requirements before uploading a list or activating any channel. Keep media spend, data purchases, live sends, CRM writes, scoring changes, and public claims behind their authorized human owners.

## Day 1 - Define the market and funnel decision

Start with the business decision, target market, sales motion, current evidence, and measurement definitions:

```text
Use $gtm-context to create or update our shared GTM context from approved product, market, customer, pipeline, and campaign sources. Separate Verified facts, Inferred interpretations, Hypotheses, and Unknowns. Record source dates, audiences, restrictions, and the human reviewers required before activation.
```

Then make the audience thesis falsifiable:

```text
Use $define-icp to compare the segments supported by our evidence. Define fit criteria, exclusions, disqualifiers, observable fields, evidence strength, sample limits, and a bounded validation plan. Do not turn campaign engagement, seller preference, or an internal target into verified customer fit.
```

State the primary decision the experiment should inform. Define each funnel state, denominator, cohort entry date, source system, and owner before comparing rates. Keep the audience, budget, launch date, and success threshold **Proposed** or **Unknown** until the responsible owner accepts them.

## Day 2 - Build a claim-safe message hypothesis

Use customer and decision evidence to frame one testable message:

```text
Use $develop-positioning for [segment and buying situation]. Build a claim ledger, alternatives, message pillars, proof status, limitations, objections, and one bounded message test. Keep supported capability, expected workflow change, customer outcome, and approved public proof distinct.
```

A message that earns attention is not necessarily accurate, useful, or suitable for publication. Product, customer proof, brand, legal, privacy, security, accessibility, and regional reviewers must approve the claims and intended audience that fall within their authority. Leave unsupported claims held; do not strengthen them to make a test more attractive.

## Day 3 - Design the audience and outreach pilot

Translate the ICP into a finite, explainable test population:

```text
Use $plan-prospecting to design a small pilot for [objective]. Define exclusions first, then observable fit fields, account tiers, buying-group coverage, source freshness, deduplication, consent and suppression checks, selection method, and stop criteria. Return to the ICP if the criteria are not scoreable.
```

Create outreach only after the audience and claims are reviewable:

```text
Use $write-outbound to create a responsible sequence for the approved pilot. Ground each message in a verified signal or transparent role-level hypothesis, preserve claim status, provide approved personalization fallbacks, make opting out easy, and test one variable. Do not fabricate familiarity, intent, urgency, referrals, or customer proof.
```

The output is a proposed experiment, not permission to buy data, upload contacts, spend budget, or send messages. An authorized human must approve channel activation, sender identity, audience, claims, consent and suppression handling, timing, spend, data purchases, list uploads, live sends, CRM writes, scoring changes, public claims, and stop conditions.

## Day 4 - Inspect buyer progress and pipeline handoff

Join campaign records to the canonical account, person, and opportunity records without silently merging or overwriting them:

```text
Use $review-pipeline to inspect the canonical opportunity population associated with this pilot. Preserve stable IDs, duplicates, source lineage, currencies, dates, stage evidence, accepted next steps, and exclusions. Separate campaign touch, response, qualified conversation, created opportunity, buyer evidence, and forecast category.
```

**Engagement is not buyer progress. Attributed pipeline is not caused revenue.** A click, reply, meeting, MQL, or campaign-member record cannot establish opportunity quality, buyer commitment, or incremental impact by itself. Keep platform attribution, first or last touch, self-reported buyer source, sales interpretation, and experimental evidence as separate fields.

## Day 5 - Learn from outcomes without rewriting history

Use the complete eligible cohort, including nonresponses, disqualifications, no-decisions, losses, and wins:

```text
Use $analyze-win-loss for the pilot cohort and an explicitly comparable baseline or holdout when available. Audit identities and outcome labels, preserve buyer and seller evidence separately, report counts and sample size beside rates, inspect counterexamples, and propose the next falsifiable audience or message test. Do not infer causality from attribution fields.
```

Do not backfill favorable stages, change source values, exclude inconvenient outcomes, or present a tiny or biased sample as a stable pattern. Use `Hypothesis` for an untested explanation and `Unknown` when the evidence cannot distinguish message, audience, channel, seller follow-up, product fit, seasonality, or another confounder.

## Measure the acquisition system

Keep each layer and denominator visible:

| Layer | Inspect | Do not claim |
| --- | --- | --- |
| Eligibility and delivery | Approved audience, exclusions, valid delivery, suppression, spend | Delivered records were relevant or consented everywhere |
| Engagement | Views, clicks, replies, form completions with bot and missingness limits | Attention proves interest, fit, or buyer progress |
| Conversation | Positive replies, held conversations, accepted follow-ups, disqualifications | A booked meeting is a qualified opportunity |
| Buyer progress | Confirmed problem, stakeholders, criteria, decision action, valid no | Seller activity or CRM stage proves commitment |
| Pipeline | Canonical opportunities, accepted stage evidence, value definition, cohort | Attribution proves the campaign created pipeline |
| Outcome | Wins, losses, no-decisions, value, cost, period, counterfactual limits | Association proves incremental revenue or ROI |

Report the numerator, denominator, cohort window, spend scope, source coverage, missingness, duplicate handling, and material definition changes. Present cost per outcome, conversion, payback, or ROI only when the underlying costs, values, and attribution assumptions are supported and inspectable. A credible result can be no lift, a negative effect, or evidence that measurement is not yet decision-ready.

## The operating cadence

- **Before launch:** freeze the audience, claims, exclusions, review matrix, measurement contract, and stop conditions.
- **During the pilot:** monitor consent, suppression, delivery quality, spend, complaints, and material data drift without silently changing the cohort.
- **Weekly:** inspect conversations and canonical pipeline evidence; keep cleanup work separate from selling actions and experiment results.
- **At the decision date:** compare the full cohort, counterexamples, costs, and alternative explanations; continue, revise, or stop.
- **After the decision:** record what changed, who approved it, and which evidence remains valid for the next test.

Use the [evidence and status contract](../evidence-contract.md) when moving claims and records between context, ICP, positioning, prospecting, outreach, pipeline, and win/loss analysis. Preserve source, date, audience, status, limitation, and approval so campaign polish cannot convert a hypothesis into market truth.
