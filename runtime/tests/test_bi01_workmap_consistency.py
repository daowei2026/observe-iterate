"""Offline Git fixture: R-round transport must not invalidate adopted Workmap intake."""
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "bi01_workmap_gate_under_test", PROJECT / "runtime" / "overlay" / "tools" / "workmap_gate.py"
)
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)
BINDING = "runtime/config/WORKMAP_BINDING.json"
RUN = "runs/BI-01-V2-02"


class WorkmapSnapshotOffline(unittest.TestCase):
    def setUp(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        self.repo = Path(td.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic Tester")
        self.git("config", "user.email", "synthetic@example.invalid")
        b = json.loads((PROJECT / "runtime/operations/v2/templates/WORKMAP_BINDING_TEMPLATE.json").read_text())
        b["status"] = "ADOPTED"  # synthetic only, never commit this into real repo.
        self.write(BINDING, json.dumps(b, ensure_ascii=False))
        self.write(RUN + "/README.md", (PROJECT / RUN / "README.md").read_text())
        for path in b["owner_sources"] + b["rule_paths"]:
            if not (self.repo / path).exists():
                self.write(path, "Synthetic document: " + path + "\n")
        for target in ("runtime/operations/BI01_V2_RUN_GUIDE.md",
                       "runtime/operations/V2_ROUND_RECORD_CONTRACT.md"):
            self.write(target, "Synthetic linked target.\n")
        self.write(
            RUN + "/00_长程推进地图.md",
            "\n".join(
                '<a id="' + name + '"></a>\n## ' + name + '\nSynthetic manager-owned work area.'
                for name in b["streams"]["bi01"]["map"]["anchors"]
            ),
        )
        self.write(RUN + "/01_当前任务.md", "task_id: synthetic-task\nSynthetic task only.")
        self.decision = RUN + "/reviews/management-R0001/DECISION.md"
        self.write(self.decision, "Synthetic manager receipt; not real authorization.")
        self.a = self.commit("synthetic manager map without intake")
        initial = gate.snapshot(self.repo, self.a, BINDING, "bi01")
        report_oid = self.git("rev-parse", self.a + ":" + self.decision)
        task = b["streams"]["bi01"]["task"]
        task_oid = self.git("rev-parse", self.a + ":" + task)
        receipt = {
            "schema": "workmap-intake/v1",
            "intakes": {
                "bi01": {
                    "snapshot": initial["fingerprint"],
                    "manager": {"role": "management_review", "context": "synthetic-manager"},
                    "decision_report": {"path": self.decision, "blob": report_oid},
                    "reader_check": {"status": "PENDING"},
                    "dispatch": {"decision": "ISSUED", "task_id": "synthetic-task",
                                 "task_path": task, "task_blob": task_oid,
                                 "kind": "EXISTING_AUTHORIZED_REPAIR",
                                 "requires_reader_check": False,
                                 "reader_reason": "Synthetic local test only",
                                 "method_paths": [b["rule_paths"][0]]},
                    "validation_claims": [],
                },
            },
        }
        self.write(b["receipt_path"], json.dumps(receipt, ensure_ascii=False))
        self.b = self.commit("synthetic durable intake")
        self.assertEqual(gate.snapshot(self.repo, self.b, BINDING, "bi01")["fingerprint"],
                         initial["fingerprint"])

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE
        ).decode().strip()

    def write(self, name, content):
        p = self.repo / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def test_new_round_transport_does_not_self_stale_workmap(self):
        self.write(RUN + "/provenance/turns/R0002/PROMPT.md", "Synthetic prepared round.")
        c = self.commit("synthetic pending round transport")
        self.assertEqual(gate.snapshot(self.repo, self.b, BINDING, "bi01")["fingerprint"],
                         gate.snapshot(self.repo, c, BINDING, "bi01")["fingerprint"])
        result = gate.check(self.repo, c, BINDING, "bi01")
        self.assertNotIn("INTAKE_STALE", result["errors"])

    def test_substantive_artifact_requires_new_management_intake(self):
        self.write(RUN + "/artifacts/SYNTHETIC.md", "Synthetic new substantive result.")
        c = self.commit("synthetic substantive result")
        result = gate.check(self.repo, c, BINDING, "bi01")
        self.assertIn("INTAKE_STALE", result["errors"])


if __name__ == "__main__":
    unittest.main()
