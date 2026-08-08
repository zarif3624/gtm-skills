# Founder Playbook

For founders doing founder-led sales: you have a product, some early conversations, and no sales infrastructure. This playbook takes you from scattered knowledge to a repeatable early motion in about a week of part-time work.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context --skill define-icp --skill research-account --skill prepare-discovery --skill analyze-sales-call --skill qualify-opportunity
```

## Day 1 — Capture what you already know

Point [`gtm-context`](../../skills/gtm-context/) at your real material:

```text
Create our GTM context from the product docs, pricing page, and customer notes in this repository. Label anything you infer rather than verify.
```

You get `.agents/gtm-context.md` — a shared background file every other skill reads. Ten minutes here saves you from re-explaining your product in every future session.

## Day 2 — Define who you are actually for

Founder ICPs drift toward "anyone who could buy." [`define-icp`](../../skills/define-icp/) is built to resist that:

```text
Use $define-icp to draft an initial ICP from our first 12 customer conversations and 3 paying customers. Name counterexamples and what evidence would falsify this profile.
```

Expect honest output: with three customers you get hypotheses to test, not scores. The skill refuses to invent weights your sample size cannot support — that restraint is the feature.

## Day 3 — Research before you reach out

Before your next call, run [`research-account`](../../skills/research-account/):

```text
Use $research-account to build a brief on [company] before Thursday's call. Cite every external claim with a source and access date. Mark what you could not verify.
```

No invented funding rounds, no hallucinated tech stacks, no fake "personalization." What is verified, inferred, and unknown stays labeled.

## Day 4 — Run discovery like you've done it 1,000 times

```text
Use $prepare-discovery to plan a 30-minute first call with [company]. I want hypotheses to test, not a script to read.
```

[`prepare-discovery`](../../skills/prepare-discovery/) produces questions tied to the problems you believe they have, plus what a disqualifying answer sounds like — because a fast no is a founder's second-best outcome.

## Day 5 — Mine the call, then decide

After the call, feed the transcript or your notes to [`analyze-sales-call`](../../skills/analyze-sales-call/) and [`qualify-opportunity`](../../skills/qualify-opportunity/):

```text
Use $analyze-sales-call on this transcript: separate what the customer actually said from what I hoped they said. Then use $qualify-opportunity to show what we verified, what we assumed, and the single next step that tests the biggest unknown.
```

This pair is the founder's antidote to happy ears.

## When you hire your first seller

Re-run `$gtm-context` to update the shared context, then hand your new rep the [account executive playbook](account-executive.md). Your ICP, positioning, and call evidence transfer with them — not just vibes.

## What to skip for now

Territories, partner channels, and forecasting need volume you do not have yet. The skills will tell you the same thing: their evidence gates fail loudly on thin data instead of producing confident fiction.
