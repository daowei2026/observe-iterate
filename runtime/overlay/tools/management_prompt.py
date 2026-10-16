"""Coordinator dispatch v3. Immutable Git inputs; no model, scheduler or phone.
Policy, role mapping and exact adopted records remain separate inputs. This module
checks mechanical relations, not authority, actual reading or business truth.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Callable

POLICY_PATH = "runtime/overlay/08_自然语言运行提示_v0.3.md"
SHA = re.compile(r"[0-9a-f]{40}\Z")
ROLES = {"management", "professional", "review", "receiver", "maintenance", "owner"}
DISPATCH_KINDS = {"NORMAL", "DELIVERY_REPAIR"}
MODE_PURPOSES = {"professional_work", "read_only_reception"}


def fail(message: str) -> None:
    raise ValueError(message)


def obj(value: Any, required: set[str], optional: set[str] = frozenset()) -> dict:
    if not isinstance(value, dict) or not required <= value.keys() or value.keys() - required - optional:
        fail("INVALID_OR_UNKNOWN_FIELDS:" + ",".join(sorted(required)))
    return value


def text(value: Any) -> str:
    if not isinstance(value, str) or not value.strip() or "\x00" in value:
        fail("NONEMPTY_TEXT_REQUIRED")
    return value


def unique(pairs: list) -> dict:
    out = {}
    for k, v in pairs:
        if k in out: fail("DUPLICATE_KEY:" + k)
        out[k] = v
    return out


def loads(raw: str) -> Any:
    return json.loads(raw, object_pairs_hook=unique)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    try:
        return subprocess.check_output(["git", "-C", str(repo), *args], stderr=subprocess.PIPE, timeout=15)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise ValueError("GIT_SOURCE_UNAVAILABLE:" + " ".join(args[:2])) from exc


def read_git(repo: Path, ref: str, path: str) -> tuple[str, str]:
    if not isinstance(ref, str) or not SHA.fullmatch(ref): fail("EXACT_COMMIT_REQUIRED")
    p = PurePosixPath(text(path))
    if p.is_absolute() or ".." in p.parts or "\\" in path or path.startswith("-"):
        fail("UNSAFE_PATH")
    if git(repo, "cat-file", "-t", ref).strip() != b"commit": fail("COMMIT_REQUIRED")
    oid = git(repo, "rev-parse", "--verify", ref + ":" + path).decode().strip()
    if git(repo, "cat-file", "-t", oid).strip() != b"blob": fail("TEXT_FILE_REQUIRED")
    if not 0 < int(git(repo, "cat-file", "-s", oid)) <= 10_000_000: fail("SOURCE_SIZE")
    raw = git(repo, "cat-file", "blob", oid)
    return text(raw.decode("utf-8")), oid


def marked(body: str, name: str) -> str:
    begin, end = "<!-- " + name + "_BEGIN -->", "<!-- " + name + "_END -->"
    if body.count(begin) != 1 or body.count(end) != 1: fail("MARKER_MISSING_OR_DUPLICATE:" + name)
    a, b = body.index(begin) + len(begin), body.index(end)
    if b <= a: fail("MARKER_ORDER")
    return text(body[a:b].strip())


def selected(body: str, selector: str) -> str:
    if selector in {"full", "全文"}: return body
    if selector.startswith("marker:"): return marked(body, selector[7:])
    if re.fullmatch(r"L[1-9][0-9]*-L[1-9][0-9]*", selector):
        a, b = map(int, re.findall(r"[0-9]+", selector)); lines = body.splitlines(keepends=True)
        if not 1 <= a <= b <= len(lines): fail("LINE_RANGE")
        return text("".join(lines[a-1:b]))
    if selector.startswith("#"):
        anchor = selector[1:]
        pattern = r'<a\s+id=[\"\']' + re.escape(anchor) + r'[\"\']\s*></a>'
        hits = list(re.finditer(pattern, body))
        if len(hits) != 1: fail("ANCHOR_MISSING_OR_DUPLICATE:" + selector)
        start = hits[0].start()
        nxt = re.search(r'<a\s+id=', body[hits[0].end():])
        end = hits[0].end() + nxt.start() if nxt else len(body)
        return body[start:end]
    fail("UNSUPPORTED_SELECTOR:" + selector)


def source(repo: Path, loc: dict, repository: str, default_ref: str | None = None) -> tuple[str, dict]:
    obj(loc, {"path", "selector"}, {"repo", "commit"})
    if loc.get("repo", repository) != repository: fail("OTHER_REPO_NEEDS_LOCAL_SOURCE")
    ref = loc.get("commit", default_ref)
    body, oid = read_git(repo, ref, loc["path"])
    part = selected(body, text(loc["selector"]))
    meta = {"repo": repository, "commit": ref, "path": loc["path"], "selector": loc["selector"], "blob": oid}
    return part, meta


def cite(meta: dict) -> str:
    return meta["repo"] + "@" + meta["commit"] + ":" + meta["path"] + "::" + meta["selector"]


def resolve(loc: dict, carrier: dict) -> dict:
    if isinstance(loc, dict) and set(loc) == {"answer_ref"}:
        return {k: carrier[k] for k in ("repo", "commit", "path")} | {"selector": loc["answer_ref"]}
    return loc


def render_source_reads(repo: Path, entries: Any, carrier: dict, repository: str,
                        reader: Callable | None = None) -> tuple[str, list[dict]]:
    """Render already-selected DR14 sources; never discover links or certify reading."""
    if entries is None or entries == []:
        return ("本绑定尚未展开source_reads；本次角色按已给完整任务和方法入口取得所需正文。"
                "原责任者在下一次正常改派/绑定更新中补齐准确位置、用途及相邻合同；"
                "不为补字段重发旧任务，也不把缺少清单写成已经读取。", [])
    if not isinstance(entries, list): fail("SOURCE_READS_ARRAY_REQUIRED")
    reader = reader or source
    requirements = {"MODE_FULL", "FOCUS_FULL", "BOUNDARY", "PROVENANCE_TRIGGER"}
    blocks, metas = [], []
    for entry in entries:
        item = obj(entry, {"source", "requirement", "purpose"}, {"reuse_evidence"})
        requirement = text(item["requirement"])
        if requirement not in requirements: fail("SOURCE_READ_REQUIREMENT")
        purpose = text(item["purpose"])
        loc = resolve(item["source"], carrier)
        if isinstance(loc, dict) and loc.get("source_kind") in {"OWNER_MESSAGE", "ATTACHMENT"}:
            blocks.append("- " + requirement + "；用途与边界：" + purpose
                          + "\n  原始来源：`" + json.dumps(loc, ensure_ascii=False, sort_keys=True)
                          + "`\n  原件由接收者实际取得；本工具未读取或验证原件。")
            continue
        obj(loc, {"commit", "path", "selector"}, {"repo"})
        ref = text(loc["commit"])
        if not SHA.fullmatch(ref): fail("EXACT_COMMIT_REQUIRED")
        path, selector = text(loc["path"]), text(loc["selector"])
        p = PurePosixPath(path)
        if p.is_absolute() or ".." in p.parts or "\\" in path or path.startswith("-"):
            fail("UNSAFE_PATH")
        source_repo = text(loc.get("repo", repository))
        if source_repo == repository:
            _, meta = reader(repo, loc, repository)
            availability = "本checkout已核位置；正文仍须接收者实际读取。"
        else:
            meta = {"repo": source_repo, "commit": ref, "path": path,
                    "selector": selector, "blob": None}
            availability = "外仓准确定位；本checkout未读取，接收者按原工具取得正文。"
        metas.append(meta)
        reuse = item.get("reuse_evidence")
        reuse_note = ("本次不主张已读复用。" if reuse is None else
                      "所给复用依据：" + json.dumps(reuse, ensure_ascii=False, sort_keys=True)
                      + "；仍须同一上下文、未变且关键内容可恢复。")
        blocks.append("- " + requirement + "：`" + cite(meta) + "`\n  用途与边界："
                      + purpose + "\n  " + availability + " " + reuse_note)
    return "\n\n".join(blocks), metas


def find_return(body: str) -> dict:
    found = []
    for raw in re.findall(r"```(?:json)?\s*\n(.*?)\n```", body, re.S):
        try: v = loads(raw)
        except (ValueError, TypeError): continue
        if isinstance(v, dict) and v.get("kind") == "RETURN" and str(v.get("schema", "")).startswith("question-work/"):
            found.append(v)
    if len(found) != 1: fail("ONE_QUESTION_WORK_RETURN_REQUIRED")
    return found[0]


def dispatch_identity(body: str) -> dict:
    try:
        value = loads(body)
    except (ValueError, TypeError):
        value = None
    if isinstance(value, dict) and str(value.get("schema", "")).startswith("coordinator-message/"):
        return {key: text(value[key]) for key in ("work_id", "invocation_id", "role", "recipient")}
    found = {}
    for key in ("work_id", "invocation_id", "role", "recipient"):
        hits = re.findall(r"(?m)^" + re.escape(key) + r":\s*(.+?)\s*$", body)
        if len(hits) != 1:
            fail("ORIGINAL_DISPATCH_IDENTITY_REQUIRED:" + key)
        found[key] = text(hits[0])
    return found


def mode_definition(work: dict, mode: Any) -> dict:
    modes = work["modes"]
    if not isinstance(modes, dict) or not modes or mode not in modes:
        fail("BINDING_STAGE_OR_MODE_MISMATCH")
    definition = obj(modes[mode], {"display_name", "purpose"})
    if definition["purpose"] not in MODE_PURPOSES:
        fail("MODE_PURPOSE")
    text(definition["display_name"])
    return definition


def role_body(policy: str, role: str, stage: str) -> str:
    """Choose exact pre-authored role text. Stage is only a configured marker key.

    Specialized professional obligations live in BI-01 professional sources and
    the actual binding. The coordinator never reconstructs them from CYF A/B/C.
    """
    suffix = text(stage)
    if not re.fullmatch(r"[A-Z][A-Z0-9_-]{1,40}", suffix):
        fail("INVALID_STAGE_ID")
    if role == "management":
        return "\n\n".join([marked(policy, "MANAGEMENT_DUTY"),
                           marked(policy, "MANAGEMENT_STAGE_" + suffix)])
    if role in {"receiver", "review"}:
        return marked(policy, "READONLY_RECEPTION_" + suffix)
    return "\n\n".join([marked(policy, "TASK_DUTY"),
                       marked(policy, "STAGE_" + suffix)])


def current_sources_at_return(repo: Path, response_meta: dict, task_meta: dict,
                              adoption_meta: dict) -> bool:
    for meta in (task_meta, adoption_meta):
        if meta["repo"] != response_meta["repo"]:
            return False
        try:
            _, oid = read_git(repo, response_meta["commit"], meta["path"])
        except ValueError:
            return False
        if oid != meta["blob"]:
            return False
    return True


def prepare_bootstrap(repo: Path, policy_ref: str, config_path: str, event: dict,
                      policy: str, policy_oid: str, cfg_oid: str, repository: str,
                      work: dict, bootstrap: dict, bound_meta: dict) -> dict:
    b = obj(bootstrap, {"schema", "kind", "work_id", "goal_ref", "authority_ref",
                       "entry_sources", "existing_work_refs", "parent", "recipient_ref",
                       "return_to_ref", "question_ref", "instructions_ref"})
    if b["schema"] != "question-work/v2": fail("BOOTSTRAP_VERSION")
    if b["work_id"] != event["work_id"]: fail("BINDING_WORK_MISMATCH")
    if event["route"] != "same_work":
        fail("BOOTSTRAP_MANAGEMENT_ROUTE_REQUIRED")
    repair = event["dispatch_kind"] == "DELIVERY_REPAIR"
    if not repair and "repair_context" in event:
        fail("REPAIR_CONTEXT_ONLY_FOR_DELIVERY_REPAIR")
    for key in ("current_task_ref", "task_adoption_ref"):
        if key not in event: fail("CURRENT_TASK_AND_ADOPTION_REQUIRED")
    if event["current_task_ref"].get("selector") not in {"full", "全文"}:
        fail("CURRENT_TASK_FULL_TEXT_REQUIRED")
    mode = "M-START"
    definition = mode_definition(work, mode)
    target = text(b["recipient_ref"])
    text(b["return_to_ref"])
    goal, goal_meta = source(repo, work["goal_ref"], repository, policy_ref)
    bound_goal, bound_goal_meta = source(repo, b["goal_ref"], repository)
    if goal_meta != bound_goal_meta or goal != bound_goal:
        fail("BOOTSTRAP_FIXED_GOAL_MISMATCH")
    refs = [("本次首次管理输入", bound_meta), ("Owner完整目标", goal_meta)]
    for key, label in (("authority_ref", "本次启动授权"), ("instructions_ref", "本次原始要求"),
                       ("question_ref", "M-START完整题面")):
        loc = b[key]
        if key == "question_ref" and loc.get("selector") != "#m-start":
            fail("BOOTSTRAP_M_START_REQUIRED")
        _, meta = source(repo, loc, repository); refs.append((label, meta))
    parent = obj(b["parent"], {"status", "ref", "reason_ref"})
    if parent["status"] not in {"NOT_APPLICABLE_NEW_CASE", "PRESENT", "REQUIRED_MISSING"}:
        fail("BOOTSTRAP_PARENT_STATUS")
    if (parent["status"] == "PRESENT") != (parent["ref"] is not None):
        fail("BOOTSTRAP_PARENT_REFERENCE")
    for loc in [parent["reason_ref"]] + ([parent["ref"]] if parent["ref"] is not None else []):
        _, meta = source(repo, loc, repository); refs.append(("父合同及实际适用说明", meta))
    for key, label in (("entry_sources", "完整起始材料"), ("existing_work_refs", "已存在工作")):
        values = b[key]
        if not isinstance(values, list) or (key == "entry_sources" and not values):
            fail("BOOTSTRAP_ENTRY_SOURCES_REQUIRED")
        for loc in values:
            _, meta = source(repo, loc, repository); refs.append((label, meta))
    for key, label in (("current_task_ref", "当前生效任务"), ("task_adoption_ref", "当前任务采用依据")):
        _, meta = source(repo, event[key], repository); refs.append((label, meta))
    if repair:
        if event.get("latest_return_ref") or event.get("latest_response_ref"):
            fail("BOOTSTRAP_REPAIR_USES_ORIGINAL_AND_ISSUE_REFS")
        repair_context = obj(event.get("repair_context"),
                             {"original_dispatch_ref", "issue_ref", "missing_output_refs"})
        original, original_meta = source(repo, repair_context["original_dispatch_ref"], repository)
        original_id = dispatch_identity(original)
        if (original_id["work_id"] != event["work_id"]
                or original_id["role"] != "management"
                or original_id["recipient"] != target
                or original_id["invocation_id"] == event["invocation_id"]):
            fail("BOOTSTRAP_REPAIR_ORIGINAL_CALL_MISMATCH")
        _, issue_meta = source(repo, repair_context["issue_ref"], repository)
        missing = repair_context["missing_output_refs"]
        if not isinstance(missing, list) or not missing:
            fail("BOOTSTRAP_REPAIR_MISSING_OUTPUT_REFS_REQUIRED")
        refs.extend([("本次有限补交的原管理调用", original_meta),
                     ("已记录的具体交付缺件", issue_meta)])
        for loc in missing:
            _, meta = source(repo, loc, repository)
            refs.append(("需要补齐的原管理交付位置", meta))
    latest_return, latest_response = event.get("latest_return_ref"), event.get("latest_response_ref")
    if bool(latest_return) != bool(latest_response): fail("LATEST_RETURN_AND_RESPONSE_REQUIRED_TOGETHER")
    if latest_return:
        raw, meta = source(repo, latest_return, repository)
        _, response_meta = source(repo, latest_response, repository)
        if latest_response.get("selector") not in {"full", "全文"}: fail("LATEST_RESPONSE_FULL_TEXT_REQUIRED")
        if meta["blob"] != response_meta["blob"]: fail("LATEST_RETURN_RESPONSE_BLOB_MISMATCH")
        ret = find_return(raw)
        if ret.get("work_id") != b["work_id"]: fail("RETURN_WORK_MISMATCH")
        if ret.get("binding_ref") != event["binding_ref"]: fail("RETURN_BINDING_MISMATCH")
        refs.append(("最新完整管理回答", response_meta))
        _, continuation = source(repo, resolve(ret["continuation_ref"], meta), repository)
        refs.append(("同一管理事项最新接续", continuation))
    evidence = event.get("evidence_refs", [])
    if not isinstance(evidence, list): fail("EVIDENCE_ARRAY")
    for loc in evidence:
        _, meta = source(repo, loc, repository); refs.append(("本次实际证据", meta))
    identity = "\n".join(k + ": " + str(event[k]) for k in ("work_id", "invocation_id", "assignment_token"))
    identity += "\nrole: management\nrecipient: " + target + "\n当前阶段：专业任务 " + work["stage"]
    identity += ("\n当前职责：专业任务 " + work["stage"]
                 + (" 原管理交付缺件定向补交" if repair else " 首次实质管理"))
    locations = "\n".join(label + "：`" + cite(meta) + "`" for label, meta in refs)
    message = "[" + event["invocation_id"] + "]\n" + identity
    if repair:
        message += "\n\n" + marked(policy, "RETURN_REPAIR")
        message += "\n\n## 原调用与具体缺件的准确来源\n\n" + locations
        message += ("\n\n仅在原调用所对应的同一物理管理聊天里补齐具体交付；"
                    "不得重做 M-START、改变既有管理决定、创建新的专业任务或以此文本自称已发送。")
        message += "\n\n" + marked(policy, "RETURN_REPAIR_TAIL") + "\n"
    else:
        message += "\n\n" + role_body(policy, "management", work["stage"])
        message += "\n\n## Owner完整目的\n\n" + goal + "\n来源：" + cite(goal_meta)
        message += "\n\n## 本轮原文与位置\n\n" + locations
        message += "\n\n" + marked(policy, "REFERENCE_USE") + "\n\n" + marked(policy, "RETURN_TAIL") + "\n"
    sources = list({tuple(meta[k] for k in ("repo", "commit", "path", "selector", "blob")): meta
                    for _, meta in refs}.values())
    return {"schema": "coordinator-message/v3", "policy_commit": policy_ref, "policy_blob": policy_oid,
            "config_path": config_path, "config_blob": cfg_oid, "work_id": b["work_id"],
            "invocation_id": event["invocation_id"], "recipient": target, "role": "management",
            "stage": work["stage"], "mode": mode, "mode_display_name": definition["display_name"],
            "dispatch_kind": event["dispatch_kind"], "route": "same_work", "sources": sources, "message": message,
            "message_sha256": digest(message.encode("utf-8")),
            "delivery_key_sha256": digest((target + "\0" + message).encode("utf-8")),
            "sent": False, "semantic_review_passed": False,
            "limits": ("BOOTSTRAP 缺件补交仅使用原管理工作身份及实际缺件证据，"
                       "不重做管理业务、不授权新建聊天、不证明真实发送或实际接收。"
                       if repair else
                       "仅核首次管理输入的机械关系，不编计划或预算，不证明权限、专业判断或实际发送。")}


def prepare_dispatch(repo: str | Path, policy_ref: str, config_path: str, event: dict) -> dict:
    repo = Path(repo).resolve()
    obj(event, {"work_id", "invocation_id", "assignment_token", "binding_ref", "route", "send_state",
                "dispatch_kind"},
        {"current_task_ref", "task_adoption_ref", "latest_return_ref", "latest_response_ref",
         "repair_context", "evidence_refs", "observed_at", "effective_calls", "elapsed_hours"})
    for name in ("work_id", "invocation_id", "assignment_token"): text(event[name])
    if event["send_state"] not in {"NOT_SENT", "CONFIRMED_SEND_FAILED"}: fail("NOT_SAFE_TO_SEND")
    if event["dispatch_kind"] not in DISPATCH_KINDS: fail("DISPATCH_KIND")
    policy, policy_oid = read_git(repo, policy_ref, POLICY_PATH)
    cfg_raw, cfg_oid = read_git(repo, policy_ref, config_path)
    cfg = obj(loads(cfg_raw), {"schema", "repository", "works"})
    if cfg["schema"] != "coordinator-dispatch/v3": fail("CONFIG_VERSION")
    repository = text(cfg["repository"])
    if not isinstance(cfg["works"], dict) or event["work_id"] not in cfg["works"]: fail("UNKNOWN_WORK")
    w = obj(cfg["works"][event["work_id"]], {"stage", "modes", "goal_ref"})
    if not isinstance(w["stage"], str) or not re.fullmatch(r"[A-Z][A-Z0-9_-]{1,40}", w["stage"]): fail("STAGE")
    bound_raw, bound_meta = source(repo, event["binding_ref"], repository)
    b = loads(bound_raw)
    if isinstance(b, dict) and b.get("kind") == "BOOTSTRAP":
        return prepare_bootstrap(repo, policy_ref, config_path, event, policy, policy_oid,
                                 cfg_oid, repository, w, b, bound_meta)
    if b.get("kind") != "BINDING" or b.get("schema") not in {"question-work/v1", "question-work/v2"}: fail("BINDING_REQUIRED")
    if b.get("work_id") != event["work_id"]: fail("BINDING_WORK_MISMATCH")
    mode = text(b.get("professional_mode"))
    mode_def = mode_definition(w, mode)
    route_key = text(event["route"])
    if route_key.startswith("trigger:"):
        ts = [t for t in b.get("triggers", []) if t["trigger_id"] == route_key[8:]]
        if len(ts) != 1: fail("TRIGGER_NOT_BOUND")
        route = ts[0]["route"]
    else:
        if route_key not in b.get("routes", {}): fail("ROUTE_NOT_BOUND")
        route = b["routes"][route_key]
    role = route.get("recipient_role")
    if role not in ROLES: fail("ROLE_NOT_BOUND")
    target = text(route.get("recipient_ref"))
    _, request_meta = source(repo, resolve(route["instructions_ref"], bound_meta), repository)
    if role in {"review", "receiver"} and mode_def["purpose"] != "read_only_reception":
        fail("RECEPTION_MODE_REQUIRED")
    if role == "professional" and mode_def["purpose"] != "professional_work":
        fail("PROFESSIONAL_MODE_REQUIRED")
    repair = event["dispatch_kind"] == "DELIVERY_REPAIR"
    refs = [("本次原始要求", request_meta), ("上一轮实际采用的任务绑定", bound_meta)]
    goal = None
    goal_meta = None
    task_meta = None
    adoption_meta = None
    task_body = None
    current_work_body = None
    current_work_meta = None
    if repair:
        if "current_task_ref" in event or "task_adoption_ref" in event:
            fail("DELIVERY_REPAIR_MUST_NOT_LOAD_CURRENT_TASK")
        context = obj(event.get("repair_context"),
                      {"original_dispatch_ref", "issue_ref", "missing_output_refs"})
        original_body, original_meta = source(repo, context["original_dispatch_ref"], repository)
        original = dispatch_identity(original_body)
        if original["work_id"] != event["work_id"]: fail("DELIVERY_REPAIR_WORK_MISMATCH")
        if original["invocation_id"] == event["invocation_id"]: fail("DELIVERY_REPAIR_NEEDS_NEW_INVOCATION")
        if original["role"] != role:
            fail("DELIVERY_REPAIR_ROLE_MISMATCH:expected=" + original["role"] + ":actual=" + role)
        if original["recipient"] != target:
            fail("DELIVERY_REPAIR_RECIPIENT_MISMATCH:expected=" + original["recipient"] + ":actual=" + target)
        _, issue_meta = source(repo, context["issue_ref"], repository)
        missing = context["missing_output_refs"]
        if not isinstance(missing, list) or not missing: fail("MISSING_OUTPUT_REFS_REQUIRED")
        refs = [("原调用", original_meta), ("具体缺件检查", issue_meta),
                ("本次补交要求", request_meta), ("原调用采用的任务绑定", bound_meta)]
        for loc in missing:
            _, meta = source(repo, loc, repository)
            refs.append(("需要补齐的原产物", meta))
    else:
        if "repair_context" in event: fail("REPAIR_CONTEXT_ONLY_FOR_DELIVERY_REPAIR")
        if "current_task_ref" not in event or "task_adoption_ref" not in event:
            fail("CURRENT_TASK_AND_ADOPTION_REQUIRED")
        if event["current_task_ref"].get("selector") not in {"full", "全文"}:
            fail("CURRENT_TASK_FULL_TEXT_REQUIRED")
        task_body, task_meta = source(repo, event["current_task_ref"], repository)
        _, adoption_meta = source(repo, event["task_adoption_ref"], repository)
        goal, goal_meta = source(repo, w["goal_ref"], repository, policy_ref)
        refs = [("本次原始要求", request_meta), ("当前生效任务", task_meta),
                ("当前任务采用依据", adoption_meta), ("上一轮实际采用的任务绑定", bound_meta)]
    if role == "management" and not repair:
        for key, label in (("plan_ref", "上次管理安排与整体位置"), ("budget_ref", "原投入与复看条件"), ("full_scope_ref", "完整工作范围")):
            _, meta = source(repo, resolve(b[key], bound_meta), repository)
            refs.append((label, meta))
    elif role in {"review", "receiver"} and not repair:
        for key, label in (("full_scope_ref", "接收完整范围"), ("focus_ref", "本次接收重点"),
                           ("deliverables_ref", "接收交付"), ("completion_ref", "接收完成条件")):
            _, meta = source(repo, resolve(b[key], bound_meta), repository)
            refs.append((label, meta))
    elif not repair:
        _, meta = source(repo, resolve(b["full_scope_ref"], bound_meta), repository)
        refs.append(("完整工作范围", meta))
    latest_return = event.get("latest_return_ref")
    latest_response = event.get("latest_response_ref")
    if bool(latest_return) != bool(latest_response): fail("LATEST_RETURN_AND_RESPONSE_REQUIRED_TOGETHER")
    if latest_return:
        raw, return_meta = source(repo, latest_return, repository)
        response_raw, response_meta = source(repo, latest_response, repository)
        if latest_response.get("selector") not in {"full", "全文"}: fail("LATEST_RESPONSE_FULL_TEXT_REQUIRED")
        if return_meta["blob"] != response_meta["blob"]: fail("LATEST_RETURN_RESPONSE_BLOB_MISMATCH")
        r = find_return(raw)
        if r.get("work_id") != b["work_id"]: fail("RETURN_WORK_MISMATCH")
        if r.get("binding_ref") != event["binding_ref"]: fail("RETURN_BINDING_MISMATCH")
        if not response_raw.strip(): fail("LATEST_RESPONSE_EMPTY")
        refs.append(("最新完整回答", response_meta))
        if route_key == "same_work":
            cont_body, cont = source(repo, resolve(r["continuation_ref"], return_meta), repository)
            label = "原任务内最新接续"
            if not repair and current_sources_at_return(repo, response_meta, task_meta, adoption_meta):
                # Authorized latest continuation is not tied to any CYF Mission.
                current_work_body = text(cont_body)
                current_work_meta = cont
            else:
                label = "被当前任务替代的旧续作（仅历史）" if not repair else label
            refs.append((label, cont))
    if not repair and current_work_body is None:
        # New adopted tasks must use their full authorized text; do not infer
        # the current work from a special C_WORKFLOW/CURRENT_C_WORK marker.
        current_work_body = text(task_body)
        current_work_meta = task_meta
    ev = event.get("evidence_refs", [])
    if not isinstance(ev, list): fail("EVIDENCE_ARRAY")
    for loc in ev:
        _, meta = source(repo, loc, repository)
        refs.append(("本次实际证据", meta))
    context_body, context_metas = ("", [])
    if not repair:
        context_body, context_metas = render_source_reads(repo, b.get("source_reads"), bound_meta, repository)
    facts = []
    if "observed_at" in event:
        from datetime import datetime
        stamp = datetime.fromisoformat(text(event["observed_at"]).replace("Z", "+00:00"))
        if stamp.tzinfo is None: fail("TIMEZONE_REQUIRED")
        facts.append("观察时间：" + event["observed_at"])
    for key, label in (("effective_calls", "有效回交数"), ("elapsed_hours", "原起点累计小时")):
        if key in event:
            import math
            n = event[key]
            if isinstance(n, bool) or not isinstance(n, (int, float)) or not math.isfinite(n) or n < 0: fail("INVALID_EFFORT")
            facts.append(label + "：" + str(n))
    identity = "\n".join(k + ": " + str(event[k]) for k in ("work_id", "invocation_id", "assignment_token"))
    identity += "\nrole: " + role + "\nrecipient: " + target + "\n当前阶段：专业任务 " + w["stage"]
    if role == "management":
        duty = "专业任务 " + w["stage"] + " 实质管理与阶段接收"
    elif role in {"review", "receiver"}:
        duty = "专业任务 " + w["stage"] + " 独立只读审查"
    else:
        duty = mode_def["display_name"]
    identity += "\n当前职责：" + duty
    if duty != mode_def["display_name"]:
        identity += "\n对应专业工作：" + mode_def["display_name"]
    if repair:
        body = marked(policy, "RETURN_REPAIR")
    else:
        body = role_body(policy, role, w["stage"])
        body += "\n\n## Owner完整目的\n\n" + goal + "\n来源：" + cite(goal_meta)
    if not repair and current_work_body is not None:
        body += "\n\n## 本轮当前工作\n\n" + current_work_body + "\n来源：" + cite(current_work_meta)
    locations = "\n".join(label + "：`" + cite(meta) + "`" for label, meta in refs)
    message = "[" + event["invocation_id"] + "]\n" + identity + "\n\n" + body + "\n\n## 本轮原文与位置\n\n" + locations
    if not repair:
        message += "\n\n## 本次直接读取的上下文\n\n" + context_body
        message += "\n\n" + marked(policy, "REFERENCE_USE")
    if facts: message += "\n\n运行事实（来自现有记录）：\n" + "\n".join(facts)
    message += "\n\n" + marked(policy, "RETURN_REPAIR_TAIL" if repair else "RETURN_TAIL") + "\n"
    delivery_key = digest((target + "\0" + message).encode("utf-8"))
    source_metas = []
    seen_sources = set()
    for meta in ([m for m in (goal_meta, task_meta, adoption_meta) if m]
                 + [m for _, m in refs] + context_metas):
        key = tuple(meta[k] for k in ("repo", "commit", "path", "selector", "blob"))
        if key not in seen_sources:
            source_metas.append(meta)
            seen_sources.add(key)
    return {"schema": "coordinator-message/v3", "policy_commit": policy_ref, "policy_blob": policy_oid,
            "config_path": config_path, "config_blob": cfg_oid, "work_id": b["work_id"],
            "invocation_id": event["invocation_id"], "recipient": target, "role": role,
            "stage": w["stage"], "mode": mode, "mode_display_name": mode_def["display_name"],
            "dispatch_kind": event["dispatch_kind"], "route": route_key, "sources": source_metas,
            "message": message, "message_sha256": digest(message.encode()),
            "delivery_key_sha256": delivery_key, "sent": False,
            "semantic_review_passed": False,
            "limits": "仅核已采用输入的机械关系；不认证授权、实际阅读/使用、业务正确、实际发送或现场不可绕过。"}


def verify(prepared: dict, payload: bytes) -> None:
    if payload != prepared["message"].encode("utf-8"): fail("MESSAGE_CHANGED")


def verify_recipient(prepared: dict, recipient: str) -> None:
    if text(recipient) != prepared["recipient"]: fail("RECIPIENT_CHANGED")


def replay(repo: str | Path, original: dict, repository: str, expected_digest: str) -> bytes:
    body, _ = source(repo, original, repository)
    raw = body.encode("utf-8")
    if digest(raw) != expected_digest: fail("RECOVERY_DIGEST_MISMATCH")
    return raw


def checked_send(prepared: dict, payload: bytes, recipient: str,
                 sender: Callable[[str, bytes], Any]) -> Any:
    verify(prepared, payload)
    verify_recipient(prepared, recipient)
    return sender(recipient, payload)


def prepare(*args: Any, **kwargs: Any) -> dict:
    fail("LEGACY_CONTEXT_NOT_FOR_NEW_DISPATCH: use adopted config and prepare_dispatch; replay original for recovery")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=("prepare", "verify"))
    for name in ("repo", "ref", "config", "dispatch"): p.add_argument("--" + name, required=True)
    p.add_argument("--message-output"); p.add_argument("--output"); p.add_argument("--payload"); p.add_argument("--recipient")
    a = p.parse_args()
    try:
        event = loads(Path(a.dispatch).read_text(encoding="utf-8"))
        result = prepare_dispatch(a.repo, a.ref, a.config, event)
        if a.command == "verify":
            if not a.payload or not a.recipient or a.message_output: fail("VERIFY_PAYLOAD_AND_RECIPIENT_ONLY")
            verify(result, Path(a.payload).read_bytes()); verify_recipient(result, a.recipient); result["ok"] = True
        elif a.payload: fail("USE_VERIFY")
        outs = [Path(x).resolve() for x in (a.output, a.message_output) if x]
        protected = {Path(a.dispatch).resolve(), (Path(a.repo) / POLICY_PATH).resolve(), (Path(a.repo) / a.config).resolve()}
        if len(outs) != len(set(outs)) or any(x in protected for x in outs): fail("OVERWRITE_INPUT")
        if a.command == "prepare" and a.message_output: Path(a.message_output).write_bytes(result["message"].encode())
        report = {k: v for k, v in result.items() if k != "message"}
        raw = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if a.output: Path(a.output).write_text(raw, encoding="utf-8")
        print(raw, end="")
        return 0
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(json.dumps({"ok": False, "sent": False, "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__": raise SystemExit(main())
