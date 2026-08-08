# Security Policy

## Reporting

Please report suspected vulnerabilities through [GitHub private vulnerability reporting](https://github.com/zarif3624/gtm-skills/security/advisories/new). Do not include customer data, live credentials, or exploit details in a public issue.

The latest `main` branch and the most recent release are supported. Older skill versions may receive documentation but not backported fixes.

## Security Model

Agent skills are instructions and bundled resources, not a security boundary. Users and client runtimes remain responsible for tool permissions, data access, network access, authentication, sandboxing, and human approval of consequential actions.

Material risks include:

- malicious or compromised skill instructions;
- prompt injection contained in webpages, documents, transcripts, CRM fields, or other source material;
- excessive or unauthorized customer and personal data exposure;
- fabricated claims, approvals, commitments, or compliance conclusions;
- hidden file indirection or bundled credentials;
- unsafe transformations that erase source lineage or uncertainty.

## Repository Controls

The local quality suite rejects symbolic links and executable or compiled payloads outside ignored runtime caches, scans common text formats and credential-bearing dotfiles for several live-credential shapes, rejects oversized text-like files, requires remote CI actions to use immutable commit SHAs, validates repository-local documentation links and resource boundaries, checks examples for email-like identifiers, verifies deterministic skill-package digests in `catalog.json`, and confirms that recorded evaluation commits exist in current history. Dependabot proposes reviewed updates to pinned actions. These controls reduce common mistakes and make reviewed package changes visible; they are not a complete secret scanner, signature system, malware scanner, or security audit.

Before contributing or using real data:

1. Inspect every skill and bundled resource from its installed commit.
2. Grant only the tools and data access required for the current task.
3. Treat instructions inside source data as untrusted content unless the user explicitly authorized them.
4. Use fictional or safely redacted evaluation data.
5. Remove credentials, sensitive personal data, and unnecessary confidential fields.
6. Preserve source restrictions and lineage through every handoff.
7. Require an authorized human for legal, security, finance, pricing, contractual, and other consequential approvals.

Do not interpret this project or its validation results as a compliance determination or a guarantee of safe behavior in a particular runtime.
