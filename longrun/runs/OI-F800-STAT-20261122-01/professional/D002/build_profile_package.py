"""把已完成的全量计算组织为锁定Skill原生输出，不执行诊断、调参或生产。"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from hashlib import sha256
import csv
import json

ROOT=Path(__file__).resolve().parent
P=ROOT/'profile'
RUN='OI-F800-STAT-20261122-01'
UNDER='daowei2026/observe-iterate@78b684ba6956f4c33a03b9167e846e3b741316a5:longrun/runs/'+RUN+'/professional/D001/FeatureUnderstandingPackage.json'
FRP='daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574:src/Frp/Instance/ISL/Opportunity/U2/'
SKILL='daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/feature-global-behavior-profiling/'
def load(name):return json.loads((ROOT/name).read_text())
def write(name,value):(ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def rows(name):
    with (P/(name+'.csv')).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def num(x):return float(x)
def intnum(x):return int(float(x))
S=load('profile/SUMMARY.json');checks=load('profile/STRUCTURAL_CHECKS.json')
B=load('FeatureRunResultBinding.json');ready=load('StatisticsInputReadiness.json')
defs=load('StatisticDefinitions.json')['statistics_definitions']
assert ready['binding_match']==dict(code_version='MATCH',parameter_version='MATCH',data_scope='CONFIRMED')
assert {c['check_id']:c['repeat_count'] for c in checks if c['repeat_count']}=={'coverage_flag_vs_continuous_input':22}
revs=rows('candidate_revisions');births=rows('candidate_births');turns=rows('scale_turns');life=rows('lifecycles')
cf=rows('violations_coverage_flag_vs_continuous_input');cfkeys={(r['life'],r['revision']) for r in cf}
byexact={(r['life'],r['revision']):r for r in revs}

def location(row):
    return dict(life=row['life'],revision=row['revision'],timestamp=row['timestamp'],known_uti=intnum(row['known']),
        parent_coordinates={k:row[k] for k in ['timestamp','occurrence','record_id','child_id_2']},
        symbols=row['symbols'].split('+'),table='occurrences',source='readback/tables/occurrences.csv')

finding_id='F800-GF-001'
representatives=[byexact[(cf[0]['life'],cf[0]['revision'])]]
day=next(r for r in cf if r['timestamp'][11:19]<'15:01:00')
representatives.append(byexact[(day['life'],day['revision'])])
pair=next(r for r in cf if r['symbols']=='hc+rb' and r['life']!=cf[0]['life'])
representatives.append(byexact[(pair['life'],pair['revision'])])
count=len(cf);lives=len({r['life'] for r in cf});tickcount=len({r['timestamp'] for r in cf})
observation=f'三对象公开KLine在[u-480000,u]均有效且整数UTI连续、正常入口Clock可用时，groupCoverageIncomplete仍为1；{count}个Revision occurrence、{lives}个Life、{tickcount}个发行时刻。'
finding=dict(finding_id=finding_id,finding_type='STRUCTURAL_FINDING_CANDIDATE',feature_ref=B['feature_name'],
    run_binding='FeatureRunResultBinding.json',reasonableness_unit_ref=UNDER+'#business_objects/BO3',business_object_ref=UNDER+'#business_objects/BO3',
    observation=observation,structural_invariant_ref=FRP+'GroupCandidateMaterial.hs#advanceMaterial/covered',
    evidence_scope=dict(scope=B['data_scope'],time_range=[min(r['timestamp'] for r in cf),max(r['timestamp'] for r in cf)],
        table='occurrences',source_fields=['groupCoverageIncomplete','groupKnownFrom','KLine.closeUti','KLine.close'],
        full_population_occurrences=S['candidate_revision_occurrences'],conditional_population_coverage_incomplete=S['coverage_incomplete_occurrences'],
        repeated_publication_ticks=tickcount,life_denominator=S['candidate_lives'],affected_lives=lives,
        affected_life_ratio=lives/S['candidate_lives'],conditional_affected_ratio=count/S['coverage_incomplete_occurrences']),
    repeat_count=count,affected_count=count,affected_ratio=count/S['candidate_revision_occurrences'],
    representative_locations=[location(r) for r in representatives],
    alternative_non_error_explanations=[
        '冷启动/未积累800Δ：另8个coverageIncomplete观点保留为未冲突；本finding的连续区间远早于u-480000，不适用冷启动解释',
        '真实缺价、Calendar断点或未知Clock：本对照逐品种检查有效价格/整数UTI，正常KLine adapter始终携带Clock；仍交诊断确认端到端语义',
        'groupCoverageIncomplete承诺的是不同覆盖域：若存在已冻结且不同于当前固定三对象窗口的正式合同，应提供反证；本Skill不改写预期'],
    current_confidence='HIGH：输入与公开标志重复冲突；只确认值得诊断，尚未确认实现根因或业务裁决',
    next_route='BUSINESS_DISCREPANCY_DIAGNOSIS',diagnosis_input_adapter_ref='DiagnosisInputAdapters.json#F800-DA-001')

control=next(r for r in revs if r['life']==cf[0]['life'] and r['coverage_incomplete']=='0')
cold=next(r for r in revs if r['coverage_incomplete']=='1' and (r['life'],r['revision']) not in cfkeys)
comparison=dict(comparison_id='F800-GC-001',scenario_id='GLOBAL_PROFILE',data_binding='FeatureRunResultBinding.json',
    time_basis='Asia/Shanghai原publication与groupKnownFrom；KLine整数closeUti，120UTI/开放分钟；逐个检查[u-480000,u]',
    parameter_version=B['parameter_version'],evidence_items=[
        dict(kind='全量输出',ref='profile/violations_coverage_flag_vs_continuous_input.csv',rows=count,lives=lives,ticks=tickcount),
        dict(kind='源输入边界',ref='INPUT_SCOPE_VALIDATION.json',rule='各品种5m UTI递增600；连续有效close重置断点，不将69个缺价行桥接'),
        dict(kind='清楚代表',location=location(representatives[0]),input_continuous_from={s:intnum(cf[0]['continuous_'+s]) for s in ['rb','hc','i']},
             required_from=intnum(cf[0]['required_from']),observed_flag=1),
        dict(kind='同Life未冲突对照',location=location(control),observed_flag=0),
        dict(kind='冷启动反例边界',location=location(cold),observed_flag=1,interpretation='输入历史不足800Δ，未列为冲突')],
    judgment='STRUCTURAL_CONFLICT_CANDIDATE：当前明确覆盖预期与22个正式观点冲突；根因、责任分类和修复方案均待Skill3')
adapter=dict(adapter_id='F800-DA-001',finding_id=finding_id,
    frozen_expectation=dict(expectation_id='F800-INV-COVERAGE-001',version='FRP@ac1927518ad6105f15ffbe37fea45e4be91ba574',
        statement='正常KLine固定rb/hc/i域、无未知Clock且三对象在[u-800Δ,u]有成功连续观测时，不应标记当前观察域不完整。',
        origin=[FRP+'GroupCandidateMaterial.hs#covered/incomplete',FRP+'GroupCandidateKLineInput.hs#buildKLineGroupSource',UNDER+'#processing_relations/R2'],
        applicable_conditions=['本正式参数实例与三对象固定域','正常KLine入口，无framePatches/未知Clock','全三对象有效close与整数UTI覆盖整个观察窗；不含冷启动或真实缺口'],
        falsifier_or_counterevidence=['指出所列窗口内某对象真实未观测/缺价/失知','提供预先存在、声明不同覆盖域或不同时间语义的有效合同','证明独立导出与实际生产输入并非同实例']),
    evidence_comparison_package=comparison,
    business_intent_ref=UNDER+'#business_objects/BO3',processing_chain_ref=UNDER+'#processing_relations/R2,R3',
    relevant_code_or_requirement_refs=[FRP+'GroupCandidateMaterial.hs',FRP+'GroupCandidateKLineInput.hs',FRP+'GroupCandidateEvolution.hs',
        'daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md#6,7'],
    data_binding_and_time_basis=dict(run_binding='FeatureRunResultBinding.json',parameter_version=B['parameter_version'],
        input_manifest='UPSTREAM_EXTRACTION.json',time_basis=comparison['time_basis'],code_version=B['code_version']))

def question(qid,pattern,why,visual,priority,locations):
    return dict(question_id=qid,finding_type='SCENARIO_INTERPRETATION_QUESTION',feature_ref=B['feature_name'],
        reasonableness_unit_ref=UNDER+'#business_objects/BO2,BO3',statistical_pattern=pattern,
        why_statistics_cannot_decide=why,recommended_visual_evidence=visual,representative_locations=locations,
        priority=priority,next_route='BUSINESS_EXPECTATION_DERIVATION')
unused=next(t for t in turns if t['symbol']=='i' and t['first_block_screen']=='REFERENCE_NO_OTHER_SYMBOL_WITHIN_2DELTA' and t['initial_anchor']=='False')
usedi=next(r for r in births if 'i' in r['symbols'].split('+') and r['direction']!='Unavailable')
long=max(births,key=lambda r:num(r['known'])-num(r['original_anchor']))
overlap=next(r for r in revs if r['observation']=='Subsumed')
late=next(r for r in births if r['timestamp'].startswith('2023'))
early=next(r for r in births if r['timestamp'].startswith('2021') and r['direction']!='Unavailable')
questions=[
 question('F800-SQ-001','i有1004个尺度位置，236个参加F（23.51%），rb为324/425（76.24%）、hc315/430（73.26%）；i未参加位置759个无其他品种actual≤2Δ邻点，9个近边被四坐标参考否决。',
    '独立筛查未发现合格非否决边完全不出组；但跨品种同步性是否符合“共同转折”的真实过程需要图上判断，不能把低参与率直接判成漏报。',
    ['三品种同尺度actual、confirm、selected知识轴与价格图','未参加i位置及邻域其他对象的真实过程，与已参加i位置对照','目标包含/排除场景应先冻结；当前未确认任何业务漏报'],
    'HIGH',[dict(symbol='i',turn_id=unused['turn_id'],actual_ts=unused['actual_ts'],known_ts=unused['known_ts']),location(usedi)]),
 question('F800-SQ-002','候选Life按知识年为244→162→74；每1000个输入位置Revision为47.41→31.16→14.74；同期尺度位置929→642→288。日/夜Revision密度30.81/31.71，开盘15分钟窗口50.91。',
    '上游活动自身下降、钟点分布与市场过程可能解释分层差异；统计没有稳定密度真值，也没有因少而直接判错的阈值。',
    ['2021密集段与2023稀疏段的同参数上游/候选图','日夜盘与开盘窗口按实际Calendar位置归一化，观察有无同一真实过程反复建组'],
    'MEDIUM',[location(early),location(late)]),
 question('F800-SQ-003','全部原观察窗4000开放分钟，修订尾30、交接尾90；首次准入actual年龄中位280、最大1665分钟；责任内峰值36个Life，469/480个组在旧6Δ期限之后才准入。',
    '800使延迟尺度转折有机会参加，但长责任期是否造成不需要的并行候选/迟到解释，不能靠组数增加或覆盖某延迟分位数裁决；K6仅参考筛查，未做第二个正式实例对比。',
    ['最长准入延迟与常见延迟位置对照的三品种价格、P/T/C、组责任边界','被支持严格超集覆盖的2/3成员组及共享成员桥','后续若要标定需先冻结保留、排除与holdout场景，不直接试值'],
    'HIGH',[location(long),location(overlap)]),
 question('F800-SQ-004','Supported1543、Incomplete3、Contradicted0；Withdrawn/EndedByScope0；3个初始化无方向锚点参加同一个Incomplete Life；所有真实选中位置几何confirm至selected均5开放分钟。',
    '当前正常KLine无修订patch和显式scopeEnded。零分支只是本实例未观察，不能证明分支不可达；初始化锚点是否需要在业务观察中弱化也缺少冻结预期。',
    ['冷启动三锚点及首次实际峰谷的同图对照','把样本中无适用输入的分支覆盖限制交给后续验证，不以零次数构造结构错误'],
    'MEDIUM',[location(cold)])]

cases=[]
def case(cid,source,row,reason):
    cases.append(dict(case_candidate_id=cid,source_finding_or_question_id=source,symbol=row['symbols'].split('+'),
        start_time=row['timestamp'],end_time=row['timestamp'],object_ids=[row['life'],row['revision']],
        related_events=[location(row)],selection_reason=reason,
        required_fields=['三对象KLine.close/closeUti','groupReference/groupCoverageIncomplete/groupKnownFrom','成员actual/confirm/known及准确上游来源','原观察/修订/交接边界'],
        candidate_only=True,context_request='后续依Calendar UTI扩展到至少[u-480000,u]或完整Life，当前不冻结正式场景'))
case('F800-CC-001',finding_id,representatives[0],'清楚三成员夜盘冲突；历史已充分，区分冷启动解释')
case('F800-CC-002',finding_id,control,'同Life此前flag=0，对照组身份与成员不变')
case('F800-CC-003',finding_id,cold,'真实历史不足窗口的flag=1对照，防止把所有标志都当冲突')
case('F800-CC-004',finding_id,representatives[1],'同一疑点跨日盘/夜盘，不以单一Session解释')
case('F800-CC-005','F800-SQ-001',usedi,'i已参加位置，和独立上游未出组位置比较')
cases.append(dict(case_candidate_id='F800-CC-006',source_finding_or_question_id='F800-SQ-001',symbol=['i'],
    start_time=unused['actual_ts'],end_time=unused['known_ts'],object_ids=[unused['turn_id']],related_events=[],
    selection_reason='从上游选未参加输出位置，不用F成员表反推覆盖；独立参考首阻断为无其他品种2Δ邻点',
    required_fields=['上游三品种尺度位置与真实价格','actual/confirm/selected知识轴','2Δ邻域及其他尺度过程'],candidate_only=True))
case('F800-CC-007','F800-SQ-002',early,'2021候选相对密集年份代表')
case('F800-CC-008','F800-SQ-002',late,'2023候选较少年份对照')
case('F800-CC-009','F800-SQ-003',long,'本样本最大准入actual年龄1665分钟边界，检验迟到解释')
case('F800-CC-010','F800-SQ-003',overlap,'Subsumed覆盖并行责任代表；不把覆盖标签当已退出')

profile=dict(profile_id='F800-GLOBAL-PROFILE-D002',feature_ref=B['feature_name'],run_binding='FeatureRunResultBinding.json',
    statistics_definitions=defs,candidate_profile=[],object_profile=[],event_profile=[],state_occupancy_profile=[],transition_profile=[],
    lifecycle_profile=[],branch_reachability_profile=[],density_profile=[],reason_profile=[],reference_integrity_profile=[],
    same_tick_order_profile=[],cross_symbol_profile=[],cross_period_profile=[],cross_session_profile=[],limits=ready['partial_items']+ready['not_exposed_items'])
def item(target,sid,stratum,value,n,den,source,notes=''):
    profile[target].append(dict(statistic_id=sid,stratum_id=stratum,value_or_distribution=value,sample_size=n,
        denominator_value=den,source_location=source,notes=notes))
counts=rows('counts_by_symbol');allc=next(x for x in counts if x['symbol']=='ALL_DISTINCT')
item('candidate_profile','ST01','ALL',dict(raw_positions=S['upstream_raw_positions'],initial_raw_anchors=3,
    scope='同参数Rct唯一posUTI1，非所有市场潜在转折'),S['upstream_raw_positions'],sum(f['tables'][0]['rows'] for f in load('UPSTREAM_EXTRACTION.json')['features'] if f['kind']=='rct'),'profile/raw_turns.csv')
item('candidate_profile','ST02','ALL',dict(scale_positions=S['upstream_scale_positions'],initial_anchors=3,noninitial=1856,used_positions=875,
    selected_to_used_ratio=875/1859,noninitial_used_ratio=872/1856,raw_to_selected_position_ratio=1859/10073),1859,1859,'profile/counts_by_symbol.csv; profile/scale_turns.csv',
    '含锚点总数与非初始化总数分别列出；F成员3472行是跨Revision关系，不是上游分母')
item('candidate_profile','ST14','ALL',dict(near_actual_pairs=648,positive_pairs=624,unresolved=3,veto=21,
    positive_joint_800=624,positive_joint_6_reference=16,eligible_nonveto_unseen=0),648,648,'profile/near_actual_pair_screen.csv',
    '近时pair为独立筛查，不是应输出真值；初始Unknown边保留为Unresolved；未确认业务漏报')
item('candidate_profile','ST15','SYMBOL',rows('first_block_reference_by_symbol'),1859,1859,'profile/first_block_reference_by_symbol.csv',
    '首阻断顺序是独立规则桶，native内部首阻断轨迹未暴露')
item('object_profile','ST03','ALL',dict(candidate_lives=480,revision_occurrences=1546,member_relations=3472,required_pairs=2306,
    unique_group_exact_violations=0,peak_responsibility_active_lives=36),480,480,'profile/SUMMARY.json; profile/candidate_births.csv')
item('object_profile','ST10','ALL',dict(reference_check_count=len([c for c in checks if 'integrity' in c['check_id'] or 'references' in c['check_id']]),violations=0),1546,1546,'profile/STRUCTURAL_CHECKS.json')
item('event_profile','ST04','ALL',dict(publication_events=1218,definition_only=1,candidate_revision_occurrences=1546,
    candidate_publication_events=1217,no_candidate_publication_input_positions=49683-1217),1218,49683,'profile/SUMMARY.json; readback/report.json',
    '一个发行事件可含多个候选观点；无候选occurrence不自动表示失败或无有效状态')
item('state_occupancy_profile','ST05','ALL',rows('state_occupancy'),1546,1546,'profile/state_occupancy.csv',
    'held_view_minutes仅已发表观点持有；末段截断于revisionEnd/样本末。无内部逐Tick trace')
item('transition_profile','ST06','ALL',rows('state_transitions'),1066,1066,'profile/state_transitions.csv',
    '相邻revision边数=1546-480；自环可反映关闭责任或关系变化，不自动视重复')
item('lifecycle_profile','ST07','ALL',dict(distributions=rows('lifecycle_distributions'),duty_closed_complete=479,right_censored=1,
    one_revision_lives=sum(intnum(x['revision_count'])==1 for x in life)),480,480,'profile/lifecycles.csv; profile/lifecycle_distributions.csv',
    '有限观察/修订责任，不是原始市场运动寿命；样本末尚未到r不假造End')
item('lifecycle_profile','ST13','SYMBOL',rows('latency_by_symbol'),1856,1856,'profile/latency_by_symbol.csv',
    'actual/几何confirm/selected三轴分开；几何confirm到selected均5开放分钟；非初始化1856个')
item('branch_reachability_profile','ST08','ALL',rows('branch_reachability'),1546,1546,'profile/branch_reachability.csv',
    '仅本完整实例是否观察到，零分支无适用输入证明，不形成不可达finding')
item('density_profile','ST12','ALL',dict(revisions_per_1000_input_positions=1546*1000/49683,
    publication_event_ratio=1218/49683,peak_responsibility_active_lives=36),1546,49683,'profile/SUMMARY.json',
    '以公共Calendar轴为分母；输入三对象行149049另列。当前发行远低于逐拍，不凭密度断言业务合理')
item('reason_profile','ST09','ALL',rows('required_reasons'),2306,2306,'profile/required_reasons.csv',
    'Required每观点重复为不同已发表断言；历史same pair不当独立业务对象累加')
for c in checks:
    item('reference_integrity_profile','ST16' if c['check_id']=='coverage_flag_vs_continuous_input' else 'ST10','ALL',c,
        c['denominator'],c['denominator'],'profile/violations_'+c['check_id']+'.csv; profile/STRUCTURAL_CHECKS.json',c['invariant'])
item('same_tick_order_profile','ST11','ALL',dict(same_life_same_tick_multiple_views=len(rows('same_tick_multiple_views')),
    previous_reference_edges=1066,previous_reference_violations=0),1546,1546,'profile/same_tick_multiple_views.csv; profile/violations_previous_reference_integrity.csv',
    '保留原坐标、引用及发生，不凭UUID大小或跨表行号猜业务顺序；跨Life同拍是合法批量')
cross=rows('cross_strata_comparison');statecross=rows('cross_strata_states');reasoncross=rows('cross_strata_reasons');heldcross=rows('cross_strata_held_view_time')
for target,dimensions in [('cross_symbol_profile',['SYMBOL']),('cross_period_profile',['YEAR']),('cross_session_profile',['SESSION','OPENING'])]:
    for cr in cross:
        if cr['dimension'] not in dimensions:continue
        layer=cr['stratum_id'];dimension=cr['dimension']
        bundle=dict(summary=cr,states=[x for x in statecross if x['dimension']==dimension and x['stratum_id']==layer],
            reasons=[x for x in reasoncross if x['dimension']==dimension and x['stratum_id']==layer],
            sampled_held_views=[x for x in heldcross if x['dimension']==dimension and x['stratum_id']==layer])
        if dimension=='SYMBOL':bundle['upstream_counts']=next(x for x in counts if x['symbol']==layer)
        if dimension=='YEAR':bundle['upstream_counts']=[x for x in rows('counts_by_symbol_year') if x['year']==layer]
        item(target,'ST17',dimension+':'+layer,bundle,intnum(cr['revision_occurrences']),intnum(cr['input_positions']),
            'profile/cross_strata_comparison.csv; profile/cross_strata_states.csv; profile/cross_strata_reasons.csv; profile/cross_strata_held_view_time.csv','品种含组可重叠；Life/跨度按创建层，观点按当次知识层；观点持有分时段拆分')
item('cross_period_profile','ST17','MONTH',rows('counts_by_month'),1546,49683,'profile/counts_by_month.csv')
item('cross_symbol_profile','ST17','DIRECTION',rows('counts_by_direction'),1859,1859,'profile/counts_by_direction.csv',
    '初始化Unknown与公开Unavailable同义；不能据此构造方向冲突')
gate=dict(status='DIAGNOSIS_REQUIRED',reasons=['F800-GF-001：22个正式观点/12个Life的覆盖标志与独立连续输入对照冲突；尚未进入或完成Skill3',
    '其余23项结构检查未观察到违例；所有可支持剖面已完成，不因单一finding中止全量统计'],
    valid_profile_ref='GlobalBehaviorProfile.json',next_action='manager消费本D002 Return，按原流程委派business-discrepancy-diagnosis处理F800-GF-001；若后续修改行为则重跑X/G。场景问题队列保留，当前不越过Gate做释放。')
write('GlobalBehaviorProfile.json',profile)
write('GlobalFindingCandidates.json',[finding]);write('ScenarioQuestionQueue.json',questions)
write('CandidateCaseIndex.json',cases);write('DiagnosisInputAdapters.json',[adapter]);write('GlobalProfileGate.json',gate)
result=dict(statistics_input_readiness=ready,global_behavior_profile=profile,global_finding_candidates=[finding],
    scenario_question_queue=questions,candidate_case_index=cases,diagnosis_input_adapters=[adapter],gate=gate)
write('FeatureGlobalBehaviorProfilingResult.json',result)
write('D001_GAP_RESOLUTION.json',dict(prior_package=UNDER,prior_package_unchanged=True,items=[
    dict(id='U1',status='RESOLVED_BY_X',evidence=['FeatureRunResultBinding.json','NATIVE_OUTPUT_MANIFEST.json','INPUT_SCOPE_VALIDATION.json']),
    dict(id='U2',status='RESOLVED_BY_X_ACTUAL_LOADING',evidence=['FRP_SOURCE_BINDING.json','TIS_SOURCE_RECHECK.json','NATIVE_PROCESS_OBSERVATION.json','PRODUCTION_RECONCILIATION.json'],
         note='复用已编译锁定引擎；未重新编译，实际正式进程与完整配置原生消费已验实'),
    dict(id='U3',status='UPSTREAM_DENOMINATORS_RESOLVED_NATIVE_INTERNAL_TRACE_NOT_EXPOSED',evidence=['UPSTREAM_EXTRACTION.json','profile/scale_turns.csv','StatisticsInputReadiness.json']),
    dict(id='U4',status='OLD_RESULT_REJECTED_NEW_EXACT_INSTANCE_PRODUCED',evidence=['FeatureRunResultBinding.json']),
    dict(id='U5',status='G_COMPLETE_REASONABLENESS_AND_FINDING_OPEN',evidence=['GlobalFindingCandidates.json','ScenarioQuestionQueue.json'],
         note='K800数量与延迟关系已实测；不等于标定通过，历史覆盖问题未宣布关闭'),
    dict(id='U6',status='RESOLVED_BY_WORKSPACE_PLATFORM_ROUTING_AND_REAL_FLOCK',evidence=['PLATFORM_STORAGE_BINDING.json','PRODUCTION_PROCESS.json','PRODUCTION_RECONCILIATION.json'])]))
write('WORKFLOW_COMPLETION.json',dict(skill=SKILL+'SKILL.md',steps=[
    dict(step='G1',completed=True,evidence=['StatisticsInputReadiness.json','FeatureRunResultBinding.json']),
    dict(step='G2',completed=True,evidence=['StatisticDefinitions.json','StratificationPlan.json']),
    dict(step='G3',completed=True,evidence=['GlobalBehaviorProfile.json','profile/SUMMARY.json']),
    dict(step='G4',completed=True,evidence=['profile/STRUCTURAL_CHECKS.json','GlobalFindingCandidates.json']),
    dict(step='G5',completed=True,evidence=['profile/cross_strata_comparison.csv','profile/cross_strata_states.csv','profile/cross_strata_reasons.csv','profile/cross_strata_held_view_time.csv']),
    dict(step='G6',completed=True,evidence=['GlobalFindingCandidates.json','ScenarioQuestionQueue.json']),
    dict(step='G7',completed=True,evidence=['DiagnosisInputAdapters.json','CandidateCaseIndex.json']),
    dict(step='G8',completed=True,evidence=['GlobalProfileGate.json'])],
    completed_at=datetime.now(timezone.utc).isoformat(),business_chain='同参数KLine→Rct原始位置→两轮ScaleTurn资格→当前材料/四坐标关系→候选Life/Revision→正式输出与形成参与',
    scope_complete='D002 X/G已完成本专业职责；不是父Run或FeatureRelease完成'))

def mdtable(data,cols):
    return '\n'.join(['| '+' | '.join(label for _,label in cols)+' |','| '+' | '.join('---' for _ in cols)+' |']+
        ['| '+' | '.join(str(row[k]) for k,_ in cols)+' |' for row in data])
counttable=mdtable(counts,[('symbol','品种/去重全局'),('raw_turn_positions','原始实际位置'),('scale_turn_positions','尺度位置'),('used_scale_turn_positions','参加F的位置'),('candidate_lives','候选Life'),('candidate_revision_occurrences','Revision occurrence')])
period=mdtable([r for r in rows('counts_by_symbol_year') if r['symbol']=='ALL_DISTINCT'],[('year','知识年'),('scale_turn_positions','尺度位置'),('used_scale_turn_positions','参加位置'),('candidate_lives','新建Life'),('candidate_revision_occurrences','观点')])
session=mdtable(rows('counts_by_session'),[('session','Session钟点'),('input_5m_positions','5m分母'),('candidate_lives','新建Life'),('revision_occurrences','观点'),('coverage_conflict_occurrences','覆盖冲突观点')])
report=f'''# D002｜F800 正式 X 与全量 G 专业报告

本次已完成准确实例的新生产、独立只读回读与原 Skill G1–G8。产出 **480 个候选 Life、1546 次候选 Revision occurrence**。`GlobalProfileGate=DIAGNOSIS_REQUIRED`：覆盖完整标志存在一项结构疑点，22 次观点涉及 12 个 Life，需交原 manager 委派偏差诊断。本报告不将 D002 完成交付扩大为 FeatureRelease 或父 Run 完成。

## 1. 版本、授权与正式 X

本 D 来源：`daowei2026/observe-iterate@d22655642b4e4dd8f9b1371cfce743164c7dbf6d:longrun/runs/{RUN}/delegations/D002/DELEGATION.json`。接收者仍为 E1，workers=[]，回原 manager。D001 已接收，本次只复核其关键入口哈希与未决输入，不重做完整理解。准确来源审计见 [SOURCE_AUDIT.json](SOURCE_AUDIT.json)。

仅生产 `CommonPriceTurnGroupCandidatesFrp`（make_features 的 f）。FRP `ac1927518ad6105f15ffbe37fea45e4be91ba574`；TIS `2f460d663d821cf2ba25555eda13e78b697d0767`。完整配置 [configuration.json](configuration.json) SHA-256 `{B['parameter_version']}`，与 D001 逐值、逐文件哈希一致。唯一业务 override 是 observation_multiple=800；delta=600、CalendarUTITick、method.revision=1；2Δ actual贴近仍为1200 UTI（10开放分钟）。

准确原候选目录无 fields.json；历史 F800 修改了 method.revision，不满足复用。故选择新生产，未拿历史目录冒充当前实例。平台用正常进程配置将 APP_DIR、store、日志和任务输出指向本工作区；SOF 原输入路径保持原配置，配置差异证据在 [PLATFORM_STORAGE_BINDING.json](PLATFORM_STORAGE_BINDING.json)。实际目录：

`{B['result_identity']['full_dir']}`

实际 ts PID **1712794**，可执行文件 SHA-256 `{B['actual_loading']['engine_sha256']}`。778 个相关 FRP 源文件与锁定提交一致；关键 TIS 6 文件再次对照已接收哈希一致。正式 Feature Python PID1712546，UTC {B['production']['started_at']} 至 {B['production']['finished_at']}，引擎日志总耗时约508.6秒。实际共享 flock 由 supervisor1712483 持有，独立进程争锁退出73证实排他；结果均写本Run独立store。证据见 [FRP_SOURCE_BINDING.json](FRP_SOURCE_BINDING.json)、[TIS_SOURCE_RECHECK.json](TIS_SOURCE_RECHECK.json)、[NATIVE_PROCESS_OBSERVATION.json](NATIVE_PROCESS_OBSERVATION.json)。

监控脚本最初按PID只记录一次，漏记同PID shell exec为ts，导致生产结束后监控收尾断言退出1。Feature Python已退出0、正式生产和公开读取成功；先前新鲜独立/proc快照已记录真实ts。执行过的脚本原样保留，修正版未再启动生产；[PRODUCTION_RECONCILIATION.json](PRODUCTION_RECONCILIATION.json)明确区分真实生产成功与监控失败。未伪造监控原记录或精确锁释放时刻。

由另一 Python 进程1720502只读加载准确结果，31张公开表行数、列、CSV SHA-256全部与生产后导出相同；to_df与occurrences一致。fields SHA-256 `{B['result_identity']['fields_sha256']}`。145个原生文件共13180182字节逐文件登记。所有1546个观点的原deadline-anchor均480000，原revisionEnd-deadline均3600：800已由原生引擎消费。见 [FeatureRunResultBinding.json](FeatureRunResultBinding.json)、[NATIVE_OUTPUT_MANIFEST.json](NATIVE_OUTPUT_MANIFEST.json)。

## 2. 范围与统计口径

请求 rb/hc/i、5m、2021-01-01至2023-12-31、night_end_at_2300、TA_updto20240229_DBA/steel。实际每品种49683行，首2021-01-04 09:05:00、末2023-12-29 15:00:00；三品种共149049输入行且时间轴相同。年分母16599/16530/16554；无重复或乱序，closeUti连续每步600。每品种69个非有限close仍计入日历位置，独立有效覆盖对照会断开。完整同参数KLine/Zig/Rct/ScaleTurn缓存均以OnlyRead取得，没有补算或运行Source、Q/V。见 [UPSTREAM_EXTRACTION.json](UPSTREAM_EXTRACTION.json)、[INPUT_SCOPE_VALIDATION.json](INPUT_SCOPE_VALIDATION.json)。

原生readiness为PARTIAL：核心版本、参数、范围、对象键可靠；未暴露逐Tick Dynamic、materialTotals及native首阻断轨迹。该限制不阻止完成已支持剖面。[StatisticDefinitions.json](StatisticDefinitions.json)登记17项口径，[StratificationPlan.json](StratificationPlan.json)声明品种、知识年/月、日夜盘和开盘窗口。Life数、Revision occurrence、发行事件、成员关系和上游位置分别计数；品种组数按包含关系，会重叠；全局Life去重。公共Calendar位置49683用于事件密度，149049输入行另列。原始位置含每品种一个初始化锚点；1859个尺度位置中非初始化1856，参加F的875个中非初始化872。

actual、几何confirm、selected原事件知识及F发表时间分别保留；成员T.pointKnownFrom是raw知识。UUID按uint64高低位精确解码，不转float；子表按完整父坐标归属，同刻保留occurrence/child坐标并以previous核序。无 occurrence 不当成失败。定义事件可单独发表。

## 3. 业务链分母、转化与潜在漏报筛查

{counttable}

全局原始位置10073、尺度位置1859（含3个锚点），875个尺度位置曾参加候选，比例47.07%；非初始化872/1856=46.98%。3472个成员子表行是跨观点的关系数，不能作尺度总分母。三品种候选包含数401/375/310之和大于480，原因是共同组本来跨品种。

全量独立建立648个跨品种actual距离≤2Δ近边：624个四坐标正向、3个初始化Unresolved、21个否决。624个正边全满足800首次共同可知期限，K6参考仅16个；480个Life中469个首次准入在旧6Δ期限之后。1859个尺度位置均在自身800窗口内首次可知；K6参考91个。K6是同输入期限参考筛查，不是额外正式生产，也不是“800已标定成功”的结论。

按独立规则筛查，rb未参加101个均无跨品种2Δ邻点；hc为114个无邻点、1个近边否决；i为759个无邻点、9个近边否决。当前未发现“合格非否决近边完全未进入任何候选”的位置，但这仍不是全部市场真值，更不能宣称无业务漏报。见 [profile/first_block_reference_by_symbol.csv](profile/first_block_reference_by_symbol.csv)、[profile/near_actual_pair_screen.csv](profile/near_actual_pair_screen.csv)。

## 4. 对象、事件、状态与有限责任

1218个公开发行事件，其中1个只有definitions，1217个含候选；一事件可含多个观点。1546观点/49683位置=每千位置31.117观点；责任内同时Life峰值36，当前没有接近逐拍发行的证据。对象准确身份、成员与上游actual/价格/confirm/known、原问题固定、期限不扩张、关闭不重开、责任关闭后不再更新、previous/overlap/coveredBy、admission/candidate/alternative exact及bridge、四坐标和2Δ等23项检查未见违例。初始化无方向在公开表称Unavailable，与参考Unknown对应，未错误列作冲突。

观察状态观点数：Open498、ClosedSupported805、ClosedInsufficient2、Subsumed241、Withdrawn0、EndedByScope0；局部Supported1543、Incomplete3、Contradicted0。Required2306条的verdict/gap/veto分布及分层见 [profile/required_reasons.csv](profile/required_reasons.csv)、[profile/cross_strata_reasons.csv](profile/cross_strata_reasons.csv)。零分支缺少适用输入证明，只作为覆盖限制。Subsumed与责任退出分别表达，未合并。

同Life相邻观点1066条转换，含Open→ClosedSupported398、Open→Subsumed80、Open→ClosedInsufficient1，以及同状态正文/责任变化；没有同Life同拍多观点或previous悬空。状态占用只按已发表观点持有区间计算，末段截断于修订终点或样本末；分年/Session占用另按公开5m位置拆分，不冒充内部逐Tick trace。

480个原观察窗全部4000开放分钟；修订尾30、交接尾90。首次准入actual年龄中位280、最大1665分钟；观察剩余责任中位3720分钟；已发表观点跨度中位3750分钟。479个Life末观点责任已关，1个样本末右删失；不把这些期限称为真实市场运动寿命。非初始化actual→selected中位rb280、hc270、i110分钟，几何confirm→selected均5开放分钟。见 [profile/lifecycles.csv](profile/lifecycles.csv)、[profile/latency_by_symbol.csv](profile/latency_by_symbol.csv)。

## 5. 分层比较

{period}

{session}

知识年Revision密度47.41→31.16→14.74/千输入位置，伴随上游尺度位置929→642→288。i参与比例低于rb/hc，未据此判错。日/夜密度30.81/31.71接近；开盘首15分钟钟点窗口为50.91/千位置，其他29.24；该窗口以真实Calendar行作分母，不臆测交易日归属。上/下方向分别227/252个Life，另1个初始化无方向Life。

各品种、年份、Session与开盘窗口的密度、出生责任跨度、右删失、状态/依据、Required reason、观点持有期、覆盖冲突率均另有全量对照，而非只报平均。参见 [profile/cross_strata_comparison.csv](profile/cross_strata_comparison.csv) 及同目录states/reasons/held_view_time；月度、actual年与知识年分别保留。没有可靠环境标签时未猜牛熊或波动市场阶段。

## 6. 结构疑点、场景问题与Gate

**F800-GF-001：覆盖完整标志冲突候选。** {observation} 范围2021-08-31 21:45至2021-09-15 21:25；占全部观点22/1546=1.423%、Life12/480=2.5%；在30个coverageIncomplete观点中占73.33%。分年全在2021；日盘7、夜盘15。另8个flag观点未满足完整历史条件，未列为冲突；没有把冷启动当异常。清楚代表Life `{cf[0]['life']}`，Revision `{cf[0]['revision']}`，2021-08-31 21:45，u=78643799，需要从78163799覆盖，而三品种有效连续输入均从72004199开始。该组同Life此前flag=0，成员身份和原问题未变。

这里只冻结已有覆盖合同与观测事实，不写根因、补丁、参数建议或宣称历史finding关闭。最强竞争解释和可证伪条件均在 [GlobalFindingCandidates.json](GlobalFindingCandidates.json)、[DiagnosisInputAdapters.json](DiagnosisInputAdapters.json) 中；全部22个准确位置可复现。

4项场景解释问题另列 [ScenarioQuestionQueue.json](ScenarioQuestionQueue.json)：i低参与和潜在漏报边界、跨年/Session密度、800带来的长责任与并行候选、零分支及初始化。10项 [CandidateCaseIndex.json](CandidateCaseIndex.json) 是最小区分候选（清楚反例、同Life对照、冷启动、日夜、上游未出组、跨年及延迟边界），不是已画图或冻结的正式场景集。

原生完整输出 [FeatureGlobalBehaviorProfilingResult.json](FeatureGlobalBehaviorProfilingResult.json)，独立组件 [GlobalBehaviorProfile.json](GlobalBehaviorProfile.json) 与 [GlobalProfileGate.json](GlobalProfileGate.json)。Gate为 **DIAGNOSIS_REQUIRED**，应由原manager按Skill3处理F800-GF-001；若后续处理改变行为，再按X/G重验。当前D002职责已完成，无生产或统计阻断；尚有专业诊断门槛，不宣称800业务合理、Feature已释放或父Run结束。

## 7. Owner七项进度与验收边界

1. D001：已由manager接收，本次未重做完整U；六项缺口的处置见 [D001_GAP_RESOLUTION.json](D001_GAP_RESOLUTION.json)。
2. X：已开始且验收完成，准确结果绑定及独立只读已形成。
3. 复用/生产：准确旧结果不合格，执行一次新生产；未因监控脚本失败重复生产。
4. 正式进程：真实ts1712794已运行并结束，Python成功；监控异常如实保留并核销证据。
5. 结果目录：上列本工作区D002/store准确实例；原生dba与上游输入CSV保留本地，记录分支发布31张F公开表CSV、全量统计、合同、脚本、定位与SHA-256。
6. G：已完成原Skill G1–G8，24项结构筛查、全部可支持剖面与分层已完成。
7. 阻断：本D无未完成生产/统计阻断；后续Gate为DIAGNOSIS_REQUIRED。该专业下一步交manager，不把它伪装成本executor仍持有的未完原D。

本轮未修改正式Feature代码或业务参数，未运行额外专业任务、未创建Worker、未向其他线程发消息。只更新本Run记录分支与Owner工作区。合法PRO_RETURN待专业产物先真实发布后，以该提交exact ref另行回交，不写未来自引用。
'''
(ROOT/'EXECUTOR_REPORT.md').write_text(report)
write('PROFILE_BUILD_AUDIT.json',dict(completed_at=datetime.now(timezone.utc).isoformat(),source='全量profile CSV，非抽样',
    source_summary_sha256=sha256((P/'SUMMARY.json').read_bytes()).hexdigest(),structural_candidates=1,scenario_questions=4,candidate_cases=10,
    diagnosis_adapters=1,profile_gate=gate['status'],profile_records={k:len(v) for k,v in profile.items() if isinstance(v,list)}))
print(json.dumps(dict(g_complete=True,gate=gate['status'],findings=1,questions=4,cases=10,adapters=1),ensure_ascii=False))
