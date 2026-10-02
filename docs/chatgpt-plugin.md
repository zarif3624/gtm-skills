# ChatGPT Plugin Launch Candidate

This is a **skills-only release candidate**, not a published directory listing or a
claim that ChatGPT installation and behavior have passed. The existing Skills CLI
and Codex installation paths remain unchanged.

## Build the exact upload artifact

From the repository root with Python 3.10–3.14:

```bash
python3 scripts/update_generated.py
python3 scripts/check.py
python3 scripts/build_plugin.py
python3 scripts/build_plugin.py --check
```

The builder writes `dist/gtm-skills-0.1.9-rc.1.zip` and a matching `.zip.sha256`
sidecar. It performs no network calls, installs, sign-ins, or publication. It uses
sorted entries, fixed timestamps and permissions, and uncompressed ZIP storage
for byte-identical output across supported Python versions. `--check` builds twice
in memory without writing an archive. To choose a destination, pass `--output`.

**Upload the generated ZIP, not GitHub's source-code archive.** The upload has
`plugin.json` directly at its root, without an enclosing repository directory.
Source inputs are in [packaging/chatgpt](../packaging/chatgpt/).

## Payload and host adaptation

The archive contains:

- Root portable `plugin.json`, MIT `LICENSE`, and two original SVG icons
- All 25 skills, with every template, reference, and interface YAML resource
- `bundle-manifest.json`, recording canonical package hashes, the host-adapter
  hash, and SHA-256 values for every other archive entry

The builder allowlists the payload and rejects stale catalogs, unsafe paths,
symlinks, unsupported files, likely credentials, broken local resource links, and
active SVG content. It does not package repository history, local GTM context,
environment files, evaluation responses, examples, documentation, or test tools.
Secret-pattern checks are safeguards, not proof that content is safe to disclose;
review the complete archive before uploading it.

The canonical `skills/` source files remain byte-identical to their existing
behavioral evidence. In the **generated plugin only**, a version-controlled
[host adapter](../packaging/chatgpt/runtime-context.md) is inserted into each
`SKILL.md`. It makes project paths optional, accepts conversation or attached
context, provides a chat/file fallback, and prohibits unsupported persistence or
tool claims. The generated `gtm-context` description also describes its portable
output. All other source resource bytes and routing descriptions are preserved.

The adapter is part of the plugin's behavior. Existing Codex reports **do not**
validate the transformed package. Keep package checks, isolated adapter smoke
tests, actual client tests, and portal scans separate. See the
[compatibility matrix](compatibility.md) and [test plan](../packaging/chatgpt/TESTING.md).

## Prepared listing

The [source manifest](../packaging/chatgpt/plugin.json) contains:

- Display name: **GTM Skills**
- Subtitle: **Evidence-first sales workflows**
- Publisher label: **Zarif**, matching the existing repository license/profile
- Proposed category: **Productivity**
- Three starter prompts, capability labels, light/dark icons, and release notes
- Existing public repository and issue-tracker URLs

The portal's selected verified developer identity determines the published
publisher name. Confirm that it matches before submitting. No legal name, company,
verification status, email address, new privacy policy, or terms were invented.
Country availability is omitted for the publisher to review. No screenshot is
provided because no actual ChatGPT installation has been captured.

No `apps`, MCP server, hooks, credentials, authentication, or remote service is
included. Research and file operations rely on the host's available tools and the
user's authorized sources. Skills-only metadata does not require the four MCP
review URLs. If the portal asks for additional materials, use its findings and
current documentation rather than inventing a policy or test result.

## Next: test the installed package in ChatGPT

The documented local-marketplace route uses the ChatGPT desktop app. On a
computer with that app, create a **new disposable test workspace** and run from
the candidate checkout:

```bash
mkdir gtm-plugin-test-workspace
python3 -m zipfile -e dist/gtm-skills-0.1.9-rc.1.zip gtm-plugin-test-workspace/plugins/gtm-skills
mkdir -p gtm-plugin-test-workspace/.agents/plugins
cp packaging/chatgpt/marketplace.example.json gtm-plugin-test-workspace/.agents/plugins/marketplace.json
```

Open that workspace in Work mode or Codex in the ChatGPT desktop app, restart
the app, select **GTM Skills Local Test** in the Plugins Directory, and install
GTM Skills. Use a new chat for the [test plan](../packaging/chatgpt/TESTING.md).
The example marks the plugin available; it does not install it or create
credentials. Its authentication policy field is marketplace metadata; this
skills-only plugin has no authentication flow.

This setup has not been executed on the publisher's computer. If the local
source is unavailable on a particular client, record the client/version and
use its supported path rather than claiming that uploading a ZIP in a chat
installs a plugin. See [official local packaging guidance](https://developers.openai.com/plugins/build/plugins#build-your-own-curated-plugin-list).

For submission, the publisher must choose the owning organization/project and
its verified developer identity in the [Plugins portal](https://platform.openai.com/plugins).
An organization owner or member with **Apps Management Write** can submit.
Verify access and identity there before any upload; the directory publisher name
comes from that selected identity, not from this repository alone.

## Remaining launch gates

1. Review and merge the release-preparation PR only when authorized; verify both
   Python CI jobs on the exact proposed commit
2. Install the built candidate through a supported ChatGPT local/developer route
   in a new chat. Record client/model/version, exact ZIP hash, discovery, routing,
   resource loading, context reuse, and representative behavior
3. Confirm the owning OpenAI organization/project, verified developer identity,
   directory category, and intended availability with the publisher
4. With upload authorization, upload this ZIP to the [Plugins portal](https://platform.openai.com/plugins),
   wait for Metadata & Skills checks, and resolve required findings
5. Obtain the publisher's authorization for attestations, review submission, and
   eventual publication. These are separate from preparing a draft PR or ZIP
6. After approval, publish only when authorized and verify the real directory
   listing and installation. Record any new restrictions or differences

Skills-only packages do not need an MCP account, server, reviewer credentials,
or an MCP demo recording. Do not add unnecessary infrastructure for this launch.
The current submission flow cannot add MCP to an existing skills-only plugin;
consider that constraint before future product expansion.

## Official source basis

Reviewed 2026-10-02:

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Build skills](https://developers.openai.com/plugins/build/skills)
- [Upload and submit](https://developers.openai.com/plugins/deploy/submission)
- [Portable manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)

These sources support the chosen package format; successful local validation is
not a substitute for the dashboard's current checks or review.
