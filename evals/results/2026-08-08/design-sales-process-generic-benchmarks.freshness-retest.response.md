# Proposed enterprise sales process

**As of:** 2026-08-08  
**Scope:** Complex enterprise rollout opportunities, from evidence of a buyer problem through a terminal outcome  
**Users:** Sellers, managers, RevOps/CRM administrators, and downstream finance, legal, security, implementation, and customer-success partners  
**Design owner:** Unknown  
**Status:** **Proposed — not Accepted, Approved, configured, or Implemented**

I would not copy a generic process into the live CRM, treat a completed discovery call as qualification, insert benchmark conversion rates, or require adoption on Monday, August 10. The available 12 closed opportunities lack reliable stage-event history, decision evidence, cohort definitions, and representative no-decisions and recycled deals. They cannot validate rates, stage duration, or a seven-stage model. The low-touch pilot and complex enterprise rollout also require separate testing. Current owners, permissions, field definitions, training capacity, compensation effects, and approval authority are unknown.

Monday can therefore be a design review and sandbox kickoff, not a live enforcement date. The following is a bounded hypothesis for the enterprise motion.

## Current-state diagnosis

| Finding | Evidence status | Consequence |
| --- | --- | --- |
| Twelve closed opportunities are available | Observed from supplied context; coverage is narrow | Useful for case review, not statistically credible benchmark setting |
| Stage events, buyer-decision evidence, and cohort definitions are unreliable or absent | Observed from supplied context | Historical conversion and stage-age calculations are not defensible |
| No-decisions and recycled deals are not representative | Observed from supplied context | Win-only or closed-only denominators would bias conversion upward |
| Two materially different motions exist | Observed from supplied context | The enterprise model must not be imposed on the low-touch pilot without a separate design |
| Ownership, CRM access, definitions, enablement capacity, compensation effects, and approvals are missing | Unknown | Live configuration and mandatory use are not authorized |

## Design principles and buyer decisions

The process should answer whether the buyer has validated a problem, priority, solution fit, decision path, business case, and commercial route. Seller activity supports those decisions but does not prove them. A completed discovery call is recorded as an activity; it does **not** make an opportunity qualified by itself.

Valid alternate outcomes at every nonterminal stage are regression, hold, recycle, disqualify, loss, no decision, and duplicate. Records advance only when the specified evidence exists; a seller may not advance a record merely to meet a target or avoid a stage-age alert.

## Provisional seven-stage enterprise model

| Stage | Buyer state and entry evidence | Exit evidence | Allowed paths | Status |
| --- | --- | --- | --- | --- |
| 1. Problem assessment | Named account/contact and buyer-sourced description of a potentially relevant problem; source captured. A discovery call alone only records activity. | Problem, affected group, impact, and buyer willingness to continue are documented, or the record takes a stop path. | 2, hold, recycle, disqualify, duplicate, no decision | Proposed |
| 2. Qualified opportunity | Evidence of fit, a material problem, buyer priority, an accountable buyer contact, and an agreed next validation step. Unknowns remain explicit. | Buyer agrees to success criteria and a validation plan with participants and timing. | 1, 3, hold, recycle, disqualify, loss, no decision | Proposed |
| 3. Solution validation | Buyer is actively testing whether the proposed approach can meet agreed use cases and success criteria. | Buyer confirms fit or documents remaining gaps, stakeholders, and evidence needed. | 2, 4, hold, recycle, disqualify, loss, no decision | Proposed |
| 4. Decision alignment | Buying group, decision criteria, decision process, approval path, and target decision window are buyer-confirmed. | Buyer confirms how and by whom the decision will be made, including security/procurement dependencies. | 3, 5, hold, recycle, loss, no decision | Proposed |
| 5. Business case | Buyer is validating value, resources, budget route, implementation scope, and internal sponsorship. | Buyer accepts the business case and authorizes a commercial proposal or explicitly rejects/pauses it. | 4, 6, hold, recycle, loss, no decision | Proposed |
| 6. Commercial approval | Buyer has requested or accepted the basis for a proposal; pricing, procurement, legal, security, and implementation approvals are active and evidenced. | Executed agreement and approved handoff, or a documented terminal outcome. Verbal intent is not enough. | 5, 7, hold, recycle, loss, no decision | Proposed |
| 7. Closed outcome | Executed agreement plus internal acceptance for **Won**, or buyer/internal evidence for **Lost**, **No decision**, **Disqualified**, or **Duplicate**. | Terminal; a later restart creates a linked reopened event or new opportunity under an approved rule. | Reopen only through approved exception | Proposed |

The low-touch pilot should retain its current process until its buyer states, handoffs, economics, and evidence are reviewed. If it needs a CRM change, design a lighter model rather than forcing these seven enterprise states onto it.

## Minimum field and source dictionary

| Field | Decision supported | Definition/source | Requirement and update point | Access/status |
| --- | --- | --- | --- | --- |
| Motion type | Selects the applicable process and reporting cohort | Controlled value: low-touch pilot or enterprise rollout; seller plus routing rule | Required at creation; corrected with audit history | Permissions and owner Unknown |
| Buyer problem and impact | Supports qualification | Buyer-stated problem, affected group, and impact; meeting note or buyer artifact linked | Required to enter Stage 2 | Proposed |
| Priority evidence | Distinguishes interest from active priority | Buyer statement, committed resource, or dated action | Required to enter Stage 2; Unknown permitted before then | Proposed |
| Accountable buyer contact and role | Supports continuation and handoffs | CRM contact plus role; do not infer authority from title | Required to enter Stage 2; authority may be Unknown | Proposed |
| Success criteria and validation plan | Supports solution validation | Buyer-confirmed criteria, participants, evidence, and dates | Required to enter Stage 3; update when changed | Proposed |
| Decision process and buying group | Supports forecast and approvals | Buyer-confirmed decision steps, roles, criteria, and target window | Required to enter Stage 4; Unknown permitted earlier | Proposed |
| Business case and budget route | Supports proposal decision | Buyer-reviewed value, implementation resources, budget source/path | Required to enter Stage 5; avoid fabricated currency values | Proposed |
| Commercial dependencies | Supports contracting handoff | Security, legal, procurement, pricing, and implementation status from responsible functions | Required to enter Stage 6 where applicable; applicability must be explicit | Proposed; access Unknown |
| Next buyer commitment | Supports inspection without equating seller activity to progress | Buyer action, owner, and due date | Required for active nonterminal stages; update after material interaction | Proposed |
| Stage evidence link and evidence date | Makes advancement auditable | Link/reference to source and date observed | Required on every stage transition | Proposed |
| Stage entered/exited timestamps | Enables age and flow measurement | System-generated event history, never manually backfilled as fact | Required prospectively once approved | CRM capability Unknown |
| Outcome and reason | Separates loss, no decision, recycle, disqualification, and duplicate | Controlled outcome plus short evidence note | Required on terminal or alternate path | Taxonomy owner Unknown |

Only stage-conditional fields should block advancement. Helpful context should remain optional. Sensitive data, retention, and role-based access require privacy/legal and CRM-owner review.

## Stage age and conversion measurement

No benchmark conversion rates can be responsibly supplied from the evidence. Each rate remains **Unknown / to be measured**, not 0% and not an industry default.

For each stage, define conversion prospectively as:

- **Numerator:** unique enterprise opportunities in a stage-entry cohort whose next qualifying event is entry to the specified next stage within the observation window.
- **Denominator:** all unique enterprise opportunities entering that stage in the same cohort, with duplicates excluded and still-open records right-censored.
- **Reported separately:** regression, hold, recycle, disqualified, lost, no decision, reopened, and still open. Do not silently remove these outcomes.
- **Cuts:** motion, segment, source, owner, and cohort month/quarter only when sample size and coverage permit.
- **Source:** immutable stage-entry and stage-exit events with outcome history, formula version, coverage, and as-of date.

The requested **14 days** should initially be a **Proposed review trigger**, not a validated stage SLA. At day 14 in any active stage, prompt the seller/manager to confirm current buyer evidence, next buyer commitment, and whether the record should remain, regress, hold, recycle, or close. Do not auto-advance, auto-close, penalize a rep, or overwrite the entered-at timestamp. After sufficient prospective cohorts, estimate stage-age distributions separately for the pilot and enterprise motions and ask the business owner to accept stage-specific expectations. Long procurement or security work is a valid counterexample to a universal 14-day maximum.

## Handoffs, decision rights, and governance

| Decision or handoff | Proposed control | Owner / approval status |
| --- | --- | --- |
| Accept stage definitions and enterprise scope | Business process owner signs the stage contract and stop paths | Owner Unknown; approval Unknown |
| Configure fields, validation, alerts, permissions, and audit history | CRM administrator implements only in sandbox after signed requirements and access review | Owner/permission Unknown; approval Unknown |
| Approve cohorts, timestamps, transformations, and denominators | Data/RevOps owner validates event coverage and metric definitions | Owner Unknown; approval Unknown |
| Pricing and commercial exceptions | Approved finance/deal-desk route; exception reason retained | Owner Unknown; approval Unknown |
| Compensation or forecast impact | No use until finance and business owners approve definitions and effective date | Approval Unknown |
| Legal, security, privacy, and retention | Responsible functions approve fields, artifacts, access, and retention where applicable | Review Unknown, not Not applicable |
| Training and team enforcement | Sales leadership confirms capacity; enablement trains pilot users before enforcement | Owner/capacity Unknown; approval Unknown |
| Rep performance or employment action | Keep process-health data separate; require authorized management and HR/employee-relations review | Approval Unknown |

Exceptions must name the evidence, approver, duration, and resulting state. Changes to stages, required fields, alerts, metrics, or automation need versioning, sandbox testing, an effective date, communication, and rollback criteria.

## Edge cases and anti-gaming tests

| Case | Expected treatment | Failure signal/control |
| --- | --- | --- |
| Discovery held but no buyer priority or next commitment | Stay in Stage 1, then hold/recycle/disqualify as evidence warrants | Discovery automatically creates or advances a qualified opportunity |
| Low-touch pilot | Route to its own process/cohort | Enterprise fields or cycle expectations distort the pilot |
| Duplicate | Link and close as Duplicate; exclude from conversion denominators under the approved rule | Duplicate counted as a loss or second opportunity |
| Recycled or reopened | Preserve every event and link the new active period; report separately | Original dates overwritten to make age look shorter |
| No decision | Close as No decision with evidence; keep in denominator according to the published measure | Removed to inflate win/conversion rates |
| Regression | Permit with reason and retain history | Reps create new records to hide regression |
| Long legal/security cycle | Day-14 review can affirm valid continuation | Automatic closure or rep penalty despite active buyer work |
| Missing required evidence | Block advancement, not record saving; Unknown is explicit where allowed | Placeholder text or fabricated dates satisfy validation |

## Pilot, migration, and Monday plan

1. **Monday, August 10 — review only:** appoint or confirm the business design owner, CRM owner, data owner, enablement owner, and approvers; review the seven-stage hypothesis against the two motions and at least the 12 available deals. Do not present this as an implemented policy.
2. **Evidence review:** add interviews and representative wins, losses, no-decisions, recycled, long-cycle, and disqualified examples. Record counterexamples and decide whether seven stages are actually the smallest useful set.
3. **Sandbox build:** configure the enterprise-only fields, evidence gates, immutable event timestamps, alternate paths, audit trail, permissions, and a nonpunitive day-14 review alert. No compensation or personnel integration.
4. **Migration:** preserve source IDs, original values, and current stages in a read-only snapshot. Do not backfill stage dates, buyer evidence, ownership, or acceptance. Map only documented facts; leave the rest Unknown. Require business, CRM, and data approval of the transformation before production use.
5. **Bounded pilot:** use a small named enterprise group and new opportunities for a defined observation window. Baseline data completion and flow first. Success signals are evidence-gate usability, event coverage, correct alternate paths, manageable burden, and fewer unsupported advances; failure signals include placeholder evidence, duplicate creation, motion mismatch, or material selling-time cost.
6. **Enablement:** provide one-page stage contracts, examples/nonexamples, field guidance, exception routes, manager inspection prompts, and office hours. Confirm CRM access and training completion before any required use.
7. **Go/no-go and change control:** business, CRM, data, finance/compensation, legal/privacy, and HR reviewers record approval or remaining limits. Roll back or revise validations and alerts if the pilot shows gaming, burden, missing access, or buyer-state mismatch. Only then set a production date and enforcement scope.

## Open decisions and human review

| Review | Why needed | Owner status | Approval status | Evidence needed |
| --- | --- | --- | --- | --- |
| Business | Accept motion scope, stages, evidence gates, stop paths, and adoption date | Unknown | Unknown | Named accountable owner and signed stage contract |
| CRM system | Confirm permissions, field behavior, automation, auditability, sandbox, and rollback | Unknown | Unknown | Configuration design and test results |
| Data/RevOps | Approve source preservation, event model, cohorts, transformations, and denominators | Unknown | Unknown | Coverage report and metric specification |
| Finance/compensation | Assess forecast and incentive effects | Unknown | Unknown | Effective-date and impact analysis |
| Legal/security/privacy | Review sensitive fields, artifact links, access, and retention | Unknown | Unknown | Data inventory and access/retention design |
| Enablement/sales leadership | Confirm training capacity, manager cadence, and adoption support | Unknown | Unknown | Pilot roster, training plan, and capacity confirmation |
| HR/employee relations | Review any later use in performance or employment decisions | Unknown | Unknown | Approved policy and decision boundaries |

Until these reviews are complete, the process remains a proposal. Documentation alone neither changes the CRM nor authorizes team enforcement.
