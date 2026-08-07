#!/usr/bin/env python3
"""Run every dependency-free repository quality check."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = (
    (sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"),
    (sys.executable, "scripts/scan_repository.py"),
    (sys.executable, "scripts/validate_skills.py"),
    (sys.executable, "scripts/build_catalog.py", "--check"),
    (sys.executable, "scripts/validate_evals.py"),
    (sys.executable, "scripts/validate_eval_reports.py"),
    (sys.executable, "scripts/validate_routing_reports.py"),
    (sys.executable, "scripts/validate_examples.py"),
    (sys.executable, "scripts/validate_reference_packs.py"),
    (sys.executable, "scripts/quality_summary.py", "--check"),
)


def main() -> int:
    for command in COMMANDS:
        print(f"\n==> {' '.join(command[1:])}", flush=True)
        completed = subprocess.run(command, cwd=ROOT, check=False)
        if completed.returncode:
            return completed.returncode
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
