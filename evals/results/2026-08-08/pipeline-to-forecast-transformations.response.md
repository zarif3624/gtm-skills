# Pipeline Review — RelayFox

**As of:** 2026-08-08
**Period:** Q3 2026, assumed July 1–September 30
**Currencies:** USD and EUR reported separately; no approved conversion rate
**Records reviewed:** 7 rows, representing 6 opportunity IDs
**Source treatment:** No source values were changed.

## Data Quality

| Issue | Records affected | Impact | Proposed correction |
| --- | ---: | --- | --- |
| Duplicate ID with conflicting stage, amount, and category | RF-102 | Canonical pipeline and EUR forecast are unresolved | Confirm whether €95k/Validation/Best Case or €105k/Proposal/Commit is authoritative; retain one canonical opportunity |
| Required milestone occurs after close date | RF-103 | August close and Commit status are unsupported | Confirm security-review timing, assign its owner, then revise the close date if necessary |
| Past next-step date | RF-102 | Momentum cannot be established | Record the outcome of the August 1 technical-review step and a buyer-accepted next action |
| Missing buyer action or next-step date | RF-104 | Seller emails do not establish buyer progress | Record a meaningful buyer action and accepted date, or recycle the opportunity |
| Mixed currencies without an approved rate | All EUR/USD rows | No defensible combined total or coverage calculation | Keep currencies separate until a dated conversion policy is approved |
| Forecast definitions, target, and historical rates unavailable | Entire export | Qualified coverage and a calibrated central forecast cannot be calculated | Supply target, category definitions, and comparable win/slip history |

The Q3 open pipeline contains four canonical buying decisions: **$480k USD plus one unresolved EUR opportunity entered at both €95k and €105k**. This is entered pipeline, not confirmed qualified pipeline. An additional **$80k USD** closes in Q4, and **$70k USD** is Closed Lost.

## Deal Priorities

| Opportunity | Classification | Evidence and primary risk | Recommended action | Owner/date status |
| --- | --- | --- | --- | --- |
| RF-101 — Alder Manufacturing | Validate | Buyer action is current, but budget, authority, security, and September timing remain unknown | Send the validation outline and secure answers to the four stated gaps | Alex and Aug. 10 confirmed |
| RF-102 — Beacon Transit | Act now | Duplicate records conflict; buyer action is stale and the Aug. 1 next step has passed | Resolve the canonical record and re-establish the technical review with a buyer-accepted next step | Morgan confirmed; revised date unknown |
| RF-103 — Cascade Foods | Act now | $210k Commit, but security is dated Sept. 10 after the Aug. 31 close; milestone owner is missing | Assign an owner, confirm remaining commercial steps, and either advance security or propose a supportable close date | Owner unknown; revised close proposed |
| RF-104 — Driftwood Energy | Hold or recycle | Q4 close, no supplied buyer action, and no next-step date; 12 seller emails are not momentum | Require an accepted stakeholder meeting before treating the deal as active | Alex confirmed; date unknown |
| RF-105 — Elm Logistics | Monitor | Buyer accepted the workflow-test scope; funding and decision process remain unknown | Run the test, capture its result, and validate funding and decision process | Jamie and Aug. 20 confirmed |
| RF-106 — Fairview Labs | Validate | Closed Lost is clear, but “Price” is not supported by buyer evidence | Validate the loss reason for learning and reporting; do not reopen based on this export | Owner and review timing unknown |

## Patterns

- **Stage integrity:** RF-102 and RF-103 have material contradictions. Stage exit criteria are not defined well enough to validate the remaining stages conclusively.
- **Momentum:** RF-105 has the strongest current buyer evidence. RF-101 is current but still lightly qualified. RF-102 and RF-103 need immediate validation; RF-104 lacks buyer momentum.
- **Concentration:** RF-103 represents **43.8% of Q3 USD open pipeline** and **58.3% of the modeled USD upside** below.
- **Flow:** Pipeline creation, movement, slips, and recycling cannot be measured from a single snapshot.
- **Coverage:** Target and historical conversion are missing, so qualified coverage is **Unknown**.

### Coaching questions

1. What buyer evidence justifies Commit for RF-103 before security is completed?
2. Which RF-102 record reflects the current buying decision, and what happened after the missed technical-review date?
3. What observable result from RF-105’s workflow test would advance—or disqualify—the deal?

## CRM Cleanup

| Record | Proposed change | Evidence | Approval needed |
| --- | --- | --- | --- |
| RF-102 | Merge or retire the duplicate after confirming stage, amount, and category | Same ID with conflicting values | Opportunity owner/RevOps |
| RF-103 | Add milestone owner and correct sequencing between security and close | Sept. 10 milestone follows Aug. 31 close | Opportunity owner |
| RF-104 | Populate buyer action and next-step date, or recycle | Both are absent | Opportunity owner |
| RF-106 | Amend the loss reason only if buyer evidence supports it | “Price” is seller-selected without a decision artifact | Opportunity owner/manager |

# Q3 Sales Forecast — RelayFox

**Method:** Deal inspection from one CRM snapshot
**Evidence window:** Buyer activity supplied through 2026-08-07
**Target:** Unknown

## Forecast Summary

| Measure | Value | Note |
| --- | ---: | --- |
| Closed Won | $0 USD; €0 EUR | Supported floor |
| Central estimate | **Unknown** | No calibrated history and insufficient milestone evidence |
| Forecast range | **$0–$360k USD; €0–€105k EUR** | Upper bounds require the named milestones below; EUR amount remains disputed |
| Seller-entered Commit | $210k USD + €105k EUR | Input only; both Commit entries have material integrity issues |
| Plausible upside | $360k USD + one unresolved €95k/€105k deal | Not a combined-currency total |
| Theoretical ceiling | $480k USD + one unresolved €95k/€105k deal | All Q3 open pipeline; not an upside forecast |
| Excluded from Q3 | $80k USD | RF-104 closes in Q4 |
| Closed Lost contribution | $0 | RF-106’s $70k does not contribute |
| Gap to target | Unknown | Target not supplied |

## Scenarios

| Scenario | Value | Assumptions and required milestones |
| --- | ---: | --- |
| Downside | **$0 USD; €0 EUR** | No Closed Won revenue exists, and every open deal can still slip or lose |
| Expected | **Unknown** | Current evidence cannot support a calibrated central estimate |
| Upside | **$360k USD + €95k/€105k EUR** | RF-105 completes its test and confirms funding/decision process; RF-103 completes security, establishes ownership, and retains a supportable Q3 close; RF-102 is deduplicated and completes technical review |

## Deal Contributions

| Opportunity | Amount | Forecast treatment | Evidence and timing risk |
| --- | ---: | --- | --- |
| RF-101 | $120k | Theoretical ceiling only | Discovery-stage qualification gaps make a September close insufficiently supported |
| RF-102 | €95k/€105k | Conditional upside | Canonical amount, stage, and category unresolved; technical step overdue |
| RF-103 | $210k | Conditional upside | Security follows entered close date; milestone owner absent |
| RF-105 | $150k | Conditional upside | Strongest buyer evidence, but funding and decision process remain unknown |
| RF-104 | $80k | Excluded | Close date is Q4 and buyer momentum is absent |
| RF-106 | $70k | Zero contribution | Closed Lost |

## Risks and Sensitivities

- If RF-103 cannot retain a supportable Q3 close, modeled USD upside falls from **$360k to $150k**.
- If RF-105’s buyer test does not confirm value or funding, no USD opportunity has enough current evidence to anchor an expected case.
- Resolving RF-102 changes the EUR amount by **€10k** and may materially change its forecast category.
- Historical conversion, slip behavior, sales-cycle data, and the target are required to replace the **Unknown** central estimate.

## Actions

- **Improve the outcome:** Complete RF-105’s buyer-approved test; resolve RF-103’s security sequence and ownership; re-establish RF-102’s technical review.
- **Improve forecast accuracy:** Resolve the RF-102 duplicate, define stage exits and forecast categories, provide the Q3 target and comparable history, and capture buyer-backed dates and milestones.

**Backtesting snapshot:** Assumptions recorded above; review timing is **Proposed** after the RF-102 and RF-103 validations and RF-105’s scheduled buyer test. Actual outcome is pending.
