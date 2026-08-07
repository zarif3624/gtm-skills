# Routing Results

This directory stores raw blind-routing responses and their computed reports. A raw response uses the suffix `.response.json`; its matching report uses `.json`.

Create a packet that does not expose expected or excluded skills:

```bash
python3 scripts/create_routing_packet.py --output /tmp/gtm-routing-packet.md
```

Give that packet to a clean client with the repository skills installed. Save its exact JSON response here, then create the report:

```bash
python3 scripts/create_routing_report.py \
  --agent "Agent name" \
  --model "Model identifier" \
  --lineage "stable-agent-model-lane" \
  --response evals/routing/results/2026-08-08.response.json \
  --output evals/routing/results/2026-08-08.json
```

The report is calculated from the hidden corpus and raw response. `pass` requires the exact smallest intended skill set for every case. Selecting extra non-excluded skills is `partial`; missing an expected skill or selecting an explicitly excluded neighbor is `fail`.
