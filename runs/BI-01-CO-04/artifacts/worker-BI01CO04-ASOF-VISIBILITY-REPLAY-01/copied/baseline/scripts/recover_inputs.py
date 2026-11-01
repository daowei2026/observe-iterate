"""只读恢复现有运行；不导入模型运行时，不生成特征，不写源目录。"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import mmap
import os
import platform
import shutil
import subprocess

import numpy as np
import pandas as pd
from pydim import DbArray

OUT = Path(__file__).resolve().parents[1]
REPO = OUT.parents[3]
WORK = Path('/dwdhome/fy/BASE_E6_2')
SRC = WORK / 'mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101'
RUN_ID = 'GTQH_C001_three_turns_20261101_162005'
RUN = SRC / 'three_turn_plot' / RUN_ID
DATA = Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208')
SYMS = ['rb', 'hc', 'i']
ROLES = ['big', 'mid']
NOW = datetime.now(timezone.utc).isoformat()
TOOL = {'name': 'recover_inputs.py', 'python': platform.python_version(),
        'numpy': np.__version__, 'pandas': pd.__version__, 'algorithm_runs': 0}
provenance = {}
checks = {'source_run_id': RUN_ID, 'checked_at': NOW, 'failures': [], 'warnings': [],
          'symbols': {}, 'parameter_checks': [], 'formal_slices': []}


def digest(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def save_json(rel, obj, sources=None):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    provenance[rel] = {'source_path': sources or '工单内工程整理', 'copied_or_regenerated': 'regenerated',
                       'generation_kind': 'evidence_not_feature_computation'}
    return p


def copy_file(source, rel):
    source = Path(source)
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    before = digest(source)
    shutil.copyfile(source, p)
    assert before == digest(p) == digest(source), source
    provenance[rel] = {'source_path': str(source), 'source_sha256': before,
                       'copied_or_regenerated': 'copied', 'generation_kind': 'byte_copy',
                       'source_mtime': datetime.fromtimestamp(source.stat().st_mtime, timezone.utc).isoformat()}
    return p


def save_csv(rel, frame, sources):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(p, index=False, lineterminator='\n')
    provenance[rel] = {'source_path': sources, 'copied_or_regenerated': 'regenerated',
                       'generation_kind': 'read_only_export_no_feature_recalculation'}
    return p


def read_dba(directory, field, dtype):
    return DbArray(str(directory), field, dtype, access=mmap.ACCESS_READ).ndarray


def record_dba(p):
    p = Path(p)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': digest(p)}


order = REPO / 'runs/BI-01-CO-04/reviews/management-R0006/WORKER_ORDER.md'
assert digest(order) == '8ab35241f8bf350f600ccb03adc415ee22698b2bffa8e643cf62daa1dcccc4ea'
copy_file(order, 'copied/order/WORKER_ORDER.md')
required = [
    ('runs/BI-01-CO-04/artifacts/R0005/REPORT.md', '71bb32486c8c35ae346b8956282ac68622af31b3'),
    ('runs/BI-01-CO-04/artifacts/R0005/EVIDENCE_INDEX.md', '71bb32486c8c35ae346b8956282ac68622af31b3'),
    ('runs/BI-01-CO-04/artifacts/R0005/INPUT_QUALIFICATION.json', '71bb32486c8c35ae346b8956282ac68622af31b3'),
    ('runs/BI-01-CO-04/reviews/management-R0006/DECISION.md', '71bb32486c8c35ae346b8956282ac68622af31b3'),
    ('professional/exploration/03_TOOLING_AND_DATA_USAGE.md', 'b6ccf766dac055a793e75f76b77a73f4cfc74064'),
    ('professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md', 'b6ccf766dac055a793e75f76b77a73f4cfc74064')]
reads = []
for rel, commit in required:
    frozen = subprocess.check_output(['git', 'show', commit + ':' + rel], cwd=REPO)
    assert frozen == (REPO / rel).read_bytes(), rel
    reads.append({'path': rel, 'commit': commit, 'sha256': hashlib.sha256(frozen).hexdigest(),
                  'read_status': 'FULL_READ_IN_WORKER_TURN', 'checkout_matches_fixed_source': True})
save_json('evidence/REQUIRED_READS.json', reads)

for f in ['selected_turn_parameters.json', 'build_three_turn_plot.py', 'build_three_turn_plot.log',
          'prepare_staged_turn_jobs.py', 'run_staged_turn_job.py', 'validate_staged_turn_job.py',
          'generation_engine_readiness.json', 'handoff_source_change_audit.json',
          'calendar_axis_check.json', 'calendar_alias.json']:
    copy_file(SRC / f, 'copied/config_and_consumption/' + f)
for f in ['run_brief.json', 'manifest/run_summary.json', 'manifest/feature_slice_stats.csv',
          'manifest/timespan_index.csv', 'manifest/chart_manifest.csv',
          'delivery/DELIVERY_MANIFEST.json', 'delivery/PACKAGE_INDEX.csv']:
    copy_file(RUN / f, 'copied/run/' + f)
for f in ['three_turn_page.json', 'single_three_turns.fason.txt', 'chart_slice_alignment.json',
          'platform_plot.png', '验收报告.md']:
    copy_file(SRC / 'three_turn_plot' / f, 'copied/chart/' + f)
for source, rel in [
    (WORK / 'm3sof/settings/sof/GTQH_L1_20210104_20240208.py', 'source_config.py'),
    (SRC / 'turn_staging/prepared_jobs.json', 'prepared_jobs.json'),
    (SRC / 'turn_staging/app/mquant/config/prod/sof/GTQH_L1_20210104_20240208.json', 'engine_source_config.json'),
    (SRC / 'turn_staging/app/mquant/config/prod/store_dir.json', 'engine_store_dir.json'),
    (DATA / 'feature-parameters/read_verified_native_e.py', 'read_verified_native_e.py'),
    (Path('/m3varK/workspace/mquant_e6.2_prod/mquant/worker/adt/dbaw.py'), 'original_E_dbaw.py'),
    (WORK / 'mquant/tis/frpExample/STCalendar.py', 'STCalendar.py'),
    (WORK / 'mquant/tis/frpExample/Wave.py', 'Wave.py'),
    (WORK / 'mquant/aidata/feature_slicer.py', 'feature_slicer.py'),
    (WORK / 'mquant/aidata/csv_feature.py', 'csv_feature.py')]:
    copy_file(source, 'copied/config_and_consumption/' + rel)

selection = json.loads((SRC / 'selected_turn_parameters.json').read_text())
prepared = json.loads((SRC / 'turn_staging/prepared_jobs.json').read_text())
page = json.loads((SRC / 'three_turn_plot/three_turn_page.json').read_text())
summary = json.loads((RUN / 'manifest/run_summary.json').read_text())
assert page['run_id'] == summary['run_id'] == RUN_ID
assert page['members'] == summary['member_symbols'] == SYMS
assert summary['feature_slice_summary']['failed_slices'] == 0
code = {}
for rel in ['mquant/aidata', 'mquant/frame', 'mquant/tis', 'mquant/uplot', 'm3sof', 'pydim']:
    d = WORK / rel
    code[rel] = {'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=d, text=True).strip(),
                 'tracked_status': subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=no'], cwd=d, text=True),
                 'scope': 'CURRENT_CHECKOUT_NOT_ASSERTED_FULL_HISTORICAL_BUILD'}
save_json('evidence/ENVIRONMENT.json', {'tool': TOOL, 'source_code': code,
          'source_run_build_evidence': 'copied/config_and_consumption/handoff_source_change_audit.json',
          'engine': json.loads((SRC / 'generation_engine_readiness.json').read_text()),
          'regeneration_exact_gate': False,
          'regeneration_gate_reason': '未取得该二进制的完整编译源码/构建绑定；日历与bar时间合同存在实值冲突，不能猜测同配置重生能恢复as-of语义。'})

stats = pd.read_csv(RUN / 'manifest/feature_slice_stats.csv', keep_default_na=False)
bars_by_sym = {}
cal_by_sym = {}
inputs = []
differences = []
for sym in SYMS:
    inp = next(v for v in prepared['inputs'] if v['symbol'] == sym)
    d = Path(inp['staged_kline_cache'])
    raw = pd.DataFrame({k: read_dba(d, k, 'M8[ns]' if v.startswith('datetime') else v).copy()
                        for k, v in inp['fields'].items()})
    assert len(raw) == inp['rows'] == 8964
    # 实际原运行从源起点计算；只导出必要warm-up及完整9月30日，不导出2024全历史。
    frame = raw[raw.closeTs < pd.Timestamp('2021-10-01')].copy()
    frame.insert(0, 'symbol', sym)
    frame['source_key'] = [f'{d}:__ts__:{i}' for i in frame.index]
    frame['source_row'] = frame.index
    frame['source_index_ts'] = read_dba(d, '__ts__', 'M8[ns]')[frame.index]
    # 所有原生字段保留；不将natural_tsa覆盖到closeTs。
    bars_by_sym[sym] = frame
    path = f'regenerated/market/{sym}_30m_warmup_through_20210930.csv'
    save_csv(path, frame, str(d))
    inputs.extend(record_dba(d / (k + '.dba')) for k in list(inp['fields']) + ['__ts__'])
    caldir = DATA / 'calendar' / sym
    calendar = read_dba(caldir, 'natural_tsa', 'M8[ns]')
    cal_by_sym[sym] = calendar
    mapping = frame[['symbol', 'source_row', 'openUti', 'closeUti', 'openTs', 'closeTs', 'source_index_ts']].copy()
    mapping['calendar_open_time'] = calendar[frame.openUti.to_numpy(dtype='int64')]
    mapping['calendar_close_time'] = calendar[frame.closeUti.to_numpy(dtype='int64')]
    mapping['calendar_close_equals_bar_close'] = mapping.calendar_close_time == mapping.closeTs
    mapping['calendar_close_equals_index'] = mapping.calendar_close_time == mapping.source_index_ts
    save_csv(f'regenerated/time/{sym}_bar_calendar_mapping.csv', mapping, str(caldir / 'natural_tsa.dba'))
    bad = mapping[~mapping.calendar_close_equals_bar_close].copy()
    differences.append(bad)
    inputs.append({'path': str(caldir / 'natural_tsa.dba'), 'bytes': (caldir / 'natural_tsa.dba').stat().st_size,
                   'sha256': None, 'hash_status': 'FULL_LARGE_CALENDAR_NOT_HASHED',
                   'retained_evidence': f'regenerated/time/{sym}_bar_calendar_mapping.csv'})
    formal = RUN / f'feature_slices/big_000001/symbol/{sym}/gtqh_kline_30m/__default__.csv'
    fd = pd.read_csv(formal)
    matches = frame.set_index('closeUti', drop=False).loc[fd.closeUti]
    for col in ['open', 'high', 'low', 'close', 'volume', 'openInt', 'openUti', 'closeUti']:
        assert np.array_equal(matches[col].to_numpy(), fd[col].to_numpy()), (sym, col)
    copy_file(formal, f'copied/formal_slices/{sym}/gtqh_kline_30m.csv')
    checks['symbols'][sym] = {'frequency': '30m', 'source_input_rows': len(raw), 'exported_warmup_rows': len(frame),
        'first_business_time': str(frame.closeTs.min()), 'last_business_time': str(frame.closeTs.max()),
        'source_input_first': str(raw.closeTs.min()), 'source_input_last': str(raw.closeTs.max()),
        'warmup_start': str(raw.closeTs.min()), 'warmup_end_exclusive': '2021-08-15 00:00:00',
        'window_rows_including_sep30': int(((frame.closeTs >= '2021-08-15') & (frame.closeTs < '2021-10-01')).sum()),
        'formal_market_rows': len(fd), 'formal_market_matches_consumed_staged_input': True,
        'calendar_close_disagrees_with_bar_close': len(bad),
        'calendar_close_disagrees_with_source_index': int((~mapping.calendar_close_equals_index).sum()),
        'market_nulls': {k: int(v) for k, v in frame.isna().sum().items() if v}}
save_csv('evidence/TIME_MAPPING_CONFLICTS.csv', pd.concat(differences, ignore_index=True),
         [str(DATA / 'calendar'), 'staged KLine closeTs/closeUti'])

objects = []
for role in ROLES:
    merged = SRC / f'three_turn_plot/{role}_original_E.csv'
    assert digest(merged) == page['exports'][role]['sha256']
    full = pd.read_csv(merged, keep_default_na=False)
    assert len(full) == page['exports'][role]['rows']
    for sym in SYMS:
        name = sym + '__' + role
        for suffix in ['task.json', 'state.json', 'validated.json', 'engine.log']:
            copy_file(SRC / 'turn_staging' / (name + '.' + suffix),
                      'copied/config_and_consumption/jobs/' + name + '.' + suffix)
        task = json.loads((SRC / 'turn_staging' / (name + '.task.json')).read_text())
        state = json.loads((SRC / 'turn_staging' / (name + '.state.json')).read_text())
        valid = json.loads((SRC / 'turn_staging' / (name + '.validated.json')).read_text())
        job = next(x for x in prepared['jobs'] if x['symbol'] == sym and x['role'] == role)
        assert digest(SRC / 'turn_staging' / (name + '.task.json')) == job['task_sha256']
        assert valid['feature_ppid'] == selection['bindings'][role]['feature_ppid'] == job['feature_ppid']
        assert digest(valid['validated_csv']) == valid['csv_sha256']
        assert state['returncode'] == 0
        params = json.loads(task['task_params']['params'])
        assert params['specTerm'] == selection['bindings'][role]['specTerm']
        assert params['stMembershipLine'] == selection['bindings'][role]['stMembershipLine']
        assert params['falter']['zig']['retracePct'] == selection['bindings'][role]['zig_retracePct']
        assert params['falter']['zig']['featIn']['tar']['freq'] == '30m'
        # 日志实际记录的参数全JSON，逐项比较而不是仅依文件名认领。
        log = (SRC / 'turn_staging' / (name + '.engine.log')).read_text()
        logged = next(line.split('参数: ', 1)[1] for line in log.splitlines() if line.startswith('开始优化 ScaleTurnCalendar 参数: '))
        assert json.loads(logged) == params
        checks['parameter_checks'].append({'symbol': sym, 'role': role, 'task_hash_matches_prepared': True,
            'task_equals_engine_logged_parameters': True, 'ppid_matches_selection': True,
            'validated_csv_hash_matches': True, 'merged_consumed_csv_sha256': digest(merged),
            'engine_returncode': 0})
        formal = RUN / f'feature_slices/big_000001/symbol/{sym}/gtqh_E_{role}/__default__.csv'
        fd = pd.read_csv(formal, keep_default_na=False)
        copy_file(formal, f'copied/formal_slices/{sym}/gtqh_E_{role}.csv')
        record = stats[(stats.target_id == sym) & (stats.feature_key == 'gtqh_E_' + role)].iloc[0]
        assert int(record.row_count) == len(fd)
        for _, row in fd.iterrows():
            source = full.iloc[int(row['_csv_source_row']) - 2]
            for key in ['event_ts', 'x', 'y', 'xConfirm', 'yConfirm', 'symbol', 'turn_round']:
                assert str(source[key]) == str(row[key]), (sym, role, key)
        # 独立保留前置背景：仅冻结event_ts在9月30日及以前的原有事件。
        subset = full[(full.symbol == sym) & (pd.to_datetime(full.event_ts) < '2021-10-01')].copy()
        subset.insert(0, 'source_row', subset.index + 2)
        subset['scale'] = role
        subset['source_csv_sha256'] = digest(merged)
        subset['source_key'] = [f'{digest(merged)}:csv_line:{i + 2}' for i in subset.index]
        subset['object_id'] = ''
        subset['object_id_status'] = 'SOURCE_HAS_NO_OBJECT_ID_USE_SOURCE_KEY_ONLY'
        subset['direction'] = ''
        subset['direction_status'] = 'NOT_PROVIDED_UNVERIFIED_UPSTREAM_LINK'
        subset['revision'] = ''
        subset['revision_status'] = 'NOT_PROVIDED'
        subset['current_status'] = 'PRESENT_IN_FROZEN_EXPORT_ASOF_NOT_VALIDATED'
        subset['segment_id'] = ''
        bars = bars_by_sym[sym].set_index('closeUti')
        for field, price in [('x', 'y'), ('xConfirm', 'yConfirm')]:
            assert subset[field].isin(bars.index).all(), (sym, role, field)
            matched = bars.loc[subset[field]]
            assert np.allclose(matched.close, subset[price], rtol=0, atol=1e-8)
            subset[field + '_bar_close_time'] = matched.closeTs.to_numpy()
            subset[field + '_calendar_time'] = cal_by_sym[sym][subset[field].to_numpy(dtype='int64')]
        rel = f'regenerated/objects/{sym}_{role}_events_through_20210930.csv'
        save_csv(rel, subset, str(merged))
        objects.append({'symbol': sym, 'scale': role, 'rows': len(subset), 'path': rel,
                        'formal_window_rows': len(fd), 'source_merged_sha256': digest(merged),
                        'actual_and_confirm_uti_price_match_consumed_market': True,
                        'direction_known_rows': 0, 'official_object_id_rows': 0, 'revision_known_rows': 0})
        checks['formal_slices'].append({'symbol': sym, 'scale': role, 'rows': len(fd),
            'source_row_and_hash_link_verified': True, 'slice_success': bool(record.slice_success)})

# 三品种的原始时间轴比较，仍不能消除同轴内部的两种时间冲突。
first = bars_by_sym['rb']
checks['three_symbol_axes_equal'] = all(
    bars_by_sym[s][['openUti', 'closeUti', 'openTs', 'closeTs', 'source_index_ts']].reset_index(drop=True).equals(
        first[['openUti', 'closeUti', 'openTs', 'closeTs', 'source_index_ts']].reset_index(drop=True)) for s in SYMS)
checks['warnings'] = ['SOURCE_TIME_AXIS_CONFLICT', 'DIRECTION_NOT_PRESENT_OR_CONFIG_LINKED',
                       'REVISION_LIFECYCLE_NOT_PROVEN', 'NO_FULL_HISTORICAL_BUILD_ATTESTATION']
checks['verification_scope'] = '字节身份、参数消费、行数和坐标/价格关系通过；as-of语义未通过。'
save_json('evidence/VALIDATION.json', checks)
save_json('evidence/SOURCE_INPUTS.json', inputs)
save_json('evidence/OBJECT_COVERAGE.json', objects)
save_json('evidence/TOOL.json', TOOL)
save_json('DATA_MANIFEST.json', {
    'schema': 'bi01-input-recovery/v1', 'order_id': 'BI01CO04-INPUT-RECOVERY-01', 'work_id': 'BI-01',
    'run_id': 'BI-01-CO-04', 'source_run_id': RUN_ID, 'source_root': str(SRC),
    'source_data_root': str(DATA), 'original_output_root': str(RUN), 'delivery_root': str(OUT),
    'symbols': SYMS, 'frequency': '30m',
    'original_window': {'start': '2021-08-15 00:00:00', 'end': '2021-09-30 00:00:00', 'end_includes_sep30_day': False},
    'recovery_export_window': {'start': '2021-01-04 09:30:00', 'end_exclusive': '2021-10-01 00:00:00',
                               'reason': '实际原运行源起点warm-up，补齐工单9月30日；无全历史复制'},
    'core': {'aidata_head': 'b5a752c2701dd8997b47583808f30bc5da5d9769',
             'engine_version_from_log': 'e6.2.0.6',
             'engine_sha256_from_original_receipts': 'dba166c7fc8d0acf2e56499699b36ac47dd30c923a739e52a7288860fae57450',
             'historical_source_build_complete': False},
    'p0': {'5.1_formal_identity': 'PARTIAL', '5.2_actual_parameters_and_consumption': 'SATISFIED',
           '5.3_market': 'PARTIAL', '5.4_large_mid_objects': 'PARTIAL', '5.5_semantic_dictionary': 'PARTIAL',
           '5.6_receipt': 'SATISFIED'},
    'overall_p0': 'PARTIAL_BLOCKED_FOR_ASOF', 'suitable_for_professional_asof_resume': False,
    'p1': 'EXISTING_STATIC_PNG_RECOVERED_AND_VIEWED',
    'object_coverage': objects, 'market_coverage': checks['symbols'],
    'missing': ['direction及其与本配置上游zig的可靠逐对象对应', 'revision/撤回/更新及current状态的原合同',
                'UTI natural_tsa、bar closeTs、event index 三者可知时间冲突的权威解释',
                '原E二进制完整源码/构建绑定及冻结日历版本'],
    'algorithm_regeneration': {'performed': False, 'allowed_exact_conditions_met': False},
    'classification': {'copied': 'copied/：原字节；其中图像含原small图例但不补小尺度数据',
                       'regenerated': 'regenerated/：现存缓存/CSV的只读时间截取与字段整理，零特征重算'},
    'generated_at': NOW})
save_json('evidence/PROVENANCE.json', provenance)
print(json.dumps({'output': str(OUT), 'market': checks['symbols'], 'objects': objects,
                  'failures': checks['failures'], 'algorithm_runs': 0}, ensure_ascii=False, indent=2))
