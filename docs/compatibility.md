# Compatibility Evidence

The skills follow the [Agent Skills specification](https://agentskills.io/specification), but format conformance does not guarantee identical routing or behavior across clients and models. This matrix reports only what has been exercised.

**Last updated:** 2026-08-08

| Client or path | Discovery / installation evidence | Behavioral evidence | Current status |
| --- | --- | --- | --- |
| `skills` CLI against this repository | `npx -y skills add . --list` discovered all 22 skills locally | Not applicable | Verified locally on 2026-08-08 |
| Repository quality tools | CI exercises the dependency-free suite on the oldest and newest supported Python lines (3.10 and 3.14) | Local suite passed on Python 3.9.6; CI results remain authoritative for supported lines | Configured; verify the two CI jobs on every change |
| OpenAI Codex clean-context subagent | Skills loaded from their repository paths; one blind metadata-only run selected the exact intended minimal set for 25/25 routing requests with zero excluded neighbors | Five latest recorded behavioral scenarios pass, including pipeline→forecast, sparse forecast, source-injection, coaching, and customer-outcome risks; exact model identifier was unavailable | Limited positive evidence for the recorded lineage and commits; see [behavior history](../evals/results/) and [routing evidence](../evals/routing/results/) |
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

The repository scripts target supported CPython 3.10 through 3.14 and use only the standard library. The CI boundary jobs are the support claim; an incidental pass on an older local interpreter does not extend that support window.
