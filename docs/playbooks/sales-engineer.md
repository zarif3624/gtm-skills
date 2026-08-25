# Sales Engineer Playbook

For sales engineers and solutions consultants running technical discovery, demos, validation plans, and proof reviews. This playbook turns buyer evidence into a bounded technical evaluation without treating a polished demo, pilot result, or internal claim as proof of production fit.

## Install

```bash
npx skills add zarif3624/gtm-skills --skill research-account --skill prepare-discovery --skill analyze-sales-call --skill prepare-demo --skill handle-objections --skill create-mutual-action-plan
```

Use only approved account material, transcripts, architecture notes, and product documentation. Remove credentials, access tokens, unnecessary personal data, customer data, and configuration details the intended audience should not access. Confirm recording, privacy, and data-use permissions before processing call or environment material.

## Before technical discovery - separate context from assumptions

Start with the account and the decision the buyer is trying to make:

```text
Use $research-account for [account] before technical discovery. Verify the company identity, current initiatives, and public technical context with direct sources and access dates. Keep technology, integration, security, scale, and ownership assumptions Inferred or Unknown unless evidence supports them.
```

Then create a short discovery plan:

```text
Use $prepare-discovery for a technical conversation with [attendees]. Define the decision this call should enable, three evidence-backed hypotheses at most, questions about the current workflow and constraints, disqualifying answers, and a useful next-step standard. Do not assume attendee authority or lead the buyer toward our preferred architecture.
```

The meeting owner must confirm the objective, actual attendees, material account facts, and which product or technical claims are approved before the call.

## After discovery - preserve what the buyer actually said

```text
Use $analyze-sales-call on this approved technical-discovery transcript. Separate buyer statements, seller claims, jointly accepted decisions, analyst inferences, constraints, objections, and next steps with source locators. Mark unsupported architecture, integration, scale, timeline, and ownership claims Unknown.
```

A transcript verifies that someone made a statement; it does not verify that the statement is technically true. Proposed owners, dates, environments, and tests stay Proposed until the buyer accepts them.

## Design the demo - show less, prove more

```text
Use $prepare-demo from the approved discovery evidence. Map each buyer outcome or question to the smallest product moment that can test it. Use fictional or explicitly approved data, include setup and fallback checks, and list every capability, availability, roadmap, performance, security, compliance, and integration claim that needs an authorized owner before presentation.
```

Demo evidence is not production proof. A scripted path, mock, sample dataset, or successful single run cannot establish production scale, reliability, security, implementation effort, or general availability.

## Handle technical objections without bluffing

```text
Use $handle-objections on the buyer's exact technical concerns. Separate the stated objection from possible meanings, ask clarifying questions, and answer only with approved evidence. Identify the artifact or authorized product, engineering, security, legal, privacy, or commercial owner needed for anything unresolved.
```

Do not hide limitations or turn an unsupported roadmap item, workaround, reference architecture, or internal benchmark into a commitment. A concern that remains unresolved is a valid result; so is a pause or no.

## Build a buyer-owned validation path

When the buyer wants deeper proof, draft the shared path rather than declaring a generic proof of concept:

```text
Use $create-mutual-action-plan to draft a technical validation plan for [account]. Start with buyer-owned proof criteria and the decision each criterion supports. Include only relevant environment, data, integration, performance, security, legal, procurement, and implementation reviews. Keep owners and dates Proposed or Unknown until the buyer accepts them, and define the evidence required to complete each milestone.
```

The buyer must be able to edit, accept, reject, or stop the plan. Do not call a seller-authored checklist mutual, and do not treat access to a test environment as authorization to inspect, copy, or change systems beyond the approved scope.

## The operating cadence

- **Before discovery:** use `$research-account` and `$prepare-discovery` to define the decision, hypotheses, and evidence gaps.
- **After each technical call:** use `$analyze-sales-call` to preserve claims, constraints, decisions, contradictions, and acceptance status.
- **Before a demo:** use `$prepare-demo` to bind the storyline to buyer outcomes and approved product evidence.
- **When concerns surface:** use `$handle-objections` to clarify the risk and route unsupported claims to an authorized owner.
- **For deeper validation:** use `$create-mutual-action-plan` for buyer-owned proof criteria, milestone evidence, dependencies, and stop paths.
- **At every handoff:** keep what is Verified, Inferred, Proposed, accepted, contradicted, and Unknown distinct.

Use the [evidence and status contract](../evidence-contract.md) when moving technical claims between discovery, call analysis, demo, objection, and validation artifacts. A clean handoff helps the AE, buyer, product team, and security reviewers challenge the same evidence without turning sales momentum into technical certainty.
