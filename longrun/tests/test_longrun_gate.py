"""Offline positive/negative fixtures. They do not prove authenticated transport or GitHub side effects."""
import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from longrun_gate import check

RUN = "OI-20261114-01"
REPO = "daowei2026/observe-iterate"
SHA = "a" * 40
M = "chatgpt:" + RUN + ":manager"
E = "chatgpt:" + RUN + ":executor:p1"
W = "codex:" + RUN + ":worker:w1"
Q = "operation=read-test execution_context=repo:branch:workspace allowed_writes=repo/path"


def ref(suffix):
    return REPO + "@" + SHA + ":longrun/runs/" + RUN + "/" + suffix


def fixture():
    b_ref = ref("RUN_BINDING.json")
    owner = ref("OWNER_START.md")
    d_ref = ref("delegations/D001/DELEGATION.json")
    o_ref = ref("work_orders/W001/ORDER.json")
    m_inv = ref("calls/C0001/INVOCATION.json")
    m_ret = ref("calls/C0001/PRO_RETURN.json")
    e_inv = ref("calls/C0002/INVOCATION.json")
    e_ret = ref("calls/C0002/PRO_RETURN.json")
    w_ret = ref("worker_results/W001/WORKER_RETURN.json")
    evidence = ref("worker_results/W001/RESULT.json")
    grant = dict(operation="read-test", execution_context="repo:branch:workspace",
                 allowed_writes=["repo/path"], authority_quote=Q)
    binding = dict(schema="longrun-binding/v2", run_id=RUN, work_id="WORK-A",
                   owner_go_ref=owner, coordinator="codex:controller",
                   manager=M, executors=[E], workers=[W], grants=[grant])
    d = dict(schema="longrun-delegation/v2", run_id=RUN, delegation_id="D001",
             issuer_call_id="C0001", issuer=M, recipient=E, return_to=M,
             task_ref=owner, business_context_ref=None, input_refs=[owner],
             expected_outputs=["professional-report"], permitted_operations=["read-test"],
             allowed_writes=["repo/path"])
    o = dict(schema="longrun-order/v2", run_id=RUN, work_order_id="W001",
             delegation_ref=d_ref, issuer_call_id="C0002", issuer=E, worker=W,
             return_to=E, instructions_ref=ref("work_orders/W001/ORDER.md"),
             input_refs=[owner], deliverables=["result"], grant=copy.deepcopy(grant))
    m = dict(schema="longrun-professional-return/v2", run_id=RUN, call_id="C0001",
             role="manager", sender=M, delegation_ref=None, return_to=None,
             result_ref=ref("calls/C0001/FULL_RESPONSE.md"), issued_delegation_refs=[d_ref],
             issued_order_refs=[], accepted_worker_refs=[], professional_state="IN_PROGRESS",
             remaining_scope_ref=owner, continuation_ref=None, owner_request_ref=None)
    e = dict(schema="longrun-professional-return/v2", run_id=RUN, call_id="C0002",
             role="executor", sender=E, delegation_ref=d_ref, return_to=M,
             result_ref=ref("calls/C0002/FULL_RESPONSE.md"), issued_delegation_refs=[],
             issued_order_refs=[o_ref], accepted_worker_refs=[], professional_state="IN_PROGRESS",
             remaining_scope_ref=owner, continuation_ref=None, owner_request_ref=None)
    mi = dict(schema="longrun-invocation/v2", run_id=RUN, call_id="C0001",
              recipient=M, token="T111", assignment_ref=owner, origin_ref=None,
              source_refs=[owner])
    ei = dict(schema="longrun-invocation/v2", run_id=RUN, call_id="C0002",
              recipient=E, token="T222", assignment_ref=d_ref, origin_ref=owner,
              source_refs=[owner, d_ref])
    worker = dict(schema="longrun-worker-return/v2", run_id=RUN,
                  work_order_id="W001", order_ref=o_ref, worker=W, return_to=E,
                  outcome="EXECUTED", result_ref=ref("worker_results/W001/FULL_RESPONSE.md"),
                  missing=[], manifest={"result": {"ref": evidence, "sha256": "1" * 64}})
    return dict(
        mode="resume", binding_ref=b_ref, run_index={RUN: b_ref},
        owner_go_text=Q, binding=binding,
        delegation=d, delegation_ref=d_ref, delegation_index={"D001": d_ref},
        order=o, order_ref=o_ref, order_index={"W001": o_ref},
        manager_return=m, manager_return_ref=m_ret, manager_invocation=mi,
        manager_invocation_ref=m_inv,
        manager_receipt=dict(call_id="C0001", recipient=M, token="T111",
                             invocation_ref=m_inv, return_ref=m_ret),
        executor_return=e, executor_return_ref=e_ret, executor_invocation=ei,
        executor_invocation_ref=e_inv,
        executor_receipt=dict(call_id="C0002", recipient=E, token="T222",
                              invocation_ref=e_inv, return_ref=e_ret),
        worker_return=worker, worker_return_ref=w_ret,
        worker_receipt=dict(worker=W, order_ref=o_ref, return_ref=w_ret),
        verified_evidence_sha256={evidence: "1" * 64},
        verified_worker_return_refs=[],
        actions={RUN + "/W001": ["NOT_SENT"]},
        workspace_available=True,
        physical_bindings={M: "manager-chat", E: "executor-chat", W: "worker-thread"},
        invocation=mi, invocation_ref=m_inv, call_index={"C0001": m_inv},
        previous_tokens=[], verified_origin_refs=[],
    )


class LongrunV2Tests(unittest.TestCase):
    def setUp(self):
        self.c = fixture()

    def block(self, action):
        with self.assertRaises((ValueError, Exception)):
            check(action, self.c)

    def test_binding_delegation_and_worker_preflight(self):
        self.assertEqual(check("validate-binding", self.c)["run_id"], RUN)
        self.c["actions"][RUN + "/C0001"] = ["NOT_SENT"]
        self.assertEqual(check("validate-invocation", self.c)["recipient"], M)
        self.assertEqual(check("validate-delegation", self.c)["recipient"], E)
        self.assertEqual(check("validate-order", self.c)["recipient"], W)

    def test_executor_invocation_from_verified_origin(self):
        self.c["invocation"] = self.c["executor_invocation"]
        self.c["invocation_ref"] = self.c["executor_invocation_ref"]
        self.c["call_index"] = {"C0002": self.c["executor_invocation_ref"]}
        self.c["verified_origin_refs"] = [self.c["binding"]["owner_go_ref"]]
        self.c["actions"][RUN + "/C0002"] = ["NOT_SENT"]
        self.assertEqual(check("validate-invocation", self.c)["recipient"], E)
        self.c["previous_tokens"] = ["T222"]
        self.block("validate-invocation")

    def test_invocation_missing_physical_binding(self):
        self.c["actions"][RUN + "/C0001"] = ["NOT_SENT"]
        self.c["physical_bindings"] = {}
        self.block("validate-invocation")

    def test_bad_manager_issuance_blocks_delegation(self):
        self.c["manager_return"]["issued_delegation_refs"] = []
        self.block("validate-delegation")

    def test_unverified_professional_receipt_blocks(self):
        self.c["executor_receipt"]["token"] = "wrong"
        self.block("validate-order")

    def test_worker_order_is_not_manager_order(self):
        self.c["order"]["issuer"] = M
        self.block("validate-order")

    def test_worker_returns_to_executor_not_manager(self):
        self.c["order"]["return_to"] = M
        self.block("validate-order")

    def test_order_cannot_expand_owner_authority(self):
        self.c["order"]["grant"]["allowed_writes"] = ["repo/other"]
        self.block("validate-order")

    def test_order_cannot_expand_delegation(self):
        self.c["delegation"]["permitted_operations"] = ["write-anything"]
        self.block("validate-order")

    def test_workspace_lock_is_not_assumed(self):
        self.c["workspace_available"] = False
        self.block("validate-order")

    def test_unknown_send_must_not_be_resent(self):
        self.c["actions"][RUN + "/W001"] = ["NOT_SENT", "UNKNOWN"]
        self.block("validate-order")

    def test_worker_return_goes_to_executor(self):
        self.c["actions"][RUN + "/W001"] = ["NOT_SENT", "IN_FLIGHT"]
        r = check("validate-worker-return", self.c)
        self.assertEqual(r["recipient"], E)
        self.assertEqual(r["action"], "RETURN_TO_EXECUTOR")
        self.c["result_kind"] = "worker"
        self.assertEqual(check("route-return", self.c)["recipient"], E)

    def test_missing_verified_digest_blocks(self):
        self.c["actions"][RUN + "/W001"] = ["NOT_SENT", "IN_FLIGHT"]
        self.c["verified_evidence_sha256"] = {}
        self.block("validate-worker-return")

    def test_worker_return_deduplicated(self):
        self.c["actions"][RUN + "/W001"] = ["NOT_SENT", "IN_FLIGHT", "COMPLETED"]
        self.c["completed_worker_refs"] = {"W001": self.c["worker_return_ref"]}
        self.assertEqual(check("validate-worker-return", self.c)["action"], "NOOP")
        self.c["completed_worker_refs"] = {"W001": ref("different/WORKER_RETURN.json")}
        self.block("validate-worker-return")

    def test_direct_executor_completion_needs_no_worker(self):
        e = self.c["executor_return"]
        e.update(issued_order_refs=[], professional_state="REPORTED_COMPLETE",
                 remaining_scope_ref=None)
        r = check("validate-executor-return", self.c)
        self.assertEqual(r["return_to"], M)
        self.c["result_kind"] = "executor"
        self.assertEqual(check("route-return", self.c)["recipient"], M)

    def test_executor_cannot_self_certify_worker_result(self):
        e = self.c["executor_return"]
        e["accepted_worker_refs"] = [self.c["worker_return_ref"]]
        self.block("validate-executor-return")
        self.c["verified_worker_return_refs"] = [self.c["worker_return_ref"]]
        self.assertEqual(check("validate-executor-return", self.c)["return_to"], M)

    def test_action_history_and_cross_run_rejected(self):
        self.assertEqual(check("reconcile-actions", self.c)[RUN + "/W001"], "NOT_SENT")
        self.c["actions"] = {RUN + "/W001": ["NOT_SENT", "IN_FLIGHT", "UNKNOWN", "IN_FLIGHT"]}
        self.assertEqual(check("reconcile-actions", self.c)[RUN + "/W001"], "IN_FLIGHT")
        self.c["actions"] = {"FOREIGN/W001": ["NOT_SENT"]}
        self.block("reconcile-actions")

    def test_unadopted_binding_blocks_all(self):
        self.c["run_index"] = {}
        self.block("validate-binding")

    def test_path_traversal_rejected(self):
        self.c["binding_ref"] = REPO + "@" + SHA + ":longrun/runs/../RUN_BINDING.json"
        self.block("validate-binding")

    def test_manager_complete_not_parent_task_gate(self):
        m = self.c["manager_return"]
        m.update(issued_delegation_refs=[], professional_state="REPORTED_COMPLETE",
                 remaining_scope_ref=None)
        r = check("validate-manager-return", self.c)
        self.assertEqual(r["return_to"], "PROFESSIONAL_OWNER_DECISION")


if __name__ == "__main__":
    unittest.main()
