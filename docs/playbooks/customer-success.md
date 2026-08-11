# Customer Success Playbook

For Customer Success managers taking an account from signed agreement through adoption, outcome review, renewal, and responsible expansion. This playbook keeps seller promises, product activity, customer evidence, and internal targets separate so the account plan reflects what the customer has actually accepted.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill gtm-context --skill handoff-customer --skill review-customer-outcomes --skill plan-account --skill build-business-case
```

If your team maintains `.agents/gtm-context.md`, the skills read it automatically. Use only approved account material and remove credentials, unnecessary personal data, and content the intended audience should not access.

## Day 1 - Accept the handoff without inheriting assumptions

Start with the signed agreement, approved sales notes, mutual action plan, and call evidence:

```text
Use $handoff-customer for [account]. Separate contractual commitments, seller-reported promises, customer-stated goals, open questions, risks, and next actions. Keep every owner, date, and approval Proposed or Unknown unless the source confirms it.
```

Review the artifact with the account executive and implementation owner. A seller-reported promise is not a customer-accepted success measure, and an internal close note is not a contractual commitment. Escalate contradictions to the authorized owner; do not silently resolve them.

## Week 1 - Confirm the customer's outcome baseline

Ask the customer to confirm the goals, measures, baseline, target, measurement source, decision owner, and review cadence that matter to them. Then use [`review-customer-outcomes`](../../skills/review-customer-outcomes/) to establish the first evidence review:

```text
Use $review-customer-outcomes for [account] with the accepted handoff, approved usage data, support history, and customer notes. Separate activity, adoption, customer outcomes, realized value, renewal readiness, and expansion hypotheses. Mark unconfirmed targets and measures Unknown.
```

**Activity is not an outcome.** Logins, enabled seats, meetings, and feature use can support an adoption assessment, but they do not prove time saved, risk reduced, revenue created, or customer value without a defined link and customer-validated evidence.

## Monthly - Review evidence, not account color

Re-run `$review-customer-outcomes` before the account review. Ask for:

- customer-stated progress and concerns with source locators;
- adoption evidence with scope and as-of date;
- outcome evidence with baseline, measure, and limitations;
- open product, support, security, and commercial dependencies;
- the smallest next check that would resolve each material Unknown.

Do not convert a health score, sentiment label, or executive attendance into renewal confidence. Keep contradicted evidence visible and route product, legal, security, finance, or commercial decisions to their authorized owners.

## Before renewal - Build a decision record

Use the latest outcome review to separate four questions: what value is supported, what remains unmeasured, what obligations remain open, and what the customer has said about the next term. Contract dates and renewal mechanics must come from an approved source.

```text
Use $review-customer-outcomes to prepare a renewal evidence review for [account]. Distinguish verified value, unresolved risks, contractual facts, customer-stated intent, and internal assumptions. Do not infer renewal from activity or relationship strength.
```

A renewal recommendation remains **Proposed** until the authorized customer and internal owners confirm the relevant decision, terms, and dates.

## When expansion is plausible - Test it with the customer

Use [`plan-account`](../../skills/plan-account/) to map the current footprint, relationships, unresolved outcomes, and evidence-backed whitespace. An internal expansion target is not customer demand.

```text
Use $plan-account for [account] from the accepted handoff and current outcome review. Separate verified footprint from whitespace hypotheses. Recommend only the next discovery or validation actions that improve the customer's decision.
```

When the customer validates a new problem and wants to evaluate change, use [`build-business-case`](../../skills/build-business-case/) with buyer-provided or sourced inputs:

```text
Use $build-business-case for the customer-validated [initiative]. Show baseline, scenarios, break-even, evidence sources, and every assumption. Leave unsupported values Unknown rather than inventing ROI.
```

Expansion is ready for a commercial process only when the problem, affected stakeholders, decision path, and value inputs have evidence. A clear no or a decision to revisit later is a valid outcome.

## The operating cadence

- **At handoff:** reconcile commitments, goals, risks, and status labels with accountable owners.
- **Monthly:** review adoption and outcome evidence, then assign the smallest next validation actions.
- **Before renewal:** produce an inspectable decision record rather than a color or confidence score.
- **Before expansion:** validate the customer's problem before building a plan or business case.

Use the [evidence and status contract](../evidence-contract.md) when moving claims or actions between tools. If the account needs a portable record, the [evidence and action ledger pack](../../reference-packs/evidence-ledger/) preserves source, status, owner, and review state without turning proposals into facts.
