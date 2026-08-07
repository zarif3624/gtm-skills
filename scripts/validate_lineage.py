#!/usr/bin/env python3
"""Shared validation for report supersession graphs."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any


def field(report: dict[str, Any], dotted: str) -> Any:
    value: Any = report
    for part in dotted.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


def validate_lineage_graph(
    reports: dict[Path, dict[str, Any]],
    root: Path,
    *,
    identity_fields: tuple[str, ...],
) -> list[str]:
    """Require one acyclic supersession chain per comparison identity."""
    root = root.resolve()
    errors: list[str] = []
    predecessor: dict[Path, Path] = {}
    successors: dict[Path, list[Path]] = defaultdict(list)
    groups: dict[tuple[Any, ...], list[Path]] = defaultdict(list)

    for path, report in reports.items():
        groups[tuple(field(report, item) for item in identity_fields)].append(path)
        raw_prior = report.get("supersedes")
        if not raw_prior:
            continue
        prior = (root / raw_prior).resolve()
        predecessor[path] = prior
        successors[prior].append(path)
        if prior not in reports:
            errors.append(
                f"{path.relative_to(root)} supersedes a report that is absent or invalid"
            )

    for prior, children in successors.items():
        if len(children) > 1:
            names = ", ".join(
                str(path.relative_to(root)) for path in sorted(children)
            )
            errors.append(
                f"{prior.relative_to(root)} has multiple successors in one lineage: {names}"
            )

    for start in reports:
        seen: set[Path] = set()
        current = start
        while current in predecessor:
            if current in seen:
                errors.append(f"supersession cycle includes {current.relative_to(root)}")
                break
            seen.add(current)
            current = predecessor[current]

    superseded = set(successors)
    for identity, paths in groups.items():
        latest = [path for path in paths if path not in superseded]
        if len(latest) != 1:
            label = ", ".join(str(value) for value in identity)
            errors.append(
                f"lineage {label} must have exactly one latest report; found {len(latest)}"
            )
    return list(dict.fromkeys(errors))
