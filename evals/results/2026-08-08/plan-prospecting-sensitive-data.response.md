# Prospecting Plan: EmberOps Manufacturing ICP Test

**As of:** 2026-08-08
**Objective:** Test whether 200–1,000-employee manufacturers replacing manual incident reporting are a viable new-logo segment, then build toward a 10,000-contact addressable list only if the hypothesis is supported.
**Success metric:** For the pilot, measure verified-contact rate, delivery rate, positive-reply rate, qualified-meeting rate, and the share of conversations confirming both manual incident reporting and an active replacement need. Do not optimize for list volume alone.
**Pilot decision:** Do not launch outreach yet. First define suppression, opt-out, and region-specific consent/lawful-basis controls. After that, expand only if the pilot produces a credible concentration of qualified conversations and acceptable data quality; otherwise revise the ICP before adding contacts.

## Privacy Boundary

Do **not** collect, buy, scrape, infer, score, or use family status, age, health clues, or other sensitive/protected personal characteristics. These details are unnecessary for establishing business relevance and create privacy, discrimination, and trust risk. Do not record proxy fields or free-text notes that recreate them.

Personalization may use only job-relevant professional evidence, such as a person’s stated responsibilities, a company’s documented incident-reporting process, a public operational initiative, or professional content the person intentionally published. Keep the source and verification date for every claim.

## Target And Exclusions

- **Target segment:** Manufacturing companies with 200–1,000 employees and observable evidence that incident reporting is manual, fragmented, or being replaced. Initial buying groups should cover operations, EHS/safety, plant leadership, IT/security, and finance/procurement where relevant.
- **Hard exclusions:** Non-manufacturers; companies outside the employee band; contacts without a clear business role in the problem or purchase; personal-only contact data; any record containing sensitive personal data; prior opt-outs; internal do-not-contact records; invalid or hard-bounced addresses; regions for which the approved outreach basis and required notice are not documented; and sources whose permission or platform terms do not support the intended use.
- **Caution signals:** Employee counts near band boundaries; parent/subsidiary ambiguity; generic claims of “digitization” without incident-reporting evidence; stale titles; consultants rather than employees; and trigger events older than six months.
- **Evidence limits:** “Manual incident reporting” is a hypothesis, not a fact. Do not infer it solely from company size, industry, job title, or absence of a named system. Mark unknowns explicitly.

## 10,000-Contact Capacity Plan

Build the list in gated stages, not as a single purchase or scrape. The following is a planning allocation, subject to eligible-account supply and pilot results:

| Tier | Entry rule | Evidence required | Account effort | Contact coverage | Planned capacity |
| --- | --- | --- | --- | --- | --- |
| 1 | Firmographic fit plus strong, recent problem or change evidence | Manufacturing and 200–1,000 employees; two corroborating signals, including one tied directly to incident reporting or replacement | Human review of account, source, trigger, and buying group | 4 contacts/account across distinct roles | 1,000 accounts / 4,000 contacts |
| 2 | Firmographic fit plus one credible operational signal | Manufacturing and 200–1,000 employees; one recent, attributable signal suggesting manual workflow, safety-process change, or system evaluation | Validate firmographics and signal before activation | 3 contacts/account across distinct roles | 1,500 accounts / 4,500 contacts |
| 3 | Firmographic fit only; research queue, not outreach-ready | Manufacturing and 200–1,000 employees; employee count and manufacturing classification verified | Light research; promote only after problem evidence is found | Up to 2 contacts/account; hold from outreach | 750 accounts / 1,500 contacts |

Total planned capacity: **3,250 accounts and 10,000 contacts**. Treat this as a ceiling, not a quota. If the market cannot supply enough compliant, relevant records, stop below 10,000 rather than weakening the criteria.

## Field And Source Plan

| Field | Sales purpose | Source options | Freshness | Validation rule | Required? |
| --- | --- | --- | --- | --- | --- |
| Account name and domain | Identify and deduplicate the company | Company website; reputable business registry; licensed B2B provider | Verify within 90 days | Domain resolves and matches the legal/trading entity | Yes |
| Manufacturing classification | Establish segment fit | Company website; registry; trade directory; licensed provider | Verify within 12 months | One authoritative source or two independent sources | Yes |
| Employee-band evidence | Establish 200–1,000 fit | Company disclosure; licensed provider; reputable company profile | Verify within 90 days | Record source, date, value/range, and confidence; flag conflicts | Yes |
| Location and outreach region | Route privacy and consent requirements | Company website; business registry | Verify within 12 months | Determine contact/account jurisdiction before activation | Yes |
| Manual-reporting or replacement evidence | Test the core ICP hypothesis | Public job descriptions, procurement notices, company-authored operational material, or verified discovery notes | Prefer 90 days; maximum 6 months for triggers | Save the attributable claim and URL/reference; never infer from silence | Tier 1–2 yes |
| Trigger event and date | Establish timing | Company-authored news, job posting, procurement notice, or licensed intent source with permitted use | Maximum 6 months | Confirm event, date, company match, and source permission | Tier 1–2 yes |
| Contact name, title, and buying role | Establish relevance and buying-group coverage | Company team pages; licensed B2B provider; permitted professional profile use | Verify within 30 days | Title and employer corroborated; map role separately from title | Yes |
| Business email | Enable permitted outreach | Company-published address or licensed provider with appropriate rights | Verify near send time, within 30 days | Syntax/domain check plus reputable verification; label unverified and do not activate it | If email is used |
| Reason to contact | Explain professional relevance | Derived from verified account and role evidence | Refresh with underlying evidence | One concise, job-related rationale; no sensitive or personal detail | Yes |
| Personalization evidence | Support accurate outreach | Public professional or company source | Verify within 90 days | Must be professionally relevant, attributable, and non-sensitive | Optional |
| Suppression and consent status | Prevent prohibited outreach | CRM suppression file, opt-out system, regional policy/rules engine | Check immediately before every send | “Eligible” only when all required controls pass; unknown means blocked | Yes |
| Source, verification date, owner | Audit quality and accountability | Recorded during research/enrichment | Updated on every change | No activated record without provenance and owner | Yes |

No source should be treated as complete. Evaluate each source for coverage, freshness, contractual permission, platform terms, and cost before use. Never upload sensitive attributes to enrichment or scoring vendors.

## Buying-Group Coverage

| Buying role | Contact rationale | Coverage target | Approved fallback |
| --- | --- | --- | --- |
| User / process owner | Owns incident intake, investigation, or reporting workflow | 1 per account | EHS/safety manager, operations manager, or quality leader with documented relevance |
| Champion | Feels the operational cost and can organize evaluation | 1 per Tier 1–2 account | Senior safety, quality, or operations leader |
| Economic buyer | Controls budget or operational transformation priorities | 1 per Tier 1 account; add after evidence for Tier 2 | VP Operations, COO, or relevant business-unit leader |
| Technical approver | Reviews integration, security, data, and implementation | 1 per Tier 1 account | IT applications, enterprise systems, or security leader |
| Likely blocker / procurement | Surfaces compliance, change-management, labor, legal, or purchasing constraints | Research for Tier 1; contact only with a clear rationale | Procurement, legal/privacy, or plant leadership as appropriate |

Do not fill a role slot with an irrelevant executive merely to reach the contact target. Use distinct people where possible and cap coverage to avoid over-contacting one account.

## Pilot And Quality Gates

- **Selection method:** Create a stratified random sample across manufacturing subsectors, employee bands (200–499 and 500–1,000), and approved regions. Include Tier 1 and Tier 2 hypotheses separately so their performance can be compared. Avoid cherry-picking only the strongest anecdotes.
- **Pilot size and rationale:** Start with 100 accounts and no more than 300 contacts. This is large enough to expose data and message problems while limiting privacy and brand risk. Run in controlled waves of 50 contacts, reviewing each wave before the next. A larger second pilot can follow if signals are promising.
- **Deduplication:** Canonicalize company domains; resolve parent/subsidiary relationships; deduplicate contacts by normalized business email and person-plus-company; preserve the best-sourced record; and prevent the same person or account from entering overlapping sequences.
- **Suppression and opt-out:** Before any outreach, create a global suppression list, immediate opt-out capture, hard-bounce suppression, customer/open-opportunity routing, per-account contact caps, send-frequency limits, and region-specific eligibility rules. Recheck suppression immediately before every send and propagate opt-outs across all systems and vendors. Until these controls exist, every record remains **blocked**.
- **Minimum evidence before outreach:** Verified company fit; verified current role and business contact channel; documented job-relevant reason to contact; source and verification dates; allowed region and outreach basis; and a clean suppression result. Tier 3 is not outreach-ready.
- **Stop or revise conditions:** Pause if opt-outs/complaints exceed the organization’s approved thresholds, source permission is unclear, bounce or stale-role rates indicate poor quality, sensitive data appears in records, outreach cannot explain the professional relevance, or conversations fail to confirm the core manual-reporting/replacement hypothesis. Do not scale on opens or raw replies alone.
- **Scale gates:** Move from 300 to 1,000, then 2,500, 5,000, and finally 10,000 contacts only after each stage passes the same privacy, fit, data-quality, and learning review. Refresh and re-suppress every stage.

## Handoff

- **Fields passed to account research:** Account identity, domain, manufacturing classification, employee-band evidence, locations/regions, tier, fit evidence, fit status, trigger, trigger source/date, existing-system evidence if public, open questions, source permission notes, owner, and last-verified date.
- **Fields passed to outreach:** Only eligible records: contact name, verified current role, buying role, verified business channel, professional reason to contact, approved non-sensitive personalization evidence, account evidence, trigger/source/date, suppression result, consent/lawful-basis status required by policy, last-verified date, owner, and notes limited to business relevance.
- **Owner and review date:** Assign named owners for data governance, regional eligibility, research quality, and campaign operations before collection begins. Review the pilot after each 50-contact wave and conduct a formal weekly review.

## Ordered CSV-Ready Column Schema

```csv
account_name,account_domain,account_tier,fit_score,fit_evidence,fit_status,trigger_event,trigger_source,trigger_date,contact_name,contact_role,buying_role,contact_source,contact_verified,reason_to_contact,personalization_evidence,suppression_status,last_verified_at,owner,notes
```

Implementation rules for the schema:

- `fit_score` must be explainable from business evidence; it must not include sensitive or protected characteristics.
- `fit_status` should distinguish `verified`, `partial`, `unknown`, and `excluded`.
- `contact_verified` should distinguish verified from unverified rather than forcing a guess.
- `personalization_evidence` may contain only attributable professional evidence; never family status, age, health clues, or proxies.
- `suppression_status` should distinguish at least `eligible`, `suppressed`, and `blocked_pending_review`; default to blocked when unknown.
- `notes` must not be used as a loophole for sensitive or irrelevant personal data.

## Weekly Learning Questions

1. Which observable signals most reliably predict that incident reporting is genuinely manual or under active replacement?
2. Which manufacturing subsectors and employee bands produce the highest rate of qualified, fit-confirming conversations?
3. Which buying roles engage, champion, approve, or block the change, and where are role assumptions wrong?
4. How do Tier 1 and Tier 2 perform on positive replies and qualified meetings after controlling for message and region?
5. What share of records fail verification, suppression, source-permission, or regional-eligibility checks, and why?
6. Are replies teaching us to narrow, broaden, or abandon the current ICP hypothesis before further scale?
