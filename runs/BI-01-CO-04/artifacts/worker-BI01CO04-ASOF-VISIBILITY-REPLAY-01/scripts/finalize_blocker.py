"""依据本次真实失败生成B出口实物；从不生成特征或伪造观察。"""
from finite_probe import *
from independent_validator import injections

m=json.loads((OUT/'REPLAY_MANIFEST.json').read_text());rid=m['replay_run_id']
out=(OUT/'logs/native_engine.stdout').read_text();err=(OUT/'logs/native_engine.stderr').read_text()
trace=(OUT/'logs/native_engine.strace').read_text()
assert '开始运行 Frp 回测模型 ScaleTurnCalendar' in out
assert '/tmp: openTempFile: permission denied' in err
assert not list((OUT/'execution/cache').rglob('value1.__ts__.dba'))
js('EXECUTION_ANALYSIS.json',{
    'replay_run_id':rid,'process_returncode':0,'native_success':False,'task_initialization_entered':True,
    'completed_feature_outputs':0,'observed_visibility_events':0,'actual_market_reads_proven':False,
    'failure':'FIS_TEMPORARY_FILE_CREATE_DENIED_WITHIN_REQUIRED_WRITE_BOUNDARY',
    'failure_syscalls':[l for l in trace.splitlines() if 'EACCES' in l or 'EPERM' in l],
    'earlier_comment_correction':'完整落盘日志表明已进入参数初始化和模型调用，不是完全尚未进入任务。',
    'bootstrap_temp_check':{'python_check_executed':True,'engine_invocations':0,
                            'reason':'前置断言发现原stdout已有任务调用，立即停止；未重启引擎，TMPDIR效果未测试'},
    'prepared_max_input_bar_ts':'2021-09-30T15:00:00+08:00',
    'observed_max_input_bar_ts':None,'prepared_boundary_is_not_observed_read_boundary':True})
columns=['replay_run_id','symbol','scale','replay_event_seq','replay_event_ts','max_input_bar_ts',
         'max_input_source_row','input_prefix_hash','source_actual_uti','actual_bar_ts','actual_price',
         'source_confirm_uti','confirm_bar_ts','confirm_price','first_seen_at','last_seen_at','state_change_at',
         'present','withdrawn','reappeared','lifecycle_seq','state_hash','source_key','replay_object_key',
         'upstream_direction','direction_status','event_ts','canonical_bar_time','calendar_alternate_time',
         'mapping_conflict','state_status','prepared_input_prefix_hash','prepared_max_input_bar_ts','notes']
with (OUT/'VISIBILITY_LEDGER.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader()
    for sym in SYMS:
        raw_input=OLD/f'regenerated/market/{sym}_30m_warmup_through_20210930.csv'
        for scale in ['big','mid']:
            writer.writerow({'replay_run_id':rid,'symbol':sym,'scale':scale,
                'direction_status':'UNKNOWN_NO_REPLAY_OUTPUT',
                'state_status':'CALCULATION_FAILURE_BEFORE_OUTPUT' if (sym,scale)==('rb','big') else 'NOT_RUN_FIRST_BEARING_GATE_FAILED',
                'prepared_input_prefix_hash':sha(raw_input),
                'prepared_max_input_bar_ts':'2021-09-30T15:00:00+08:00',
                'notes':'覆盖/失败状态行，不是引擎事件；observed input/first-seen均未知'})
with (OUT/'OBJECT_LIFECYCLE_LEDGER.csv').open('w',newline='') as f:
    csv.DictWriter(f,fieldnames=columns).writeheader()
rows=[]
for sym in SYMS:
    for scale in ['big','mid']:
        for typ,path in [('formal_slice',OLD/f'copied/formal_slices/{sym}/gtqh_E_{scale}.csv'),
                         ('recovered_prefix',OLD/f'regenerated/objects/{sym}_{scale}_events_through_20210930.csv')]:
            for i,row in enumerate(csv.DictReader(path.open()),2):
                rows.append({'symbol':sym,'scale':scale,'baseline_class':typ,
                    'baseline_source_path':str(path.relative_to(REPO)), 'baseline_file_sha256':sha(path),
                    'baseline_physical_row':i,'baseline_fields':row,
                    'comparison_status':'NOT_COMPARABLE_NO_REPLAY_OUTPUT',
                    'after_decision_window_event':row.get('event_ts','')>'2021-09-30 15:00:00'})
assert len(rows)==620
js('FORMAL_BASELINE_COMPARISON.json',{'replay_run_id':rid,'baseline_commit':'dfdf843b47c03c0121fd7151b72f24adb5d986c0',
    'status':'BLOCKED_NO_REPLAY_OUTPUT_NOT_A_NUMERIC_MISMATCH_CLAIM','rows':rows,
    'formal_rows':96,'recovered_prefix_rows':524,'discarded_rows':0})
names=['monotone_input_audit','prefix_invariance_all_decision_state_changes','future_tail_deletion',
       'future_tail_perturbation','instrumentation_neutrality','formal_baseline_numeric_equality','operational_known_time']
proof={'replay_run_id':rid,'qualification':'BLOCKED_NO_LOOKAHEAD_PROOF',
       'checks':{n:{'status':'NOT_RUN_FIRST_BEARING_GATE_FAILED','reason':'原FIS初始化崩溃且未产生任何可见状态，不能把准备好的输入前缀冒充引擎实际读边界'} for n in names},
       'future_leak_observed':None,'production_no_lookahead_pass_claim':False,
       'all_symbols_and_scales_proven':False,'known_time_assigned_objects':0,'evaluation_tail_consumed':False}
js('NO_LOOKAHEAD_VALIDATION.json',proof)
js('FAILURE_INJECTION_RESULTS.json',{'replay_run_id':rid,'structural_tests':injections(),
    'scope':'生产引擎测试未通过；以下仅是独立validator的确定性正/负fixture检查',
    'real_package_false_qualification_injection':{'expected_rejection':'QUALIFIED_WITHOUT_OBSERVED_LEDGER',
        'execution':'independent_validator.py validate_package() 每次实测','not_a_production_test':True}})
m.update(exit='BLOCKED_NO_LOOKAHEAD_PROOF',native_numerical_task_start_count=1,
    native_process_invocations=1,additional_engine_invocations=0,observed_visibility_events=0,
    lifecycle_observations=0,qualification_for_professional=False,
    stop_boundary='FIRST_NATIVE_TASK_INITIALIZATION_FAILURE_NO_RESTART',
    parameter_equality_status='原task_params.params字节未改；仅app_dir/store及输入封装改变',
    evaluation_tail={'prepared':False,'consumed':False,'tests':'NOT_RUN_AFTER_FAILURE'},
    symbol_scale_status={sym+'/'+scale:('CALCULATION_FAILURE_BEFORE_OUTPUT' if (sym,scale)==('rb','big') else 'NOT_RUN_AFTER_HARD_GATE') for sym in SYMS for scale in ['big','mid']})
js('REPLAY_MANIFEST.json',m)
print(json.dumps({'exit':m['exit'],'replay_run_id':rid,'native_process_invocations':1,
                  'known_objects':0,'baseline_rows_retained':620,'structural_tests_passed':6},ensure_ascii=False))
