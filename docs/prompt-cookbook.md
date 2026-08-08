# Prompt Cookbook

One battle-ready prompt per skill. Copy, replace the bracketed parts, paste into your agent. Every prompt assumes the skill is installed (`npx skills add zarif3624/gtm-skills`) and works with or without a shared `.agents/gtm-context.md`.

The prompts are deliberately demanding about evidence — that is what makes the output usable in front of a buyer, a CFO, or a board.

## Foundation

**[`gtm-context`](../skills/gtm-context/)** — run once, benefit everywhere:

```text
Create our GTM context from the product docs, pricing, and customer material in this repository. Keep verified facts, inferences, and unknowns labeled. Ask me only for gaps that matter.
```

## Strategy

**[`define-icp`](../skills/define-icp/)**:

```text
Use $define-icp to refine our ICP using last quarter's wins, losses, and churn. Name counterexamples that contradict the current profile and the evidence that would falsify the new one.
```

**[`develop-positioning`](../skills/develop-positioning/)**:

```text
Use $develop-positioning to audit our homepage messaging against what buyers actually said in these call notes. Map every claim to its proof or mark it unproven.
```

**[`design-sales-process`](../skills/design-sales-process/)**:

```text
Use $design-sales-process to audit our stages against buyer decision states. Where do stages measure seller activity instead of buyer commitment? Propose exit evidence per stage.
```

**[`plan-territories`](../skills/plan-territories/)**:

```text
Use $plan-territories with this account list and team roster. Show capacity scenarios, fairness tradeoffs, and the assignment rules behind each option.
```

## Targeting and outreach

**[`research-account`](../skills/research-account/)**:

```text
Use $research-account on [company] before Thursday's call. Cite every external claim with a source and access date. Mark what you could not verify instead of guessing.
```

**[`plan-account`](../skills/plan-account/)**:

```text
Use $plan-account for [account]: current footprint, relationship map, whitespace, and the investments worth making this year — with the evidence behind each.
```

**[`plan-prospecting`](../skills/plan-prospecting/)**:

```text
Use $plan-prospecting to turn our ICP into a tiered account and contact plan for this quarter, prioritized by observable trigger events.
```

**[`write-outbound`](../skills/write-outbound/)**:

```text
Use $write-outbound for [contact] at [account] from this research brief. Three touches. Every personalized line must trace to a cited fact — no fake familiarity.
```

## Conversations

**[`prepare-discovery`](../skills/prepare-discovery/)**:

```text
Use $prepare-discovery for a 45-minute call with a [title] at [account]. Hypotheses to test, questions that test them, and what a disqualifying answer sounds like.
```

**[`analyze-sales-call`](../skills/analyze-sales-call/)**:

```text
Use $analyze-sales-call on this transcript. Separate what the customer said from what we claimed, list decisions, objections, and next steps with timestamps.
```

**[`coach-sales-rep`](../skills/coach-sales-rep/)**:

```text
Use $coach-sales-rep with these three call transcripts for [rep]. One narrow, observable development experiment — not a personality review.
```

## Deal execution

**[`qualify-opportunity`](../skills/qualify-opportunity/)**:

```text
Use $qualify-opportunity on [deal] from these notes. What is verified, what is assumed, and what single next step tests the biggest unknown?
```

**[`plan-deal`](../skills/plan-deal/)**:

```text
Use $plan-deal for [opportunity]. Buying group map, competitive risk, and the three actions that most reduce uncertainty this week.
```

**[`handle-objections`](../skills/handle-objections/)**:

```text
Use $handle-objections on: "[objection]". Diagnose what it actually is — price, priority, trust, or a polite no — before drafting a response.
```

**[`prepare-demo`](../skills/prepare-demo/)**:

```text
Use $prepare-demo for [account]'s technical evaluation. Build around their stated outcomes, define what success looks like to each attendee, and plan the follow-up.
```

**[`build-business-case`](../skills/build-business-case/)**:

```text
Use $build-business-case for [account] using only inputs the buyer gave us or we can source. Scenarios, break-even, and every assumption inspectable. No invented ROI.
```

**[`prepare-negotiation`](../skills/prepare-negotiation/)**:

```text
Use $prepare-negotiation for [deal]. Packages, trades, and walk-away points within my approved discount authority. Flag anything needing approval I do not have.
```

**[`create-mutual-action-plan`](../skills/create-mutual-action-plan/)**:

```text
Use $create-mutual-action-plan for [opportunity] targeting [date]. Mark every step Proposed until the buyer accepts it.
```

## Management

**[`review-pipeline`](../skills/review-pipeline/)**:

```text
Use $review-pipeline on this CRM export. Do not silently fix the source. Surface duplicates, currency mixes, stale next steps, and deals with no buyer-verified evidence.
```

**[`forecast-sales`](../skills/forecast-sales/)**:

```text
Use $forecast-sales from the reviewed pipeline. Downside, expected, and upside scenarios with every assumption stated and challengeable.
```

## Post-sale and learning

**[`handoff-customer`](../skills/handoff-customer/)**:

```text
Use $handoff-customer for [account]. Every promise made in the sales cycle, goals, risks, and open items — so customer success inherits context, not surprises.
```

**[`review-customer-outcomes`](../skills/review-customer-outcomes/)**:

```text
Use $review-customer-outcomes for [account] with this usage and support data. Value evidence, renewal readiness, and expansion hypotheses — labeled, not assumed.
```

**[`analyze-win-loss`](../skills/analyze-win-loss/)**:

```text
Use $analyze-win-loss on last quarter's closed opportunities. Separate what buyers said from what reps recorded. Which patterns distinguish wins from no-decisions?
```

**[`plan-partner-channel`](../skills/plan-partner-channel/)**:

```text
Use $plan-partner-channel to design a referral motion with [partner type]. Testable, deduplicated against direct pipeline, with clear rules of engagement.
```

## Chaining prompts

The highest-leverage sequences:

- **The deal loop**: `$analyze-sales-call` → `$qualify-opportunity` → `$plan-deal` — after every significant call.
- **The forecast loop**: `$review-pipeline` → `$forecast-sales` — review before the number, never after.
- **The outbound loop**: `$research-account` → `$write-outbound` — never write before researching.
- **The learning loop**: `$analyze-win-loss` → `$define-icp` → `$develop-positioning` — quarterly.

For role-based sequences with more context, see the [playbooks](playbooks/README.md).
