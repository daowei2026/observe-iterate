"""Guard current-branch V2 history trimming without treating historical methods as active."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "professional/v2"
RETAINED = (
    "README.md",
    "04_BI01_BUSINESS_BASELINE.md",
    "06_U2_U3_DESIGN_SOURCE_MAP.md",
    "07_BUSINESS_SCENE_OBSERVATION_METHOD.md",
)
SUPERSEDED = (
    "00_PURPOSE_AND_THREE_STEP_FLOW.md",
    "01_AIDATA_CHART_AND_DATA.md",
    "02_OBSERVATION_IDEAS_AND_VALIDATION.md",
    "03_EXECUTION_HANDOFF.md",
    "05_BI01_FIXED_INPUT_DATA.md",
)
HISTORY_COMMIT = "c7971cc616e09db47681abc868e77acdc272f84a"


class V2HistoryBoundary(unittest.TestCase):
    def test_only_selected_v2_knowledge_remains(self):
        self.assertEqual({p.name for p in V2.iterdir() if p.is_file()}, set(RETAINED))
        for name in SUPERSEDED:
            self.assertFalse((V2 / name).exists())
        self.assertIn(HISTORY_COMMIT, (V2 / "README.md").read_text(encoding="utf-8"))

    def test_old_runs_only_available_from_fixed_history(self):
        for run in ("BI-01-V2-01", "BI-01-V2-02"):
            self.assertFalse((ROOT / "runs" / run).exists())
            history = (ROOT / "runs/history" / (run + ".md")).read_text(encoding="utf-8")
            self.assertIn(HISTORY_COMMIT, history)
            self.assertIn("/runs/" + run, history)

    def test_active_feature_work_and_run_still_exist(self):
        self.assertTrue((ROOT / "professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md").is_file())
        self.assertTrue((ROOT / "professional/feature_observation/03_REUSE_FROM_V2.md").is_file())
        self.assertTrue((ROOT / "runs/BI-01-FO-01/01_当前任务.md").is_file())
        self.assertTrue((ROOT / "runs/BI-01-FO-01/provenance").is_dir())
        self.assertIn("BI-01-FO-01", (ROOT / "runs/README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
