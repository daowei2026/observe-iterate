#!/usr/bin/env python3
"""BI-01 new-run Git evidence gate. Read-only, no phone, no business decisions.

Exit 0 means mechanical prerequisites are present at an exact local Git commit.
It never authorizes a message or certifies actual send, management quality or G1-G6.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

RUN = "runs/BI-01-RESTART-01"
BINDING = "runtime/config/WORKMAP_BINDING.json"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
ROUND = re.compile(r"^R[0-9]{4}$")
ROLES = {"management", "professional", "review", "receiver"}
REQUIRED = (
    "schema", "run_id", "round_id", "work_id", "invocation_id",
    "assignment_token", "round_marker", "role", "recipient_ref",
    "policy_commit", "prompt_sha256",
)


class Git:
    def __init__(self, root: str, ref: str):
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
        b = view.obj(BINDING)
    except (ValueError, KeyError, UnicodeError, json.JSONDecodeError):
        return ["WORKMAP_BINDING_UNREADABLE"]
    if b.get("status") != "ADOPTED":
        return ["WORKMAP_NOT_ADOPTED"]
    if b.get("schema") != "workmap-binding/v2":
        return ["WORKMAP_BINDING_SCHEMA"]
    try:
        stream = b["streams"]["bi01"]
        paths = [
            (b["overview"]["path"], RUN + "/README.md"),
            (stream["map"]["path"], RUN + "/00_长程推进地图.md"),
            (stream["task"], RUN + "/01_当前任务.md"),
            (b["receipt_path"], RUN + "/reviews/WORKMAP_INTAKE_CURRENT.json"),
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
    root = RUN + "/provenance/turns/" + round_id
    record = view.obj(root + "/INVOCATION.json")
    prompt = view.raw(root + "/PROMPT.md")
    errors = require([
        (all(key in record for key in REQUIRED), "INVOCATION_FIELDS_MISSING"),
        (record.get("schema") == "bi01-invocation/v1", "INVOCATION_SCHEMA"),
        (record.get("run_id") == "BI-01-RESTART-01", "RUN_ID_MISMATCH"),
        (record.get("round_id") == round_id, "ROUND_ID_MISMATCH"),
        (record.get("role") in ROLES, "ROLE_INVALID"),
        (HEX40.fullmatch(str(record.get("policy_commit", ""))) is not None, "POLICY_COMMIT_REQUIRED"),
        (HEX64.fullmatch(str(record.get("prompt_sha256", ""))) is not None, "PROMPT_DIGEST_INVALID"),
        (hashlib.sha256(prompt).hexdigest() == record.get("prompt_sha256"), "PROMPT_BYTES_CHANGED"),
    ])
    for name in ("work_id", "invocation_id", "assignment_token", "round_marker", "recipient_ref"):
        if not isinstance(record.get(name), str) or not record[name].strip():
            errors.append("MISSING_IDENTITY:" + name)
    # Existing coordinator-dispatch/v3 emits [invocation_id] as its first line.
    # That EXACT line is also the common phone scheduler's bracketed round marker.
    prefix = "BI01-RESTART-01-" + round_id + "-"
    invocation_id = record.get("invocation_id")
    marker = record.get("round_marker")
    if (not isinstance(invocation_id, str)
            or not invocation_id.startswith(prefix)
            or len(invocation_id) < len(prefix) + 3
            or not re.fullmatch(r"[^\[\]\s]{3,180}", invocation_id)
            or marker != "[" + invocation_id + "]"):
        errors.append("ROUND_MARKER_OR_INVOCATION_MISMATCH")
    if prompt.split(b"\n", 1)[0] != str(marker).encode("utf-8"):
        errors.append("PROMPT_FIRST_LINE_NOT_SCHEDULER_MARKER")
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
    if not isinstance(path, str) or (run_scoped and not path.startswith(RUN + "/")):
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
    p = RUN + "/provenance/turns/" + round_id + "/SEND_RECEIPT.json"
    if not view.exists(p):
        # Absence is not proof of no attempted phone action: live scheduler check required.
        return "NOT_RECORDED", []
    obj = view.obj(p)
    state = obj.get("state")
    if state not in {"NOT_SENT", "CONFIRMED_SEND_FAILED", "COMMITTED", "UNKNOWN", "BLOCKED"}:
        return str(state), ["SEND_STATE_INVALID"]
    return state, []


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
        errors.extend(locator(view, rec.get("current_task_ref"), "current_task_ref"))
        errors.extend(locator(view, rec.get("task_adoption_ref"), "task_adoption_ref"))
    else:
        errors.extend(active_binding(view))
        for name in ("binding_ref", "current_task_ref", "task_adoption_ref"):
            errors.extend(locator(view, rec.get(name), name))
        if isinstance(rec.get("current_task_ref"), dict) and rec["current_task_ref"].get("selector") not in ("full", "全文"):
            errors.append("CURRENT_TASK_FULL_TEXT_REQUIRED")
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
    p = RUN + "/provenance/turns/" + round_id
    if not view.exists(p + "/FULL_RESPONSE.md"):
        errors.append("FULL_RESPONSE_MISSING")
    else:
        body = view.text(p + "/FULL_RESPONSE.md")
        if not body.strip():
            errors.append("FULL_RESPONSE_EMPTY")
    try:
        role = view.obj(p + "/ROLE_RETURN.json")
        for field in ("work_id", "invocation_id", "assignment_token"):
            if role.get(field) != rec.get(field):
                errors.append("ROLE_RETURN_MISMATCH:" + field)
        if not str(role.get("schema", "")).startswith("longrun-return/"):
            errors.append("ROLE_RETURN_SCHEMA")
    except (ValueError, json.JSONDecodeError):
        errors.append("ROLE_RETURN_MISSING")
    if rec.get("question_work_required", False) and not view.exists(p + "/QUESTION_WORK_RETURN.json"):
        errors.append("QUESTION_WORK_RETURN_MISSING")
    return {
        "check": "after-return", "round_id": round_id, "ok": not errors,
        "errors": sorted(set(errors)),
        "limits": "Reply/Return integrity only. Management reception, independent audit and G1-G6 remain separate.",
        "business_gate": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["status", "pre-dispatch", "after-return"])
    parser.add_argument("--repo", required=True)
    parser.add_argument("--ref", required=True)
    parser.add_argument("--round", help="R0001, R0002, ...")
    args = parser.parse_args()
    try:
        view = Git(args.repo, args.ref)
        if args.command == "status":
            ready_root = view.exists(RUN + "/README.md")
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
