"""Run/Binding isolation with synthetic local Git only; never authorizes sending."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "runtime/tools/bi01_run_gate.py"
spec = importlib.util.spec_from_file_location("run_identity_gate", TOOL)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class RunIdentityTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.repo = Path(tmp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic Test")
        self.git("config", "user.email", "synthetic@example.invalid")
        self.old = "BI-01-V2-02"
        self.new = "BI-01-CASE-TEST"
        self.custom = "runs/" + self.new + "/WORKMAP_BINDING.json"
        self.seed(self.old, gate.BINDING)
        self.seed(self.new, self.custom)
        self.ref = self.commit()

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE
        ).decode().strip()

    def write(self, path, content):
        p = self.repo / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-qm", "synthetic fixture only")
        return self.git("rev-parse", "HEAD")

    def seed(self, run, binding):
        r = "runs/" + run
        paths = [r + "/README.md", r + "/00_长程推进地图.md", r + "/01_当前任务.md"]
        for path in paths:
            self.write(path, "Synthetic; no real business or GO.\n")
        receipt = r + "/reviews/WORKMAP_INTAKE_CURRENT.json"
        self.write(receipt, json.dumps({"schema": "workmap-intake/v1", "intakes": {"bi01": {}}}))
        self.write(binding, json.dumps({
            "schema": "workmap-binding/v2", "status": "ADOPTED",
            "overview": {"path": paths[0]}, "receipt_path": receipt,
            "streams": {"bi01": {"map": {"path": paths[1]}, "task": paths[2]}},
        }, ensure_ascii=False))

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, str(TOOL), "status", "--repo", str(self.repo),
             "--ref", self.ref, *args], capture_output=True, text=True, timeout=15)

    def test_cli_requires_explicit_run(self):
        result = self.cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("--run-id", result.stderr)

    def test_selected_binding_is_used(self):
        view = gate.Git(self.repo, self.ref, self.new, self.custom)
        self.assertEqual(gate.active_binding(view), [])
        self.assertEqual(view.binding_path, self.custom)
        self.assertEqual(view.invocation_prefix, "BI01-CASE-TEST")

    def test_global_old_binding_cannot_adopt_new_run(self):
        errors = gate.active_binding(gate.Git(self.repo, self.ref, self.new))
        self.assertTrue(any(e.startswith("WORKMAP_PATH_MISMATCH:") for e in errors))

    def test_cli_selected_binding_never_claims_authority(self):
        result = self.cli("--run-id", self.new, "--binding", self.custom)
        self.assertEqual(result.returncode, 0, result.stderr)
        obj = json.loads(result.stdout)
        self.assertTrue(obj["adoption_mechanically_present"])
        self.assertFalse(obj["sent"])
        self.assertFalse(obj["business_gate"])
        self.assertIsNone(obj["run_started"])

    def test_missing_selected_binding_does_not_fall_back(self):
        errors = gate.active_binding(gate.Git(self.repo, self.ref, self.old, "missing.json"))
        self.assertEqual(errors, ["WORKMAP_BINDING_UNREADABLE"])

    def test_nonadopted_binding_does_not_borrow_old_adoption(self):
        self.write(self.custom, '{"schema":"workmap-binding/v2","status":"NOT_CONFIGURED"}')
        self.ref = self.commit()
        errors = gate.active_binding(gate.Git(self.repo, self.ref, self.new, self.custom))
        self.assertEqual(errors, ["WORKMAP_NOT_ADOPTED"])

    def test_unsafe_binding_paths_rejected(self):
        for path in ("../other.json", "/tmp/other.json", "a\\b.json", "-bad.json", ""):
            with self.subTest(path=path), self.assertRaises(ValueError):
                gate.Git(self.repo, self.ref, self.new, path)

    def test_old_run_with_explicit_identity_remains_supported(self):
        self.assertEqual(gate.active_binding(gate.Git(self.repo, self.ref, self.old)), [])

    def test_invalid_run_id_rejected(self):
        with self.assertRaisesRegex(ValueError, "INVALID_RUN_ID"):
            gate.Git(self.repo, self.ref, "../old", self.custom)


if __name__ == "__main__":
    unittest.main()
