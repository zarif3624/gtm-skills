# Compatibility Evidence

The skills follow the [Agent Skills specification](https://agentskills.io/specification), but format conformance does not guarantee identical routing or behavior across clients and models. This matrix reports only what has been exercised.

**Last updated:** 2026-09-11

| Client or path | Discovery / installation evidence | Behavioral evidence | Current status |
| --- | --- | --- | --- |
| Skills CLI `1.5.25` against published tag `v0.1.7` | `npx -y skills@1.5.25 add zarif3624/gtm-skills@v0.1.7 --skill '*' --copy --yes` installed all 25 skills; the comparator matched 25 packages and 92 files byte for byte at commit `e683fbb32ea4e8b68c702c1f274d6d6561c49d90` | Not applicable | Verified from the public tag in a disposable Git project on macOS 26.6.2 arm64 on 2026-09-11; installation evidence only |
| Official skills-ref `0.1.0` | [`agentskills/agentskills` skills-ref](https://github.com/agentskills/agentskills/tree/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref) at commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379` validated all 25 packages from tag `v0.1.7` | Format validation does not establish behavioral compatibility | Verified on Python 3.12.7 and macOS 26.6.2 arm64 on 2026-09-11; reference-validator conformance only |
| Repository quality tools | CI exercises the dependency-free suite on the oldest and newest supported Python lines (3.10 and 3.14) | Local suite passed on Python 3.9.6, 3.10.0, and 3.12.7; CI results remain authoritative for Python 3.14 | Configured; verify the two CI jobs on every change |
| OpenAI Codex clean-context subagent | The latest self-contained blind packet exposed only installed names and descriptions; the evaluator selected the exact intended minimal set for 38/38 requests with zero excluded neighbors, covering every skill and all twelve journey topologies | All 37 current behavioral definitions pass: 25 isolated skill cases and 12 cross-skill journeys spanning the full catalog and its tested handoffs; exact model identifier was unavailable | Limited positive evidence for the recorded lineage, frozen corpora, and tested commits; see [behavior history](../evals/results/) and [routing evidence](../evals/routing/results/) |
| Claude Code | Not recorded | Not recorded | Unknown / not yet tested |
| Cursor | Not recorded | Not recorded | Unknown / not yet tested |
| Windsurf | Not recorded | Not recorded | Unknown / not yet tested |
| Other Agent Skills clients | Not recorded | Not recorded | Unknown / test per client and version |

## Reproduce The Snapshot

Run these commands from an empty disposable directory. The install check uses the public tag and compares the copied package tree with that exact checkout:

```bash
git clone https://github.com/zarif3624/gtm-skills.git
git -C gtm-skills checkout v0.1.7
mkdir install-check
git -C install-check init
(
  cd install-check
  DISABLE_TELEMETRY=1 npx -y skills@1.5.25 add zarif3624/gtm-skills@v0.1.7 --skill '*' --copy --yes
)
python3 gtm-skills/scripts/compare_installed_skills.py install-check/.agents/skills
```

The reference-validator environment pins both the upstream implementation and the dependency versions observed in this run:

```bash
git clone https://github.com/agentskills/agentskills.git
git -C agentskills checkout 69ef37e9424c0a7ea9dd2293b559e43ec8176379
python3.12 -m venv skills-ref-venv
skills-ref-venv/bin/pip install click==8.5.0 python-dateutil==2.9.0.post0 six==1.17.0 strictyaml==1.7.3
skills-ref-venv/bin/pip install --no-deps -e agentskills/skills-ref
for skill in gtm-skills/skills/*; do
  skills-ref-venv/bin/skills-ref validate "$skill"
done
```

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
