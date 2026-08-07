# Proposed Outbound Plan — RelayFox Operations Leaders

**Fictional example:** Yes
**As of:** 2026-08-08
**Sequence goal:** Test whether a verified operations leader has a relevant approval workflow and is open to a short comparison
**Channel and region:** Email; region unknown
**Artifact status:** Proposed; not approved to send

## Claim Handoff

| Upstream claim | Evidence status | Approval status | Channel use | Limitation or hold reason |
| --- | --- | --- | --- | --- |
| RelayFox routes workflow approvals | Verified | Proposed | Adapt | Product owner must confirm exact wording |
| RelayFox records decision history | Verified | Proposed | Adapt | No compliance, audit, or outcome implication |
| Operations teams coordinate approvals in spreadsheets | Reported at one fictional account | Proposed | Conditional hypothesis only | Not established for a recipient or segment |
| Delay, rework, cost, risk, integrations, security, or compliance outcomes | Unknown | Unknown | Hold | No applicable evidence or approval |

## Message Hypothesis

Operations leaders who oversee repeated approvals may care about defined routing or recorded decision history. There is no recipient-level signal, so outreach must state role-level relevance transparently and ask whether the workflow exists.

## Sequence

| Touch | Timing | Channel | Purpose | Copy | Stop condition |
| ---: | --- | --- | --- | --- | --- |
| 1 | Day 1 | Email | Test routing relevance | **Subject: A question about approval routing**\n\nHi {{first_name}},\n\nI’m reaching out because you lead operations at {{company}}. RelayFox routes workflow approvals and records decision history.\n\nIf a repeated approval process is difficult to coordinate, would comparing one current workflow be useful?\n\nBest,\n{{approved_sender}}\n\nIf this is not relevant, reply “no thanks” and I’ll stop. | Any reply, opt-out, bounce, complaint, or suppression signal |
| 2 | Day 5 | Email | Test decision-history relevance | **Subject: Recording approval decisions**\n\nHi {{first_name}},\n\nA second reason operations teams may examine an approval workflow is the decision history. RelayFox records decisions as approvals are routed.\n\nIs there one workflow where that would be worth evaluating?\n\nBest,\n{{approved_sender}} | Any reply, opt-out, bounce, complaint, or suppression signal |
| 3 | Day 10 | Email | Close without pressure | **Subject: Close the loop?**\n\nHi {{first_name}},\n\nI do not want to assume approval coordination is a priority for your team. If it is, reply with the workflow you would compare. Otherwise, no action is needed and I will close this out.\n\nBest,\n{{approved_sender}} | End sequence after this touch or any earlier stop signal |

## Personalization And Fallbacks

| Field | Evidence needed | Approved fallback |
| --- | --- | --- |
| `{{first_name}}` | Permitted, current contact source | Generic greeting only if brand and regional review allow it |
| `{{company}}` | Verified employer and spelling | Remove company reference |
| Operations responsibility | Verified current role | Use a transparent, broader role hypothesis |
| `{{approved_sender}}` | Accurate approved identity | No send |

## Review Before Launch

| Review area | Applicability | Owner status | Claim or operation | Decision status |
| --- | --- | --- | --- | --- |
| Product | Required | Unknown | Capability wording | Proposed |
| Brand | Required | Unknown | Copy, identity, and tone | Proposed |
| Customer proof | Required | Unknown | Confirm proof and outcomes remain omitted | Proposed |
| Legal | Unknown | Unknown | Claims and regional outreach requirements | Proposed |
| Privacy | Required | Unknown | Contact source, permitted use, retention | Proposed |
| Security | Unknown | Unknown | Sending systems and data access | Proposed |
| Regional outreach | Required | Unknown | Consent or lawful basis, identification, unsubscribe, timing | Proposed |
| Suppression | Required | Unknown | Opt-out propagation, reply, bounce, and complaint handling | Proposed |
| Commercial | Required | Unknown | Offer and sender guidance | Proposed |

## Bounded Test

- **One variable:** Touch 1 leads with approval routing versus recorded decision history.
- **Success measure:** Qualified replies that confirm a relevant workflow and accept a substantive comparison.
- **Guardrails:** Opt-outs, negative replies, complaints, bounces, mistaken-role responses, and downstream disqualification.
- **Interpretation:** The test may rank two supportable framings. It cannot validate held outcome, integration, security, compliance, or market claims.
