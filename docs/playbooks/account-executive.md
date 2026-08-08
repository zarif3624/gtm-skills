# Account Executive Playbook

For AEs carrying a quota: you live in discovery calls, deal reviews, demos, and negotiations. This playbook wires the skills into the rhythm of an active deal so every stage produces an inspectable artifact instead of optimistic CRM notes.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill research-account --skill prepare-discovery --skill analyze-sales-call --skill qualify-opportunity --skill plan-deal --skill prepare-demo --skill handle-objections --skill build-business-case --skill prepare-negotiation --skill create-mutual-action-plan
```

If your team already keeps a shared `.agents/gtm-context.md`, every skill below reads it automatically.

## Before the first meeting

```text
Use $research-account to build a brief on [account] ahead of Tuesday's discovery call. Cite sources with access dates. Flag anything inferred.
```

Then:

```text
Use $prepare-discovery for a 45-minute call with a [title] at [account]. Build hypotheses from the brief, questions that test them, and what a disqualifying answer sounds like.
```

## After every call

```text
Use $analyze-sales-call on this transcript. Separate customer evidence from my claims, list decisions and objections, then use $qualify-opportunity to update qualification and name the biggest unknown.
```

The output distinguishes what the buyer said from what you heard — the difference that decides Q4.

## When the deal gets real

[`plan-deal`](../../skills/plan-deal/) maps stakeholders, risks, and strategy in one artifact:

```text
Use $plan-deal for [opportunity]. Map the buying group, what each person verifiably cares about, competitive risk, and the three actions that most reduce uncertainty this week.
```

For the demo, [`prepare-demo`](../../skills/prepare-demo/) builds around their outcomes, not your feature tour. For pushback, [`handle-objections`](../../skills/handle-objections/) diagnoses whether an objection is price, priority, trust, or a polite no — and prepares honest responses, not manipulation scripts.

## Building the buyer's case

```text
Use $build-business-case for [account]. Use only cost and outcome inputs the buyer gave us or we can source. Show scenarios and break-even. Do not invent ROI numbers.
```

A business case the buyer's CFO can audit beats one that looks impressive until someone checks the math. That is what [`build-business-case`](../../skills/build-business-case/) produces.

## Closing without praying

[`create-mutual-action-plan`](../../skills/create-mutual-action-plan/) keeps proposed dates separate from buyer-accepted dates — so your close date rests on commitments, not hope. [`prepare-negotiation`](../../skills/prepare-negotiation/) plans trades within your actual approval boundaries before procurement tests them.

```text
Use $create-mutual-action-plan for [opportunity] closing [date]. Mark every step Proposed until the buyer accepts it. Then use $prepare-negotiation to plan packages and trades within my approved discount authority.
```

## The weekly habit

One loop, every week, per active deal: call → `$analyze-sales-call` → `$qualify-opportunity` → update `$plan-deal`. Fifteen minutes per deal, and your pipeline review defends itself.
