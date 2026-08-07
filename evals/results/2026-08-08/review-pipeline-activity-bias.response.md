# Pipeline Review: Provided Fictional Export

**As of:** Unknown
**Period and currency:** Period unknown; mixed USD and EUR, with no conversion rules
**Records reviewed:** Exact count unknown because duplicate opportunity IDs have not been reconciled

## Data Quality

| Issue | Records affected | Impact | Proposed correction | Owner status |
| --- | ---: | --- | --- | --- |
| Duplicate opportunity IDs | Unknown | May double-count pipeline and activity and makes deal-level attribution unreliable | Reconcile duplicates against the CRM source of truth before counting records or aggregating amounts | Unknown |
| Mixed USD and EUR without conversion rules | Unknown | Total pipeline, concentration, and coverage cannot be stated reliably | Keep currencies separate until a reporting currency, rate source, and effective date are confirmed | Unknown |
| Missing next-step dates | Unknown | Momentum and execution timing cannot be verified | Add a buyer-relevant next step and date where confirmed; otherwise leave status unknown | Unknown |
| Close date before required security milestone | At least 1 | The close date is not supportable because a required buyer milestone occurs later | Validate the milestone sequence and propose a corrected close date; do not overwrite it without approval | Unknown |
| Reporting date, period, ownership, completeness, and team stage definitions unavailable | All | Limits stage, age, flow, coverage, and owner analysis | Confirm these inputs before using the review for forecasting | Unknown |

## Executive Summary

- **Supportable pipeline:** Cannot be totaled because IDs are duplicated and currencies cannot be combined. The deal with a buyer-approved validation milestone is the healthiest identifiable deal because it contains explicit buyer progress.
- **Material movement:** A buyer-approved validation milestone is the strongest evidence of forward movement in the supplied context. Two emails do not weaken that evidence.
- **Concentration or coverage risk:** Not assessable from the supplied fields.
- **Most important action this period:** Validate the next buyer commitment and timing for the milestone-backed deal, while separately testing whether the high-email deal has any real buyer action.
- **Data limitations:** No complete deal-level export, reporting date, period, owners, currency conversion policy, stage history, or historical conversion data was provided.

## Deal Priorities

| Opportunity | Classification | Evidence | Primary risk or gap | Action | Owner status | Date or dependency status |
| --- | --- | --- | --- | --- | --- | --- |
| Deal with two emails and a buyer-approved validation milestone | Validate (healthiest relative signal) | Buyer-approved validation is direct evidence of buyer commitment and completed progress; low email volume is not a negative signal by itself | Next-step date and the milestone's relationship to stage exit and close timing are not provided | Confirm the next buyer-owned step, required evidence, and milestone-relative timing | Unknown | Proposed: tie follow-up to completion or acceptance of the validation milestone; calendar date unknown |
| Deal with 25 seller emails and no recorded buyer action | Validate | High seller activity, but no accepted buyer action, stakeholder progress, completed validation, or resolved decision is recorded | Activity volume may be masking stalled or one-sided engagement | Ask for evidence of a buyer commitment; if none exists, correct the stage/close timing and consider hold or recycle | Unknown | Unknown; next-step date is missing |
| Deal whose close date precedes its security milestone | Act now | Required security work occurs after the stated close date | Forecast sequence is internally impossible unless the milestone is not actually required | Confirm whether security is a true prerequisite; if it is, propose moving the close date after milestone completion | Unknown | Dependency conflict confirmed; corrected date unknown |

## Patterns

- **Stage integrity:** The security-date contradiction makes the affected forecast position unsupported, and the high-email deal's stage requires validation because buyer progress is absent. The milestone-backed deal has the strongest stage evidence, subject to the team's unavailable exit criteria.
- **Age and momentum:** Email volume is not momentum. Buyer approval of a validation milestone is meaningful momentum; 25 seller emails without buyer action is not.
- **Qualification:** Confirm the security prerequisite, the buyer's acceptance criteria, and the next buyer-owned commitment. Missing dates remain consequential unknowns.
- **Concentration:** Not assessable without reliable unique records, normalized amounts, accounts, segments, or owners.
- **Flow and coverage:** Not assessable without reporting-period movement, target, and historical conversion data. Do not use a universal coverage multiplier.

## Coaching Questions

1. What did the buyer explicitly approve, complete, or commit to on each deal, and what evidence is recorded?
2. For the 25-email deal, what buyer action would justify retaining its current stage and close date?
3. Is security a required pre-close milestone, and if so, what close timing is supportable after it is completed?

## CRM Cleanup

| Record | Proposed change | Evidence | Approval requirement and status |
| --- | --- | --- | --- |
| Duplicate opportunity IDs | Merge or otherwise reconcile duplicates, preserving raw records and activity history | Repeated IDs in the export | Approval/source-of-truth check required; status unknown |
| Mixed-currency opportunities | Add currency metadata and report USD and EUR separately until a conversion policy is approved | Export contains both currencies without rules | Finance/revenue-operations policy required; status unknown |
| Opportunities missing next-step dates | Populate only confirmed buyer-relevant next steps and dates | Dates are absent | Deal-owner confirmation required; status unknown |
| Security-conflict opportunity | Propose a close-date or milestone-sequence correction | Close date precedes a required milestone | Deal-owner/forecast approval required; status unknown |

**Health ranking from the available activity evidence:** (1) the deal with the buyer-approved validation milestone; (2) the high-email deal only after buyer action is verified. Seller email count alone should not be used to rank deal health.
