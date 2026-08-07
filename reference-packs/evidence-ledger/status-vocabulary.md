# Status Vocabulary And Transitions

## Evidence

| State | Meaning | Evidence needed to enter |
| --- | --- | --- |
| Verified | Direct support for the stated scope | Authoritative source, locator, and date |
| Reported | Attributed but not independently verified | Source identity or stable system record and locator |
| Inferred | Reasoned conclusion from cited evidence | Supporting evidence, reasoning, and material counterevidence |
| Hypothesis | Testable possibility | Rationale and falsifiable validation step |
| Unknown | Not supportable | None; record the smallest needed evidence |
| Contradicted | Material sources disagree | Both locators and the unresolved conflict |

Repetition never upgrades evidence. `Reported`, `Inferred`, and `Hypothesis` require new authoritative support to become `Verified`.

## Actions And Governance

- **Actor:** `Confirmed`, `Proposed`, or `Unknown`.
- **Timing:** `Confirmed`, `Proposed`, `Accepted`, or `Unknown`.
- **Buyer:** `Proposed`, `Accepted`, `Rejected`, `Completed`, or `Unknown`.
- **Approval:** `Approved`, `Proposed`, `Rejected`, or `Unknown`.
- **Completion:** `Completed`, `Not completed`, or `Unknown`.

Each axis needs its own source. A named actor does not confirm timing; buyer acceptance does not prove approval or completion; CRM entry does not prove any of them.

## Transformation

Use `Proposed`, `Approved`, `Rejected`, or `Unknown`. Preserve the original claim and source locator. A transformation status authorizes the stated mapping or calculation only; it does not verify the transformed claim's real-world truth.
