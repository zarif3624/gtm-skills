# SDR Playbook

For SDRs and BDRs building pipeline: your job is relevance at volume without becoming the spam everyone screenshots. These skills refuse to fabricate personalization — which is exactly why the outreach they produce gets replies.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill plan-prospecting --skill research-account --skill write-outbound --skill prepare-discovery
```

## Step 1 — Turn the ICP into a working list plan

If your team has an ICP (or you built one with [`define-icp`](../../skills/define-icp/)):

```text
Use $plan-prospecting to turn our ICP into an account and contact plan for this quarter. Prioritize by observable trigger events, not gut feel. Show what signals to watch per tier.
```

[`plan-prospecting`](../../skills/plan-prospecting/) outputs tiers with entry rules you can defend in pipeline council, not a wish list.

## Step 2 — Research the accounts that matter

For tier-one accounts, one brief each:

```text
Use $research-account on [account]. I need verifiable facts I can reference in outreach: initiatives, hiring patterns, public statements, stack signals. Cite each with a source and access date. Skip anything you cannot verify.
```

The skill will not invent a "recent funding round" that never happened. An email built on a wrong fact burns the account; an email built on a verified one starts a conversation.

## Step 3 — Write outbound that survives scrutiny

```text
Use $write-outbound for [contact] at [account] using the research brief. Three-touch sequence: email, LinkedIn, call opener. Every personalized line must trace to a cited fact. If we have no real reason to reach out, say so instead of faking one.
```

[`write-outbound`](../../skills/write-outbound/) is deliberately opinionated: relevance over volume, permission over pressure, and no fake "I noticed you..." lines. It also surfaces consent and outreach-regulation considerations for human review instead of pretending they do not exist.

## Step 4 — Hand off meetings that stick

When a meeting books, run [`prepare-discovery`](../../skills/prepare-discovery/) and pass the artifact to your AE — hypotheses, cited facts, and suggested questions in one file. Meetings with an evidence trail keep their show rate and survive the handoff.

```text
Use $prepare-discovery to build a handoff brief for the meeting with [contact] on [date], from the research brief and my outreach thread.
```

## The habit that compounds

Log which cited facts and triggers got replies, then feed that back:

```text
Here are the last 20 outreach attempts with reply outcomes. Which trigger events and evidence types correlated with replies? What should next week's list prioritize? Label small-sample caution where it applies.
```

Small honest samples beat big fabricated benchmarks — and after a quarter you have your own playbook, not a template someone sold you.
