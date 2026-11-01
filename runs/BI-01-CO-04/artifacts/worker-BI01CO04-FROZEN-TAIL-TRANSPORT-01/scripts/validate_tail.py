"""独立消费者校验；不导入提取器，不运行引擎。默认离线，--live-source 复读确切原源。"""
import argparse
import array
import ast
import csv
import hashlib
import json
import math
import sys
from datetime import datetime, timedelta
from fractions import Fraction
from pathlib import Path

SYMS = ['rb', 'hc', 'i']
FIELDS = {'close': 'd', 'closeTs': 'q', 'closeUti': 'q', 'high': 'd', 'low': 'd',
          'open': 'd', 'openInt': 'd', 'openTs': 'q', 'openUti': 'q', 'volume': 'd'}
T = '2021-09-30T15:00:00+08:00'
END = '2021-10-15T15:00:00+08:00'
DATA = Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208')
STAGE = Path('/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101/turn_staging/cache/BaseData/futures/GTQH_L1_20210104_20240208/fao/prod/KLine/e/c/3/e/0/2/3/0a9cc80a32b85890741475ee0505af8dc')


def digest(b):
    return hashlib.sha256(b).hexdigest()


def decode(payload, kind):
    a = array.array(kind)
    a.frombytes(payload)
    if sys.byteorder != 'little':
        a.byteswap()
    return list(a)


def header_count(b):
    assert len(b) >= 64
    words = [int.from_bytes(b[i:i + 4], 'little') for i in range(0, 16, 4)]
    assert words == [0, 64, 8, 8], words
    n = int.from_bytes(b[16:24], 'little', signed=True)
    assert n >= 0
    return n


def time_ns(t):
    d = datetime.fromisoformat(t).replace(tzinfo=None) - datetime(1970, 1, 1)
    return ((d.days * 86400 + d.seconds) * 1000000 + d.microseconds) * 1000


def fraction(d):
    return Fraction(*float(d).as_integer_ratio())


def check_ratio(actual, expected):
    assert Fraction(actual['exact_fraction']) == expected
    assert actual['value'] == float(expected)


def csv_meta(path):
    with path.open(newline='') as f:
        rows = list(csv.DictReader(f))
    if rows:
        field = next((s for s in ['business_timestamp', 'closeTs', 'bar_cutoff_asia_shanghai'] if s in rows[0]), None)
        times = [r[field] for r in rows] if field else []
        return len(rows), min(times) if times else None, max(times) if times else None
    return 0, None, None


def validate(root, live=False, data_only=False):
    def j(p):
        return json.loads((root / p).read_text())
    manifest, identity, metrics = j('TAIL_MANIFEST.json'), j('SOURCE_IDENTITY_CHECK.json'), j('TAIL_MECHANICAL_METRICS.json')
    freeze, contract = j('inputs/DECISION_FREEZE.json'), j('EXTRACTION_CONTRACT.json')
    assert manifest['exit'] == 'TAIL_PACKAGE_READY'
    assert manifest['symbols'] == SYMS and manifest['frequency'] == '30m'
    assert manifest['cutoff'] == contract['cutoff'] == freeze['time_boundary']['bar_cutoff'] == T
    assert manifest['endpoint'] == contract['endpoint'] == freeze['time_boundary']['future_evaluation_end_inclusive'] == END
    assert freeze['time_boundary']['future_evaluation_start_exclusive'] == T
    assert freeze['target_process']['eligible_pair'] == ['rb', 'hc']
    assert freeze['future_evaluation_plan_frozen']['case_only_material_separation'] == 'absolute terminal return gap >= 5 percentage points OR absolute difference in minimum tail return >= 5 percentage points'
    assert freeze['artifact_hashes']['TIME_CONTRACT.md_sha256'] == digest((root / 'inputs/replay_TIME_CONTRACT.md').read_bytes())
    assert freeze['artifact_hashes']['QUERY_SNAPSHOT_STATE_TABLE.csv_sha256'] == digest((root / 'inputs/QUERY_SNAPSHOT_STATE_TABLE.csv').read_bytes())
    assert manifest['extraction_attempts'] == 2 and manifest['feature_engine_calls'] == identity['feature_engine_calls'] == 0
    assert identity['status'] == 'MATCH' and not manifest['interpolation']
    assert manifest['source_snapshot'] == identity['source_snapshot'] == 'GTQH_L1_20210104_20240208'
    assert manifest['source_run_id'] == identity['source_run_id'] == 'GTQH_C001_three_turns_20261101_162005'
    assert manifest['replay_run_id'] == identity['replay_run_id'] == freeze['replay_run_id']
    assert manifest['timezone'] == 'Asia/Shanghai'
    reads = j('REQUIRED_READS.json')
    assert {r['required_item'] for r in reads if 'required_item' in r} == set(range(1, 9))
    for r in reads:
        b = (root / r['snapshot_path']).read_bytes()
        assert len(b) == r['bytes'] and digest(b) == r['sha256']
    old_receipt = j('inputs/prior_PACKAGE_RECEIPT.json')['files']
    baseline = {r['path']: r for r in j('inputs/prior_SOURCE_INPUTS.json')}
    prefix_receipt = j('inputs/replay_PNV_PREFIX_ROUTE_RECEIPT.json')['files']
    source_snapshot = j('inputs/replay_SOURCE_SNAPSHOT.json')['files']
    cfg = j('inputs/prior_engine_source_config.json')
    assert cfg['pnv_dir'] == str(DATA / 'pnv')
    assert identity['session_configuration'] == {'opt_start_hour': cfg['opt_start_hour'], 'opt_end_hour': cfg['opt_end_hour']}
    assert identity['session_configuration'] == {'opt_start_hour': '21:00:00', 'opt_end_hour': '20:00:00'}
    assert len(identity['files']) == 30
    assert {(r['symbol'], r['field']) for r in identity['files']} == {(s, f) for s in SYMS for f in FIELDS}
    all_rows, returns, live_files = {}, {}, 0
    for s in SYMS:
        with (root / f'{s}_30m_tail.csv').open(newline='') as f:
            rows = list(csv.DictReader(f))
        assert len(rows) > 1
        times = [r['business_timestamp'] for r in rows]
        assert all(a < b for a, b in zip(times, times[1:]))
        assert times[0] == T and times[-1] == END
        assert len(set(times)) == len(times)
        assert sum(r['row_role'] == 'CUTOFF_ANCHOR' for r in rows) == 1
        assert rows[0]['row_role'] == 'CUTOFF_ANCHOR'
        assert all(r['row_role'] == 'EVALUATION_TAIL' and T < r['business_timestamp'] <= END for r in rows[1:])
        assert [int(r['source_row']) for r in rows] == list(range(2159, 2159 + len(rows)))
        stats = manifest['outputs'][s]
        for key, value in {'rows': len(rows), 'anchor_rows': 1, 'tail_rows': len(rows) - 1,
                           'first_timestamp': times[0], 'last_timestamp': times[-1],
                           'anchor_close': float(rows[0]['close']), 'anchor_closeUti': int(rows[0]['closeUti']),
                           'tail_first_timestamp': times[1], 'tail_first_close': float(rows[1]['close']),
                           'tail_last_close': float(rows[-1]['close']), 'endpoint_status': 'EXACT_ENDPOINT_PRESENT'}.items():
            assert stats[key] == value, (s, key)
        for row in rows:
            assert row['symbol'] == s and row['frequency'] == '30m' and row['timezone'] == 'Asia/Shanghai'
            assert row['source_snapshot'] == identity['source_snapshot']
            assert row['business_timestamp'] == row['closeTs'].replace(' ', 'T') + '+08:00'
            assert int(row['closeTs_raw_ns']) == time_ns(row['business_timestamp'])
            assert row['source_index_ts'] == row['closeTs']
            assert row['source_series_path'] == str(DATA / 'pnv/30m' / s)
            assert row['source_key'] == row['source_series_path'] + ':row:' + row['source_row']
            assert all(row[k] == '' for k in identity['missing_source_fields'])
            assert all(math.isfinite(float(row[k])) for k, typ in FIELDS.items() if typ == 'd')
            assert float(row['close']) > 0
        original = next(csv.DictReader((root / f'inputs/{s}_prior_cutoff_row.csv').open()))
        old = next(r for r in old_receipt if r['path'] == f'regenerated/market/{s}_30m_warmup_through_20210930.csv')
        ref = next(r for r in reads if r.get('snapshot_path') == f'inputs/{s}_prior_cutoff_row.csv')
        assert ref['source_sha256'] == old['sha256'] == identity['symbols'][s]['prior_market_sha256']
        assert original['source_row'] == rows[0]['source_row'] == '2159'
        assert original['source_key'] == str(STAGE / s) + ':__ts__:2159'
        for f, kind in FIELDS.items():
            rec = next(r for r in identity['files'] if r['symbol'] == s and r['field'] == f)
            expected_source = DATA / 'pnv/30m' / s / (f + '.dba')
            expected_stage = STAGE / s / (f + '.dba')
            assert rec['source_path'] == str(expected_source) and rec['staging_path'] == str(expected_stage)
            assert rec['source_rows'] == 8964 and rec['source_full_file_sha256'] is None
            assert rec['source_logical_bytes'] == 64 + 8 * 8964
            assert rec['source_sha256_before'] == rec['source_sha256_after']
            assert rec['source_stat_before'] == rec['source_stat_after']
            assert rec['staging_stat_before'] == rec['staging_stat_after']
            assert rec['staging_sha256_before'] == rec['staging_sha256_after'] == baseline[str(expected_stage)]['sha256']
            assert rec['full_payload_equals_verified_staging'] and rec['frozen_prefix_payload_equals_source']
            prefix = (root / rec['frozen_prefix_path']).read_bytes()
            pp = next(r for r in prefix_receipt if r['source_path'] == str(expected_source))
            fs = next(r for r in source_snapshot if r['source_path'] == str(expected_stage))
            assert digest(prefix) == pp['sha256'] == rec['frozen_prefix_sha256'] == fs['sha256']
            assert header_count(prefix) == 2160 and len(prefix) == 64 + 2160 * 8
            assert digest(prefix[64:]) == pp['payload_sha256'] == fs['payload_sha256']
            payload = (root / rec['range_path']).read_bytes()
            assert digest(payload) == rec['range_sha256'] and len(payload) == len(rows) * 8 == rec['range_bytes']
            assert rec['range_rows'] == len(rows) and rec['range_source_row_first'] == 2159
            assert rec['range_source_row_last'] == 2158 + len(rows)
            assert rec['source_byte_start'] == 64 + 8 * 2159
            assert rec['source_byte_end_exclusive'] == 64 + 8 * (2159 + len(rows))
            decoded = decode(payload, kind)
            old_anchor = time_ns(original[f]) if f.endswith('Ts') else float(original[f])
            assert decoded[0] == decode(prefix[-8:], kind)[0] == old_anchor
            column = f + '_raw_ns' if f.endswith('Ts') else f
            cv = [int(r[column]) if kind == 'q' else float(r[column]) for r in rows]
            assert decoded == cv, (s, f, 'raw range versus CSV')
            if live:
                with expected_source.open('rb') as h:
                    head = h.read(64)
                    n = header_count(head)
                    logical = h.read(8 * n)
                assert n == 8964 and digest(head + logical) == rec['source_sha256_before']
                assert expected_source.stat().st_size == rec['source_bytes']
                stage_bytes = expected_stage.read_bytes()
                assert digest(stage_bytes) == baseline[str(expected_stage)]['sha256']
                assert logical == stage_bytes[64:64 + 8 * n]
                assert payload == logical[2159 * 8:(2159 + len(rows)) * 8]
                if f == 'closeTs':
                    full = decode(logical, 'q')
                    selected = [i for i, ts in enumerate(full) if time_ns(T) <= ts <= time_ns(END)]
                    assert selected == [int(r['source_row']) for r in rows]
                live_files += 2
        if live:
            ip = STAGE / s / '__ts__.dba'
            assert digest(ip.read_bytes()) == baseline[str(ip)]['sha256']
            assert ip.read_bytes()[64:] == (STAGE / s / 'closeTs.dba').read_bytes()[64:]
            live_files += 1
        all_rows[s] = rows
        anchor = fraction(rows[0]['close'])
        returns[s] = {r['business_timestamp']: (fraction(r['close']) - anchor) / anchor for r in rows[1:]}
        expected_stats = [returns[s][END], min(returns[s].values()), max(returns[s].values())]
        for key, value in zip(['terminal_return_s', 'minimum_tail_return_s', 'maximum_tail_return_s'], expected_stats):
            check_ratio(metrics['per_symbol'][s][key], value)
        assert metrics['per_symbol'][s]['minimum_timestamps'] == [t for t, v in returns[s].items() if v == expected_stats[1]]
        assert metrics['per_symbol'][s]['maximum_timestamps'] == [t for t, v in returns[s].items() if v == expected_stats[2]]
    common = sorted(set(returns['rb']) & set(returns['hc']) & set(returns['i']))
    aligned = manifest['timestamp_alignment']
    assert aligned == identity['timestamp_alignment']
    assert aligned['evaluation_common_timestamps'] == common
    assert aligned['evaluation_common_timestamp_count'] == len(common)
    assert aligned['per_symbol_timestamps_outside_common'] == {s: sorted(set(returns[s]) - set(common)) for s in SYMS}
    assert aligned['all_three_timestamp_sets_equal'] == all(set(returns[s]) == set(common) for s in SYMS)
    pair = sorted(set(returns['rb']) & set(returns['hc']))
    assert [v['business_timestamp'] for v in metrics['rb_minus_hc_path']] == pair
    for item in metrics['rb_minus_hc_path']:
        t = item['business_timestamp']
        check_ratio(item['r_rb'], returns['rb'][t])
        check_ratio(item['r_hc'], returns['hc'][t])
        check_ratio(item['rb_minus_hc_path'], returns['rb'][t] - returns['hc'][t])
    gap = returns['rb'][END] - returns['hc'][END]
    minimum = min(returns['rb'].values()) - min(returns['hc'].values())
    check_ratio(metrics['terminal_gap'], gap)
    check_ratio(metrics['minimum_return_difference'], minimum)
    test = metrics['frozen_case_only_test']
    assert test == {'threshold': 0.05, 'threshold_exact_fraction': '1/20',
                    'abs_terminal_gap_gte_0_05': abs(gap) >= Fraction(1, 20),
                    'abs_minimum_return_difference_gte_0_05': abs(minimum) >= Fraction(1, 20),
                    'boolean_or': abs(gap) >= Fraction(1, 20) or abs(minimum) >= Fraction(1, 20),
                    'eligible_pair': ['rb', 'hc'], 'i_enters_test': False}
    assert metrics['per_symbol']['i']['role'] == 'DIAGNOSTIC_ONLY'
    code = (root / 'scripts/extract_tail.py').read_bytes()
    assert digest(code) == manifest['tool']['script_sha256'] == j('DBA_LAYOUT_CORRECTION.json')['corrected_script_sha256']
    original_code = (root / 'diagnostics/extract_tail.attempt-01.py').read_bytes()
    assert digest(original_code) == contract['extraction_script_sha256'] == j('DBA_LAYOUT_CORRECTION.json')['original_script_sha256']
    imports = set()
    for n in ast.walk(ast.parse(code)):
        if isinstance(n, ast.Import):
            imports.update(a.name for a in n.names)
        elif isinstance(n, ast.ImportFrom):
            imports.add(n.module)
        elif isinstance(n, ast.Call):
            name = n.func.id if isinstance(n.func, ast.Name) else n.func.attr if isinstance(n.func, ast.Attribute) else ''
            assert name not in {'Popen', 'runRealTime', 'pushTick', 'pushTicks', 'system', 'exec', 'eval', '__import__', 'CDLL'}
    assert imports <= {'csv', 'hashlib', 'json', 'math', 'os', 'platform', 'struct', 'sys', 'time', 'traceback', 'datetime', 'fractions', 'pathlib'}
    expected_opens = {str(DATA / 'pnv/30m' / s / (f + '.dba')) for s in SYMS for f in FIELDS}
    expected_opens |= {str(STAGE / s / (f + '.dba')) for s in SYMS for f in [*FIELDS, '__ts__']}
    assert set(identity['source_opened_paths']) == expected_opens
    assert j('logs/extraction-01.json')['returncode'] == 1
    assert j('logs/extraction-02-same-script-repair.json')['returncode'] == 0
    checks = ['fixed_symbols_frequency_interval', 'unique_matching_anchor', 'strict_tail_and_exact_endpoint',
              'monotone_finite_closes', 'same_identity_and_explicit_calendar', 'raw_source_range_to_CSV_all_ten_fields',
              'frozen_formula_independent_exact_recalculation', 'source_allowlist_and_zero_feature_execution']
    files_checked = None
    if not data_only:
        receipt = j('TAIL_PACKAGE_RECEIPT.json')
        files = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.runtime' not in p.relative_to(root).parts}
        entries = {r['path']: r for r in receipt['files']}
        assert set(entries) == files - {'TAIL_PACKAGE_RECEIPT.json', 'SHA256SUMS'}
        for name, rec in entries.items():
            b = (root / name).read_bytes()
            assert digest(b) == rec['sha256'] and len(b) == rec['bytes'], name
            assert rec['source_path'] and rec['verification_status']
            if name.endswith('.csv'):
                count, first, last = csv_meta(root / name)
                assert (count, first, last) == (rec['rows'], rec['first_timestamp'], rec['last_timestamp']), name
            if name in [s + '_30m_tail.csv' for s in SYMS]:
                s = name.split('_', 1)[0]
                rows = all_rows[s]
                assert rec['anchor_close'] == float(rows[0]['close'])
                assert rec['tail_first_close'] == float(rows[1]['close'])
                assert rec['tail_last_close'] == float(rows[-1]['close'])
                assert set(rec['source_path']) == {r['source_path'] for r in identity['files'] if r['symbol'] == s}
            elif name.startswith('evidence/source_ranges/'):
                assert rec['rows'] == len(b) // 8
                assert rec['first_timestamp'] == T and rec['last_timestamp'] == END
            elif name.startswith('inputs/frozen_prefix/'):
                assert rec['rows'] == header_count(b) == 2160
                assert rec['first_timestamp'] == '2021-01-04T09:30:00+08:00'
                assert rec['last_timestamp'] == T
        seal = {}
        for line in (root / 'SHA256SUMS').read_text().splitlines():
            h, name = line.split('  ', 1)
            assert name not in seal
            seal[name] = h
        assert set(seal) == files - {'SHA256SUMS'}
        for name, h in seal.items():
            assert digest((root / name).read_bytes()) == h, name
        assert receipt['file_count_excluding_envelope'] == len(entries)
        assert receipt['bytes_excluding_envelope'] == sum(r['bytes'] for r in entries.values())
        files_checked = len(entries)
        checks.append('receipt_hash_bytes_rows_timestamps_and_complete_outer_seal')
    return {'status': 'PASS', 'exit': manifest['exit'], 'mode': 'DATA_ONLY' if data_only else 'SEALED_PACKAGE',
            'checks_passed': checks, 'rows': {s: len(all_rows[s]) for s in SYMS},
            'tail_rows': {s: len(returns[s]) for s in SYMS}, 'common_tail_timestamps': len(common),
            'all_ten_fields_compared': True, 'live_source_files_independently_read': live_files,
            'receipt_files_checked': files_checked, 'formula_values_and_exact_fractions_match': True,
            'feature_engine_calls': 0, 'frozen_decision_changed': False}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--live-source', action='store_true')
    p.add_argument('--data-only', action='store_true')
    a = p.parse_args()
    print(json.dumps(validate(a.root.resolve(), a.live_source, a.data_only), ensure_ascii=False))
