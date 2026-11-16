"""Synthetic checks; these fixtures are NOT real Owner GO or Run receipts."""
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "multi_run_check.py"
SPEC = importlib.util.spec_from_file_location("multi_run_check", SCRIPT)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)
SHA = "a" * 40


def run(rid, workspace):
    return {
        "run_id": rid,
        "work_id": "synthetic-work",
        "business_case_id": "synthetic-case",
        "binding_ref": f"daowei2026/observe-iterate@{SHA}:longrun/runs/{rid}/RUN_BINDING.json",
        "resource_binding_ref": f"daowei2026/observe-iterate@{SHA}:longrun/runs/{rid}/RUN_RESOURCE_BINDING.json",
        "owner_workspace_path": workspace,
        "adopted_protocol_ref": f"daowei2026/observe-iterate@{SHA}:longrun/contracts/LONGRUN_PROTOCOL_V2.md",
    }


def registry(entries):
    return {"schema": MOD.SCHEMA, "runs": entries}


class MultiRunCheckTest(unittest.TestCase):
    def test_empty_registry_bootstrap(self):
        self.assertEqual(MOD.validate_registry(registry({}))["run_count"], 0)

    def test_different_workspaces(self):
        r = registry({"A": run("A", "/tmp/run-a"), "B": run("B", "/tmp/run-b")})
        self.assertEqual(MOD.validate_registry(r)["run_count"], 2)

    def test_same_directory_fails(self):
        r = registry({"A": run("A", "/tmp/work"), "B": run("B", "/tmp/work")})
        with self.assertRaisesRegex(MOD.CheckError, "workspace overlap"):
            MOD.validate_registry(r)

    def test_parent_directory_fails(self):
        r = registry({"A": run("A", "/tmp/work"), "B": run("B", "/tmp/work/child")})
        with self.assertRaisesRegex(MOD.CheckError, "workspace overlap"):
            MOD.validate_registry(r)

    def test_invalid_relative_path(self):
        with self.assertRaisesRegex(MOD.CheckError, "absolute Linux path"):
            MOD.validate_registry(registry({"A": run("A", "relative") }))

    def test_identity_and_ref_are_run_scoped(self):
        r = registry({"A": run("B", "/tmp/run-a")})
        with self.assertRaisesRegex(MOD.CheckError, "run_id mismatch"):
            MOD.validate_registry(r)
        r["runs"]["A"]["run_id"] = "A"
        with self.assertRaisesRegex(MOD.CheckError, "reference must point"):
            MOD.validate_registry(r)

    def test_incorrect_ref_sha(self):
        r = registry({"A": run("A", "/tmp/run-a")})
        r["runs"]["A"]["binding_ref"] = "owner/repo@main:longrun/runs/A/RUN_BINDING.json"
        with self.assertRaisesRegex(MOD.CheckError, "not an exact"):
            MOD.validate_registry(r)

    def test_symlinks_on_actual_worker_host(self):
        with tempfile.TemporaryDirectory() as root:
            a = os.path.join(root, "a")
            b = os.path.join(root, "b")
            os.mkdir(a)
            os.symlink(a, b)
            r = registry({"A": run("A", a), "B": run("B", b)})
            self.assertEqual(MOD.validate_registry(r)["run_count"], 2)
            with self.assertRaisesRegex(MOD.CheckError, "workspace overlap"):
                MOD.validate_registry(r, on_worker_host=True)

    def test_local_worker_host_missing_directory(self):
        r = registry({"A": run("A", "/tmp/not-existing-oi-multirun-example")})
        with self.assertRaisesRegex(MOD.CheckError, "does not exist"):
            MOD.validate_registry(r, on_worker_host=True)


if __name__ == "__main__":
    unittest.main()
