# Compatibility Evidence

The skills follow the [Agent Skills specification](https://agentskills.io/specification), but format conformance does not guarantee identical routing or behavior across clients and models. This matrix reports only what has been exercised.

**Last updated:** 2026-08-08

| Client or path | Discovery / installation evidence | Behavioral evidence | Current status |
| --- | --- | --- | --- |
| `skills` CLI against this repository | `npx -y skills add . --list` discovered all 25 skills; an isolated `--copy` install preserved all 92 files across all 25 packages byte for byte | Not applicable | Verified locally on 2026-08-08; installation from a published tag remains a release check |
| Repository quality tools | CI exercises the dependency-free suite on the oldest and newest supported Python lines (3.10 and 3.14) | Local suite passed on Python 3.9.6, 3.10.0, and 3.12.7; CI results remain authoritative for Python 3.14 | Configured; verify the two CI jobs on every change |
| OpenAI Codex clean-context subagent | The latest self-contained blind packet exposed only installed names and descriptions; the evaluator selected the exact intended minimal set for 38/38 requests with zero excluded neighbors, covering every skill and all twelve journey topologies | All 37 current behavioral definitions pass: 25 isolated skill cases and 12 cross-skill journeys spanning the full catalog and its tested handoffs; exact model identifier was unavailable | Limited positive evidence for the recorded lineage, frozen corpora, and tested commits; see [behavior history](../evals/results/) and [routing evidence](../evals/routing/results/) |
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
