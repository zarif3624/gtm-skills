# GTM Skills for AI Agents

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
| Targeting | [`research-account`](skills/research-account/) | Build a sourced account brief without inventing facts |
| Targeting | [`plan-prospecting`](skills/plan-prospecting/) | Turn an ICP into a focused account and contact plan |
| Outreach | [`write-outbound`](skills/write-outbound/) | Write responsible, relevant multichannel outreach |
| Discovery | [`prepare-discovery`](skills/prepare-discovery/) | Prepare questions, hypotheses, and a call plan |
| Qualification | [`qualify-opportunity`](skills/qualify-opportunity/) | Assess evidence, gaps, and next validation steps |
| Deal execution | [`plan-deal`](skills/plan-deal/) | Map stakeholders, risks, strategy, and next actions |
| Deal execution | [`handle-objections`](skills/handle-objections/) | Diagnose objections and prepare honest responses |
| Deal execution | [`prepare-demo`](skills/prepare-demo/) | Design a buyer-specific demo around outcomes |
| Buying process | [`create-mutual-action-plan`](skills/create-mutual-action-plan/) | Build a shared, buyer-owned decision plan |
| Management | [`review-pipeline`](skills/review-pipeline/) | Find deal risk and prioritize actions across a pipeline |
| Management | [`forecast-sales`](skills/forecast-sales/) | Produce an auditable forecast with assumptions and scenarios |
| Post-sale | [`handoff-customer`](skills/handoff-customer/) | Transfer promises, goals, risks, and context to customer success |

## How The Skills Work Together

`gtm-context` creates `.agents/gtm-context.md`, the shared source of truth. Every other skill reads it when available and asks only for task-specific gaps.

```text
gtm-context
    |
    +-- define-icp -- research-account -- plan-prospecting -- write-outbound
    |
    +-- prepare-discovery -- qualify-opportunity -- plan-deal
    |                                         |-- handle-objections
    |                                         |-- prepare-demo
    |                                         `-- create-mutual-action-plan
    |
    +-- review-pipeline -- forecast-sales
    |
    `-- handoff-customer
```

## Install

Install every skill:

```bash
npx skills add zarif3624/gtm-skills
```

Install selected skills:

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context research-account prepare-discovery
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

## Trust Standard

Every contribution should preserve these rules:

1. Never invent account facts, contacts, intent signals, quotes, budgets, timelines, or customer proof.
2. Label claims as **Verified**, **Inferred**, or **Unknown** when the distinction matters.
3. Cite external research with a direct source and access date.
4. Treat CRM stage, probability, and seller confidence as inputs, not truth.
5. Never claim legal or regulatory compliance; surface applicable consent, privacy, and outreach requirements for human review.
6. Do not use sensitive personal data or manipulative tactics.
7. Preserve buyer agency. A good outcome can be a clear no.

## Contributing

Contributions are welcome, especially from working sellers, founders, RevOps operators, and customer success teams. See [CONTRIBUTING.md](CONTRIBUTING.md) for the quality bar and validation steps.

## Roadmap

- Sales call coaching and transcript analysis
- Territory planning and capacity modeling
- Account planning for enterprise deals
- Pricing and commercial negotiation
- Partner and channel sales
- Win/loss analysis
- CRM-specific reference packs and import/export helpers
- Evaluation fixtures that test skills against realistic sales scenarios

## License

[MIT](LICENSE). Use, adapt, and contribute back.

Built by [Zarif](https://github.com/zarif3624), creator of [Zarif Automates](https://zarif-automates-site.vercel.app).
