"""同一冻结 GTQH 行情的确定性尾部运输。只解码 DBA，不导入或运行特征引擎。"""
import csv
import hashlib
import json
import math
import os
import platform
import struct
import sys
import time
import traceback
from datetime import datetime, timedelta, timezone
from fractions import Fraction
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
DATA = Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208')
SOURCE = Path('/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101')
SYMBOLS = ('rb', 'hc', 'i')
T = '2021-09-30 15:00:00'
END = '2021-10-15 15:00:00'
EPOCH = datetime(1970, 1, 1)
IDENTITY = {'source_snapshot': 'GTQH_L1_20210104_20240208',
            'source_run_id': 'GTQH_C001_three_turns_20261101_162005',
            'replay_run_id': 'BI01CO04_ASOF_REPLAY_20261101T203232Z_f4a75f64'}
opened = []


def audit(event, args):
    if event in ('subprocess.Popen', 'os.system', 'os.exec', 'os.posix_spawn', 'ctypes.dlopen'):
        raise RuntimeError('本行情运输脚本不允许进程/动态引擎调用: ' + event)
    if event == 'open':
        path, mode, flags = args
        if isinstance(path, (str, bytes, os.PathLike)):
            p = Path(os.fsdecode(path)).absolute()
            if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
                if not p.resolve().is_relative_to(OUT):
                    raise RuntimeError('写入越过唯一输出目录: ' + str(p))
            elif p.is_relative_to(DATA) or p.is_relative_to(SOURCE):
                opened.append(str(p))


sys.addaudithook(audit)


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(b):
    return hashlib.sha256(b).hexdigest()


def read_json(rel):
    return json.loads((OUT / rel).read_text())


def save(rel, obj):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def stat(p):
    s = p.stat()
    return {'resolved_path': str(p.resolve()), 'device': s.st_dev, 'inode': s.st_ino,
            'bytes': s.st_size, 'mtime_ns': s.st_mtime_ns, 'ctime_ns': s.st_ctime_ns}


def ns(text):
    d = datetime.fromisoformat(text) - EPOCH
    return (d.days * 86400 + d.seconds) * 10**9 + d.microseconds * 1000


def raw_time(n):
    seconds, nanos = divmod(n, 10**9)
    d = EPOCH + timedelta(seconds=seconds)
    return d.isoformat(sep=' ') + ('.' + f'{nanos:09d}'.rstrip('0') if nanos else '')


def business_time(n):
    return raw_time(n).replace(' ', 'T') + '+08:00'


def dba(b, dtype):
    assert len(b) >= 64
    version, offset, item_size, alignment = struct.unpack_from('<4I', b)
    n = struct.unpack_from('<q', b, 16)[0]
    assert (version, offset, item_size, alignment) == (0, 64, 8, 8)
    assert n >= 0 and len(b) >= 64 + 8 * n
    code = 'd' if dtype == 'f8' else 'q'
    return list(struct.unpack('<' + str(n) + code, b[64:64 + 8 * n]))


def logical_source_bytes(p):
    # 原PNV为预分配文件。只读取头部声明的有效行；容量尾部不是行情行。
    with p.open('rb') as f:
        header = f.read(64)
        assert len(header) == 64
        count = struct.unpack_from('<q', header, 16)[0]
        assert count == 8964
        payload = f.read(count * 8)
        assert len(payload) == count * 8
    return header + payload


def ratio(q):
    return {'value': float(q), 'exact_fraction': f'{q.numerator}/{q.denominator}'}


def fraction(value):
    return Fraction.from_float(float(value))


def run():
    assert sys.argv[1:] in ([], ['--repair-dba-capacity'])
    repair = bool(sys.argv[1:])
    if repair:
        assert read_json('logs/extraction-01.json')['returncode'] == 1
        failure = read_json('EXTRACTION_FAILURE.json')
        assert 'sv, v = dba(sb, dtype), dba(b, dtype)' in failure['traceback']
        assert not any((OUT / f'{s}_30m_tail.csv').exists() for s in SYMBOLS)
    marker = OUT / ('.runtime/extraction-repair-started.json' if repair else '.runtime/extraction-started.json')
    fd = os.open(marker, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    os.write(fd, (json.dumps({'started_at': now(), 'script_sha256': sha(Path(__file__).read_bytes())}) + '\n').encode())
    os.close(fd)
    freeze = read_json('inputs/DECISION_FREEZE.json')
    boundary = freeze['time_boundary']
    assert boundary['bar_cutoff'] == T.replace(' ', 'T') + '+08:00'
    assert boundary['future_evaluation_start_exclusive'] == boundary['bar_cutoff']
    assert boundary['future_evaluation_end_inclusive'] == END.replace(' ', 'T') + '+08:00'
    plan = freeze['future_evaluation_plan_frozen']
    assert plan['case_only_material_separation'] == 'absolute terminal return gap >= 5 percentage points OR absolute difference in minimum tail return >= 5 percentage points'
    assert freeze['target_process']['eligible_pair'] == ['rb', 'hc']
    prepared = read_json('inputs/prior_prepared_jobs.json')['inputs']
    prior = {v['path']: v for v in read_json('inputs/prior_SOURCE_INPUTS.json')}
    old_receipt = read_json('inputs/prior_PACKAGE_RECEIPT.json')['files']
    prefix = read_json('inputs/replay_PNV_PREFIX_ROUTE_RECEIPT.json')['files']
    cfg = read_json('inputs/prior_engine_source_config.json')
    assert cfg['pnv_dir'] == str(DATA / 'pnv')
    assert (cfg['opt_start_hour'], cfg['opt_end_hour']) == ('21:00:00', '20:00:00')
    source_records, symbol_checks, csv_stats, paths = [], {}, {}, {}
    from_ns, to_ns = ns(T), ns(END)
    save('SOURCE_IDENTITY_CHECK.json', {'status': 'STARTED', 'started_at': now(), **IDENTITY})
    for sym in SYMBOLS:
        item = next(x for x in prepared if x['symbol'] == sym)
        fields = item['fields']
        stage = Path(item['staged_kline_cache'])
        assert stage.is_relative_to(SOURCE / 'turn_staging/cache')
        assert '/GTQH_L1_20210104_20240208/fao/prod/KLine/' in str(stage)
        srcdir = DATA / 'pnv/30m' / sym
        actual_fields = sorted(p.name for p in srcdir.iterdir())
        assert actual_fields == sorted(k + '.dba' for k in fields)
        values, blobs, records = {}, {}, []
        for field, dtype in fields.items():
            sp = stage / (field + '.dba')
            dp = srcdir / (field + '.dba')
            stage_before, pnv_before = stat(sp), stat(dp)
            sb, b = sp.read_bytes(), logical_source_bytes(dp)
            expected = prior[str(sp)]
            assert len(sb) == expected['bytes'] and sha(sb) == expected['sha256'], str(sp)
            sv, v = dba(sb, dtype), dba(b, dtype)
            assert len(v) == len(sv) == item['rows'] == 8964
            assert b[64:] == sb[64:], (sym, field, '完整PNV与既有已核staging数值字节不一致')
            rec = next(x for x in prefix if x['source_path'] == str(dp))
            frozen_file = OUT / 'inputs/frozen_prefix/30m' / sym / (field + '.dba')
            frozen = frozen_file.read_bytes()
            assert sha(frozen) == rec['sha256']
            assert sha(frozen[64:]) == rec['payload_sha256']
            assert frozen[64:] == b[64:64 + 2160 * 8]
            assert dba(frozen, dtype) == v[:2160]
            record = {'symbol': sym, 'field': field, 'dtype': dtype, 'source_path': str(dp),
                      'source_stat_before': pnv_before, 'source_sha256_before': sha(b),
                      'source_bytes': pnv_before['bytes'], 'source_logical_bytes': len(b), 'source_rows': len(v),
                      'source_full_file_sha256': None,
                      'source_hash_scope': 'original header64 + all 8964 logical rows; preallocated capacity beyond logical length not hashed',
                      'source_header_hex': b[:64].hex(),
                      'staging_path': str(sp), 'staging_stat_before': stage_before,
                      'staging_sha256_before': sha(sb), 'prior_staging_sha256': expected['sha256'],
                      'full_payload_equals_verified_staging': True,
                      'frozen_prefix_path': str(frozen_file.relative_to(OUT)),
                      'frozen_prefix_sha256': rec['sha256'], 'frozen_prefix_rows': 2160,
                      'frozen_prefix_payload_equals_source': True}
            records.append(record)
            values[field], blobs[field] = v, b
        index_path = stage / '__ts__.dba'
        index_before = stat(index_path)
        index_blob = index_path.read_bytes()
        assert sha(index_blob) == prior[str(index_path)]['sha256']
        assert dba(index_blob, 'datetime64[ns]') == values['closeTs']
        timestamps = values['closeTs']
        assert all(a < b for a, b in zip(timestamps, timestamps[1:]))
        assert raw_time(timestamps[0]) == '2021-01-04 09:30:00'
        assert raw_time(timestamps[-1]) == '2024-02-08 15:00:00'
        anchors = [i for i, t in enumerate(timestamps) if t == from_ns]
        endpoints = [i for i, t in enumerate(timestamps) if t == to_ns]
        assert anchors == [2159], (sym, 'ANCHOR_MISSING_OR_NOT_UNIQUE', anchors)
        assert len(endpoints) == 1, (sym, 'ENDPOINT_MISSING_OR_NOT_UNIQUE', endpoints)
        indices = [i for i, t in enumerate(timestamps) if from_ns <= t <= to_ns]
        assert indices == list(range(anchors[0], endpoints[0] + 1))
        assert len(indices) > 1
        anchor = next(csv.DictReader((OUT / f'inputs/{sym}_prior_cutoff_row.csv').open()))
        old = next(r for r in old_receipt if r['path'] == f'regenerated/market/{sym}_30m_warmup_through_20210930.csv')
        assert old['source_path'] == str(stage) and old['rows'] == 2160
        assert anchor['source_row'] == '2159' and anchor['closeTs'] == T
        for field, dtype in fields.items():
            expected_value = ns(anchor[field]) if dtype.startswith('datetime') else float(anchor[field])
            assert values[field][2159] == expected_value, (sym, field, 'anchor mismatch')
        for field, b in blobs.items():
            rel = f'evidence/source_ranges/{sym}/{field}.bin'
            data = b[64 + indices[0] * 8:64 + (indices[-1] + 1) * 8]
            dest = OUT / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            record = next(r for r in records if r['field'] == field)
            record.update({'range_path': rel, 'range_sha256': sha(data), 'range_bytes': len(data),
                           'range_source_row_first': indices[0], 'range_source_row_last': indices[-1],
                           'range_rows': len(indices), 'source_byte_start': 64 + indices[0] * 8,
                           'source_byte_end_exclusive': 64 + (indices[-1] + 1) * 8})
        columns = ['symbol', 'frequency', 'business_timestamp', 'closeTs', 'closeTs_raw_ns',
                   'close', 'closeUti', 'open', 'high', 'low', 'volume', 'openInt',
                   'openTs', 'openTs_raw_ns', 'openUti', 'source_index_ts', 'source_row',
                   'source_key', 'source_series_path', 'source_snapshot', 'timezone',
                   'contract_id', 'continuous_series_id', 'adjustment_id', 'trading_day',
                   'session', 'night_session_attribution', 'row_role']
        output_path = OUT / f'{sym}_30m_tail.csv'
        rows = []
        for i in indices:
            assert all(math.isfinite(values[f][i]) for f, typ in fields.items() if typ == 'f8')
            assert values['close'][i] > 0
            row = {f: values[f][i] for f in fields}
            row.update(symbol=sym, frequency='30m', business_timestamp=business_time(timestamps[i]),
                       closeTs=raw_time(timestamps[i]), closeTs_raw_ns=timestamps[i],
                       openTs=raw_time(values['openTs'][i]), openTs_raw_ns=values['openTs'][i],
                       source_index_ts=raw_time(timestamps[i]), source_row=i,
                       source_key=f'{srcdir}:row:{i}', source_series_path=str(srcdir),
                       source_snapshot=IDENTITY['source_snapshot'], timezone='Asia/Shanghai',
                       contract_id='', continuous_series_id='', adjustment_id='', trading_day='',
                       session='', night_session_attribution='',
                       row_role='CUTOFF_ANCHOR' if i == 2159 else 'EVALUATION_TAIL')
            rows.append(row)
        with output_path.open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=columns, lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
        for record in records:
            dp, sp = Path(record['source_path']), Path(record['staging_path'])
            record['source_sha256_after'] = sha(logical_source_bytes(dp))
            record['source_stat_after'] = stat(dp)
            record['staging_sha256_after'] = sha(sp.read_bytes())
            record['staging_stat_after'] = stat(sp)
            assert record['source_sha256_after'] == record['source_sha256_before']
            assert record['source_stat_before'] == record['source_stat_after']
            assert record['staging_sha256_after'] == record['staging_sha256_before']
            assert record['staging_stat_before'] == record['staging_stat_after']
        assert sha(index_path.read_bytes()) == prior[str(index_path)]['sha256']
        assert index_before == stat(index_path)
        source_records.extend(records)
        symbol_checks[sym] = {'status': 'MATCH', 'anchor_source_row': 2159,
                             'anchor_timestamp': business_time(from_ns), 'anchor_close': values['close'][2159],
                             'anchor_closeUti': values['closeUti'][2159], 'prior_market_sha256': old['sha256'],
                             'pnv_full_payload_equals_prior_verified_staging': True,
                             'all_ten_fields_frozen_prefix_match': True,
                             'source_field_names': actual_fields,
                             'staging_index_path': str(index_path), 'staging_index_sha256': sha(index_blob),
                             'staging_index_equals_closeTs': True,
                             'source_input_rows': 8964, 'source_input_first': raw_time(timestamps[0]),
                             'source_input_last': raw_time(timestamps[-1]),
                             'source_rows_selected': [indices[0], indices[-1]],
                             'range_is_all_source_rows_matching_fixed_interval': True}
        csv_stats[sym] = {'path': output_path.name, 'rows': len(rows), 'anchor_rows': 1,
                          'tail_rows': len(rows) - 1, 'first_timestamp': rows[0]['business_timestamp'],
                          'last_timestamp': rows[-1]['business_timestamp'],
                          'anchor_close': rows[0]['close'], 'anchor_closeUti': rows[0]['closeUti'],
                          'tail_first_timestamp': rows[1]['business_timestamp'],
                          'tail_first_close': rows[1]['close'], 'tail_last_close': rows[-1]['close'],
                          'endpoint_status': 'EXACT_ENDPOINT_PRESENT'}
        paths[sym] = {r['business_timestamp']: fraction(r['close']) / fraction(rows[0]['close']) - 1 for r in rows[1:]}
        print(json.dumps({'symbol': sym, **csv_stats[sym]}, ensure_ascii=False), flush=True)
        save('SOURCE_IDENTITY_CHECK.json', {'status': 'IN_PROGRESS', **IDENTITY,
             'symbols': symbol_checks, 'files': source_records})
    common = sorted(set.intersection(*(set(paths[s]) for s in SYMBOLS)))
    differences = {s: sorted(set(paths[s]) - set(common)) for s in SYMBOLS}
    pair_common = sorted(set(paths['rb']) & set(paths['hc']))
    terminal = END.replace(' ', 'T') + '+08:00'
    per_symbol = {s: {'terminal_return_s': ratio(paths[s][terminal]),
                      'minimum_tail_return_s': ratio(min(paths[s].values())),
                      'maximum_tail_return_s': ratio(max(paths[s].values())),
                      'minimum_timestamps': [t for t, r in paths[s].items() if r == min(paths[s].values())],
                      'maximum_timestamps': [t for t, r in paths[s].items() if r == max(paths[s].values())],
                      'role': 'DIAGNOSTIC_ONLY' if s == 'i' else 'FROZEN_PAIR_MEMBER'} for s in SYMBOLS}
    gap = paths['rb'][terminal] - paths['hc'][terminal]
    min_diff = min(paths['rb'].values()) - min(paths['hc'].values())
    save('TAIL_MECHANICAL_METRICS.json', {'schema': 'frozen-tail-mechanical-metrics/v1',
         'formula': 'r_s(t) = close_s(t) / C_s(T) - 1; minimum and maximum exclude anchor',
         'arithmetic': 'exact rational arithmetic on decoded IEEE754 input prices; numeric value is float(exact_fraction)',
         'cutoff': T.replace(' ', 'T') + '+08:00', 'endpoint': terminal,
         'per_symbol': per_symbol,
         'rb_minus_hc_path': [{'business_timestamp': t, 'r_rb': ratio(paths['rb'][t]),
                              'r_hc': ratio(paths['hc'][t]),
                              'rb_minus_hc_path': ratio(paths['rb'][t] - paths['hc'][t])} for t in pair_common],
         'terminal_gap': ratio(gap), 'minimum_return_difference': ratio(min_diff),
         'frozen_case_only_test': {'threshold': 0.05, 'threshold_exact_fraction': '1/20',
             'abs_terminal_gap_gte_0_05': abs(gap) >= Fraction(1, 20),
             'abs_minimum_return_difference_gte_0_05': abs(min_diff) >= Fraction(1, 20),
             'boolean_or': abs(gap) >= Fraction(1, 20) or abs(min_diff) >= Fraction(1, 20),
             'eligible_pair': ['rb', 'hc'], 'i_enters_test': False},
         'business_interpretation': 'NOT_PERFORMED_WORKER_TRANSPORT_ONLY'})
    alignment = {'all_three_timestamp_sets_equal': all(set(paths[s]) == set(common) for s in SYMBOLS),
                 'evaluation_common_timestamp_count': len(common), 'evaluation_common_timestamps': common,
                 'per_symbol_timestamps_outside_common': differences,
                 'rb_hc_common_timestamp_count': len(pair_common), 'interpolation': False}
    save('SOURCE_IDENTITY_CHECK.json', {'status': 'MATCH', **IDENTITY, 'files': source_records,
         'symbols': symbol_checks, 'timestamp_alignment': alignment,
         'calendar_contract': 'PNV closeTs naive business text interpreted as Asia/Shanghai, identical to frozen prefix; same closeUti and staging __ts__ route',
         'missing_source_fields': ['contract_id', 'continuous_series_id', 'adjustment_id', 'trading_day', 'session', 'night_session_attribution'],
         'missing_fields_policy': 'source does not expose these per-row fields; blank preserved, not inferred or filled from another source',
         'session_configuration': {'opt_start_hour': '21:00:00', 'opt_end_hour': '20:00:00'},
         'source_opened_paths': sorted(set(opened)), 'feature_engine_calls': 0, 'finished_at': now()})
    save('TAIL_MANIFEST.json', {'schema': 'frozen-tail-transport/v1',
         'order_id': 'BI01CO04-FROZEN-TAIL-TRANSPORT-01', 'work_id': 'BI-01', 'run_id': 'BI-01-CO-04',
         'exit': 'TAIL_PACKAGE_READY', **IDENTITY, 'symbols': list(SYMBOLS), 'frequency': '30m',
         'cutoff': T.replace(' ', 'T') + '+08:00', 'endpoint': terminal,
         'selection_rule': 'source closeTs >= cutoff and <= endpoint; anchor exactly == cutoff; tail strictly > cutoff',
         'timezone': 'Asia/Shanghai', 'source_version_policy': 'same GTQH snapshot with full numeric payload equal to prior SHA256-verified staging; no replacement source',
         'outputs': csv_stats, 'timestamp_alignment': alignment,
         'source_identity_check': 'SOURCE_IDENTITY_CHECK.json', 'metrics': 'TAIL_MECHANICAL_METRICS.json',
         'extraction_attempts': 2 if repair else 1,
         'correction': 'same-script DBA logical length versus preallocated capacity fix' if repair else None,
         'feature_engine_calls': 0, 'interpolation': False,
         'frozen_decision_modified': False, 'professional_automatically_continued': False,
         'tool': {'name': 'extract_tail.py', 'python': platform.python_version(),
                  'script_sha256': sha(Path(__file__).read_bytes())}, 'finished_at': now()})


if __name__ == '__main__':
    started, start = now(), time.monotonic()
    try:
        run()
    except Exception as exc:
        save('EXTRACTION_REPAIR_FAILURE.json' if sys.argv[1:] else 'EXTRACTION_FAILURE.json', {'started_at': started, 'failed_at': now(),
             'elapsed_seconds': time.monotonic() - start, 'error': repr(exc),
             'traceback': traceback.format_exc(), 'source_opened_paths': sorted(set(opened)),
             'feature_engine_calls': 0})
        traceback.print_exc()
        sys.exit(1)
