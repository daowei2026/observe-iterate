"""依据已完成的原生计算和ABI实测形成最终B出口；不以临时目录故障作最终阻断。"""
from finite_probe import *
from collections import Counter
from independent_validator import injections

m=json.loads((OUT/'REPLAY_MANIFEST.json').read_text());rid=m['replay_run_id']
archive=OUT/'diagnostics/superseded_before_environment_repair';archive.mkdir(parents=True,exist_ok=True)
for name in ['EXECUTION_ANALYSIS.json','VISIBILITY_LEDGER.csv','OBJECT_LIFECYCLE_LEDGER.csv',
             'FORMAL_BASELINE_COMPARISON.json','NO_LOOKAHEAD_VALIDATION.json','FAILURE_INJECTION_RESULTS.json']:
    src=OUT/name
    if src.exists() and not (archive/name).exists():shutil.copyfile(src,archive/name)
(archive/'STATUS.txt').write_text('历史中间态，已被Owner工程范围澄清及随后真实修复/数值计算取代；不得作为当前结论。\n')
native={};baseline={};all_objects=[]
def tuple_key(row):return (row['turn_round'],row['event_ts'],int(row['x']),float(row['y']),int(row['xConfirm']),float(row['yConfirm']))
for sym in SYMS:
 for role in ['big','mid']:
    label='instrumented' if (sym,role)==('rb','big') else 'fixed_prefix'
    source=OUT/f'recomputed/{label}/{sym}_{role}.json'
    data=json.loads(source.read_text())['rows'];native[(sym,role)]=data
    baseline[(sym,role)]=list(csv.DictReader((OLD/f'regenerated/objects/{sym}_{role}_events_through_20210930.csv').open()))
    assert Counter(map(tuple_key,data))==Counter(map(tuple_key,baseline[(sym,role)]))
    for i,row in enumerate(data):
        all_objects.append({**row,'replay_run_id':rid,'source_key':sha(source)+':native_readback_row:'+str(i),
            'replay_object_key':rid+':'+sym+':'+role+':batch_occurrence:'+str(i),
            'replay_key_status':'REPLAY_LOCAL_BATCH_OCCURRENCE_NOT_AUDITED_LIFECYCLE_ID',
            'first_seen_at':'','last_seen_at':'','state_change_at':'','present':'',
            'withdrawn':'','reappeared':'','lifecycle_seq':'','state_hash':'',
            'upstream_direction':'','direction_status':'NOT_MAPPED_NO_KNOWN_TIME_PROOF',
            'record_status':'ACTUAL_NATIVE_BATCH_OUTPUT_NOT_OPERATIONAL_KNOWN_STATE'})
assert len(all_objects)==524
with (OUT/'RECOMPUTED_OBJECT_ROWS.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(all_objects[0]));writer.writeheader();writer.writerows(all_objects)
a=json.loads((OUT/'recomputed/instrumented/rb_big.json').read_text())['rows']
b=json.loads((OUT/'recomputed/untraced/rb_big.json').read_text())['rows'];assert a==b
js('INSTRUMENTATION_NEUTRALITY.json',{'status':'PASS_FIXED_PREFIX_ONLY','symbol':'rb','scale':'big',
    'input_prefix_bars':2160,'rows':14,'full_ordered_numeric_and_event_tuple_equality':True,
    'instrumented':'NATIVE_PREFIX_ROUTE_EXECUTION.json','untraced':'OBSERVER_CAPABILITY_EXECUTION.json',
    'does_not_prove_per_event_observer_neutrality':True})
cap=(OUT/'logs/observer_capability.stdout').read_text()
methods=re.findall(r'^  ([A-Za-z_][A-Za-z_0-9]*)= ',cap,re.M)
assert methods==['__repr__','run','runRealTime','stopRealTime','pushTick','pushTicks','packEventName','uniqueId']
trace=(OUT/'logs/pnv_prefix_probe.strace').read_text()
market_opens=[line for line in trace.splitlines() if 'openat' in line and '/pnv/30m/' in line and '= -1' not in line]
external_market=[line for line in trace.splitlines() if 'openat' in line and '/m3varF/' in line and '= -1' not in line]
assert len(market_opens)>=8 and not external_market
route=json.loads((OUT/'PNV_PREFIX_ROUTE_RECEIPT.json').read_text())
unchanged=[]
for record in route['files']:
 p=OUT/record['path'];assert sha(p)==record['sha256'];unchanged.append(record['path'])
js('NATIVE_OBSERVABILITY_ASSESSMENT.json',{'replay_run_id':rid,
 'final_exit':'BLOCKED_NO_LOOKAHEAD_PROOF','temporary_directory_failure_resolved':True,
 'owned_pnv_route_resolved':True,'native_successful_symbol_scales':6,'native_recomputed_rows':524,
 'native_public_class_methods':methods,'instance_scope_result':'No scope inside native host object',
 'per_event_state_subscription_or_step_readback_exposed':False,
 'history_interface_result':'batch result available after history completion, without per-event first-seen/withdraw/reappear observations',
 'source_reference_not_build_attestation':True,
 'critical_missing':'主顺序增量执行的逐事件状态/输入前缀观察合同与可用观察入口，及其与本冻结二进制的绑定',
 'not_claimed':['算法含未来信息','算法数学错误','临时目录不可修复','只允许启动一次进程'],
 'counterfactual_prefix_queries_are_not_primary_event_observations':True,
 'why_not_more_same_runs':'重复batch仅增加终态快照，不补该次主执行内部首次输出/撤回/重现及逐事件实际读边界；独立prefix计算是第9.2节校验，不能未经合同改名为第7节主增量观察。',
 'minimum_recovery':'给同一冻结原引擎提供只观察的逐事件输出/状态回读与输入frontier回调，或由Management具名采用不同的查询式可知性合同；前者需neutrality及全部第9节检验，后者不得由Worker自行替换。'})
js('BATCH_INPUT_BOUNDARY_AUDIT.json',{'scope':'rb/big fixed prefix actual native IO only',
 'market_open_lines':market_opens,'external_formal_market_opens':external_market,
 'input_prefix_rows':2160,'source_row_upper_bound':2159,'canonical_upper_bound':'2021-09-30T15:00:00+08:00',
 'pnv_after_engine_unchanged_files':unchanged,'per_event_read_frontiers_observed':False,
 'physical_prefix_bound_passed':True,'per_event_no_lookahead_not_proven':True})
columns=['replay_run_id','symbol','scale','replay_event_seq','replay_event_ts','max_input_bar_ts',
 'max_input_source_row','input_prefix_hash','source_actual_uti','actual_bar_ts','actual_price',
 'source_confirm_uti','confirm_bar_ts','confirm_price','first_seen_at','last_seen_at','state_change_at',
 'present','withdrawn','reappeared','lifecycle_seq','state_hash','source_key','replay_object_key',
 'upstream_direction','direction_status','event_ts','canonical_bar_time','calendar_alternate_time',
 'mapping_conflict','state_status','batch_input_upper_bound','batch_object_rows','notes']
with (OUT/'VISIBILITY_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=columns);w.writeheader()
 for sym in SYMS:
  for role in ['big','mid']:
   w.writerow({'replay_run_id':rid,'symbol':sym,'scale':role,
     'direction_status':'NOT_MAPPED_NO_OPERATIONAL_KNOWN_TIME',
     'state_status':'BATCH_RECOMPUTED_EVENT_OBSERVATION_UNAVAILABLE',
     'batch_input_upper_bound':'2021-09-30T15:00:00+08:00','batch_object_rows':len(native[(sym,role)]),
     'notes':'批次覆盖状态行，不是逐事件观察；第7节所有未知字段留空'})
with (OUT/'OBJECT_LIFECYCLE_LEDGER.csv').open('w',newline='') as f:csv.DictWriter(f,fieldnames=columns).writeheader()
rows=[]
for sym in SYMS:
 for role in ['big','mid']:
  known=Counter(map(tuple_key,native[(sym,role)]))
  for typ,path in [('formal_slice',OLD/f'copied/formal_slices/{sym}/gtqh_E_{role}.csv'),
                   ('recovered_prefix',OLD/f'regenerated/objects/{sym}_{role}_events_through_20210930.csv')]:
   for physical,row in enumerate(csv.DictReader(path.open()),2):
    found=known[tuple_key(row)]>0
    after=row['event_ts']>'2021-09-30 15:00:00'
    status='MATCH_SAME_SEMANTIC_TUPLE' if found else ('OUTSIDE_FROZEN_PREFIX_EVENT_NOT_REPRODUCED' if after else 'UNEXPLAINED_MISMATCH')
    assert status!='UNEXPLAINED_MISMATCH'
    rows.append({'symbol':sym,'scale':role,'baseline_class':typ,'baseline_physical_row':physical,
      'baseline_source_path':str(path.relative_to(REPO)),'baseline_file_sha256':sha(path),
      'baseline_fields':row,'comparison_status':status,'after_decision_window_event':after})
assert len(rows)==620 and sum(r['comparison_status']=='MATCH_SAME_SEMANTIC_TUPLE' for r in rows)==619
js('FORMAL_BASELINE_COMPARISON.json',{'replay_run_id':rid,'status':'PASS_FROZEN_PREFIX_NUMERICS_WITH_EXPLICIT_OUT_OF_PREFIX_ROW',
 'formal_rows':96,'recovered_prefix_rows':524,'matching_prefix_rows':524,'matching_formal_rows':95,
 'outside_prefix_formal_rows':1,'unexplained_mismatches':0,'discarded_rows':0,'rows':rows,
 'operational_known_time_not_compared_or_proven':True})
js('NO_LOOKAHEAD_VALIDATION.json',{'replay_run_id':rid,'qualification':'BLOCKED_NO_LOOKAHEAD_PROOF',
 'checks':{
  'monotone_input_audit':{'status':'NOT_PROVEN_PER_EVENT','batch_bound':'PASS_RB_BIG_2160_ONLY'},
  'prefix_invariance_all_decision_state_changes':{'status':'NOT_PROVEN_NO_PRIMARY_EVENT_LEDGER'},
  'future_tail_deletion':{'status':'NOT_RUN_NO_PRIMARY_EVENT_LEDGER'},
  'future_tail_perturbation':{'status':'NOT_RUN_NO_PRIMARY_EVENT_LEDGER'},
  'instrumentation_neutrality':{'status':'PASS_FIXED_PREFIX_ONLY','scope':'rb/big 2160 bars 14 rows'},
  'formal_baseline_numeric_equality':{'status':'PASS_FROZEN_PREFIX_COMPARISON','rows_compared':620,'explicit_outside_prefix':1},
  'operational_known_time':{'status':'BLOCKED_NATIVE_EVENT_OBSERVATION_ABI_UNAVAILABLE'}},
 'production_no_lookahead_pass_claim':False,'future_leak_observed':None,
 'known_time_assigned_objects':0,'evaluation_tail_consumed':False})
js('FAILURE_INJECTION_RESULTS.json',{'replay_run_id':rid,'structural_tests':injections(),
 'scope':'独立validator约束测试，绝不代替未完成的生产无未来/生命周期实测',
 'real_package_false_qualification_injection':{'expected_rejection':'QUALIFIED_WITHOUT_OBSERVED_LEDGER',
     'execution':'independent_validator.py每次实测','not_a_production_no_lookahead_test':True}})
js('EXECUTION_ANALYSIS.json',{'replay_run_id':rid,'native_process_invocations':9,
 'initialization_failures':2,'successful_native_computations':7,'covered_symbol_scales':6,
 'recomputed_objects':524,'operational_known_objects':0,'observed_primary_event_lifecycle_rows':0,
 'first_failure_resolved_by':'TMPDIR within owned output',
 'second_failure_resolved_by':'owned PNV prefix route with exact payload equality to frozen consumed FAO',
 'aborted_python_temp_precheck':'stdout-empty assertion failed before creating an additional native process; preserved separately',
 'final_blocker':'EVENT_OBSERVATION_AND_PER_EVENT_INPUT_FRONTIER_NOT_EXPOSED',
 'algorithm_math_or_parameters_changed':False,'old_order_resumed':False})
m.update(exit='BLOCKED_NO_LOOKAHEAD_PROOF',native_process_invocations=9,successful_native_computations=7,
 native_task_initialization_count=9,remaining_symbol_scales=[],
 symbol_scale_status={s+'/'+r:'BATCH_RECOMPUTED_KNOWN_TIME_BLOCKED' for s in SYMS for r in ['big','mid']},
 native_recomputed_rows=524,observed_visibility_events=0,lifecycle_observations=0,
 qualification_for_professional=False,final_blocker='EVENT_OBSERVATION_AND_PER_EVENT_INPUT_FRONTIER_NOT_EXPOSED',
 stop_boundary='NO_ALTERNATIVE_CAUSALITY_DEFINITION_OR_NATIVE_REBUILD_IN_THIS_ORDER',
 evaluation_tail={'prepared':False,'consumed':False,'tests':'NOT_RUN_AFTER_NATIVE_OBSERVABILITY_GATE'},finished_at=NOW())
js('REPLAY_MANIFEST.json',m)
print(json.dumps({'exit':m['exit'],'native_calls':9,'successful_computations':7,'objects':524,
                  'baseline_matches':619,'explicit_out_of_prefix_rows':1,'operational_known_objects':0},ensure_ascii=False))
