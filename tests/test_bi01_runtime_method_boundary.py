"""Canonical runtime prose must not load retired professional source paths."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class RuntimeMethodBoundary(unittest.TestCase):
    def test_canonical_runtime_has_no_retired_professional_links(self):
        paths = set()
        for directory in ("runtime/overlay", "runtime/dual_route_execution", "runtime/operations"):
            paths.update((ROOT / directory).glob("*.md"))
        retired = (
            "professional/feature_observation/", "professional/v2/",
            "FEATURE_OBSERVATION_PREPARATION_GUIDE.md",
            "FEATURE_OBSERVATION_PREP_REVIEW_20261021.md",
            "operations/feature_observation/templates",
        )
        findings = []
        for path in sorted(paths):
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                # Exact historical GitHub references do not reload current local methods.
                without_urls = re.sub(r"https?://[^\s)]+", "", line)
                for old in retired:
                    if old in without_urls:
                        findings.append(f"{path.relative_to(ROOT)}:{line_number}: {old}")
        self.assertEqual(findings, [], "Retired active references:\n" + "\n".join(findings))

    def test_workflow_contract_does_not_require_old_four_works(self):
        for name in ("DR13_WORK_ARRANGEMENT_AND_CONTEXT.md", "DR14_QUESTION_WORK_CONTRACT.md"):
            text = (ROOT / "runtime/dual_route_execution" / name).read_text(encoding="utf-8")
            for phrase in ("四项可往返工作", "当前四项工作方法", "BI-01工作2/3", "新的具体特征观察当前仍无"):
                with self.subTest(file=name, phrase=phrase):
                    self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
