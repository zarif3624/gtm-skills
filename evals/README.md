# Evaluation Guide

The cases in `evals/cases/` test whether each skill remains useful under realistic ambiguity and pressure. The cases in `evals/journeys/` test whether evidence, uncertainty, decisions, and commitments keep their meaning across adjacent skills. They are intentionally fictional and focus on failure modes that structural validation cannot catch.

The contrastive corpus in `evals/routing/` tests whether natural requests select the intended skill and avoid a plausible neighboring skill. It includes both single-skill and composed-workflow prompts. Run routing tests without exposing expected or excluded skill names to the agent or router.

## Case Design

Every case defines:

- the skill and user prompt;
- the limited context available to the agent;
- the consequential risk being tested;
- behaviors the response must demonstrate;
- behaviors the response must avoid;
- decisions or claims that require human review.

A behavioral change to a skill should add or update the smallest case that would have caught the old behavior.

A handoff change should add or update a journey. Journey assertions focus on information that must survive the handoff and information that must never be upgraded from unknown, proposed, or reported into verified or accepted.

## Forward-Test Protocol

1. Generate a self-contained blind packet with `python3 scripts/create_eval_packet.py <case-id> --output <temporary-path>`.
2. Start a clean agent session with only the target skill packages and their directly linked resources available, then submit that packet without the source eval definition.
3. Save the raw response with the agent, model, date, and skill commit.
4. Score every assertion `Pass`, `Partial`, or `Fail` and cite response evidence.
5. Treat any prohibited behavior as a critical failure.
6. Revise the skill, then rerun the original case and at least one adjacent case to check for regressions.

The generated packet includes the exact prompt, context, and target skills but excludes the risk statement and assertions. Use `scripts/create_eval_report.py` only after saving the response, then store the finalized report and raw response under [`evals/results/`](results/). The repository check verifies that each report still matches its source assertions and that its summary follows the acceptance rule.

For routing, freeze the live corpus with `scripts/create_routing_snapshot.py`, generate a self-contained blind packet from that snapshot and the current installed-skill metadata, save the client's exact JSON selection, and create a computed report with `scripts/create_routing_report.py`. Store responses and reports under [`evals/routing/results/`](routing/results/) and immutable corpora under `evals/routing/corpora/`. The packet includes exact skill names and descriptions but excludes expected and neighboring-skill labels; the report validator joins those labels back only after the run. A later corpus change cannot rewrite an earlier result.

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

The local check validates case shape, one-case-per-skill coverage, and any finalized result reports. An eval definition alone does not claim that a model passed the behavioral evaluation.
