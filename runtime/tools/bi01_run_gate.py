#!/usr/bin/env python3
"""BI-01 new-run Git evidence gate. Read-only, no phone, no business decisions.

Exit 0 means mechanical prerequisites are present at an exact local Git commit.
It never authorizes a message or certifies actual send, management quality or professional business acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

# Legacy library/fixture compatibility only; the CLI requires an explicit run ID.
DEFAULT_RUN_ID = "BI-01-V2-02"
RUN = "runs/" + DEFAULT_RUN_ID
BINDING = "runtime/config/WORKMAP_BINDING.json"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
ROUND = re.compile(r"^R[0-9]{4}$")
ROLES = {"management", "professional", "review", "receiver"}
READER_TASK = RUN + "/reviews/management-R0001/READER_TASK.md"
REQUIRED = (
    "schema", "run_id", "round_id", "work_id", "invocation_id",
    "assignment_token", "round_marker", "role", "recipient_ref",
    "policy_commit", "prompt_sha256",
)


class Git:
    def __init__(self, root: str, ref: str, run_id: str = DEFAULT_RUN_ID,
                 binding_path: str = BINDING):
        if not isinstance(run_id, str) or not re.fullmatch(r"BI-01-[A-Z0-9]+(?:-[A-Z0-9]+)*", run_id):
            raise ValueError("INVALID_RUN_ID")
        self.run_id = run_id
        self.run_root = "runs/" + run_id
        self.binding_path = self.path(binding_path)
        self.invocation_prefix = run_id.replace("BI-01-", "BI01-", 1)
        self.reader_task = self.run_root + "/reviews/management-R0001/READER_TASK.md"
        if not HEX40.fullmatch(ref):
            raise ValueError("EXACT_COMMIT_REQUIRED")
        self.root = Path(root).resolve()
        self.ref = ref
        if self.run("cat-file", "-t", ref).strip() != b"commit":
            raise ValueError("COMMIT_REQUIRED")

    def run(self, *args: str) -> bytes:
        try:
            return subprocess.check_output(
                ["git", "-C", str(self.root), *args],
                stderr=subprocess.PIPE, timeout=20,
            )
        except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as ex:
            raise ValueError("GIT_READ_FAILED:" + " ".join(args[:2])) from ex

    def path(self, path: str) -> str:
        if (not isinstance(path, str) or not path or "\x00" in path
                or "\\" in path or path.startswith("-")):
            raise ValueError("INVALID_PATH")
        p = PurePosixPath(path)
        if p.is_absolute() or ".." in p.parts:
            raise ValueError("UNSAFE_PATH")
        return p.as_posix()

    def raw(self, path: str) -> bytes:
        p = self.path(path)
        oid = self.run("rev-parse", "--verify", self.ref + ":" + p).decode().strip()
        if self.run("cat-file", "-t", oid).strip() != b"blob":
            raise ValueError("NOT_FILE:" + p)
        if int(self.run("cat-file", "-s", oid)) > 5_000_000:
            raise ValueError("SOURCE_TOO_LARGE:" + p)
        return self.run("cat-file", "blob", oid)

    def text(self, path: str) -> str:
        return self.raw(path).decode("utf-8")

    def obj(self, path: str) -> dict:
        body = json.loads(self.text(path))
        if not isinstance(body, dict):
            raise ValueError("OBJECT_REQUIRED:" + path)
        return body

    def exists(self, path: str) -> bool:
        try:
            self.raw(path)
            return True
        except (ValueError, UnicodeError):
            return False


def require(conditions: list[tuple[bool, str]]) -> list[str]:
    return [message for valid, message in conditions if not valid]


def active_binding(view: Git) -> list[str]:
    """Only verify adopted structural references; real intake requires workmap_gate."""
    try:
        b = view.obj(view.binding_path)
    except (ValueError, KeyError, UnicodeError, json.JSONDecodeError):
        return ["WORKMAP_BINDING_UNREADABLE"]
    if b.get("status") != "ADOPTED":
        return ["WORKMAP_NOT_ADOPTED"]
    if b.get("schema") != "workmap-binding/v2":
        return ["WORKMAP_BINDING_SCHEMA"]
    try:
        stream = b["streams"]["bi01"]
        paths = [
            (b["overview"]["path"], view.run_root + "/README.md"),
            (stream["map"]["path"], view.run_root + "/00_长程推进地图.md"),
            (stream["task"], view.run_root + "/01_当前任务.md"),
            (b["receipt_path"], view.run_root + "/reviews/WORKMAP_INTAKE_CURRENT.json"),
        ]
        problems = [
            "WORKMAP_PATH_MISMATCH:" + expected
            for actual, expected in paths if actual != expected
        ]
        for path, _ in paths:
            if not view.exists(path):
                problems.append("WORKMAP_SOURCE_MISSING:" + path)
        if not problems:
            receipt = view.obj(b["receipt_path"])
            if receipt.get("schema") != "workmap-intake/v1" \
                    or "bi01" not in receipt.get("intakes", {}):
                problems.append("MANAGEMENT_INTAKE_MISSING")
        return problems
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return ["WORKMAP_INCOMPLETE"]


def invocation(view: Git, round_id: str) -> tuple[dict, list[str]]:
    if not ROUND.fullmatch(round_id):
        raise ValueError("ROUND_ID_REQUIRED_RNNNN")
    root = view.run_root + "/provenance/turns/" + round_id
    record = view.obj(root + "/INVOCATION.json")
    prompt = view.raw(root + "/PROMPT.md")
    errors = require([
        (all(key in record for key in REQUIRED), "INVOCATION_FIELDS_MISSING"),
        (record.get("schema") == "bi01-invocation/v1", "INVOCATION_SCHEMA"),
        (record.get("run_id") == view.run_id, "RUN_ID_MISMATCH"),
        (record.get("round_id") == round_id, "ROUND_ID_MISMATCH"),
        (record.get("role") in ROLES, "ROLE_INVALID"),
        (HEX40.fullmatch(str(record.get("policy_commit", ""))) is not None, "POLICY_COMMIT_REQUIRED"),
        (HEX64.fullmatch(str(record.get("prompt_sha256", ""))) is not None, "PROMPT_DIGEST_INVALID"),
        (hashlib.sha256(prompt).hexdigest() == record.get("prompt_sha256"), "PROMPT_BYTES_CHANGED"),
        (record.get("question_work_required") is True, "QUESTION_WORK_V2_REQUIRED"),
    ])
    for name in ("work_id", "invocation_id", "assignment_token", "round_marker", "recipient_ref"):
        if not isinstance(record.get(name), str) or not record[name].strip():
            errors.append("MISSING_IDENTITY:" + name)
    # Existing coordinator-dispatch/v3 emits [invocation_id] as its first line.
    # That EXACT line is also the common phone scheduler's bracketed round marker.
    prefix = view.invocation_prefix + "-" + round_id + "-"
    invocation_id = record.get("invocation_id")
    marker = record.get("round_marker")
    if (not isinstance(invocation_id, str)
            or not invocation_id.startswith(prefix)
            or len(invocation_id) < len(prefix) + 3
            or not re.fullmatch(r"[^\[\]\s]{3,180}", invocation_id)
            or marker != "[" + invocation_id + "]"):
        errors.append("ROUND_MARKER_OR_INVOCATION_MISMATCH")
    if prompt.split(b"\n", 1)[0] != str(marker).encode("utf-8"):
        errors.append("PROMPT_FIRST_LINE_NOT_SCHEDULER_MARKER",)
    if record.get("work_id") != "BI-01":
        errors.append("COORDINATOR_FIXED_WORK_ID_REQUIRED")
    if record.get("policy_commit") != view.ref:
        # Policy may be an earlier exact commit, but it must be available locally.
        try:
            if view.run("cat-file", "-t", str(record.get("policy_commit"))).strip() != b"commit":
                errors.append("POLICY_COMMIT_UNAVAILABLE")
        except ValueError:
            errors.append("POLICY_COMMIT_UNAVAILABLE")
    return record, errors


def locator(view: Git, value: object, label: str, run_scoped: bool = True) -> list[str]:
    """Use coordinator-dispatch/v3 Git locators, never guess a plain path."""
    if not isinstance(value, dict):
        return ["INVALID_GIT_LOCATOR:" + label]
    if value.get("repo") != "daowei2026/observe-iterate":
        return ["OTHER_REPOSITORY_NOT_CURRENT:" + label]
    ref, path, selector = value.get("commit"), value.get("path"), value.get("selector")
    if not isinstance(ref, str) or not HEX40.fullmatch(ref):
        return ["LOCATOR_COMMIT_REQUIRED:" + label]
    if not isinstance(path, str) or (run_scoped and not path.startswith(view.run_root + "/")):
        return ["LOCATOR_PATH_OUTSIDE_NEW_RUN:" + label]
    if not isinstance(selector, str) or not selector:
        return ["LOCATOR_SELECTOR_REQUIRED:" + label]
    try:
        p = view.path(path)
        oid = view.run("rev-parse", "--verify", ref + ":" + p).decode().strip()
        if view.run("cat-file", "-t", oid).strip() != b"blob":
            return ["LOCATOR_NOT_BLOB:" + label]
    except ValueError:
        return ["LOCATOR_SOURCE_UNAVAILABLE:" + label]
    return []


def send_state(view: Git, round_id: str) -> tuple[str, list[str]]:
    p = view.run_root + "/provenance/turns/" + round_id + "/SEND_RECEIPT.json"
    if not view.exists(p):
        # Absence is not proof of no attempted phone action: live scheduler check required.
        return "NOT_RECORDED", []
    obj = view.obj(p)
    state = obj.get("state")
    if state not in {"NOT_SENT", "CONFIRMED_SEND_FAILED", "COMMITTED", "UNKNOWN", "BLOCKED"}:
        return str(state), ["SEND_STATE_INVALID"]
    return state, []


def first_reader(view: Git, round_id: str, rec: dict) -> list[str]:
    """Check the manager-issued producer of initial intake evidence.

    This uses the existing dispatcher and Workmap snapshot, never an adopted
    professional dispatch or a caller-supplied exemption flag. Authority still
    requires the external Owner/role checks listed in the result.
    """
    try:
        tools = Path(__file__).resolve().parents[1] / "overlay" / "tools"
        modules = []
        for name in ("management_prompt", "workmap_gate"):
            spec = importlib.util.spec_from_file_location(name, tools / (name + ".py"))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules.append(module)
        coordinator, workmap = modules
        repository = "daowei2026/observe-iterate"
        task_ref, bound_ref, adoption = (rec[k] for k in
                                         ("current_task_ref", "binding_ref", "task_adoption_ref"))
        if (task_ref["path"] != view.reader_task or bound_ref["path"] != view.reader_task
                or bound_ref["commit"] != task_ref["commit"]):
            raise ValueError("READER_TASK_BINDING_SOURCE_MISMATCH")
        task, _ = coordinator.source(view.root, task_ref, repository)
        if task.encode("utf-8") != view.raw(view.reader_task):
            raise ValueError("READER_TASK_NOT_CURRENT")
        if not re.search(r"^task_id: " + re.escape(view.invocation_prefix) + r"-WORKMAP-READER-01$", task, re.M):
            raise ValueError("READER_TASK_ID_MISMATCH")
        binding = coordinator.binding_target(view.root, bound_ref, repository)["binding"]
        section = coordinator.selected(task, "#question-work-binding")
        blocks = re.findall(r"^```json\s*\n(.*?)^```\s*$", section, re.M | re.S)
        if len(blocks) != 1 or binding != coordinator.loads(blocks[0]):
            raise ValueError("READER_BINDING_NOT_CURRENT")

        event = view.obj(view.run_root + "/provenance/turns/" + round_id + "/DISPATCH.json")
        for key in ("work_id", "invocation_id", "assignment_token", "binding_ref"):
            if event.get(key) != rec.get(key):
                raise ValueError("DISPATCH_IDENTITY_MISMATCH:" + key)
        if event.get("dispatch_kind") == "NORMAL":
            for key in ("current_task_ref", "task_adoption_ref"):
                if event.get(key) != rec.get(key):
                    raise ValueError("DISPATCH_SOURCE_MISMATCH:" + key)
        prepared = coordinator.prepare_dispatch(
            view.root, rec["policy_commit"], "runtime/config/COORDINATOR_DISPATCH.json", event)
        coordinator.verify(prepared, view.raw(view.run_root + "/provenance/turns/" + round_id + "/PROMPT.md"))
        coordinator.verify_recipient(prepared, rec["recipient_ref"])
        if prepared["role"] != "review" or prepared["mode"] != "INDEPENDENT_REVIEW":
            raise ValueError("FIRST_READER_READ_ONLY_ROLE_REQUIRED")

        plan = binding["plan_ref"]
        manager_path = re.fullmatch(re.escape(view.run_root) + r"/reviews/management-(R[0-9]{4})/DECISION.md",
                                    adoption["path"])
        if (not manager_path or adoption["selector"] != "#adoption"
                or plan["path"] != adoption["path"] or plan["commit"] != adoption["commit"]
                or plan["selector"] != "#reader-pre-adoption"):
            raise ValueError("FIRST_READER_MANAGEMENT_ADOPTION_REQUIRED")
        coordinator.source(view.root, adoption, repository)
        authority = Git(str(view.root), adoption["commit"], view.run_id, view.binding_path)
        decision = authority.text(adoption["path"])
        if decision.encode("utf-8") != view.raw(adoption["path"]):
            raise ValueError("FIRST_READER_MANAGEMENT_DECISION_NOT_CURRENT")
        manager_round = manager_path[1]
        manager, problems = invocation(authority, manager_round)
        if problems or manager["role"] != "management":
            raise ValueError("FIRST_READER_MANAGEMENT_INVOCATION_REQUIRED")
        for key, expected in (("work_id", "BI-01"), ("run_id", view.run_id),
                              ("role", "management"), ("invocation_id", manager["invocation_id"]),
                              ("assignment_token", manager["assignment_token"])):
            if not re.search(r"^" + key + ": " + re.escape(expected) + r"$", decision, re.M):
                raise ValueError("FIRST_READER_MANAGEMENT_IDENTITY:" + key)
        returned = view.obj(view.run_root + "/provenance/turns/" + manager_round + "/ROLE_RETURN.json")
        artifact = {k: adoption[k] for k in ("repo", "commit", "path")}
        if (send_state(view, manager_round)[0] != "COMMITTED"
                or returned.get("schema") != "longrun-return/v1"
                or returned.get("work_id") != "BI-01"
                or returned.get("invocation_id") != manager["invocation_id"]
                or returned.get("assignment_token") != manager["assignment_token"]
                or not returned.get("role_outputs", {}).get("management")
                or artifact not in returned.get("artifact_refs", [])):
            raise ValueError("FIRST_READER_ISSUED_MANAGEMENT_DECISION_REQUIRED")

        sources = [entry["source"] for entry in binding["source_reads"]]
        input_paths = [view.run_root + "/README.md", view.run_root + "/00_长程推进地图.md",
                       view.run_root + "/01_当前任务.md", view.binding_path]
        inputs = []
        for path in input_paths + [view.run_root + "/OWNER_START.md"]:
            refs = [s for s in sources if s.get("path") == path]
            if len(refs) != 1 or refs[0].get("selector") not in ("full", "全文"):
                raise ValueError("FIRST_READER_FULL_INPUT_REQUIRED:" + path)
            source_body, _ = coordinator.source(view.root, refs[0], repository)
            if path.endswith("/OWNER_START.md"):
                if source_body.encode("utf-8") != view.raw(path):
                    raise ValueError("FIRST_READER_OWNER_SOURCE_CHANGED")
            else:
                inputs.append(refs[0]["commit"])
        if len(set(inputs)) != 1:
            raise ValueError("FIRST_READER_INPUT_COMMIT_MISMATCH")
        frozen = workmap.snapshot(view.root, inputs[0], view.binding_path, "bi01")
        current = workmap.snapshot(view.root, view.ref, view.binding_path, "bi01")
        if ("reader_fingerprint" not in frozen
                or frozen["reader_fingerprint"] != current.get("reader_fingerprint")):
            raise ValueError("FIRST_READER_INPUT_CHANGED")
        return []
    except (ValueError, KeyError, TypeError, UnicodeError) as ex:
        return ["FIRST_READER_PRE_ADOPTION_INVALID:" + str(ex)]


def first_reader_reception(view: Git, round_id: str, rec: dict) -> list[str]:
    """Receive actual first-reader evidence before an intake can be adopted.

    This is the manager route already signed in that Reader's Binding, not a
    general unadopted-management exemption. Recheck the original issued Reader,
    its committed dispatch, complete saved return, exact source and frozen input.
    """
    try:
        tools = Path(__file__).resolve().parents[1] / "overlay" / "tools"
        spec = importlib.util.spec_from_file_location("management_prompt", tools / "management_prompt.py")
        coordinator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(coordinator)
        repository = "daowei2026/observe-iterate"
        root = view.run_root + "/provenance/turns/"
        event = view.obj(root + round_id + "/DISPATCH.json")
        for key in ("work_id", "invocation_id", "assignment_token", "binding_ref",
                    "current_task_ref", "task_adoption_ref"):
            if event.get(key) != rec.get(key):
                raise ValueError("DISPATCH_SOURCE_MISMATCH:" + key)
        if event.get("dispatch_kind") != "NORMAL" or event.get("route") not in {"accept", "decide"}:
            raise ValueError("SIGNED_READER_RECEPTION_ROUTE_REQUIRED")
        prepared = coordinator.prepare_dispatch(
            view.root, rec["policy_commit"], "runtime/config/COORDINATOR_DISPATCH.json", event)
        coordinator.verify(prepared, view.raw(root + round_id + "/PROMPT.md"))
        coordinator.verify_recipient(prepared, rec["recipient_ref"])
        if prepared["role"] != "management" or prepared["mode"] != "INDEPENDENT_REVIEW":
            raise ValueError("READER_MANAGEMENT_RECIPIENT_REQUIRED")
        body, response_meta = coordinator.source(view.root, event["latest_response_ref"], repository)
        return_body, return_meta = coordinator.source(view.root, event["latest_return_ref"], repository)
        if event["latest_response_ref"]["selector"] not in {"full", "全文"} or response_meta["blob"] != return_meta["blob"]:
            raise ValueError("READER_FULL_RETURN_SOURCE_REQUIRED")
        returned = coordinator.find_return(return_body)
        match = re.fullmatch(re.escape(view.invocation_prefix) + r"-(R[0-9]{4})-\S+", returned["invocation_id"])
        if not match or match[1] == round_id:
            raise ValueError("ORIGINAL_READER_ROUND_REQUIRED")
        reader_round = match[1]
        reader, problems = invocation(view, reader_round)
        if problems or reader.get("role") != "review":
            raise ValueError("ORIGINAL_READER_INVOCATION_INVALID")
        if (reader["current_task_ref"] != rec["current_task_ref"]
                or reader["task_adoption_ref"] != rec["task_adoption_ref"]
                or coordinator.binding_target(view.root, reader["binding_ref"], repository)
                != coordinator.binding_target(view.root, rec["binding_ref"], repository)):
            raise ValueError("ORIGINAL_READER_AUTHORITY_MISMATCH")
        problems = first_reader(view, reader_round, reader)
        if problems or not after_return(view, reader_round)["ok"]:
            raise ValueError("ORIGINAL_READER_OR_RETURN_INVALID:" + ",".join(problems))
        if body.encode("utf-8") != view.raw(root + reader_round + "/FULL_RESPONSE.md"):
            raise ValueError("ORIGINAL_READER_FULL_RESPONSE_MISMATCH")
        if returned != view.obj(root + reader_round + "/QUESTION_WORK_RETURN.json"):
            raise ValueError("ORIGINAL_READER_QUESTION_RETURN_MISMATCH")
        role = view.obj(root + reader_round + "/ROLE_RETURN.json")
        roles = [coordinator.loads(raw) for raw in re.findall(r"^```json\s*\n(.*?)^```\s*$", body, re.M | re.S)
                 if '"longrun-return/' in raw]
        if (roles != [role] or role.get("handoff", {}).get("route_key") != event["route"]
                or not role.get("role_outputs", {}).get("review")):
            raise ValueError("ORIGINAL_READER_BOUND_HANDOFF_REQUIRED")
        return []
    except (ValueError, KeyError, TypeError, UnicodeError) as ex:
        return ["FIRST_READER_RECEPTION_INVALID:" + str(ex)]


def pre_dispatch(view: Git, round_id: str) -> dict:
    rec, errors = invocation(view, round_id)
    state, state_errors = send_state(view, round_id)
    errors.extend(state_errors)
    if state not in {"NOT_RECORDED", "NOT_SENT", "CONFIRMED_SEND_FAILED"}:
        errors.append("SEND_NOT_SAFE:" + state)
    if rec.get("role") == "management" and rec.get("bootstrap_ref"):
        # The v3 dispatcher requires real current_task_ref and task_adoption_ref
        # even for BOOTSTRAP. Both may cite the next Owner's actual START record;
        # neither is a fictitious management map/task.
        errors.extend(locator(view, rec.get("bootstrap_ref"), "bootstrap_ref"))
        if rec.get("binding_ref") != rec.get("bootstrap_ref"):
            errors.append("BOOTSTRAP_BINDING_REF_MISMATCH")
        try:
            ref = rec["bootstrap_ref"]
            bootstrap = Git(str(view.root), ref["commit"], view.run_id, view.binding_path).obj(ref["path"])
            if (ref.get("selector") not in ("full", "全文")
                    or bootstrap.get("schema") != "question-work/v2"
                    or bootstrap.get("kind") != "BOOTSTRAP"
                    or bootstrap.get("work_id") != rec.get("work_id")
                    or bootstrap.get("recipient_ref") != rec.get("recipient_ref")):
                errors.append("BOOTSTRAP_IDENTITY_MISMATCH")
        except (ValueError, KeyError, TypeError):
            errors.append("BOOTSTRAP_UNREADABLE")
        errors.extend(locator(view, rec.get("current_task_ref"), "current_task_ref"))
        errors.extend(locator(view, rec.get("task_adoption_ref"), "task_adoption_ref"))
    else:
        for name in ("binding_ref", "current_task_ref", "task_adoption_ref"):
            errors.extend(locator(view, rec.get(name), name))
        if isinstance(rec.get("current_task_ref"), dict) and rec["current_task_ref"].get("selector") not in ("full", "全文"):
            errors.append("CURRENT_TASK_FULL_TEXT_REQUIRED")
        try:
            unconfigured = view.obj(view.binding_path).get("status") == "NOT_CONFIGURED"
        except (ValueError, TypeError):
            unconfigured = False
        if (rec.get("role") == "review" and not rec.get("bootstrap_ref")
                and isinstance(rec.get("current_task_ref"), dict)
                and rec["current_task_ref"].get("path") == view.reader_task
                and unconfigured):
            errors.extend(first_reader(view, round_id, rec))
        elif (rec.get("role") == "management" and not rec.get("bootstrap_ref")
                and isinstance(rec.get("current_task_ref"), dict)
                and rec["current_task_ref"].get("path") == view.reader_task
                and unconfigured):
            errors.extend(first_reader_reception(view, round_id, rec))
        else:
            errors.extend(active_binding(view))
    return {
        "check": "pre-dispatch", "round_id": round_id, "ok": not errors,
        "errors": sorted(set(errors)), "recorded_send_state": state,
        "next_external_checks": [
            "OWNER_START_AND_ROLE_AUTHORIZATION",
            "ACTUAL_MCP_PHONE_CONTROL_AND_UNIQUE_RECIPIENT",
            "LOCAL_SCHEDULER_SEND_DEDUP",
            "OVERLAY12_EXACT_PAYLOAD_AND_RECIPIENT_VERIFY",
        ],
        "sent": False, "business_gate": False,
    }


def after_return(view: Git, round_id: str) -> dict:
    rec, errors = invocation(view, round_id)
    state, state_errors = send_state(view, round_id)
    errors.extend(state_errors)
    if state != "COMMITTED":
        errors.append("NO_CONFIRMED_SEND_FOR_RETURN")
    p = view.run_root + "/provenance/turns/" + round_id
    if not view.exists(p + "/FULL_RESPONSE.md"):
        errors.append("FULL_RESPONSE_MISSING")
    else:
        body = view.text(p + "/FULL_RESPONSE.md")
        if not body.strip():
            errors.append("FULL_RESPONSE_EMPTY")
    role = {}
    try:
        role = view.obj(p + "/ROLE_RETURN.json")
        for field in ("work_id", "invocation_id", "assignment_token"):
            if role.get(field) != rec.get(field):
                errors.append("ROLE_RETURN_MISMATCH:" + field)
        if not str(role.get("schema", "")).startswith("longrun-return/"):
            errors.append("ROLE_RETURN_SCHEMA")
    except (ValueError, json.JSONDecodeError):
        errors.append("ROLE_RETURN_MISSING")
    try:
        qret = view.obj(p + "/QUESTION_WORK_RETURN.json")
        if qret.get("schema") != "question-work/v2" or qret.get("kind") != "RETURN":
            errors.append("QUESTION_WORK_RETURN_VERSION")
        for key in ("work_id", "invocation_id"):
            if qret.get(key) != rec.get(key):
                errors.append("QUESTION_WORK_RETURN_MISMATCH:" + key)
        tools = Path(__file__).resolve().parents[1] / "overlay" / "tools"
        modules = []
        for name in ("management_prompt", "question_work_check"):
            spec = importlib.util.spec_from_file_location(name, tools / (name + ".py"))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules.append(module)
        coordinator, question_work = modules
        if not question_work.binding_refs_equal(
                rec.get("binding_ref"), qret.get("binding_ref"),
                resolver=lambda loc: coordinator.binding_target(
                    view.root, loc, "daowei2026/observe-iterate")):
            errors.append("QUESTION_WORK_RETURN_BINDING_MISMATCH")
        if not isinstance(qret.get("focus_results"), list) or not qret["focus_results"]:
            errors.append("QUESTION_WORK_FOCUS_RESULTS_MISSING")
        if not isinstance(qret.get("trigger_observations"), list):
            errors.append("QUESTION_WORK_TRIGGER_RESULTS_MISSING")
        if not isinstance(qret.get("continuation_ref"), dict):
            errors.append("QUESTION_WORK_CONTINUATION_MISSING")
        if role.get("question_work_ref") in (None, ""):
            errors.append("ROLE_RETURN_QUESTION_WORK_REF_MISSING")
    except (ValueError, json.JSONDecodeError):
        errors.append("QUESTION_WORK_RETURN_MISSING")
    return {
        "check": "after-return", "round_id": round_id, "ok": not errors,
        "errors": sorted(set(errors)),
        "limits": "Reply/Return integrity only. Management reception and applicable independent review remain separate.",
        "business_gate": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["status", "pre-dispatch", "after-return"])
    parser.add_argument("--repo", required=True)
    parser.add_argument("--ref", required=True)
    parser.add_argument("--run-id", required=True,
                        help="Explicit run identity; paths and markers stay scoped to this run")
    parser.add_argument("--binding", default=BINDING,
                        help="Repository-relative Workmap Binding path for this run")
    parser.add_argument("--round", help="R0001, R0002, ...")
    args = parser.parse_args()
    try:
        view = Git(args.repo, args.ref, args.run_id, args.binding)
        if args.command == "status":
            ready_root = view.exists(view.run_root + "/README.md")
            problems = [] if ready_root else ["NEW_RUN_ROOT_MISSING"]
            # A future OWNER GO and real adopted work are never inferred from files.
            result = {
                "check": "status", "ok": not problems, "errors": problems,
                "workmap_problems": active_binding(view),
                "adoption_mechanically_present": not active_binding(view),
                "preparation_only": bool(active_binding(view)),
                "sent": False, "run_started": None, "business_gate": False,
            }
        else:
            if not args.round:
                raise ValueError("ROUND_ID_REQUIRED")
            result = (pre_dispatch(view, args.round) if args.command == "pre-dispatch"
                      else after_return(view, args.round))
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0 if result["ok"] else 2
    except (ValueError, TypeError, KeyError, UnicodeError, json.JSONDecodeError) as ex:
        print(json.dumps({"ok": False, "error": str(ex), "sent": False}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
