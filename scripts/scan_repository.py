#!/usr/bin/env python3
"""Scan repository text and paths for common accidental supply-chain risks."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"}
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".csv", ".txt", ".toml"}
SENSITIVE_TEXT_NAMES = {".env", ".npmrc", ".pypirc", ".netrc"}
MAX_TEXT_BYTES = 1_000_000
SECRET_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,255}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "GitLab token": re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}\b"),
    "npm token": re.compile(r"\bnpm_[A-Za-z0-9]{36,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "Stripe secret": re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{20,}\b"),
}


def repository_paths(root: Path) -> tuple[list[Path], list[str]]:
    files: list[Path] = []
    errors: list[str] = []
    for current, dirs, names in os.walk(root, followlinks=False):
        current_path = Path(current)
        child_dirs = sorted(dirs)
        dirs[:] = []
        for name in child_dirs:
            directory = current_path / name
            if directory.is_symlink():
                errors.append(
                    f"symbolic link is not allowed: {directory.relative_to(root).as_posix()}"
                )
            elif name not in SKIP_DIRS:
                dirs.append(name)
        for name in sorted(names):
            path = current_path / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                errors.append(f"symbolic link is not allowed: {relative}")
            elif (
                path.suffix.lower() in TEXT_SUFFIXES
                or name in SENSITIVE_TEXT_NAMES
                or name.startswith(".env.")
            ):
                files.append(path)
    return files, errors


def scan_text(path: Path, root: Path) -> list[str]:
    if path.stat().st_size > MAX_TEXT_BYTES:
        return [
            f"text-like file exceeds {MAX_TEXT_BYTES} bytes: "
            f"{path.relative_to(root).as_posix()}"
        ]
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [f"text-like file is not valid UTF-8: {path.relative_to(root).as_posix()}"]
    errors: list[str] = []
    for label, pattern in SECRET_PATTERNS.items():
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            errors.append(
                f"possible {label}: {path.relative_to(root).as_posix()}:{line}"
            )
    return errors


def scan_repository(root: Path = ROOT) -> tuple[int, list[str]]:
    files, errors = repository_paths(root)
    for path in files:
        errors.extend(scan_text(path, root))
    return len(files), errors


def main() -> int:
    file_count, errors = scan_repository()
    for error in errors:
        print(f"FAIL {error}")
    print(f"\nScanned {file_count} text files; {len(errors)} risks found.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
