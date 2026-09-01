# Partner and Channel Leader Playbook

For partner and channel leaders designing referral, reseller, services, marketplace, or co-sell motions that create customer value and withstand pipeline inspection. This playbook connects partner strategy to activation evidence, canonical opportunity records, and an auditable forecast without manufacturing partner fit or mutual commitment.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context --skill define-icp --skill plan-partner-channel --skill research-account --skill review-pipeline --skill forecast-sales
```

Use only approved partner, customer, opportunity, and commercial material. Remove credentials and unnecessary personal or confidential data. Confirm access, purpose, retention, customer consent, and contractual data-sharing rights before moving information between your company, a partner, and a customer.

## Day 1 - Establish the customer and authority boundary

Start with the customer outcome, ICP, route-to-market hypothesis, current evidence, and decisions that require approval:

```text
Use $gtm-context to update our shared GTM context from approved product, customer, route-to-market, partner, and commercial material. Separate Verified facts, Inferred interpretations, Hypotheses, Proposed decisions, and Unknowns. Identify partner claims and decisions that require customer, product, channel, sales, finance, legal, privacy, security, data, brand, competition, delivery, or executive review.
```

Do not turn an exploratory conversation, mutual interest, draft agreement, or internal target into partner commitment. Proposed economics, owners, territories, exclusivity, dates, customer access, and obligations remain **Proposed** or **Unknown** until an authorized source confirms them.

## Day 2 - Define the customer problem before the partner list

Use [`define-icp`](../../skills/define-icp/) to identify where a partner could improve a real buying or delivery outcome:

```text
Use $define-icp to define the customer segment and buying situation for this partner-motion hypothesis. Separate firmographic fit from buyer role, trigger, timing, and channel preference. Include disqualifiers, counterexamples, evidence limits, and the smallest test that could disconfirm the segment.
```

Then use [`plan-partner-channel`](../../skills/plan-partner-channel/) to make the partner thesis falsifiable:

```text
Use $plan-partner-channel to compare direct, referral, reseller, services, marketplace, and co-sell routes for this customer problem. Define the proposed partner profile, customer value, mutual value, contribution roles, activation evidence, pilot, stop criteria, governance, and approval boundaries. Leave unsupported capabilities, economics, commitments, and market access Unknown.
```

Preserve buyer choice. Do not force a partner route when a direct or different route better serves the customer's decision, implementation, support, or commercial needs.

## Day 3 - Research candidates without manufacturing fit

For each candidate organization, use [`research-account`](../../skills/research-account/) with first-party sources where possible:

```text
Use $research-account to assess [candidate partner] against the approved partner profile. Cite every external fact with a direct source and access date. Separate Verified facts, Inferred fit, and Unknowns. Do not infer capability, customer access, geographic coverage, certification, capacity, intent, or commitment from generic marketing language.
```

Research can establish a candidate hypothesis; it cannot establish mutual interest, agreed scope, customer access, or an activated relationship. Record the evidence against explicit selection criteria and carry contradictions forward.

## Day 4 - Run a finite activation pilot

Return to `$plan-partner-channel` to define a bounded pilot with named owners, enablement, customer safeguards, observable activation evidence, and stop criteria.

**A signed partner is not an activated partner.** Keep `Target`, `Recruit`, `Contracted`, `Enabled`, `Activated`, `Productive`, and `Inactive` distinct. Training attendance, portal login, a shared account list, or a registered lead may be useful activity, but it is not customer progress or revenue evidence by itself.

Before launch, require authorized review for agreements, economics, incentives, territories, exclusivity, brand use, competitive constraints, customer communications, data access, security, privacy, service delivery, and external commitments. A missing reviewer is not approval.

## Day 5 - Inspect partner pipeline before forecasting

Use [`review-pipeline`](../../skills/review-pipeline/) to normalize records and challenge evidence:

```text
Use $review-pipeline on this approved direct and partner opportunity export. Preserve source values, contradictions, duplicate candidates, currency and as-of dates, buyer evidence, and approval status. Use one canonical opportunity ID per buying decision. Keep sourced, influenced, delivered, and transacted partner contribution roles separate from canonical amount, opportunity ownership, stage, and forecast category.
```

Partner-reported pipeline is not forecast. A registration, referral, introduction, seller assertion, or partner estimate does not become qualified pipeline without buyer and opportunity evidence. Resolve duplicate candidates through an authorized owner; do not silently merge or assign credit. This prevents double counting while preserving legitimate partner contribution.

## Forecast without upgrading the evidence

After pipeline review, use [`forecast-sales`](../../skills/forecast-sales/) on the canonical opportunity set:

```text
Use $forecast-sales on the reviewed opportunity set as of [date]. Produce commit, best-case, and downside scenarios with assumptions, exclusions, contradictions, partner contribution roles, and sensitivity. Do not add partner-reported amounts separately or upgrade stage, probability, timing, buyer intent, or forecast category without supporting evidence.
```

Report partner-sourced and partner-influenced views as attribution cuts of canonical opportunities, not additive revenue pools. Keep expected economics, commissions, rebates, and delivery costs separate from forecast amount unless the approved model explicitly calls for them.

## Customer data and consequential actions

Customer consent is necessary but not sufficient for customer-data sharing. Confirm the permitted purpose, minimum fields, recipients, retention, deletion, security controls, and contractual authority with accountable legal, privacy, security, data, customer, and commercial reviewers. Do not expose customer lists, opportunity details, buyer communications, or personal data merely because a partner agreement exists.

The agent may draft research, scorecards, pilot plans, review artifacts, and recommendations. Humans with verified authority must approve partner outreach, agreements, incentives, deal registration, account sharing, customer communications, data transfer, attribution changes, forecast changes, and external commitments.

## The operating cadence

- **Weekly:** review pilot activity, activation evidence, customer impact, opportunity contradictions, and actions awaiting approval.
- **Monthly:** inspect the canonical partner pipeline before forecast and reconcile attribution without changing source records.
- **Quarterly:** compare partner cohorts on activation, customer outcomes, cycle time, win rate, delivery quality, cost, and retention using documented denominators and caveats.
- **At each stage change:** record the evidence, source, as-of date, owner, and approval that supports it.
- **At pilot end:** scale, revise, pause, or stop against the pre-agreed criteria rather than sunk effort or relationship pressure.

Use the [evidence and status contract](../evidence-contract.md) when moving claims between partner strategy, candidate research, activation, pipeline, and forecast. The handoff should preserve source, status, limitation, contribution role, canonical opportunity identity, customer permission, and approval instead of letting a partner label upgrade weak evidence into revenue.
