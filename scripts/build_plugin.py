#!/usr/bin/env python3
"""Build a minimal, deterministic skills-only plugin ZIP (no network or credentials)."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))
from build_catalog import build_catalog
from scan_repository import SECRET_PATTERNS, reject_duplicate_keys
from validate_skills import parse_frontmatter, local_links

CONFIG = "packaging/chatgpt"
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NUMERIC = r"(?:0|[1-9][0-9]*)"
PRERELEASE = r"(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
VERSION = re.compile(rf"^{NUMERIC}\.{NUMERIC}\.{NUMERIC}(?:-{PRERELEASE}(?:\.{PRERELEASE})*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_file(root: Path, relative: str) -> bytes:
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or "\\" in relative:
        raise ValueError(f"unsafe package path: {relative}")
    target = root
    for part in path.parts:
        target = target / part
        if target.is_symlink():
            raise ValueError(f"symbolic link is not allowed: {relative}")
    if not target.resolve().is_relative_to(root.resolve()) or not target.is_file():
        raise ValueError(f"missing or unsafe file: {relative}")
    data = target.read_bytes()
    if len(data) > 5 * 1024 * 1024:
        raise ValueError(f"file exceeds 5 MiB: {relative}")
    text = data.decode("utf-8")
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            raise ValueError(f"possible {label} in {relative}")
    return data


def validate_manifest(manifest: dict) -> None:
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be a JSON object")
    allowed = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}
    if set(manifest) - allowed or manifest.get("$schema") != SCHEMA:
        raise ValueError("manifest must use the portable skills-only format")
    if not NAME.fullmatch(manifest.get("name", "")) or len(manifest["name"]) > 64:
        raise ValueError("invalid plugin name")
    if not VERSION.fullmatch(manifest.get("version", "")):
        raise ValueError("an explicit semantic version is required")
    extensions = manifest.get("extensions")
    if not isinstance(extensions, dict) or not isinstance(extensions.get("com.openai"), dict):
        raise ValueError("OpenAI extension must be an object")
    extension = extensions["com.openai"]
    if set(extension) - {"interface", "onboardingSkill", "publication"}:
        raise ValueError("skills-only package must omit MCP review and hooks")
    interface = extension.get("interface")
    if not isinstance(interface, dict):
        raise ValueError("listing interface must be an object")
    for field, maximum in {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80, "category": 120}.items():
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip() or len(value) > maximum:
            raise ValueError(f"invalid listing field: {field}")
    prompts = interface.get("defaultPrompt", [])
    if not isinstance(prompts, list) or len(prompts) > 3 or any(not isinstance(p, str) or not p.strip() or len(p) > 128 for p in prompts):
        raise ValueError("invalid starter prompts")
    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if field in interface and (not isinstance(interface[field], str) or not interface[field].startswith("https://") or len(interface[field]) > 1024):
            raise ValueError(f"invalid HTTPS listing URL: {field}")
    for field in ("composerIcon", "logo"):
        if not isinstance(interface.get(field), str) or not interface[field].startswith("./assets/"):
            raise ValueError(f"missing package icon: {field}")


def adapt_skill(data: bytes, adapter: str, name: str) -> bytes:
    """Apply a visible, separately tested host adapter; never edit canonical skills."""
    text = data.decode("utf-8")
    fields, body, errors = parse_frontmatter(text)
    if errors or fields.get("name") != name:
        raise ValueError(f"invalid source skill: {name}")
    header = text.split("\n---\n", 1)[0]
    if name == "gtm-context":
        old = "Produces `.agents/gtm-context.md`."
        if header.count(old) != 1:
            raise ValueError("gtm-context description changed; review the host adapter")
        header = header.replace(old, "Produces shared GTM context in a document or the conversation.")
    title, rest = body.lstrip("\n").split("\n", 1)
    return (header + "\n---\n\n" + title + "\n\n" + adapter.strip() + "\n" + rest).encode("utf-8")


def validate_svg(data: bytes, name: str) -> None:
    svg = ElementTree.fromstring(data)
    if svg.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError(f"not an SVG icon: {name}")
    box = [float(v) for v in svg.attrib.get("viewBox", "").split()]
    if len(box) != 4 or not all(math.isfinite(v) for v in box) or box[2] != box[3] or box[2] < 48:
        raise ValueError(f"icon must be square and at least 48px: {name}")
    safe_tags = {"svg", "title", "rect", "path", "circle"}
    for item in svg.iter():
        if item.tag.rsplit("}", 1)[-1] not in safe_tags:
            raise ValueError(f"unsupported SVG element: {name}")
        if any(key.lower().startswith("on") or "href" in key.lower() or "url(" in value.lower() for key, value in item.attrib.items()):
            raise ValueError(f"active or external SVG content: {name}")


def package_files(root: Path = ROOT) -> dict[str, bytes]:
    manifest_bytes = read_file(root, f"{CONFIG}/plugin.json")
    manifest = json.loads(manifest_bytes, object_pairs_hook=reject_duplicate_keys)
    validate_manifest(manifest)
    skills_root = root / "skills"
    if skills_root.is_symlink() or not skills_root.is_dir():
        raise ValueError("skills directory must exist without symbolic links")
    for path in skills_root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"symbolic link is not allowed: {path.relative_to(root)}")
    catalog = json.loads(read_file(root, "catalog.json"))
    # Do not silently build a stale catalog, a changed resource, or an unreviewed extra file.
    if catalog != build_catalog(root):
        raise ValueError("catalog is stale; run scripts/update_generated.py and review changes")
    adapter = read_file(root, f"{CONFIG}/runtime-context.md").decode("utf-8")
    files = {"plugin.json": manifest_bytes, "LICENSE": read_file(root, "LICENSE")}
    sources = []
    for skill in catalog["skills"]:
        name = skill["name"]
        if not NAME.fullmatch(name) or skill["path"] != f"skills/{name}":
            raise ValueError("invalid catalog skill path")
        for relative in skill["files"]:
            path = PurePosixPath(relative)
            allowed = relative in {"SKILL.md", "agents/openai.yaml"} or (path.parts[0] in {"assets", "references"} and path.suffix in {".md", ".csv"} and not any(p.startswith(".") for p in path.parts))
            if not allowed:
                raise ValueError(f"file not allowlisted for skills-only packaging: {name}/{relative}")
            destination = f"skills/{name}/{relative}"
            data = read_file(root, destination)
            files[destination] = adapt_skill(data, adapter, name) if relative == "SKILL.md" else data
        sources.append({"name": name, "canonical_package_sha256": skill["package_sha256"]})
    interface = manifest["extensions"]["com.openai"]["interface"]
    for field in ("composerIcon", "composerIconDark", "logo", "logoDark"):
        if field not in interface:
            continue
        destination = interface[field]
        if not destination.startswith("./assets/") or not destination.endswith(".svg"):
            raise ValueError(f"unsupported icon path: {field}")
        destination = destination[2:]
        data = read_file(root, f"{CONFIG}/{destination}")
        validate_svg(data, destination)
        files[destination] = data
    onboarding = manifest["extensions"]["com.openai"].get("onboardingSkill", "")
    if onboarding and (not onboarding.startswith("./skills/") or onboarding[2:] not in files):
        raise ValueError("onboarding skill is not in the package")
    # Validate actual archive-relative resource links, not repository-relative lookalikes.
    for name, data in files.items():
        if name.endswith(".md"):
            for link in local_links(data.decode("utf-8")):
                if link == "URL":  # Document template placeholder, not a bundled resource.
                    continue
                target = PurePosixPath(name).parent / link
                if ".." in target.parts or str(target) not in files:
                    raise ValueError(f"unpackaged resource link in {name}: {link}")
    provenance = {
        "schema_version": 1,
        "canonical_catalog_sha256": digest(read_file(root, "catalog.json")),
        "host_adapter_sha256": digest(adapter.encode("utf-8")),
        "canonical_skills": sources,
        "files": [{"path": name, "sha256": digest(data)} for name, data in sorted(files.items())],
        "evidence_scope": "Canonical repository behavioral reports do not validate these adapted plugin skills. ChatGPT installation, routing, behavior, and portal scans must be tested separately."
    }
    files["bundle-manifest.json"] = (json.dumps(provenance, indent=2) + "\n").encode()
    return files


def archive_bytes(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    # Stored entries avoid platform/zlib-version differences and keep the ZIP reproducible.
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(files.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    return buffer.getvalue()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="ZIP destination; defaults to dist/name-version.zip")
    parser.add_argument("--check", action="store_true", help="validate and verify deterministic bytes without writing")
    args = parser.parse_args(argv)
    try:
        files = package_files()
        data = archive_bytes(files)
        if data != archive_bytes(package_files()):
            raise ValueError("package rebuild was not deterministic")
        manifest = json.loads(files["plugin.json"])
        if not args.check:
            output = args.output or ROOT / "dist" / f"{manifest['name']}-{manifest['version']}.zip"
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
            output.with_suffix(".zip.sha256").write_text(f"{digest(data)}  {output.name}\n", encoding="utf-8")
            print(f"Built {output}")
        print(f"PASS plugin package: {len(files)} files, {len(data)} bytes, SHA-256 {digest(data)}")
    except (OSError, ValueError, KeyError, TypeError, IndexError, ElementTree.ParseError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
