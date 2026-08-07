# Evidence And Action Ledger Pack

This vendor-neutral pack turns the repository's evidence and status contract into portable CSV and JSON record shapes. Use it when claims, actions, approvals, or commitments must move between skills, agents, spreadsheets, CRMs, or internal tools without becoming stronger through repetition.

## Files

- [evidence ledger template](evidence-ledger-template.csv) and [evidence record schema](evidence-record.schema.json) preserve claims, source locators, scope, transformations, validation, and access classification;
- [action ledger template](action-ledger-template.csv) and [action record schema](action-record.schema.json) keep actor, timing, buyer, approval, and completion status on separate axes;
- [status vocabulary](status-vocabulary.md) defines the allowed states and transition evidence.

## Minimum Safe Workflow

1. Keep immutable source material outside the ledger and record a stable locator.
2. Create one claim or action per row. Do not combine statements with different sources or statuses.
3. Preserve subject, scope, source date, and as-of date; the same sentence may have a different status for another scope or time.
4. Record transformations separately. Never overwrite the source claim with a normalized or calculated output.
5. Use `Unknown` rather than empty certainty. A nullable field means the value was not supplied, not that it is false or zero.
6. Keep proposed owners and timing distinct from confirmed ownership, buyer acceptance, approval, and completion.
7. Restrict access to the source and ledger consistently. Do not export credentials, unnecessary personal data, or confidential free text.
8. Require a cited acceptance, approval, completion, or verification source before strengthening a status.

The schemas validate record shape, not truth. Teams remain responsible for source access, definitions, transformation review, retention, and authorization.
