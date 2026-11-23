"""复用绑定及必要增量统计口径；不再次OnlyRead/生产或执行既有G脚本。"""
from common import *
import os,csv
B=read_json(U,PREFIX+'/professional/D008/FeatureRunResultBinding.json')
UO=read_json(U,PREFIX+'/professional/D008/CurrentFeatureUnderstandingPackage.json')
assert B['code_version']['frp']=='daowei2026/frp@39f02ec4548e68ba8dbd30061afc870546000994'
assert B['code_version']['tis']=='daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767'
assert B['parameter_version']==UO['current_applicability']['parameter_version']=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
assert B['data_scope']['symbols']==['rb','hc','i'] and B['data_scope']['start_time']=='2021-01-01' and B['data_scope']['end_time']=='2023-12-31'
assert B['data_scope']['calendar']=='night_end_at_2300' and B['data_scope']['freq']=='5m'
assert Path(B['result_identity']['full_dir']).resolve().is_relative_to(BASE)
assert B['readback_validation']['all_31_tables_equal'] and B['readback_validation']['independent_process'] and B['readback_validation']['only_read']
sources=[]
names=['GlobalBehaviorProfile.json','StatisticsInputReadiness.json','StatisticDefinitions.json','StratificationPlan.json',
       'FindingDisposition.json','FindingRegister.json','GlobalProfileGate.json','UPSTREAM_EXTRACTION.json',
       'profile/SUMMARY.json','profile/STRUCTURAL_CHECKS.json','profile/candidate_births.csv',
       'profile/candidate_revisions.csv','profile/lifecycles.csv','profile/scale_turns.csv',
       'profile/near_actual_pair_screen.csv','profile/counts_by_symbol.csv','profile/counts_by_symbol_year.csv',
       'profile/cross_strata_comparison.csv','profile/cross_strata_states.csv','profile/cross_strata_reasons.csv',
       'profile/cross_strata_held_view_time.csv','profile/first_block_reference_by_symbol.csv',
       'profile/state_occupancy.csv','profile/state_transitions.csv','profile/branch_reachability.csv',
       'profile/required_reasons.csv','profile/lifecycle_distributions.csv','profile/latency_by_symbol.csv']
names+=['readback/tables/'+t['name']+'.csv' for t in B['run_result_tables']]
for name in names:
    raw=(D008/name).read_bytes();exact=git_bytes(U,PREFIX+'/professional/D008/'+name)
    assert raw==exact
    sources.append(dict(source_ref=pro_ref(name),local_path=str(D008/name),bytes=len(raw),sha256=sha(raw),exact_git_object_match=True))
for table in B['run_result_tables']:
    assert sha(Path(table['path']).read_bytes())==table['sha256']
    with Path(table['path']).open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f));assert len(rows)==table['rows']
assert len(B['run_result_tables'])==31
save('REUSE_EVIDENCE_READBACK.json',dict(verified_at=now(),binding_ref=pro_ref('FeatureRunResultBinding.json'),
    source_refs=sources,table_count=31,all_exact_bytes_match=True,new_public_reader_invoked=False,
    native_producer_invoked=False,prior_G_script_executed=False,
    boundary='对已有效结果及剖面做准确只读绑定核验；不是重新三年X、31表独立OnlyRead或既有G复跑。'))
save('CurrentReviewTarget.json',dict(current_goal='在D008当前正式F800全范围结果上完成覆盖面与高置信度并重的发现补充，先形成结果绑定队列，再按新Workflow逐个D。',
    professional_control_commit=LOCKED,source_ref=ref('4bf46f3fbe402915e3272e49a71dc94eac787c15',PREFIX+'/owner-decisions/CONTINUE-20261123/OWNER_CONTINUE.original.txt'),
    continuation_ref=ref(LOCKED,'task-inputs/wall-f-parallel-closure-20261122/F_CURRENT_RUN_CONTINUATION.md'),
    explicit_non_goals=['不重复有效U/X/D008 G/31表独立读回或S1/S2','不重诊GF001/002，除非新证据直接推翻闭环',
        '不在G提前LogicLocalization/根因诊断或讨论修法','不改变正式行为/参数/常量/数据处理/输出合同','不签FeatureRelease、不启动Q/V、不管理其他Run'],
    owner_raised_candidates=[dict(finding_id='F-LIFE-PEAK-CONCURRENCY',candidate_origin='OWNER_RAISED',status='CANDIDATE',must_assess_before_release=True,
        observation='旧剖面峰值责任内Life=36；需先核口径，不能预设active/历史累积/800根因/固定最大数/最终缺陷。')],
    required_regression_findings=['F800-GF-001','F800-GF-002'],regression_basis=pro_ref('FindingDisposition.json'),
    latest_owner_barrier='F独立继续；最新Campaign原文覆盖接续文件末尾旧WALL/F联合Barrier文字。',
    current_release_candidate_accepted=False))
defs=[]
def add(sid,name,unit,keys,basis,denom,fields,notes,strata):
    defs.append(dict(statistic_id=sid,name=name,business_item_ref=pro_ref('CurrentFeatureUnderstandingPackage.json')+'#business_objects/BO3',
        count_unit=unit,object_group_key=keys,time_basis=basis,denominator=denom,
        deduplication_rule='Life/exact及完整父坐标各自去重，不合并不同真实成员或不同原问题；UUID不是排序键。',
        same_tick_rule='同拍保留occurrence/record_id/child_id_2及previous；公开持有取同Life该拍最后准确观点。',
        strata=strata,source_fields=fields,notes=notes))
add('D015-ST01','旧责任内口径与边界/公开持有状态分列','Calendar位置上的Life数','准确实例+Life',
    'D008责任内闭区间[firstKnown,min(r,sampleEnd)]；另列[firstKnown,r)边界后责任投影；最新公开Open不作native active',
    '当前三品种共享49683个5m Calendar位置，不乘3',['profile/candidate_births.known/revision_end','candidate_revisions.known/observation/duty_closed','KLine closeUti/timestamp'],
    '复核Owner引述统计现象并登记可追溯峰值位置/并发分布；不建立可接受上限，不定位原因。',['ALL','YEAR','SESSION'])
add('D015-ST02','Life身份与成员/原问题的跨版稳定性','Life及原生Revision比较边','Life/完整成员Turn Life集合/原a,d,r',
    '同Life按公开父坐标和known序', '480个Life，1538个Revision；自然身份跨Life查询另列Life分母',
    ['occurrences.groupReference/originalAnchor/originalDeadline/originalRevisionEnd','groupMembers.memberTurn_referenceLife','groupMembers.memberObject'],
    '检查同Life换成员、同一准确成员+原问题重复Life；不同问题/不同Turn不自动相同。',['ALL','member_symbol_set'])
add('D015-ST03','已发行覆盖/重叠关系业务资格','关系边断言','完整父坐标+关系child_id_3',
    '关系时点已公开的源/目标观点；Known不超前；不恢复内部集合',
    '当前CoveredBy 242条、Overlaps 219条，各自分母',['groupCoveredBy','groupOverlaps','groupMembers.memberTurn_referenceLife','occurrences.anchor/deadline/revisionEnd/localBasis/observation'],
    '覆盖应有同问题的严格支持超集；重叠应共享具体Turn；不是仅检查目标UUID存在。',['relation_kind','YEAR'])
add('D015-ST04','当前业务链的转化/分层发现复核','上游位置、pair参考边、Life、publication分别列',
    '沿D008各ST定义保持原单位','原selected/publication知识年/Session；actual年另列',
    '复用10073原上游位置、1859已选、627合资格非否决参考边、480Life、49683Calendar位置，各层分母不互换',
    ['profile/counts_by_symbol','profile/first_block_reference_by_symbol','profile/near_actual_pair_screen','profile/cross_strata_comparison'],
    '复用原G计数与参考筛查，不重新全量枚举，不当业务真值/未暴露原生首阻断。',['SYMBOL','YEAR','SESSION','OPENING'])
save('IncrementalStatisticDefinitions.json',dict(prior_definitions_ref=pro_ref('StatisticDefinitions.json'),definitions=defs,
    registered_at=now(),registered_before_incremental_analysis=True,automatic_error_thresholds=[]))
save('RESOURCE_SCOPE.json',dict(observed_at=now(),pid=os.getpid(),cwd=str(Path.cwd().resolve()),authorized_workspace=str(BASE.resolve()),
    task_write_root=str(ROOT.resolve()),record_write_prefix=PREFIX,analysis_input_bytes=sum(s['bytes'] for s in sources),
    operation='只读已归档CSV/JSON和准确Git对象；写D015/本C记录',shared_cache_or_database_writes=False,
    native_feature_run=False,formal_production_lock_needed=False,
    policy_ref='/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/HEAVY_RESOURCE_POLICY.json',
    reason='当前仅无冲突统计；未取得也未声称持有正式生产锁，不执行会写共享生产面的进程。'))
save('StatisticsInputReadiness.json',dict(binding_match=dict(code_version='MATCH',parameter_version='MATCH',data_scope='CONFIRMED'),
    core_object_keys=['准确实例+Life','Life/Revision','timestamp/occurrence/record_id/child_id_2','成员Turn完整Life引用'],
    core_time_keys=['groupKnownFrom','publication timestamp','original/current anchor/deadline/revisionEnd','Calendar closeUti'],
    available_items=['当前1538公开观点/成员/Required/关系/参与表','完整D008上游/计数/分层/生命周期及结构检查','D00831表已独立读回及当前字节绑定'],
    partial_items=['由公开稀疏观点持有区间推得的采样状态，不是内部active轨迹'],
    not_exposed_items=['内部逐tick材料/枚举/首次阻断','原生连续coverage区间','未到达的撤回/Clock修订/scopeEnded适用输入'],
    data_quality_findings=[],readiness_status='PARTIAL',
    readiness_boundary='本G补充所需公开对象与计数可可靠分组，未公开部分不冒充已统计；不阻断发现补充。',
    feature_run_result_binding=pro_ref('FeatureRunResultBinding.json'),professional_control_commit=LOCKED,
    reused_readiness_ref=pro_ref('StatisticsInputReadiness.json'),verified_at=now()))
print(json.dumps(dict(reused_exact_files=len(sources),tables_verified=31,input_bytes=sum(s['bytes'] for s in sources),incremental_definitions=len(defs)),ensure_ascii=False))
