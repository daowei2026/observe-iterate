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
