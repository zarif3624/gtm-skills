#!/usr/bin/env python3
"""Compare a copied installation with the repository's source skill packages."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"


def inventory(root: Path, label: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not root.is_dir() or root.is_symlink():
        return {}, [f"{label} root must be a real directory: {root}"]
    files: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"{label} path must not be a symbolic link: {relative}")
        elif path.is_file():
            files[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return files, errors


def compare(source: Path, installed: Path) -> tuple[int, int, list[str]]:
    source_files, errors = inventory(source, "source")
    installed_files, installed_errors = inventory(installed, "installed")
    errors.extend(installed_errors)
    source_paths = set(source_files)
    installed_paths = set(installed_files)
    for path in sorted(source_paths - installed_paths):
        errors.append(f"installed tree is missing: {path}")
    for path in sorted(installed_paths - source_paths):
        errors.append(f"installed tree has an extra file: {path}")
    for path in sorted(source_paths & installed_paths):
        if source_files[path] != installed_files[path]:
            errors.append(f"installed file differs from source: {path}")
    skill_count = len({path.split("/", 1)[0] for path in source_paths})
    return skill_count, len(source_files), errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "installed_root",
        type=Path,
        help="copied project skill root, for example .agents/skills",
    )
    args = parser.parse_args(argv)
    try:
        skill_count, file_count, errors = compare(SOURCE, args.installed_root.resolve())
    except OSError as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    for error in errors:
        print(f"FAIL {error}")
    print(
        f"Compared {skill_count} source packages and {file_count} files; "
        f"{len(errors)} mismatches."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
