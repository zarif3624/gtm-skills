#!/usr/bin/env python3
"""Build or verify a deterministic release index for packages and current evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "release-manifest.json"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def latest_reports(
    reports: dict[Path, dict[str, Any]], root: Path
) -> list[tuple[Path, dict[str, Any]]]:
    superseded = {
        (root / report["supersedes"]).resolve()
        for report in reports.values()
        if report.get("supersedes")
    }
    return sorted(
        ((path, report) for path, report in reports.items() if path not in superseded),
        key=lambda item: item[0].as_posix(),
    )


def build_manifest(root: Path = ROOT) -> dict[str, Any]:
    root = root.resolve()
    catalog_path = root / "catalog.json"
    summary_path = root / "quality-summary.json"
    catalog = load_json(catalog_path)

    behavior_paths = sorted((root / "evals" / "results").rglob("*.json"))
    behavior_reports = {path.resolve(): load_json(path) for path in behavior_paths}
    routing_paths = sorted((root / "evals" / "routing" / "results").glob("*.json"))
    routing_reports = {
        path.resolve(): load_json(path)
        for path in routing_paths
        if not path.name.endswith(".response.json")
    }

    behavior = []
    for path, report in latest_reports(behavior_reports, root):
        response_path = root / report["run"]["response_path"]
        behavior.append(
            {
                "case_id": report["case_id"],
                "case_type": report["case_type"],
                "lineage": report["run"]["lineage"],
                "verdict": report["summary"]["verdict"],
                "repository_commit": report["run"]["repository_commit"],
                "report_path": path.relative_to(root).as_posix(),
                "report_sha256": sha256(path),
                "response_path": report["run"]["response_path"],
                "response_sha256": sha256(response_path),
            }
        )

    routing = []
    for path, report in latest_reports(routing_reports, root):
        corpus_path = root / report["corpus_path"]
        response_path = root / report["run"]["response_path"]
        routing.append(
            {
                "lineage": report["run"]["lineage"],
                "verdict": report["summary"]["verdict"],
                "total_cases": report["summary"]["total_cases"],
                "exact_matches": report["summary"]["exact_matches"],
                "repository_commit": report["run"]["repository_commit"],
                "corpus_path": report["corpus_path"],
                "corpus_sha256": sha256(corpus_path),
                "report_path": path.relative_to(root).as_posix(),
                "report_sha256": sha256(path),
                "response_path": report["run"]["response_path"],
                "response_sha256": sha256(response_path),
            }
        )

    return {
        "schema_version": 1,
        "generated_artifacts": {
            "catalog": {"path": "catalog.json", "sha256": sha256(catalog_path)},
            "quality_summary": {
                "path": "quality-summary.json",
                "sha256": sha256(summary_path),
            },
        },
        "skill_packages": [
            {
                "name": skill["name"],
                "path": skill["path"],
                "package_sha256": skill["package_sha256"],
            }
            for skill in catalog["skills"]
        ],
        "current_evidence": {"behavioral": behavior, "routing": routing},
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", action="store_true", help="update release-manifest.json")
    action.add_argument("--check", action="store_true", help="fail when the manifest is stale")
    args = parser.parse_args(argv)
    try:
        rendered = json.dumps(build_manifest(), indent=2) + "\n"
        if args.write:
            MANIFEST_PATH.write_text(rendered, encoding="utf-8")
            print(f"Updated {MANIFEST_PATH.relative_to(ROOT)}")
        elif args.check:
            if MANIFEST_PATH.read_text(encoding="utf-8") != rendered:
                print(
                    "FAIL release-manifest.json is stale; run "
                    "scripts/build_release_manifest.py --write"
                )
                return 1
            print("PASS release-manifest.json")
        else:
            print(rendered, end="")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
