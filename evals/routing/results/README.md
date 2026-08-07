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

The report is calculated from the immutable hidden-corpus snapshot and raw response. Never edit or reuse a snapshot after a run; create a new one when the live corpus changes. `pass` requires the exact smallest intended skill set for every case. Selecting extra non-excluded skills is `partial`; missing an expected skill or selecting an explicitly excluded neighbor is `fail`.
