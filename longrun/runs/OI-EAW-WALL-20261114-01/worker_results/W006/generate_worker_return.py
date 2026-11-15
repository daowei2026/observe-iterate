#!/usr/bin/python3.12
"""W006正式运输文件生成与验证；只读历史证据，不执行工程代码。"""
import datetime
import errno
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator


B = Path('/dwdhome/fy/BASE_E6_2')
A = Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01')
R = B / '.oi-runs/OI-EAW-WALL-20261114-01/D003/W006'
F = R / 'final-return'
NATIVE = Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
RUN = 'OI-EAW-WALL-20261114-01'
THREAD = '01a1da55-5881-7590-94a1-0661f0236977'
TURN = '01a1dcdb-b8ae-7980-8112-3ed42ea4aa43'
COMMIT = 'e9f4e0c569caa2939f3c5bfc2f882df6842f915f'
ORDER_REF = 'daowei2026/observe-iterate@050e7050a615709eadd10e811a75ad5a128db533:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W006/ORDER.json'
WORKER = 'codex:OI-EAW-WALL-20261114-01:worker:W1'
E1 = 'chatgpt:OI-EAW-WALL-20261114-01:executor:E1'
STOP_CODE = 'STOP_PROBE_HOLDER_FDINFO_READ_EACCES'
REPORT_SHA = '1332b77c97b889a0f77bec34977e56222565f229ce80613c200ebe225cc8b2b2'
PUBLICATION_PREFIX = 'longrun/runs/' + RUN + '/worker_results/W006/'
FINAL_NAMES = {
    'FINALIZE_PREFLIGHT.json', 'generate_worker_return.py',
    'WORKER_RETURN.json', 'WORKER_RETURN_VALIDATION.json', 'COMMAND_LOG.jsonl',
}
GENERATOR_COMMAND = (
    'PYTHONDONTWRITEBYTECODE=1 TMPDIR=' + str(F)
    + ' XDG_CACHE_HOME=' + str(F) + ' XDG_CONFIG_HOME=' + str(F)
    + ' /usr/bin/python3.12 -I -B ' + str(F / 'generate_worker_return.py')
)


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_bytes())


def facts(path):
    st = path.lstat()
    assert stat.S_ISREG(st.st_mode) and st.st_nlink == 1
    assert path.resolve() == path
    data = path.read_bytes()
    return {
        'path': str(path), 'bytes': len(data), 'sha256': sha(data),
        'mtime_ns': st.st_mtime_ns, 'mtime_ns_exact': str(st.st_mtime_ns),
        'inode': st.st_ino, 'dev': st.st_dev,
    }


def new_json(name, value):
    path = F / name
    assert name in FINAL_NAMES and path.parent == F
    data = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(data)
    return facts(path)


def lock_check():
    path = B / '.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock'
    ticks = Path('/proc/248632/stat').read_text().rsplit(')', 1)[1].split()[19]
    assert ticks == '48206357'
    st = path.lstat()
    assert stat.S_ISREG(st.st_mode) and st.st_ino == 14806399
    holder_fd = os.stat('/proc/248632/fd/3')
    assert (holder_fd.st_dev, holder_fd.st_ino) == (st.st_dev, st.st_ino)
    info = Path('/proc/248632/fdinfo/3').read_text()
    assert 'FLOCK' in info and 'WRITE 248632' in info and '14806399' in info
    fd = os.open(path, os.O_RDWR | os.O_NOFOLLOW | os.O_CLOEXEC)
    try:
        contender = os.fstat(fd)
        assert (contender.st_dev, contender.st_ino) == (st.st_dev, st.st_ino)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            assert error.errno in (errno.EAGAIN, errno.EACCES)
            blocked_errno = error.errno
        else:
            raise AssertionError('STOP_EXPECTED_HELD_LOCK_NOT_BLOCKING')
    finally:
        os.close(fd)
    return {
        'at': now(), 'holder_pid': 248632, 'startticks': ticks,
        'inode': st.st_ino, 'dev': st.st_dev, 'fd': 3,
        'session_as_dispatched': 91789, 'fdinfo': info,
        'same_inode_independent_competition_errno': blocked_errno,
        'only_own_contender_closed': True, 'holder_untouched': True,
        'scope': '普通已授权Return执行器核验；不是受限probe重跑。',
    }


def verify_originals(publication, expected):
    observed = []
    for entry in publication['files']:
        path = Path(entry['path'])
        assert path.is_relative_to(R) and not path.is_relative_to(F)
        row = facts(path)
        for key in ('bytes', 'sha256', 'mtime_ns', 'mtime_ns_exact', 'inode', 'dev'):
            assert row[key] == entry[key] == expected[str(path)][key], (str(path), key)
        data = path.read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\x00' + data).hexdigest()
        assert blob == entry['git_blob']
        assert entry['remote_content_equal'] and entry['remote_git_blob_equal']
        assert entry['ref'] == 'daowei2026/observe-iterate@' + COMMIT + ':' + entry['repo_path']
        assert entry['repo_path'] == (
            'longrun/runs/' + RUN + '/delegations/D003/results/W006/' + entry['relative']
        )
        observed.append(row)
    actual = set()
    for root, directories, files in os.walk(R, followlinks=False):
        for name in directories:
            assert not (Path(root) / name).is_symlink()
        if Path(root) == R:
            directories[:] = [name for name in directories if name != 'final-return']
        for name in files:
            actual.add(str(Path(root) / name))
            assert len(actual) <= 200
    assert actual == set(expected) == {entry['path'] for entry in observed}
    assert len(observed) == 93 and sum(row['bytes'] for row in observed) == 1805193
    hashes = (R / 'artifacts/HASHES.sha256').read_text().splitlines()
    assert len(hashes) == 91
    for line in hashes:
        digest, relative = line.split('  ', 1)
        assert expected[str(R / relative)]['sha256'] == digest
    freeze = read_json(R / 'artifacts/FREEZE_RECEIPT.json')
    assert len(freeze['all_files_except_this_receipt']) == 92
    for entry in freeze['all_files_except_this_receipt']:
        for key in ('bytes', 'sha256', 'mtime_ns', 'mtime_ns_exact', 'inode', 'dev'):
            assert entry[key] == expected[entry['path']][key]
    return {
        'file_count': 93, 'bytes': 1805193,
        'bytes_sha256_git_blob_mtime_ns_inode_dev_unchanged': True,
        'HASHES_entries_verified': 91, 'freeze_metadata_entries_verified': 92,
        'scope': '仅W006原93份具名文件，排除本阶段final-return；不是全BASE/HOME扫描。',
        'observations': observed,
    }


def check_ref(value):
    assert re.fullmatch(r'[^/@:]+/[^/@:]+@[0-9a-f]{40}:.+', value)
    path = value.split(':', 1)[1]
    assert '\\' not in path
    assert not any(part in ('', '.', '..', '.git') for part in path.split('/'))


def archive_commands():
    assert NATIVE.stat().st_size < 30000000
    commands = {}
    changes = {}
    last_context = None
    failed_commands = []
    with NATIVE.open() as stream:
        for line in stream:
            event = json.loads(line)
            payload = event.get('payload', {})
            if event.get('type') == 'turn_context':
                last_context = payload
            if event.get('type') != 'event_msg':
                continue
            if payload.get('turn_id') != TURN or payload.get('thread_id') != THREAD:
                continue
            if payload.get('type') != 'item_completed':
                continue
            item = payload.get('item', {})
            if item.get('type') not in ('CommandExecution', 'FileChange'):
                continue
            # 仅原生命令/文件改动事实，严格不导出Reasoning或整段会话。
            record = {
                'record_type': 'native_completed_item', 'timestamp': event.get('timestamp'),
                'thread_id': THREAD, 'turn_id': TURN,
                'started_at_ms': payload.get('started_at_ms'),
                'completed_at_ms': payload.get('completed_at_ms'), 'item': item,
            }
            if item['type'] == 'CommandExecution':
                raw_cwd = item['cwd']
                if raw_cwd.startswith('file:'):
                    parsed = urlsplit(raw_cwd)
                    assert parsed.scheme == 'file' and parsed.netloc == ''
                    normalized_cwd = unquote(parsed.path)
                else:
                    normalized_cwd = raw_cwd
                assert normalized_cwd == str(B)
                record['native_cwd_normalized'] = normalized_cwd
                if item['exit_code'] != 0:
                    assert item['id'] == 'exec-87871bfe-f720-48db-b2d7-ff6531924ee9'
                    assert item['status'] == 'failed' and item['exit_code'] == 1
                    assert "assert item['cwd'] == str(B)" in item['aggregated_output']
                    failed_commands.append({'id': item['id'], 'exit_code': item['exit_code']})
                else:
                    assert item['status'] == 'completed'
                commands[item['id']] = record
            else:
                changes[item['id']] = record
    context = {key: last_context[key] for key in ('turn_id', 'cwd', 'model', 'effort')}
    assert context == {'turn_id': TURN, 'cwd': str(B), 'model': 'gpt-6.1-sol', 'effort': 'max'}
    assert len(commands) >= 11
    assert len(failed_commands) == 1
    header = {
        'record_type': 'phase_command_log_scope', 'at': now(),
        'stage': 'W006_FORMAL_RETURN_ONLY', 'source': str(NATIVE),
        'thread_id': THREAD, 'turn_id': TURN,
        'native_completed_commands': len(commands), 'native_file_changes': len(changes),
        'failed_formal_generator_commands_preserved': failed_commands,
        'exact_native_command_argv_outputs_exit_duration_preserved': True,
        'reasoning_and_other_turns_exported': False,
        'scope': '本阶段截至冻结时的全部原生命令完成事件及FileChange；当前生成器在尾项如实记运行中。',
    }
    rows = [header]
    rows.extend(sorted([*commands.values(), *changes.values()], key=lambda row: row['timestamp']))
    rows.append({
        'record_type': 'current_generator_invocation_at_log_freeze',
        'at': now(), 'cwd': str(B), 'shell_command': GENERATOR_COMMAND,
        'source': '本次真实提交的exec_command；该进程此刻尚未返回。',
        'status': 'RUNNING_AT_LOG_FREEZE', 'exit_code_at_freeze': None,
        'terminal_evidence': '执行器真实退出码与原生完成事件在本记录冻结之后产生，交付末尾报告实际结果；不伪填未来退出码。',
    })
    log = F / 'COMMAND_LOG.jsonl'
    with log.open('xb') as stream:
        for row in rows:
            stream.write((json.dumps(row, ensure_ascii=False) + '\n').encode())
    return context, header, facts(log)


def main():
    assert sys.dont_write_bytecode and Path.cwd() == B
    assert os.environ['HOME'] == '/home/dw' and os.environ['CODEX_HOME'] == '/home/dw/.codex'
    assert os.environ['PYTHONDONTWRITEBYTECODE'] == '1'
    for name in ('TMPDIR', 'XDG_CACHE_HOME', 'XDG_CONFIG_HOME'):
        assert os.environ[name] == str(F)
    assert F.resolve() == F and F.is_dir()
    assert {path.name for path in F.iterdir()} == {
        'FINALIZE_PREFLIGHT.json', 'generate_worker_return.py', 'WORKER_RETURN.json',
    }
    assert facts(F / 'WORKER_RETURN.json')['sha256'] == 'a168c4e3cade10303f53b0b91705b53a33729615d87125e189a454f59075f283'
    lock_start = lock_check()
    preflight_bytes = (F / 'FINALIZE_PREFLIGHT.json').read_bytes()
    assert sha(preflight_bytes) == '8bb58fee4cffd07b18e78de7cf9b4cc2e06025af56260fd1d3fc24784d87f386'
    preflight = json.loads(preflight_bytes)
    assert preflight['status'] == 'LOCAL_TRANSPORT_PREFLIGHT_PASS'
    publication_bytes = (A / 'W006-published-refs.json').read_bytes()
    assert sha(publication_bytes) == '48441450735964443ab6aaefaa6dc3f43dae8dff0afc65b67b72e164d5303873'
    publication = json.loads(publication_bytes)
    assert publication['commit'] == COMMIT and publication['file_count'] == 93
    for key in ('all_remote_exact_bytes_gitblob_sha256_verified', 'only_93_allowed_added_paths', 'branch_head_verified'):
        assert publication[key] is True
    expected = {entry['path']: entry for entry in preflight['frozen_originals']['observations']}
    originals_before = verify_originals(publication, expected)
    for entry in preflight['readonly_contracts']:
        data = Path(entry['path']).read_bytes()
        assert len(data) == entry['bytes'] and sha(data) == entry['sha256']
        if 'frozen_identical_input' in entry:
            assert data == Path(entry['frozen_identical_input']).read_bytes()
    task_bytes = Path(preflight['task']['path']).read_bytes()
    assert len(task_bytes) == 6173 and sha(task_bytes) == '356c9bc7900704464a0c5f3c41539a1f8bf66a26f9ef045d4ea5fcc31a7490e7'

    order = read_json(A / 'C0014-remote-work_orders--W006--ORDER.json')
    contract = read_json(A / 'observe-iterate/longrun/contracts/longrun_schema_v2.json')
    Draft202012Validator({'$defs': contract['$defs'], '$ref': '#/$defs/order'}).validate(order)
    assert order['run_id'] == RUN and order['work_order_id'] == 'W006'
    assert order['issuer_call_id'] == 'C0014' and order['issuer'] == E1
    assert order['worker'] == WORKER and order['return_to'] == E1
    handoff = read_json(R / 'artifacts/LOCAL_STAGE_HANDOFF.json')
    assert handoff['outcome'] == 'STOP' and handoff['stop_code'] == STOP_CODE
    assert len(handoff['missing']) == 15
    assert [row['deliverable_literal'] for row in handoff['deliverable_mapping']] == order['deliverables']
    entries_by_path = {entry['path']: entry for entry in publication['files']}
    entries_by_ref = {entry['ref']: entry for entry in publication['files']}
    manifest = {}
    for entry in publication['files']:
        assert entry['relative'] not in manifest
        manifest[entry['relative']] = {'ref': entry['ref'], 'sha256': entry['sha256']}
    coverage = []
    for row in handoff['deliverable_mapping']:
        literal = row['deliverable_literal']
        local_files = row['local_files']
        if local_files:
            primary = entries_by_path[local_files[0]]
            assert literal not in manifest
            manifest[literal] = {'ref': primary['ref'], 'sha256': primary['sha256']}
            coverage.append({
                'deliverable_literal': literal, 'literal_manifest_alias_present': True,
                'associated_actual_evidence': [
                    {'path': path, 'ref': entries_by_path[path]['ref'], 'sha256': entries_by_path[path]['sha256']}
                    for path in local_files
                ],
                'substantive_status': '真实STOP证据/成功子事实；标签覆盖不是专业或业务PASS。',
            })
        else:
            assert literal in (order['deliverables'][13], order['deliverables'][15])
            coverage.append({
                'deliverable_literal': literal, 'literal_manifest_alias_present': False,
                'associated_actual_evidence': [],
                'explanation': (
                    '四项Phase0 PASS未成立，条件八EP未进入，保持无条件成果文件。'
                    if literal == order['deliverables'][13] else
                    '本阶段本地正式Return已生成；自身尚未出版，不能伪造self/future ref或把它列入自身manifest。'
                ),
            })
    assert len(manifest) == 107 and len(entries_by_ref) == 93
    assert sum(row['literal_manifest_alias_present'] for row in coverage) == 14
    missing = list(handoff['missing'][:12])
    missing[0] = (
        STOP_CODE + '：P0-P3及kernel policy/bootstrap/FIOCLEX成功事实保留；' + missing[0]
    )
    missing.append(
        '93份原证据已真实出版并逐项核验，证据出版缺口已解决；本阶段正式v2 WORKER_RETURN已本地生成并只回原E1。'
        '其自身与本阶段验证/命令日志/生成器/资格原件仍待主控逐字出版至worker_results/W006/，'
        '新Return实际ref、独立receipt及完整Gate尚未产生；ORDER标签“V2 WORKER_RETURN.json returning only to executor E1”'
        '不以未来或自身ref填入本Return manifest。'
    )
    missing.append(handoff['missing'][14])
    assert len(missing) == len(set(missing)) == 14
    report_entry = entries_by_path[str(R / 'artifacts/WORKER_EXECUTION_REPORT.md')]
    assert report_entry['sha256'] == REPORT_SHA and report_entry['ref'] == publication['result_ref']
    worker_return = {
        'schema': 'longrun-worker-return/v2', 'run_id': RUN, 'work_order_id': 'W006',
        'order_ref': ORDER_REF, 'worker': WORKER, 'return_to': E1, 'outcome': 'STOP',
        'result_ref': publication['result_ref'], 'missing': missing, 'manifest': manifest,
    }
    validator = Draft202012Validator({'$defs': contract['$defs'], '$ref': '#/$defs/worker_return'})
    validator.validate(worker_return)
    for key, value in manifest.items():
        assert set(value) == {'ref', 'sha256'}
        check_ref(value['ref'])
        assert value['ref'] in entries_by_ref and value['sha256'] == entries_by_ref[value['ref']]['sha256']
    assert {value['ref'] for value in manifest.values()} == set(entries_by_ref)
    check_ref(worker_return['order_ref'])
    check_ref(worker_return['result_ref'])

    # 以下只读取冻结JSON证据；绝不import、执行或修订原P0-P4/engine/probe。
    verdict = read_json(R / 'artifacts/PHASE0_RECOVERY_VERDICT.json')
    assert verdict['outcome'] == 'STOP' and verdict['stop_code'] == STOP_CODE
    assert [verdict['preparation_stages'][key] for key in ('P0', 'P1', 'P2', 'P3')] == ['PASS'] * 4
    assert verdict['R0_A1_attempts'] == 1 and verdict['R0_A1_exit_code'] == 1
    for key in ('R0_B_attempts', 'R0_C_attempts', 'scenario_runs', 'normal_runs', 'build_compile_serialization_current_material_runs'):
        assert verdict[key] == 0
    for key in ('WRITE_CONFINEMENT_PASS', 'OFFLINE_CLOSURE_PASS', 'FOUR_BUDGETS_KNOWN_WITHIN_CAP', 'CONTINUOUS_MONITORS_PASS', 'automatic_retry', 'policy_guard_or_probe_adjusted_after_attempt', 'conditional_EP_entered', 'professional_acceptance_or_parent_completion_decided'):
        assert verdict[key] is False
    static_evidence = read_json(R / 'artifacts/SECCOMP_FILTER_STATIC_EVALUATION.json')
    assert static_evidence['status'] == 'PASS'
    assert len(static_evidence['mandatory_and_extra_cases']) == 11
    assert all(row['PASS'] for row in static_evidence['mandatory_and_extra_cases'])
    assert static_evidence['semantic_comparison_cases'] == 24240
    assert len(static_evidence['candidate_jump_targets']) == 61
    for key in ('all_jumps_in_bounds', 'all_paths_explicit_terminal_action', 'no_unintended_fallthrough', 'non_ioctl_semantics_equivalent_to_baseline', 'only_verified_FIOCLEX_produces_expected_difference'):
        assert static_evidence[key] is True
    assert static_evidence['expected_FIOCLEX_differences'] == 4
    launcher = read_json(R / 'receipts/r0a1-launcher.json')
    assert launcher['abi'] == 6 and launcher['status'] == 'KERNEL_POLICY_INSTALLED_BEFORE_EXEC'
    assert len(launcher['calls']) == 6
    assert all(row['return'] >= 0 and row['errno'] == 0 for row in launcher['calls'])
    probe = read_json(R / 'receipts/probe-main.json')
    assert probe['status'] == 'FAILED_STOP' and len(probe['checks']) == 6
    assert all(row['PASS'] for row in probe['checks'])
    assert probe['error']['type'] == 'PermissionError' and '/proc/248632/fdinfo/3' in probe['error']['text']
    assert '[Errno 13]' in probe['error']['text']
    execution = read_json(R / 'receipts/r0a1-execution.json')
    assert execution['exit_code'] == 1 and execution['timed_out'] is False
    assert execution['started_at'] == '2026-11-15T01:21:38.944026+00:00'
    assert execution['completed_at'] == '2026-11-15T01:21:40.221839+00:00'
    kernel = read_json(R / 'artifacts/FIOCLEX_KERNEL_OBSERVATION.json')
    assert len(kernel['post_policy_FIOCLEX']) == 1
    assert kernel['post_policy_FIOCLEX'][0]['line'] == 1508
    assert kernel['post_policy_FIOCLEX'][0]['text'].endswith('FIOCLEX) = 0')
    assert kernel['same_descriptor_F_GETFD_after_FIOCLEX_proof'] is False
    trace = read_json(R / 'artifacts/FULL_WRITE_TRACE_REVIEW.json')
    assert trace['trace_lines'] == 2290
    assert trace['successful_descriptor_write_count'] == 3 and trace['successful_descriptor_write_bytes'] == 6594
    assert trace['successful_outside_file_writes_in_this_trace'] == trace['unknown_write_paths_in_this_trace'] == 0
    assert trace['global_zero_outside_writes_PASS'] is False and trace['probe_child_grandchild_count'] == 0
    assert trace['exact_failure_open']['line'] == 2240
    assert 'O_RDONLY|O_CLOEXEC) = -1 EACCES' in trace['exact_failure_open']['text']

    # 首次生成的合法Return保持字节不变；仅修正本阶段日志归档器的URI表示处理。
    assert read_json(F / 'WORKER_RETURN.json') == worker_return
    return_fact = facts(F / 'WORKER_RETURN.json')
    actual_return = read_json(F / 'WORKER_RETURN.json')
    assert actual_return == worker_return
    validator.validate(actual_return)
    context, command_header, command_fact = archive_commands()
    originals_after = verify_originals(publication, expected)
    assert originals_after == originals_before
    lock_end = lock_check()
    files_before_validation = sorted(path.name for path in F.iterdir())
    assert set(files_before_validation) == FINAL_NAMES - {'WORKER_RETURN_VALIDATION.json'}
    for path in F.iterdir():
        assert path.is_file() and not path.is_symlink()
    local_file_facts = [facts(F / name) for name in files_before_validation]
    validation = {
        'schema': 'w006-formal-return-local-validation/v1', 'at': now(),
        'stage': 'W006_FORMAL_RETURN_ONLY', 'status': 'LOCAL_RETURN_VALIDATION_PASS',
        'outcome': 'STOP', 'stop_code': STOP_CODE,
        'schema_validation': {
            'contract': str(A / 'observe-iterate/longrun/contracts/longrun_schema_v2.json'),
            'sha256': '32c1e2409ff4936a87d688848736bb9af71fe0415d338ba66dd031e3149243d3',
            'validator': 'jsonschema.Draft202012Validator',
            'same_worker_return_subschema_as_official_gate': '#/$defs/worker_return',
            'order_subschema': '#/$defs/order', 'order_and_return_valid': True,
        },
        'identity': {'run_id': RUN, 'work_order_id': 'W006', 'worker': WORKER, 'return_to': E1, 'order_ref': ORDER_REF},
        'current_context': context, 'physical_thread_id': THREAD,
        'HOME': os.environ['HOME'], 'CODEX_HOME': os.environ['CODEX_HOME'],
        'HOME_CODEX_reset': False, 'only_business_write_root': str(F),
        'lock_start': lock_start, 'lock_end': lock_end,
        'publication_receipt': preflight['publication_receipt'],
        'result_ref': report_entry['ref'], 'report_sha256': REPORT_SHA,
        'manifest_validation': {
            'entries': len(manifest), 'distinct_published_refs': len(entries_by_ref),
            'canonical_published_evidence_entries': 93, 'applicable_literal_aliases': 14,
            'all_values_exactly_ref_and_sha256': True,
            'all_refs_from_actual_publication_receipt': True,
            'all_local_bytes_sha256_git_blobs_match_receipt': True,
            'no_self_future_or_unperformed_conditional_refs': True,
            'literal_manifest_keys_uncovered': [row['deliverable_literal'] for row in coverage if not row['literal_manifest_alias_present']],
            'STOP_missing_explains_uncovered_literals': True,
            'deliverable_literal_coverage': coverage,
        },
        'missing_count': len(missing), 'missing': missing,
        'state_updates': {
            'old_handoff_preserved': True, 'old_evidence_publication_gap_resolved': True,
            'local_formal_return_generation_gap_resolved': True,
            'this_new_return_publication_and_independent_receipt_pending': True,
        },
        'formal_generator_correction': {
            'failed_native_command_id': 'exec-87871bfe-f720-48db-b2d7-ff6531924ee9',
            'failed_exit_code': 1,
            'initial_generator_bytes': 26771,
            'initial_generator_sha256': 'f1ec616a0ae90f6c66ae9ee963ab1887a35552791c275ae2a8c6c41f21223589',
            'cause': '原生命令cwd实际采用file:///dwdhome/fy/BASE_E6_2；初版日志归档器错误地要求原字段直接等于POSIX路径。实际进程cwd始终BASE。',
            'correction': '日志保留原字段并解析file URI后比较；保留该失败命令完整输出及exit1，未排除失败记录。',
            'previously_generated_return_reused_byte_identical': True,
            'return_bytes': return_fact['bytes'], 'return_sha256': return_fact['sha256'],
            'P0_P4_or_any_engineering_code_changed_or_rerun': False,
        },
        'frozen_evidence_facts_preserved': {
            'preparation_stages': verdict['preparation_stages'],
            'P3_cases': 11, 'P3_semantic_comparisons': 24240, 'P3_jumps': 61,
            'P3_actual_success_preserved': True, 'kernel_ABI': launcher['abi'],
            'kernel_install_calls': launcher['calls'], 'seccomp_instruction_count_as_frozen': 126,
            'bootstrap_and_post_policy_FIOCLEX_succeeded': kernel['post_policy_FIOCLEX'],
            'probe_six_prior_checks_passed': probe['checks'],
            'unique_R0_A1': {'started_at': execution['started_at'], 'completed_at': execution['completed_at'], 'elapsed_seconds': execution['elapsed_seconds'], 'exit_code': 1, 'timed_out': False},
            'readonly_holder_open_failure': trace['exact_failure_open'],
            'failure_type': 'PermissionError/EACCES', 'concrete_procfs_LSM_cause_investigated': False,
            'kernel_unsupported_static_failure_or_FIOCLEX_failure_claimed': False,
            'parent_unconfined_lock_recheck_does_not_erase_restricted_child_failure': True,
            'same_inside_FD_clear_FIOCLEX_GETFD_effect_test_reached': False,
            'full_inside_positive_negative_child_grand_symlink_socket_connect_probes_reached': False,
            'failed_chain_only_trace': {'lines': 2290, 'successful_writes': 3, 'bytes': 6594, 'outside_file_writes': 0, 'unknown_write_paths': 0},
            'global_zero_writes_or_confinement_PASS_claimed': False,
            'R0_B_C_entered': False, 'both_closure_candidates_assessed_or_failed_claimed': False,
            'four_budget_bounds_continuous_monitors_and_eight_EP_completed': False,
            'all_scenario_normal_current_material_runs': 0,
            'original26_named_input_check_is_not_global_BASE_HOME_scan': True,
        },
        'frozen_originals_before': {key: value for key, value in originals_before.items() if key != 'observations'},
        'frozen_originals_after': originals_after,
        'old93_before_after_identical': True,
        'readonly_contracts': preflight['readonly_contracts'],
        'command_log': {'path': command_fact['path'], 'sha256': command_fact['sha256'], 'bytes': command_fact['bytes'], **command_header},
        'new_local_files_except_this_validation': local_file_facts,
        'publication_handoff': {
            'publisher': '主控逐字运输；Worker无GitHub写授权',
            'targets': [{'local_path': str(F / name), 'publication_target': PUBLICATION_PREFIX + name, 'actual_ref': None} for name in sorted(FINAL_NAMES)],
            'self_hash_note': '本validation自身hash只在真实执行器末尾交付，不嵌自hash；新正式Return及其他新增文件无未来ref。',
        },
        'full_gate': {
            'status': 'PENDING_ACTUAL_RETURN_PUBLICATION_AND_INDEPENDENT_RECEIPT',
            'executed_here': False, 'pass_claimed': False,
            'reason': '完整Gate须主控提供真实新worker_return_ref、独立receipt及账本；本阶段仅schema/身份/运输事实验证，不伪造Gate输入。',
        },
        'professional_acceptance_action_eligibility_G_RUN_H3_parent_Q_or_parent_completion_decided': False,
        'engineering_P0_P4_revisions_retries_build_tests_runs_performed_this_stage': 0,
        'network_GitHub_or_other_chat_writes_performed': 0,
        'local_goal_completion_scope': '仅本地正式Return与验证交付结束；不代表W006、专业接受或父任务完成。',
    }
    new_json('WORKER_RETURN_VALIDATION.json', validation)
    assert {path.name for path in F.iterdir()} == FINAL_NAMES
    final_files = [facts(F / name) for name in sorted(FINAL_NAMES)]
    print(json.dumps({
        'status': 'LOCAL_RETURN_VALIDATION_PASS', 'outcome': 'STOP', 'stop_code': STOP_CODE,
        'manifest_entries': 107, 'distinct_actual_refs': 93, 'applicable_literal_aliases': 14,
        'missing_count': 14, 'old93_bytes_hash_metadata_unchanged': True,
        'full_gate': 'PENDING_ACTUAL_RETURN_PUBLICATION_AND_INDEPENDENT_RECEIPT',
        'return_to': E1, 'current_command_status_before_return': 'RUNNING',
        'files': [{**entry, 'publication_target': PUBLICATION_PREFIX + Path(entry['path']).name} for entry in final_files],
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
