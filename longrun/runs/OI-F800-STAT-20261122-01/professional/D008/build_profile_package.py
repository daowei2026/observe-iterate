"""将本次完整X/G实测组织为原Skill原生合同，保留旧finding复验和场景问题。"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import json

ROOT=Path(__file__).resolve().parent
def load(n): return json.loads((ROOT/n).read_text())
def write(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rows(n,folder='profile'):
    with (ROOT/folder/(n+'.csv')).open(encoding='utf-8-sig',newline='') as f: return list(csv.DictReader(f))
def iv(x): return int(float(x))
def fv(x): return float(x)
def now(): return datetime.now(timezone.utc).isoformat()

B=load('FeatureRunResultBinding.json'); S=load('profile/SUMMARY.json'); C=load('VersionComparison.json')
ready=load('StatisticsInputReadiness.json'); checks=load('profile/STRUCTURAL_CHECKS.json')
assert ready['binding_match']==dict(code_version='MATCH',parameter_version='MATCH',data_scope='CONFIRMED')
defs=load('StatisticDefinitions.json')['statistics_definitions']
revs=rows('candidate_revisions');births=rows('candidate_births');turns=rows('scale_turns');lives=rows('lifecycles')
counts=rows('counts_by_symbol');near=rows('near_actual_pair_screen')
tablemeta=load('readback/report.json')['tables']
UNDER='CurrentFeatureUnderstandingPackage.json'
RUN='OI-F800-STAT-20261122-01'
SKILL='daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/feature-global-behavior-profiling/'
old_prefix='daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/'+RUN+'/professional/D005/'
profile=dict(profile_id='F800-GLOBAL-PROFILE-D008-39f',feature_ref=B['feature_name'],run_binding='FeatureRunResultBinding.json',
    statistics_definitions=defs,**{k:[] for k in ['candidate_profile','object_profile','event_profile','state_occupancy_profile',
    'transition_profile','lifecycle_profile','branch_reachability_profile','density_profile','reason_profile',
    'reference_integrity_profile','same_tick_order_profile','cross_symbol_profile','cross_period_profile','cross_session_profile']},
    limits=ready['partial_items']+ready['not_exposed_items'])
def item(target,sid,stratum,value,n,den,source,notes=''):
    profile[target].append(dict(statistic_id=sid,stratum_id=stratum,value_or_distribution=value,sample_size=n,
        denominator_value=den,source_location=source,notes=notes))
def group_loc(r):
    return dict(symbols=r['symbols'].split('+'),life=r['life'],revision=r['revision'],timestamp=r['timestamp'],
        known_uti=iv(r['known']),parent_coordinates={k:r[k] for k in ['timestamp','occurrence','record_id','child_id_2']},
        table='occurrences',source='readback/tables/occurrences.csv')

noninitial=[t for t in turns if t['initial_anchor']=='False']
used_noninitial=sum(t['used_by_f800']=='True' for t in noninitial)
item('candidate_profile','ST01','ALL',dict(raw_positions=S['upstream_raw_positions'],initial_raw_anchors=3),S['upstream_raw_positions'],S['upstream_raw_positions'],'profile/raw_turns.csv','Rct可识别实际位置，非全部潜在市场转折。')
item('candidate_profile','ST02','ALL',dict(scale_positions=len(turns),initial_anchors=S['initial_scale_anchors'],noninitial=len(noninitial),
    used_positions=S['used_distinct_scale_positions'],selected_to_used_ratio=S['used_distinct_scale_positions']/len(turns),
    used_noninitial=used_noninitial,noninitial_used_ratio=used_noninitial/len(noninitial)),len(turns),len(turns),'profile/scale_turns.csv; profile/counts_by_symbol.csv','成员子表行是跨Revision关系，不能当作上游分母。')
item('candidate_profile','ST14','ALL',dict(total=len(near),decision_counts=dict(Counter(r['decision'] for r in near)),
    positive_joint_eligible_800=S['positive_near_joint_eligible_800'],positive_joint_eligible_6_reference=S['positive_near_joint_eligible_6'],
    eligible_nonveto_unseen=S['potential_eligible_pairs_unseen']),len(near),len(near),'profile/near_actual_pair_screen.csv','独立候选与规则筛查，不是真值，不冒充native试探计数。')
item('candidate_profile','ST15','SYMBOL',rows('first_block_reference_by_symbol'),len(turns),len(turns),'profile/first_block_reference_by_symbol.csv','实际参加与参考首阻断分别标识。')
item('object_profile','ST03','ALL',dict(candidate_lives=S['candidate_lives'],revision_occurrences=S['candidate_revision_occurrences'],
    member_relations=tablemeta['occurrences_groupMembers']['rows'],required_pair_assertions=tablemeta['occurrences_groupRequired']['rows'],
    peak_responsibility_active_lives=S['peak_responsibility_active_lives']),S['candidate_lives'],S['candidate_lives'],'profile/candidate_births.csv; profile/SUMMARY.json')
item('event_profile','ST04','ALL',dict(publication_events=S['publication_events'],definition_only_publication_events=S['definition_only_publication_events'],
    candidate_revision_occurrences=len(revs),candidate_publication_events=len({(r['timestamp'],r['occurrence']) for r in revs})),S['publication_events'],S['input_5m_positions'],'readback/report.json; profile/SUMMARY.json','发行事件可含多个候选观点；无occurrence不等于失败。')
item('state_occupancy_profile','ST05','ALL',rows('state_occupancy'),len(revs),len(revs),'profile/state_occupancy.csv','公开观点知识区间持有，非内部逐Tick trace。')
item('transition_profile','ST06','ALL',rows('state_transitions'),len(revs)-len(births),len(revs)-len(births),'profile/state_transitions.csv','同Life相邻已发表观点；自环可来自关系或责任变化。')
item('lifecycle_profile','ST07','ALL',dict(distributions=rows('lifecycle_distributions'),duty_closed_last_lives=sum(iv(r['final_duty_closed']) for r in lives),
    right_censored_lives=S['right_censored_lives'],single_revision_lives=sum(iv(r['revision_count'])==1 for r in lives)),len(lives),len(lives),'profile/lifecycles.csv; profile/lifecycle_distributions.csv','有限形成/修订责任，非市场运动寿命。')
item('lifecycle_profile','ST13','SYMBOL',rows('latency_by_symbol'),len(noninitial),len(noninitial),'profile/latency_by_symbol.csv','actual/几何confirm/selected知识分开；初始化单列。')
item('branch_reachability_profile','ST08','ALL',rows('branch_reachability'),len(revs),len(revs),'profile/branch_reachability.csv','未发生分支先核有无适用输入；零次数不自动形成不可达finding。')
item('density_profile','ST12','ALL',dict(revisions_per_1000_input_positions=S['revision_events_per_1000_input_positions'],
    publication_event_ratio=S['publication_events']/S['input_5m_positions'],peak_responsibility_active_lives=S['peak_responsibility_active_lives']),len(revs),S['input_5m_positions'],'profile/SUMMARY.json','以共享Calendar轴为分母；三对象输入行另列，数量不直接判合理。')
item('reason_profile','ST09','ALL',rows('required_reasons'),tablemeta['occurrences_groupRequired']['rows'],tablemeta['occurrences_groupRequired']['rows'],'profile/required_reasons.csv','同pair跨Revision是多次已发表断言。')
for c in checks:
    item('reference_integrity_profile','ST16' if c['check_id'] in ('coverage_flag_vs_continuous_input','complete_flag_with_input_price_gap') else 'ST10','ALL',c,c['denominator'],c['denominator'],'profile/violations_'+c['check_id']+'.csv; profile/STRUCTURAL_CHECKS.json',c['invariant'])
item('same_tick_order_profile','ST11','ALL',dict(same_life_same_tick_multiple_views=len(rows('same_tick_multiple_views')),
    previous_edges=tablemeta['occurrences_groupPrevious']['rows'],complete_previous_chain=next(c for c in checks if c['check_id']=='complete_previous_chain')),len(revs),len(revs),'profile/same_tick_multiple_views.csv; profile/STRUCTURAL_CHECKS.json','同拍按实际坐标和previous准确引用，不按UUID大小排序。')
cross=rows('cross_strata_comparison');states=rows('cross_strata_states');reasons=rows('cross_strata_reasons');held=rows('cross_strata_held_view_time')
for target,dimensions in [('cross_symbol_profile',['SYMBOL']),('cross_period_profile',['YEAR']),('cross_session_profile',['SESSION','OPENING'])]:
    for r in cross:
        if r['dimension'] not in dimensions:continue
        dimension,layer=r['dimension'],r['stratum_id']
        bundle=dict(summary=r,states=[x for x in states if x['dimension']==dimension and x['stratum_id']==layer],
            reasons=[x for x in reasons if x['dimension']==dimension and x['stratum_id']==layer],sampled_held_views=[x for x in held if x['dimension']==dimension and x['stratum_id']==layer])
        if dimension=='SYMBOL':bundle['upstream_counts']=next(x for x in counts if x['symbol']==layer)
        if dimension=='YEAR':bundle['upstream_counts']=[x for x in rows('counts_by_symbol_year') if x['year']==layer]
        item(target,'ST17',dimension+':'+layer,bundle,iv(r['revision_occurrences']),iv(r['input_positions']),'profile/cross_strata_comparison.csv; profile/cross_strata_states.csv; profile/cross_strata_reasons.csv; profile/cross_strata_held_view_time.csv','Life及跨度按创建层，观点按当次知识层；持有时间按实际Calendar位置拆分，SYMBOL包含关系可重叠。')
item('cross_period_profile','ST17','MONTH',rows('counts_by_month'),len(revs),S['input_5m_positions'],'profile/counts_by_month.csv')
item('cross_symbol_profile','ST17','DIRECTION',rows('counts_by_direction'),len(turns),len(turns),'profile/counts_by_direction.csv','初始化Unknown与公开Unavailable对应。')

item('reference_integrity_profile','ST18','FULL_VERSION_COMPARISON',C,C['native_asof_comparisons'],C['native_asof_comparisons'],'VersionComparison.json; comparison/*.csv','各版UUID链独立核验；跨版自然Life对齐，只用于本次同输入对照。')

item('reference_integrity_profile','ST18','ORIGINAL_AC_BASELINE',load('InitialVersionComparison.json'),load('InitialVersionComparison.json')['native_asof_comparisons'],load('InitialVersionComparison.json')['native_asof_comparisons'],'InitialVersionComparison.json; comparison_ac/*.csv','原GF00122+8控制独立保留；当前原生身份/引用均按当前新X核。')
item('reference_integrity_profile','ST18','INPUT_MISSING_RETEST',load('MISSING_INPUT_WINDOW_VALIDATION.json'),load('MISSING_INPUT_WINDOW_VALIDATION.json')['original_view_count'],load('MISSING_INPUT_WINDOW_VALIDATION.json')['original_view_count'],'MISSING_INPUT_WINDOW_VALIDATION.json; comparison/gf002_retest.csv','原8观点自然Life/known及全部新published缺价窗均实测。')
native_retest=load('NATIVE_RETEST_API.json')
AC=load('InitialVersionComparison.json')
assert native_retest['completed'] and native_retest['total']==native_retest['passed']
check_by={c['check_id']:c for c in checks}
prior=[]
for fid,proposal,kind,total,comparison in [
    ('F800-GF-001','F800-MP-001','OLD_FALSE_FLAG',22,AC),
    ('F800-GF-002','F800-MP-002','OLD_PRICE_GAP_FLAG',8,C)]:
    targets=[r for r in native_retest['results'] if r['retest_kind']==kind]
    cold=[r for r in native_retest['results'] if r['retest_kind']=='OLD_COLD_START_CONTROL']
    violation='coverage_flag_vs_continuous_input' if fid=='F800-GF-001' else 'complete_flag_with_input_price_gap'
    ok=(len(targets)==total and all(r['passed'] for r in targets) and len(cold)==8 and all(r['passed'] for r in cold)
        and check_by[violation]['repeat_count']==0 and C['all_upstream_equal'] and AC['all_upstream_equal'])
    prior.append(dict(finding_id=fid,status='CLOSED_ON_LATEST_PROFILE' if ok else 'CONFIRMED',closed=ok,
        latest_run='FeatureRunResultBinding.json',latest_profile='GlobalBehaviorProfile.json',approved_proposal=proposal,
        adopted_frp=B['code_version']['frp'],prior_status='CLOSED_ON_D005' if fid=='F800-GF-001' else 'FIXED_PENDING_RERUN',
        prior_exact=('daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/'+RUN+'/professional/D005/FindingDisposition.json' if fid=='F800-GF-001' else
          'daowei2026/observe-iterate@08f5d8d4bd6982648fc93ce80b9cf843f183c8fd:longrun/runs/'+RUN+'/professional/D007/FindingDisposition.json'),
        retest=dict(original_positions=len(targets),passed=sum(r['passed'] for r in targets),cold_controls=len(cold),cold_passed=sum(r['passed'] for r in cold),
            full_population_conflicts=check_by[violation]['repeat_count'],full_population_denominator=check_by[violation]['denominator'],
            evidence='comparison_ac/coverage_retest.csv' if fid=='F800-GF-001' else 'comparison/gf002_retest.csv',
            native_api_retest='NATIVE_RETEST_API.json',whole_window_validation='MISSING_INPUT_WINDOW_VALIDATION.json' if fid=='F800-GF-002' else None),
        closure_basis='最新39f完整三年正式X、独立31表、完整G和原生Life/AsOf复验；历史基线同输入已核，实际新身份/发行/引用变化另全量比较。',
        release_decision='本D只给原生G与finding复验；FeatureReleaseGate/下游释放由原manager按CurrentReviewTarget继续。'))
closed=all(d['closed'] for d in prior)
disposition=dict(run_binding='FeatureRunResultBinding.json',findings=prior,all_prior_findings_closed=closed)
write('FindingDisposition.json',disposition)
findings=[];adapters=[]
for idx,c in enumerate(checks,1):
    if not c['repeat_count']:continue
    fid='F800-GF-001' if c['check_id']=='coverage_flag_vs_continuous_input' else 'F800-GF-002' if c['check_id']=='complete_flag_with_input_price_gap' else 'F800-GF-D008-'+c['check_id']
    aid='F800-DA-D008-'+c['check_id']
    finding=dict(finding_id=fid,finding_type='STRUCTURAL_FINDING_CANDIDATE',feature_ref=B['feature_name'],run_binding='FeatureRunResultBinding.json',
        reasonableness_unit_ref=UNDER+'#business_objects/BO3',business_object_ref=UNDER+'#business_objects/BO3',
        observation=c['invariant']+'；最新全量检查出现'+str(c['repeat_count'])+'项待诊断反例。',structural_invariant_ref=c['evidence'],
        evidence_scope=dict(data_scope=B['data_scope'],check_id=c['check_id'],source='profile/violations_'+c['check_id']+'.csv'),
        repeat_count=c['repeat_count'],affected_count=c['repeat_count'],affected_ratio=c['affected_ratio'],representative_locations=([c['examples'][0],c['examples'][-1]] if len(c['examples'])>1 else c['examples']),
        alternative_non_error_explanations=['核对独立筛查的适用输入、时间合同和未暴露内部状态；当前统计不提前写根因。'],
        current_confidence='结构疑点候选，进入既有偏差诊断核实',next_route='BUSINESS_DISCREPANCY_DIAGNOSIS',diagnosis_input_adapter_ref='DiagnosisInputAdapters.json#'+aid)
    findings.append(finding)
    adapters.append(dict(adapter_id=aid,finding_id=fid,
        frozen_expectation=dict(expectation_id=fid+'-INV',version=B['code_version']['frp'],statement=c['invariant'],origin=[c['evidence'],UNDER],
            applicable_conditions=[B['data_scope'],'本次完整配置与可读取公开结构合同'],falsifier_or_counterevidence=['证明反例不在规则适用范围','提供已存在的不同时间/身份合同或输入不匹配证据']),
        evidence_comparison_package=dict(comparison_id=fid+'-COMPARE',scenario_id='GLOBAL_PROFILE',data_binding='FeatureRunResultBinding.json',
            time_basis='原publication与Calendar UTI；120UTI/开放分钟',parameter_version=B['parameter_version'],evidence_items=[c],judgment='STRUCTURAL_FINDING_CANDIDATE'),
        business_intent_ref=UNDER+'#business_objects/BO3',processing_chain_ref=UNDER+'#processing_relations',relevant_code_or_requirement_refs=[c['evidence']],
        data_binding_and_time_basis=dict(binding='FeatureRunResultBinding.json',time_basis='publication知识轴与明确actual/confirm分别保留')))
    if fid=='F800-GF-002':
        frozen=json.loads((ROOT.parent/'D006/FrozenExpectation.json').read_text())
        adapters[-1]['frozen_expectation']=frozen
        adapters[-1]['prior_diagnosis_ref']='daowei2026/observe-iterate@46de903caa04be60a5600ef9f416445f5a6366cd:longrun/runs/'+RUN+'/professional/D006/DiagnosisReport.json'
        adapters[-1]['approved_fix_and_current_boundary_ref']='daowei2026/observe-iterate@08f5d8d4bd6982648fc93ce80b9cf843f183c8fd:longrun/runs/'+RUN+'/professional/D007/CurrentFeatureUnderstandingDelta.json'
for d in prior:
    if not d['closed'] and not any(f['finding_id']==d['finding_id'] for f in findings):
        raise RuntimeError(d['finding_id']+'原finding复验未满足，须补准确未决事实/适配，不允许自动通过')

def question(qid,pattern,why,visual,priority,locations):
    return dict(question_id=qid,finding_type='SCENARIO_INTERPRETATION_QUESTION',feature_ref=B['feature_name'],
        reasonableness_unit_ref=UNDER+'#business_objects/BO2,BO3',statistical_pattern=pattern,why_statistics_cannot_decide=why,
        recommended_visual_evidence=visual,representative_locations=locations,priority=priority,next_route='BUSINESS_EXPECTATION_DERIVATION',
        prior_question_ref=old_prefix+'ScenarioQuestionQueue.json#'+qid,status='SCENARIO_INTERPRETATION_REMAINS_OPEN',latest_binding='FeatureRunResultBinding.json')
unused=next(t for t in turns if t['symbol']=='i' and t['first_block_screen']=='REFERENCE_NO_OTHER_SYMBOL_WITHIN_2DELTA' and t['initial_anchor']=='False')
used_i=next(r for r in births if 'i' in r['symbols'].split('+') and r['direction']!='Unavailable')
early=next(r for r in births if r['timestamp'].startswith('2021') and r['direction']!='Unavailable')
late=next(r for r in births if r['timestamp'].startswith('2023'))
long=max(births,key=lambda r:fv(r['known'])-fv(r['original_anchor']))
overlap=next((r for r in revs if r['observation']=='Subsumed'),long)
cold=next((r for r in revs if iv(r['coverage_incomplete'])),births[0])
count_pattern='；'.join(r['symbol']+' '+r['used_scale_turn_positions']+'/'+r['scale_turn_positions']+' ('+format(fv(r['used_scale_ratio'])*100,'.2f')+'%)' for r in counts if r['symbol']!='ALL_DISTINCT')
years=[r for r in rows('counts_by_symbol_year') if r['symbol']=='ALL_DISTINCT']
year_pattern='；'.join(r['year']+'年 '+r['candidate_lives']+' Life/'+r['candidate_revision_occurrences']+' Revision，上游'+r['scale_turn_positions'] for r in years)
questions=[
 question('F800-SQ-001','最新选中尺度位置参加率：'+count_pattern+'。独立合格非否决边未出组候选='+str(S['potential_eligible_pairs_unseen'])+'。',
    '低参与率不能直接判漏报；共同转折的跨品种同步含义与市场过程需真实场景解释。',
    ['三品种同尺度价格与actual/几何confirm/selected知识轴','独立上游i未参加位置与已参加位置对照，先冻结包含/排除预期'],
    'HIGH',[dict(symbol='i',turn_id=unused['turn_id'],actual_ts=unused['actual_ts'],known_ts=unused['known_ts']),group_loc(used_i)]),
 question('F800-SQ-002',year_pattern+'；日夜/开盘密度和状态分层见最新cross_strata_comparison。',
    '上游活动变化可解释分层差异；没有数量或密度真值，不能由稀少或密集直接判错。',
    ['2021密集与2023稀疏段同参数上下游图','日夜及开盘按Calendar位置归一化后对照真实市场过程'],
    'MEDIUM',[group_loc(early),group_loc(late)]),
 question('F800-SQ-003','800Δ=4000开放分钟，修订尾30/交接尾90；峰值责任Life='+str(S['peak_responsibility_active_lives'])+'，旧6Δ之后首次准入='+str(S['candidate_births_after_legacy_6'])+'/'+str(len(births))+'，最大首次actual年龄='+str((fv(long['known'])-fv(long['original_anchor']))/120)+'开放分钟。',
    '800恢复延迟资格的统计事实不证明参数已合理；长责任/重叠候选是否有业务意义需场景过程与保留/排除预期。K6仅参考筛查，未生产第二实例。',
    ['最大迟到与常见迟到对照','2/3成员组的Subsumed及共享成员桥和责任边界'],
    'HIGH',[group_loc(long),group_loc(overlap)]),
 question('F800-SQ-004','最新状态/理由全分布见branch_reachability/required_reasons；初始化尺度锚点='+str(S['initial_scale_anchors'])+'，当前正常KLine无framePatches/scopeEnded适用输入。',
    '零分支不证明不可达；初始化无方向锚点在业务展示及场景解释中的作用还需冻结预期。',
    ['冷启动三锚点与首次实际峰谷对照','将缺少修订/失知适用输入的覆盖边界传递后继，不把零频次判成结构错误'],
    'MEDIUM',[group_loc(cold)])]
cases=[]
for q in questions:
    for idx,loc in enumerate(q['representative_locations'],1):
        cases.append(dict(case_candidate_id=q['question_id']+'-C'+str(idx),source_finding_or_question_id=q['question_id'],
            symbol=loc.get('symbols',[loc.get('symbol')]),start_time=loc.get('actual_ts',loc.get('timestamp')),end_time=loc.get('known_ts',loc.get('timestamp')),
            object_ids=[loc[k] for k in ('life','revision','turn_id') if k in loc],related_events=[loc],selection_reason=q['statistical_pattern'],
            required_fields=q['recommended_visual_evidence'],candidate_only=True,context_request='后续按准确Calendar扩展真实过程/完整责任窗；本索引不是图上正式选场景。'))

# 每个结构finding保留全量证据，再选能区分语义的最小位置，不替代正式场景。
for f in findings:
    for i,loc in enumerate(f['representative_locations'],1):
        cases.append(dict(case_candidate_id=f['finding_id']+'-C'+str(i),source_finding_or_question_id=f['finding_id'],
            symbol=loc.get('symbols','rb+hc+i').split('+'),start_time=loc.get('first_missing',loc.get('timestamp')),end_time=loc.get('timestamp'),
            object_ids=[loc[k] for k in ('life','revision') if k in loc],related_events=[loc],
            selection_reason='公开输入缺价与完整覆盖标志的清楚代表/时间边界对照；全量事实保留，不在G断言根因',
            required_fields=['三对象原始KLine OHLC/closeUti、真实事件存在性与数据/Calendar豁免合同','原生flag/knowledge/exact及覆盖定义'],
            candidate_only=True,context_request='原Skill3先核缺价含义、Source与Calendar/覆盖语义；需要真实场景再按原Workflow准备材料。'))

gate=dict(status='DIAGNOSIS_REQUIRED' if findings else 'PASS_TO_SCENARIO_REVIEW',
    reasons=([f['finding_id']+'：最新全量结构疑点待原Skill3诊断' for f in findings] if findings else
        ['F800-GF-001/002在最新39f完整X/G与原生AsOf复验关闭；'+str(len(checks))+'项可支持结构检查无新反例。','剩余四项问题需要场景解释、真实过程对照或覆盖边界判断；统计通过不证明Feature全面合理。']),
    valid_profile_ref='GlobalBehaviorProfile.json',
    next_action=('原manager消费D008后，按原Workflow委派business-discrepancy-diagnosis；本D不修改正式行为。' if findings else
        '原manager消费D008，以最新U/X/G、finding和已知限制按CurrentReviewTarget处理FeatureReleaseGate/UpstreamReleasePackage；需场景时按原Workflow进入观察材料M与Skill1/2。本D不自动启动Q/V。'))
write('FindingRegister.json',[dict(finding_id=d['finding_id'],observation='原覆盖标志确认问题',business_conflict='覆盖与实际输入责任窗冲突',direct_responsibility_stage='原D003/D006定位及D004/D007已批准修复；本D完整复验',confirmed_facts=d,competing_explanations='原诊断已确认，本D不重做根因判断',resolution_route=d['status'],resolution_status=d['status'],cross_effects_to_check=['VersionComparison.json','InitialVersionComparison.json']) for d in prior]+[dict(finding_id=f['finding_id'],observation=f['observation'],business_conflict=f['structural_invariant_ref'],direct_responsibility_stage='UNCONFIRMED，新疑点交原Skill3',confirmed_facts=f['evidence_scope'],competing_explanations=f['alternative_non_error_explanations'],resolution_route=f['next_route'],resolution_status='CANDIDATE',cross_effects_to_check='按原Workflow诊断后确认') for f in findings])
write('GlobalBehaviorProfile.json',profile);write('GlobalFindingCandidates.json',findings)
write('ScenarioQuestionQueue.json',questions);write('CandidateCaseIndex.json',cases);write('DiagnosisInputAdapters.json',adapters);write('GlobalProfileGate.json',gate)
write('FeatureGlobalBehaviorProfilingResult.json',dict(statistics_input_readiness=ready,global_behavior_profile=profile,
    global_finding_candidates=findings,scenario_question_queue=questions,candidate_case_index=cases,diagnosis_input_adapters=adapters,gate=gate))
write('D001_GAP_RESOLUTION.json',dict(prior_package=load('CurrentFeatureUnderstandingPackage.json')['current_applicability']['original_package_ref'],prior_package_unchanged=True,current_applicability='CurrentFeatureUnderstandingPackage.json',
    items=[dict(id='U1',status='RESOLVED_BY_LATEST_X',evidence=['FeatureRunResultBinding.json','INPUT_SCOPE_VALIDATION.json','NATIVE_OUTPUT_MANIFEST.json']),
    dict(id='U2',status='RESOLVED_BY_LATEST_ACTUAL_LOADING',evidence=['FRP_SOURCE_BINDING.json','TIS_SOURCE_RECHECK.json','NATIVE_PROCESS_OBSERVATION.json','PRODUCTION_PROCESS.json']),
    dict(id='U3',status='UPSTREAM_DENOMINATORS_RESOLVED_NATIVE_INTERNAL_TRACE_NOT_EXPOSED',evidence=['UPSTREAM_EXTRACTION.json','StatisticsInputReadiness.json']),
    dict(id='U4',status='OLD_CODE_RESULT_HISTORICAL_NEW_EXACT_INSTANCE_PRODUCED',evidence=['RESULT_REUSE_ASSESSMENT.json','FeatureRunResultBinding.json']),
    dict(id='U5',status='G_COMPLETE_FINDINGS_RETESTED_SEE_NATIVE_GATE',evidence=['FindingDisposition.json','GlobalFindingCandidates.json','DiagnosisInputAdapters.json','GlobalProfileGate.json','ScenarioQuestionQueue.json']),
    dict(id='U6',status='RESOLVED_BY_APPROVED_LOCAL_STORE_AND_REAL_FLOCK',evidence=['PLATFORM_STORAGE_BINDING.json','STORE_WRITER_AUDIT.json','PRODUCTION_PROCESS.json'])]))
workflow=[('G1',['StatisticsInputReadiness.json','CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json']),
    ('G2',['StatisticDefinitions.json','StratificationPlan.json']),('G3',['GlobalBehaviorProfile.json','profile/SUMMARY.json']),
    ('G4',['profile/STRUCTURAL_CHECKS.json','FindingDisposition.json','VersionComparison.json']),('G5',['profile/cross_strata_comparison.csv','profile/cross_strata_states.csv','profile/cross_strata_reasons.csv','profile/cross_strata_held_view_time.csv']),
    ('G6',['GlobalFindingCandidates.json','ScenarioQuestionQueue.json']),('G7',['DiagnosisInputAdapters.json','CandidateCaseIndex.json']),('G8',['GlobalProfileGate.json'])]
write('WORKFLOW_COMPLETION.json',dict(skill=SKILL+'SKILL.md',completed_at=now(),steps=[dict(step=s,completed=True,evidence=e) for s,e in workflow],
    business_chain='KLine→Rct实际位置→两轮ScaleTurn资格→当前材料/四坐标关系→候选Life/Revision→正式发行及下游exact/形成参与',
    scope_complete='D008完整新版本X、31表独立读回、G1-G8及原finding复验；不代父Run释放。'))
write('PROFILE_BUILD_AUDIT.json',dict(built_at=now(),source_binding='FeatureRunResultBinding.json',summary='profile/SUMMARY.json',
    current_understanding='CurrentFeatureUnderstandingPackage.json',new_structural_findings=len(findings),scenario_questions=len(questions),candidate_cases=len(cases),gate=gate['status']))
print(json.dumps(dict(gate=gate['status'],finding_status={d['finding_id']:d['status'] for d in prior},new_findings=len(findings),questions=len(questions),cases=len(cases)),ensure_ascii=False))
