# GTM Skills for AI Agents

[![Validate skills](https://github.com/zarif3624/gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/zarif3624/gtm-skills/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/zarif3624/gtm-skills)](https://skills.sh/zarif3624/gtm-skills)

Open-source sales and go-to-market skills for AI agents. Built for founders, sellers, RevOps teams, and customer-facing operators who want useful sales work without fabricated research, fake personalization, or mystery forecasts.

Works with OpenAI Codex, Claude Code, Cursor, Windsurf, and other agents that support the [Agent Skills specification](https://agentskills.io).

## Why This Exists

Sales is too large and too consequential to hide inside a general marketing prompt. A good GTM agent needs to understand the whole revenue path: who to target, why they might care, what evidence exists, how to run discovery, how to qualify a deal, and how to hand the customer over without losing context.

This project is deliberately:

- **Evidence-first**: facts, inferences, and unknowns stay separate.
- **Buyer-aware**: workflows optimize for a sound buying decision, not pressure.
- **Operational**: every skill produces artifacts a team can use in real work.
- **Composable**: a shared GTM context connects the skills without making them dependent on one agent or CRM.
- **Curated**: a focused collection with consistent quality beats hundreds of shallow prompts.

## Skills

| Stage | Skill | Use it for |
| --- | --- | --- |
| Foundation | [`gtm-context`](skills/gtm-context/) | Create the shared product, market, sales-motion, and evidence context |
| Strategy | [`define-icp`](skills/define-icp/) | Define, test, and score an ideal customer profile |
| Planning | [`plan-territories`](skills/plan-territories/) | Design fair, executable territories and capacity scenarios |
| Targeting | [`research-account`](skills/research-account/) | Build a sourced account brief without inventing facts |
| Account strategy | [`plan-account`](skills/plan-account/) | Connect footprint, relationships, whitespace, and investments |
| Targeting | [`plan-prospecting`](skills/plan-prospecting/) | Turn an ICP into a focused account and contact plan |
| Outreach | [`write-outbound`](skills/write-outbound/) | Write responsible, relevant multichannel outreach |
| Discovery | [`prepare-discovery`](skills/prepare-discovery/) | Prepare questions, hypotheses, and a call plan |
| Conversation | [`analyze-sales-call`](skills/analyze-sales-call/) | Extract evidence, decisions, next steps, and coaching from sales calls |
| Qualification | [`qualify-opportunity`](skills/qualify-opportunity/) | Assess evidence, gaps, and next validation steps |
| Deal execution | [`plan-deal`](skills/plan-deal/) | Map stakeholders, risks, strategy, and next actions |
| Deal execution | [`handle-objections`](skills/handle-objections/) | Diagnose objections and prepare honest responses |
| Deal execution | [`prepare-demo`](skills/prepare-demo/) | Design a buyer-specific demo around outcomes |
| Deal execution | [`prepare-negotiation`](skills/prepare-negotiation/) | Plan pricing and commercial negotiations within verified authority |
| Buying process | [`create-mutual-action-plan`](skills/create-mutual-action-plan/) | Build a shared, buyer-owned decision plan |
| Management | [`review-pipeline`](skills/review-pipeline/) | Find deal risk and prioritize actions across a pipeline |
| Management | [`forecast-sales`](skills/forecast-sales/) | Produce an auditable forecast with assumptions and scenarios |
| Post-sale | [`handoff-customer`](skills/handoff-customer/) | Transfer promises, goals, risks, and context to customer success |
| Learning | [`analyze-win-loss`](skills/analyze-win-loss/) | Find decision patterns across wins, losses, and no-decisions |
| Ecosystem | [`plan-partner-channel`](skills/plan-partner-channel/) | Design and test referral, reseller, services, and co-sell motions |

## How The Skills Work Together

`gtm-context` creates `.agents/gtm-context.md`, the shared source of truth. Every other skill reads it when available and asks only for task-specific gaps.

```text
gtm-context
    |
    +-- define-icp -- plan-territories
    |             `-- research-account -- plan-account
    |                                  `-- plan-prospecting -- write-outbound
    |
    +-- prepare-discovery -- analyze-sales-call -- qualify-opportunity -- plan-deal
    |                                                                |-- handle-objections
    |                                                                |-- prepare-demo
    |                                                                |-- prepare-negotiation
    |                                                                `-- create-mutual-action-plan
    |
    +-- review-pipeline -- forecast-sales
    |
    +-- handoff-customer
    |
    +-- analyze-win-loss
    |
    `-- plan-partner-channel
```

## Choose A Starting Point

| What you have | What you need | Start with |
| --- | --- | --- |
| Product docs and scattered sales knowledge | Shared, reusable background | `$gtm-context` |
| Early customer evidence or a broad target market | A testable customer profile | `$define-icp` |
| An account universe and coverage team | Territories, capacity, and assignment rules | `$plan-territories` |
| A named account or upcoming first meeting | Evidence and a conversation plan | `$research-account`, then `$prepare-discovery` |
| A strategic account with multiple teams or opportunities | A durable account-wide investment plan | `$plan-account` |
| A transcript or call notes | Decisions, qualification changes, and coaching | `$analyze-sales-call`, then `$qualify-opportunity` |
| A complex active opportunity | Risks, stakeholder strategy, and actions | `$plan-deal` |
| Pricing, procurement, or contract requests | Packages, trades, and approval boundaries | `$prepare-negotiation` |
| A CRM export or forecast call | Portfolio truth and revenue scenarios | `$review-pipeline`, then `$forecast-sales` |
| A signed order and scattered deal history | A complete post-sale transfer | `$handoff-customer` |
| Closed opportunities, decision notes, or buyer interviews | Repeatable win/loss learning | `$analyze-win-loss` |
| A partner idea, agreement, or reported channel pipeline | A testable, deduplicated partner motion | `$plan-partner-channel` |

Skills accept partial information. Give the agent the strongest source material you have and the decision or artifact you need; the skill should label important gaps and continue.

## Install

Preview the available skills:

```bash
npx skills add zarif3624/gtm-skills --list
```

Install every skill:

```bash
npx skills add zarif3624/gtm-skills
```

Install selected skills:

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context --skill research-account --skill prepare-discovery
```

Or clone and copy them into a project:

```bash
git clone https://github.com/zarif3624/gtm-skills.git
cp -R gtm-skills/skills/* .agents/skills/
```

## Try It

Once installed, ask naturally:

```text
Create our GTM context from the product docs in this repository.
Research Acme Corp for an enterprise discovery call. Cite every external claim.
Turn these call notes into a qualification assessment and next-step plan.
Review this CSV pipeline and show which deals need action this week.
Build a forecast with commit, best-case, and downside scenarios.
```

You can also invoke a skill directly, such as `$prepare-discovery` or `$review-pipeline`.

Start with the artifact you need; `.agents/gtm-context.md` is helpful, not required. When it is missing, each skill should use the evidence you provide, label consequential gaps, and continue. Create it with `$gtm-context` when you want consistent background across repeated workflows.

## Worked Example

Use the [RelayFox fictional workspace](examples/relayfox/) to try conversation analysis, qualification, pipeline review, forecasting, and win/loss learning with a coherent set of safe source files. The example deliberately contains ambiguity and dirty data so you can inspect whether evidence and unknowns survive each handoff.

## Trust Standard

Every contribution should preserve these rules:

1. Never invent account facts, contacts, intent signals, quotes, budgets, timelines, or customer proof.
2. Label claims as **Verified**, **Inferred**, or **Unknown** when the distinction matters.
3. Cite external research with a direct source and access date.
4. Treat CRM stage, probability, and seller confidence as inputs, not truth.
5. Never claim legal or regulatory compliance; surface applicable consent, privacy, and outreach requirements for human review.
6. Do not use sensitive personal data or manipulative tactics.
7. Preserve buyer agency. A good outcome can be a clear no.
8. Keep proposed owners, dates, approvals, and customer actions distinct from what is confirmed or accepted.

## Contributing

Contributions are welcome, especially from working sellers, founders, RevOps operators, and customer success teams. See [CONTRIBUTING.md](CONTRIBUTING.md) for the quality bar and validation steps.

## Roadmap

The near-term priority is to make quality measurable: realistic eval cases, consistent evidence contracts, stronger validation, and tested handoffs between skills. Then the collection will expand into call analysis, win/loss, territory planning, commercial negotiation, enterprise account planning, and partner sales.

See the [full product roadmap](ROADMAP.md) for priorities, measures, and deliberate non-goals.

## License

[MIT](LICENSE). Use, adapt, and contribute back.

Built by [Zarif](https://github.com/zarif3624), creator of [Zarif Automates](https://zarifautomates.com).
