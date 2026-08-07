# Proposed Sales Process Design

**As of:** 2026-08-08
**Scope:** Low-touch pilot and complex enterprise rollout motions
**Object:** Opportunity, from evaluation through signed agreement or terminal outcome
**Status:** **Proposed — not approved, configured, or implemented**

## Decision

Do not copy a generic seven-stage process into the live CRM, count discovery calls as qualification, install benchmark conversion rates, or enforce 14-day stage SLAs next Monday.

The available evidence—12 closed opportunities without reliable stage history, buyer-decision evidence, cohort definitions, or representative no-decisions and recycled deals—cannot validate those rules. The two sales motions may also require different evidence and timing. Required owners, permissions, field definitions, training capacity, compensation impacts, and approval authority remain unknown.

Monday, August 10 can be a design kickoff and readiness review, not a mandatory go-live.

## Current-State Diagnosis

| Finding | Evidence status | Consequence |
| --- | --- | --- |
| Only 12 closed opportunities are available | Observed | Too little and too selected to establish conversion or stage-duration expectations |
| Stage-event history and buyer-decision evidence are unreliable or absent | Observed | Historical conversion and stage-age calculations would not be defensible |
| No-decisions and recycled deals are not representative | Observed | Funnel results would overstate success and omit legitimate paths |
| Pilot and enterprise-rollout motions differ materially | Observed | A single undifferentiated funnel could create false comparisons and inappropriate SLAs |
| Ownership, permissions, field definitions, enablement capacity, compensation effects, and approval authority are unknown | Observed | Configuration and enforcement are not authorized or operationally ready |

A completed discovery call should remain an activity event. It may trigger review, but it does not prove that a buyer has a validated problem, priority, owner, or decision path and therefore must not automatically create a qualified opportunity.

## Provisional Buyer-Decision Map

| Buyer decision or state | Minimum proposed evidence | Valid alternate path |
| --- | --- | --- |
| Explore a problem | Buyer acknowledges a relevant problem or desired change | Nurture, disqualify |
| Treat it as a priority | Buyer confirms consequence, desired outcome, and reason to act | Hold, recycle, no decision |
| Organize an evaluation | Buyer identifies an internal owner and evaluation approach | Hold, recycle |
| Define how a decision will be made | Stakeholders, criteria, authority, and approval path are understood | Regress, hold, disqualify |
| Validate the offer | Motion-specific success criteria and results are documented | Regress, loss, no decision |
| Seek commercial approval | Scope, price, procurement, legal, and other approvals are actively addressed | Hold, loss |
| Commit | Buyer selection and required approvals are evidenced | Closed won, loss, no decision |

## Provisional Seven-Stage Validation Skeleton

This is a hypothesis to test—not a standard to configure unchanged.

| Stage | Buyer state | Entry evidence | Exit evidence |
| --- | --- | --- | --- |
| 1. Evaluation opened | Buyer agrees to explore a relevant issue | Buyer-confirmed issue and agreed next evaluation step | Problem and consequence validated |
| 2. Problem validated | Buyer confirms the problem or desired change | Buyer statement and evidence source | Desired outcome and priority established |
| 3. Priority established | Buyer has a reason and intent to act | Outcome, consequence, timing rationale, and internal owner | Evaluation approach agreed |
| 4. Decision path confirmed | Buyer explains how the decision will be made | Stakeholders, criteria, authority, and approval path | Validation plan accepted |
| 5. Solution validated | Buyer evaluates the offer against agreed criteria | Motion-specific plan and success criteria | Buyer confirms results meet or fail criteria |
| 6. Commercial approval | Buyer is pursuing approval for defined scope and terms | Proposal or commercial package under active review | Selection and required approvals evidenced |
| 7. Commitment | Buyer has selected the offer and is completing commitment | Selection evidence and remaining commitment steps | Signed agreement or terminal outcome |

For a low-touch pilot, Stage 5 should capture pilot success criteria, duration, ownership, and next-step decision. For an enterprise rollout, it may require technical, security, implementation, procurement, and business validation. Their conversion and timing must be measured separately.

Every active stage must allow regression, hold, recycle, disqualification, loss, and no-decision where appropriate. Discovery completion alone satisfies none of the stage exits.

## Minimum Proposed Fields

| Field | Purpose | Source | Requirement status |
| --- | --- | --- | --- |
| Sales motion | Separates pilot from rollout | Seller selection under defined rules | Proposed required |
| Buyer problem or desired change | Supports qualification | Buyer evidence | Proposed required for Stage 2 |
| Consequence and desired outcome | Supports priority decision | Buyer evidence | Proposed required for Stage 3 |
| Internal buyer owner | Identifies evaluation ownership | Buyer confirmation | Proposed required for Stage 3 |
| Decision criteria and process | Supports evaluation planning | Buyer confirmation or shared plan | Proposed required for Stage 4 |
| Stakeholders and approval path | Supports handoffs and forecasting | Buyer evidence | Proposed required for Stage 4; unknown permitted where explicitly documented |
| Validation plan and result | Supports solution-fit decision | Shared plan and outcome | Proposed required for Stage 5 |
| Commercial/procurement status | Supports commitment work | Buyer, proposal, or approval record | Proposed required for Stage 6 |
| Stop-path reason | Distinguishes loss, no decision, recycle, and disqualification | Seller with controlled definitions | Proposed required on exit |
| Evidence source and date | Makes advancement auditable | Linked note or approved source | Proposed required at each stage transition |
| Stage event timestamp | Enables flow measurement | CRM-generated event | Proposed required; never manually backfilled without approved transformation |

Field access, retention, maintenance responsibility, and CRM feasibility remain unconfirmed.

## Measurement Plan

No benchmark conversion rates can be responsibly set from the supplied data. Instead, instrument the process and build internal baselines.

| Measure | Definition | Limitation/status |
| --- | --- | --- |
| Stage conversion | Eligible cohort entrants reaching the defined next state ÷ eligible entrants, by motion and entry period | Proposed; needs reliable event history and an observation window |
| End-to-end conversion | Qualified opportunities reaching signed agreement ÷ qualified cohort entrants | Proposed; qualification evidence must first be validated |
| Stage age | Current time minus system-recorded stage-entry time | Proposed; report separately by motion and censor still-open records |
| Flow | Opportunity entries, exits, regressions, holds, recycles, and terminal outcomes per period | Proposed |
| No-decision and recycle rate | Respective outcomes ÷ eligible cohort entrants | Proposed; currently underrepresented |
| Data quality | Evidence-complete transitions ÷ all transitions | Proposed |

A 14-day threshold may be tested as a **review trigger**, not as a validated SLA and never as an automatic advancement, closure, or rep-performance penalty. Pilot and enterprise-rollout distributions should be analyzed separately before any service expectation is approved.

## Governance and Anti-Gaming Controls

| Case | Required treatment |
| --- | --- |
| Discovery completed without buyer evidence | Record the activity; keep unqualified or nurture rather than advancing |
| Long-cycle enterprise evaluation | Trigger review after the proposed threshold; allow an evidenced exception |
| Pilot converting to rollout | Preserve the pilot outcome and create an approved transition or linked rollout episode |
| No decision | Record distinctly from competitive or fit loss |
| Recycled deal | Preserve prior events and create a new episode or explicit recycle transition |
| Reopened opportunity | Preserve the original outcome and history; do not overwrite timestamps |
| Duplicate | Resolve through an approved merge process while retaining source history |
| Missing evidence | Use an explicit unknown state where allowed; do not fabricate or backfill evidence |
| Stage gaming | Require source, date, and observable exit evidence for advancement |

Process-health reporting must remain separate from compensation or employment action until authorized management, Finance, and applicable HR review approve the consequences.

## Pilot, Migration, and Rollout

1. **Monday readiness review:** Assign or confirm the business process owner, CRM owner, data/reporting owner, enablement owner, and approvers. Review the two-motion hypothesis and unresolved compensation effects.
2. **Evidence review:** Test the proposed stages against available wins plus newly collected losses, no-decisions, recycled deals, and exceptions. Conduct buyer-facing or seller interviews where records are insufficient.
3. **Configuration design:** Confirm permissions, field definitions, transition rules, timestamps, reports, and rollback method in a non-production environment.
4. **Bounded pilot:** Use a small, named cohort for each motion. Treat 14 days only as a review alert. Capture false advancement, burden, exceptions, and missing buyer states.
5. **Migration:** Prefer new opportunities for clean measurement. Review existing opportunities individually; do not invent historical entry dates or qualification evidence.
6. **Enablement:** Provide stage-evidence examples, stop-path guidance, CRM instructions, manager review guidance, and a feedback channel before activation.
7. **Approval and go-live:** Require documented business, CRM-system, data, enablement, and Finance approval. Add Legal, Privacy, or HR review where fields or enforcement consequences require it.
8. **Change control:** Version definitions, document approvals, monitor results by motion, and permit rollback or revision when the pilot reveals burden, gaming, or segment mismatch.

## Open Decisions

| Decision | Proposed owner status | Approval status |
| --- | --- | --- |
| Qualification evidence and opportunity creation point | Business owner unknown | Unapproved |
| Whether one stage model can serve both motions | Business owner unknown | Unapproved |
| Field definitions, access, and retention | CRM/data owners unknown | Unapproved |
| Stage-event instrumentation and cohort rules | Data owner unknown | Unapproved |
| Review thresholds or eventual SLAs | Business/data owners unknown | Unvalidated |
| Compensation and performance-reporting effects | Sales leadership/Finance/HR unknown | Unapproved |
| Training capacity and enforcement date | Enablement/business owners unknown | Unapproved |
| CRM configuration and migration authority | System owner unknown | Unapproved |

The earliest responsible next step is the Monday readiness review—not live enforcement.
