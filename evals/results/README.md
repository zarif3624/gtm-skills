# Evaluation Results

This directory stores reproducible, finalized forward-test evidence. Keep raw model responses in a run-specific subdirectory and keep their scored JSON reports beside them. Use only fictional or safely redacted inputs.

First create a blind packet and run it in a clean agent session:

```bash
python3 scripts/create_eval_packet.py forecast-sales-arbitrary-probability \
  --output /tmp/forecast-sales-forward-test.md
```

Create a scoring draft only after saving the exact response:

```bash
python3 scripts/create_eval_report.py forecast-sales-arbitrary-probability \
  --agent "Agent name" \
  --model "Model identifier" \
  --lineage "stable-agent-model-lane" \
  --response evals/results/2026-08-08/forecast-sales-arbitrary-probability.response.md \
  --output evals/results/2026-08-08/forecast-sales-arbitrary-probability.json
```

The command copies each hidden assertion into an unscored report. Score every item as `pass`, `partial`, or `fail`, and cite the smallest useful excerpt or location from the raw response. Then set the summary verdict from the scores:

- `pass` only when every assertion passes;
- `fail` when any assertion fails;
- `partial` otherwise.

Set `critical_failure` to `true` exactly when a prohibited-behavior assertion fails. Finalized reports cannot contain `unscored` items or empty evidence. `python3 scripts/check.py` validates their source case, metadata, raw-response link, scores, computed verdict, and critical-failure state.

For a rerun, pass `--supersedes` with the repository-relative path of the prior JSON report. A lineage is one stable agent-and-model comparison lane; do not supersede a result from a different lineage. Historical failures stay visible, while the validator reports the latest result for each case and lineage separately from the all-run history.

Do not write or save a preferred answer. A report records observed behavior and evidence; it does not reveal the assertions to the agent before the run.
