# Product Roadmap

The goal is not to become the largest prompt library. It is to become the most trustworthy, useful, and portable system for AI-assisted B2B sales work.

## North Star

A user should be able to give an agent imperfect real-world GTM context and receive a practical artifact that:

- keeps facts, inferences, and unknowns distinct;
- helps a buyer or seller make a better decision;
- exposes the next evidence needed instead of filling gaps with confidence;
- can move between tools without losing its meaning;
- is consistent enough for a team to inspect and improve.

## How We Will Measure Progress

| Dimension | Measure |
| --- | --- |
| Reliability | Pass rate across realistic eval cases and zero critical trust failures |
| Usefulness | Required artifact sections are complete, prioritized, and actionable |
| Evidence quality | Material claims are traceable and uncertainty is labeled |
| Portability | Every skill passes the repository and Agent Skills format checks |
| Adoption | A new user can install a skill and produce a first useful artifact in under 10 minutes |
| Maintainability | Every behavioral change adds or updates an eval case |

Targets are product goals, not claims about current performance. Publish measured results only after the evaluation harness can reproduce them.

## Current Status — 2026-08-08

The repository now has 25 focused skills, one isolated adversarial case per skill, ten cross-skill journey cases, a contrastive routing corpus, a dependency-free validation suite, a validated fictional workspace, and reproducible behavioral and blind-routing reports. The latest recorded routing run selected the exact intended skill set for all 27 prompts in its frozen corpus, and seven current behavioral scenarios pass in the recorded Codex lineage. These are bounded results tied to their frozen corpus and tested commits, not a claim that every model, client, or untested behavior passes.

The current product frontier is measured portability: run the same hidden cases across skills-compatible agents, publish raw-response evidence and scored reports, then use observed failures to prioritize skill changes.

Current compatibility claims and unknowns are tracked in the [compatibility evidence matrix](docs/compatibility.md).

## Phase 1: Make Quality Testable

- Strengthen structural, metadata, catalog, and resource validation.
- Add a realistic evaluation case and risk trap for every skill.
- Define a repeatable scoring protocol and regression-report format.
- Require validator tests and eval validation in continuous integration.
- Add explicit trust and partial-information checks to contribution review.

## Phase 2: Make Skills Consistent

- Standardize the shared evidence vocabulary and source format.
- Give each artifact explicit inputs, assumptions, decisions, actions, and handoff fields.
- Make partial-input behavior, stop conditions, and human-review points consistent.
- Test handoffs between adjacent skills, not only skills in isolation.
- Add machine-readable companion schemas where structured data creates clear value.

## Phase 3: Complete The Revenue Learning Loop

The first expansion set now includes sales-call analysis, win/loss analysis, positioning, territory planning, sales-process design, negotiation preparation, strategic account planning, partner-channel planning, customer-outcome review, and buyer business-case development. Further skills should be added only when a distinct job and adversarial evaluation justify the context and maintenance cost.

The next phase should test these workflows as a system: handoffs into qualification, coaching, positioning, ICP refinement, capacity review, deal governance, customer outcomes, and canonical pipeline attribution.

Every new skill must ship with UI metadata, at least one adversarial eval case, and any reusable template or reference needed to produce its artifact.

## Phase 4: Prove Portability And Operational Fit

- Publish tested end-to-end workflow examples using fictional data.
- Add opt-in reference packs for common CRM field models and CSV handoffs.
- Document import and export boundaries without making a CRM mandatory.
- Test installation, routing, and behavior across multiple skills-compatible agents and stable model lineages.
- Version releases and publish evidence-backed compatibility notes.

## Deliberate Non-Goals

- Hundreds of shallow or overlapping prompts.
- Automated prospecting that prioritizes volume over relevance and permission.
- Universal benchmarks, conversion assumptions, or qualification scores.
- Vendor-specific dependencies in the core skills.
- Claims that an agent replaces legal, security, finance, or sales leadership review.

## Near-Term Definition Of Done

The quality foundation is complete when:

- all current skills pass structural and metadata validation;
- all current skills have a realistic eval case with explicit failure traps;
- continuous integration runs validator unit tests, skill validation, and eval validation;
- contributors can reproduce the checks with one documented command;
- the README explains how to get a useful result with or without shared GTM context.
