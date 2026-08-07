#!/usr/bin/env python3
"""Create a blind routing packet without expected or excluded skill labels."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "evals" / "routing" / "cases.json"
SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_catalog import build_catalog


def render_packet(corpus: dict[str, Any], skills: list[dict[str, Any]]) -> str:
    lines = [
        "# Blind Skill Routing Run",
        "",
        "For each request below, select the smallest set of installed skills needed to "
        "complete it. Use only the installed skill metadata in this packet; do not open "
        "evaluation definitions or skill bodies. In `selected_skills`, use exact names from "
        "the installed metadata rather than request IDs. Return JSON with one top-level "
        "`selections` array. Each item must contain `id`, `selected_skills`, and a short "
        "`rationale`. Preserve the case order.",
        "",
        "## Installed skill metadata",
        "",
    ]
    for skill in skills:
        lines.extend((f"### {skill['name']}", "", skill["description"], ""))
    lines.extend(("## Requests", ""))
    for case in corpus["cases"]:
        lines.extend((f"### {case['id']}", "", case["prompt"], ""))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--corpus", type=Path, default=DEFAULT_CORPUS, help="routing corpus to blind"
    )
    parser.add_argument("--output", type=Path, help="write the packet instead of stdout")
    args = parser.parse_args(argv)
    try:
        corpus = json.loads(args.corpus.read_text(encoding="utf-8"))
        packet = render_packet(corpus, build_catalog()["skills"])
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(packet, encoding="utf-8")
        print(f"Created blind routing packet: {args.output}")
    else:
        print(packet, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
