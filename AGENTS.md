# Repository Guide

This repository contains portable Agent Skills for B2B sales and GTM work.

When changing a skill:

1. Read its `SKILL.md`; read linked resources when they govern the change. Do not load every skill or reference for unrelated work.
2. Keep YAML frontmatter to `name` and `description`.
3. Preserve the evidence-first rules in the root README.
4. Keep descriptions short and specific to the requested artifact or decision. Keep essential evidence and approval boundaries in the skill; load detailed methods by task. Preserve portable behavior across clients and models.
5. Use fictional data in examples.
6. Use `docs/architecture.md` for the affected release and evaluation requirements. Run `python3 scripts/validate_skills.py` for skill changes. Documentation-only edits need affected-link and diff checks, not unrelated behavioral runs.

Complete authorized edits through relevant verification and report any remaining release gate. Do not claim historical evaluations validate a changed skill package. Use focused checks while iterating, and retain the required full release checks before publication.

Do not add generated CRM exports, prospect lists, personal data, secrets, or vendor credentials.
