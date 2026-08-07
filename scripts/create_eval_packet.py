#!/usr/bin/env python3
"""Create a self-contained behavioral forward-test packet without hidden assertions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"


def find_definition(case_id: str) -> tuple[Path, dict[str, Any]]:
    matches = sorted((EVALS / "cases").glob(f"{case_id}.json"))
    matches.extend(sorted((EVALS / "journeys").glob(f"{case_id}.json")))
    if len(matches) != 1:
        raise ValueError(
            f"expected one evaluation definition named {case_id}; found {len(matches)}"
        )
    path = matches[0]
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("evaluation definition must be a JSON object")
    return path, value


def target_skills(definition: dict[str, Any]) -> list[str]:
    if isinstance(definition.get("skill"), str):
        return [definition["skill"]]
    skills = definition.get("skills")
    if isinstance(skills, list) and all(isinstance(item, str) for item in skills):
        return skills
    raise ValueError("evaluation definition must identify skill or skills")


def render_packet(definition: dict[str, Any]) -> str:
    skills = target_skills(definition)
    lines = [
        "# Blind Behavioral Forward Test",
        "",
        "Run this request in a clean context with only the target skill packages and their "
        "directly linked resources available. Return a finished user artifact. Do not inspect "
        "evaluation definitions, scoring assertions, preferred answers, prior responses, or "
        "reports.",
        "",
        f"**Target skills:** {', '.join(skills)}",
        "",
        "## User request",
        "",
        definition["prompt"],
        "",
        "## Supplied context",
        "",
    ]
    context = definition.get("context", [])
    if not isinstance(context, list) or not all(isinstance(item, str) for item in context):
        raise ValueError("evaluation context must be a list of strings")
    lines.extend(f"- {item}" for item in context)
    lines.extend(("", "Save the exact response unchanged before scoring.", ""))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_id", help="evaluation case or journey id")
    parser.add_argument("--output", type=Path, help="write the packet instead of stdout")
    args = parser.parse_args(argv)
    try:
        _path, definition = find_definition(args.case_id)
        packet = render_packet(definition)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(packet, encoding="utf-8")
            print(f"Created blind behavioral packet: {args.output}")
        else:
            print(packet, end="")
    except (OSError, ValueError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
