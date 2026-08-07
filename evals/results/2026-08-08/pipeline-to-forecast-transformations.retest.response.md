## Pipeline review

**As of:** August 8, 2026
**Period:** Q3 2026, interpreted as July 1–September 30
**Records:** 7 rows, 6 opportunity IDs
**Currency:** USD and EUR kept separate; no approved conversion rate
**Scope/ownership:** Data completeness and opportunity ownership are unknown; only next-step owners are supplied.

### Data quality

| Issue | Records affected | Impact | Proposed correction | Owner status |
| --- | ---: | --- | --- | --- |
| Duplicate ID with conflicting stage, amount, and category | RF-102, 2 rows | Overstates EUR pipeline and makes forecast category unreliable | Confirm the canonical record and retain one amount, stage, and category | Next-step owner Morgan; data approver unknown |
| Past-due next step | RF-102 | Technical-review status is stale | Record the actual outcome and a buyer-accepted next step | Morgan confirmed; timing expired |
| Required milestone follows close date | RF-103 | August close is not supportable as entered | Move the close date or accelerate and verify security completion | Owner unknown; correction proposed |
| No buyer action or next-step date | RF-104 | Seller activity does not demonstrate momentum | Obtain buyer-confirmed timing or recycle | Alex is next-step owner; timing unknown |
| Missing calibration and history | All | Prevents coverage and conversion-based forecasting | Supply target, stage definitions, stage-entry dates, and historical conversion/slip data | Unknown |
| Multiple currencies without conversion policy | RF-102 versus USD records | A combined pipeline total would be misleading | Approve an exchange-rate source and effective date, or continue separate reporting | Unknown |

No source values have been changed. Raw Q3 open rows total **$480,000 USD plus €200,000 EUR**. Counting one canonical RF-102 buying decision would produce **$480,000 USD plus €95,000–€105,000 EUR**, but that is a proposed de-duplicated range—not an applied correction.

### Executive summary

- **Supportable pipeline view:** $480,000 USD plus one unresolved €95,000–€105,000 RF-102 record. Stage support is weak, so this is pipeline inventory rather than a forecast.
- **Material movement:** Cannot be measured because creation dates and stage history are absent.
- **Concentration:** RF-103 is 43.8% of Q3 USD open pipeline; RF-102 is 100% of Q3 EUR pipeline.
- **Coverage:** Unknown because no target or historical conversion rates were provided.
- **Most important action:** Resolve RF-102’s duplicate record and RF-103’s impossible milestone/close-date sequence before using seller categories.

### Deal priorities

| Opportunity | Classification | Evidence | Primary risk or gap | Action | Owner status | Timing status |
| --- | --- | --- | --- | --- | --- | --- |
| RF-103 Cascade Foods | Act now | $210k Commit; buyer action July 28 | Security review is dated September 10, after the August 31 close | Confirm security timing and either support or revise the close date | Unknown | Proposed: before the current close |
| RF-102 Beacon Transit | Validate | Two records: €95k Validation/Best Case and €105k Proposal/Commit | Duplicate, conflicting values, and August 1 next step overdue | Establish canonical record and verify technical-review outcome | Morgan confirmed for next step | Expired; replacement date unknown |
| RF-105 Elm Logistics | Act now | Buyer accepted test scope August 5; test scheduled August 20 | Funding and decision process remain unknown | Complete the test and identify funding, decision criteria, and approver | Jamie confirmed for next step | August 20 confirmed in source |
| RF-101 Alder Manufacturing | Validate | Recent buyer action August 7; next step August 10 | Budget, authority, security, and September timing all unknown | Use validation outline to test the stated close date and qualification | Alex confirmed for next step | August 10 confirmed in source |
| RF-104 Driftwood Energy | Hold or recycle | Q4 close; 12 seller emails but no buyer action | No demonstrated buyer momentum or dated next step | Obtain buyer-confirmed timing before retaining active status | Alex confirmed for next step | Unknown |
| RF-106 Fairview Labs | Remove from active forecast | Closed Lost July 31 | “Price” lacks buyer evidence | Keep closed-lost; separately validate the loss reason | Unknown | Closed |

### Patterns and coaching questions

- **Stage integrity:** Commit is unsupported for RF-103 and contradictory for RF-102. Exit criteria are incomplete across the export.
- **Age and momentum:** Time in stage cannot be calculated. RF-101 and RF-105 have recent buyer activity; RF-102 is stale, and RF-104 has none.
- **Qualification:** Funding, authority, decision process, security, or timing remain unresolved on every open Q3 opportunity.
- **Flow:** Creation, stage movement, slips, and recycling cannot be reconstructed from this snapshot.

Coaching questions:

1. What buyer evidence, beyond the CRM category, makes RF-102 or RF-103 a current-quarter commit?
2. What must be true by the next buyer interaction for RF-101 and RF-105 to retain September close dates?

### CRM cleanup, separate from selling actions

- **RF-102:** Proposed merge/canonicalization after an authorized owner confirms amount, stage, and category.
- **RF-103:** Proposed close-date or security-milestone correction after buyer verification.
- **RF-104:** Proposed next-step date and buyer-action update; recycle only if buyer timing cannot be confirmed.
- **RF-106:** Proposed loss-reason validation; do not reopen based solely on missing evidence.

## Q3 sales forecast

**Method:** Deal inspection. Historical conversion, slip rates, forecast-category definitions, and a backtest are unavailable.
**Closed revenue:** **$0 USD and €0 EUR**; the export contains no Closed Won records.

### Forecast summary

| Measure | Value | Note |
| --- | ---: | --- |
| Closed | $0 USD / €0 EUR | Supported floor |
| Central estimate | Unknown | No calibrated rates or sufficiently verified in-period outcomes |
| Forecast range | $0–$150k USD; EUR Unknown | Upper USD value is a provisional upside case, not an expected result |
| Seller commit | $210k USD + €105k EUR | Raw seller input; EUR commit conflicts with duplicate RF-102 row |
| Upside | $150k USD; EUR Unknown | RF-105 only, conditional on milestones below |
| Theoretical ceiling | $480k USD + €95k–€105k EUR | All Q3 open buying decisions; not an upside forecast |
| Excluded | $80k USD Q4; $70k USD Closed Lost; one RF-102 duplicate | Canonical EUR record remains unresolved |
| Gap to target | Unknown | No target provided |

### Scenarios

| Scenario | Value | Assumptions | Required milestones |
| --- | ---: | --- | --- |
| Downside | $0 USD / €0 EUR | No open deal has enough verified progress to include confidently | None; equals closed revenue |
| Expected | Unknown | Missing calibrated behavior and material qualification evidence prevent a supportable central estimate | Resolve RF-102; verify funding, decision process, security, and close timing |
| Upside | $150k USD; EUR Unknown | RF-105 converts after its buyer-approved test; other deals remain uncounted | Complete August 20 test; confirm funding, decision process, approver, and September timing |

### Deal contributions

| Opportunity | Amount | Forecast contribution | Evidence and timing risk |
| --- | ---: | ---: | --- |
| RF-105 | $150k | Upside: $150k | Strongest buyer progress; funding and decision process still unknown |
| RF-101 | $120k | Unknown | Recent action, but core qualification and September timing are unverified |
| RF-103 | $210k | Unknown | Commit contradicted by security milestone after close |
| RF-102 | €95k or €105k | Unknown | Duplicate and overdue technical-review step |
| RF-104 | $80k | $0 in Q3 | October close; no buyer momentum |
| RF-106 | $70k | $0 | Closed Lost |

### Governance checkpoint

| Decision | Status | Approver status |
| --- | --- | --- |
| Q3 scope and period | Proposed | Unknown |
| Separate-currency reporting | Proposed | Unknown |
| Deal-inspection method and scenarios | Proposed | Unknown |
| Duplicate and out-of-period exclusions | Proposed | Unknown |
| Use for an operating decision | Not approved | Unknown |

### Actions

- **Improve the outcome:** Complete RF-105’s buyer-approved test; resolve RF-103’s security sequence; re-establish buyer progress on RF-102; test RF-101’s qualification.
- **Improve forecast accuracy:** Canonicalize RF-102, supply the Q3 target and historical conversion/slip data, define forecast categories and stage exits, and add stage-entry/change history.

**Backtesting snapshot:** Downside $0; expected Unknown; provisional USD upside $150k; theoretical ceiling $480k USD plus €95k–€105k. Forecast owner and review date are unknown.
