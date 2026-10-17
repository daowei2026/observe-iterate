"""V2 business-source boundary tests. Read-only: no Pro, phone or environment/data access."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

V2_SOURCES = [
    "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md",
    "professional/v2/01_AIDATA_CHART_AND_DATA.md",
    "professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md",
    "professional/v2/03_EXECUTION_HANDOFF.md",
    "professional/v2/04_BI01_BUSINESS_BASELINE.md",
    "professional/v2/05_BI01_FIXED_INPUT_DATA.md",
]
ACTIVE_DOCS = [
    *sorted((ROOT / "runtime/dual_route_execution").glob("DR*.md")),
    *sorted((ROOT / "runtime/overlay").glob("[0-9][0-9]_*.md")),
    ROOT / "runtime/AGENTS.md",
    ROOT / "runtime/overlay/AGENTS.md",
    ROOT / "runtime/operations/BI01_V2_RUN_GUIDE.md",
]
FORBIDDEN_ACTIVE_POINTERS = (
    "professional/source/",
    "professional/interfaces/",
    "runs/BI-01-RESTART-01/README.md",
    "runtime/operations/BI01_REAL_RUN_V1.md",
    "runtime/operations/ROUND_RECORD_CONTRACT.md",
    "runtime/operations/templates/WORKMAP_BINDING_TEMPLATE.json",
)


class V2Boundary(unittest.TestCase):
    def test_old_business_sources_are_not_present(self):
        for path in (
            "professional/source",
            "professional/interfaces",
            "runs/BI-01-RESTART-01",
            "runtime/operations/templates",
            "runtime/operations/BI01_REAL_RUN_V1.md",
            "runtime/operations/ROUND_RECORD_CONTRACT.md",
        ):
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists())

    def test_actual_new_professional_sources_exist(self):
        for path in V2_SOURCES:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())
                self.assertTrue((ROOT / path).read_text(encoding="utf-8").strip())

    def test_active_documents_do_not_direct_to_deleted_sources(self):
        for doc in ACTIVE_DOCS:
            if not doc.is_file():
                self.fail(f"Expected live method document missing: {doc}")
            body = doc.read_text(encoding="utf-8")
            for missing in FORBIDDEN_ACTIVE_POINTERS:
                with self.subTest(doc=str(doc.relative_to(ROOT)), path=missing):
                    self.assertNotIn(missing, body)

    def test_active_dispatch_and_schema_use_v2_questions_only(self):
        dispatch = json.loads((ROOT / "runtime/config/COORDINATOR_DISPATCH.json").read_text(encoding="utf-8"))
        work = dispatch["works"]["BI-01"]
        self.assertEqual(work["goal_ref"]["path"], V2_SOURCES[0])
        self.assertEqual(
            set(work["modes"]),
            {"M-START", "M-REASSESS", "M-CLOSE", "OBSERVATION_SCOPE",
             "OBSERVATION_CHART", "OBSERVATION_IDEAS", "INDEPENDENT_REVIEW"}
        )

        schema = json.loads((ROOT / "runtime/overlay/tools/question_work.schema.json").read_text(encoding="utf-8"))
        defs = schema["$defs"]
        questions = defs["bindingV2"]["properties"]["question_ids"]["items"]["anyOf"][0]["enum"]
        returned = defs["returnV2"]["properties"]["focus_results"]["items"]["properties"]["question_id"]["anyOf"][0]["enum"]
        for ids in (questions, returned):
            self.assertTrue({"S1", "S2", "S3"} <= set(ids))
            self.assertFalse(set(ids) & {"I1", "I2", "I3", "I4", "I5", "I6"})

    def test_fixed_precomputed_data_and_original_business_context(self):
        business = (ROOT / V2_SOURCES[4]).read_text(encoding="utf-8")
        fixed = (ROOT / V2_SOURCES[5]).read_text(encoding="utf-8")
        goal = (ROOT / V2_SOURCES[0]).read_text(encoding="utf-8")
        chart = (ROOT / V2_SOURCES[1]).read_text(encoding="utf-8")

        self.assertIn("OP-01", business)
        self.assertIn("Q-01", business)
        self.assertIn("I1", business)
        self.assertIn("I2", business)
        self.assertIn("I3", business)
        for filename in (
            "steel_U2_U3_执行结果_20261010.zip",
            "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip",
        ):
            with self.subTest(filename=filename):
                self.assertIn(filename, fixed)
                self.assertIn("两份 ZIP", goal)
        for checksum in (
            "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c",
            "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987",
            "ff3215126461a0cda564c82c4a6e42b99bf94cb7b6a8320df9c8ba93d269d70a",
        ):
            self.assertIn(checksum, fixed)
        self.assertIn("23 个 CSV", fixed)
        self.assertIn("15 CSV", fixed)
        self.assertIn("不安排重算", goal)
        self.assertIn("本轮不让 AI 看渲染图片", chart)
        self.assertIn("另建独立工作分支", chart)

        binding = json.loads((ROOT / "runtime/config/WORKMAP_BINDING.json").read_text(encoding="utf-8"))
        template = json.loads((ROOT / "runtime/operations/v2/templates/WORKMAP_BINDING_TEMPLATE.json").read_text(encoding="utf-8"))
        for config in (binding, template):
            self.assertEqual(config["status"], "NOT_CONFIGURED")
            for path in V2_SOURCES:
                self.assertIn(path, config["rule_paths"])

    def test_v2_business_goal_is_not_a_role_assignment(self):
        goal = (ROOT / "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md").read_text(encoding="utf-8")
        first_section = goal.split("## 2.", 1)[0]
        self.assertIn("业务认识", first_section)
        self.assertIn("不合理", first_section)
        self.assertIn("原因", first_section)
        self.assertIn("U2", first_section)
        self.assertIn("U3", first_section)

    def test_codex_workspace_and_pro_zip_fallback_are_separate(self):
        chart = (ROOT / "professional/v2/01_AIDATA_CHART_AND_DATA.md").read_text(encoding="utf-8")
        handoff = (ROOT / "professional/v2/03_EXECUTION_HANDOFF.md").read_text(encoding="utf-8")
        data = (ROOT / "professional/v2/05_BI01_FIXED_INPUT_DATA.md").read_text(encoding="utf-8")
        operations = (ROOT / "runtime/operations/BI01_V2_RUN_GUIDE.md").read_text(encoding="utf-8")
        rounds = (ROOT / "runtime/operations/V2_ROUND_RECORD_CONTRACT.md").read_text(encoding="utf-8")
        workspace = "/dwdhome/fy/BASE_E6_2"
        mcp_share = r"H:\fy\observe-iterate-share"
        codex_share = "/dwdhome/fy/observe-iterate-share"
        for content in (chart, handoff, data, operations):
            self.assertIn(workspace, content)
        for content in (handoff, operations, rounds):
            self.assertIn(mcp_share, content)
            self.assertIn(codex_share, content)
        self.assertIn("不是两份固定 ZIP", data)
        self.assertIn("先核是否真未提交", rounds)
        self.assertIn("不要再应用同轮 ZIP", rounds)
        self.assertIn("非 force 提交并远端回读", rounds)
        self.assertIn("不因不能提交", rounds)
        self.assertIn("不规定一个不存在的专用 MCP API", rounds)

    def test_new_run_not_adopted_or_sent(self):
        binding = json.loads((ROOT / "runtime/config/WORKMAP_BINDING.json").read_text(encoding="utf-8"))
        self.assertEqual(binding["status"], "NOT_CONFIGURED")
        self.assertEqual(binding["streams"]["bi01"]["map"]["path"], "runs/BI-01-V2-01/00_长程推进地图.md")
        self.assertEqual(binding["streams"]["bi01"]["task"], "runs/BI-01-V2-01/01_当前任务.md")
        for path in ("runs/BI-01-V2-01/OWNER_START.md", "runs/BI-01-V2-01/BOOTSTRAP.json"):
            self.assertFalse((ROOT / path).exists())
        gate = (ROOT / "runtime/tools/bi01_run_gate.py").read_text(encoding="utf-8")
        self.assertIn('RUN = "runs/BI-01-V2-01"', gate)


if __name__ == "__main__":
    unittest.main()
