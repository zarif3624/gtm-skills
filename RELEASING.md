# Release Process

A release is a reviewed compatibility statement, not just a tag.

## Prepare

1. Choose the version and move relevant `Unreleased` entries in [CHANGELOG.md](CHANGELOG.md) under that version and date.
2. Confirm the working tree contains only intended release changes.
3. Run `python3 scripts/update_generated.py`, review the catalog metadata, package digests, evidence counts, and release manifest, then commit the generated changes.
4. Run `python3 scripts/check.py`.
5. Run `DISABLE_TELEMETRY=1 npx -y skills add . --list` and confirm every catalog skill is discovered.
6. Run current routing and behavioral cases for each client/model lineage whose compatibility will be claimed.
7. Update the [compatibility evidence matrix](docs/compatibility.md) with versions, commits, and limitations.
8. Inspect raw evaluation responses for confidential or personal data before publishing.

## Review

- Confirm the README skill count, catalog, quickstart, reference packs, and local links.
- Confirm `release-manifest.json` binds the current `catalog.json` package digests to `quality-summary.json`, `quality-policy.json`, behavioral definition coverage, current-corpus routing coverage, eval definitions, example workspaces, reference packs, and SHA-256 digests for the latest reports, raw responses, and routing corpora.
- Confirm each new or materially changed skill has an adversarial case and a clean-context forward test.
- Confirm the evidence-freshness check finds no current report whose target skill content changed after its tested commit.
- Confirm current results are distinguishable from historical failures.
- Confirm `quality-policy.json` still expresses the intended release floor; lowering a threshold requires explicit review and rationale.
- Confirm no legal, security, compliance, model, or cross-client claim exceeds the recorded evidence.
- Review the repository security scan and bundled resources from the release commit.

## Publish

1. Merge the reviewed release commit to `main`.
2. Create an annotated semantic version tag from that exact commit.
3. Publish release notes from the matching changelog section.
4. Re-run installation from the tag rather than the working tree.
5. Record any installation or behavior regression against the tagged commit.

Do not rewrite a published tag. Correct a bad release with a new patch version and an explicit changelog entry.
