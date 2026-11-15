import json
import os
import hashlib
from pathlib import Path
from runtime import B, R, save, desc, now, guard

A = R / 'artifacts'
guard()
assert not (A / 'FREEZE_RECEIPT.json').exists()
order = json.loads((R / 'input/C0017-pin-ORDER.json').read_text())
idx = json.loads((R / 'input/W008-INPUT_INDEX.json').read_text())
assert len(idx) == 24
assert set(x['ref'] for x in idx) == set([order['instructions_ref'], *order['input_refs']])
for x in idx:
    p = R / 'input' / Path(x['local_path']).name
    b = p.read_bytes()
    assert len(b) == x['bytes'] and hashlib.sha256(b).hexdigest() == x['sha256']
    assert hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest() == x['gitblob']
assert desc(R / 'input/WORKER_TASK-W008.md')['sha256'] == '52e5ea0c4b194eaf51ae14905f389d7ffd2cf45c8f5ec03eb28028b79425a02c'
mat = json.loads((A / 'CURRENT_MATERIAL_MANIFEST.json').read_text())
assert mat['outcome'] == 'PARTIAL' and mat['material_status'] == 'PARTIAL_WITH_LIMITS'
for x in mat['raw_and_derived_materials']:
    y = desc(x['path'])
    assert y['bytes'] == x['bytes'] and y['sha256'] == x['sha256']
normal = [json.loads(l) for l in (R / 'materials/CURRENT_NORMAL_CHAIN.jsonl').read_text().splitlines() if '"firing"' in l]
assert len(normal) == 3 and [x['published_count'] for x in normal] == [1, 2, 1]
pubs = [o['canonical_typed_show'] for f in normal for o in f['published_occurrences']]
bson = [json.loads(l) for l in (R / 'materials/CURRENT_BSON_READER.jsonl').read_text().splitlines()]
assert [x['occurrence_show'] for x in bson] == pubs
assert all(x['readback_equal'] is True for x in bson)
recon = json.loads((R / 'materials/CURRENT_NORMAL_RECONCILIATION.json').read_text())
assert recon['state_rows'][-1]['A_is_empty']
assert 'WallEndedState' in recon['state_rows'][-1]['actual_C_update_map_show']
for file, err in [('EXISTING_CROSS_FIRING_DUPLICATE.jsonl', 'WallStartedTwice'), ('EXISTING_AFTER_END_UPDATE.jsonl', 'WallUpdateBeforeStart')]:
    rows = [json.loads(l) for l in (R / 'materials' / file).read_text().splitlines()]
    assert rows[-1]['result'] == 'Left' and rows[-1]['error_show'].startswith(err)
audit = json.loads((A / 'BASE_SIDE_EFFECTS_AND_DIFF_REPORT.json').read_text())
for x in audit['source_and_inputs_checks']:
    y = desc(x['after']['path'])
    assert all(y[k] == x['before'][k] for k in ['bytes', 'sha256', 'mtime_ns', 'inode', 'dev'])
for repo in audit['repo_checks']:
    for c in repo['comparisons']:
        assert Path(c['pre']['path']).read_bytes() == Path(c['post']['path']).read_bytes()
old = json.loads((A / 'W007_EVIDENCE_RETENTION_MANIFEST.json').read_text())
assert len(old['files']) == 85 and old['bytes'] == 2075599
assert not Path('/proc/251010').exists()
R7 = B / '.oi-runs/OI-EAW-WALL-20261114-01/D003/W007'
assert sorted(str(p) for p in R7.rglob('*') if p.is_file()) == sorted(x['path'] for x in old['files'])
assert not (R7 / 'WORKER_RETURN.json').exists() and not (R7 / 'final-return').exists()
assert not list(R.rglob('WORKER_RETURN.json'))
assert not (A / 'BASE_CHANGE_CANDIDATE.md').exists()
receipts = [json.loads(l) for l in (R / 'logs/COMMAND_EXECUTIONS.jsonl').read_text().splitlines()]
assert len(receipts) == 57
for q in receipts:
    assert q['exit_code'] is not None and q['timeout_seconds'] <= 600 and q['stop_reason'] is None
    for k in ['stdout', 'stderr']:
        y = desc(q[k]['path'])
        assert y['bytes'] == q[k]['bytes'] and y['sha256'] == q[k]['sha256']
        assert y['bytes'] < 5 * 1024**3
    for z in [R / 'receipts' / (q['label'] + '.json'), R / 'receipts' / (q['label'] + '.pre.json')]:
        assert z.is_file()
assert len([q for q in receipts if q['label'].startswith('existing-scenario-')]) == 2
assert not list(R.rglob('__pycache__'))
assert not any(p.is_symlink() for p in R.rglob('*'))

S = Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
turn = '01a1dd94-f3c1-7450-888f-69e268898780'
commands = {}
toolcalls = {}
outputs = set()
tool_records = []
contexts = []
active = False
with S.open() as f:
    for line in f:
        obj = json.loads(line)
        p = obj.get('payload', {})
        if obj['type'] == 'turn_context':
            active = p.get('turn_id') == turn
            if active:
                contexts.append(p)
        if obj['type'] == 'event_msg' and p.get('turn_id') == turn and p.get('type') == 'item_completed' and p.get('item', {}).get('type') in ['CommandExecution', 'FileChange']:
            commands[p['item']['id']] = {'native_timestamp': obj.get('timestamp'), 'native_event': p}
        if active and obj['type'] == 'response_item':
            if p.get('type') in ['custom_tool_call', 'function_call']:
                toolcalls[p['call_id']] = p
                tool_records.append({'native_timestamp': obj.get('timestamp'), 'native_tool_record': p})
            elif p.get('type') in ['custom_tool_call_output', 'function_call_output']:
                outputs.add(p['call_id'])
                tool_records.append({'native_timestamp': obj.get('timestamp'), 'native_tool_record': p})
assert contexts and all(c['model'] == 'gpt-6.1-sol' and c['effort'] == 'max' and c['cwd'] == str(B) for c in contexts)
for c in commands.values():
    item = c['native_event']['item']
    if item['type'] == 'CommandExecution':
        assert item['cwd'] in [str(B), 'file://' + str(B)]
        assert item['exit_code'] is not None, (item['id'], item['status'])
selfcalls = [
    {'native_tool_call': c, 'status': 'IN_FLIGHT_AT_CAPTURE', 'exit_code': None,
     'note': '本封存调用自身尚在执行；最终真实exit由工具终态回执给出，不预造exit0'}
    for key, c in toolcalls.items()
    if key not in outputs and 'seal_local_stage.py' in str(c.get('input', c.get('arguments', '')))
]
assert len(selfcalls) == 1, len(selfcalls)
with (A / 'NATIVE_TOOL_TRANSPORT_LOG.jsonl').open('w') as f:
    for row in tool_records:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
with (A / 'COMMAND_LOG.jsonl').open('w') as f:
    header = {
        'kind': 'capture_header', 'at': now(), 'physical_turn': turn,
        'native_session_path': str(S),
        'scope': '仅本W当前turn所有已终态CommandExecution/FileChange及本封存inflight原调用；完整命令/cwd/输出/exit/duration原文；不含Reasoning/其他turn/其他chat',
        'native_command_count': len(commands), 'self_inflight_count': len(selfcalls),
        'nested_command_receipts': str(R / 'logs/COMMAND_EXECUTIONS.jsonl'),
        'transport_log': str(A / 'NATIVE_TOOL_TRANSPORT_LOG.jsonl')
    }
    f.write(json.dumps(header, ensure_ascii=False) + '\n')
    for c in commands.values():
        f.write(json.dumps({'kind': 'native_execution_original', **c}, ensure_ascii=False) + '\n')
    for c in selfcalls:
        f.write(json.dumps({'kind': 'sealing_self_inflight', **c}, ensure_ascii=False) + '\n')

handoff = json.loads((A / 'LOCAL_STAGE_HANDOFF.json').read_text())
assert len(handoff['deliverable_mapping']) == len(order['deliverables']) == 12
for i, mapping in enumerate(handoff['deliverable_mapping']):
    assert mapping['order_literal'] == order['deliverables'][i]
    for file in mapping['local_files']:
        if Path(file).name not in ['PUBLICATION_MANIFEST.json', 'HASHES.sha256']:
            assert Path(file).is_file(), file
assert handoff['formal_return_to'] == 'chatgpt:OI-EAW-WALL-20261114-01:executor:E1'
validation = {
    'at': now(), 'schema': 'w008-local-validation/v1', 'outcome': 'PARTIAL',
    'material_status': 'PARTIAL_WITH_LIMITS',
    'task_6930_bytes_SHA256': 'PASS', 'exact_index24_bytes_SHA256_gitblob_refs': 'PASS',
    'actual_Sol_max_BASE_context': 'PASS', 'new_lock': guard(),
    'readonly_423_comparisons': len(audit['source_and_inputs_checks']),
    'three_repo_status_diff_unchanged': True, 'W00785_unchanged_no_resume_no_Return': True,
    'normal_three_calls_four_inputs_four_O': True, 'actual_End_A_empty_C_Ended': True,
    'actual_same_call_C_last_update': True, 'two_existing_expression_exact_errors': True,
    'four_BSON_readbacks_equal_same_normal_occurrences': True,
    'bounded_command_receipts_checked': len(receipts),
    'ORDER_12_literal_mapping': 'PASS_WITH_CONDITIONAL_NOT_TRIGGERED_AND_FORMAL_RETURN_DEFERRED',
    'all_refs_unpublished_null': True, 'no_self_future_Return': True,
    'conditional_BASE_CHANGE_CANDIDATE': 'NOT_TRIGGERED',
    'native_command_count': len(commands),
    'native_TOOL_transport_count': len(tool_records),
    'sealing_own_call_status': 'IN_FLIGHT_AT_CAPTURE_EXIT_NULL',
    'local_tooling_failures_preserved': [
        'PATH ghc/ghc-pkg libtinfo.so.5 loader exit127; existing same9.4.8 tinfo6 selected',
        'snapshot root361 exceeds declared200 child search; assertion stopped before child probes',
        'Worker observation-script OverloadedLists ambiguity compile exit1; only W008 script fixed',
        'archive-script creation quoting SyntaxError before file write; corrected using exact own native command',
        'first seal-script creation command rejected by exec CreateProcess nul byte validation; no OS process launched; corrected using apply_patch'
    ],
    'qualification_limits': mat['missing'],
    'hash_closure_validation': '在本同一封存命令随后实核；本记录不自证尚未完成的终态，成功以命令真实exit0及最终stdout为准'
}
save(A / 'LOCAL_VALIDATION.json', validation)

PREFIX = 'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/W008/'
def target(p):
    rel = p.relative_to(R)
    if rel.parts[0] == 'artifacts':
        rel = Path(*rel.parts[1:])
    return PREFIX + rel.as_posix()

def file_description(p):
    row = desc(p)
    b = p.read_bytes()
    try:
        b.decode('utf-8')
        text_file = b'\0' not in b
    except UnicodeDecodeError:
        text_file = False
    if text_file:
        mime = 'application/json' if p.suffix in ['.json', '.jsonl'] else 'text/plain'
    elif b.startswith(b'\x7fELF'):
        mime = 'application/x-executable' if os.access(p, os.X_OK) else 'application/x-object'
    else:
        mime = 'application/octet-stream'
    return {
        **row, 'relative_path': p.relative_to(R).as_posix(), 'mime_type': mime,
        'encoding': 'UTF-8' if text_file else 'NON_UTF8_BINARY_OR_NUL_DATA',
        'publication_target': target(p), 'ref': None
    }

closure_names = {'PUBLICATION_MANIFEST.json', 'HASHES.sha256', 'FREEZE_RECEIPT.json'}
payload = sorted(p for p in R.rglob('*') if p.is_file() and not (p.parent == A and p.name in closure_names))
descriptions = [file_description(p) for p in payload]
assert len(set(x['publication_target'] for x in descriptions)) == len(descriptions)
for d in descriptions:
    assert d['publication_target'].startswith(PREFIX)
save(A / 'PUBLICATION_MANIFEST.json', {
    'schema': 'w008-local-publication-manifest/v1', 'at': now(),
    'run_id': 'OI-EAW-WALL-20261114-01', 'work_order_id': 'W008',
    'outcome': 'PARTIAL', 'material_status': 'PARTIAL_WITH_LIMITS',
    'repository': 'daowei2026/observe-iterate',
    'publication_prefix': PREFIX, 'real_commit': None,
    'files': descriptions, 'payload_count': len(descriptions),
    'payload_bytes': sum(x['bytes'] for x in descriptions),
    'generated_hash_closure': [
        {'local_path': str(A / n), 'publication_target': target(A / n)}
        for n in ['PUBLICATION_MANIFEST.json', 'HASHES.sha256', 'FREEZE_RECEIPT.json']
    ],
    'closure_rule': 'manifest描述payload；HASHES覆盖payload与manifest；FREEZE覆盖除自身全部文件；自身真实SHA由终态工具回执交付，不伪造自hash',
    'formal_Worker_Return': '尚未生成；未来不进入本manifest/selfref',
    'binary_policy': '真实二进制逐字保留，类型/bytes/SHA如实；不能把不可运输项当已发布，真实refs须逐项回读'
})
hash_files = sorted(p for p in R.rglob('*') if p.is_file() and p not in [A / 'HASHES.sha256', A / 'FREEZE_RECEIPT.json'])
(A / 'HASHES.sha256').write_text(''.join(desc(p)['sha256'] + '  ' + p.relative_to(R).as_posix() + '\n' for p in hash_files))
freeze_files = sorted(p for p in R.rglob('*') if p.is_file() and p != A / 'FREEZE_RECEIPT.json')
frozen = [file_description(p) for p in freeze_files]
freeze = {
    'schema': 'w008-local-freeze-receipt/v1', 'at': now(),
    'root': str(R), 'work_order_id': 'W008', 'outcome': 'PARTIAL',
    'material_status': 'PARTIAL_WITH_LIMITS',
    'file_count_including_this_receipt': len(frozen) + 1,
    'bytes_excluding_this_receipt': sum(x['bytes'] for x in frozen),
    'receipt_bytes': 0, 'bytes_including_this_receipt': 0,
    'all_files_except_this_receipt': frozen,
    'this_receipt': {'local_path': str(A / 'FREEZE_RECEIPT.json'), 'publication_target': target(A / 'FREEZE_RECEIPT.json'), 'ref': None},
    'self_hash_policy': '不含自hash；真实SHA在完成本命令后的工具stdout交付',
    'source_qualified_unchanged': True,
    'old_W007_frozen85_retained': True,
    'new_D004_lock_kept_not_released': True,
    'formal_Return_created': False,
    'formal_Return_next': '真实出版refs回原W1同W008，仅生成Return只回原E1',
    'seal_call_at_command_log_capture': 'IN_FLIGHT; actual terminal receipt is authoritative'
}
for _ in range(10):
    blob = (json.dumps(freeze, ensure_ascii=False, indent=2) + '\n').encode()
    if freeze['receipt_bytes'] == len(blob):
        break
    freeze['receipt_bytes'] = len(blob)
    freeze['bytes_including_this_receipt'] = freeze['bytes_excluding_this_receipt'] + len(blob)
else:
    raise RuntimeError('freeze byte-count fixed point did not converge')
assert len(blob) == freeze['receipt_bytes']
(A / 'FREEZE_RECEIPT.json').write_bytes(blob)
all_files = sorted(p for p in R.rglob('*') if p.is_file())
assert len(all_files) == freeze['file_count_including_this_receipt']
assert sum(p.stat().st_size for p in all_files) == freeze['bytes_including_this_receipt']
for d in frozen:
    y = desc(d['path'])
    assert all(y[k] == d[k] for k in ['bytes', 'sha256', 'mtime_ns', 'inode', 'dev'])
for line in (A / 'HASHES.sha256').read_text().splitlines():
    sha, rel = line.split('  ', 1)
    assert desc(R / rel)['sha256'] == sha
guard()
important = [
    A / n for n in [
        'WORKER_EXECUTION_REPORT.md', 'LOCAL_STAGE_HANDOFF.json',
        'CURRENT_MATERIAL_MANIFEST.json', 'LOCAL_VALIDATION.json',
        'PUBLICATION_MANIFEST.json', 'HASHES.sha256', 'FREEZE_RECEIPT.json', 'COMMAND_LOG.jsonl'
    ]
]
print(json.dumps({
    'seal_validation': 'PASS', 'outcome': 'PARTIAL', 'material_status': 'PARTIAL_WITH_LIMITS',
    'files': len(all_files), 'bytes': freeze['bytes_including_this_receipt'],
    'non_utf8_or_binary_file_count': sum(x['encoding'] != 'UTF-8' for x in frozen),
    'formal_Return_created': False, 'new_D004_lock': 'HELD_BY_ROOT_UNCHANGED',
    'important_files': [desc(p) for p in important],
    'all_output_paths_SHA256_bytes_metadata_and_targets': str(A / 'FREEZE_RECEIPT.json'),
    'publication_prefix': PREFIX,
    'goal_completion_scope': '本W本地原件交付；非W/D/父任务完成'
}, ensure_ascii=False))
