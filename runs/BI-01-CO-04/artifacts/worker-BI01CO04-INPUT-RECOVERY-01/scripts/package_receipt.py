"""std-lib 独立消费校验和逐文件 receipt 封口，不读取源数据盘。"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
RUN = 'GTQH_C001_three_turns_20261101_162005'
OUTER = {'PACKAGE_RECEIPT.json', 'SHA256SUMS'}
HEADER = {
    'order_id': 'BI01CO04-INPUT-RECOVERY-01',
    'work_id': 'BI-01',
    'run_id': 'BI-01-CO-04',
    'issuer_invocation_id': 'BI01-CO-04-R0006-PROFESSIONAL-INTAKE-6fd91174',
    'return_to': 'chatgpt:BI-01-CO-04:management',
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory():
    files = []
    for p in sorted(ROOT.rglob('*')):
        rel = p.relative_to(ROOT)
        if '.runtime' in rel.parts:
            continue
        assert not p.is_symlink(), f'不允许未封口symlink: {rel}'
        if p.is_file():
            files.append(p)
    return files


def table(p):
    with p.open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        rows = list(reader)
    return columns, rows


def metadata(p):
    data = {'sha256': sha(p), 'bytes': p.stat().st_size,
            'rows': None, 'first_business_time': None, 'last_business_time': None,
            'business_time_field': None, 'not_applicable_reason': '非CSV或无统一业务时间列'}
    if p.suffix.lower() == '.csv':
        columns, rows = table(p)
        data['rows'] = len(rows)
        key = next((k for k in ['closeTs', 'event_ts', 'start_ts'] if k in columns), None)
        if key:
            times = [r[key] for r in rows if r.get(key)]
            data.update(first_business_time=min(times) if times else None,
                        last_business_time=max(times) if times else None,
                        business_time_field=key, not_applicable_reason=None if times else '空表')
    return data


def validate_data():
    manifest = json.loads((ROOT / 'DATA_MANIFEST.json').read_text())
    assert manifest['source_run_id'] == RUN
    assert manifest['overall_p0'] == 'PARTIAL_BLOCKED_FOR_ASOF'
    assert manifest['suitable_for_professional_asof_resume'] is False
    assert manifest['symbols'] == ['rb', 'hc', 'i'] and manifest['frequency'] == '30m'
    assert manifest['algorithm_regeneration']['performed'] is False
    formal_expected = {'rb': {'big': 2, 'mid': 18}, 'hc': {'big': 1, 'mid': 16}, 'i': {'big': 12, 'mid': 47}}
    prefix_expected = {'rb': {'big': 14, 'mid': 112}, 'hc': {'big': 20, 'mid': 109}, 'i': {'big': 45, 'mid': 224}}
    result = {'schema': 'independent-package-check/v1', 'byte_gate': 'PASS',
              'asof_semantic_gate': 'BLOCKED', 'market_rows': {}, 'object_rows': {},
              'time_conflicts': {}, 'future_events_in_formal_actual_position_slice': [],
              'checks': ['完整文件集合', '逐文件hash/bytes/CSV行数/首末时间', '精确五字段',
                         '三品种30m和窗口', '原正式行情与warmup导出重叠逐值相符',
                         '每个整理对象actual/confirm位置及价格精确连接',
                         '缺方向/revision保留未知', '原切片未来event边界单列', '无小尺度数据或算法重算']}
    total_objects = 0
    for sym in ['rb', 'hc', 'i']:
        _, bars = table(ROOT / f'regenerated/market/{sym}_30m_warmup_through_20210930.csv')
        assert len(bars) == 2160
        assert all(r['symbol'] == sym and r['closeTs'] < '2021-10-01' for r in bars)
        assert bars[0]['closeTs'] == '2021-01-04 09:30:00'
        assert bars[-1]['closeTs'] == '2021-09-30 15:00:00'
        assert sum(r['closeTs'] >= '2021-08-15' for r in bars) == 376
        by_uti = {r['closeUti']: r for r in bars}
        assert len(by_uti) == len(bars)
        _, formal_market = table(ROOT / f'copied/formal_slices/{sym}/gtqh_kline_30m.csv')
        assert len(formal_market) == 368
        for r in formal_market:
            original = by_uti[r['closeUti']]
            for k in ['open', 'high', 'low', 'close', 'volume', 'openInt', 'openUti', 'closeUti', 'openTs', 'closeTs']:
                assert original[k] == r[k], (sym, k)
        _, mappings = table(ROOT / f'regenerated/time/{sym}_bar_calendar_mapping.csv')
        assert len(mappings) == len(bars)
        conflicts = [r for r in mappings if r['calendar_close_time'] != r['closeTs']]
        assert len(conflicts) == 182
        result['time_conflicts'][sym] = {'warmup_and_window': len(conflicts),
            'observation_window': sum(r['closeTs'] >= '2021-08-15' for r in conflicts)}
        result['market_rows'][sym] = {'with_warmup': len(bars), 'formal': len(formal_market), 'complete_observation': 376}
        for role in ['big', 'mid']:
            _, objects = table(ROOT / f'regenerated/objects/{sym}_{role}_events_through_20210930.csv')
            assert len(objects) == prefix_expected[sym][role]
            total_objects += len(objects)
            sources = {}
            for r in objects:
                assert r['event_ts'] < '2021-10-01' and r['symbol'] == sym and r['scale'] == role
                assert not r['direction'] and not r['revision'] and not r['object_id']
                assert r['current_status'] == 'PRESENT_IN_FROZEN_EXPORT_ASOF_NOT_VALIDATED'
                assert int(r['source_row']) >= 2
                assert r['source_key'].endswith(':csv_line:' + r['source_row'])
                for x, y in [('x', 'y'), ('xConfirm', 'yConfirm')]:
                    assert r[x] in by_uti
                    b = by_uti[r[x]]
                    assert float(r[y]) == float(b['close'])
                    assert r[x + '_bar_close_time'] == b['closeTs']
                key = (r['source_csv_sha256'], r['source_row'])
                assert key not in sources
                sources[key] = r
            _, formal_objects = table(ROOT / f'copied/formal_slices/{sym}/gtqh_E_{role}.csv')
            assert len(formal_objects) == formal_expected[sym][role]
            for r in formal_objects:
                if r['event_ts'] >= '2021-10-01':
                    result['future_events_in_formal_actual_position_slice'].append({
                        'symbol': sym, 'scale': role, 'source_row': r['_csv_source_row'],
                        'event_ts': r['event_ts'], 'x': r['x'], 'xConfirm': r['xConfirm'],
                        'original_actual_time': r['x_ts'], 'original_confirm_time': r['xConfirm_ts']})
                    continue
                o = sources[(r['_csv_source_sha256'], r['_csv_source_row'])]
                for k in ['event_ts', 'x', 'y', 'xConfirm', 'yConfirm', 'turn_round']:
                    assert o[k] == r[k], (sym, role, k)
            result['object_rows'][sym + '/' + role] = {'prefix': len(objects), 'formal': len(formal_objects)}
    assert total_objects == 524
    assert len(result['future_events_in_formal_actual_position_slice']) == 1
    assert not list((ROOT / 'copied/formal_slices').rglob('*small*'))
    _, conflicts = table(ROOT / 'evidence/TIME_MAPPING_CONFLICTS.csv')
    assert len(conflicts) == 546
    result['total_prefix_objects'] = total_objects
    result['total_time_conflicts'] = len(conflicts)
    report = ROOT / 'FULL_RESPONSE.md'
    if report.exists():
        lines = report.read_text().splitlines()
        for i, (key, value) in enumerate(HEADER.items()):
            assert lines[i] == key + ': ' + value
    return result


def seal():
    now = datetime.now(timezone.utc).isoformat()
    result = validate_data()
    (ROOT / 'evidence/INDEPENDENT_VALIDATION.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    provenance = json.loads((ROOT / 'evidence/PROVENANCE.json').read_text())
    files = []
    for p in inventory():
        rel = p.relative_to(ROOT).as_posix()
        if rel in OUTER:
            continue
        source = provenance.get(rel, {'source_path': '本工单原单与已封装证据；Worker工程整理',
                                     'copied_or_regenerated': 'regenerated',
                                     'generation_kind': 'documentation_or_package_validation'})
        if source['copied_or_regenerated'] == 'copied':
            assert sha(p) == source['source_sha256']
        files.append({'path': rel, **source, **metadata(p), 'generated_at': now,
                      'generated_at_semantics': '本次包封装时间；原计算时间如有见source/log，不以mtime冒充',
                      'tool': 'recover_inputs.py + package_receipt.py',
                      'version': {'recover_script_sha256': sha(ROOT / 'scripts/recover_inputs.py'),
                                  'receipt_script_sha256': sha(Path(__file__))},
                      'source_run_id': RUN,
                      'verification_status': 'BYTE_AND_STRUCTURE_VERIFIED_SEMANTICS_PARTIAL'})
    receipt = {'schema': 'bi01-input-recovery-receipt/v1', **HEADER,
               'generated_at': now, 'source_run_id': RUN,
               'overall_p0': 'PARTIAL_BLOCKED_FOR_ASOF',
               'self_reference_exclusion': {'paths': sorted(OUTER),
                   'reason': 'receipt由外层SHA256SUMS封口；SHA256SUMS自身由Git blob/commit封口'},
               'file_count': len(files), 'total_bytes_excluding_envelope': sum(f['bytes'] for f in files),
               'copied_file_count': sum(f['copied_or_regenerated'] == 'copied' for f in files),
               'regenerated_file_count': sum(f['copied_or_regenerated'] == 'regenerated' for f in files),
               'algorithm_regeneration_count': 0, 'files': files}
    (ROOT / 'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    entries = [f'{sha(p)}  {p.relative_to(ROOT).as_posix()}' for p in inventory() if p.name != 'SHA256SUMS']
    (ROOT / 'SHA256SUMS').write_text('\n'.join(entries) + '\n')


def verify():
    receipt = json.loads((ROOT / 'PACKAGE_RECEIPT.json').read_text())
    assert {k: receipt[k] for k in HEADER} == HEADER
    actual = {p.relative_to(ROOT).as_posix(): p for p in inventory()}
    expected = {f['path'] for f in receipt['files']}
    assert len(expected) == len(receipt['files']) == receipt['file_count']
    assert expected | OUTER == set(actual), (set(actual) - expected - OUTER, expected - set(actual))
    for record in receipt['files']:
        rel = record['path']
        assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
        observed = metadata(actual[rel])
        for k, v in observed.items():
            assert record[k] == v, (rel, k)
    sums = {}
    for line in (ROOT / 'SHA256SUMS').read_text().splitlines():
        checksum, rel = line.split('  ', 1)
        assert rel not in sums
        sums[rel] = checksum
    assert set(sums) == set(actual) - {'SHA256SUMS'}
    for rel, checksum in sums.items():
        assert sha(actual[rel]) == checksum, rel
    assert validate_data() == json.loads((ROOT / 'evidence/INDEPENDENT_VALIDATION.json').read_text())
    print(json.dumps({'result': 'PASS_BYTE_AND_STRUCTURE_GATE', 'p0': 'PARTIAL_BLOCKED_FOR_ASOF',
                      'files_verified': receipt['file_count'], 'outer_files_verified': len(sums),
                      'copied': receipt['copied_file_count'], 'regenerated': receipt['regenerated_file_count'],
                      'algorithm_runs': 0, 'source_disk_required': False}, ensure_ascii=False))


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in ['seal', 'verify']
    if sys.argv[1] == 'seal':
        seal()
    verify()
