# Product Marketing Playbook

For product marketers turning customer, deal, and product evidence into an ICP, positioning, message tests, and value enablement. This playbook keeps internal learning, approved proof, and external claims separate so a compelling narrative does not outrun what customers and source material support.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context --skill review-customer-outcomes --skill analyze-win-loss --skill define-icp --skill develop-positioning --skill build-business-case
```

Use only material approved for the intended audience. Remove credentials, unnecessary personal data, confidential account details, and customer content you are not authorized to analyze. Confirm data access, aggregation, customer permission, quotation rights, and retention requirements before reusing customer or buyer evidence.

## Day 1 - Establish the claim boundary

Start with the product, audience, buying decision, alternatives, approved proof, and claims that need review:

```text
Use $gtm-context to update our shared GTM context from approved product documentation, current messaging, customer evidence, and competitive material. Separate Verified facts, Inferred interpretations, Hypotheses, and Unknowns. Identify claims that require product, customer, brand, legal, privacy, security, commercial, or regional review.
```

Do not convert roadmap intent, sales repetition, or internal aspiration into product availability, customer value, market consensus, or competitive proof. Suggested owners, review dates, and approvals remain **Proposed** or **Unknown** until an authoritative source confirms them.

## Day 2 - Learn from customer outcomes without manufacturing proof

Use [`review-customer-outcomes`](../../skills/review-customer-outcomes/) across approved account material to distinguish activity, adoption, workflow change, business outcomes, and realized value:

```text
Use $review-customer-outcomes on this approved, minimized customer evidence. Report the source, period, baseline, observed result, attribution limit, customer-validation status, contradictions, and missing evidence for each proposed outcome. Do not infer value from usage alone.
```

**Customer evidence is not publication permission.** An internally supported outcome, customer statement, or account artifact does not authorize a named case study, quote, logo, benchmark, or external claim. Keep confidential findings aggregated where possible and route every intended public use through the accountable customer, legal, privacy, brand, and product reviewers.

## Day 3 - Turn win/loss learning into bounded hypotheses

```text
Use $analyze-win-loss for [period and segment]. Audit outcomes, duplicates, source coverage, interview response, and missing records before finding patterns. Keep buyer evidence, seller interpretation, CRM reason codes, product evidence, and commercial records distinct. Report counts, sample size, missingness, counterexamples, and alternative explanations beside every pattern.
```

Small or biased samples produce a learning agenda, not a market conclusion. Treat association as association, preserve no-decisions and disqualifications, and label each recommended product, positioning, process, or enablement change as a **Hypothesis** with a falsifiable test.

## Day 4 - Refine the ICP without inventing precision

Feed the outcome and decision evidence into [`define-icp`](../../skills/define-icp/):

```text
Use $define-icp to refine [segment] from the approved customer-outcome and win/loss evidence. Separate company fit from persona, intent, and timing. Include disqualifiers, counterexamples, scoreability, evidence limits, and the smallest segment test that could disconfirm the profile.
```

Do not add numeric weights, tiers, market sizes, or conversion assumptions unless applicable outcome history and an authorized GTM owner support them. `Not scoreable` is better than false precision.

## Day 5 - Build positioning that carries its evidence

```text
Use $develop-positioning for the approved ICP and [buying situation]. Build a claim ledger, alternative map, positioning statement, message pillars, proof status, limitations, likely objections, and one bounded message test. Keep product capability, operational change, customer outcome, and public proof distinct.
```

The review matrix must account for product, customer proof, brand, legal, privacy, security, commercial, and regional review as `Required`, `Not applicable`, or `Unknown`. A missing reviewer is not approval, and a click, preference, or response-rate result is a test signal rather than proof that the message is true.

## Before value enablement - make the economics inspectable

When sales or marketing needs a value narrative, use buyer-provided, finance-reviewed, or explicitly illustrative inputs:

```text
Use $build-business-case to create a buyer-inspectable value model for [decision]. Show every baseline, formula, source, cost, realization dependency, scenario, break-even question, exclusion, and approval status. Leave unsupported inputs Unknown and label illustrative values clearly.
```

Do not turn time saved into cash, pipeline into revenue, or a theoretical ceiling into an expected outcome. Keep `Draft`, `Illustrative`, `Customer validated`, `Finance reviewed`, and `Approved` distinct, and route external financial claims to authorized customer, finance, commercial, delivery, legal, tax, and accounting reviewers.

## The operating cadence

- **Monthly:** refresh approved customer-outcome evidence and material contradictions.
- **Quarterly:** run win/loss analysis with explicit population, sample size, source coverage, and counterexamples.
- **When the market hypothesis changes:** re-test ICP boundaries before creating more message variants.
- **Before campaigns or enablement updates:** rebuild the claim ledger and human-review matrix.
- **Before external value claims:** validate inputs, permission, attribution, limitations, and approval status.

Use the [evidence and status contract](../evidence-contract.md) when moving claims between customer reviews, win/loss analysis, ICP, positioning, and business cases. The handoff should preserve source, audience, status, limitation, and approval instead of letting polished copy silently upgrade a hypothesis into fact.
