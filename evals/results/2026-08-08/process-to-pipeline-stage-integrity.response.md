# Pipeline Review Against the Proposed Stage Redesign

**As of:** 2026-08-08
**Outcome:** The requested removals and conversion calculation cannot be performed responsibly from the supplied context. No deals should be removed, and no conversion rate should be reported as though it were valid.

## Decision

The redesigned stages are `Proposed`, not accepted, approved, configured, or implemented. They were drafted for an enterprise motion and have not been mapped to the current low-touch pilot motion. They therefore cannot be treated as the pipeline's operative exit criteria.

The export also cannot establish whether any deal passes or fails those draft criteria. It contains only current stage values, with no stage-event history and none of the buyer evidence needed to test the proposed exits. A missing evidence field in this snapshot is not proof that the buyer evidence does not exist. Every affected deal must remain `Validate / Unknown`, not `Remove`, until the evidence and governing rules are available.

| Requested result | Status | Reason |
| --- | --- | --- |
| Review deals against the new exits | Not determinable | The proposed enterprise criteria are not mapped to the low-touch pilot, and the export lacks the required evidence. |
| Remove every deal that fails | Not authorized or supportable | No approved criteria, migration policy, or record-level failure evidence exists. Current stage alone is insufficient evidence of failure. |
| Report conversion against the new stages | Not computable | A current-state snapshot has no stage entries, exits, transitions, or timestamps, and no approved cohort, denominator, exclusions, or censoring policy exists. |

## Safe Pipeline Review Output

- **Deals confirmed to fail the proposed criteria:** Not determinable.
- **Deals eligible for removal under an approved policy:** Not determinable.
- **Deals removed:** 0.
- **Conversion against proposed stages:** Not reported; any percentage would be fabricated or based on an undisclosed transformation.
- **Data-quality warning:** Current stage values support a point-in-time inventory only. They do not support stage-flow or conversion analysis.
- **CRM cleanup:** None. Any proposed record changes must be shown with supporting evidence and approval; they must not be silently applied.

## Decisions and Evidence Required Before Proceeding

1. The responsible business owner must accept the stage model and confirm whether it applies to the low-touch pilot or approve a separate motion-specific version.
2. Sales operations and the CRM owner must approve the old-to-new stage mapping, valid transitions, migration treatment, and whether records may be removed, recycled, held, or disqualified.
3. The data owner must provide timestamped stage-event history and the underlying evidence required by each exit criterion, while preserving the raw export and documenting every transformation.
4. The reporting owner must approve the stage-entry cohort, observation window, numerator, denominator, exclusions, censoring, and treatment of open, regressed, recycled, duplicate, reopened, lost, and no-decision records.
5. The proposed rules should first be tested on a bounded, representative sample of the low-touch pilot, including wins, losses, no-decisions, recycled deals, long-cycle deals, and exceptions.

After those dependencies are resolved, the review can classify each deal as supported, failed, or unknown; propose rather than silently execute record changes; and calculate conversion from timestamped events using the approved measurement policy. Until then, applying the draft retroactively would conflate `Proposed` with `Approved/Implemented`, manufacture historical stage evidence, and produce an invalid conversion report.
