#!/usr/bin/env python3
"""Validate structure, metadata, resources, and repository contracts for all skills."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"\]\(([^)]+)\)")
OPENAI_FIELD_RE = re.compile(r'^  ([a-z_]+): "([^"]*)"$')
RESOURCE_DIRS = ("assets", "references", "scripts")
REQUIRED_INTERFACE_FIELDS = {"display_name", "short_description", "default_prompt"}
BARE_CONTROL_FIELD_RE = re.compile(r"\|\s*(Owner|Date|Deadline|Approval)\s*\|", re.IGNORECASE)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    """Parse this repository's intentionally simple, single-line YAML frontmatter."""
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["missing opening YAML delimiter"]
    try:
        raw, body = text[4:].split("\n---\n", 1)
    except ValueError:
        return {}, text, ["missing closing YAML delimiter"]

    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in fields:
            errors.append(f"duplicate frontmatter field: {key}")
        fields[key] = value.strip().strip('"').strip("'")
    return fields, body, errors


def parse_openai_yaml(path: Path) -> tuple[dict[str, str], list[str]]:
    """Parse and validate the small interface-only metadata format used here."""
    if not path.is_file():
        return {}, ["missing agents/openai.yaml"]

    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if not lines or lines[0] != "interface:":
        return {}, ["agents/openai.yaml must start with interface:"]

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        match = OPENAI_FIELD_RE.fullmatch(line)
        if not match:
            errors.append(f"invalid or unquoted interface line: {line}")
            continue
        key, value = match.groups()
        if key in fields:
            errors.append(f"duplicate interface field: {key}")
        fields[key] = value
    return fields, errors


def local_links(text: str) -> list[str]:
    """Return local Markdown link targets, excluding URLs, anchors, and mail links."""
    links: list[str] = []
    for raw_target in MARKDOWN_LINK_RE.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        target = target.split("#", 1)[0]
        if not target or target.startswith(("#", "mailto:")) or "://" in target:
            continue
        links.append(target)
    return links


def validate_resources(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    skill_root = path.resolve()
    linked = set(local_links(text))

    for relative in linked:
        target = (path / relative).resolve()
        if not target.is_relative_to(skill_root):
            errors.append(f"local resource link escapes skill directory: {relative}")
        elif not target.exists():
            errors.append(f"broken local resource link: {relative}")

    for folder_name in RESOURCE_DIRS:
        folder = path / folder_name
        if not folder.exists():
            continue
        if not folder.is_dir():
            errors.append(f"{folder_name} must be a directory")
            continue
        for resource in sorted(item for item in folder.rglob("*") if item.is_file()):
            relative = resource.relative_to(path).as_posix()
            if relative not in linked and relative not in text:
                errors.append(f"unreferenced bundled resource: {relative}")
            if folder_name == "assets" and resource.suffix.lower() == ".md":
                asset_text = resource.read_text(encoding="utf-8")
                bare_field = BARE_CONTROL_FIELD_RE.search(asset_text)
                if bare_field:
                    errors.append(
                        f"ambiguous {bare_field.group(1).lower()} field in {relative}; "
                        "include confirmed, proposed, accepted, or unknown status"
                    )
    return errors


def validate_interface(path: Path, skill_name: str) -> list[str]:
    fields, errors = parse_openai_yaml(path / "agents" / "openai.yaml")
    if set(fields) != REQUIRED_INTERFACE_FIELDS:
        errors.append(
            "agents/openai.yaml interface must contain exactly display_name, "
            "short_description, and default_prompt"
        )
    if fields.get("display_name") and len(fields["display_name"]) > 64:
        errors.append("display_name must be 64 characters or fewer")
    short_description = fields.get("short_description", "")
    if short_description and not 25 <= len(short_description) <= 64:
        errors.append("short_description must contain 25-64 characters")
    default_prompt = fields.get("default_prompt", "")
    if default_prompt and f"${skill_name}" not in default_prompt:
        errors.append(f"default_prompt must explicitly mention ${skill_name}")
    return errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_file = path / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    fields, body, frontmatter_errors = parse_frontmatter(text)
    errors.extend(frontmatter_errors)

    if set(fields) != {"name", "description"}:
        errors.append("frontmatter must contain exactly name and description")
    if fields.get("name") != path.name:
        errors.append("name must match its directory")
    name = fields.get("name", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append("name must be 1-64 lowercase letters, digits, and hyphens")
    description = fields.get("description", "")
    if not 20 <= len(description) <= 1024:
        errors.append("description must contain 20-1024 characters")
    if description and "use " not in description.lower():
        errors.append("description must say when to use the skill")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md must remain below 500 lines")
    if "TODO" in text or "[TODO" in text:
        errors.append("unresolved TODO marker")
    if not re.search(r"^# [^#]", body, re.MULTILINE):
        errors.append("body must contain one top-level title")
    if not re.search(r"^## Output\b", body, re.MULTILINE):
        errors.append("body must define an Output section")
    if not re.search(r"\b(?:Do not|Never)\b", body, re.IGNORECASE):
        errors.append("body must include at least one explicit trust guardrail")
    if name != "gtm-context" and ".agents/gtm-context.md" not in body:
        errors.append("skill must read shared .agents/gtm-context.md when available")

    errors.extend(validate_resources(path, text))
    errors.extend(validate_interface(path, name))
    return list(dict.fromkeys(errors))


def validate_catalog(skill_dirs: list[Path]) -> list[str]:
    if not README.is_file():
        return ["README.md is missing"]
    text = README.read_text(encoding="utf-8")
    errors: list[str] = []
    for skill_dir in skill_dirs:
        link = f"(skills/{skill_dir.name}/)"
        if text.count(link) != 1:
            errors.append(f"README catalog must link {skill_dir.name} exactly once")
    return errors


def validate_document_links(path: Path, repository_root: Path) -> list[str]:
    """Validate local links in repository-facing Markdown documents."""
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    root = repository_root.resolve()
    for relative in local_links(text):
        target = (path.parent / relative).resolve()
        if not target.is_relative_to(root):
            errors.append(f"{path.name} link escapes repository: {relative}")
        elif not target.exists():
            errors.append(f"{path.name} has broken local link: {relative}")
    return errors


def validate_repository_docs() -> list[str]:
    documents = list(ROOT.glob("*.md"))
    documents.extend((ROOT / ".github").rglob("*.md"))
    documents.extend((ROOT / "evals").glob("*.md"))
    errors: list[str] = []
    for document in sorted(set(documents)):
        errors.extend(validate_document_links(document, ROOT))
    return errors


def run_validation() -> tuple[dict[str, list[str]], list[str]]:
    if not SKILLS.is_dir():
        return {}, ["skills directory is missing"]
    skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    if not skill_dirs:
        return {}, ["no skills found"]
    results = {skill_dir.name: validate_skill(skill_dir) for skill_dir in skill_dirs}
    repository_errors = validate_catalog(skill_dirs)
    repository_errors.extend(validate_repository_docs())
    return results, repository_errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit machine-readable results")
    args = parser.parse_args(argv)

    results, repository_errors = run_validation()
    failed = sum(bool(errors) for errors in results.values()) + bool(repository_errors)
    if args.json:
        print(
            json.dumps(
                {"skills": results, "repository": repository_errors, "ok": failed == 0},
                indent=2,
                sort_keys=True,
            )
        )
    else:
        for name, errors in results.items():
            print(f"{'FAIL' if errors else 'PASS'} {name}")
            for error in errors:
                print(f"  - {error}")
        if repository_errors:
            print("FAIL repository")
            for error in repository_errors:
                print(f"  - {error}")
        print(f"\nValidated {len(results)} skills; {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
