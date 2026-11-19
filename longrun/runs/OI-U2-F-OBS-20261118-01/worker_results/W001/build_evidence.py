import datetime
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

RUN = Path(__file__).resolve().parent
SOURCE = RUN / "source/observe-iterate"
RUN_ID = "OI-U2-F-OBS-20261118-01"
HEAD = "f4f0e4b276b1118b779473c1fbe462bc7a64b358"
ORDER_REF = (
    "daowei2026/observe-iterate@74562f258d93fdea8db0ab334fb0ebb23f1cfb99:"
    f"longrun/runs/{RUN_ID}/work_orders/W001/ORDER.json"
)
WORKER = f"codex:{RUN_ID}:worker:W1"
RETURN_TO = f"chatgpt:{RUN_ID}:executor:E1"
D_REL = f"longrun/runs/{RUN_ID}/artifacts/D/u2_f_caegraph_definition.py"
C_REL = f"longrun/runs/{RUN_ID}/artifacts/C/caegraph_display.py"
ENV = os.environ.copy()
ENV["GIT_OPTIONAL_LOCKS"] = "0"
ENV["PYTHONDONTWRITEBYTECODE"] = "1"


def git(*args):
    return subprocess.check_output(["git", "-C", str(SOURCE), *args], env=ENV)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(relative, value):
    path = RUN / relative
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


actual_head = git("rev-parse", "HEAD").decode().strip()
diff = git("diff", "--binary", "HEAD")
status = git("status", "--porcelain=v1", "--untracked-files=all")
assert actual_head == HEAD
assert diff == b"", "Unexpected source modifications; do not seal"
assert status == b"", "Unexpected source worktree status; do not seal"
for name, raw in (
    ("repair.diff", diff),
    ("final_git_status.txt", status),
    ("final_head.txt", (actual_head + "\n").encode()),
):
    with (RUN / name).open("xb") as stream:
        stream.write(raw)

source_entries = {}
for key, relative, commit in (
    ("final_script", D_REL, HEAD),
    ("c3_script", C_REL, "508d494c964d5dabeaa1e7ea17bef908f749e9c8"),
):
    raw = (SOURCE / relative).read_bytes()
    assert raw == git("show", f"{commit}:{relative}")
    source_entries[key] = {
        "path": str(SOURCE / relative),
        "ref": f"daowei2026/observe-iterate@{commit}:{relative}",
        "bytes": len(raw),
        "sha256": sha(raw),
        "modified": False,
    }
write_json("source_hashes.json", source_entries)

definition_path = RUN / "output/u2_f_caegraph/definition_run_report.json"
definition = json.loads(definition_path.read_text())
runtime = json.loads((RUN / "logs/python_runtime.json").read_text())
finished = json.loads((RUN / "logs/w1_run.finished.json").read_text())
exit_code = int((RUN / "logs/w1_run.exit_code").read_text())
trace = (RUN / "logs/semlock_probe.strace").read_text()
denied = [line for line in trace.splitlines() if "/dev/shm/" in line and "EACCES" in line]
assert len(denied) == 1
match = re.search(r'"(/dev/shm/[^\"]+)"', denied[0])
assert match
probe_path = match.group(1)
write_json(
    "first_blocker.json",
    {
        "run_id": RUN_ID,
        "work_order_id": "W001",
        "factual_status": "BLOCKED",
        "proposed_worker_outcome_after_transport": "STOP",
        "primary_exception": definition["error_type"],
        "primary_error": definition["error"],
        "primary_stage": "D.main import mquant.frame, before make_features and fields.json guard",
        "import_side_effect_source": "/dwdhome/fy/BASE_E6_2_copy/mquant/apt/tool/misc.py:144",
        "import_side_effect": "ProcessPoolExecutor(max_workers=os.getpid() - 2)",
        "primary_traceback": definition["traceback"],
        "actual_execution_condition": runtime["write_boundary"],
        "diagnostic": {
            "scope": "stdlib multiprocessing.Lock only; D/F/Q/V not loaded",
            "blocked_path": probe_path,
            "syscall": denied[0],
            "primary_run_exact_ipc_filename": "not traced; diagnostic filename must not be attributed to primary run",
            "log": str(RUN / "logs/semlock_probe.log"),
            "trace": str(RUN / "logs/semlock_probe.strace"),
        },
        "interpretation": "The observed D run failed under the Worker-added strict W001 write boundary. A separate stdlib diagnostic shows the same SemLock operation needs /dev/shm IPC file creation. This is not proof of failure in the unguarded original environment or of missing F data.",
        "stop_basis": "W001 narrows writes to RUN_ROOT; changing external IPC access or import behavior is returned to E1 rather than selected by Worker.",
        "repair_applied": False,
        "producer_invoked": False,
        "f_instance_constructed": False,
        "fields_json_existence": "NOT_CHECKED",
    },
)

baseline_rel = f"longrun/runs/{RUN_ID}/artifacts/E/E1_EXECUTION_AND_REVIEW_BASELINE_C0013.md"
checks = {
    "active_order_json_matches_exact_remote_blob": (RUN / "inputs/ORDER.json").read_bytes()
    == git("show", "74562f258d93fdea8db0ab334fb0ebb23f1cfb99:" + f"longrun/runs/{RUN_ID}/work_orders/W001/ORDER.json"),
    "active_order_md_matches_exact_remote_blob": (RUN / "inputs/ORDER.md").read_bytes()
    == git("show", "973c0da06c28b0ce7f343205858d9002f97667c9:" + f"longrun/runs/{RUN_ID}/work_orders/W001/ORDER.md"),
    "baseline_mirror_matches_exact_remote_blob": (RUN / "inputs/E1_EXECUTION_AND_REVIEW_BASELINE_C0013.md").read_bytes()
    == git("show", "1a4d2e455a1175f1c20226fa9873c587c697021d:" + baseline_rel),
    "head_is_requested_D_commit": actual_head == HEAD,
    "source_worktree_clean": not status,
    "repair_diff_empty": not diff,
    "run_exit_is_1": exit_code == 1,
    "definition_report_records_failure": definition["completed"] is False,
    "traceback_is_import_semlock_failure": "_multiprocessing.SemLock" in definition["traceback"]
    and "from mquant.frame import" in definition["traceback"],
    "runtime_write_guard_was_active": runtime["landlock_abi"] >= 1,
    "diagnostic_denied_dev_shm_creation": bool(denied),
    "html_not_generated": not (RUN / "output/u2_f_caegraph/u2_f_caegraph.html").exists(),
    "prepared_tables_not_generated": not (RUN / "output/u2_f_caegraph/prepared_tables").exists(),
    "plot_data_not_generated": not (RUN / "output/u2_f_caegraph/plot_data").exists(),
}
assert all(checks.values()), checks
write_json("evidence_checks.json", checks)

missing = [
    "候选 u2_f_caegraph.html 未生成",
    "精确 F 实例与 fields.json 存在性未检查：导入阶段已停止",
    "prepared_tables 与 plot_data 未生成",
    "E2/E3 专业核图、图接受及 E4/W2 正式取数未执行",
]
facts = {
    "run_id": RUN_ID,
    "work_order_id": "W001",
    "order_ref": ORDER_REF,
    "worker": WORKER,
    "return_to": RETURN_TO,
    "factual_status": "BLOCKED",
    "proposed_worker_outcome_after_transport": "STOP",
    "source_stage_report": str(RUN / "source_stage_report.json"),
    "source_root": str(SOURCE),
    "head": actual_head,
    "final_script": source_entries["final_script"],
    "candidate_html": None,
    "definition_run_report": str(definition_path),
    "run_log": str(RUN / "logs/w1_run.log"),
    "run_exit_code": exit_code,
    "run_elapsed_seconds": finished["elapsed_seconds"],
    "run_duration_precision": "exact",
    "preparation_and_recovery_duration_precision": "unknown",
    "business_attempt_count": 1,
    "separate_diagnostic": "one stdlib SemLock probe; no D/F/Q/V execution",
    "repair_diff": str(RUN / "repair.diff"),
    "repair_diff_bytes": 0,
    "source_changed": False,
    "first_blocker": str(RUN / "first_blocker.json"),
    "f_instance_constructed": False,
    "fields_json_existence": "NOT_CHECKED",
    "f_rerun_called": False,
    "q_or_v_read": False,
    "producer_called": False,
    "prepared_tables": None,
    "plot_data": None,
    "remote_push_performed": False,
    "formal_worker_return_signed": False,
    "transport_state": "AWAITING_CONTROLLER_PUBLICATION_AND_EXACT_REFS",
    "missing": missing,
    "known_execution_deviations": [
        "Used a local wrapper for the existing run-python.sh environment to keep its .migration logs outside the execution path.",
        "Worker added a kernel Landlock write boundary. The fatal SemLock error is a result under that condition; it is not a demonstrated unguarded-product failure.",
        "An early AGENTS filename search accidentally included /dwdhome/fy, returning sibling paths. It was stopped; no sibling Run file body or phone ledger was read and no sibling file was modified.",
    ],
}
write_json("facts.json", facts)

report = f"""# W001 最小事实报告

run_id：{RUN_ID}
work_order_id：W001
worker：{WORKER}
return_to：{RETURN_TO}
order_ref：{ORDER_REF}

状态：BLOCKED。真实 D 执行一次；正式机读 Return 待运输后拟签认 outcome=STOP。
source staging：{RUN / 'source_stage_report.json'}；SUCCESS，detached HEAD={actual_head}。
最终脚本：{SOURCE / D_REL}；D/C3 均与原件逐字节一致。
候选 HTML：无。
运行日志：{RUN / 'logs/w1_run.log'}。
退出码：1；本次命令（含环境入口）壁钟 {finished['elapsed_seconds']:.6f} 秒（独立实测）；其余准备、检查和恢复未独立计时，不并入该数，总成本未知。
实际修改：无；{RUN / 'repair.diff'} 为 0 字节，{RUN / 'final_git_status.txt'} 为空。
definition_run_report：{definition_path}；completed=false，error_type=PermissionError。

首个致命阻断发生于 D:676 导入 mquant.frame。调用链到达工作区 mquant/apt/tool/misc.py:144 的 ProcessPoolExecutor(max_workers=os.getpid() - 2)，创建 _multiprocessing.SemLock 时得到 PermissionError: [Errno 13] Permission denied。尚未导入 make_features、构造 F 或检查 fields.json。因此不能声明精确 F 结果存在或缺失。

执行条件必须一并运输：Worker 为落实 W001 的目录写入限制额外采用了 Landlock，仅允许 W001 内文件写入。独立的标准库 multiprocessing.Lock 诊断（不加载 D/F/Q/V）在相同限制下证实 openat 创建 {probe_path} 被 EACCES 拒绝。该随机路径来自诊断，主运行的具体 IPC 文件名未跟踪。本结果证明的是该写入限制下的真实阻断，不能用来断言无保护原环境也会失败；不是已证实的 D/C3 或 F 产品缺陷。是否允许工作区外的运行时 IPC，或采用何种其他入口，交原 executor:E1 判断；Worker 未扩大写权限、改动全局库或选择另一业务方案。

实际入口为 /bin/bash {RUN / 'run_w001.sh'}。其复用现有 m3rc、.runtime/python-deps 及 run-python.sh 中已配置的 TLS 库，Python 为 {runtime['python_executable']}（3.10.13）；没有新建环境、安装依赖或切换项目版本。源码 cwd={SOURCE}。其执行 python {RUN / 'boundary_runner.py'} {SOURCE / D_REL} --output-dir {RUN / 'output/u2_f_caegraph'}。运行包装器、边界实现及实际环境记录均在证据包内。

日志中 nif2 的 DNS 报错后已采用现有 run-python.sh 的 M3HOST 回退；后续 D 确已启动。joblib 的串行模式警告与写入保护有关；上述两项都不能替代最终 SemLock 致命 traceback。

未调用 f.rerun、全历史 producer 或 Q/V；未生成 prepared_tables、plot_data；未标记 DATA_READY；未进行 E2/E3 核图或 E4/W2。未修改既有环境、生产数据、其他 Run 或外部 symlink 目标，未推送 source checkout。

范围偏差记录：早期一次 AGENTS 文件名定位误将范围包含 /dwdhome/fy，返回了相邻目录路径；随即收敛到精确路径。未读取相邻 Run 正文或手机台账，未修改相邻文件。

本地事实证据已封存；正式 result_ref 与新证据 manifest.ref 尚待主控原样发布后提供真实 commit。现有 D/C3 精确 refs 可复用；没有伪造未来 refs，也没有把本地准备稿宣称为正式 worker_return。收到真实 refs 后，在同一 W001 下核哈希并完成 longrun-worker-return/v2 签认；结果回原 executor:E1，专业分类与下一步由 E1 完成。
"""
with (RUN / "FACT_REPORT.md").open("x", encoding="utf-8") as stream:
    stream.write(report)

write_json(
    "RETURN_PREPARATION.json",
    {
        "preparation_format": "local-only; not a schema-valid formal Worker Return",
        "state": "AWAITING_TRANSPORT_PUBLICATION",
        "target_schema_ref": "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json",
        "target_definition": "#/$defs/worker_return",
        "fixed_fields": {
            "schema": "longrun-worker-return/v2",
            "run_id": RUN_ID,
            "work_order_id": "W001",
            "order_ref": ORDER_REF,
            "worker": WORKER,
            "return_to": RETURN_TO,
            "outcome": "STOP",
            "missing": missing,
        },
        "existing_manifest_entries": {
            key: {"ref": value["ref"], "sha256": value["sha256"]}
            for key, value in source_entries.items()
        },
        "awaiting_fields": ["result_ref", "manifest entries for newly published evidence"],
        "result_local_path": str(RUN / "FACT_REPORT.md"),
        "publication_authority": "controller transports exact evidence; Worker does not push source checkout",
        "next_action": "Receive exact published refs, independently compare bytes/hashes, then sign formal worker_return within this same W001 without rerunning the business command.",
    },
)
print("FACTUAL_STATUS=BLOCKED")
print("BUSINESS_ATTEMPT_COUNT=1")
print("SOURCE_DIFF_BYTES=0")
print("FORMAL_RETURN=AWAITING_TRANSPORT_REFS")
print(report)
