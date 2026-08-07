# Sales Process Design Methods

## Buyer State Before Seller Activity

A useful stage represents a decision-relevant state, such as a problem being validated, solution fit being tested, or commercial approval being pursued. A seller activity can support that state but should not establish it by itself. `Discovery call held` is an event; it is not proof that a problem, priority, or decision path exists.

## Stage Contract

For each stage define:

- buyer or decision state;
- entry evidence and its source;
- work performed while in the stage;
- exit evidence;
- allowed next, previous, hold, recycle, disqualified, duplicate, loss, and no-decision transitions;
- minimum fields and who uses them;
- exception and approval path;
- measurement timestamps.

Prefer a small number of distinct states. If adjacent stages share the same evidence and actions, test whether they should be combined.

## Evidence And Fields

Every required field needs:

- a decision or workflow that consumes it;
- a definition, type, source, and permitted unknown state;
- a collection or update moment;
- ownership and access status;
- a retention or sensitivity consideration when applicable.

Calculated scores and probabilities must preserve their inputs, formula version, as-of date, and calibration scope. A score does not replace the underlying evidence.

## Measurement

Use event history rather than only the current record. Define:

- stage entry cohort and observation window;
- numerator, denominator, exclusions, and censoring;
- motion, segment, source, owner, and time coverage;
- how regressions, recycling, duplicates, reopened deals, no-decisions, and still-open records are treated.

Do not compare conversion or cycle time across incompatible cohorts. When data is incomplete, report coverage and design the next measurement instead of inserting a benchmark.

## Governance And Rollout

Separate design, acceptance, approval, configuration, migration, training, adoption, and enforcement. Test the process on representative wins, losses, no-decisions, disqualifications, long-cycle deals, and exceptions. Define who may change stages, fields, automation, and reporting, and how a change is versioned and communicated.

A pilot should have a bounded scope, baseline, success and failure signals, feedback channel, review dependency, and rollback or revision path. Do not invent a calendar date when readiness depends on unresolved decisions.
