# Proposed outbound plan: Operations leaders

**As of:** 2026-08-08
**Artifact status:** Proposed — copy-complete, but not cleared for launch
**Sequence goal:** Test whether operations leaders have a relevant approval-routing problem and earn a qualified conversation
**Channel and region:** Email; region unknown

The requested “#1 AI approvals platform,” “trusted by Fortune 500 companies,” “universal integrations,” and “50% savings” claims are not used. None is supported or approved. Repeating them would not make them valid, and this sequence should not be sent until the launch checks below are complete.

## Message hypothesis

- **Audience and responsibility:** Operations leaders responsible for workflow execution or oversight.
- **Verified reason to contact:** Role-level relevance only; there is no recipient- or account-level signal.
- **Problem hypothesis:** Some operations teams may coordinate approvals in spreadsheets or otherwise find decision history difficult to trace. This is a hypothesis, not an observed fact about any recipient.
- **Relevant value and approved proof:** The product routes workflow approvals and records decision history. No customer or outcome proof is available.
- **Important unknowns:** Current workflow, systems, integrations, product fit, buying priority, account relevance, region, consent or lawful basis, sender identity, and claim approvals.

## Evidence and personalization

| Field or claim | Evidence status | Approved use or fallback |
| --- | --- | --- |
| Product routes workflow approvals | Verified | State directly. |
| Product records decision history | Verified | State directly. |
| Spreadsheet coordination | Hypothesis | Use only as an explicit “if”; never assert it about the recipient. |
| Recipient name, company, and role | Unknown until record-level verification | Verify before use; if role is unverified, remove the role-specific opener. |
| Account workflow or intent signal | Unknown | Do not imply one. Use transparent segment-level relevance. |
| Customer proof or measured outcomes | Unknown | Omit. |
| “#1 AI approvals platform” | Unknown and unapproved | Hold pending a defined category, current independent ranking evidence, verified AI capability, scope, and claim approval. |
| “Trusted by Fortune 500 companies” | Unknown and unapproved | Hold pending applicable customer evidence, permission, scope, recency, and approval. |
| “Universal integrations” | Unknown and unapproved | Hold pending a current integration inventory, supported-system boundaries, testing evidence, and approval. |
| “50% savings” | Unknown and unapproved | Hold pending an approved metric definition, baseline, methodology, representative results, limitations, recency, and approval. |

## Sequence

### Touch 1 — Day 1 — Email

**Purpose:** Introduce the verified capability and test the problem hypothesis.

**Subject:** How {{company}} routes approvals

Hi {{first_name}},

I’m reaching out because you lead operations at {{company}}.

If approval handoffs are coordinated across spreadsheets or scattered tools, {{product_name}} may be relevant. It routes workflow approvals and records the decision history.

Would a 15-minute comparison with one of your current approval processes be useful?

Best,
{{sender_name}}
{{sender_company}}

If this isn’t relevant, reply “no thanks” and I’ll stop.

**Stop condition:** Any reply, opt-out, bounce, complaint, or suppression signal.

### Touch 2 — Day 4 — Email

**Purpose:** Offer a second reason to engage: traceable decision history.

**Subject:** Decision history for approvals

Hi {{first_name}},

One specific workflow {{product_name}} supports is routing an approval and recording its decision history.

If tracing approval decisions is relevant to your team, I can show the workflow using one process you choose. Worth a brief look?

Best,
{{sender_name}}

If not, reply “no thanks” and I’ll close this out.

**Stop condition:** Any reply, opt-out, bounce, complaint, or suppression signal.

### Touch 3 — Day 8 — Email

**Purpose:** Avoid assuming the current state and offer a low-friction evaluation.

**Subject:** A workflow to compare?

Hi {{first_name}},

I don’t want to assume spreadsheets are part of your approval process.

If you do have a workflow worth reviewing, I can send a simple outline of how {{product_name}} handles approval routing and decision history. Which process, if any, would be useful to compare?

Best,
{{sender_name}}

**Stop condition:** Any reply, opt-out, bounce, complaint, or suppression signal.

### Touch 4 — Day 13 — Email

**Purpose:** Close the sequence without manufactured urgency.

**Subject:** Close the loop?

Hi {{first_name}},

I’ll close this out after today.

If approval routing is on your radar, reply “workflow” and I’ll send a short outline. Otherwise, no action needed and I won’t follow up again.

Best,
{{sender_name}}

**Stop condition:** End the sequence after this message or immediately upon any earlier reply, opt-out, bounce, complaint, or suppression signal.

## Additional subject-line options

- Approval routing at {{company}}
- One approval process to compare
- How are approval decisions recorded?
- Workflow approval question

## Required personalization fields

| Field | Requirement | Fallback |
| --- | --- | --- |
| `{{first_name}}` | Verify against the permitted contact source. | Use “Hello” only if the channel and brand guidelines allow it. |
| `{{company}}` | Verify employer and spelling. | Remove the company reference. |
| Operations-leader opener | Verify the recipient’s current role and responsibility. | “I’m reaching out because approval workflows may be relevant to your work.” |
| `{{product_name}}` | Insert the approved product name. | No send until supplied. |
| `{{sender_name}}` and `{{sender_company}}` | Use the real, approved sender identity. | No fallback; do not send without accurate identification. |

## Review before launch

- Confirm product and brand approval for the two capability statements and final wording.
- Identify the recipient’s region and have a responsible human verify the lawful basis or consent, identification, contact-data use, unsubscribe requirements, quiet hours, and platform rules that apply. This is operational guidance, not a legal determination.
- Confirm suppression lists, opt-out propagation, bounce handling, complaint handling, reply monitoring, sending domain, frequency, and data-retention rules.
- Ensure “no thanks” replies are monitored and suppressed promptly; add an operable unsubscribe mechanism wherever required.
- Verify every recipient’s name, company, current role, source, and permitted use. Do not infer account pain or intent.
- Keep the four unsupported claims above out of all subjects, body copy, landing pages, call scripts, and follow-ups until evidence and authorized approval exist.
- Stop automation on any reply so a human can assess relevance and avoid contradictory follow-ups.

## Bounded message test

- **One variable:** Primary framing in Touch 1 — approval routing versus recorded decision history.
- **Controls:** Same verified operations-leader segment, channel, offer, sender, timing, number of touches, region, and measurement window.
- **Success measure:** Qualified positive replies that confirm a relevant approval workflow and accept a next step; track progression to a substantive conversation.
- **Failure signal:** No qualified progression after the predefined sample and review window.
- **Guardrails:** Opt-outs, negative replies, complaints, bounces, mistaken-role responses, and downstream disqualification.
- **Review timing status:** Proposed; sample size, window, owner, and thresholds must be set before launch.
- **Interpretation limit:** Test performance can rank the two supportable framings; it cannot validate the held leadership, AI, customer-trust, integration, or savings claims.
