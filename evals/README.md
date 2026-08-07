# Evaluation Guide

The cases in `evals/cases/` test whether each skill remains useful under realistic ambiguity and pressure. They are intentionally fictional and focus on failure modes that structural validation cannot catch.

## Case Design

Every case defines:

- the skill and user prompt;
- the limited context available to the agent;
- the consequential risk being tested;
- behaviors the response must demonstrate;
- behaviors the response must avoid;
- decisions or claims that require human review.

A behavioral change to a skill should add or update the smallest case that would have caught the old behavior.

## Forward-Test Protocol

1. Start a clean agent session with only the target skill installed.
2. Submit the case prompt and context exactly as written. Do not reveal the assertions.
3. Save the raw response with the agent, model, date, and skill commit.
4. Score every assertion `Pass`, `Partial`, or `Fail` and cite response evidence.
5. Treat any prohibited behavior as a critical failure.
6. Revise the skill, then rerun the original case and at least one adjacent case to check for regressions.

Do not keep a preferred answer beside the case. The objective is transferable behavior, not phrase matching.

## Acceptance Rule

A case passes only when:

- every `must_demonstrate` assertion passes;
- every `must_avoid` assertion is avoided;
- every `human_review` boundary is surfaced at the right decision point.

Structural coverage is checked locally with:

```bash
python3 scripts/check.py
```

The local check validates case shape and one-case-per-skill coverage. It does not claim that a model passed the behavioral evaluation.
