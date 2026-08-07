---
name: review-pipeline
description: "Review a B2B sales pipeline from CRM exports, spreadsheets, deal notes, or summaries. Use for weekly pipeline reviews, manager inspection, stale-deal analysis, stage hygiene, coverage analysis, rep prioritization, or finding the few actions most likely to improve pipeline truth and execution."
---

# Review Pipeline

Turn pipeline data into a prioritized inspection and action list. Do not confuse CRM volume with revenue quality.

## Inputs

Read `.agents/gtm-context.md` for stages, exit criteria, cycle, segment, and forecast definitions. Confirm the reporting date, currency, period, ownership, and whether the data is complete.

Normalize fields before analysis. Preserve the raw values and report any transformations.

## Inspect

1. **Data quality:** missing values, duplicates, inconsistent stages, future or stale dates, and impossible amounts.
2. **Stage integrity:** whether available evidence supports the stated stage and exit criteria.
3. **Age and momentum:** time in stage, last meaningful buyer action, next step, owner, and date.
4. **Qualification:** consequential unknowns or contradictions.
5. **Concentration:** exposure by account, rep, segment, source, and close period.
6. **Flow:** new pipeline, stage movement, slips, losses, wins, and recycling.
7. **Coverage:** compare qualified pipeline with target using the team's historical conversion, not a universal multiplier.

Read [the review rules](references/review-rules.md) for consistent flags.

## Prioritize

Classify each deal:

- **Act now:** a specific action can change or clarify the outcome.
- **Validate:** important evidence is missing or contradictory.
- **Hold or recycle:** timing is real but not current.
- **Remove:** stage, amount, or close date is not supportable.
- **Monitor:** evidence and next steps are current.

## Output

Use [the pipeline review template](assets/pipeline-review.md). Provide:

- data-quality warnings;
- executive pipeline summary;
- prioritized deal table with evidence, risk, action, and confirmed or proposed owner and timing status;
- stage, age, and concentration patterns;
- pipeline created and moved during the period when data supports it;
- coaching questions, not scripted manager conclusions;
- CRM cleanup list separated from selling actions.

Do not silently overwrite CRM data. Propose corrections and show the evidence. Do not invent ownership or deadlines; prefer milestone-relative timing and label suggestions as `Proposed` or `Unknown`.
