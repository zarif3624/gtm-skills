# Routing Results

This directory stores raw blind-routing responses and their computed reports. A raw response uses the suffix `.response.json`; its matching report uses `.json`.

Freeze the live corpus before the run, then create a packet that does not expose expected or excluded skills:

```bash
python3 scripts/create_routing_snapshot.py 2026-08-08-v1
python3 scripts/create_routing_packet.py \
  --corpus evals/routing/corpora/2026-08-08-v1.json \
  --output /tmp/gtm-routing-packet.md
```

Give that packet to a clean client with the repository skills installed. Save its exact JSON response here, then create the report:

```bash
python3 scripts/create_routing_report.py \
  --agent "Agent name" \
  --model "Model identifier" \
  --lineage "stable-agent-model-lane" \
  --corpus evals/routing/corpora/2026-08-08-v1.json \
  --response evals/routing/results/2026-08-08.response.json \
  --output evals/routing/results/2026-08-08.json
```

The report is calculated from the immutable hidden-corpus snapshot and raw response. Never edit or reuse a snapshot after a run; create a new one when the live corpus changes. Use `--supersedes` to link the new report to the prior report in the same agent-and-model lineage, including when the corpus version changes. `pass` requires the exact smallest intended skill set for every case. Selecting extra non-excluded skills is `partial`; missing an expected skill or selecting an explicitly excluded neighbor is `fail`.

## Interpreting The Evidence

- A report is current only when it is the unsuperseded tip of its lineage.
- A current report is content-fresh only when its frozen corpus and the installed skill names and routing descriptions match its tested commit.
- Changing a request, expected route, excluded neighbor, skill name, or routing description requires a new blind run. A skill-body-only change does not invalidate routing evidence.
- Historical partial and failed runs stay committed. They show what changed and prevent a corrected corpus or skill description from erasing the earlier result.
- Compatibility claims are bounded to the recorded agent/model lineage, tested commit, and frozen corpus. They are not universal claims about every client or model.

The repository check validates the supersession graph, recomputes every score from the frozen corpus and raw selections, rejects stale current evidence, and requires a routing request for every ordered skill topology exercised by a behavioral journey. The generated [`quality-summary.json`](../../../quality-summary.json) distinguishes the current frontier from retained history.
