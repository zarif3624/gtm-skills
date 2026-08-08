# Contributing

Thanks for helping make AI-assisted sales more useful and trustworthy.

## Before You Start

- Open an issue for a new skill or a substantial workflow change.
- Keep each skill focused on one recognizable job.
- Do not submit copied proprietary playbooks, customer data, credentials, or confidential examples.
- Use fictional companies and contacts in examples.

## Add A Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Use lowercase letters, digits, and hyphens for the directory and `name`.
3. Include only `name` and `description` in YAML frontmatter.
4. Put detailed frameworks in `references/` and reusable output templates in `assets/`.
5. Keep `SKILL.md` below 500 lines.
6. Add the skill to the human catalog in `README.md`.
7. Add a fictional, adversarial case in `evals/cases/` that targets the most consequential failure mode.
8. Run `python3 scripts/update_generated.py` to refresh `catalog.json`, `quality-summary.json`, and `release-manifest.json`.
9. Run `python3 scripts/check.py`.

For a substantial behavior change, follow the [forward-test protocol](evals/README.md) and add a finalized evidence report when the result should be published.

## Quality Bar

A skill should:

- State when it triggers in the frontmatter description.
- Read `.agents/gtm-context.md` when shared context is relevant.
- Work with partial information and name important gaps.
- Separate verified facts, inferences, and unknowns.
- Produce a defined, practical artifact.
- Avoid unsupported benchmarks and universal claims.
- Preserve buyer agency and avoid deceptive or coercive tactics.
- Include edge cases, stop conditions, and human-review points where risk is meaningful.
- Stay tool-agnostic unless the skill is explicitly for one system.
- Include matching `agents/openai.yaml` metadata whose default prompt explicitly names the skill.
- Label operational control fields such as owners, dates, approvals, and buyer actions as confirmed, proposed, accepted, or unknown.
- Prefer milestone dependencies to arbitrary dates, and do not assume named internal functions exist.

Use the repository's [evidence and status contract](docs/evidence-contract.md) when adding labels, source fields, operational states, or handoffs.

## Pull Requests

Keep pull requests focused. Explain the user problem, show an example input and output, and note how you tested the skill. Do not include a preferred eval answer beside a case; preserve clean forward testing. By contributing, you agree that your work is licensed under the MIT License.

Generated catalog, quality-summary, and release-manifest changes must accompany the source change that caused them. Do not edit their counts, metadata, or hashes by hand.

The full check also compares every current behavioral report's tested commit with the present evaluation definition and target skill directories. If a definition or skill changes, forward-test and supersede every affected current case and journey report; unrelated repository changes do not invalidate the evidence.
