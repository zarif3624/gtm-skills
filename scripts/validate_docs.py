#!/usr/bin/env python3
"""Validate repository-local Markdown links across documentation and skill resources."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXCLUDED_PARTS = {".git", "__pycache__", "node_modules"}


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file() and not set(path.relative_to(root).parts) & EXCLUDED_PARTS
    )


def local_target(raw: str) -> str | None:
    value = raw.strip()
    if not value or value == "URL" or value.startswith(("#", "http://", "https://", "mailto:", "data:")):
        return None
    if value.startswith("<") and ">" in value:
        value = value[1 : value.index(">")]
    elif " \"" in value:
        value = value.split(" \"", 1)[0]
    value = value.split("#", 1)[0].split("?", 1)[0]
    return unquote(value) if value else None


def validate_file(path: Path, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if path.is_symlink():
        return ["Markdown file must not be a symbolic link"]
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target_value = local_target(raw)
        if target_value is None:
            continue
        if target_value.startswith("/"):
            errors.append(f"repository link must be relative: {raw}")
            continue
        unresolved = path.parent / target_value
        target = unresolved.resolve()
        if unresolved.is_symlink():
            errors.append(f"repository link traverses a symbolic link: {raw}")
        elif not target.is_relative_to(root.resolve()):
            errors.append(f"repository link escapes the repository: {raw}")
        elif not target.exists():
            errors.append(f"repository link target does not exist: {raw}")
    return errors


def main() -> int:
    files = markdown_files(ROOT)
    failures = 0
    for path in files:
        errors = validate_file(path)
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
    print(f"\nValidated local links in {len(files)} Markdown files; {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
