# GTM Skills for AI Agents

[![Validate skills](https://github.com/zarif3624/gtm-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/zarif3624/gtm-skills/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/zarif3624/gtm-skills)](https://skills.sh/zarif3624/gtm-skills)

Open-source sales and go-to-market skills for AI agents. Built for founders, sellers, RevOps teams, and customer-facing operators who want useful sales work without fabricated research, fake personalization, or mystery forecasts.

Uses the open [Agent Skills specification](https://agentskills.io). It is designed for skills-compatible clients, but installation and behavior can vary by client and model. See the [compatibility evidence matrix](docs/compatibility.md) for what is verified, limited, or still unknown.

Machines and catalog UIs can read [`catalog.json`](catalog.json) for normalized skill metadata, resource paths, and deterministic SHA-256 package digests. The validation suite fails if it drifts from the skill packages.

New here? Follow the [ten-minute quickstart](QUICKSTART.md).

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
| Operations | [`design-sales-process`](skills/design-sales-process/) | Design buyer-state stages, evidence gates, governance, and measurement |
| Strategy | [`define-icp`](skills/define-icp/) | Define, test, and score an ideal customer profile |
| Planning | [`plan-territories`](skills/plan-territories/) | Design fair, executable territories and capacity scenarios |
| Targeting | [`research-account`](skills/research-account/) | Build a sourced account brief without inventing facts |
| Account strategy | [`plan-account`](skills/plan-account/) | Connect footprint, relationships, whitespace, and investments |
| Targeting | [`plan-prospecting`](skills/plan-prospecting/) | Turn an ICP into a focused account and contact plan |
| Outreach | [`write-outbound`](skills/write-outbound/) | Write responsible, relevant multichannel outreach |
| Discovery | [`prepare-discovery`](skills/prepare-discovery/) | Prepare questions, hypotheses, and a call plan |
| Conversation | [`analyze-sales-call`](skills/analyze-sales-call/) | Extract evidence, decisions, next steps, and coaching from sales calls |
| Enablement | [`coach-sales-rep`](skills/coach-sales-rep/) | Build focused coaching experiments from observable behavior |
| Qualification | [`qualify-opportunity`](skills/qualify-opportunity/) | Assess evidence, gaps, and next validation steps |
| Deal execution | [`plan-deal`](skills/plan-deal/) | Map stakeholders, risks, strategy, and next actions |
| Deal execution | [`handle-objections`](skills/handle-objections/) | Diagnose objections and prepare honest responses |
| Deal execution | [`prepare-demo`](skills/prepare-demo/) | Design a buyer-specific demo around outcomes |
| Value engineering | [`build-business-case`](skills/build-business-case/) | Build inspectable value, cost, scenario, and break-even models |
| Deal execution | [`prepare-negotiation`](skills/prepare-negotiation/) | Plan pricing and commercial negotiations within verified authority |
| Buying process | [`create-mutual-action-plan`](skills/create-mutual-action-plan/) | Build a shared, buyer-owned decision plan |
| Management | [`review-pipeline`](skills/review-pipeline/) | Find deal risk and prioritize actions across a pipeline |
| Management | [`forecast-sales`](skills/forecast-sales/) | Produce an auditable forecast with assumptions and scenarios |
| Post-sale | [`handoff-customer`](skills/handoff-customer/) | Transfer promises, goals, risks, and context to customer success |
| Post-sale | [`review-customer-outcomes`](skills/review-customer-outcomes/) | Review value evidence, renewal readiness, and expansion hypotheses |
| Learning | [`analyze-win-loss`](skills/analyze-win-loss/) | Find decision patterns across wins, losses, and no-decisions |
| Ecosystem | [`plan-partner-channel`](skills/plan-partner-channel/) | Design and test referral, reseller, services, and co-sell motions |

## How The Skills Work Together

`gtm-context` creates `.agents/gtm-context.md`, the shared source of truth. Every other skill reads it when available and asks only for task-specific gaps.

```text
gtm-context
    |
    +-- design-sales-process -- review-pipeline -- forecast-sales
    |
    +-- define-icp -- plan-territories
    |             `-- research-account -- plan-account
    |                                  `-- plan-prospecting -- write-outbound
    |
    +-- prepare-discovery -- analyze-sales-call -- qualify-opportunity -- plan-deal
    |                              |
    |                              `-- coach-sales-rep
    |                                                                |-- handle-objections
    |                                                                |-- prepare-demo -- build-business-case
    |                                                                |-- prepare-negotiation
    |                                                                `-- create-mutual-action-plan
    |
    +-- review-pipeline -- forecast-sales
    |
    +-- handoff-customer -- review-customer-outcomes
    |
    +-- analyze-win-loss
    |
    `-- plan-partner-channel
```

## Choose A Starting Point

| What you have | What you need | Start with |
| --- | --- | --- |
| Product docs and scattered sales knowledge | Shared, reusable background | `$gtm-context` |
| Inconsistent stages, fields, or handoffs | A buyer-state sales process and rollout plan | `$design-sales-process` |
| Early customer evidence or a broad target market | A testable customer profile | `$define-icp` |
| An account universe and coverage team | Territories, capacity, and assignment rules | `$plan-territories` |
| A named account or upcoming first meeting | Evidence and a conversation plan | `$research-account`, then `$prepare-discovery` |
| A strategic account with multiple teams or opportunities | A durable account-wide investment plan | `$plan-account` |
| A transcript or call notes | Decisions, qualification changes, and coaching | `$analyze-sales-call`, then `$qualify-opportunity` |
| Multiple calls, observations, and outcomes for one rep | A narrow developmental experiment | `$coach-sales-rep` |
| A complex active opportunity | Risks, stakeholder strategy, and actions | `$plan-deal` |
| Outcome evidence, cost inputs, and an investment decision | An inspectable value model or budget case | `$build-business-case` |
| Pricing, procurement, or contract requests | Packages, trades, and approval boundaries | `$prepare-negotiation` |
| A CRM export or forecast call | Portfolio truth and revenue scenarios | `$review-pipeline`, then `$forecast-sales` |
| A signed order and scattered deal history | A complete post-sale transfer | `$handoff-customer` |
| Usage, success, support, stakeholder, and contract evidence | An outcome, renewal, and expansion-readiness review | `$review-customer-outcomes` |
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
Build an inspectable buyer business case without inventing ROI inputs.
```

You can also invoke a skill directly, such as `$prepare-discovery` or `$review-pipeline`.

Start with the artifact you need; `.agents/gtm-context.md` is helpful, not required. When it is missing, each skill should use the evidence you provide, label consequential gaps, and continue. Create it with `$gtm-context` when you want consistent background across repeated workflows.

## Worked Example

Use the [RelayFox fictional workspace](examples/relayfox/) to try conversation analysis, qualification, pipeline review, forecasting, and win/loss learning with a coherent set of safe source files. The example deliberately contains ambiguity and dirty data so you can inspect whether evidence and unknowns survive each handoff.

## Bring Your Own CRM Export

Use the [generic CRM handoff pack](reference-packs/generic-crm/) to map pipeline data without silently changing source records. It includes CSV templates, lineage and status fields, a dated currency-policy template, and a matching JSON Schema for structured integrations. No CRM vendor is required.

## Preserve Evidence Across Tools

Use the [evidence and action ledger pack](reference-packs/evidence-ledger/) when claims, actions, approvals, or commitments need to move between agents, spreadsheets, CRMs, and internal tools. Its matching CSV and JSON contracts keep evidence, source lineage, transformations, buyer acceptance, approval, and completion on separate axes.

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

The [evidence and status contract](docs/evidence-contract.md) defines the vocabulary and the handoff invariants behind these rules.

Current catalog and evaluation counts are published in [`quality-summary.json`](quality-summary.json). The validation suite fails when that snapshot no longer matches the repository, preventing release notes from quietly outliving the evidence.

## Contributing

Contributions are welcome, especially from working sellers, founders, RevOps operators, and customer success teams. See [CONTRIBUTING.md](CONTRIBUTING.md) for the quality bar and validation steps.

For security concerns and the project threat model, see [SECURITY.md](SECURITY.md).

Run the full dependency-free quality suite with:

```bash
python3 scripts/check.py
```

After changing a skill, eval definition, result, example, or reference pack, refresh committed metadata with `python3 scripts/update_generated.py` before running the suite.

The suite checks all 24 skill packages, their metadata and bundled resources, one adversarial case per skill, cross-skill journey cases, finalized behavioral and blind-routing reports, the fictional example data, and operational reference packs. See the [evaluation guide](evals/README.md) for clean-context forward testing and evidence scoring.

## Roadmap

The quality foundation and first workflow expansion are in place. The next priority is to publish reproducible compatibility results across agents, add opt-in CRM handoff packs, and measure whether a new user can reach a useful first artifact in under ten minutes.

See the [full product roadmap](ROADMAP.md) for priorities, measures, and deliberate non-goals.

Release history and the evidence-gated publication checklist are in [CHANGELOG.md](CHANGELOG.md) and [RELEASING.md](RELEASING.md).

## License

[MIT](LICENSE). Use, adapt, and contribute back.

Built by [Zarif](https://github.com/zarif3624), creator of [Zarif Automates](https://zarifautomates.com).
