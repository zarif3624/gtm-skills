from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_docs.py"
SPEC = importlib.util.spec_from_file_location("validate_docs", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class DocumentationLinkTests(unittest.TestCase):
    def test_valid_relative_and_external_links_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "docs").mkdir()
            (root / "target.md").write_text("# Target\n", encoding="utf-8")
            source = root / "docs" / "source.md"
            source.write_text(
                "[local](../target.md#section) [web](https://example.com)\n",
                encoding="utf-8",
            )
            self.assertEqual(VALIDATOR.validate_file(source, root), [])

    def test_missing_and_escaping_links_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source.md"
            source.write_text("[missing](no.md) [escape](../outside.md)\n", encoding="utf-8")
            errors = VALIDATOR.validate_file(source, root)
            self.assertIn("repository link target does not exist: no.md", errors)
            self.assertIn("repository link escapes the repository: ../outside.md", errors)

    def test_symlink_target_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            outside = root.parent / "doc-link-outside.md"
            outside.write_text("# Outside\n", encoding="utf-8")
            try:
                (root / "linked.md").symlink_to(outside)
                source = root / "source.md"
                source.write_text("[linked](linked.md)\n", encoding="utf-8")
                errors = VALIDATOR.validate_file(source, root)
                self.assertTrue(any("symbolic link" in error for error in errors))
            finally:
                outside.unlink(missing_ok=True)


class CustomerSuccessPlaybookTests(unittest.TestCase):
    def test_customer_success_playbook_is_discoverable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "playbooks" / "README.md").read_text(encoding="utf-8")

        self.assertIn("[Customer Success playbook](docs/playbooks/customer-success.md)", readme)
        self.assertIn("[Customer Success playbook](customer-success.md)", index)

    def test_customer_success_playbook_preserves_outcome_evidence_boundaries(self) -> None:
        path = ROOT / "docs" / "playbooks" / "customer-success.md"
        self.assertTrue(path.is_file(), "Customer Success playbook is missing")
        playbook = path.read_text(encoding="utf-8")

        for skill in (
            "$handoff-customer",
            "$review-customer-outcomes",
            "$plan-account",
            "$build-business-case",
        ):
            self.assertIn(skill, playbook)
        self.assertIn("Activity is not an outcome", playbook)
        self.assertIn("customer-validated", playbook)
        self.assertIn("Proposed", playbook)
        self.assertIn("Unknown", playbook)


class SalesManagerPlaybookTests(unittest.TestCase):
    def test_sales_manager_playbook_is_discoverable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "playbooks" / "README.md").read_text(encoding="utf-8")

        self.assertIn("[Sales manager playbook](docs/playbooks/sales-manager.md)", readme)
        self.assertIn("[Sales manager playbook](sales-manager.md)", index)

    def test_sales_manager_playbook_preserves_operating_boundaries(self) -> None:
        path = ROOT / "docs" / "playbooks" / "sales-manager.md"
        self.assertTrue(path.is_file(), "Sales manager playbook is missing")
        playbook = path.read_text(encoding="utf-8")

        for skill in (
            "$analyze-sales-call",
            "$qualify-opportunity",
            "$review-pipeline",
            "$forecast-sales",
            "$plan-deal",
            "$coach-sales-rep",
        ):
            self.assertIn(skill, playbook)
        self.assertIn("pipeline review before the forecast call", playbook)
        self.assertIn("buyer evidence", playbook)
        self.assertIn("formal employment", playbook)
        self.assertIn("Proposed", playbook)
        self.assertIn("Unknown", playbook)


class SalesEngineerPlaybookTests(unittest.TestCase):
    def test_sales_engineer_playbook_is_discoverable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "playbooks" / "README.md").read_text(encoding="utf-8")
        quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")

        self.assertIn("[Sales engineer playbook](docs/playbooks/sales-engineer.md)", readme)
        self.assertIn("[Sales engineer playbook](sales-engineer.md)", index)
        self.assertIn("sales engineers", quickstart.lower())

    def test_sales_engineer_playbook_preserves_technical_proof_boundaries(self) -> None:
        path = ROOT / "docs" / "playbooks" / "sales-engineer.md"
        self.assertTrue(path.is_file(), "Sales engineer playbook is missing")
        playbook = path.read_text(encoding="utf-8")

        for skill in (
            "$research-account",
            "$prepare-discovery",
            "$analyze-sales-call",
            "$prepare-demo",
            "$handle-objections",
            "$create-mutual-action-plan",
        ):
            self.assertIn(skill, playbook)
        self.assertIn("Demo evidence is not production proof", playbook)
        self.assertIn("buyer-owned proof criteria", playbook)
        self.assertIn("roadmap", playbook.lower())
        self.assertIn("security", playbook.lower())
        self.assertIn("Proposed", playbook)
        self.assertIn("Unknown", playbook)


class ProductMarketingPlaybookTests(unittest.TestCase):
    def test_product_marketing_playbook_is_discoverable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "playbooks" / "README.md").read_text(encoding="utf-8")
        quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")

        self.assertIn("[Product marketing playbook](docs/playbooks/product-marketing.md)", readme)
        self.assertIn("[Product marketing playbook](product-marketing.md)", index)
        self.assertIn("product marketers", quickstart.lower())

    def test_product_marketing_playbook_preserves_claim_evidence_boundaries(self) -> None:
        path = ROOT / "docs" / "playbooks" / "product-marketing.md"
        self.assertTrue(path.is_file(), "Product Marketing playbook is missing")
        playbook = path.read_text(encoding="utf-8")

        for skill in (
            "$gtm-context",
            "$review-customer-outcomes",
            "$analyze-win-loss",
            "$define-icp",
            "$develop-positioning",
            "$build-business-case",
        ):
            self.assertIn(skill, playbook)
        self.assertIn("Customer evidence is not publication permission", playbook)
        self.assertIn("sample size", playbook.lower())
        self.assertIn("customer permission", playbook.lower())
        self.assertIn("legal", playbook.lower())
        self.assertIn("Hypothesis", playbook)
        self.assertIn("Proposed", playbook)
        self.assertIn("Unknown", playbook)


class PartnerChannelPlaybookTests(unittest.TestCase):
    def test_partner_channel_playbook_is_discoverable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "playbooks" / "README.md").read_text(encoding="utf-8")
        quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")

        self.assertIn(
            "[Partner and channel leader playbook](docs/playbooks/partner-channel.md)",
            readme,
        )
        self.assertIn(
            "[Partner and channel leader playbook](partner-channel.md)",
            index,
        )
        self.assertIn("partner and channel leaders", quickstart.lower())

    def test_partner_channel_playbook_preserves_attribution_and_authority_boundaries(
        self,
    ) -> None:
        path = ROOT / "docs" / "playbooks" / "partner-channel.md"
        self.assertTrue(path.is_file(), "Partner and channel leader playbook is missing")
        playbook = path.read_text(encoding="utf-8")

        for skill in (
            "$gtm-context",
            "$define-icp",
            "$plan-partner-channel",
            "$research-account",
            "$review-pipeline",
            "$forecast-sales",
        ):
            self.assertIn(skill, playbook)
        self.assertIn("A signed partner is not an activated partner", playbook)
        self.assertIn("partner-reported pipeline is not forecast", playbook.lower())
        self.assertIn("canonical opportunity", playbook.lower())
        self.assertIn("double counting", playbook.lower())
        self.assertIn("customer consent", playbook.lower())
        self.assertIn("Proposed", playbook)
        self.assertIn("Unknown", playbook)


class RevenueEnablementPlaybookTests(unittest.TestCase):
    def test_revenue_enablement_playbook_is_discoverable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "playbooks" / "README.md").read_text(encoding="utf-8")
        quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")

        self.assertIn(
            "[Revenue Enablement leader playbook](docs/playbooks/revenue-enablement.md)",
            readme,
        )
        self.assertIn(
            "[Revenue Enablement leader playbook](revenue-enablement.md)",
            index,
        )
        self.assertIn("revenue enablement leaders", quickstart.lower())

    def test_revenue_enablement_playbook_preserves_learning_boundaries(self) -> None:
        path = ROOT / "docs" / "playbooks" / "revenue-enablement.md"
        self.assertTrue(path.is_file(), "Revenue Enablement leader playbook is missing")
        playbook = path.read_text(encoding="utf-8")

        for skill in (
            "$gtm-context",
            "$analyze-sales-call",
            "$analyze-win-loss",
            "$develop-positioning",
            "$prepare-demo",
            "$coach-sales-rep",
        ):
            self.assertIn(skill, playbook)
        self.assertIn("Training completion is not behavior change", playbook)
        self.assertIn("Behavior change is not revenue impact", playbook)
        self.assertIn("sample size", playbook.lower())
        self.assertIn("customer permission", playbook.lower())
        self.assertIn("formal employment", playbook.lower())
        self.assertIn("Hypothesis", playbook)
        self.assertIn("Proposed", playbook)
        self.assertIn("Unknown", playbook)


class DemandGenerationPlaybookTests(unittest.TestCase):
    def test_demand_generation_playbook_is_discoverable(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs" / "playbooks" / "README.md").read_text(encoding="utf-8")
        quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")

        self.assertIn(
            "[Demand Generation leader playbook](docs/playbooks/demand-generation.md)",
            readme,
        )
        self.assertIn(
            "[Demand Generation leader playbook](demand-generation.md)",
            index,
        )
        self.assertIn("demand generation leaders", quickstart.lower())

    def test_demand_generation_playbook_preserves_funnel_and_attribution_boundaries(
        self,
    ) -> None:
        path = ROOT / "docs" / "playbooks" / "demand-generation.md"
        self.assertTrue(path.is_file(), "Demand Generation leader playbook is missing")
        playbook = path.read_text(encoding="utf-8")

        for skill in (
            "$gtm-context",
            "$define-icp",
            "$develop-positioning",
            "$plan-prospecting",
            "$write-outbound",
            "$review-pipeline",
            "$analyze-win-loss",
        ):
            self.assertIn(skill, playbook)
        self.assertIn("Engagement is not buyer progress", playbook)
        self.assertIn("Attributed pipeline is not caused revenue", playbook)
        self.assertIn("canonical opportunity", playbook.lower())
        self.assertIn("denominator", playbook.lower())
        self.assertIn("consent", playbook.lower())
        self.assertIn("sample size", playbook.lower())
        self.assertIn("Confirm consent, suppression, privacy", playbook)
        approval_start = playbook.index("An authorized human must approve")
        approval_paragraph = playbook[approval_start:].split("\n\n", 1)[0]
        for action in (
            "channel activation",
            "data purchases",
            "list uploads",
            "live sends",
            "CRM writes",
            "scoring changes",
            "public claims",
        ):
            self.assertIn(action, approval_paragraph)
        self.assertIn("Hypothesis", playbook)
        self.assertIn("Proposed", playbook)
        self.assertIn("Unknown", playbook)


if __name__ == "__main__":
    unittest.main()
