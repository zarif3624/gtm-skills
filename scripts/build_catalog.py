#!/usr/bin/env python3
"""Build or verify the machine-readable skill catalog and package digests."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validate_skills import parse_frontmatter, parse_openai_yaml


def package_digest(path: Path) -> tuple[str, list[str]]:
    digest = hashlib.sha256()
    files = sorted(
        item for item in path.rglob("*") if item.is_file() and not item.is_symlink()
    )
    relative_files: list[str] = []
    for item in files:
        relative = item.relative_to(path).as_posix()
        relative_files.append(relative)
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest(), relative_files


def build_catalog(root: Path = ROOT) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for skill in sorted(path for path in (root / "skills").iterdir() if path.is_dir()):
        frontmatter, _body, frontmatter_errors = parse_frontmatter(
            (skill / "SKILL.md").read_text(encoding="utf-8")
        )
        interface, interface_errors = parse_openai_yaml(skill / "agents" / "openai.yaml")
        errors = frontmatter_errors + interface_errors
        if errors:
            raise ValueError(f"cannot catalog {skill.name}: {'; '.join(errors)}")
        digest, files = package_digest(skill)
        entries.append(
            {
                "name": frontmatter["name"],
                "description": frontmatter["description"],
                "display_name": interface["display_name"],
                "short_description": interface["short_description"],
                "default_prompt": interface["default_prompt"],
                "path": f"skills/{skill.name}",
                "files": files,
                "package_sha256": digest,
            }
        )
    return {"schema_version": 1, "skills": entries}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", action="store_true", help="update catalog.json")
    action.add_argument("--check", action="store_true", help="fail when catalog.json is stale")
    args = parser.parse_args(argv)
    try:
        rendered = json.dumps(build_catalog(), indent=2) + "\n"
        if args.write:
            CATALOG_PATH.write_text(rendered, encoding="utf-8")
            print(f"Updated {CATALOG_PATH.relative_to(ROOT)}")
        elif args.check:
            if CATALOG_PATH.read_text(encoding="utf-8") != rendered:
                print("FAIL catalog.json is stale; run scripts/build_catalog.py --write")
                return 1
            print("PASS catalog.json")
        else:
            print(rendered, end="")
    except (OSError, ValueError, KeyError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
