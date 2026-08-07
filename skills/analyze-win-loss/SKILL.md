---
name: analyze-win-loss
description: "Analyze individual or aggregate B2B wins, losses, no-decisions, and disqualifications using CRM records, buyer interviews, call notes, proposals, and deal history. Use for win/loss reviews, loss-reason audits, segment comparisons, product and messaging feedback, sales-process learning, or deciding which GTM hypotheses to test without turning seller opinion into buyer truth."
---

# Analyze Win Loss

Explain what the evidence supports about buying decisions and what the team should test next. Do not reduce a complex decision to one convenient reason code.

## Inputs And Scope

Read `.agents/gtm-context.md` when available. Confirm:

- decision period, segment, product, geography, and opportunity population;
- outcome definitions for won, lost, no decision, disqualified, and unknown;
- source types, response rates, missing records, and who supplied each explanation;
- whether the task is a single-deal review, a cohort comparison, or a portfolio analysis.

Preserve a stable opportunity identifier while removing unnecessary personal data. Do not merge similarly named accounts or double-count reopened opportunities.

Read [the analysis methods](references/methods.md) for coding evidence, comparing cohorts, interviewing buyers, and handling small samples.

## Workflow

1. Audit outcome labels, duplicates, missing fields, reopened deals, and inconsistent dates before analysis.
2. Build a source map for each decision. Keep buyer evidence, seller interpretation, CRM fields, and product or commercial records distinct.
3. Reconstruct the buyer's decision: desired change, alternatives, criteria, process, stakeholders, decisive events, and final outcome.
4. Code contributing factors consistently across wins, losses, and no-decisions. Allow multiple factors per outcome.
5. Label each finding as `Verified`, `Inferred`, `Unknown`, or `Contradicted`, with a source and date.
6. Compare relevant cohorts only when definitions and sample sizes support the comparison. Report counts and missingness beside percentages.
7. Separate association from causation. Use `contributed to`, `was reported as`, or `co-occurred with` unless the evidence supports a stronger claim.
8. Identify patterns, counterexamples, and alternative explanations.
9. Convert findings into a small number of product, positioning, process, or enablement hypotheses with falsifiable tests. Use proposed owners and review dates unless the source confirms them.
10. Rank new evidence to collect, including which buyer interviews would most reduce uncertainty.

## Guardrails

- Never treat a CRM loss reason, seller summary, competitor mention, or buyer courtesy response as complete buyer truth.
- Do not blame individual buyers or sellers, grade personality, or infer sensitive traits.
- Do not claim price caused a loss merely because `Price` was selected; identify the value, packaging, authority, comparison, or process evidence behind it.
- Do not present tiny or biased samples as representative. Name interview nonresponse and survivorship bias.
- Do not invent interview participation, opportunity attributes, owners, deadlines, approvals, or completed analysis steps. Mark suggested owners and dates as `Proposed`; otherwise use `Unknown`.
- Do not publish buyer quotes, account identities, or confidential commercial details beyond their approved audience.
- Do not recommend a roadmap promise, discount, or process change without an authorized owner reviewing the evidence and tradeoffs.

## Output

Use [the win/loss template](assets/win-loss-analysis.md). Provide:

- scope, population, source coverage, and data-quality limits;
- outcome distribution using explicit definitions;
- evidence-backed decision-factor patterns with counts and counterexamples;
- cohort comparisons only where supportable;
- buyer, seller, product, and process perspectives kept distinct;
- unknowns, alternative explanations, and confidence;
- prioritized hypotheses and tests with confirmed or explicitly proposed owners and review dates;
- recommended interview sample and human-review boundaries.

When the evidence is too weak for a pattern, return an evidence-collection plan instead of a confident story.
