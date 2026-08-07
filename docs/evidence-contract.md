# Evidence And Status Contract

This contract gives every skill and handoff a shared language. It prevents an agent from turning a statement into a fact, a suggestion into a commitment, or a CRM value into truth merely because the information moved between artifacts.

## 1. Claim Evidence

| Status | Meaning | Minimum support |
| --- | --- | --- |
| Verified | Directly supported for the stated scope | Authoritative source plus locator and observation/access date |
| Reported | Attributed to a person or system but not independently verified | Named source and locator |
| Inferred | Reasoned conclusion from cited evidence | Supporting evidence and reasoning; disconfirming evidence when material |
| Hypothesis | Testable possibility, not a conclusion | Reason for the hypothesis and a falsifiable test |
| Unknown | Not supportable from available evidence | The smallest useful evidence needed |
| Contradicted | Material sources disagree | Both sources, the conflict, and the decision needed |

Confidence is not a substitute for evidence status. A highly confident inference remains `Inferred`.

## 2. Buyer Or Customer State

Use `Proposed`, `Accepted`, `Rejected`, `Completed`, or `Unknown` for plans, next steps, dates, and commitments. A seller-entered action is not buyer-accepted unless the source shows acceptance. Silence, meeting attendance, email opens, and CRM stage do not establish acceptance.

## 3. Ownership And Governance

Keep the person or role separate from its status.

| Axis | Allowed states | Example |
| --- | --- | --- |
| Owner | Confirmed / Proposed / Unknown | `Buyer security owner: Unknown` |
| Timing | Confirmed / Proposed / Accepted / Unknown | `Review after validation: Proposed` |
| Approval | Approved / Proposed / Rejected / Unknown | `Currency policy: Proposed` |
| Execution | Executed / Not executed / Unknown | `Order form: Not executed` |

Do not invent a department, approver, or cadence. Describe the required responsibility when the organization is unknown.

## 4. Source Locator

A material claim should be traceable with the smallest locator that another reviewer can inspect:

- source name or stable identifier;
- URL, document section, page, row, record ID, or transcript timestamp;
- observed or accessed date;
- source type and coverage limitation when relevant;
- access restriction or sensitivity note when needed.

Use direct sources over summaries when practical. Do not cite a source for a broader claim than it supports.

## 5. Transformation Record

Never silently overwrite source evidence. For deduplication, normalization, currency conversion, date changes, scoring, or classification, record:

| Field | Required content |
| --- | --- |
| Source | Record and original value |
| Transformation | Rule or proposed change |
| Rationale | Evidence supporting the change |
| Status | Proposed / Approved / Rejected / Unknown |
| Approver status | Confirmed / Proposed / Unknown |
| Output | Resulting value, kept separate from source |

## 6. Handoff Invariants

Across skills and systems:

1. `Unknown` never becomes known without new evidence.
2. `Reported`, `Inferred`, and `Hypothesis` never become `Verified` merely through repetition.
3. `Proposed` never becomes `Accepted`, `Approved`, or `Completed` without an acceptance or approval source.
4. CRM stage, probability, forecast category, and seller confidence remain reported inputs until calibrated or corroborated.
5. Conflicts and exclusions remain visible downstream.
6. Source restrictions and sensitivity do not disappear at handoff.

When a downstream artifact needs a stronger state than its input supports, keep the current state and name the validation step.

## Portable Records

The vendor-neutral [evidence and action ledger pack](../reference-packs/evidence-ledger/) provides matching CSV headers and closed JSON Schemas for these rules. Use it when a workflow needs structured handoffs across agents, spreadsheets, CRMs, or internal tools. The schemas validate vocabulary and shape; they do not verify the underlying claims or authorize access.
