# Compatibility Evidence

The skills follow the [Agent Skills specification](https://agentskills.io/specification), but format conformance does not guarantee identical routing or behavior across clients and models. This matrix reports only what has been exercised.

**Last updated:** 2026-08-08

| Client or path | Discovery / installation evidence | Behavioral evidence | Current status |
| --- | --- | --- | --- |
| `skills` CLI against this repository | `npx -y skills add . --list` discovered all 21 skills locally | Not applicable | Verified locally on 2026-08-08 |
| OpenAI Codex clean-context subagent | Skills loaded from their repository paths for isolated tests | Latest recorded pipeline→forecast journey and sparse forecast case pass; exact model identifier was unavailable | Limited evidence; see [result history](../evals/results/) |
| Claude Code | Not recorded | Not recorded | Unknown / not yet tested |
| Cursor | Not recorded | Not recorded | Unknown / not yet tested |
| Windsurf | Not recorded | Not recorded | Unknown / not yet tested |
| Other Agent Skills clients | Not recorded | Not recorded | Unknown / test per client and version |

## Compatibility Protocol

For each client and model lineage:

1. Record client, version, model identifier, operating system, installation method, and skill commit.
2. Confirm that all expected skill names and descriptions are discoverable.
3. Run the contrastive routing corpus without revealing expected or excluded skills.
4. Run isolated behavioral cases and cross-skill journeys without revealing assertions.
5. Save raw responses and finalized evidence reports.
6. Publish failures as failures; do not infer compatibility from format validation alone.

Compatibility evidence expires when the client, model, skill commit, or installation mechanism materially changes. A prior pass is a baseline, not a permanent guarantee.
