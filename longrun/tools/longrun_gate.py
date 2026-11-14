#!/usr/bin/env python3
"""Read-only longrun V2 mechanical checks. No dispatch, lock, GitHub read or professional judgment."""
import argparse
import json
from pathlib import Path
import re
import sys

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:
    raise SystemExit("Missing jsonschema; install it before running this offline gate") from exc

SCHEMA = json.loads(
    (Path(__file__).resolve().parents[1] / "contracts/longrun_schema_v2.json").read_text("utf-8")
)
ACTIONS = (
    "validate-binding", "validate-invocation", "validate-delegation", "validate-order",
    "validate-worker-return", "validate-executor-return", "validate-manager-return",
    "route-return", "reconcile-actions",
)
STATES = {"NOT_SENT", "IN_FLIGHT", "COMPLETED", "UNKNOWN", "BLOCKED", "SUPERSEDED"}
TRANSITIONS = {
    ("NOT_SENT", "IN_FLIGHT"), ("NOT_SENT", "UNKNOWN"),
    ("NOT_SENT", "BLOCKED"), ("NOT_SENT", "SUPERSEDED"),
    ("IN_FLIGHT", "COMPLETED"), ("IN_FLIGHT", "UNKNOWN"),
    ("IN_FLIGHT", "BLOCKED"), ("IN_FLIGHT", "SUPERSEDED"),
    ("UNKNOWN", "IN_FLIGHT"), ("UNKNOWN", "COMPLETED"),
    ("UNKNOWN", "BLOCKED"), ("UNKNOWN", "SUPERSEDED"),
    ("BLOCKED", "COMPLETED"), ("BLOCKED", "SUPERSEDED"),
}
REF_PATTERN = re.compile(r"^([\w.-]+/[\w.-]+)@([a-f0-9]{40}):([^\s:#]+)$", re.ASCII)


def require(condition, why):
    if not condition:
        raise ValueError(why)


def validated(kind, value):
    require(isinstance(value, dict), "missing " + kind)
    Draft202012Validator({"$defs": SCHEMA["$defs"], "$ref": "#/$defs/" + kind}).validate(value)
    return value


def ref_parts(ref):
    match = REF_PATTERN.fullmatch(ref)
    require(match, "not an immutable GitHub reference")
    repo, commit, path = match.groups()
    require("\\" not in path and all(p not in ("", ".", "..", ".git") for p in path.split("/")),
            "unsafe reference path")
    return repo, commit, path


def exact_path(ref, run, suffix):
    repo, _, path = ref_parts(ref)
    require(repo and path == "longrun/runs/" + run + "/" + suffix,
            "wrong identity/path: " + path)


def object_ref_fields(obj):
    for k, v in obj.items():
        if k.endswith("_ref") and isinstance(v, str):
            ref_parts(v)
        if k.endswith("_refs") and isinstance(v, list):
            for item in v:
                ref_parts(item)


def grant_covers(scope, candidate):
    return (
        scope["operation"] == candidate["operation"]
        and scope["execution_context"] == candidate["execution_context"]
        and candidate["authority_quote"] == scope["authority_quote"]
        and set(candidate["allowed_writes"]).issubset(scope["allowed_writes"])
    )


def binding(c):
    b = validated("binding", c.get("binding"))
    run = b["run_id"]
    exact_path(c["binding_ref"], run, "RUN_BINDING.json")
    require(b["manager"] == "chatgpt:" + run + ":manager", "bad manager logical identity")
    require(all(re.fullmatch(re.escape("chatgpt:" + run + ":executor:") + r"[A-Za-z0-9._-]+", x)
                for x in b["executors"]), "bad executor logical identity")
    require(all(re.fullmatch(re.escape("codex:" + run + ":worker:") + r"[A-Za-z0-9._-]+", x)
                for x in b["workers"]), "bad Worker logical identity")
    roles = [b["coordinator"], b["manager"], *b["executors"], *b["workers"]]
    require(len(roles) == len(set(roles)), "role identity collision")
    require(isinstance(c.get("run_index"), dict), "trusted adopted run index missing")
    if c.get("mode") == "new":
        require(run not in c["run_index"], "new run already registered")
        require(c.get("actual_owner_go_ref") == b["owner_go_ref"], "not original GO")
    else:
        require(c.get("mode") == "resume" and c["run_index"].get(run) == c["binding_ref"],
                "binding not adopted")
    owner = c.get("owner_go_text")
    require(isinstance(owner, str) and owner, "trusted Owner GO original unavailable")
    for grant in b["grants"]:
        quote = grant["authority_quote"]
        require(quote in owner, "owner grant not in original GO")
        require(all(x in quote for x in [grant["operation"], grant["execution_context"],
                                         *grant["allowed_writes"]]), "grant quote missing exact scope")
    return b


def invocation_preflight(c, b):
    i = validated("invocation", c.get("invocation"))
    run = b["run_id"]
    require(i["run_id"] == run and i["recipient"] in
            [b["manager"], *b["executors"]], "unbound professional recipient")
    exact_path(c["invocation_ref"], run, "calls/" + i["call_id"] + "/INVOCATION.json")
    require(c.get("call_index", {}).get(i["call_id"]) == c["invocation_ref"],
            "call ID missing/conflicting in trusted index")
    require(i["token"] not in c.get("previous_tokens", []), "invocation token reused")
    require(i["assignment_ref"] in i["source_refs"], "full assignment not among sources")
    if i["origin_ref"] is not None:
        require(i["origin_ref"] in i["source_refs"] and
                i["origin_ref"] in c.get("verified_origin_refs", []),
                "unverified or missing successor trigger")
    require(c.get("physical_bindings", {}).get(i["recipient"]),
            "recipient physical chat/role not verified")
    require(reconcile(c.get("actions", {}).get(run + "/" + i["call_id"])) == "NOT_SENT",
            "call already sent, blocked or uncertain")
    return {"call_id": i["call_id"], "recipient": i["recipient"],
            "status": "PREFLIGHT_ONLY_NOT_SENT"}


def professional_receipt(c, role, p):
    i = validated("invocation", c.get(role + "_invocation"))
    rec = c.get(role + "_receipt", {})
    require(i["run_id"] == p["run_id"] and i["call_id"] == p["call_id"]
            and i["recipient"] == p["sender"], role + " invocation mismatch")
    require(
        rec.get("call_id") == i["call_id"]
        and rec.get("recipient") == i["recipient"]
        and rec.get("token") == i["token"]
        and rec.get("invocation_ref") == c.get(role + "_invocation_ref")
        and rec.get("return_ref") == c.get(role + "_return_ref"),
        "no matching independently verified " + role + " receipt",
    )
    exact_path(c[role + "_invocation_ref"], p["run_id"],
               "calls/" + p["call_id"] + "/INVOCATION.json")
    exact_path(c[role + "_return_ref"], p["run_id"],
               "calls/" + p["call_id"] + "/PRO_RETURN.json")


def pro_state(p):
    has_followup = bool(p["issued_order_refs"] or p["issued_delegation_refs"]
                        or p["continuation_ref"] or p["owner_request_ref"])
    if p["professional_state"] == "REPORTED_COMPLETE":
        require(p["remaining_scope_ref"] is None and not has_followup,
                "complete report still has outgoing actions / remaining scope")
    else:
        require(p["remaining_scope_ref"] is not None and has_followup,
                "unfinished professional work has no recorded successor")
    require((p["professional_state"] == "WAITING_OWNER") == bool(p["owner_request_ref"]),
            "waiting Owner and owner_request_ref inconsistent")


def manager_return(c, b):
    p = validated("professional_return", c.get("manager_return"))
    require(p["run_id"] == b["run_id"] and p["role"] == "manager" and
            p["sender"] == b["manager"] and p["delegation_ref"] is None
            and p["return_to"] is None and not p["issued_order_refs"]
            and not p["accepted_worker_refs"], "invalid manager return")
    professional_receipt(c, "manager", p)
    pro_state(p)
    return p


def delegation(c, b):
    d = validated("delegation", c.get("delegation"))
    require(d["run_id"] == b["run_id"] and d["issuer"] == b["manager"]
            and d["recipient"] in b["executors"] and d["return_to"] == b["manager"],
            "invalid manager-to-executor delegation")
    exact_path(c["delegation_ref"], d["run_id"],
               "delegations/" + d["delegation_id"] + "/DELEGATION.json")
    p = manager_return(c, b)
    require(d["issuer_call_id"] == p["call_id"] and
            c["delegation_ref"] in p["issued_delegation_refs"], "manager did not issue this D")
    require(c["delegation_ref"] == c.get("delegation_index", {}).get(d["delegation_id"]),
            "D missing or conflicting in trusted index")
    for x in [d["task_ref"], *d["input_refs"]]:
        ref_parts(x)
    if d["business_context_ref"]:
        ref_parts(d["business_context_ref"])
    return d


def executor_return(c, b, d):
    p = validated("professional_return", c.get("executor_return"))
    require(p["run_id"] == b["run_id"] and p["role"] == "executor" and
            p["sender"] == d["recipient"] and p["delegation_ref"] == c["delegation_ref"]
            and p["return_to"] == d["issuer"] and not p["issued_delegation_refs"],
            "invalid executor return / wrong parent D")
    professional_receipt(c, "executor", p)
    pro_state(p)
    verified = set(c.get("verified_worker_return_refs", []))
    require(set(p["accepted_worker_refs"]).issubset(verified),
            "executor accepted an unverified Worker return")
    return p


def order(c, b, d):
    o = validated("order", c.get("order"))
    require(o["run_id"] == b["run_id"] and o["delegation_ref"] == c["delegation_ref"]
            and o["issuer"] == d["recipient"] and o["return_to"] == d["recipient"]
            and o["worker"] in b["workers"], "invalid executor-to-worker order")
    exact_path(c["order_ref"], o["run_id"],
               "work_orders/" + o["work_order_id"] + "/ORDER.json")
    require(o["grant"]["operation"] in d["permitted_operations"]
            and set(o["grant"]["allowed_writes"]).issubset(d["allowed_writes"]),
            "W exceeds delegated scope")
    require(any(grant_covers(g, o["grant"]) for g in b["grants"]), "W outside original Owner grant")
    p = executor_return(c, b, d)
    require(o["issuer_call_id"] == p["call_id"]
            and c["order_ref"] in p["issued_order_refs"], "executor did not issue W")
    require(c.get("order_index", {}).get(o["work_order_id"]) == c["order_ref"],
            "W not uniquely registered")
    return o


def worker_return(c, b, o):
    w = validated("worker_return", c.get("worker_return"))
    require(w["run_id"] == b["run_id"] and w["work_order_id"] == o["work_order_id"]
            and w["order_ref"] == c["order_ref"] and w["worker"] == o["worker"]
            and w["return_to"] == o["issuer"], "wrong Worker result binding")
    exact_path(c["worker_return_ref"], w["run_id"],
               "worker_results/" + w["work_order_id"] + "/WORKER_RETURN.json")
    rec = c.get("worker_receipt", {})
    require(rec.get("worker") == w["worker"] and rec.get("order_ref") == c["order_ref"]
            and rec.get("return_ref") == c["worker_return_ref"],
            "no independent Worker receipt")
    verified = c.get("verified_evidence_sha256", {})
    for item in w["manifest"].values():
        ref_parts(item["ref"])
        require(verified.get(item["ref"]) == item["sha256"],
                "evidence digest not independently checked")
    missing = set(o["deliverables"]) - set(w["manifest"])
    require(not missing or (w["outcome"] != "EXECUTED" and w["missing"]),
            "missing deliverables concealed")
    return w


def reconcile(history):
    require(isinstance(history, list) and history and history[0] == "NOT_SENT",
            "no original authoritative action registration")
    state = history[0]
    for nxt in history[1:]:
        require(nxt in STATES and (nxt == state or (state, nxt) in TRANSITIONS),
                "illegal action state transition")
        state = nxt
    return state


def check(action, c):
    if action == "reconcile-actions":
        b = binding(c)
        states = c.get("actions")
        require(isinstance(states, dict) and states, "no trusted action ledger")
        prefix = b["run_id"] + "/"
        require(all(re.fullmatch(re.escape(prefix) + r"(C[0-9]{4,}|D[0-9]{3,}|W[0-9]{3,})", k)
                for k in states), "cross-run or invalid action ledger")
        return {k: reconcile(v) for k, v in states.items()}
    b = binding(c)
    if action == "validate-binding":
        return {"run_id": b["run_id"], "status": "STRUCTURE_VALID_ONLY"}
    if action == "validate-invocation":
        return invocation_preflight(c, b)
    if action == "validate-manager-return":
        p = manager_return(c, b)
        return {"return_to": "PROFESSIONAL_OWNER_DECISION", "call_id": p["call_id"],
                "state": p["professional_state"]}
    d = delegation(c, b)
    if action == "validate-delegation":
        return {"delegation_id": d["delegation_id"], "recipient": d["recipient"]}
    if action == "validate-executor-return":
        p = executor_return(c, b, d)
        return {"call_id": p["call_id"], "return_to": d["issuer"],
                "state": p["professional_state"]}
    if action == "route-return" and c.get("result_kind") == "executor":
        p = executor_return(c, b, d)
        return {"recipient": p["return_to"], "reason": "EXECUTOR_RETURN",
                "source_ref": c["executor_return_ref"]}
    o = order(c, b, d)
    if action == "validate-order":
        require(c.get("physical_bindings", {}).get(o["worker"]),
                "worker physical thread not verified")
        require(c.get("workspace_available") is True,
                "workspace availability or exclusive ownership unverified")
        require(reconcile(c.get("actions", {}).get(b["run_id"] + "/" + o["work_order_id"])) == "NOT_SENT",
                "order already sent, blocked or uncertain")
        return {"work_order_id": o["work_order_id"], "recipient": o["worker"],
                "status": "PREFLIGHT_ONLY_NOT_LOCK"}
    w = worker_return(c, b, o)
    state = reconcile(c.get("actions", {}).get(b["run_id"] + "/" + o["work_order_id"]))
    require(state in ("IN_FLIGHT", "UNKNOWN", "BLOCKED", "COMPLETED"),
            "unsent or superseded W cannot return")
    if state == "COMPLETED":
        require(c.get("completed_worker_refs", {}).get(o["work_order_id"]) == c["worker_return_ref"],
                "conflicting late Worker return")
    if action == "validate-worker-return":
        return {"action": "NOOP" if state == "COMPLETED" else "RETURN_TO_EXECUTOR",
                "recipient": w["return_to"], "outcome": w["outcome"]}
    if action == "route-return" and c.get("result_kind") == "worker":
        return {"recipient": w["return_to"], "reason": "WORKER_RETURN",
                "source_ref": c["worker_return_ref"]}
    raise ValueError("unsupported action/result kind")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=ACTIONS)
    parser.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    try:
        result = check(args.action, json.loads(args.snapshot.read_text("utf-8")))
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    except Exception as exc:
        print("BLOCKED: " + str(exc), file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
