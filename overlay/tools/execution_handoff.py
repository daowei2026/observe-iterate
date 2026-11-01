#!/usr/bin/env python3
"""Exact task reads, bound dispatch, and observed signal projection. No scheduler."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path


def module(name):
    spec=importlib.util.spec_from_file_location("_"+name,Path(__file__).with_name(name+".py"))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


SIGNALS=frozenset({"NEW_BATCH","FIRST_BUSINESS_SHAPE","IMPORTANT_PREMISE","REVIEW_RESULT",
    "CONSUMER_FEEDBACK","REAL_DATA_RESULT","OWNER_CHANGE","METHOD_CHANGE","STAGE_HANDOFF",
    "REPEATED_FAILURE","NO_SUBSTANTIVE_PROGRESS","UNASSIGNED_WORK","EXPECTATION_CHANGED","CONTEXT_LOSS"})
ACTION_KINDS=frozenset({"PRIMARY_CONTINUE","INDEPENDENT_RECEPTION","MANAGEMENT_REVIEW","DELIVERY_REPAIR"})
ACTION_STATES=frozenset({"NOT_SENT","CONFIRMED_SEND_FAILED","IN_FLIGHT","COMPLETED","UNKNOWN","BLOCKED","SUPERSEDED"})


def prepare(repo, ref, task_path, method_paths):
    if not method_paths: raise ValueError("PROFESSIONAL_METHOD_INPUT_REQUIRED")
    v=module("workmap_gate").GitView(repo,ref);text=v.text(task_path);methods=[]
    for path in dict.fromkeys(method_paths):
        v.text(path);methods.append({"path":path,"blob":v.oid(path)})
    return {"schema":"exact-task-delivery/v1","source_commit":ref,"task_path":task_path,
            "task_blob":v.oid(task_path),"task_text":text,
            "task_payload_sha256":hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "method_inputs":methods,"sent":False,"methods_read":False,
            "limits":"仅取得原文与方法身份；新消息使用dispatch，不将内层任务冒充已核整条消息。"}


def verify_payload(prepared,payload):
    if hashlib.sha256(payload.encode("utf-8")).hexdigest()!=prepared["task_payload_sha256"]:
        raise ValueError("TASK_PAYLOAD_CHANGED: do not paraphrase or append business restrictions")


def notice(events, handled, inflight):
    if not isinstance(events,list) or not isinstance(handled,list) or not isinstance(inflight,list):
        raise ValueError("events, handled and inflight must be lists from actual runner records")
    seen=set(handled)|set(inflight);selected=[]
    for event in events:
        if not isinstance(event,dict) or not event.get("id") or not event.get("kind") or not event.get("evidence"):
            raise ValueError("a management signal needs an identity, kind and actual evidence")
        if event["kind"]=="POLL":continue
        if event["kind"] not in SIGNALS:raise ValueError("unknown management signal:"+str(event["kind"]))
        if event["id"] in seen:continue
        selected.append(event);seen.add(event["id"])
    return {"schema":"management-notice/v1","management_required":bool(selected),"events":selected,
            "recipient":"management_review" if selected else None,"dispatched":False,"stop_unaffected_work":False,
            "instruction":"沿已绑定管理路线及Overlay08组装实际消息；同责任合并去重。" if selected else "继续现场已授权工作。",
            "limits":"信号性质来自实际记录；不评价业务、不设阈值、不写状态或实际发送。"}


def reconcile_actions(actions, records):
    """Keep separately issued work visible; never collapse it into the main continuation."""
    if not isinstance(actions,list) or not isinstance(records,list):
        raise ValueError("actions and records must be lists from actual adopted records")
    action_ids=[x.get("action_id") for x in actions if isinstance(x,dict)]
    if len(action_ids)!=len(actions) or any(not x for x in action_ids) or len(action_ids)!=len(set(action_ids)):
        raise ValueError("DUPLICATE_OR_INVALID_ACTION")
    record_ids=[x.get("action_id") for x in records if isinstance(x,dict)]
    if len(record_ids)!=len(records) or any(not x for x in record_ids) or len(record_ids)!=len(set(record_ids)):
        raise ValueError("DUPLICATE_OR_INVALID_ACTION_RECORD")
    by_id={x["action_id"]:x for x in records};out={k:[] for k in ("to_send","to_collect","completed","unknown","blocked","superseded")}
    for action in actions:
        if set(action)!={"action_id","kind","recipient_ref","evidence_ref"} or action["kind"] not in ACTION_KINDS:
            raise ValueError("INVALID_ISSUED_ACTION")
        if not all(isinstance(action[k],str) and action[k].strip() for k in ("recipient_ref","evidence_ref")):
            raise ValueError("ACTION_EVIDENCE_AND_RECIPIENT_REQUIRED")
        record=by_id.get(action["action_id"]);state="NOT_SENT" if record is None else record.get("state")
        if state not in ACTION_STATES:raise ValueError("UNKNOWN_ACTION_STATE")
        item=dict(action,state=state)
        if state in {"NOT_SENT","CONFIRMED_SEND_FAILED"}:out["to_send"].append(item)
        elif state=="IN_FLIGHT":out["to_collect"].append(item)
        elif state=="COMPLETED":out["completed"].append(item)
        elif state=="UNKNOWN":out["unknown"].append(item)
        elif state=="BLOCKED":out["blocked"].append(item)
        else:out["superseded"].append(item)
    orphan=sorted(set(by_id)-set(action_ids))
    if orphan:raise ValueError("ACTION_RECORD_WITHOUT_ISSUED_ACTION:"+",".join(orphan))
    return {"schema":"issued-action-reconciliation/v1",**out,"mutated":False,
            "limits":"只保留已签发动作及真实状态；不决定业务、授权、发送或完成。"}


def main():
    # One new-message front door: role/purpose are derived inside the assembler.
    if len(sys.argv)>1 and sys.argv[1]=="dispatch":
        sys.argv=sys.argv[:1]+sys.argv[2:]
        return module("management_prompt").main()
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest="command",required=True)
    q=sub.add_parser("prepare")
    for k in ("repo","ref","task"):q.add_argument("--"+k,required=True)
    q.add_argument("--method",action="append",required=True);q.add_argument("--verify-payload");q.add_argument("--output")
    q=sub.add_parser("notice");q.add_argument("--observations",required=True);q.add_argument("--output")
    q=sub.add_parser("reconcile-actions");q.add_argument("--actions",required=True);q.add_argument("--output")
    q=sub.add_parser("replay")
    for k in ("repo","repository","original-ref","expected-digest","message-output"):q.add_argument("--"+k,required=True)
    a=p.parse_args()
    try:
        if a.command=="prepare":
            out=prepare(a.repo,a.ref,a.task,a.method)
            if a.verify_payload:verify_payload(out,Path(a.verify_payload).read_text(encoding="utf-8"))
        elif a.command=="replay":
            m=module("management_prompt");loc=m.loads(Path(a.original_ref).read_text(encoding="utf-8"))
            if Path(a.message_output).resolve()==Path(a.original_ref).resolve():raise ValueError("OVERWRITE_INPUT")
            raw=m.replay(a.repo,loc,a.repository,a.expected_digest);Path(a.message_output).write_bytes(raw)
            out={"sent":False,"replay":True,"message_sha256":m.digest(raw)}
        elif a.command=="notice":
            data=json.loads(Path(a.observations).read_text(encoding="utf-8"))
            out=notice(data["events"],data.get("handled_event_ids",[]),data.get("inflight_event_ids",[]))
        else:
            data=json.loads(Path(a.actions).read_text(encoding="utf-8"))
            out=reconcile_actions(data["actions"],data.get("records",[]))
        raw=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
        if getattr(a,"output",None):Path(a.output).write_text(raw,encoding="utf-8")
        print(raw,end="");return 0
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print(json.dumps({"ok":False,"error":str(exc),"sent":False},ensure_ascii=False));return 2

if __name__=="__main__":raise SystemExit(main())
