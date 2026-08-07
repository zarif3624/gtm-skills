# Territory Plan: Four-Rep Equal-Count Request

**As of:** 2026-08-08
**Planning period:** Unknown
**Decision and scope:** Evaluate splitting 2,000 fictional accounts across four reps and determine whether the resulting territories can be certified as fair.
**Policy owner status:** Unknown

## Decision

An equal-count allocation is arithmetically **500 accounts per rep**. That is only a provisional count target, not a supported record-level assignment and not proof of fair territories.

**Fairness certification: Not issued.** The supplied data cannot establish comparable opportunity, feasible workload, continuity, or capacity. In particular, one rep is part-time and one is a new hire, but their approved availability and ramp factors are unknown. Assigning each person 500 accounts could therefore create materially unequal or infeasible workloads. No assignment authority or governing territory policy has been supplied, so the proposed split should not be activated.

## Definitions And Data Readiness

For this review, fairness means comparable supportable opportunity, feasible workload relative to approved capacity, transparent rules, and equal access to exceptions. Equal account count is a transparent arithmetic rule, but by itself it does not establish any of those fairness outcomes.

| Item | Definition or source | Coverage | Freshness | Status |
| --- | --- | ---: | --- | --- |
| Eligible account universe | The stated 2,000 fictional accounts; eligibility and exclusions not supplied | Unknown | Unknown | Unknown |
| Assignment unit | Account versus parent group not defined | Unknown | Unknown | Unknown |
| Opportunity signal | Reliable segment, revenue, hierarchy, and fit fields are absent | Insufficient | Unknown | Unknown |
| Workload signal | Reliable workload and active-opportunity fields are absent | Insufficient | Unknown | Unknown |
| Role capacity | Four reps; one part-time and one new hire, with no approved availability or ramp assumptions | Insufficient | Unknown | Unknown |
| Constraints and policy | No continuity, language, quota, planning-period, or territory-policy inputs supplied | None | Unknown | Unknown |

## Current State

- **Coverage gaps:** Cannot be measured because account eligibility, required coverage motions, and planning period are unknown.
- **Duplicate or conflicting ownership:** Cannot be audited from the supplied context.
- **Opportunity concentration:** Cannot be measured because opportunity and hierarchy signals are unreliable or absent.
- **Workload extremes:** Cannot be measured because workload and active-opportunity signals are absent.
- **Continuity constraints:** Unknown; active opportunities and customer relationships must not be moved without review.

## Assumptions

| Assumption | Value or range | Source and locator | Evidence status | Sensitivity test |
| --- | --- | --- | --- | --- |
| Equal-count arithmetic | 2,000 / 4 = 500 accounts per rep | User request | Confirmed only as arithmetic | Compare with capacity-weighted counts after capacity factors are approved |
| Rep availability | Unknown for every rep; one is known to be part-time | Supplied context | Incomplete | Vary each approved capacity factor and recalculate assignments |
| New-hire ramp | Unknown | Supplied context | Incomplete | Test approved ramp factors by phase and planning period |
| Account-level opportunity | Unknown | Supplied context | Insufficient | Re-score after segment, revenue, hierarchy, and fit data pass quality checks |
| Account-level workload | Unknown | Supplied context | Insufficient | Rebalance after workload and active-opportunity data are available |
| Full-time or fully ramped status | Not assumed for any rep | Territory-planning guardrail | Provisional | Source an individual capacity factor for each covered role |

Capacity should be modeled for each rep as:

`usable capacity = available work time × selling-work share × ramp factor`

If approved capacity factors are `c1` through `c4`, a capacity-proportional count-only baseline would be:

`rep i account target = 2,000 × c_i / (c1 + c2 + c3 + c4)`

The 500-each result follows only if all four capacity factors are equal. That equality is not supported and must not be assumed.

## Scenario Comparison

| Scenario | Opportunity balance | Workload balance | Continuity | Coverage | Key tradeoff |
| --- | --- | --- | --- | --- | --- |
| Continuity-first | Unknown | Unknown | Cannot construct without current ownership, customer, and active-opportunity data | Unknown | Minimizes disruption only after continuity records are verified |
| Opportunity-balanced | Cannot construct | Unknown | Unknown | Unknown | Requires reliable segment, revenue, hierarchy, and fit signals |
| Workload-balanced | Unknown | Cannot construct | Unknown | Unknown | Requires workload signals and approved rep capacity factors |
| Equal-count baseline | Exactly 500 accounts per rep | Unproven | Unproven | Unproven | Simple and transparent, but ignores opportunity, workload, continuity, and unequal capacity |

No scenario can be recommended or stress-tested at record level from the supplied inputs. The equal-count baseline is especially sensitive to the missing part-time availability and new-hire ramp factors: any approved factor below those of the other reps changes the appropriate capacity-weighted count.

## Recommended Design

- **Assignment rules:** Do not activate assignments yet. First deduplicate the universe, resolve parent-child groups, verify eligibility, preserve active opportunities and customer relationships pending authorized review, apply hard constraints, then balance on opportunity and workload relative to approved capacity.
- **Role and overlay model:** Unknown. Obtain approved available-work-time, selling-work-share, and ramp factors for each rep. Treat part-time availability and new-hire ramp as capacity inputs, not judgments of ability.
- **Explicit exclusions:** Unknown; identify ineligible records, named accounts, partners, existing customers, and ownership conflicts before allocation.
- **Tradeoffs accepted:** None approved. Equal counts would accept unknown imbalances in opportunity, workload, continuity, and capacity.
- **Unresolved decisions:** Planning period, assignment unit, hierarchy rules, policy owner, assignment authority, quota, continuity rule, language constraints, capacity assumptions, exception process, and success measures.

## Assignment And Exceptions

| Record or cohort | Proposed owner | Rule applied | Exception | Approval status | Effective date status |
| --- | --- | --- | --- | --- | --- |
| 500-account count target | Rep 1 placeholder | Equal count only | Record-level composition unknown | Proposed | Unknown |
| 500-account count target | Rep 2 placeholder | Equal count only | Record-level composition unknown | Proposed | Unknown |
| 500-account count target | Rep 3 placeholder | Equal count only | Record-level composition unknown | Proposed | Unknown |
| 500-account count target | Rep 4 placeholder | Equal count only | Record-level composition unknown | Proposed | Unknown |

These rows are planning placeholders, not account assignments. The supplied context does not identify which placeholder corresponds to the part-time rep or new hire, and no such mapping should be invented.

## Transition And Governance

- **Active-opportunity treatment:** Freeze moves until active opportunities are reliably identified; require authorized review for any transfer.
- **Customer continuity:** Preserve existing relationships until a confirmed policy defines when reassignment is allowed.
- **Conflict process:** Proposed: route parent-child, duplicate-ownership, active-deal, language, quota, and exception conflicts to the authorized policy owner; record the decision, reason, and approver.
- **Change communication:** Proposed only after assignment authority approves a versioned assignment table.
- **Review cadence:** Proposed: review after data repair and capacity approval, again before activation, and at an authorized cadence during the planning period.

The versioned assignment table should include source fields, rule applied, exception reason, approver, effective date, and review date.

## Measures And Rebalance Triggers

| Measure | Baseline | Target or learning goal | Owner status | Review date status |
| --- | --- | --- | --- | --- |
| Eligible-account and hierarchy coverage | Unknown | Proposed: sufficient verified coverage for record-level assignment | Unknown | Unknown |
| Opportunity-signal coverage and freshness | Unknown | Proposed: policy-owner-approved threshold | Unknown | Unknown |
| Workload and active-opportunity coverage | Unknown | Proposed: policy-owner-approved threshold | Unknown | Unknown |
| Approved capacity factor per rep | Unknown | Required for all four reps | Unknown | Unknown |
| Opportunity balance | Unknown | Proposed: approved tolerance | Unknown | Unknown |
| Workload-to-capacity balance | Unknown | Proposed: approved tolerance | Unknown | Unknown |
| Continuity exceptions | Unknown | Proposed: 100% documented and approved | Unknown | Unknown |

Rebalance when approved capacity or ramp changes materially, data quality crosses the approved readiness threshold, an active opportunity or continuity conflict is discovered, opportunity or workload exceeds the approved tolerance, or the planning period or quota changes.

## Conditions Required Before Certification

1. Verify the eligible account universe, duplicates, and parent-child assignment unit.
2. Repair and validate segment, revenue, hierarchy, fit, workload, and active-opportunity fields, including freshness and coverage.
3. Obtain approved capacity factors for all four reps, including the part-time availability and new-hire ramp schedule.
4. Confirm the territory policy, planning period, quotas, continuity and language rules, exception path, and assignment authority.
5. Build and compare continuity-first, opportunity-balanced, and workload-balanced assignments; test sensitivity to material assumptions and inspect extremes, not only averages.
6. Document all exceptions and obtain authorized approval.

Only after those conditions are met can a reviewer determine whether the territories are fair on the selected dimensions. Until then, the defensible conclusion is: **500 each is equal by count, but fairness is unverified and cannot be certified.**
