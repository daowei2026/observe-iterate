"""Offline-only BI-01 round gate tests; no Pro, phone, business inputs or sending."""
import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
MODULE_PATH = PROJECT / "runtime" / "tools" / "bi01_run_gate.py"
spec = importlib.util.spec_from_file_location("bi01_gate_under_test", MODULE_PATH)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

RUN = "runs/BI-01-V2-01"
ROLE = "management"
RID = "R0001"
INV = "BI01-V2-01-R0001-synthetic-unique-a"
MARKER = "[" + INV + "]"


class RoundGateOffline(unittest.TestCase):
    def setUp(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        self.repo = Path(td.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic Tester")
        self.git("config", "user.email", "synthetic@example.invalid")
        self.write(RUN + "/README.md", "# Synthetic pending run\n")
        self.write(RUN + "/OWNER_START.md", "Synthetic Owner GO; not a real authority.\n")
        self.write(RUN + "/BOOTSTRAP.json", json.dumps({"schema": "question-work/v2", "kind": "BOOTSTRAP", "work_id": "BI-01"}))
        self.write("runtime/config/WORKMAP_BINDING.json", '{"schema":"workmap-binding/v2","status":"NOT_CONFIGURED"}')
        self.policy = self.commit("synthetic source baseline")
        self.owner = self.loc(RUN + "/OWNER_START.md")
        self.bootstrap = self.loc(RUN + "/BOOTSTRAP.json")
        self.prompt = MARKER + "\nSynthetic message; NO PHONE.\n"
        self.record = {
            "schema": "bi01-invocation/v1",
            "run_id": "BI-01-V2-01",
            "round_id": RID,
            "work_id": "BI-01",
            "invocation_id": INV,
            "assignment_token": "synthetic-unique-token",
            "round_marker": MARKER,
            "role": ROLE,
            "recipient_ref": "synthetic-management-chat",
            "policy_commit": self.policy,
            "prompt_sha256": hashlib.sha256(self.prompt.encode()).hexdigest(),
            "bootstrap_ref": self.bootstrap,
            "binding_ref": self.bootstrap,
            "current_task_ref": self.owner,
            "task_adoption_ref": self.owner,
            "question_work_required": True,
        }
        self.save_invocation()
        self.current = self.commit("synthetic first management invocation")

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE
        ).decode().strip()

    def write(self, name, raw):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(raw, encoding="utf-8")

    def save_invocation(self):
        p = RUN + "/provenance/turns/" + RID + "/"
        self.write(p + "INVOCATION.json", json.dumps(self.record, ensure_ascii=False))
        self.write(p + "PROMPT.md", self.prompt)

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def loc(self, path):
        return {"repo": "daowei2026/observe-iterate", "commit": self.policy,
                "path": path, "selector": "full"}

    def view(self):
        return gate.Git(self.repo, self.current)

    def test_first_management_bootstrap_is_preparable_without_map(self):
        result = gate.pre_dispatch(self.view(), RID)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["recorded_send_state"], "NOT_RECORDED")
        self.assertEqual(result["sent"], False)

    def test_exact_first_line_and_marker_are_required(self):
        self.record["round_marker"] = "[DIFFERENT]"
        self.save_invocation()
        self.current = self.commit("synthetic wrong marker")
        errors = gate.pre_dispatch(self.view(), RID)["errors"]
        self.assertIn("ROUND_MARKER_OR_INVOCATION_MISMATCH", errors)
        self.assertIn("PROMPT_FIRST_LINE_NOT_SCHEDULER_MARKER", errors)

    def test_professional_cannot_use_unadopted_workmap(self):
        self.record["role"] = "professional"
        self.record.pop("bootstrap_ref")
        self.save_invocation()
        self.current = self.commit("synthetic professional without map")
        result = gate.pre_dispatch(self.view(), RID)
        self.assertFalse(result["ok"])
        self.assertIn("WORKMAP_NOT_ADOPTED", result["errors"])

    def test_unknown_send_cannot_be_resent(self):
        p = RUN + "/provenance/turns/" + RID + "/SEND_RECEIPT.json"
        self.write(p, json.dumps({"state": "UNKNOWN"}))
        self.current = self.commit("synthetic unknown send")
        result = gate.pre_dispatch(self.view(), RID)
        self.assertFalse(result["ok"])
        self.assertIn("SEND_NOT_SAFE:UNKNOWN", result["errors"])

    def test_real_returns_are_not_inferred(self):
        result = gate.after_return(self.view(), RID)
        self.assertFalse(result["ok"])
        self.assertIn("NO_CONFIRMED_SEND_FOR_RETURN", result["errors"])
        self.assertIn("ROLE_RETURN_MISSING", result["errors"])
        self.assertIn("QUESTION_WORK_RETURN_MISSING", result["errors"])

    def test_both_returns_must_match_the_actual_invocation(self):
        p = RUN + "/provenance/turns/" + RID + "/"
        self.write(p + "SEND_RECEIPT.json", json.dumps({"state": "COMMITTED"}))
        self.write(p + "FULL_RESPONSE.md", "Synthetic complete reply; not a business result.\n")
        self.write(p + "ROLE_RETURN.json", json.dumps({
            "schema": "longrun-return/v1", "work_id": "BI-01",
            "invocation_id": INV, "assignment_token": self.record["assignment_token"],
            "question_work_ref": "#question-work-return",
        }))
        question = {
            "schema": "question-work/v2", "kind": "RETURN",
            "work_id": "BI-01", "invocation_id": INV,
            "binding_ref": self.bootstrap,
            "focus_results": [{"question_id": "M-START"}],
            "trigger_observations": [], "continuation_ref": self.owner,
        }
        self.write(p + "QUESTION_WORK_RETURN.json", json.dumps(question))
        self.current = self.commit("synthetic two return records")
        result = gate.after_return(self.view(), RID)
        self.assertTrue(result["ok"], result)
        question["binding_ref"] = self.owner
        self.write(p + "QUESTION_WORK_RETURN.json", json.dumps(question))
        self.current = self.commit("synthetic wrong binding")
        result = gate.after_return(self.view(), RID)
        self.assertIn("QUESTION_WORK_RETURN_BINDING_MISMATCH", result["errors"])


if __name__ == "__main__":
    unittest.main()
