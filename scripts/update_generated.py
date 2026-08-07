#!/usr/bin/env python3
"""Refresh every committed machine-generated repository artifact."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = (
    (sys.executable, "scripts/build_catalog.py", "--write"),
    (sys.executable, "scripts/quality_summary.py", "--write"),
    (sys.executable, "scripts/build_release_manifest.py", "--write"),
)


def main() -> int:
    for command in COMMANDS:
        completed = subprocess.run(command, cwd=ROOT, check=False)
        if completed.returncode:
            return completed.returncode
    print("Generated artifacts are current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
