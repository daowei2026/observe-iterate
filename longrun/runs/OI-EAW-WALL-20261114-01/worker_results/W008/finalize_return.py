import datetime
import fcntl
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

B = Path('/dwdhome/fy/BASE_E6_2')
A = Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01')
R = B / '.oi-runs/OI-EAW-WALL-20261114-01/D004/W008'
F = R / 'final-return'
S = Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
TURN = '01a1ddd4-64b5-7672-a214-f8d8eb8aeef4'
OLD_TURN = '01a1dd94-f3c1-7450-888f-69e268898780'
PREFIX = 'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/W008/'
RETURN_PREFIX = 'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W008/'
COMMIT = 'e7d079f42bd7bd7434d63373799348d79df22696'
CONTROL_COMMIT = '0b741493bd1a5b845905f9b46e7de4a381075507'
ORDER_REF = 'daowei2026/observe-iterate@a61efeed234064599011ebc897e4da61928c2403:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W008/ORDER.json'
E1 = 'chatgpt:OI-EAW-WALL-20261114-01:executor:E1'
W1 = 'codex:OI-EAW-WALL-20261114-01:worker:W1'


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def save(path, value):
    assert path.parent == F
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def describe(path):
    data = path.read_bytes()
    stat = path.stat()
    return {
        'path': str(path), 'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
        'git_blob_sha': hashlib.sha1(b'blob ' + str(len(data)).encode() + bytes([0]) + data).hexdigest(),
        'mtime_ns_decimal': str(stat.st_mtime_ns), 'inode': stat.st_ino, 'dev': stat.st_dev
    }


def guard():
    assert Path.cwd() == B
    assert os.environ['HOME'] == '/home/dw'
    assert os.environ['CODEX_HOME'] == '/home/dw/.codex'
    assert sys.dont_write_bytecode
    holder = Path('/proc/255320')
    ticks = holder.joinpath('stat').read_text().rsplit(')', 1)[1].split()[19]
    assert ticks == '49586940'
    lock = B / '.oi-runs/OI-EAW-WALL-20261114-01/.D004-writer.lock'
    stat = lock.stat()
    fdstat = holder.joinpath('fd/3').stat()
    assert stat.st_ino == fdstat.st_ino == 14866078
    assert stat.st_dev == fdstat.st_dev
    fdinfo = holder.joinpath('fdinfo/3').read_text()
    assert 'FLOCK' in fdinfo and '255320' in fdinfo
    fd = os.open(lock, os.O_RDWR | os.O_NOFOLLOW | os.O_CLOEXEC)
    try:
        assert os.fstat(fd).st_ino == 14866078
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            raise RuntimeError('D004 lock unexpectedly available')
        except BlockingIOError as err:
            assert err.errno == 11
    finally:
        os.close(fd)
    owner = Path('/proc/2890')
    owner_ticks = owner.joinpath('stat').read_text().rsplit(')', 1)[1].split()[19]
    assert owner_ticks == '20139'
    return {
        'at': now(), 'holder_pid': 255320, 'startticks': ticks,
        'inode': stat.st_ino, 'dev': stat.st_dev, 'fd': 3, 'session': 17409,
        'fdinfo': fdinfo, 'independent_same_inode_competition_errno': 11,
        'holder_not_replaced_or_released': True, 'owner_pid': 2890,
        'owner_startticks': owner_ticks, 'owner_uid': owner.stat().st_uid,
        'HOME': os.environ['HOME'], 'CODEX_HOME': os.environ['CODEX_HOME'],
        'actual_cwd': str(Path.cwd()), 'PYTHONDONTWRITEBYTECODE': sys.dont_write_bytecode
    }


def native_facts():
    context = None
    session = None
    old_seal = None
    technical = {}
    with S.open() as stream:
        for line in stream:
            record = json.loads(line)
            payload = record.get('payload', {})
            if record['type'] == 'session_meta':
                session = payload
            if record['type'] == 'turn_context' and payload.get('turn_id') == TURN:
                context = payload
            if record['type'] != 'event_msg':
                continue
            item = payload.get('item', {})
            if payload.get('turn_id') == TURN and item.get('type') in ['CommandExecution', 'FileChange']:
                technical[item['id']] = {'native_timestamp': record.get('timestamp'), 'native_event': payload}
            if payload.get('turn_id') == OLD_TURN and item.get('type') == 'CommandExecution' and item.get('exit_code') == 0:
                try:
                    result = json.loads(item.get('aggregated_output', ''))
                except (json.JSONDecodeError, TypeError):
                    continue
                if isinstance(result, dict) and result.get('seal_validation') == 'PASS':
                    old_seal = {'id': item['id'], 'exit_code': 0, 'status': item['status'],
                                'completed_at_ms': payload.get('completed_at_ms'), 'result': result}
    assert session['id'] == '01a1da55-5881-7590-94a1-0661f0236977'
    assert context and context['cwd'] == str(B) and context['model'] == 'gpt-6.1-sol' and context['effort'] == 'max'
    assert old_seal and old_seal['status'] == 'completed'
    return context, old_seal, technical


def load_inputs():
    specifications = [
        (A / 'WORKER_TASK-W008-RETURN-ONLY.md', 6305, 'f4f2a72728e51a2eef29756c21500c6a8e3c27dad287fb29d3e8afbb296e572b'),
        (A / 'C0017-pin-ORDER.md', 14744, '148f5bd0b017cfbb5a298d9d413547ac5c11d4874479be20f94f029667322353'),
        (A / 'C0017-pin-ORDER.json', 5898, '4073eec0d7eb6736bb4a403c2eaaae626db462d02d2c873162701b5c60f81ca5'),
        (A / 'C0017-pin-PRO_RETURN.json', 1238, 'dc8e7584f3a8a89bf2d43da4821dff17147635d603b5833c5abf9743cb57f8cb'),
        (A / 'W008-published-refs.json', 577593, '188005f3ceada3b66bb2e3ec04e7f0da1d0bc7f9897bb71525750e7c2082face'),
        (A / 'W008-published-evidence-index.json', 116795, '49e139d9c68ad2984e4777771728c30b94f98753f8bd31cd01ee7ebc22b35156'),
        (A / 'W008-remote-publication-verification.json', 1364, '60c77e584ecd420cdbb08c91e87aab10fe71d7dad2564a3b1058b5a6e28c6840'),
        (A / 'W008-local-final-native.json', 6141, '281a5f3a1de7431eb14272553ce78554b4a89d5dedef1939b54a7445db1bfdb1'),
        (A / 'adopted-business-dc18a/longrun/contracts/longrun_schema_v2.json', 11508, '32c1e2409ff4936a87d688848736bb9af71fe0415d338ba66dd031e3149243d3'),
        (R / 'artifacts/LOCAL_STAGE_HANDOFF.json', 10314, 'de6de6554f090676f48aec3cbbd31f282220a05a9d14f2b49afa0b860d52ca23'),
        (R / 'artifacts/CURRENT_MATERIAL_MANIFEST.json', 9032, 'ab8fe73397bcb32999afce94c840e4c5f77641d8c67960ca75fb1fa403176252'),
        (R / 'artifacts/FREEZE_RECEIPT.json', 235898, '79917e6605f45b1e5798d4b475064a395790b5f244589902fe6afb98b5b05902')
    ]
    inputs = []
    for path, size, sha in specifications:
        row = describe(path)
        assert row['bytes'] == size and row['sha256'] == sha, str(path)
        inputs.append(row)
    def read(path):
        return json.loads(path.read_text())
    return {
        'input_checks': inputs,
        'order': read(A / 'C0017-pin-ORDER.json'),
        'issuer_return': read(A / 'C0017-pin-PRO_RETURN.json'),
        'publication': read(A / 'W008-published-refs.json'),
        'index': read(A / 'W008-published-evidence-index.json'),
        'controller_receipt': read(A / 'W008-remote-publication-verification.json'),
        'schema': read(A / 'adopted-business-dc18a/longrun/contracts/longrun_schema_v2.json'),
        'handoff': read(R / 'artifacts/LOCAL_STAGE_HANDOFF.json'),
        'material': read(R / 'artifacts/CURRENT_MATERIAL_MANIFEST.json'),
        'freeze': read(R / 'artifacts/FREEZE_RECEIPT.json')
    }


def verify_originals(data, old_seal):
    originals = data['publication']['originals']
    expected = {row['path']: row for row in originals}
    assert len(expected) == len(originals) == 354
    assert sum(row['bytes'] for row in originals) == 141179547
    actual_paths = sorted(str(path) for path in R.rglob('*') if path.is_file() and F not in path.parents)
    assert actual_paths == sorted(expected)
    metadata_count = 0
    current = []
    for row in originals:
        after = describe(Path(row['path']))
        assert all(after[key] == row[key] for key in ['bytes', 'sha256', 'git_blob_sha'])
        if 'mtime_ns_decimal' in row:
            assert all(after[key] == row[key] for key in ['mtime_ns_decimal', 'inode', 'dev'])
            metadata_count += 1
        current.append(after)
    assert metadata_count == 353
    for row in data['freeze']['all_files_except_this_receipt']:
        assert all(expected[row['path']][key] == row[key] for key in ['bytes', 'sha256', 'mtime_ns_decimal', 'inode', 'dev'])
    own = next(row for row in old_seal['result']['important_files'] if row['path'] == str(R / 'artifacts/FREEZE_RECEIPT.json'))
    after = describe(Path(own['path']))
    assert all(after[key] == own[key] for key in ['bytes', 'sha256', 'mtime_ns_decimal', 'inode', 'dev'])
    assert data['freeze']['file_count_including_this_receipt'] == 354
    return {
        'at': now(), 'original_count': 354, 'original_bytes': 141179547,
        'all_named_bytes_SHA256_gitblob_match': True,
        'metadata_353_from_freeze_plus_receipt_self_from_native_terminal': True,
        'current_inventory_digest_SHA256': hashlib.sha256(json.dumps(current, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        'mismatches': [], 'scope': '仅354具名原件；final-return明确排除；不重新调查、编译或读取业务大数据',
        'original_freeze_sha256': after['sha256'],
        'old_seal_native_terminal': {k: v for k, v in old_seal.items() if k != 'result'}
    }


def verify_publication(data):
    publication = data['publication']
    index = data['index']
    receipt = data['controller_receipt']
    assert publication['commit'] == receipt['commit'] == COMMIT
    assert publication['all_remote_byte_hash_verified'] and publication['all_originals_covered']
    assert receipt['all360_remote_path_blob_and_byte_identity'] and receipt['all354_original_bytes_archived']
    assert receipt['original_file_count'] == 354 and receipt['original_bytes'] == 141179547
    published = {row['ref']: row for row in publication['published_files']}
    assert len(index) == len(published) == 360
    for key, row in index.items():
        assert set(row) == {'ref', 'sha256'}
        assert row['ref'] == 'daowei2026/observe-iterate@' + COMMIT + ':' + PREFIX + key
        assert row['ref'] in published and row['sha256'] == published[row['ref']]['sha256']
        assert re.fullmatch('[a-f0-9]{64}', row['sha256'])
    direct = []
    members = []
    for row in publication['originals']:
        if row['publication_status'] == 'DIRECT_REMOTE_BYTE_VERIFIED':
            direct.append(row)
            assert row['direct_ref'] in published
            assert all(published[row['direct_ref']][k] == row[k] for k in ['bytes', 'sha256', 'git_blob_sha'])
        else:
            assert row['publication_status'] == 'BYTE_PRESERVING_ARCHIVE_MEMBER_REMOTE_VERIFIED'
            members.append(row)
            assert row['direct_ref'] is None and row['raw_target_not_published'] is True
            assert row['archive_manifest_ref'] == publication['binary_archive_manifest_ref']
            assert row['archive_manifest_ref'] in published
            assert not any(e['ref'].endswith(':' + row['publication_target']) for e in index.values())
    assert len(direct) == 308 and len(members) == 46
    assert len(publication['binary_archive_part_refs']) == receipt['binary_parts'] == 51
    assert all(ref in published for ref in publication['binary_archive_part_refs'])
    archive = describe(Path(receipt['archive']['path']))
    assert archive['bytes'] == receipt['archive']['bytes'] and archive['sha256'] == receipt['archive']['sha256']
    manifest = {key: dict(row) for key, row in index.items()}
    controller = publication['additional_controller_publications']
    assert len(controller) == 2
    by_name = {
        'PUBLISHED_EVIDENCE_INDEX.json': A / 'W008-published-evidence-index.json',
        'CONTROLLER_PUBLICATION_RECEIPT.json': A / 'W008-remote-publication-verification.json'
    }
    for row in controller:
        assert row['ref'] == 'daowei2026/observe-iterate@' + CONTROL_COMMIT + ':' + row['path']
        assert row['exact_utf8_match'] is True
        local = describe(by_name[Path(row['path']).name])
        assert all(local[k] == row[k] for k in ['bytes', 'sha256', 'git_blob_sha'])
        key = row['path'].removeprefix(PREFIX)
        assert key not in manifest
        manifest[key] = {'ref': row['ref'], 'sha256': row['sha256']}
    assert len(manifest) == 362
    return manifest, {
        'at': now(), 'evidence_commit': COMMIT, 'controller_commit': CONTROL_COMMIT,
        'direct_originals': 308, 'binary_archive_members': 46,
        'binary_member_original_bytes': receipt['binary_original_bytes'],
        'archive_parts': 51, 'published_evidence_entries': 360, 'additional_controller_entries': 2,
        'formal_manifest_entries': 362, 'local_archive': archive,
        'all_originals_byte_preserved': True,
        'remote_verification_author': '控制方真实逐路径readback；本阶段W1核本地原件与运输映射，没有重新向GitHub读取或写入',
        'controller_proof_basis': receipt['proof_basis'],
        'compare_endpoint_observed_files': receipt['compare_endpoint_observed_files'],
        'compare_limit': 'compare端点300项不能独立当360全量证明；采用回执列明的逐路径UTF8/base64及exact subtree范围',
        'raw_binary_refs_created': 0,
        'v2_member_representation': '用运输manifest和51分卷各自真实ref及各自文件SHA；binary原hash只保留原件/member映射，不与archive ref混配'
    }


def validator(data):
    original = data['schema']
    current = {'$schema': original['$schema'], '$defs': original['$defs'], '$ref': '#/$defs/worker_return'}
    Draft202012Validator.check_schema(current)
    return Draft202012Validator(current)


def check_identity(data):
    order = data['order']
    issuer = data['issuer_return']
    assert order['run_id'] == 'OI-EAW-WALL-20261114-01' and order['work_order_id'] == 'W008'
    assert order['worker'] == W1 and order['return_to'] == order['issuer'] == E1
    assert order['issuer_call_id'] == issuer['call_id'] == 'C0017'
    assert issuer['sender'] == E1 and ORDER_REF in issuer['issued_order_refs']
    assert order['delegation_ref'] == issuer['delegation_ref']
    assert data['handoff']['order_ref'] == ORDER_REF
    assert data['material']['outcome'] == data['handoff']['outcome'] == 'PARTIAL'
    assert data['material']['material_status'] == 'PARTIAL_WITH_LIMITS'
    for name in ['C0017-pin-ORDER.md', 'C0017-pin-ORDER.json', 'C0017-pin-PRO_RETURN.json']:
        assert (A / name).read_bytes() == (R / 'input' / name).read_bytes()


def build_return(data, manifest):
    retained = [row for row in data['material']['missing'] if row['id'] not in ['M-EVIDENCE-PUBLICATION', 'M-FORMAL-RETURN']]
    assert len(retained) == 7
    missing = [
        '[' + row['id'] + '] ' + ('material_status=PARTIAL_WITH_LIMITS；' if i == 0 else '') + row['reason']
        for i, row in enumerate(retained)
    ]
    missing += [
        '[LIMIT-BINARY-RAW-REF] 46个binary原始字节已由真实归档覆盖，原件出版缺口已解决；它们仅为archive-member，没有raw路径ref。V2 ref/sha256不能内嵌member定位，本manifest引用BINARY_TRANSPORT_MANIFEST及51分卷真实文件各自hash，不把原binary hash配给archive ref，不宣称raw直接出版。',
        '[M-FORMAL-RETURN-PUBLICATION] 本正式Return已在W008/final-return本地生成并作schema/身份/证据映射校验；自身远端出版、控制方独立worker_receipt/有效Owner-D Gate及route尚待主控实际执行。当前没有自身commit/ref，不引用自身或未来validation；本地校验不替代专业接受、W/D/父业务完成。'
    ]
    assert len(missing) == len(set(missing)) == 9
    result = {
        'schema': 'longrun-worker-return/v2', 'run_id': data['order']['run_id'],
        'work_order_id': 'W008', 'order_ref': ORDER_REF, 'worker': W1, 'return_to': E1,
        'outcome': 'PARTIAL',
        'result_ref': 'daowei2026/observe-iterate@' + COMMIT + ':' + PREFIX + 'WORKER_EXECUTION_REPORT.md',
        'missing': missing, 'manifest': manifest
    }
    assert result['result_ref'] == data['publication']['result_ref']
    assert manifest['WORKER_EXECUTION_REPORT.md']['sha256'] == '8c3fb9a360fbac3f56e37900873874dc71a60c6c77623f9ad8e4bd5e8508cf09'
    assert all('WORKER_RETURN.json' not in row['ref'] for row in manifest.values())
    assert all('RETURN_VALIDATION.json' not in row['ref'] for row in manifest.values())
    validator(data).validate(result)
    return result


def deliverable_map(data, manifest):
    originals = {row['path']: row for row in data['publication']['originals']}
    by_ref = {row['ref']: row for row in manifest.values()}
    mapped = []
    for index, old in enumerate(data['handoff']['deliverable_mapping']):
        assert old['order_literal'] == data['order']['deliverables'][index]
        row = {'index_0based': index, 'order_literal': old['order_literal'], 'published_evidence': []}
        for path in old['local_files']:
            original = originals[path]
            assert original['direct_ref'] in by_ref
            row['published_evidence'].append({'local_original': path, **by_ref[original['direct_ref']]})
        if index < 10:
            row['status'] = 'PUBLISHED_FACTS_WITH_SUBSTANTIVE_LIMITS_RETAINED'
        elif index == 10:
            row['status'] = 'CONDITIONAL_NOT_TRIGGERED_NO_EXISTING_SOURCE_CHANGE'
        else:
            row.update(status='FORMAL_RETURN_LOCAL_GENERATED_PENDING_CONTROLLER_PUBLICATION',
                       local_return=str(F / 'WORKER_RETURN.json'), own_ref=None,
                       reason='正式Return不作为自身manifest证据；不能为完成机械映射捏造self/future ref')
        mapped.append(row)
    assert len(mapped) == 12
    return mapped


def generate():
    before_lock = guard()
    data = load_inputs()
    check_identity(data)
    context, old_seal, technical = native_facts()
    originals = verify_originals(data, old_seal)
    manifest, publication = verify_publication(data)
    result = build_return(data, manifest)
    output = F / 'WORKER_RETURN.json'
    assert not output.exists()
    save(output, result)
    reread = json.loads(output.read_text())
    validator(data).validate(reread)
    assert reread == result
    original_after = verify_originals(data, old_seal)
    assert originals['current_inventory_digest_SHA256'] == original_after['current_inventory_digest_SHA256']
    validation = {
        'schema': 'w008-return-validation/v1', 'at': now(),
        'purpose': '仅本阶段正式Return本地校验，不是主控独立worker_receipt/最终Gate',
        'schema_validation': 'PASS_Draft202012Validator_actual_readback',
        'schema_source': next(x for x in data['input_checks'] if x['path'].endswith('longrun_schema_v2.json')),
        'identity_order_route': 'PASS_W008_ORIGINAL_W1_RETURN_ONLY_E1',
        'physical_context': context, 'lock_before': before_lock, 'lock_after': guard(),
        'return_file': describe(output), 'outcome': reread['outcome'],
        'material_status': 'PARTIAL_WITH_LIMITS', 'result_ref': reread['result_ref'],
        'manifest_entries_exact_ref_and_sha256_only': True,
        'manifest_count': len(manifest), 'missing': reread['missing'],
        'retained_original_substantive_missing_count': 7,
        'resolved_missing': [
            {'old_id': 'M-EVIDENCE-PUBLICATION', 'status': 'RESOLVED_BYTE_PRESERVING_PUBLICATION',
             'evidence_commit': COMMIT, 'controller_commit': CONTROL_COMMIT},
            {'old_id': 'M-FORMAL-RETURN', 'local_generation': 'RESOLVED_THIS_STAGE',
             'remote_publication': 'STILL_PENDING_AS_M_FORMAL_RETURN_PUBLICATION'}
        ],
        'publication_verification': publication, 'frozen_originals_before': originals,
        'frozen_originals_after': original_after, 'readonly_input_checks': data['input_checks'],
        'ORDER_deliverable_mapping': deliverable_map(data, manifest),
        'archive_member_limit_is_not_missing_original_bytes': True,
        'future_or_self_refs_created': 0,
        'investigation_material_compile_scenario_policy_reruns_this_phase': 0,
        'old_W007_restored_or_Return_generated': False,
        'GitHub_or_other_chat_writes': 0,
        'earlier_readonly_validation_failure': '运输originals中FREEZE自身行未带mtime_ns_decimal，首次只读检查KeyError停止；353metadata从freeze、receipt自身metadata从真实旧封存native exit0补核，未改原件',
        'terminal_boundary': '生成命令进行中时的校验；本阶段seal会在该命令真实终态后补命令日志及冻结；不预填自身exit0'
    }
    save(F / 'RETURN_VALIDATION.json', validation)
    handoff = {
        'schema': 'w008-return-phase-handoff/v1', 'at': now(),
        'run_id': data['order']['run_id'], 'work_order_id': 'W008',
        'physical_turn': TURN, 'worker': W1, 'return_to': E1, 'order_ref': ORDER_REF,
        'outcome': 'PARTIAL', 'material_status': 'PARTIAL_WITH_LIMITS',
        'return_file': describe(output), 'validation_file': describe(F / 'RETURN_VALIDATION.json'),
        'result_ref': reread['result_ref'], 'manifest_count': 362,
        'originals_frozen_unchanged': {'count': 354, 'bytes': 141179547},
        'missing': reread['missing'], 'resolved_evidence_publication': True,
        'formal_Return_publication_commit': None, 'formal_Return_ref': None,
        'publication_layout': '本目录每个实际文件仅运至worker_results/W008/同名路径；不把正式Return运到business results目录',
        'file_transport_targets': [
            {'local_path': str(F / name), 'target': RETURN_PREFIX + name}
            for name in ['WORKER_RETURN.json', 'RETURN_VALIDATION.json', 'RETURN_PHASE_HANDOFF.json',
                         'RETURN_PHASE_COMMAND_LOG.jsonl', 'RETURN_PHASE_FREEZE_RECEIPT.json', 'finalize_return.py']
        ],
        'remaining_controller_steps': [
            '确认本阶段原W1所有命令真实终态并独立核文件bytes/SHA',
            '将正式Return和同目录校验逐字出版到授权Run分支worker_results/W008/，取得真实commit/ref',
            '主控独立生成worker_receipt、执行有效Owner-D Gate并仅route原E1',
            '全部同W008写者终态后由Root真实释放D004锁；Worker不释放'
        ],
        'no_professional_acceptance_or_parent_completion': True,
        'goal_completion_scope': '仅本Return阶段本地原件交付，不是W/D/父业务完成'
    }
    save(F / 'RETURN_PHASE_HANDOFF.json', handoff)
    print(json.dumps({'generation': 'PASS', 'outcome': 'PARTIAL', 'manifest_count': 362,
                      'missing_count': 9, 'return_file': describe(output),
                      'validation_file': describe(F / 'RETURN_VALIDATION.json'),
                      'handoff_file': describe(F / 'RETURN_PHASE_HANDOFF.json')}, ensure_ascii=False))


def seal():
    lock = guard()
    data = load_inputs()
    check_identity(data)
    context, old_seal, technical = native_facts()
    originals = verify_originals(data, old_seal)
    manifest, publication = verify_publication(data)
    actual = json.loads((F / 'WORKER_RETURN.json').read_text())
    expected = build_return(data, manifest)
    assert actual == expected
    validator(data).validate(actual)
    validation = json.loads((F / 'RETURN_VALIDATION.json').read_text())
    assert describe(F / 'WORKER_RETURN.json')['sha256'] == validation['return_file']['sha256']
    assert originals['current_inventory_digest_SHA256'] == validation['frozen_originals_after']['current_inventory_digest_SHA256']
    for row in validation['readonly_input_checks']:
        assert describe(Path(row['path'])) == row
    assert not (F / 'RETURN_PHASE_FREEZE_RECEIPT.json').exists()
    for row in technical.values():
        item = row['native_event']['item']
        if item['type'] == 'CommandExecution':
            assert item['exit_code'] is not None
    with (F / 'RETURN_PHASE_COMMAND_LOG.jsonl').open('w') as stream:
        stream.write(json.dumps({
            'record_kind': 'capture_header', 'at': now(), 'physical_turn': TURN,
            'native_session_path': str(S),
            'scope': '只记本Return阶段当前turn完整终态CommandExecution/FileChange；排除Reasoning、旧调查内容和其他chat',
            'native_terminal_items': len(technical),
            'runtime_policy': '仅读取具名合同/运输/原354原件作校验；仅final-return新增；Python-B；HOME/CODEX_HOME不改',
            'lock': lock
        }, ensure_ascii=False) + '\n')
        for row in technical.values():
            stream.write(json.dumps({'record_kind': 'native_terminal_original', **row}, ensure_ascii=False) + '\n')
        stream.write(json.dumps({
            'record_kind': 'actual_sealing_process_at_capture', 'at': now(),
            'status': 'IN_FLIGHT_AT_CAPTURE', 'exit_code': None,
            'pid': os.getpid(),
            'startticks': Path('/proc/self/stat').read_text().rsplit(')', 1)[1].split()[19],
            'argv': sys.argv, 'cwd': str(Path.cwd()),
            'boundary': '自身封存OS进程尚在执行，不预填exit0；真实最终终态由工具回执交主控'
        }, ensure_ascii=False) + '\n')
    payload = sorted(path for path in F.iterdir() if path.is_file())
    assert len(payload) == 5
    records = [{**describe(path), 'publication_target': RETURN_PREFIX + path.name, 'ref': None} for path in payload]
    freeze = {
        'schema': 'w008-return-phase-freeze/v1', 'at': now(), 'root': str(F),
        'physical_turn': TURN, 'outcome': 'PARTIAL', 'material_status': 'PARTIAL_WITH_LIMITS',
        'files_except_this_receipt': records, 'count_including_this_receipt': 6,
        'bytes_excluding_this_receipt': sum(row['bytes'] for row in records),
        'receipt_bytes': 0, 'bytes_including_this_receipt': 0,
        'this_receipt': {'path': str(F / 'RETURN_PHASE_FREEZE_RECEIPT.json'),
                         'publication_target': RETURN_PREFIX + 'RETURN_PHASE_FREEZE_RECEIPT.json', 'ref': None},
        'self_hash_policy': '不伪造自hash；完成本命令后在真实工具stdout交付SHA',
        'local_schema_order_ref_hash_validation': 'PASS',
        'original354_unchanged': originals, 'lock_kept': guard(),
        'formal_Return_remote_commit_ref': None,
        'controller_independent_receipt_Gate_route': 'PENDING_REAL_CONTROLLER_ACTION',
        'seal_capture_terminal_boundary': '本进程进行中；最终exit以工具终态回执为准'
    }
    for _ in range(10):
        raw = (json.dumps(freeze, ensure_ascii=False, indent=2) + '\n').encode()
        if len(raw) == freeze['receipt_bytes']:
            break
        freeze['receipt_bytes'] = len(raw)
        freeze['bytes_including_this_receipt'] = freeze['bytes_excluding_this_receipt'] + len(raw)
    else:
        raise RuntimeError('freeze byte count did not converge')
    assert len(raw) == freeze['receipt_bytes']
    (F / 'RETURN_PHASE_FREEZE_RECEIPT.json').write_bytes(raw)
    paths = sorted(path for path in F.iterdir() if path.is_file())
    assert len(paths) == 6 and sum(path.stat().st_size for path in paths) == freeze['bytes_including_this_receipt']
    for row in records:
        assert all(describe(Path(row['path']))[k] == row[k] for k in ['bytes', 'sha256', 'mtime_ns_decimal', 'inode', 'dev'])
    final_originals = verify_originals(data, old_seal)
    assert originals['current_inventory_digest_SHA256'] == final_originals['current_inventory_digest_SHA256']
    guard()
    print(json.dumps({
        'seal_validation': 'PASS', 'outcome': 'PARTIAL', 'material_status': 'PARTIAL_WITH_LIMITS',
        'manifest_count': 362, 'missing_count': 9,
        'all_new_files': [{**describe(path), 'publication_target': RETURN_PREFIX + path.name} for path in paths],
        'original354_bytes': 141179547, 'original354_hashes_unchanged': True,
        'D004_lock': 'HELD_BY_ROOT_UNCHANGED', 'formal_Return_remote_ref': None,
        'remaining': 'Root逐字出版正式Return/校验，独立receipt/Gate仅route原E1；全部终态后Root释放锁'
    }, ensure_ascii=False))


if __name__ == '__main__':
    assert len(sys.argv) == 2
    if sys.argv[1] == 'generate':
        generate()
    elif sys.argv[1] == 'seal':
        seal()
    else:
        raise ValueError('expected generate or seal')
