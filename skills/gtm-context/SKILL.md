---
name: gtm-context
description: "Create or update the shared sales and go-to-market context used by other GTM skills. Use when starting work on a product, documenting the sales motion, defining buyers and value, capturing proof and competition, or when repeated sales tasks lack reliable background. Produces `.agents/gtm-context.md`."
---

# GTM Context

Create the shared source of truth at `.agents/gtm-context.md`. Keep it factual, compact, and useful to sales work.

## Workflow

1. Check for `.agents/gtm-context.md`. If it exists, read it and ask what changed.
2. If it does not exist, inspect available product docs, CRM definitions, call notes, website copy, pricing, and customer evidence.
3. Draft from evidence before asking questions. Mark every unsupported claim as `Unknown` or `Hypothesis`.
4. Ask only for gaps that materially affect targeting, qualification, or deal execution.
5. Save the result using [the context template](assets/gtm-context-template.md).
6. On substantive updates, increment the document version and prepend a dated changelog entry.

## Evidence Rules

- Separate **Verified**, **Inferred**, and **Unknown** information.
- Preserve source links or internal source names for proof, customer language, and performance claims.
- Do not turn an aspiration into a customer fact.
- Do not store credentials, raw personal data, or confidential customer details in shared context.
- Treat frameworks as optional language, not evidence.
- Label suggested owners, dates, thresholds, and process definitions as `Proposed` or `Unknown` until an authoritative source confirms them.

## Minimum Useful Context

Capture enough to answer:

- What is being sold, to whom, and for which costly problem?
- What GTM motion and sales cycle are in use?
- Which roles use, champion, approve, buy, block, and implement?
- What observable signals indicate fit, pain, timing, and risk?
- What proof supports the value claims?
- Which alternatives and status-quo behaviors compete for the decision?
- What must never be claimed without validation?

## Output

After saving, summarize:

- strongest established facts;
- consequential unknowns;
- assumptions that should be tested next;
- sections changed in this version.

Do not block downstream work because context is incomplete. Make the uncertainty visible and continue.
