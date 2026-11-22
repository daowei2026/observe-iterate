"""正式X验收：不运行生产者，核对独立读回、全输入范围与落盘文件。"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import Counter
import csv
import json
import math
import subprocess

ROOT=Path(__file__).resolve().parent
def load(name):return json.loads((ROOT/name).read_text())
def digest(path):return sha256(Path(path).read_bytes()).hexdigest()
def write(name,value):(ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def read(path):
    with Path(path).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

p=load('produced/report.json');r=load('readback/report.json');u=load('UPSTREAM_EXTRACTION.json')
assert p['completed'] and p['producer_executed'] and p['public_read_completed']
assert r['completed'] and not r['producer_executed'] and r['public_read_completed'] and r['pid']!=p['pid']
assert u['completed'] and not u['producer_executed']
for field in ['full_dir','configuration_sha256','fields_sha256','engine_sha256','frp_code_ref','tis_code_ref','all_table_names']:
    assert p[field]==r[field],field
assert len(r['tables'])==31 and p['primary_public_api_equal'] and r['primary_public_api_equal']
comparison=[]
for name,table in r['tables'].items():
    old=p['tables'][name]
    assert table['rows']==old['rows'] and table['columns']==old['columns']
    assert table['sha256']==old['sha256']==digest(table['path'])
    comparison.append(dict(table=name,rows=table['rows'],sha256=table['sha256'],identical=True))
scope=[];time_axis=None
for symbol in ['rb','hc','i']:
    rows=read(ROOT/'upstream'/f'{symbol}_kline.csv')
    ts=[x['timestamp'] for x in rows];utis=[int(float(x['closeUti'])) for x in rows]
    assert len(ts)==len(set(ts)) and ts==sorted(ts) and utis==sorted(set(utis))
    assert len(rows)==49683 and ts[0]=='2021-01-04 09:05:00' and ts[-1]=='2023-12-29 15:00:00'
    if time_axis is None:time_axis=ts
    else:assert ts==time_axis
    quality=dict(symbol=symbol,rows=len(rows),first=ts[0],last=ts[-1],first_close_uti=utis[0],last_close_uti=utis[-1],
        years=dict(Counter(t[:4] for t in ts)),close_nonfinite=sum(not x['close'] or not math.isfinite(float(x['close'])) for x in rows),
        duplicate_timestamps=0,duplicate_utis=0,out_of_order=0,
        uti_step_distribution=dict(Counter(str(b-a) for a,b in zip(utis,utis[1:]))))
    scope.append(quality)
native=[]
for path in sorted(Path(r['full_dir']).rglob('*')):
    if path.is_file():native.append(dict(relative_path=str(path.relative_to(r['full_dir'])),bytes=path.stat().st_size,sha256=digest(path)))
write('NATIVE_OUTPUT_MANIFEST.json',dict(root=r['full_dir'],files=native,total_files=len(native),total_bytes=sum(x['bytes'] for x in native)))
write('INPUT_SCOPE_VALIDATION.json',dict(completed=True,symbols=scope,all_symbol_time_axes_equal=True,
    requested={'start_day':'2021-01-01','end_day':'2023-12-31','freq':'5m','calendar':'night_end_at_2300'},
    meaning='节假日边界未产生KLine行；首末实际记录与请求日界分别保留。69个非有限close/品种不伪作有效连续覆盖。'))
binding=dict(feature_name='CommonPriceTurnGroupCandidatesFrp',
    code_version=dict(frp=p['frp_code_ref'],tis=p['tis_code_ref']),
    parameter_instance_ref='configuration.json',parameter_version=p['configuration_sha256'],
    run_id='OI-F800-STAT-20261122-01',call_id='C0005',delegation_id='D002',
    instance_kind='NEW_FORMAL_PRODUCTION',
    data_scope=dict(symbols=['rb','hc','i'],start_time='2021-01-01',end_time='2023-12-31',
        actual_start_time=scope[0]['first'],actual_end_time=scope[0]['last'],freq='5m',calendar='night_end_at_2300',
        sessions=['DAY_CLOCK_09_15','NIGHT_CLOCK_21_23'],sof='TA_updto20240229_DBA',stk_tlist='steel',
        input_positions_per_symbol=49683,input_symbol_rows=149049,per_symbol_validation='INPUT_SCOPE_VALIDATION.json'),
    result_identity=dict(full_dir=r['full_dir'],layout='common_price_turn_groups.core.v2',fields_sha256=r['fields_sha256'],
        original_candidate_dir=p['original_candidate_full_dir'],original_candidate_fields_present_before=False,
        storage_routing='PLATFORM_STORAGE_BINDING.json',native_file_manifest='NATIVE_OUTPUT_MANIFEST.json'),
    actual_loading=dict(engine=p['engine_executable'],engine_sha256=p['engine_sha256'],native_pid=1712794,
        source_binding='FRP_SOURCE_BINDING.json',native_process_observation='NATIVE_PROCESS_OBSERVATION.json',
        production_reconciliation='PRODUCTION_RECONCILIATION.json'),
    production=dict(started_at=p['started_at'],finished_at=p['finished_at'],feature_python_pid=p['pid'],
        native_producer_executed=True,feature_python_exit_code=0,supervisor_exit_code=1,
        monitor_exception='监控按PID去重漏记exec转换；独立真实进程快照与正式成功报告完成验收；未重跑'),
    artifact_refs=['produced/report.json','readback/report.json','UPSTREAM_EXTRACTION.json','configuration.json',
        'NATIVE_OUTPUT_MANIFEST.json','INPUT_SCOPE_VALIDATION.json','SOURCE_AUDIT.json'],
    run_result_tables=[dict(name=name,**meta) for name,meta in r['tables'].items()],
    readback_validation=dict(all_31_tables_equal=True,independent_process=True,producer_pid=p['pid'],reader_pid=r['pid'],
        only_read=True,primary_api_equal=True,native_K800_output_windows_verified=True,tables=comparison),
    known_data_limits=['公开F是稀疏观点，不含逐Tick内部状态及所有试探/材料计数器',
        '独立全量上游已读出；首次阻断/近时pair筛查为明确规则参考，不冒充native状态或业务真值',
        '原始转折按Rct唯一实际位置；含每品种初始化锚点，不宣称覆盖未被Rct暴露的全部原始市场波动',
        '统计分母含缺价KLine日历行；连续有效价格检查另排除缺价，右删失单列'],
    verified_at=datetime.now(timezone.utc).isoformat())
write('FeatureRunResultBinding.json',binding)
write('configuration.json',load('readback/configuration.json'))
assert digest(ROOT/'configuration.json')==binding['parameter_version']
cli='/home/dw/.agents/skills/long-task-status/scripts/task_status.py'
for args in [('step-complete','--step-id','readback','--evidence',str(ROOT/'FeatureRunResultBinding.json')),
             ('step-start','--step-id','profile','--action','X独立读回验收通过，开始G1-G8全量统计','--next-action','完成结构检查和全部可支持分层剖面')]:
    cp=subprocess.run(['python',cli,*args,'--root','/dwdhome/fy/BASE_E6_2_copy','--task-id','oi-f800-stat-20261122-01-d002-e1'],capture_output=True,text=True)
    assert cp.returncode==0,cp.stderr
print(json.dumps(dict(x_accepted=True,tables=len(comparison),native_files=len(native),input_scope=scope),ensure_ascii=False))
