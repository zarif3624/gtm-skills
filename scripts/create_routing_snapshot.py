#!/usr/bin/env python3
"""Freeze the current routing corpus for one reproducible evaluation run."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "evals" / "routing" / "cases.json"
CORPORA = ROOT / "evals" / "routing" / "corpora"
SNAPSHOT_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot_id", help="lowercase, hyphenated immutable snapshot id")
    args = parser.parse_args(argv)
    if not SNAPSHOT_RE.fullmatch(args.snapshot_id):
        print("FAIL snapshot id must use lowercase letters, digits, and hyphens", file=sys.stderr)
        return 1
    destination = CORPORA / f"{args.snapshot_id}.json"
    if destination.exists():
        print(f"FAIL snapshot already exists: {destination}", file=sys.stderr)
        return 1
    try:
        corpus = json.loads(CURRENT.read_text(encoding="utf-8"))
        CORPORA.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(corpus, indent=2) + "\n", encoding="utf-8")
    except (OSError, json.JSONDecodeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    print(f"Created immutable routing snapshot: {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
