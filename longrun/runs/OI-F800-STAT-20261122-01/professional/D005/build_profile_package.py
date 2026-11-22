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
old_prefix='daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/'+RUN+'/professional/D002/'
profile=dict(profile_id='F800-GLOBAL-PROFILE-D005-be57',feature_ref=B['feature_name'],run_binding='FeatureRunResultBinding.json',
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

native_retest=load('NATIVE_RETEST_API.json')
assert native_retest['completed'] and native_retest['total']==native_retest['passed']
closed=(native_retest['completed'] and C['all_upstream_equal'] and C['false_flag_retest_total']==22 and C['false_flag_retest_passed']==22 and
        C['cold_control_total']==C['cold_control_passed'] and S['coverage_conflict_occurrences']==0)
disposition=dict(finding_id='F800-GF-001',status='CLOSED_ON_LATEST_PROFILE' if closed else 'CONFIRMED',closed=closed,
    latest_run='FeatureRunResultBinding.json',latest_profile='GlobalBehaviorProfile.json',
    approved_proposal='F800-MP-001',adopted_frp=B['code_version']['frp'],
    prior_status='FIXED_PENDING_RERUN',prior_exact='daowei2026/observe-iterate@ba74086c56026dbc595af3b66e25334492b3a0b4:longrun/runs/'+RUN+'/professional/D004/FindingDisposition.json',
    retest=dict(false_flags=C['false_flag_retest_total'],false_flags_passed=C['false_flag_retest_passed'],cold_controls=C['cold_control_total'],cold_controls_passed=C['cold_control_passed'],
        full_population_conflicts=S['coverage_conflict_occurrences'],evidence='comparison/coverage_retest.csv',version_comparison='VersionComparison.json',native_api_retest='NATIVE_RETEST_API.json'),
    closure_basis='最新完整三年正式F、独立31表读回、全量G，按准确上游同一性复验原22位置与cold对照；不依赖局部回归。',
    release_decision='本D只关闭该finding并给原生GlobalProfileGate；FeatureReleaseGate/下游释放由原manager按CurrentReviewTarget继续。')
write('FindingDisposition.json',disposition)
findings=[];adapters=[]
for idx,c in enumerate(checks,1):
    if not c['repeat_count']:continue
    fid='F800-GF-001' if c['check_id']=='coverage_flag_vs_continuous_input' else 'F800-GF-002' if c['check_id']=='complete_flag_with_input_price_gap' else 'F800-GF-D005-'+c['check_id']
    aid='F800-DA-D005-'+c['check_id']
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
        window=load('MISSING_INPUT_WINDOW_VALIDATION.json')
        all_cases=rows('violations_complete_flag_with_input_price_gap')
        representatives=[all_cases[0],next(r for r in all_cases if r['timestamp'][11:19]<'15:01:00'),all_cases[-1]]
        by_exact={(r['life'],r['revision']):r for r in revs}
        finding['representative_locations']=[dict(**r,main_output_location=group_loc(by_exact[(r['life'],r['revision'])])) for r in representatives]
        finding['observation']=f"8个正式Revision、{window['affected_lives']}个Life、{window['publication_ticks']}个发行时刻标记groupCoverageIncomplete=0，但三品种[u-480000,u]观察窗内各有69行OHLC空值且volume=0；缺值范围2023-03-10 21:05至03-13 15:00，观点范围03-13 22:45至03-24 23:00。是否真实SourceFailure或正式Calendar豁免，待原Skill3核实。"
        finding['evidence_scope'].update(full_revision_population=len(revs),flag_zero_population=c['denominator'],
            affected_lives=window['affected_lives'],life_denominator=len(births),affected_life_ratio=window['affected_lives']/len(births),
            affected_publication_ticks=window['publication_ticks'],ratio_all_revision_occurrences=c['repeat_count']/len(revs),
            window_validation='MISSING_INPUT_WINDOW_VALIDATION.json',baseline_comparison='comparison/price_gap_baseline.csv',
            observation_preexisted_occurrences=C['price_gap_candidate_preexisted_occurrences'])
        finding['alternative_non_error_explanations']=[
            '公开表空值可能是重建/占位而非原生price事件真正失败；须核原生输入事件和实际读取合同。',
            '该69个Calendar位置可能有正式不适用/停市豁免；须提供已存在的Calendar/domain声明，不能在G临时放宽。',
            'coverage可能只承诺Calendar进展而非有效价格；须与现有Material缺价/失知断开及正常KLine覆盖语义核对。']
        finding['current_confidence']='HIGH 对照事实；尚未确认业务冲突根因、数据或实现责任。8/8在旧版同对象同知识时点也为0，本轮新识别，不宣称be57引入回归。'
        adapters[-1]['frozen_expectation'].update(expectation_id='F800-INV-COVERAGE-GAP-002',
            statement='正常KLine固定对象域若在[u-800Δ,u]存在非豁免实际缺价/SourceFailure/失知或真实未观察间隙，覆盖不能标记完整。公开OHLC空值是否满足该前件，必须先核事实与既有合同，不能由G临时定义。',
            origin=[c['evidence'],'CurrentFeatureUnderstandingPackage.json#intermediate_decisions/J4',
                'daowei2026/observe-iterate@ba74086c56026dbc595af3b66e25334492b3a0b4:longrun/runs/'+RUN+'/professional/D004/ContractAndDependencyImpact.json'],
            applicable_conditions=['本固定rb/hc/i、5m、night_end_at_2300及完整配置','缺价/失知属于实际Source失败或未观察，且无既定不适用豁免；此条件需先核实'],
            falsifier_or_counterevidence=['证明公开空值只是重建占位且真实源在各点有有效观测','提供已存在的Calendar或domain不适用豁免','提供预先存在且不同的coverage承诺，并解释其与现有缺价断开合同的关系'])
        adapters[-1]['evidence_comparison_package'].update(comparison_id='F800-GF-002-GLOBAL-COMPARE',
            evidence_items=[dict(kind='全量正式对照',ref='profile/violations_complete_flag_with_input_price_gap.csv',revision_occurrences=8,lives=window['affected_lives'],ticks=window['publication_ticks']),
                dict(kind='独立801行切片反核',ref='MISSING_INPUT_WINDOW_VALIDATION.json',windows=8*3,missing_ohlc_per_symbol=69),
                dict(kind='历史同事实',ref='comparison/price_gap_baseline.csv',old_flag_zero=C['price_gap_candidate_preexisted_occurrences'],meaning='新识别的既存候选，非已证实新增回归'),
                dict(kind='最小区分位置',locations=finding['representative_locations'])],
            judgment='STRUCTURAL_FINDING_CANDIDATE：正式完整标志与同窗公开OHLC空值并存；先核缺值/Calendar/覆盖合同，再定位责任，不在G提前写根因。')
        adapters[-1]['processing_chain_ref']='CurrentFeatureUnderstandingPackage.json#processing_relations/R1,R2'
        adapters[-1]['relevant_code_or_requirement_refs'] += [
            'daowei2026/frp@be57d6752c9d43d10f1d670e1d2993bb8153ea7c:src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs',
            'daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frpExample/STCalendar.py']
if not closed and not any(f['finding_id']=='F800-GF-001' for f in findings):
    raise RuntimeError('原finding复验条件未满足，须形成准确未决适配包，不允许自动通过')

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
        ['F800-GF-001已在最新完整X/G复验关闭；27项可支持结构检查无新反例。','剩余四项问题需要场景解释、真实过程对照或覆盖边界判断；统计通过不证明Feature全面合理。']),
    valid_profile_ref='GlobalBehaviorProfile.json',
    next_action=('原manager消费D005后，按原Workflow委派business-discrepancy-diagnosis；本D不修改正式行为。' if findings else
        '原manager消费D005，以最新U/X/G、finding和已知限制按CurrentReviewTarget处理FeatureReleaseGate/UpstreamReleasePackage；需场景时按原Workflow进入观察材料M与Skill1/2。本D不自动启动Q/V。'))
write('GlobalBehaviorProfile.json',profile);write('GlobalFindingCandidates.json',findings)
write('ScenarioQuestionQueue.json',questions);write('CandidateCaseIndex.json',cases);write('DiagnosisInputAdapters.json',adapters);write('GlobalProfileGate.json',gate)
write('FeatureGlobalBehaviorProfilingResult.json',dict(statistics_input_readiness=ready,global_behavior_profile=profile,
    global_finding_candidates=findings,scenario_question_queue=questions,candidate_case_index=cases,diagnosis_input_adapters=adapters,gate=gate))
write('D001_GAP_RESOLUTION.json',dict(prior_package=load('CurrentFeatureUnderstandingPackage.json')['current_applicability']['original_package_ref'],prior_package_unchanged=True,current_applicability='CurrentFeatureUnderstandingPackage.json',
    items=[dict(id='U1',status='RESOLVED_BY_LATEST_X',evidence=['FeatureRunResultBinding.json','INPUT_SCOPE_VALIDATION.json','NATIVE_OUTPUT_MANIFEST.json']),
    dict(id='U2',status='RESOLVED_BY_LATEST_ACTUAL_LOADING',evidence=['FRP_SOURCE_BINDING.json','TIS_SOURCE_RECHECK.json','NATIVE_PROCESS_OBSERVATION.json','PRODUCTION_PROCESS.json']),
    dict(id='U3',status='UPSTREAM_DENOMINATORS_RESOLVED_NATIVE_INTERNAL_TRACE_NOT_EXPOSED',evidence=['UPSTREAM_EXTRACTION.json','StatisticsInputReadiness.json']),
    dict(id='U4',status='OLD_CODE_RESULT_HISTORICAL_NEW_EXACT_INSTANCE_PRODUCED',evidence=['RESULT_REUSE_ASSESSMENT.json','FeatureRunResultBinding.json']),
    dict(id='U5',status='G_COMPLETE_ORIGINAL_FINDING_CLOSED_NEW_FINDING_DIAGNOSIS_REQUIRED',evidence=['FindingDisposition.json','GlobalFindingCandidates.json','DiagnosisInputAdapters.json','GlobalProfileGate.json','ScenarioQuestionQueue.json']),
    dict(id='U6',status='RESOLVED_BY_APPROVED_LOCAL_STORE_AND_REAL_FLOCK',evidence=['PLATFORM_STORAGE_BINDING.json','STORE_WRITER_AUDIT.json','PRODUCTION_PROCESS.json'])]))
workflow=[('G1',['StatisticsInputReadiness.json','CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json']),
    ('G2',['StatisticDefinitions.json','StratificationPlan.json']),('G3',['GlobalBehaviorProfile.json','profile/SUMMARY.json']),
    ('G4',['profile/STRUCTURAL_CHECKS.json','FindingDisposition.json','VersionComparison.json']),('G5',['profile/cross_strata_comparison.csv','profile/cross_strata_states.csv','profile/cross_strata_reasons.csv','profile/cross_strata_held_view_time.csv']),
    ('G6',['GlobalFindingCandidates.json','ScenarioQuestionQueue.json']),('G7',['DiagnosisInputAdapters.json','CandidateCaseIndex.json']),('G8',['GlobalProfileGate.json'])]
write('WORKFLOW_COMPLETION.json',dict(skill=SKILL+'SKILL.md',completed_at=now(),steps=[dict(step=s,completed=True,evidence=e) for s,e in workflow],
    business_chain='KLine→Rct实际位置→两轮ScaleTurn资格→当前材料/四坐标关系→候选Life/Revision→正式发行及下游exact/形成参与',
    scope_complete='D005完整新版本X、31表独立读回、G1-G8及原finding复验；不代父Run释放。'))
write('PROFILE_BUILD_AUDIT.json',dict(built_at=now(),source_binding='FeatureRunResultBinding.json',summary='profile/SUMMARY.json',
    current_understanding='CurrentFeatureUnderstandingPackage.json',new_structural_findings=len(findings),scenario_questions=len(questions),candidate_cases=len(cases),gate=gate['status']))
print(json.dumps(dict(gate=gate['status'],finding_status=disposition['status'],new_findings=len(findings),questions=len(questions),cases=len(cases)),ensure_ascii=False))
