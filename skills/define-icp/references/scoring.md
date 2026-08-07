# ICP Scoring Guide

Use numerical scoring only when the evidence can support distinctions between accounts or segments. A score is a calibrated decision aid, not decoration for a hypothesis.

## Scoreability Gate

Before assigning points, weights, ranges, or cutoffs, establish:

- the decision the score controls and the cost of a false positive or false negative;
- observable criteria tied to problem fit, ability to realize value, company fit, timing, commercial fit, and relevant disqualifiers;
- a sufficiently varied set of wins, losses, no-decisions, activation, value, retention, and delivery outcomes for the intended scope;
- consistent definitions, source coverage, observation windows, and missing-data treatment;
- evidence that each proposed criterion separates useful outcomes rather than merely describing current customers;
- an authorized GTM owner for weights, thresholds, exceptions, and review timing.

If these conditions are not met, label the model `Not scoreable`. Use a qualitative fit table with `Required`, `Important`, `Exploratory`, or `Unknown` importance and a bounded validation plan. Do not convert unknowns into a numeric ceiling or neutral point value.

## Building A Supported Model

When the scoreability gate passes:

1. Derive candidate weights from applicable outcome evidence and document the rationale.
2. Hold out examples or use a prospective cohort to test whether the model discriminates outcomes.
3. Define missing-data behavior without rewarding missing evidence.
4. Separate hard disqualifiers from additive points.
5. Review false positives, false negatives, segment bias, delivery burden, and exceptions.
6. Have the authorized GTM owner approve the model before operational use.
7. Version the model and recalibrate it when the motion, product, evidence window, or outcome mix changes.

Do not import universal weights or tier thresholds. If a team supplies an existing model, report its source and approval status and audit it against actual outcomes before calling it calibrated.
