"""Current professional sources are replaceable; historical records remain historical."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
METHOD = ROOT / "professional/case_observation"
BASE = "9badfa6f30caebbe3156c5e4ee4deb43d22cacb5"
OLDER = "c7971cc616e09db47681abc868e77acdc272f84a"
METHOD_FILES = {
    "README.md", "00_PURPOSE_AND_OUTPUTS.md", "01_RESEARCH_METHOD.md",
    "02_OWNER_DELIVERY.md", "03_AIDATA_USE.md", "04_SOURCES_AND_REUSE.md",
}
ACTIVE = [
    "README.md", "professional/README.md", "professional/CURRENT_EXECUTION.md",
    "professional/TASK_ROUTER.md", "runtime/README.md", "runtime/AGENTS.md",
    "runtime/overlay/AGENTS.md", "runtime/overlay/CURRENT_EXECUTION.md",
    "runtime/overlay/00_README_当前运行入口.md",
    "runtime/overlay/08_自然语言运行提示_v0.3.md",
    "runtime/dual_route_execution/DR00_START_HERE.md",
    "runtime/dual_route_execution/DR12_PROFESSIONAL_QUESTION_CATALOG.md",
    "runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md",
    "runtime/operations/ADOPTION_HANDOFF_CHECKLIST.md",
]


class ProfessionalSourceBoundary(unittest.TestCase):
    def test_single_current_method_and_explicit_history(self):
        self.assertEqual({p.name for p in METHOD.iterdir() if p.is_file()}, METHOD_FILES)
        for old in ("professional/feature_observation", "professional/v2"):
            self.assertFalse((ROOT / old).exists())
        self.assertIn(BASE, (METHOD / "04_SOURCES_AND_REUSE.md").read_text(encoding="utf-8"))

    def test_old_runs_remain_separate(self):
        for run in ("BI-01-V2-01", "BI-01-V2-02"):
            self.assertFalse((ROOT / "runs" / run).exists())
            body = (ROOT / "runs/history" / (run + ".md")).read_text(encoding="utf-8")
            self.assertIn(OLDER, body)
            self.assertIn("/runs/" + run, body)
        self.assertTrue((ROOT / "runs/BI-01-FO-01/01_当前任务.md").is_file())
        self.assertTrue((ROOT / "runs/BI-01-FO-01/provenance").is_dir())
        self.assertIn("BI-01-FO-01", (ROOT / "runs/README.md").read_text(encoding="utf-8"))

    def test_dispatch_selects_actual_method(self):
        cfg = json.loads((ROOT / "runtime/config/COORDINATOR_DISPATCH.json").read_text())
        work = cfg["works"]["BI-01"]
        self.assertEqual(work["stage"], "BI01")
        self.assertEqual(work["goal_ref"]["path"], "professional/case_observation/00_PURPOSE_AND_OUTPUTS.md")
        self.assertTrue((ROOT / work["goal_ref"]["path"]).is_file())
        self.assertIn("CASE_OBSERVATION", work["modes"])
        self.assertNotIn("FEATURE_OBSERVATION", work["modes"])
        self.assertNotIn("OBSERVATION_SCOPE", work["modes"])

    def test_runtime_does_not_embed_old_business_obligations(self):
        body = (ROOT / "runtime/overlay/08_自然语言运行提示_v0.3.md").read_text(encoding="utf-8")
        for old in ("professional/feature_observation/", "U2NormalNodeBehaviorFrp",
                    "本轮专业主体是有权任务指定的具名已实现", "当前四项可往返"):
            self.assertNotIn(old, body)
        for marker in ("MANAGEMENT_DUTY", "MANAGEMENT_STAGE_BI01", "TASK_DUTY", "STAGE_BI01",
                       "READONLY_RECEPTION_BI01", "RETURN_REPAIR", "REFERENCE_USE", "RETURN_TAIL",
                       "RETURN_REPAIR_TAIL"):
            self.assertEqual(body.count("<!-- " + marker + "_BEGIN -->"), 1)
            self.assertEqual(body.count("<!-- " + marker + "_END -->"), 1)
        self.assertIn("return_to", body)
        self.assertIn("--github-message-ref", body)

    def test_active_local_links_resolve(self):
        for path in [ROOT / p for p in ACTIVE] + list(METHOD.glob("*.md")):
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                with self.subTest(path=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue((path.parent / target).exists())

    def test_binding_does_not_silently_inherit_old_run(self):
        b = json.loads((ROOT / "runtime/config/WORKMAP_BINDING.json").read_text())
        self.assertIn(b["status"], {"NOT_CONFIGURED", "ADOPTED"})
        self.assertNotIn("runs/BI-01-FO-01/", b["overview"]["path"])
        for path in b["rule_paths"]:
            self.assertTrue((ROOT / path).is_file())
        if b["status"] == "NOT_CONFIGURED":
            self.assertIn("<NEW_RUN_ID>", b["overview"]["path"])
        for root in b["streams"]["bi01"]["watch_roots"]:
            self.assertNotIn("provenance/turns", root)


if __name__ == "__main__":
    unittest.main()
