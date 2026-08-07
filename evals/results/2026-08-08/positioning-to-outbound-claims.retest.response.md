# Outbound Sequence: Operations Leaders

**As of:** 2026-08-08
**Artifact status:** Proposed — copy complete, but not cleared for launch
**Sequence goal:** Start qualified conversations about approval-workflow fit
**Channel and region:** Email; region unknown

The “#1 AI approvals platform,” “trusted by Fortune 500 companies,” “universal integrations,” and “50% savings” claims are held and excluded. There is no evidence or approval supporting them, and channel adaptation cannot turn held positioning claims into outbound proof.

## Message hypothesis

- **Audience and responsibility:** Operations leaders responsible for workflow consistency, approval handoffs, and decision traceability.
- **Verified reason to contact:** Role-level relevance only; no recipient- or account-level signal is available.
- **Problem hypothesis:** Some operations teams may coordinate approvals through spreadsheets or fragmented handoffs. This is unverified and must remain conditional.
- **Relevant value:** `{{product_name}}` routes workflow approvals and records decision history.
- **Important unknowns:** The recipient’s current process, pain, priorities, systems, integration needs, consent or lawful outreach basis, region, and product fit.

## Sequence

### Touch 1 — Day 1, email

**Subject options:**

- A question about approval handoffs
- How are approvals routed today?
- Approval history at `{{company_name}}`

Hi `{{first_name}}`,

I’m reaching out because operations leaders often own how approvals move through day-to-day workflows.

`{{product_name}}` routes workflow approvals and records the decision history. If your team is coordinating approvals through spreadsheets or scattered handoffs, would it be useful to compare that process with a more structured approach?

Open to a 15-minute fit check around one approval workflow?

If this is not relevant, reply “no” and I’ll close the loop.

`{{sender_name}}`
`{{sender_company}}`
`{{required_sender_details_and_opt_out}}`

**Purpose:** Test whether the conditional workflow hypothesis is relevant.
**Stop condition:** Any opt-out, negative response, suppression signal, or reply.

### Touch 2 — Day 4, email

**Subject:** Re: approval handoffs

Hi `{{first_name}}`,

One practical question: when an approval is revisited, how easy is it to see what was decided and route the next step?

That is the narrow use case `{{product_name}}` supports: routing workflow approvals and recording decision history. I don’t want to assume how `{{company_name}}` handles it today.

Worth a short walkthrough using one process you choose?

If not, reply “no” and I won’t follow up again.

`{{sender_name}}`
`{{sender_company}}`
`{{required_sender_details_and_opt_out}}`

**Purpose:** Shift from the process hypothesis to the verified capability.
**Stop condition:** Any opt-out, negative response, suppression signal, or reply.

### Touch 3 — Day 9, email

**Subject:** Close the loop?

Hi `{{first_name}}`,

I’ll close the loop after this.

If routing approvals and keeping a decision history is something your operations team is reviewing, I can show how `{{product_name}}` handles that workflow. If it is not a priority—or I have the wrong person—no action is needed.

`{{sender_name}}`
`{{sender_company}}`
`{{required_sender_details_and_opt_out}}`

**Purpose:** Give the recipient a low-pressure final choice.
**Stop condition:** End the sequence after this message regardless of response; suppress immediately on any opt-out or negative signal.

## Personalization and fallbacks

| Field | Evidence status | Use | Approved fallback |
| --- | --- | --- | --- |
| `{{first_name}}` | Unknown until contact record is verified | Greeting only | “Hi there” only if approved for the channel and region |
| `{{company_name}}` | Unknown until account record is verified | Neutral company reference | Remove the company-specific sentence |
| Operations responsibility | Inferred from role | Role-level relevance | “I’m reaching out to operations teams…” |
| Current approval process | Unknown | Never state as fact | Use “if” or ask an open question |
| `{{sender_name}}`, `{{sender_company}}`, sender details, opt-out | Unknown | Required before sending | No fallback; do not send if incomplete |

Do not add customer names, quotes, account activity, integrations, savings, AI, rankings, enterprise trust, or competitive comparisons unless applicable evidence and approvals are added first.

## Upstream claim handoff

| Upstream claim | Evidence status | Approval status | Channel use | Limitation or hold reason |
| --- | --- | --- | --- | --- |
| Routes workflow approvals | Verified | Unknown | Adapt after product/brand approval | Capability only; do not imply realized outcomes |
| Records decision history | Verified | Unknown | Adapt after product/brand approval | Capability only; do not imply compliance or savings |
| Spreadsheet coordination is the buyer’s current problem | Hypothesis | Unknown | Conditional question only | No buyer interviews or account signal |
| “#1 AI approvals platform” | Unknown | Held | Hold | No ranking, category, AI, or competitive evidence |
| “Trusted by Fortune 500 companies” | Unknown | Held | Hold | No customers, permissions, or enterprise-trust proof |
| “Universal integrations” | Unknown | Held | Hold | No integration inventory or verification |
| “50% savings” | Unknown | Held | Hold | No measured outcome, benchmark, scope, or approval |

## Review before launch

| Review area | Applicability | Owner status | Claim or operation | Decision status |
| --- | --- | --- | --- | --- |
| Product | Required | Unknown | Exact scope of routing and decision-history capabilities | Proposed |
| Brand | Required | Unknown | Product description, sender representation, and tone | Proposed |
| Customer proof | Required | Unknown | Confirm that no customer or trust proof is implied | Proposed |
| Legal | Required | Unknown | Capability wording, claims, sender identification, and outreach requirements | Proposed |
| Privacy | Required | Unknown | Contact source, permitted use, access, retention, and personalization | Proposed |
| Security | Required | Unknown | Contact-data handling and confirmation that no security claim is implied | Proposed |
| Regional outreach | Required | Unknown | Lawful basis or consent, identification, unsubscribe, timing, and channel rules | Proposed |
| Suppression | Required | Unknown | Existing suppression check and immediate opt-out propagation | Proposed |
| Commercial | Required | Unknown | CTA, seller guidance, and absence of unapproved promises | Proposed |

Before launch, verify every contact record, region, sender identity, required disclosure, and opt-out mechanism. Do not send to anyone with an opt-out, negative response, or other suppression signal.

## Bounded message test

- **One variable:** Touch 1 opening: role-based approval-handoff framing versus the conditional spreadsheet-coordination hypothesis.
- **Controls:** Same operations-leader audience, channel, CTA, sender, delivery window, and follow-up schedule.
- **Success measure:** Qualified positive replies that confirm a relevant approval workflow and accept a fit conversation.
- **Failure signal:** No qualified progression after the agreed sample and review window.
- **Guardrail measure:** Opt-outs, complaints, negative replies, and misinterpretation of the capability claim.
- **Review timing status:** Unknown; set the sample, window, and owner before launch.

This sequence becomes sendable only after the required reviews and contact-level outreach checks are approved. Until then, it remains a proposed outbound artifact.
