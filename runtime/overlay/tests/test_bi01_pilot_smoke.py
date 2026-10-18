"""BI-01 dispatch smoke using synthetic Git records only; never phones, Pro or live work."""
import copy
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

OVERLAY = Path(__file__).resolve().parents[1]
ROOT = OVERLAY.parents[1]
MODULE = OVERLAY / "tools" / "management_prompt.py"
spec = importlib.util.spec_from_file_location("bi01_dispatch_under_test", MODULE)
dispatch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dispatch)

GOAL = "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md"
S2 = "professional/v2/01_AIDATA_CHART_AND_DATA.md"
CONFIG = "runtime/config/COORDINATOR_DISPATCH.json"


class BI01Smoke(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.repo = Path(tmp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic Fixture")
        self.git("config", "user.email", "synthetic@example.invalid")

        self.write(dispatch.POLICY_PATH,
                   (OVERLAY / "08_自然语言运行提示_v0.3.md").read_text(encoding="utf-8"))
        self.write(GOAL, (ROOT / GOAL).read_text(encoding="utf-8"))
        self.write(S2, (ROOT / S2).read_text(encoding="utf-8"))
        cfg = json.loads((ROOT / CONFIG).read_text(encoding="utf-8"))
        self.assertEqual(cfg["works"]["BI-01"]["stage"], "BI01")
        cfg["repository"] = "test/repo"  # Synthetic repository identity only.
        self.write(CONFIG, json.dumps(cfg, ensure_ascii=False))
        self.write("task.md", "合成S2任务：分析可信结果，提出反证，不冒称管理审核。")
        self.write("authority.md", "合成试验授权（仅脱机fixture）；禁止真实发送。")
        self.write("plan.md", "合成管理计划：S2当前阶段；预算不授权派发。")
        self.write("questions.md", '<a id="m-start"></a>以完整Goal作首次管理；本示例不代替Owner授权。')
        self.policy = self.commit("synthetic immutable policy and business source")

    def write(self, name, value):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE
        ).decode("utf-8").strip()

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def loc(self, path, commit=None, selector="full"):
        return {"repo": "test/repo", "commit": commit or self.policy,
                "path": path, "selector": selector}

    def event(self, kind, commit):
        return {
            "work_id": "BI-01", "invocation_id": "synthetic-one",
            "assignment_token": "synthetic-token",
            "binding_ref": self.loc(kind, commit),
            "route": "same_work", "send_state": "NOT_SENT",
            "dispatch_kind": "NORMAL",
            "current_task_ref": self.loc("task.md"),
            "task_adoption_ref": self.loc("authority.md"),
        }

    def make_binding(self, mode="OBSERVATION_CHART", role="professional"):
        binding = {
            "schema": "question-work/v2", "kind": "BINDING", "work_id": "BI-01",
            "professional_mode": mode, "goal_ref": self.loc(GOAL),
            "plan_ref": self.loc("plan.md"), "budget_ref": self.loc("plan.md"),
            "full_scope_ref": self.loc("task.md"),
            "focus_ref": self.loc("task.md"),
            "deliverables_ref": self.loc("task.md"),
            "completion_ref": self.loc("task.md"),
            "routes": {"same_work": {
                "recipient_role": role, "recipient_ref": role + "-synthetic",
                "instructions_ref": self.loc("task.md"),
            }},
            "triggers": [],
            "source_reads": [{
                "source": self.loc(S2), "requirement": "FOCUS_FULL",
                "purpose": "合成S2观察与反证来源；需要真实接收者按原文读取",
            }],
        }
        self.write("binding.json", json.dumps(binding, ensure_ascii=False))
        return self.commit("synthetic S2 binding")

    def test_bootstrap_first_management(self):
        boot = {
            "schema": "question-work/v2", "kind": "BOOTSTRAP",
            "work_id": "BI-01", "goal_ref": self.loc(GOAL),
            "authority_ref": self.loc("authority.md"),
            "entry_sources": [self.loc("task.md")], "existing_work_refs": [],
            "parent": {"status": "NOT_APPLICABLE_NEW_CASE", "ref": None,
                       "reason_ref": self.loc("task.md")},
            "recipient_ref": "management-synthetic",
            "return_to_ref": "synthetic-controller",
            "question_ref": self.loc("questions.md", selector="#m-start"),
            "instructions_ref": self.loc("task.md"),
        }
        self.write("bootstrap.json", json.dumps(boot, ensure_ascii=False))
        bound_commit = self.commit("synthetic bootstrap")
        event = self.event("bootstrap.json", bound_commit)
        prepared = dispatch.prepare_dispatch(self.repo, self.policy, CONFIG, event)
        self.assertEqual((prepared["role"], prepared["mode"], prepared["stage"]),
                         ("management", "M-START", "BI01"))
        self.assertIn("07_BUSINESS_SCENE_OBSERVATION_METHOD.md", prepared["message"])
        self.assertIn("基础 K线/贴近转折", prepared["message"])
        self.assertIn("强弱", prepared["message"])
        self.assertIn("04_BI01_BUSINESS_BASELINE.md", prepared["message"])
        self.assertIn("06_U2_U3_DESIGN_SOURCE_MAP.md", prepared["message"])
        self.assertFalse(prepared["sent"])
        self.assertFalse(prepared["semantic_review_passed"])
        dispatch.verify(prepared, prepared["message"].encode("utf-8"))
        with self.assertRaisesRegex(ValueError, "MESSAGE_CHANGED"):
            dispatch.verify(prepared, prepared["message"].encode("utf-8") + b" ")

    def test_s2_professional_with_exact_source_and_recipient(self):
        bound_commit = self.make_binding()
        event = self.event("binding.json", bound_commit)
        prepared = dispatch.prepare_dispatch(self.repo, self.policy, CONFIG, event)
        self.assertEqual((prepared["role"], prepared["mode"], prepared["stage"]),
                         ("professional", "OBSERVATION_CHART", "BI01"))
        self.assertEqual(prepared["recipient"], "professional-synthetic")
        self.assertIn("专业任务 BI01", prepared["message"])
        self.assertIn(S2, prepared["message"])
        self.assertIn("本checkout已核位置", prepared["message"])
        self.assertFalse(prepared["sent"])
        dispatch.verify(prepared, prepared["message"].encode("utf-8"))
        with self.assertRaisesRegex(ValueError, "NOT_SAFE_TO_SEND"):
            event["send_state"] = "UNKNOWN"
            dispatch.prepare_dispatch(self.repo, self.policy, CONFIG, event)

    def test_review_route_remains_partial_not_accepted(self):
        bound_commit = self.make_binding(mode="INDEPENDENT_REVIEW", role="review")
        prepared = dispatch.prepare_dispatch(
            self.repo, self.policy, CONFIG, self.event("binding.json", bound_commit))
        self.assertEqual(prepared["role"], "review")
        self.assertEqual(prepared["mode"], "INDEPENDENT_REVIEW")
        self.assertIn("PARTIAL", prepared["message"])
        self.assertFalse(prepared["semantic_review_passed"])
        self.assertFalse(prepared["sent"])


if __name__ == "__main__":
    unittest.main()
