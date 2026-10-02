from __future__ import annotations

import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import shutil
import stat
import tempfile
import unittest
import zipfile
from pathlib import Path, PurePosixPath
from unittest import mock
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_plugin", ROOT / "scripts/build_plugin.py")
assert SPEC and SPEC.loader
PLUGIN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PLUGIN)
from validate_skills import local_links, parse_frontmatter, validate_skill


def sha256(data: bytes) -> str:
    """An independent checksum oracle, rather than the builder's digest helper."""
    return hashlib.sha256(data).hexdigest()


def source_files(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted((root / "skills").rglob("*"))
        if path.is_file()
    }


class PluginFixture(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for directory in ("skills", "packaging/chatgpt"):
            shutil.copytree(ROOT / directory, self.root / directory)
        for name in ("LICENSE", "catalog.json"):
            shutil.copyfile(ROOT / name, self.root / name)

    @property
    def manifest_path(self) -> Path:
        return self.root / "packaging/chatgpt/plugin.json"

    def manifest(self) -> dict:
        return json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def write_manifest(self, value: object) -> None:
        self.manifest_path.write_text(json.dumps(value) + "\n", encoding="utf-8")

    def refresh_catalog(self) -> None:
        (self.root / "catalog.json").write_text(
            json.dumps(PLUGIN.build_catalog(self.root), indent=2) + "\n", encoding="utf-8"
        )

    def append_skill(self, text: str) -> None:
        path = self.root / "skills/research-account/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + text, encoding="utf-8")
        self.refresh_catalog()


class GeneratedPluginTests(PluginFixture):
    def test_exact_25_skills_and_92_source_files_with_only_five_package_files(self) -> None:
        sources = source_files(self.root)
        files = PLUGIN.package_files(self.root)
        self.assertEqual(len(sources), 92)
        self.assertEqual(len({name.split("/")[1] for name in sources}), 25)
        self.assertEqual(
            set(files) - set(sources),
            {"plugin.json", "LICENSE", "assets/icon.svg", "assets/icon-dark.svg", "bundle-manifest.json"},
        )
        self.assertEqual(set(sources) - set(files), set())
        self.assertEqual(len(files), 97)
        self.assertEqual(files["plugin.json"], self.manifest_path.read_bytes())
        self.assertEqual(files["LICENSE"], (self.root / "LICENSE").read_bytes())

    def test_build_preserves_every_source_byte_and_all_unadapted_payloads(self) -> None:
        before = source_files(self.root)
        files = PLUGIN.package_files(self.root)
        PLUGIN.archive_bytes(files)
        self.assertEqual(source_files(self.root), before)
        changed = set()
        for name, source in before.items():
            with self.subTest(path=name):
                if name.endswith("/SKILL.md"):
                    self.assertNotEqual(files[name], source)
                    changed.add(name)
                else:
                    self.assertEqual(files[name], source)
        self.assertEqual(len(changed), 25)

    def test_adapter_is_inserted_once_after_each_title_without_body_rewrites(self) -> None:
        files = PLUGIN.package_files(self.root)
        adapter = (self.root / "packaging/chatgpt/runtime-context.md").read_text(encoding="utf-8").strip()
        for name, source in source_files(self.root).items():
            if not name.endswith("/SKILL.md"):
                continue
            with self.subTest(path=name):
                original_fields, original_body, errors = parse_frontmatter(source.decode("utf-8"))
                actual_fields, actual_body, actual_errors = parse_frontmatter(files[name].decode("utf-8"))
                self.assertEqual(errors + actual_errors, [])
                self.assertEqual(set(actual_fields), {"name", "description"})
                self.assertEqual(actual_fields["name"], original_fields["name"])
                title, rest = original_body.lstrip("\n").split("\n", 1)
                self.assertEqual(actual_body, "\n" + title + "\n\n" + adapter + "\n" + rest)
                self.assertEqual(actual_body.count(adapter), 1)
                if original_fields["name"] == "gtm-context":
                    old = "Produces `.agents/gtm-context.md`."
                    new = "Produces shared GTM context in a document or the conversation."
                    self.assertTrue(original_fields["description"].endswith(old))
                    self.assertEqual(actual_fields["description"], original_fields["description"][:-len(old)] + new)
                else:
                    self.assertEqual(actual_fields, original_fields)

    def test_host_adapter_states_required_fallbacks_and_honest_capabilities(self) -> None:
        adapter = (self.root / "packaging/chatgpt/runtime-context.md").read_text(encoding="utf-8")
        for phrase in (
            "Shared GTM context is optional",
            "the relevant context already provided in the conversation",
            "Do not claim to have read a path or attachment you cannot access",
            "only when a writable project workspace is available",
            "never claim persistent storage or cross-chat memory without a successful save",
            "A missing local file is not a prerequisite failure",
            "Other named GTM skills are optional handoffs",
            "Drafting an artifact does not authorize sending outreach or changing source systems",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, adapter)

    def test_all_archive_relative_markdown_resources_are_bundled(self) -> None:
        files = PLUGIN.package_files(self.root)
        checked = 0
        for name, data in files.items():
            if not name.endswith(".md"):
                continue
            for link in local_links(data.decode("utf-8")):
                if link == "URL":
                    continue
                with self.subTest(source=name, target=link):
                    target = PurePosixPath(name).parent / link
                    self.assertFalse(target.is_absolute())
                    self.assertNotIn("..", target.parts)
                    self.assertIn(str(target), files)
                    checked += 1
        self.assertGreater(checked, 25)

    def test_extracted_generated_skills_pass_skill_validator(self) -> None:
        files = PLUGIN.package_files(self.root)
        with tempfile.TemporaryDirectory() as directory:
            extracted = Path(directory)
            with zipfile.ZipFile(io.BytesIO(PLUGIN.archive_bytes(files))) as archive:
                for name in archive.namelist():
                    self.assertFalse(PurePosixPath(name).is_absolute())
                    self.assertNotIn("..", PurePosixPath(name).parts)
                archive.extractall(extracted)
            skills = sorted((extracted / "skills").iterdir())
            self.assertEqual(len(skills), 25)
            for skill in skills:
                with self.subTest(skill=skill.name):
                    self.assertEqual(validate_skill(skill), [])

    def test_integrity_manifest_binds_every_payload_and_all_canonical_sources(self) -> None:
        files = PLUGIN.package_files(self.root)
        integrity = json.loads(files["bundle-manifest.json"])
        self.assertEqual(integrity["schema_version"], 1)
        self.assertEqual(integrity["canonical_catalog_sha256"], sha256((self.root / "catalog.json").read_bytes()))
        self.assertEqual(integrity["host_adapter_sha256"], sha256((self.root / "packaging/chatgpt/runtime-context.md").read_bytes()))
        self.assertEqual(integrity["files"], [
            {"path": name, "sha256": sha256(data)}
            for name, data in sorted(files.items()) if name != "bundle-manifest.json"
        ])
        canonical = []
        for skill in sorted((self.root / "skills").iterdir()):
            checksum = hashlib.sha256()
            for path in sorted(path for path in skill.rglob("*") if path.is_file()):
                checksum.update(path.relative_to(skill).as_posix().encode("utf-8") + b"\0")
                checksum.update(path.read_bytes() + b"\0")
            canonical.append({"name": skill.name, "canonical_package_sha256": checksum.hexdigest()})
        self.assertEqual(integrity["canonical_skills"], canonical)
        self.assertIn("do not validate these adapted plugin skills", integrity["evidence_scope"])
        self.assertIn("must be tested separately", integrity["evidence_scope"])

    def test_zip_has_stable_sorted_regular_file_entries_and_no_host_metadata(self) -> None:
        files = PLUGIN.package_files(self.root)
        with zipfile.ZipFile(io.BytesIO(PLUGIN.archive_bytes(files))) as archive:
            self.assertEqual(archive.namelist(), sorted(files))
            self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
            self.assertEqual(archive.comment, b"")
            self.assertIsNone(archive.testzip())
            for entry in archive.infolist():
                with self.subTest(path=entry.filename):
                    path = PurePosixPath(entry.filename)
                    self.assertFalse(path.is_absolute())
                    self.assertNotIn("..", path.parts)
                    self.assertNotIn("\\", entry.filename)
                    self.assertFalse(entry.is_dir())
                    self.assertEqual(entry.date_time, (1980, 1, 1, 0, 0, 0))
                    self.assertEqual(entry.create_system, 3)
                    self.assertEqual(entry.external_attr >> 16, stat.S_IFREG | 0o644)
                    self.assertEqual(entry.compress_type, zipfile.ZIP_STORED)
                    self.assertEqual(entry.extra, b"")
                    self.assertEqual(entry.comment, b"")
                    self.assertEqual(archive.read(entry), files[entry.filename])

    def test_reproducible_across_rebuilds_input_order_modes_and_mtimes(self) -> None:
        first = PLUGIN.package_files(self.root)
        expected = PLUGIN.archive_bytes(first)
        self.assertEqual(expected, PLUGIN.archive_bytes(dict(reversed(list(first.items())))))
        for index, path in enumerate(sorted(self.root.rglob("*"))):
            if path.is_file():
                os.utime(path, (1_000_000_000 + index, 1_700_000_000 + index))
                path.chmod(0o600)
        self.assertEqual(first, PLUGIN.package_files(self.root))
        self.assertEqual(expected, PLUGIN.archive_bytes(PLUGIN.package_files(self.root)))

    def test_repository_and_build_material_is_not_shipped(self) -> None:
        expected = PLUGIN.archive_bytes(PLUGIN.package_files(self.root))
        excluded = (
            ".git/config", ".github/workflows/ci.yml", ".agents/gtm-context.md",
            "docs/private.md", "evals/reports/raw-response.md", "examples/prospect-list.csv",
            "reference-packs/context.md", "scripts/private.py", "tests/private.py",
            "dist/old.zip", "node_modules/tool/index.js", "quality-summary.json",
            "release-manifest.json", "README.md", ".env",
        )
        for name in excluded:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Private repository-only fixture; never ship.\n", encoding="utf-8")
        self.assertEqual(expected, PLUGIN.archive_bytes(PLUGIN.package_files(self.root)))


class ManifestTests(PluginFixture):
    def test_reviewed_manifest_is_skills_only_and_all_icons_exist(self) -> None:
        manifest = self.manifest()
        PLUGIN.validate_manifest(manifest)
        self.assertEqual(manifest["name"], "gtm-skills")
        self.assertEqual(manifest["$schema"], PLUGIN.SCHEMA)
        self.assertEqual(set(manifest["extensions"]), {"com.openai"})
        extension = manifest["extensions"]["com.openai"]
        self.assertEqual(set(extension), {"interface", "onboardingSkill", "publication"})
        self.assertEqual(extension["onboardingSkill"], "./skills/gtm-context/SKILL.md")
        for key in ("composerIcon", "composerIconDark", "logo", "logoDark"):
            path = extension["interface"][key]
            self.assertTrue(path.startswith("./assets/"))
            PLUGIN.validate_svg((self.root / "packaging/chatgpt" / path).read_bytes(), path)

    def test_listing_length_boundaries(self) -> None:
        for field, maximum in {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80, "category": 120}.items():
            for value, valid in (("x" * maximum, True), ("x" * (maximum + 1), False), ("", False), ("   ", False), (None, False), (3, False)):
                with self.subTest(field=field, value_type=type(value).__name__, valid=valid):
                    manifest = self.manifest()
                    manifest["extensions"]["com.openai"]["interface"][field] = value
                    if valid:
                        PLUGIN.validate_manifest(manifest)
                    else:
                        with self.assertRaises(ValueError):
                            PLUGIN.validate_manifest(manifest)

    def test_name_boundaries_and_slug_validation(self) -> None:
        for value in ("Uppercase", "two words", "../skills", "-leading", "trailing-", "double--dash", "", "a" * 65):
            with self.subTest(name=value):
                manifest = self.manifest()
                manifest["name"] = value
                with self.assertRaises(ValueError):
                    PLUGIN.validate_manifest(manifest)
        manifest = self.manifest()
        manifest["name"] = "a" * 64
        PLUGIN.validate_manifest(manifest)

    def test_explicit_semver_accepts_release_prerelease_and_build_metadata(self) -> None:
        for version in ("0.1.9", "0.1.9-rc.1", "1.2.3+build.7", "1.2.3-rc.1+build.7"):
            with self.subTest(version=version):
                manifest = self.manifest()
                manifest["version"] = version
                PLUGIN.validate_manifest(manifest)

    def test_invalid_semver_is_rejected(self) -> None:
        for version in ("latest", "v1.2.3", "1.2", "01.2.3", "1.02.3", "1.2.03", "1.2.3-", "1.2.3-..", "1.2.3-01", "1.2.3+a..b"):
            with self.subTest(version=version):
                manifest = self.manifest()
                manifest["version"] = version
                with self.assertRaises(ValueError):
                    PLUGIN.validate_manifest(manifest)

    def test_starter_prompt_boundaries(self) -> None:
        for prompts in ([], ["x" * 128] * 3):
            manifest = self.manifest()
            manifest["extensions"]["com.openai"]["interface"]["defaultPrompt"] = prompts
            PLUGIN.validate_manifest(manifest)
        for prompts in (["x"] * 4, ["x" * 129], [""], ["   "], [None], "a prompt", None):
            with self.subTest(prompts=prompts):
                manifest = self.manifest()
                manifest["extensions"]["com.openai"]["interface"]["defaultPrompt"] = prompts
                with self.assertRaises(ValueError):
                    PLUGIN.validate_manifest(manifest)

    def test_listing_urls_require_https_and_obey_length_limit(self) -> None:
        for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
            for value in ("http://example.com", "file:///private", "", "https://" + "a" * 1017):
                with self.subTest(field=field, value=value):
                    manifest = self.manifest()
                    manifest["extensions"]["com.openai"]["interface"][field] = value
                    with self.assertRaises(ValueError):
                        PLUGIN.validate_manifest(manifest)
            manifest = self.manifest()
            manifest["extensions"]["com.openai"]["interface"][field] = "https://" + "a" * 1016
            PLUGIN.validate_manifest(manifest)

    def test_root_execution_surfaces_and_unknown_openai_extensions_are_rejected(self) -> None:
        for field in ("mcpServers", "hooks", "commands", "agents", "scripts"):
            with self.subTest(field=field):
                manifest = self.manifest()
                manifest[field] = {}
                with self.assertRaises(ValueError):
                    PLUGIN.validate_manifest(manifest)
        for field in ("mcp", "mcpServers", "hooks", "review"):
            with self.subTest(extension=field):
                manifest = self.manifest()
                manifest["extensions"]["com.openai"][field] = {}
                with self.assertRaises(ValueError):
                    PLUGIN.validate_manifest(manifest)

    def test_wrong_schema_and_duplicate_manifest_keys_are_rejected(self) -> None:
        manifest = self.manifest()
        manifest["$schema"] = "https://example.com/unrelated-schema.json"
        self.write_manifest(manifest)
        with self.assertRaises(ValueError):
            PLUGIN.package_files(self.root)
        text = (ROOT / "packaging/chatgpt/plugin.json").read_text(encoding="utf-8")
        for old, new in (("\"name\": \"gtm-skills\"", "\"name\": \"other\", \"name\": \"gtm-skills\""), ("\"displayName\": \"GTM Skills\"", "\"displayName\": \"Other\", \"displayName\": \"GTM Skills\"")):
            with self.subTest(key=old):
                self.manifest_path.write_text(text.replace(old, new), encoding="utf-8")
                with self.assertRaises(ValueError):
                    PLUGIN.package_files(self.root)

    def test_icon_paths_and_onboarding_must_resolve_inside_payload(self) -> None:
        for field, value in (
            ("composerIcon", "https://example.com/icon.svg"),
            ("logo", "./assets/missing.svg"),
            ("logoDark", "./assets/../../LICENSE.svg"),
            ("composerIconDark", "./assets/icon.png"),
        ):
            with self.subTest(field=field, value=value):
                manifest = json.loads((ROOT / "packaging/chatgpt/plugin.json").read_text(encoding="utf-8"))
                manifest["extensions"]["com.openai"]["interface"][field] = value
                self.write_manifest(manifest)
                with self.assertRaises(ValueError):
                    PLUGIN.package_files(self.root)
        for value in ("./skills/missing/SKILL.md", "../SKILL.md", "https://example.com/SKILL.md"):
            with self.subTest(onboarding=value):
                manifest = json.loads((ROOT / "packaging/chatgpt/plugin.json").read_text(encoding="utf-8"))
                manifest["extensions"]["com.openai"]["onboardingSkill"] = value
                self.write_manifest(manifest)
                with self.assertRaises(ValueError):
                    PLUGIN.package_files(self.root)


class PackageRejectionTests(PluginFixture):
    def test_changed_source_or_catalog_digest_requires_explicit_refresh(self) -> None:
        resource = self.root / "skills/research-account/assets/account-brief.md"
        resource.write_bytes(resource.read_bytes() + b"\nChanged fixture.\n")
        with self.assertRaisesRegex(ValueError, "catalog is stale"):
            PLUGIN.package_files(self.root)
        self.refresh_catalog()
        files = PLUGIN.package_files(self.root)
        self.assertEqual(files[resource.relative_to(self.root).as_posix()], resource.read_bytes())
        catalog = json.loads((self.root / "catalog.json").read_bytes())
        catalog["skills"][0]["package_sha256"] = "0" * 64
        (self.root / "catalog.json").write_text(json.dumps(catalog), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "catalog is stale"):
            PLUGIN.package_files(self.root)

    def test_unreviewed_extra_skill_file_is_rejected(self) -> None:
        path = self.root / "skills/research-account/assets/unreviewed.md"
        path.write_text("Unreviewed extra resource.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "catalog is stale"):
            PLUGIN.package_files(self.root)

    def test_unallowlisted_files_reject_even_with_fresh_catalog(self) -> None:
        for relative in (".env", "README.md", "scripts/tool.py", "agents/extra.yaml", "assets/payload.js", "assets/.hidden.md", "references/.private/note.md", "assets/data.json"):
            with self.subTest(path=relative):
                path = self.root / "skills/research-account" / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Not a permitted skill-only resource.\n", encoding="utf-8")
                self.refresh_catalog()
                with self.assertRaises(ValueError):
                    PLUGIN.package_files(self.root)
                path.unlink()
                self.refresh_catalog()

    def test_extra_skill_symlinks_cannot_disappear_from_catalog_validation(self) -> None:
        skill = self.root / "skills/research-account"
        for name, target in (("extra.md", skill / "SKILL.md"), ("dangling.md", self.root / "absent.md"), ("linked-dir", self.root / "packaging")):
            with self.subTest(path=name):
                link = skill / name
                link.symlink_to(target, target_is_directory=name == "linked-dir")
                try:
                    with self.assertRaises(ValueError):
                        PLUGIN.package_files(self.root)
                finally:
                    link.unlink()

    def test_selected_packaging_file_symlink_is_rejected(self) -> None:
        for relative in ("LICENSE", "packaging/chatgpt/plugin.json", "packaging/chatgpt/runtime-context.md", "packaging/chatgpt/assets/icon.svg"):
            with self.subTest(path=relative):
                path = self.root / relative
                original = path.read_bytes()
                target = self.root / "symlink-target.txt"
                target.write_bytes(original)
                path.unlink()
                path.symlink_to(target)
                try:
                    with self.assertRaisesRegex(ValueError, "symbolic link"):
                        PLUGIN.package_files(self.root)
                finally:
                    path.unlink()
                    path.write_bytes(original)

    def test_symlinked_parent_directory_is_rejected(self) -> None:
        assets = self.root / "packaging/chatgpt/assets"
        moved = self.root / "icon-assets"
        assets.rename(moved)
        assets.symlink_to(moved, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symbolic link"):
            PLUGIN.package_files(self.root)

    def test_missing_or_escaping_links_in_skill_body_are_rejected(self) -> None:
        source = (self.root / "skills/research-account/SKILL.md").read_text(encoding="utf-8")
        for target in ("references/missing.md", "../define-icp/SKILL.md", "/etc/passwd", "../../../README.md"):
            with self.subTest(target=target):
                (self.root / "skills/research-account/SKILL.md").write_text(source, encoding="utf-8")
                self.append_skill(f"\nRead [resource]({target}).\n")
                with self.assertRaisesRegex(ValueError, "unpackaged resource link"):
                    PLUGIN.package_files(self.root)

    def test_nested_resource_links_are_validated_from_the_resource_directory(self) -> None:
        path = self.root / "skills/research-account/assets/account-brief.md"
        path.write_bytes(path.read_bytes() + b"\n[Missing nested resource](missing.md)\n")
        self.refresh_catalog()
        with self.assertRaisesRegex(ValueError, "unpackaged resource link"):
            PLUGIN.package_files(self.root)

    def test_adapter_resource_links_are_checked_in_generated_skills(self) -> None:
        path = self.root / "packaging/chatgpt/runtime-context.md"
        path.write_bytes(path.read_bytes() + b"\n[Unbundled helper](runtime-context.md)\n")
        with self.assertRaisesRegex(ValueError, "unpackaged resource link"):
            PLUGIN.package_files(self.root)

    def test_external_links_anchors_and_document_template_placeholders_are_allowed(self) -> None:
        self.append_skill("\n[Web](https://example.com) [Email](mailto:hello@example.com) [Anchor](#output) [Source](URL)\n")
        PLUGIN.package_files(self.root)

    def test_context_description_drift_requires_adapter_review(self) -> None:
        path = self.root / "skills/gtm-context/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Produces `.agents/gtm-context.md`.", "Creates project context."), encoding="utf-8")
        self.refresh_catalog()
        with self.assertRaisesRegex(ValueError, "review the host adapter"):
            PLUGIN.package_files(self.root)

    def test_adapter_rejects_source_name_mismatch_and_bad_frontmatter(self) -> None:
        source = (self.root / "skills/research-account/SKILL.md").read_bytes()
        for data, name in ((source, "different-skill"), (b"# No frontmatter\n", "research-account"), (source.replace(b"name: research-account", b"name: research-account\nname: duplicate"), "research-account")):
            with self.subTest(name=name, length=len(data)):
                with self.assertRaises(ValueError):
                    PLUGIN.adapt_skill(data, "## Host\n", name)

    def test_secret_in_canonical_resource_is_rejected_after_catalog_refresh(self) -> None:
        candidate = "ghp_" + "A" * 36
        resource = self.root / "skills/research-account/assets/account-brief.md"
        resource.write_text(resource.read_text(encoding="utf-8") + candidate + "\n", encoding="utf-8")
        self.refresh_catalog()
        with self.assertRaisesRegex(ValueError, "possible GitHub token") as raised:
            PLUGIN.package_files(self.root)
        self.assertNotIn(candidate, str(raised.exception))

    def test_secret_in_adapter_is_rejected(self) -> None:
        candidate = "glpat-" + "A" * 24
        adapter = self.root / "packaging/chatgpt/runtime-context.md"
        adapter.write_text(adapter.read_text(encoding="utf-8") + candidate + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "possible GitLab token") as raised:
            PLUGIN.package_files(self.root)
        self.assertNotIn(candidate, str(raised.exception))


class FileAndAssetValidationTests(unittest.TestCase):
    def test_unsafe_read_paths_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for relative in ("../outside.md", "/etc/passwd", "assets/../../outside.md", "assets\\outside.md"):
                with self.subTest(path=relative):
                    with self.assertRaisesRegex(ValueError, "unsafe package path"):
                        PLUGIN.read_file(Path(directory), relative)

    def test_missing_directory_and_non_utf8_files_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "directory").mkdir()
            (root / "binary.md").write_bytes(b"\xff\xfe")
            for name in ("missing.md", "directory", "binary.md"):
                with self.subTest(path=name):
                    with self.assertRaises(ValueError):
                        PLUGIN.read_file(root, name)

    def test_file_size_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "large.md"
            path.write_bytes(b"a" * (5 * 1024 * 1024))
            self.assertEqual(len(PLUGIN.read_file(root, "large.md")), 5 * 1024 * 1024)
            with path.open("ab") as stream:
                stream.write(b"a")
            with self.assertRaisesRegex(ValueError, "exceeds 5 MiB"):
                PLUGIN.read_file(root, "large.md")

    def test_all_supported_secret_shapes_are_rejected_without_echoing_them(self) -> None:
        candidates = {
            "private key block": "-----BEGIN " + "PRIVATE KEY-----",
            "AWS access key": "AKIA" + "A" * 16,
            "GitHub token": "ghp_" + "A" * 36,
            "OpenAI-style secret": "sk-" + "A" * 24,
            "Slack token": "xoxb-" + "A" * 24,
            "GitLab token": "glpat-" + "A" * 24,
            "npm token": "npm_" + "A" * 36,
            "Google API key": "AIza" + "A" * 35,
            "Stripe secret": "sk_test_" + "A" * 24,
        }
        self.assertEqual(set(candidates), set(PLUGIN.SECRET_PATTERNS))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for label, candidate in candidates.items():
                with self.subTest(label=label):
                    (root / "candidate.md").write_text(candidate, encoding="utf-8")
                    with self.assertRaises(ValueError) as raised:
                        PLUGIN.read_file(root, "candidate.md")
                    self.assertIn(label, str(raised.exception))
                    self.assertNotIn(candidate, str(raised.exception))

    def test_minimal_safe_square_svg_is_accepted(self) -> None:
        PLUGIN.validate_svg(b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><title>Safe icon</title><rect width="48" height="48" fill="#176B53"/></svg>', "safe.svg")

    def test_svg_must_be_real_square_with_finite_dimensions(self) -> None:
        for box in ("", "0 0 47 47", "0 0 48 64", "0 0 -48 -48", "0 0 inf inf", "0 0 NaN NaN", "0 0 48", "bad values here"):
            with self.subTest(viewbox=box):
                data = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{box}"/>'.encode()
                with self.assertRaises(ValueError):
                    PLUGIN.validate_svg(data, "invalid.svg")
        for data in (b"not XML", b"<svg/>", b'<html xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"/>'):
            with self.subTest(data=data):
                with self.assertRaises((ValueError, ElementTree.ParseError)):
                    PLUGIN.validate_svg(data, "invalid.svg")

    def test_active_external_and_unsupported_svg_content_is_rejected(self) -> None:
        for content in ('<script>alert(1)</script>', '<image href="https://example.com/icon.png"/>', '<foreignObject/>', '<use href="#shape"/>', '<rect onload="alert(1)"/>', '<rect OnClick="alert(1)"/>', '<rect style="fill:url(https://example.com/fill)"/>', '<rect fill="URL(https://example.com/fill)"/>', '<rect xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="https://example.com"/>'):
            with self.subTest(content=content):
                data = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">{content}</svg>'.encode()
                with self.assertRaises(ValueError):
                    PLUGIN.validate_svg(data, "active.svg")


class PluginCommandTests(PluginFixture):
    def run_command(self, argv: list[str]) -> tuple[int, str, str]:
        original = PLUGIN.package_files
        stdout, stderr = io.StringIO(), io.StringIO()
        with mock.patch.object(PLUGIN, "package_files", side_effect=lambda: original(self.root)):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = PLUGIN.main(argv)
        return result, stdout.getvalue(), stderr.getvalue()

    def test_check_is_read_only_even_with_explicit_output(self) -> None:
        before = {path.relative_to(self.root).as_posix(): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        output = self.root / "dist/unused.zip"
        result, stdout, stderr = self.run_command(["--check", "--output", str(output)])
        self.assertEqual(result, 0, stderr)
        self.assertIn("PASS plugin package: 97 files", stdout)
        self.assertFalse(output.parent.exists())
        after = {path.relative_to(self.root).as_posix(): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(after, before)

    def test_output_zip_and_sidecar_match_verified_bytes(self) -> None:
        output = self.root / "dist/candidate.zip"
        expected = PLUGIN.archive_bytes(PLUGIN.package_files(self.root))
        result, stdout, stderr = self.run_command(["--output", str(output)])
        self.assertEqual(result, 0, stderr)
        self.assertIn("PASS plugin package", stdout)
        self.assertEqual(output.read_bytes(), expected)
        self.assertEqual(output.with_suffix(".zip.sha256").read_text(encoding="utf-8"), f"{sha256(expected)}  candidate.zip\n")

    def test_invalid_package_fails_without_creating_output(self) -> None:
        self.manifest_path.write_text("{bad JSON", encoding="utf-8")
        output = self.root / "dist/rejected.zip"
        result, stdout, stderr = self.run_command(["--output", str(output)])
        self.assertEqual(result, 1)
        self.assertEqual(stdout, "")
        self.assertIn("FAIL", stderr)
        self.assertFalse(output.parent.exists())

    def test_malformed_manifest_types_fail_cleanly(self) -> None:
        invalid_manifests = [None, [], "not an object", 3]
        for value in (None, 7, [], {}):
            manifest = self.manifest()
            manifest["extensions"]["com.openai"]["interface"]["supportURL"] = value
            invalid_manifests.append(manifest)
        for value in invalid_manifests:
            with self.subTest(value=value):
                self.write_manifest(value)
                result, stdout, stderr = self.run_command(["--check"])
                self.assertEqual(result, 1)
                self.assertNotIn("PASS", stdout)
                self.assertIn("FAIL", stderr)
                self.assertNotIn("Traceback", stderr)

    def test_nondeterministic_second_build_fails_before_write(self) -> None:
        files = PLUGIN.package_files(self.root)
        changed = copy.deepcopy(files)
        changed["LICENSE"] += b"\nChanged on second read.\n"
        output = self.root / "dist/rejected.zip"
        stderr = io.StringIO()
        with mock.patch.object(PLUGIN, "package_files", side_effect=[files, changed]):
            with contextlib.redirect_stderr(stderr):
                result = PLUGIN.main(["--output", str(output)])
        self.assertEqual(result, 1)
        self.assertIn("not deterministic", stderr.getvalue())
        self.assertFalse(output.parent.exists())


if __name__ == "__main__":
    unittest.main()
