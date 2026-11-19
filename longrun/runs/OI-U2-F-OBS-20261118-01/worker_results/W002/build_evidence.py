from pathlib import Path
import hashlib
import json
import os
import subprocess

RUN = Path(__file__).resolve().parent
SOURCE = RUN / 'source/observe-iterate'
RUN_ID = 'OI-U2-F-OBS-20261118-01'
WORKER = f'codex:{RUN_ID}:worker:W1'
RETURN_TO = f'chatgpt:{RUN_ID}:executor:E1'
COMMIT = 'f4f0e4b276b1118b779473c1fbe462bc7a64b358'
ORDER_REF = f'daowei2026/observe-iterate@2bdc0b96259b9c2a895113328b9ccc1172f09e6e:longrun/runs/{RUN_ID}/work_orders/W002/ORDER.json'
D_REL = f'longrun/runs/{RUN_ID}/artifacts/D/u2_f_caegraph_definition.py'
C_REL = f'longrun/runs/{RUN_ID}/artifacts/C/caegraph_display.py'
ENV = os.environ.copy()
ENV['GIT_OPTIONAL_LOCKS'] = '0'
ENV['PYTHONDONTWRITEBYTECODE'] = '1'


def git(*args):
    return subprocess.check_output(['git', '-C', str(SOURCE), *args], env=ENV)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save_json(relative, value):
    with (RUN / relative).open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


order = json.loads((RUN/'inputs/ORDER.json').read_bytes())
referenced_dir = RUN/'inputs/referenced'
referenced_dir.mkdir(exist_ok=False)
referenced = []
for index, ref in enumerate(order['input_refs'], 1):
    repository_commit, relative = ref.split(':', 1)
    repository, commit = repository_commit.split('@', 1)
    assert repository == 'daowei2026/observe-iterate'
    raw = git('show', commit + ':' + relative)
    path = referenced_dir / (f'{index:02d}_' + Path(relative).name)
    with path.open('xb') as stream:
        stream.write(raw)
    referenced.append({'ref': ref, 'path': str(path), 'bytes': len(raw), 'sha256': sha(raw)})
save_json('inputs/referenced_input_manifest.json', referenced)
binding_entry = next(item for item in referenced if item['ref'].endswith('/RUN_BINDING.json'))
binding = json.loads(Path(binding_entry['path']).read_bytes())
assert order['grant'] in binding['grants']
assert order['worker'] == WORKER and order['return_to'] == RETURN_TO
assert order['work_order_id'] == 'W002' and order['issuer_call_id'] == 'C0014'
assert order['delegation_ref'] == f'daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/{RUN_ID}/delegations/D005/DELEGATION.json'

head = git('rev-parse', 'HEAD').decode().strip()
diff = git('diff', '--binary', 'HEAD')
status = git('status', '--porcelain=v1', '--untracked-files=all')
assert head == COMMIT and not diff and not status
for name, raw in (('repair.diff', diff), ('final_git_status.txt', status), ('final_head.txt', (head+'\n').encode())):
    with (RUN/name).open('xb') as stream:
        stream.write(raw)
sources = {}
for name, relative, commit in (
    ('final_script', D_REL, COMMIT),
    ('c3_script', C_REL, '508d494c964d5dabeaa1e7ea17bef908f749e9c8'),
):
    raw = (SOURCE/relative).read_bytes()
    assert raw == git('show', commit+':'+relative)
    sources[name] = {'path': str(SOURCE/relative), 'ref': f'daowei2026/observe-iterate@{commit}:{relative}', 'bytes': len(raw), 'sha256': sha(raw), 'modified': False}
save_json('source_hashes.json', sources)

stage = json.loads((RUN/'source_stage_report.json').read_bytes())
ipc = json.loads((RUN/'private_shm_report.json').read_bytes())
log = (RUN/'logs/private_shm_mount.log').read_text()
assert log == 'unshare: write failed /proc/self/uid_map: Operation not permitted\n'
assert ipc['namespace_exit_code'] == 1 and ipc['namespace_inner_entered'] is False
assert ipc['alias_proven'] is False
assert ipc['semlock_probe_attempt_count'] == 0 and ipc['D_attempt_count'] == 0
assert list((RUN/'runtime/shm').iterdir()) == []
assert list((RUN/'output/u2_f_caegraph').iterdir()) == []
blocked = {
    'run_id': RUN_ID, 'work_order_id': 'W002', 'parent_delegation_id': 'D005',
    'factual_status': 'BLOCKED', 'proposed_outcome_after_transport': 'STOP',
    'blocking_stage': 'private user + mount namespace setup, before inner script entry',
    'argv': ipc['argv'], 'exit_code': 1, 'stderr_exact': log,
    'reported_operation': 'write /proc/self/uid_map', 'reported_error': 'Operation not permitted',
    'namespace_attempt_count': 1, 'namespace_inner_entered': False,
    'mount_bind_attempted': False, 'private_shm_backing_proven': False,
    'semlock_probe_attempt_count': 0, 'D_attempt_count': 0,
    'landlock_applied_this_work_order': False, 'host_shm_write_fallback': False,
    'cause_limit': 'The exact uid_map denial is observed. No further host-policy/capability diagnosis or bypass was attempted.',
    'stop_basis': 'W002 sections 5, 8 and 11 require stopping when the private user/mount envelope cannot be established; host /dev/shm fallback and platform patches are prohibited.',
    'f_instance_constructed': False, 'fields_json_existence': 'NOT_CHECKED',
    'f_rerun_called': False, 'producer_called': False, 'q_or_v_read': False,
    'source_changed': False, 'unknown_inflight_action': False,
}
save_json('first_blocker.json', blocked)

checks = {
    'active_order_json_mirror_matches_remote': (RUN/'inputs/ORDER.json').read_bytes() == (RUN/'inputs/ACTIVE_ORDER_REMOTE.json').read_bytes(),
    'active_order_md_mirror_matches_remote': (RUN/'inputs/ORDER.md').read_bytes() == (RUN/'inputs/ACTIVE_ORDER_REMOTE.md').read_bytes(),
    'e2_classification_mirror_matches_remote': (RUN/'inputs/E2_W001_RESULT_CLASSIFICATION.md').read_bytes() == (RUN/'inputs/E2_CLASSIFICATION_REMOTE.md').read_bytes(),
    'order_grant_matches_adopted_binding': order['grant'] in binding['grants'],
    'source_detached_at_D_commit': head == COMMIT and stage['detached_head'] is True and stage['verification_passed'] is True,
    'D_and_C3_exact_original_bytes': all(not item['modified'] for item in sources.values()),
    'source_worktree_clean': not diff and not status,
    'namespace_command_has_no_PID_namespace': '--pid' not in ipc['argv'] and '-p' not in ipc['argv'],
    'exact_uid_map_failure_saved': log == blocked['stderr_exact'],
    'namespace_exit_code_saved': (RUN/'logs/private_shm_mount.exit_code').read_text() == '1\n',
    'namespace_inner_script_never_entered': not (RUN/'logs/private_shm_mount.inner_entered').exists(),
    'private_shm_alias_not_claimed': ipc['alias_proven'] is False and not (RUN/'logs/private_shm_mount.alias_report.json').exists(),
    'semlock_probe_not_started': not (RUN/'logs/semlock_probe.exit_code').exists() and not (RUN/'logs/semlock_probe.log').exists(),
    'D_not_started': not (RUN/'logs/w2_run.started.json').exists() and not (RUN/'logs/w2_run.log').exists(),
    'runtime_shm_empty': not any((RUN/'runtime/shm').iterdir()),
    'output_directory_empty': not any((RUN/'output/u2_f_caegraph').iterdir()),
    'definition_report_not_generated': not (RUN/'output/u2_f_caegraph/definition_run_report.json').exists(),
}
assert all(checks.values())
save_json('evidence_checks.json', checks)

missing = [
    '私有 user/mount namespace 未能完成：/proc/self/uid_map 写入被拒绝',
    'namespace-local /dev/shm backing、findmnt、mountinfo 与 alias probe 尚未验证',
    'SemLock probe 未启动：必须先通过私有 shm 包络',
    'D 未启动；精确 F 实例及 fields.json 存在性未检查',
    '候选 HTML、definition_run_report.json、prepared_tables 与 plot_data 均未生成',
    'E3 核图接受与正式取数准入尚未发生',
]
facts = {
    'run_id': RUN_ID, 'work_order_id': 'W002', 'parent_delegation_id': 'D005',
    'issuer_call_id': 'C0014', 'worker': WORKER, 'return_to': RETURN_TO, 'order_ref': ORDER_REF,
    'factual_status': 'BLOCKED', 'proposed_outcome_after_transport': 'STOP',
    'source_stage_report': str(RUN/'source_stage_report.json'), 'source_root': str(SOURCE), 'head': head,
    'private_shm_report': str(RUN/'private_shm_report.json'), 'namespace_attempt_count': 1,
    'namespace_exit_code': 1, 'namespace_command_elapsed_seconds': ipc['elapsed_seconds'], 'namespace_duration_precision': 'exact',
    'end_to_end_duration_precision': 'unknown', 'private_shm_backing_proven': False,
    'semlock_probe_attempt_count': 0, 'semlock_probe_exit_code': None,
    'D_attempt_count': 0, 'D_exit_code': None, 'D_runtime_python_entry': None,
    'candidate_html': None, 'definition_run_report': None, 'prepared_tables': None, 'plot_data': None,
    'envelope_log': str(RUN/'logs/private_shm_mount.log'), 'D_run_log': None,
    'actual_source_modifications': False, 'repair_diff': str(RUN/'repair.diff'), 'repair_diff_bytes': 0,
    'first_blocker': str(RUN/'first_blocker.json'), 'landlock_applied_this_work_order': False,
    'host_shm_write_fallback': False, 'platform_patched': False, 'W001_write_operations': False,
    'f_instance_constructed': False, 'fields_json_existence': 'NOT_CHECKED', 'producer_called': False,
    'f_rerun_called': False, 'q_or_v_read': False, 'DATA_READY': False,
    'remote_push_performed': False, 'formal_worker_return_signed': False,
    'transport_state': 'AWAITING_CONTROLLER_PUBLICATION_AND_EXACT_REFS', 'missing': missing,
}
save_json('facts.json', facts)

report = f'''# W002 最小事实报告

run_id：{RUN_ID}
work_order_id：W002
parent_delegation_id：D005
issuer_call_id：C0014
worker：{WORKER}
return_to：{RETURN_TO}
order_ref：{ORDER_REF}

状态：BLOCKED。工单真实推进至指定私有 namespace 建立步骤，按原停止条件终止；运输后拟签认 outcome=STOP。
source staging：{RUN/'source_stage_report.json'}；SUCCESS，独立 detached HEAD={head}，D/C3 均存在且与原引用逐字节一致。
private shm：{RUN/'private_shm_report.json'}；未能进入 namespace 内部脚本，不能证明 backing 已建立。runtime/shm 已在 W002 内创建，权限 1777，目录为空。
最终脚本：{SOURCE/D_REL}；HEAD={head}，未修改，亦未执行。
候选 HTML：无。
运行日志：{RUN/'logs/private_shm_mount.log'}；D 运行日志无，因为 D 未启动。
退出码：namespace 命令为 1；SemLock probe 和 D 均未启动，二者无退出码，不能把 namespace 的 1 写成 D 退出码。
实际修改：D/C3 无修改；{RUN/'repair.diff'} 为 0 字节，{RUN/'final_git_status.txt'} 为空。
definition_run_report：无，未生成。

首个真实阻断的完整 stderr：

```text
{log.rstrip()}
```

实际命令：

```text
{' '.join(ipc['argv'])}
```

unshare、mount、findmnt 均为现有 util-linux 2.39.3，版本与路径记录于 {RUN/'tool_versions.json'}。命令只请求 user 和 mount namespace；没有请求 PID namespace。unshare 写入 /proc/self/uid_map 时返回 Operation not permitted，子 bash 尚未进入；因此 namespace 内的 mount --make-rprivate、bind mount、findmnt -T /dev/shm、mountinfo 采集、alias probe、SemLock probe、业务运行环境初始化、Landlock 和 D 全部未执行。runtime_worker.py 与 private_shm_episode.sh 是本次准备的条件执行入口，不是已经执行成功的证据。

实际次数：私有 namespace 尝试 1 次；SemLock probe 0 次；D 0 次。namespace 命令墙钟 {ipc['elapsed_seconds']:.9f} 秒（独立实测）。完整准备、输入核对、staging 和封存的端到端精确耗时未独立测量；不能把这一个子步骤的时长当作 W002 总成本。

W002 第五、八、十一节要求私有 mount 无法建立时停止。Worker 没有直接写宿主 /dev/shm，没有 sudo、其他 namespace 路径或宿主权限 fallback，没有 patch 平台库或改动 D/C3 来绕过 import，没有作进一步无界诊断。仅凭本日志不能进一步断言具体宿主安全策略或 capability 配置，也不能说明 D、F 数据或 CAEGraph 有缺陷。

F 未构造、fields.json 未检查；未调用 f.rerun、全历史 producer 或 Q/V；未生成 HTML、prepared_tables、plot_data；没有 DATA_READY 或正式取数准入。没有对 W001、其他 Run、既有平台源码、生产数据或外部 symlink 目标执行写操作，没有推送 source checkout。W001 的既有 STOP、Landlock 历史与已封存证据保持原样；W002 的直接阻断发生于 uid_map，早于本轮任何 Landlock 应用。

事实、日志、退出码、源码状态与完整正文运输包均限于 W002。正式 result_ref 与新增证据 manifest.ref 待主控按原字节发布后提供真实 commit；D/C3 可复用既有精确 refs。当前准备稿不是正式 worker_return，没有伪造未来 refs。真实 refs 返回后，在同一 W002 下核验并签认 longrun-worker-return/v2，回原 executor:E1 消费，继续 D005 / WI-E / M-E。
'''
with (RUN/'FACT_REPORT.md').open('x', encoding='utf-8') as stream:
    stream.write(report)
save_json('RETURN_PREPARATION.json', {
    'preparation_format': 'local-only; not a schema-valid formal Worker Return',
    'state': 'AWAITING_TRANSPORT_PUBLICATION',
    'target_schema_ref': 'daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json',
    'target_definition': '#/$defs/worker_return',
    'fixed_fields': {'schema': 'longrun-worker-return/v2', 'run_id': RUN_ID, 'work_order_id': 'W002', 'order_ref': ORDER_REF, 'worker': WORKER, 'return_to': RETURN_TO, 'outcome': 'STOP', 'missing': missing},
    'existing_manifest_entries': {name: {'ref': value['ref'], 'sha256': value['sha256']} for name, value in sources.items()},
    'awaiting_fields': ['result_ref', 'manifest entries for newly published evidence'],
    'result_local_path': str(RUN/'FACT_REPORT.md'), 'parent_delegation_id': 'D005',
    'publication_authority': 'Controller transports exact evidence; Worker does not push the source checkout.',
    'next_action': 'Receive actual published refs, verify hashes, then sign this W002 worker_return; do not rerun namespace, SemLock probe, D or producer.',
})
print(json.dumps({'factual_status': 'BLOCKED', 'proposed_outcome_after_transport': 'STOP', 'namespace_attempts': 1, 'semlock_probe_attempts': 0, 'D_attempts': 0, 'evidence_checks_passed': len(checks), 'referenced_inputs_saved': len(referenced), 'report_path': str(RUN/'FACT_REPORT.md')}, ensure_ascii=False))
