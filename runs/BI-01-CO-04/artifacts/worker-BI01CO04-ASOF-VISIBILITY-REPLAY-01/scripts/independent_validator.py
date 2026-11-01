"""只读独立消费者。区分B出口交付完整性与A出口可知性资格。"""
from pathlib import Path
from datetime import datetime
import copy, csv, hashlib, json, sys

ROOT=Path(__file__).resolve().parents[1]
ORDER='BI01CO04-ASOF-VISIBILITY-REPLAY-01'
FIELDS={'order_id':ORDER,'work_id':'BI-01','run_id':'BI-01-CO-04',
        'issuer_invocation_id':'BI01-CO-04-R0007-WORKER-INTAKE-c149d108',
        'return_to':'chatgpt:BI-01-CO-04:management'}


def require(condition, reason):
    if not condition: raise ValueError(reason)


def validate_fixture(rows):
    """仅验证注入测试的账本约束；不替代真实引擎的no-lookahead证据。"""
    prior=None; lifecycle={}
    for row in rows:
        ts=datetime.fromisoformat(row['replay_event_ts'])
        maximum=datetime.fromisoformat(row['max_input_bar_ts'])
        require(ts.tzinfo is not None and maximum.tzinfo is not None,'TIME_AXIS_MISMATCH')
        require(maximum<=ts,'FUTURE_INPUT_LEAK')
        require(row['clock']=='Asia/Shanghai' and row['alternate_mapping_preserved'],'TIME_AXIS_MISMATCH')
        require(prior is None or ts>prior,'OUT_OF_ORDER')
        prior=ts
        require(row['input_prefix_hash'] and row['replay_event_seq']>0,'EMPTY_EVENT_WITH_STATE')
        require(row['upstream_direction'] is not None or row['direction_status']=='MISSING_OR_NOT_PROVIDED','MISSING_DIRECTION_MISREPRESENTED')
        key=row['replay_object_key']; previous=lifecycle.get(key)
        require(not row['reappeared'] or previous is False,'REAPPEAR_WITHOUT_WITHDRAWAL')
        require(not (row['present'] and row['withdrawn']),'PRESENT_AND_WITHDRAWN')
        lifecycle[key]=row['present']
    return True


def injections():
    good=[{'replay_event_ts':'2021-08-16T09:30:00+08:00','max_input_bar_ts':'2021-08-16T09:30:00+08:00',
           'clock':'Asia/Shanghai','alternate_mapping_preserved':True,'input_prefix_hash':'a'*64,
           'replay_event_seq':1,'upstream_direction':None,'direction_status':'MISSING_OR_NOT_PROVIDED',
           'replay_object_key':'fixture-local-1','present':True,'withdrawn':False,'reappeared':False}]
    require(validate_fixture(good),'POSITIVE_FIXTURE_FAILED')
    cases=[]
    def one(name, changed, expected):
        result={'case':name,'expected_rejection':expected,'fixture_only':True}
        try: validate_fixture(changed);result.update(rejected=False,passed=False)
        except ValueError as e:result.update(rejected=True,observed_rejection=str(e),passed=str(e)==expected)
        cases.append(result)
    bad=copy.deepcopy(good);bad[0]['max_input_bar_ts']='2021-10-08T09:30:00+08:00';one('未来数据泄漏探针',bad,'FUTURE_INPUT_LEAK')
    bad=copy.deepcopy(good);bad[0]['alternate_mapping_preserved']=False;one('时间轴错配/消灭alternate',bad,'TIME_AXIS_MISMATCH')
    bad=copy.deepcopy(good);bad[0]['reappeared']=True;one('撤回重现非法连接',bad,'REAPPEAR_WITHOUT_WITHDRAWAL')
    bad=copy.deepcopy(good);bad[0]['direction_status']='VERIFIED_UPSTREAM';one('缺方向伪称已核',bad,'MISSING_DIRECTION_MISREPRESENTED')
    bad=copy.deepcopy(good);bad[0]['input_prefix_hash']='';one('空事件伪称状态',bad,'EMPTY_EVENT_WITH_STATE')
    bad=copy.deepcopy(good);bad.append(copy.deepcopy(good[0]));one('乱序或重复输入',bad,'OUT_OF_ORDER')
    return {'scope':'STRUCTURAL_VALIDATOR_FIXTURES_ONLY_NOT_PRODUCTION_REPLAY_TESTS',
            'positive_fixture_passed':True,'cases':cases,'all_expected_rejections_passed':all(c['passed'] for c in cases)}


def csv_rows(path):
    with path.open(newline='') as f:return list(csv.DictReader(f))


def gate(manifest, visibility, lifecycle, proof):
    if manifest['exit']=='BLOCKED_NO_LOOKAHEAD_PROOF':return 'B'
    require(manifest['exit']=='QUALIFIED_FOR_PROFESSIONAL_ASOF','INVALID_EXIT')
    require(visibility and lifecycle,'QUALIFIED_WITHOUT_OBSERVED_LEDGER')
    require(all(row.get('first_seen_at') for row in lifecycle),'UNOBSERVED_FIRST_SEEN')
    require(all(v['status']=='PASS' for v in proof['checks'].values()),'QUALIFIED_WITHOUT_PROOFS')
    return 'A'


def validate_package():
    m=json.loads((ROOT/'REPLAY_MANIFEST.json').read_text())
    require(m['order_id']==ORDER and m['exit']=='BLOCKED_NO_LOOKAHEAD_PROOF','WRONG_ORDER_OR_EXIT')
    require(m['symbols']==['rb','hc','i'] and m['scales']==['big','mid'],'SCOPE_CHANGED')
    require(m['replay_run_id'].startswith('BI01CO04_ASOF_REPLAY_'),'IDENTITY_REUSED')
    require(m['replay_run_id']!='GTQH_C001_three_turns_20261101_162005','OLD_RUN_RENAMED')
    r=json.loads((ROOT/'EXECUTION_RECEIPT.json').read_text())
    require(r['returncode']==0,'PROCESS_RECEIPT_CHANGED')
    out=(ROOT/'logs/native_engine.stdout').read_text()
    err=(ROOT/'logs/native_engine.stderr').read_text()
    trace=(ROOT/'logs/native_engine.strace').read_text()
    require('开始运行 Frp 回测模型 ScaleTurnCalendar' in out,'TASK_NOT_ENTERED')
    require('Edh program crashed with an error:' in err and '/tmp: openTempFile: permission denied' in err,'CRASH_PROOF_MISSING')
    require('/tmp/hsfis' in trace and 'EACCES' in trace,'SYSCALL_PROOF_MISSING')
    require('time used:' not in out,'INITIAL_FAILURE_WAS_OVERWRITTEN')
    repair=json.loads((ROOT/'BOOTSTRAP_TEMP_CHECK_RECEIPT.json').read_text())
    require('TMPDIR' in repair['environment_allowlist'],'REPAIR_ENV_NOT_FROZEN')
    require('/tmp: openTempFile: permission denied' not in (ROOT/'logs/temp_redirect_check.stderr').read_text(),'TEMP_REPAIR_DID_NOT_RESOLVE')
    route=json.loads((ROOT/'NATIVE_PREFIX_ROUTE_EXECUTION.json').read_text())
    require(route['native_success'],'ORIGINAL_ENGINE_PREFIX_DID_NOT_COMPLETE')
    matrix=json.loads((ROOT/'MATRIX_EXECUTION_RECEIPTS.json').read_text())
    require(len(matrix)==5 and all(v['native_success'] for v in matrix),'NATIVE_MATRIX_INCOMPLETE')
    require(m['native_process_invocations']==9 and m['successful_native_computations']==7,'ATTEMPT_ACCOUNTING_MISMATCH')
    logs=[('rb','big',name) for name in ['native_engine','temp_redirect_check','pnv_prefix_probe','observer_capability']]
    logs += [(s,c,'matrix_'+s+'_'+c) for s in ['rb','hc','i'] for c in ['big','mid'] if (s,c)!=('rb','big')]
    for symbol,scale,name in logs:
        text=(ROOT/'logs'/ (name+'.stdout')).read_text()
        line=next(line for line in text.splitlines() if line.startswith('开始优化 ScaleTurnCalendar 参数: '))
        consumed=json.loads(line.split('参数: ',1)[1])
        frozen=json.loads((ROOT/f'copied/baseline/copied/config_and_consumption/jobs/{symbol}__{scale}.task.json').read_text())
        current=json.loads((ROOT/f'execution/tasks/{symbol}__{scale}.json').read_text())
        require(consumed==json.loads(frozen['task_params']['params'])==json.loads(current['task_params']['params']),'ACTUAL_PARAMETER_CONSUMPTION_MISMATCH')
        require('tar_sym = "'+symbol+'"' in text,'ACTUAL_TARGET_MISMATCH')
    capability=(ROOT/'logs/observer_capability.stdout').read_text()
    require('NATIVE_OBJECT_CAPABILITY_END' in capability,'CAPABILITY_PROBE_INCOMPLETE')
    require(m['final_blocker']=='EVENT_OBSERVATION_AND_PER_EVENT_INPUT_FRONTIER_NOT_EXPOSED','TEMP_FAILURE_MISUSED_AS_FINAL_BLOCKER')
    visibility=csv_rows(ROOT/'VISIBILITY_LEDGER.csv');life=csv_rows(ROOT/'OBJECT_LIFECYCLE_LEDGER.csv')
    require(len(visibility)==6 and not life,'FABRICATED_LIFECYCLE')
    for row in visibility:
        require(not row['first_seen_at'] and not row['max_input_bar_ts'] and not row['input_prefix_hash'],'BATCH_BOUNDARY_MISREPRESENTED_AS_EVENT_OBSERVATION')
        require(row['state_status']=='BATCH_RECOMPUTED_EVENT_OBSERVATION_UNAVAILABLE','FALSE_CALCULATION_FAILURE')
    proof=json.loads((ROOT/'NO_LOOKAHEAD_VALIDATION.json').read_text())
    require(gate(m,visibility,life,proof)=='B','WRONG_GATE')
    # 集成注入：把这个真实坏包的出口改成A，必须被独立消费者拒绝。
    bad=copy.deepcopy(m);bad['exit']='QUALIFIED_FOR_PROFESSIONAL_ASOF'
    try:gate(bad,visibility,life,proof);raise AssertionError('BAD_QUALIFICATION_ACCEPTED')
    except ValueError as e:require(str(e)=='QUALIFIED_WITHOUT_OBSERVED_LEDGER','WRONG_QUALIFICATION_REJECTION')
    comparison=json.loads((ROOT/'FORMAL_BASELINE_COMPARISON.json').read_text())
    require(len(comparison['rows'])==620,'BASELINE_ROWS_DROPPED')
    require(sum(x['baseline_class']=='formal_slice' for x in comparison['rows'])==96,'FORMAL_ROWS_DROPPED')
    require(sum(x['baseline_class']=='recovered_prefix' for x in comparison['rows'])==524,'PREFIX_ROWS_DROPPED')
    require(sum(x['comparison_status']=='MATCH_SAME_SEMANTIC_TUPLE' for x in comparison['rows'])==619,'NUMERIC_BASELINE_MATCH_COUNT')
    require(sum(x['comparison_status']=='OUTSIDE_FROZEN_PREFIX_EVENT_NOT_REPRODUCED' for x in comparison['rows'])==1,'OUTSIDE_PREFIX_ROW_NOT_RETAINED')
    objects=csv_rows(ROOT/'RECOMPUTED_OBJECT_ROWS.csv');require(len(objects)==524,'RECOMPUTED_COUNT')
    require(all(not r['first_seen_at'] and r['record_status']=='ACTUAL_NATIVE_BATCH_OUTPUT_NOT_OPERATIONAL_KNOWN_STATE' for r in objects),'STATIC_FIRST_SEEN_BACKFILL')
    for sym in ['rb','hc','i']:
        for scale in ['big','mid']:
            label='instrumented' if (sym,scale)==('rb','big') else 'fixed_prefix'
            result=json.loads((ROOT/f'recomputed/{label}/{sym}_{scale}.json').read_text())['rows']
            baseline=csv_rows(ROOT/f'copied/baseline/regenerated/objects/{sym}_{scale}_events_through_20210930.csv')
            def key(r):return (r['turn_round'],r['event_ts'],int(r['x']),float(r['y']),int(r['xConfirm']),float(r['yConfirm']))
            from collections import Counter
            require(Counter(map(key,result))==Counter(map(key,baseline)),'INDEPENDENT_NATIVE_BASELINE_MISMATCH')
    require(json.loads((ROOT/'recomputed/instrumented/rb_big.json').read_text())['rows']==json.loads((ROOT/'recomputed/untraced/rb_big.json').read_text())['rows'],'NEUTRALITY_MISMATCH')
    for key,value in FIELDS.items():require((key+': '+value) in (ROOT/'FULL_RESPONSE.md').read_text().splitlines()[:5],'HEADER_MISMATCH')
    expected=json.loads((ROOT/'FAILURE_INJECTION_RESULTS.json').read_text())
    require(expected['structural_tests']==injections(),'INJECTION_RESULT_MISMATCH')
    return {'result':'PASS_BLOCKER_DELIVERY_INTEGRITY','qualification':'BLOCKED_NO_LOOKAHEAD_PROOF',
            'production_no_lookahead_tests':'NOT_COMPLETED','lifecycle_observations':0,'baseline_rows_retained':620,
            'native_calls':9,'native_successful_computations':7,'native_object_rows':524,
            'native_parameter_consumption_verified_calls':9,
            'baseline_matches':619,'explicit_out_of_prefix_rows':1,
            'structural_bad_fixtures_rejected':6,'false_qualified_real_package_rejected':True}


def verify_receipt():
    r=json.loads((ROOT/'PACKAGE_RECEIPT.json').read_text())
    wanted={v['path'] for v in r['files']}
    actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and '.runtime' not in p.relative_to(ROOT).parts}
    require(actual==wanted|{'PACKAGE_RECEIPT.json','SHA256SUMS'},'FILE_SET_MISMATCH')
    require(len(wanted)==len(r['files']),'DUPLICATE_RECEIPT_PATH')
    require(len(r['files'])==r['file_count'],'RECEIPT_FILE_COUNT_MISMATCH')
    for record in r['files']:
        name=record['path'];require(not Path(name).is_absolute() and '..' not in Path(name).parts,'PATH_ESCAPE')
        p=ROOT/name;require(p.stat().st_size==record['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==record['sha256'],'HASH_OR_BYTES_MISMATCH: '+name)
        if record['rows'] is not None:
            rows=csv_rows(p);require(len(rows)==record['rows'],'ROWS_MISMATCH: '+name)
            key=record.get('business_time_field')
            times=[row[key] for row in rows if key and row.get(key)]
            require(record['first_business_time']==(min(times) if times else None),'FIRST_TIME_MISMATCH: '+name)
            require(record['last_business_time']==(max(times) if times else None),'LAST_TIME_MISMATCH: '+name)
    sums={line.split('  ',1)[1]:line.split('  ',1)[0] for line in (ROOT/'SHA256SUMS').read_text().splitlines()}
    require(set(sums)==actual-{'SHA256SUMS'},'OUTER_SET_MISMATCH')
    for path,digest in sums.items():require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'OUTER_HASH_MISMATCH')
    return len(r['files'])


if __name__=='__main__':
    result=validate_package()
    if len(sys.argv)==1 or sys.argv[1]!='--preseal':result['files_verified']=verify_receipt()
    print(json.dumps(result,ensure_ascii=False))
