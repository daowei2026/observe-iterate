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
    "professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md",
    "professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md",
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
                self.assertIn("两份", goal)
                self.assertIn("ZIP", goal)
        for checksum in (
            "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c",
            "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987",
            "ff3215126461a0cda564c82c4a6e42b99bf94cb7b6a8320df9c8ba93d269d70a",
        ):
            self.assertIn(checksum, fixed)
        self.assertIn("23 个 CSV", fixed)
        self.assertIn("15 CSV", fixed)
        self.assertIn("不安排重算", goal)
        self.assertIn("AI 本轮只读取同图结构化数据，不视觉看图片像素", chart)
        self.assertIn("aidata 的全新独立分支", chart)

        binding = json.loads((ROOT / "runtime/config/WORKMAP_BINDING.json").read_text(encoding="utf-8"))
        template = json.loads((ROOT / "runtime/operations/v2/templates/WORKMAP_BINDING_TEMPLATE.json").read_text(encoding="utf-8"))
        for config in (binding, template):
            self.assertEqual(config["status"], "NOT_CONFIGURED")
            for path in V2_SOURCES:
                self.assertIn(path, config["rule_paths"])

    def test_v2_business_goal_is_not_a_role_assignment(self):
        goal = (ROOT / "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md").read_text(encoding="utf-8")
        first_section = goal.split("## 2.", 1)[0]
        self.assertIn("叙事", first_section)
        self.assertIn("真实市场行情", first_section)
        self.assertIn("后续实际运动", first_section)
        self.assertIn("强弱", first_section)
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
        self.assertIn("不是上述固定 ZIP 数据目录", data)
        self.assertIn("先核 **新分支远端**", rounds)
        self.assertIn("不能重复应用 ZIP", rounds)
        self.assertIn("非 force 提交并 fresh readback", rounds)
        self.assertIn("Pro 无法实际向 GitHub 提交", rounds)
        self.assertIn("禁止伪造软件 API", rounds)

    def test_fixed_zip_current_codex_location_and_method_map(self):
        fixed = (ROOT / "professional/v2/05_BI01_FIXED_INPUT_DATA.md").read_text(encoding="utf-8")
        source_map = (ROOT / "professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md").read_text(encoding="utf-8")
        chart = (ROOT / "professional/v2/01_AIDATA_CHART_AND_DATA.md").read_text(encoding="utf-8")
        for doc in (fixed, chart):
            self.assertIn("/dwdhome/fy/资金管理", doc)
        self.assertIn("Owner", fixed)
        self.assertIn("U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC", source_map)
        self.assertIn("U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC", source_map)
        self.assertIn("U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT", source_map)
        self.assertIn("U3_MA_LOCAL_CONTRACT_MOVEMENT_01", source_map)
        self.assertIn("OpportunityGroupBudgetEvidence", source_map)
        self.assertIn("ProgressBundle", source_map)
        self.assertIn("WITHHELD", source_map)
        self.assertIn("current_application=NOT_APPLIED", source_map)
        self.assertIn("5 行 = 同一个 Case", source_map)
        self.assertIn("refonly-ad8824a52552d7bffa91", fixed)
        self.assertIn("formal_assessments_committed=NO", fixed)
        self.assertIn("15 条", fixed)
        self.assertIn("同一个 hc/i/rb Case 的五个 As-Of", (ROOT / V2_SOURCES[0]).read_text(encoding="utf-8"))

    def test_scene_first_business_method_and_no_preset_classification(self):
        method = (ROOT / "professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md").read_text(encoding="utf-8")
        goal = (ROOT / "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md").read_text(encoding="utf-8")
        chart = (ROOT / "professional/v2/01_AIDATA_CHART_AND_DATA.md").read_text(encoding="utf-8")
        analysis = (ROOT / "professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md").read_text(encoding="utf-8")
        for term in ("叙事", "基础行情", "后续", "U2", "U3", "不预设"):
            self.assertIn(term, method)
        self.assertIn("这份方法不定义固定的 A/B/C 场景类别", method)
        self.assertIn("不能从某几个指标", goal)
        self.assertIn("先用上游 K 线", chart)
        self.assertIn("当时四方面判断", analysis)
        self.assertIn("不产生“提前识别”资格", method)
        self.assertIn("WITHHELD", method)
        self.assertIn("BI-01-V2-02", goal)

    def test_new_run_no_start_and_old_paused_history_retained(self):
        run = ROOT / "runs/BI-01-V2-02"
        self.assertTrue((run / "README.md").is_file())
        for path in ("OWNER_START.md", "00_长程推进地图.md",
                     "01_当前任务.md", "provenance/turns/R0001/INVOCATION.json",
                     "reviews/WORKMAP_INTAKE_CURRENT.json"):
            with self.subTest(path=path):
                self.assertFalse((run / path).exists())
        previous = ROOT / "runs/BI-01-V2-01/provenance/controller/OWNER_PAUSE_AND_CHART_REVIEW_20261018.json"
        self.assertTrue(previous.is_file())
        state = json.loads(previous.read_text(encoding="utf-8"))
        self.assertEqual(state["state"], "PAUSED_BY_OWNER_NOT_COMPLETE")
        binding = json.loads((ROOT / "runtime/config/WORKMAP_BINDING.json").read_text(encoding="utf-8"))
        self.assertEqual(binding["status"], "NOT_CONFIGURED")
        self.assertEqual(binding["overview"]["path"], "runs/BI-01-V2-02/README.md")
        self.assertNotIn("BI-01-V2-01", json.dumps(binding, ensure_ascii=False).replace("old BI-01-V2-01 remains paused", ""))

    def test_new_run_template_does_not_claim_adoption_or_owner_start(self):
        # The live run legitimately gains GO/BOOTSTRAP and adoption. The reusable
        # startup template must remain unexecuted and must never supply a GO.
        template = ROOT / "runtime/operations/v2/templates"
        binding = json.loads((template / "WORKMAP_BINDING_TEMPLATE.json").read_text(encoding="utf-8"))
        self.assertEqual(binding["status"], "NOT_CONFIGURED")
        self.assertEqual(binding["streams"]["bi01"]["map"]["path"], "runs/BI-01-V2-02/00_长程推进地图.md")
        self.assertEqual(binding["streams"]["bi01"]["task"], "runs/BI-01-V2-02/01_当前任务.md")
        for name in ("OWNER_START.md", "BOOTSTRAP.json"):
            self.assertFalse((template / name).exists())
        self.assertIn("TEMPLATE ONLY", binding["note"])
        gate = (ROOT / "runtime/tools/bi01_run_gate.py").read_text(encoding="utf-8")
        self.assertIn('RUN = "runs/BI-01-V2-02"', gate)


if __name__ == "__main__":
    unittest.main()
