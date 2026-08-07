# Pipeline Review

## Data-quality warnings

- Duplicate opportunity IDs make deal counts, activity attribution, and record-level ranking unreliable until the records are reconciled.
- USD and EUR amounts cannot be combined into a supportable pipeline total without an approved conversion rule and rate date; report them separately for now.
- Missing next-step dates weaken evidence of current momentum.
- The deal whose close date precedes its required security milestone has an unsupported close date and should be validated.
- Reporting date, review period, record ownership, and export completeness are unknown.

## Executive summary

The **relative healthiest deal is the one with two emails and a buyer-approved validation milestone**. The approved milestone is meaningful buyer progress; the low email count is not a negative signal by itself.

The deal with **25 seller emails and no recorded buyer action is not healthy on activity volume alone**. Seller effort without buyer progress is a validation flag, not evidence of momentum. No deal should be declared fully healthy until duplicates are resolved and its next step, owner, and timing are confirmed.

## Deal priorities

| Opportunity | Classification | Evidence | Primary risk or gap | Action | Owner status | Date or dependency status |
| --- | --- | --- | --- | --- | --- | --- |
| Deal with buyer-approved validation milestone | Monitor provisionally | Buyer accepted a validation milestone; two emails are sufficient because volume is not the health criterion | Next-step date and other stage-exit evidence are not supplied | Confirm the milestone remains current, record the next buyer commitment, and verify the stated stage | Unknown | Next-step date unknown; proposed timing: before the next pipeline review |
| Deal with 25 seller emails and no buyer action | Validate | High seller activity, but no recorded buyer action | Apparent activity may mask stalled or one-sided engagement | Ask the buyer for a concrete commitment; if none is secured, reassess stage, close date, and whether to hold or recycle | Unknown | Proposed timing: before treating the deal as forecastable |
| Deal with close date before security milestone | Validate | Close date precedes a required buyer milestone | Current close date is not supportable | Confirm the security dependency and propose a close-date correction; do not silently overwrite the CRM | Unknown | Security milestone date and corrected close date unknown |

## Patterns

- **Stage integrity:** Buyer-approved validation supports progress; seller email volume does not satisfy a stage exit criterion.
- **Age and momentum:** Buyer action is the meaningful signal. Missing next-step dates prevent a reliable momentum assessment.
- **Qualification:** The security milestone contradiction is consequential and unresolved.
- **Concentration:** Cannot be assessed from the supplied context.
- **Flow and coverage:** Cannot be calculated reliably because the period is unspecified, opportunity IDs are duplicated, and currencies lack a conversion rule.

## Coaching questions

1. What did the buyer explicitly approve or commit to, and what buyer-owned action happens next?
2. For the 25-email deal, what evidence shows customer progress rather than seller persistence?
3. Can the security milestone be completed before close, or should the close date and forecast status change?

## CRM cleanup

| Record | Proposed change | Evidence | Approval requirement and status |
| --- | --- | --- | --- |
| Duplicate opportunity IDs | Reconcile duplicates while preserving raw records and activity history | Repeated IDs in the export | Data/CRM owner approval unknown |
| USD and EUR opportunities | Keep currency totals separate until an approved conversion rule and rate date are provided | Mixed currencies with no conversion rules | Finance/CRM decision unknown |
| Records missing next-step dates | Add confirmed next step, owner, and date where evidence exists; otherwise flag as unknown | Missing timing fields | Deal-owner confirmation unknown |
| Close-before-security record | Propose a corrected close date or milestone plan | Close date precedes required security milestone | Deal-owner and forecast-owner approval unknown |
