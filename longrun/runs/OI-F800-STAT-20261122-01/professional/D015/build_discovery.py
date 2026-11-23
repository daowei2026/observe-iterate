"""按新原G合同形成发现说明、结果绑定队列、未升级观察及D适配；无诊断。"""
from common import *
from copy import deepcopy
import csv
def load(n):return json.loads((ROOT/n).read_text())
def prior(n):return read_json(U,PREFIX+'/professional/D008/'+n)
def csvrows(n):
    with (D008/'profile'/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
B=prior('FeatureRunResultBinding.json');old=prior('GlobalBehaviorProfile.json')
con=load('ConcurrencyProfile.json');semantic=load('IncrementalSemanticChecks.json');audit=load('SOURCE_REF_AUDIT.json')
binding=pro_ref('FeatureRunResultBinding.json');under=pro_ref('CurrentFeatureUnderstandingPackage.json')
owner=ref('4bf46f3fbe402915e3272e49a71dc94eac787c15',PREFIX+'/owner-decisions/CONTINUE-20261123/OWNER_CONTINUE.original.txt')
continuation=ref(LOCKED,'task-inputs/wall-f-parallel-closure-20261122/F_CURRENT_RUN_CONTINUATION.md')
code='daowei2026/frp@39f02ec4548e68ba8dbd30061afc870546000994:src/Frp/Instance/ISL/Opportunity/'
fid='F-LIFE-PEAK-CONCURRENCY';aid='F800-D015-DA-PEAK';qid='F800-D015-CURRENT-RESULT-QUEUE-v1'
time_basis=dict(calendar=B['data_scope']['calendar'],timezone='Asia/Shanghai',sampling='5m',
    unit='CalendarUTITick',ticks_per_open_minute=120,
    actual='原转折坐标',known='selected/publication知识轴；原始事件与payload坐标分开',
    responsibility='D008原闭区间[firstKnown,min(revisionEnd,sampleEnd)]',
    public_latest='同Life取<=u的最新原生观点；公开字段持有投影，不是内部active实测',
    peak_duration='60个5m位置的采样占用300开放分钟，非300分钟独立事件或墙钟持续')
peak=con['first_peak_public_aggregate'];source_summary=pro_ref('profile/SUMMARY.json')
concern='当前只有 rb、hc、i 三个品种；若这些 Life 表达当前仍有效或仍有业务维护意义的共同转折候选组，36 与该业务语义存在明显冲突风险。'
evidence=[
 dict(evidence_id='D015-PEAK-E1',source=source_summary,location='peak_responsibility_active_lives；ST12定义见原StatisticDefinitions',
    actual_time=None,confirm_time=con['first_peak_time'],evidence_status='SUPPORTS',
    observation='已接受D008正式G报告峰值36；本补充以相同责任闭区间在49683个Calendar位置复核为36。',
    interpretation='支持Owner引用的统计现象；旧字段名含active不构成内部active证明。',
    alternative_explanations=['有限责任内的不同历史实际问题可能同时存在','统计口径与业务有效性需要D核实'],
    data_quality='当前39f/完整参数/同一D008结果；非旧ac/be57或默认F6。'),
 dict(evidence_id='D015-PEAK-E2',source='ConcurrencyProfile.json',location='peak_runs/first_peak_other_metrics/incremental/concurrency_segments.csv',
    actual_time=None,confirm_time=con['first_peak_time'],evidence_status='SUPPORTS',
    observation='2021-11-10 14:25至2021-11-11 13:35，60个采样位置达到36；首次峰值含27 Open、9 Subsumed，36均Supported且公开dutyClosed=0。同期历史累计为211，闭/半开责任投影均36。',
    interpretation='并非只引用三年历史累计总量或一个孤立端点；值得诊断其维护语义。不是36个均应删除的证明。',
    alternative_explanations=['不同原actual问题/不同真实成员组合可产生合法并发','Subsumed可仍在修订责任内'],
    data_quality='原Calendar与稀疏公开观点的全范围采样；没有内部逐tick集合。'),
 dict(evidence_id='D015-PEAK-E3',source='IncrementalSemanticChecks.json',location='same_life_member_identity_stability/duplicate_natural_candidate_identity',
    actual_time=None,confirm_time=None,evidence_status='SUPPORTS',
    observation='480 Life跨1538观点的成员身份稳定；同完整成员身份+原a/d/r的跨Life重复为0；CoveredBy242及Overlaps219语义补查均0冲突。',
    interpretation='当前公开结构没有直接证明重复Life/身份漂移；这不能替代Owner并发业务意义判断或关闭候选。',
    alternative_explanations=['大量互不等价的有限问题可能合法','不重复仍可能业务维护不合宜；需D核实'],data_quality='完整Turn引用和父坐标，无UUID浮点转换。'),
 dict(evidence_id='D015-PEAK-E4',source=under,location='BO3/ST4/J5及unconfirmed_items',actual_time=None,confirm_time=None,
    evidence_status='MISSING',observation='公开latest/Open/duty字段不是CandidateState内部active逐tick轨迹；本G没有取完整36Life逐项责任定位。',
    interpretation='D须先LogicLocalization，厘清口径并核峰值全部Life、对账与责任逻辑；当前不确认根因。',
    alternative_explanations=['内部活跃集合与责任投影可能一致或有不同持有语义，不能据名称猜测'],data_quality='公开可读部分充分形成候选，内部事实及最终业务判断未完成。')]
candidate=dict(finding_id=fid,finding_type='HIGH_CONFIDENCE_REASONABLENESS_CANDIDATE',candidate_origin='OWNER_RAISED',
    status='CANDIDATE',feature_ref=B['code_version'],run_binding=binding,reasonableness_unit_ref=under+'#business_objects/BO3',
    business_object_ref=under+'#business_objects/BO3',observation='当前正式结果峰值责任内36 Life，连续60个5m采样位置；首次峰27 Open+9 Subsumed且公开duty均开放。',
    candidate_basis='Owner明确要求释放前评估；当前全范围事实支持该并发现象及公开责任开放，值得进入D，而非仅有一个大数。',
    why_high_confidence='对“需要进入责任逻辑和维护语义判断”的置信高：有同结果全轴复核、持续采样、当前公开状态分解和明确Owner业务关切；历史累计211与责任内36分开。三品种下大量并发维护的业务解释需要证据，不能仅用结构检查无冲突替代。',
    confidence_limits=['current_confidence保持OWNER_CONCERN，非确认代码缺陷；36不是预设上限或自动判错阈值。',
        '60个位置属于一个连续峰值区间，不是60个独立市场失败；公开Open/duty不自动等于业务active/有用。',
        '峰值有27个不同actual锚点、22个两成员/14个三成员解释，支持多问题并发的竞争解释，尚未排除。',
        '不预设历史累积/800根因，不在本G讨论修法；D须逐Life对账并定位最早责任逻辑。'],
    contract_or_business_semantics_ref=[owner+'#四、Owner指定候选',continuation+'#4.2',under+'#business_objects/BO3',under+'#states/ST4'],
    evidence_scope=dict(data_scope=B['data_scope'],source_summary=source_summary,increment='ConcurrencyProfile.json',
        count_unit='repeat_count=峰值采样位置；affected_count=首次峰值Life；affected_ratio=峰值采样位置/全Calendar位置，非缺陷率'),
    repeat_count=con['peak_sample_positions'],affected_count=peak['life_count'],affected_ratio=con['peak_sample_positions']/49683,
    representative_locations=con['representative_locations'],alternative_non_error_explanations=[
        '不同actual问题和不同Turn组合允许并发，三品种不天然规定Life数上限。',
        'Subsumed、观察关闭、修订责任开放、历史发表分别有不同语义。',
        '当前引用统计可能与业务active口径不同；须D确认是否仅需B修正口径。'],
    current_confidence='OWNER_CONCERN',statistical_observation_confidence='HIGH',defect_conclusion='UNDETERMINED',
    owner_assessment_status='PROMOTED',must_assess_before_release=True,next_route='BUSINESS_DISCREPANCY_DIAGNOSIS',
    diagnosis_input_adapter_ref='DiagnosisInputAdapters.json#'+aid,logic_localization_ref=None)
findings=[candidate]
# 若增量公开语义检查出现冲突，应另形成候选而非被Owner首候选掩盖；当前实测为0。
assert all(c['repeat_count']==0 for c in semantic['checks'])
adapter=dict(adapter_id=aid,finding_id=fid,
    frozen_expectation=dict(expectation_id=fid+'-OWNER-CONCERN-v1',version=LOCKED,statement=concern,origin='OWNER_RAISED',
        owner_source_ref=owner,applicable_conditions=['只有在36表达仍有效或有维护意义的共同转折候选时，该Owner业务关切成立；先核实际口径。'],
        falsifier_or_counterevidence=['D证明统计/绑定口径误差并完成B及G更新','D逐Life证明互不等价且业务上合理，说明各组区别后可REJECTED_AS_NON_ISSUE'],
        boundary='这里冻结Owner条件式关切；没有发明三品种固定Life数上限。'),
    evidence_comparison_package=dict(comparison_id='D015-PEAK-ECP',scenario_id='GLOBAL_PROFILE',business_intent=concern,
        expectation_id=fid+'-OWNER-CONCERN-v1',expectation_version=LOCKED,data_binding=binding,time_basis=time_basis,
        parameter_version=B['parameter_version'],evidence_items=evidence,
        judgment='DIAGNOSIS_REQUIRED：统计观察已确认且Owner必评；业务冲突/根因/处理类型未确定。',
        applicability_boundary='当前39f完整D008结果及本G公开投影；不以数量判错，不替代D。',
        confidence=dict(statistical_observation='HIGH',business_defect='UNDETERMINED'),next_action='先LogicLocalization，再决定M/B/关闭或未决。'),
    business_intent_ref=owner,processing_chain_ref=under+'#processing_relations/R2,R3,R4',
    relevant_code_or_requirement_refs=[owner,continuation,pro_ref('FRP_SOURCE_BINDING.json'),
        code+'U2/GroupCandidateEvolution.hs',code+'U2/GroupCandidateDecisions.hs'],
    relevant_ref_role='相关处理链及版本索引，尚未作为责任代码定位；本G未查源码根因。',
    data_binding_and_time_basis=dict(feature_run_result_binding=binding,parameter_version=B['parameter_version'],time_basis=time_basis,
        current_professional_control_commit=LOCKED,readiness='StatisticsInputReadiness.json',calendar_source='CALENDAR_SOURCE_READBACK.json'),
    required_diagnostic_order='按Owner第五节/接续输入§5及原D Skill先LogicLocalization；完整36Life及源码责任点留D执行。',
    owner_required_D_scope_ref=owner+'#五、候选进入D后的要求',diagnosis_performed=False)
save('GlobalFindingCandidates.json',dict(candidates=findings,run_binding=binding,professional_control_commit=LOCKED))
save('DiagnosisInputAdapters.json',dict(adapters=[adapter],current_result_binding=binding,root_cause_localization_performed=False))
case=dict(case_candidate_id='D015-PEAK-INDEX-001',source_finding_id=fid,symbol=['rb','hc','i'],
    start_time=con['peak_runs'][0]['start_time'],end_time=con['peak_runs'][0]['last_sample_time'],
    object_ids=[r['life'] for r in con['representative_locations']],
    related_events=con['representative_locations'],selection_reason='Owner必评峰值的完整采样区间与最早/最晚准入代表定位入口；不是S1场景，D仍需取全部36Life。',
    required_fields=['完整Life/Revision/父坐标','峰时全部36Life及成员actual/known/age/最新观点/expiry/状态','create/revision/end/current口径与身份对账','统计/责任规则与准确源码配置'],
    full_peak_roster_not_substituted_by_representatives=True)
save('CandidateCaseIndex.json',dict(cases=[case],automatic_scenario_workflow_started=False))

obs=[]
def observation(oid,text,refs,why,revisit):
    obs.append(dict(observation_id=oid,feature_ref=B['code_version'],run_binding=binding,observation=text,
        evidence_refs=refs,why_not_promoted=why,revisit_condition=revisit,status='OBSERVATION_NOT_PROMOTED'))
observation('D015-O01-SELECTED-CONVERSION','i已选1004、参加236；rb324/425、hc315/430。独立参考筛查中i759无2Δ内其他对象、9关系否决；627合资格非否决参考边未见缺组。',
    [pro_ref('profile/counts_by_symbol.csv'),pro_ref('profile/first_block_reference_by_symbol.csv'),pro_ref('profile/STRUCTURAL_CHECKS.json')],
    '共同对象不承诺每个单品种转折有组；分母和参考筛查可解释当前差异，没有已确认应入而未入的业务反例。参考不是原生首阻断/全市场真值。',
    '新证据给出当前资格成立且应入组的具体原上游对象，或参考筛查适用/绑定被推翻。')
observation('D015-O02-PERIOD-SESSION-DENSITY','2021/2022/2023首次Life=244/162/74，Revision/千位置=46.69/31.16/14.98；日夜约30.72/31.41，开盘50.91高于其余29.07。',
    [pro_ref('profile/cross_strata_comparison.csv'),pro_ref('profile/counts_by_symbol_year.csv')],
    '分母为各层真实Calendar位置；上游活动和知识节奏不同，没有数量配额或环境真值，不能将分层差异自动判错。',
    '差异与可靠业务资格/事件缺失或身份冲突联结，形成明确而可复核的业务矛盾。')
observation('D015-O03-LATE-ADMISSION','469/480 Life首次准入晚于旧6Δ参考，最大准入actual年龄1665开放分钟；800对应4000开放分钟，原责任、修订尾30和handoff尾90分列。',
    [pro_ref('profile/SUMMARY.json'),pro_ref('profile/lifecycle_distributions.csv'),pro_ref('profile/latency_by_symbol.csv')],
    '旧6Δ不是当前业务真值，晚知道不自动否定历史共同峰，也不证明800有用；缺下游效用/可用延迟判据。该观察不关闭并发Owner候选。',
    'Owner给定效用目标或出现已知/实际轴冲突及明确应保留/排除事实时重新评估。')
observation('D015-O04-RELATION-MULTIPLICITY','全量CoveredBy242、Overlaps219；本补充严格超集/同问题/支持及共享具体Turn检查无冲突。首次峰36含22两成员、14三成员、27个actual锚点。',
    ['IncrementalSemanticChecks.json','ConcurrencyProfile.json',under+'#processing_relations/R4'],
    '候选组合/责任问题数与独立市场峰谷数不同，结构关系有合法解释，未见同完整自然身份重复；并发业务维护意义仍由F-LIFE-PEAK-CONCURRENCY独立诊断，不因此关闭。',
    '出现同准确身份重复、无共享Turn重叠、非严格超集覆盖或D确认无业务维护意义。')
observation('D015-O05-LIFECYCLE-AND-SELF-TRANSITIONS','480 Life中479最终duty关闭，1样本末右删失；ClosedSupported→ClosedSupported 407条，Subsumed→Subsumed162条，原G无责任关闭后更新或closed重开。',
    [pro_ref('profile/lifecycles.csv'),pro_ref('profile/state_transitions.csv'),pro_ref('profile/STRUCTURAL_CHECKS.json')],
    '状态标签自环可包含责任/关系/覆盖变化；观察终止不等于修订责任终止。右删失不当未正常结束，不能仅凭标签自环判多余发行。',
    '出现完全无业务正文/决定变化的重复发行证据、终结后更新或样本末以后应结束仍未结束的实际事实。')
observation('D015-O06-REACHABILITY','Supported1535/1538、Incomplete3；Contradicted/Withdrawn/EndedByScope未在本实例观察。初始不足方向/类型/Bend各9条Required未决，未被零值填充。',
    [pro_ref('profile/branch_reachability.csv'),pro_ref('profile/required_reasons.csv'),under+'#occurrences'],
    '正常KLine路径没有framePatches/scopeEnded适用输入，零次数不证明分支无用或逻辑不可达。Supported也不等于全窗coverage或业务机会正确。',
    '新的真实适用输入出现但相应分支/理由仍缺失，或不足被无证据提升。')
observation('D015-O07-PUBLICATION-DENSITY','1538 Revision occurrence、1217 publication（含1定义专用），30.956 Revision/千共享Calendar位置；多组观点可共享一次publication。',
    [source_summary,pro_ref('FeatureRunResultBinding.json'),pro_ref('profile/STRUCTURAL_CHECKS.json')],
    '事件包装、Revision和Life是不同计数单位，当前全局密度不是逐Tick发射；27项原结构/引用/顺序检查均0冲突，无正式载体不自洽的新事实。',
    '给出同对象同刻不同载体相互冲突、非法顺序或无意义逐拍发行的准确反例。')
observation('D015-O08-COVERAGE-REGRESSION','当前coverageIncomplete16观点/12Life；完整标记1522观点；GF001/002在当前正式结果保持CLOSED_ON_LATEST_PROFILE。',
    [pro_ref('FindingDisposition.json'),pro_ref('profile/STRUCTURAL_CHECKS.json'),pro_ref('GlobalBehaviorProfile.json')],
    '当前原G双向缺价/连续输入对照冲突为0；不足标志与局部依据分别表达。没有新证据推翻已批准修复和当前闭环，不重诊旧finding。',
    '新同版结果/原输入证据直接推翻修复后coverage判定或读回绑定。')
save('ObservationsNotPromoted.json',dict(observations=obs,not_owner_accepted_deferrals=True,
    no_automatic_scenario_route=True,reason='未升级说明当前证据尚不足形成高置信候选；不宣称这些现象在所有业务目标下均合理。'))

surfaces=[
 ('原行情/上游资格到共同候选的转化','F共同对象依赖已选具体Turn，必须使用独立上游分母而非成员关系行数。',[pro_ref('GlobalBehaviorProfile.json')+'#candidate_profile',pro_ref('profile/first_block_reference_by_symbol.csv')],[],['D015-O01-SELECTED-CONVERSION']),
 ('候选身份与跨Revision成员连续性','BO3身份由原问题及具体Turn集合限定；公开Life与Revision必须分开。',['IncrementalSemanticChecks.json',pro_ref('profile/STRUCTURAL_CHECKS.json')],[],[]),
 ('主输出、publication与正式引用自洽','O3包装与O4观点不同单位，同刻ordinal/前版/成员/参与引用必须闭合。',[pro_ref('GlobalBehaviorProfile.json')+'#event_profile',pro_ref('profile/STRUCTURAL_CHECKS.json')],[],['D015-O07-PUBLICATION-DENSITY']),
 ('局部依据、coverage与三种责任/终止状态','BO3有独立状态轴，有限观察/修订/交接责任不能混作市场寿命。',[pro_ref('GlobalBehaviorProfile.json')+'#state_occupancy_profile',pro_ref('profile/lifecycles.csv'),pro_ref('FindingDisposition.json')],[],['D015-O05-LIFECYCLE-AND-SELF-TRANSITIONS','D015-O08-COVERAGE-REGRESSION']),
 ('共享成员、覆盖/重叠及多组解释','R4保留各自Life，不能把组合数当独立行情数或默认合并。',['IncrementalSemanticChecks.json','MemberCombinationStrata.json'],[],['D015-O04-RELATION-MULTIPLICITY']),
 ('actual/几何confirm/selected知识的时间关系','F新准入和有限责任依赖分开的实际与知识轴。',[pro_ref('profile/latency_by_symbol.csv'),pro_ref('GlobalBehaviorProfile.json')+'#lifecycle_profile'],[],['D015-O03-LATE-ADMISSION']),
 ('责任内并发与历史累计/公开状态的口径','Owner明确指定并发36；当前责任内计数不是历史累计，亦不能冒充native active。',['ConcurrencyProfile.json','CALENDAR_SOURCE_READBACK.json'],[fid],[]),
 ('品种/知识年份/Session和开盘分层','共同资格与上游节奏可能因品种/时期不同；全局均值不可遮蔽差异。',[pro_ref('GlobalBehaviorProfile.json')+'#cross_symbol_profile',pro_ref('profile/cross_strata_comparison.csv'),'MemberCombinationStrata.json','ConcurrencyProfile.json'],[],['D015-O01-SELECTED-CONVERSION','D015-O02-PERIOD-SESSION-DENSITY']),
 ('理由/分支适用性与未暴露处理环节','正常KLine输入域限制分支可见性，不因零次数自动判失败。',[pro_ref('profile/branch_reachability.csv'),pro_ref('profile/required_reasons.csv'),under+'#unconfirmed_items'],[],['D015-O06-REACHABILITY'])]
remaining=[
 dict(surface='内部每tick active集合、准入/枚举/首阻断及原生连续coverage轨迹',
    why_not_reviewed='当前公开运行结果NOT_EXPOSED；只有明确限域的上游参考筛查和稀疏观点。',
    effect_on_current_gate='不妨碍公开事实发现及形成队列；不能据公开投影直接Release。Owner候选D若仍证据不足须保留未决。'),
 dict(surface='撤回、Clock修订、scopeEnded等本实例未给适用输入的分支',
    why_not_reviewed='无真实适用输入，不能用代码内变量冒充实测或自行变更生产输入。',effect_on_current_gate='保留未覆盖边界，不制造分支不可达finding。'),
 dict(surface='Rct未暴露的全部原始市场局部转折真值与独立环境状态',
    why_not_reviewed='现有分母不包含全部潜在市场真值，未提供可靠牛熊/活跃环境标签；本D复用指定范围，不扩展另造真值。',
    effect_on_current_gate='不外推全量无漏报或800全面合理；当前高置信发现的边界明确。')]
summary=dict(summary_id='F800-D015-FINDING-DISCOVERY-v1',feature_ref=B['code_version'],run_binding=binding,
    professional_control_commit=LOCKED,business_surfaces_reviewed=[dict(surface=s,why_applicable=w,evidence_refs=ev,
        candidate_finding_refs=f,observation_refs=o,assessment_complete=True) for s,w,ev,f,o in surfaces],
    owner_raised_candidates=[dict(finding_id=fid,assessment_status='PROMOTED',current_status='CANDIDATE',
        current_confidence='OWNER_CONCERN',must_assess_before_release=True,evidence_refs=['ConcurrencyProfile.json','GlobalFindingCandidates.json'],
        assessment_meaning='本G已确认统计现象并决定进入D；尚未完成Owner要求的最终判断，不能释放。')],
    high_confidence_candidate_refs=[fid],observations_not_promoted=[{k:o[k] for k in ['observation_id','observation','why_not_promoted','revisit_condition']} for o in obs],
    remaining_unreviewed_surfaces=remaining,
    why_current_discovery_pass_is_sufficient='沿BO1→BO2→J1/J2/J3→BO3→状态/责任→O4/O3及R4关系逐面复用当前有效全量/分层事实，并补并发/成员自然身份/覆盖重叠语义。Owner首候选之后仍完成其余适用业务面评估；无以固定指标表穷尽或自动阈值判错。当前可见材料未支持另一个明确值得升级的冲突；不可见部分如实列明。',
    discovery_pass_complete=True,first_candidate_did_not_stop_discovery=True,queue_snapshot_id=qid,
    no_logic_localization_performed=True,created_at=now())
save('FindingDiscoverySummary.json',summary)
queue=dict(snapshot_id=qid,created_at=now(),snapshot_status='CURRENT_RESULT_TRACEABLE_SNAPSHOT',run_binding=binding,
    feature_ref=B['code_version'],parameter_version=B['parameter_version'],data_scope=B['data_scope'],
    full_result_identity=B['result_identity'],professional_control_commit=LOCKED,
    source_discovery_summary='FindingDiscoverySummary.json',candidates=findings,
    priority_order=[fid],owner_raised_assessment=[dict(finding_id=fid,status='CANDIDATE',assessment_status='PROMOTED',must_assess_before_release=True)],
    closed_findings_reused_ref=pro_ref('FindingDisposition.json'),new_evidence_may_add_candidates=True,
    root_cause_or_fix_preassigned=False,next_route='Q_THEN_ONE_FINDING_D_WITH_LOGIC_LOCALIZATION')
save('CandidateFindingQueue.json',queue)

# 继承既有剖面值及其原件路径，逐项增加来源信息，不将复用改写成新执行。
profile=deepcopy(old);profile['profile_id']='F800-GLOBAL-PROFILE-D015-DISCOVERY-SUPPLEMENT'
profile['feature_ref']=B['code_version'];profile['run_binding']=binding
profile['professional_control_commit']=LOCKED;profile['reused_profile_ref']=pro_ref('GlobalBehaviorProfile.json')
profile['prior_values_recomputed']=False
for key,values in profile.items():
    if key.endswith('_profile') and isinstance(values,list):
        for index,value in enumerate(values):
            value['provenance']=dict(origin_ref=pro_ref('GlobalBehaviorProfile.json'),origin_section=key,
                original_source_location=value.get('source_location'),mode='REUSED_VALID_D008_G')
            value['source_location']=pro_ref('GlobalBehaviorProfile.json')+'#/'+key+'/'+str(index)
profile['statistics_definitions']=deepcopy(old['statistics_definitions'])+load('IncrementalStatisticDefinitions.json')['definitions']
for i,value in enumerate(profile['statistics_definitions'][:len(old['statistics_definitions'])]):
    value['origin_ref']=pro_ref('StatisticDefinitions.json')+'#/statistics_definitions/'+str(i)
    value['business_item_ref']=under+'#business_objects'
profile['current_object_profile']=[dict(r,value_or_distribution=dict(metric=r['metric'],distribution=r['distribution'])) for r in con['distributions']]
profile['object_profile'].append(dict(statistic_id='D015-ST02',stratum_id='ALL',value_or_distribution=semantic,
    sample_size=480,denominator_value=480,source_location='IncrementalSemanticChecks.json',notes='本G补充成员身份与关系语义；27项既有检查另复用。'))
profile['reference_integrity_profile'].append(dict(statistic_id='D015-ST03',stratum_id='ALL',value_or_distribution=semantic['checks'][2:],
    sample_size=461,denominator_value=461,source_location='IncrementalSemanticChecks.json',notes='242 CoveredBy与219 Overlaps各自分母；不是新的原生读回。'))
profile['conversion_profile']=[dict(statistic_id='D015-ST04',stratum_id='SYMBOL',value_or_distribution=csvrows('counts_by_symbol.csv'),
    sample_size=1859,denominator_value=1859,source_location=pro_ref('profile/counts_by_symbol.csv'),
    notes='复用原上游/参加位置，候选Life/publication分列，不以成员关系行数当分母。'),
    dict(statistic_id='D015-ST04',stratum_id='ALL_REFERENCE_PAIR',value_or_distribution=old['candidate_profile'][2]['value_or_distribution'],
        sample_size=648,denominator_value=648,source_location=pro_ref('profile/near_actual_pair_screen.csv'),notes='参考筛查非原生试探轨迹，非业务真值。')]
profile['limits']+=['本补充并发按公开Calendar采样；责任内/公开Open/内部active/历史累计均分列，不互相升级。',
    '本G高置信候选表示值得诊断，不是最终缺陷；Owner候选未完成D判断，旧G PASS不再充当前释放依据。',
    '原G的场景问题路线保留历史；新控制不自动进入旧S1/S2，当前后继按Q逐个D。']
save('GlobalBehaviorProfile.json',profile)
gate=dict(status='DIAGNOSIS_REQUIRED',reasons=['当前高置信发现补充及队列快照已完成。',
    'F-LIFE-PEAK-CONCURRENCY为Owner必评候选，统计现象实核且已PROMOTED进D，最终业务判断未完成。',
    '当前没有新行为改变；不要求机械重跑三年Feature，不签FeatureRelease。'],
    valid_profile_ref='GlobalBehaviorProfile.json',queue_snapshot_ref='CandidateFindingQueue.json',
    source_summary_ref='FindingDiscoverySummary.json',run_binding=binding,professional_control_commit=LOCKED,
    next_action='原manager消费本回交后按新Q一次取一个finding签原D，Owner候选先LogicLocalization；再决定B/M/关闭或未决。',
    feature_release_allowed=False,rerun_feature_now=False)
save('GlobalProfileGate.json',gate)
closed=prior('FindingDisposition.json')
save('FindingRegister.json',dict(current_candidates=findings,closed_findings_reused=closed['findings'],
    prior_register_ref=pro_ref('FindingRegister.json'),old_closed_findings_reopened=False,
    prior_scenario_questions='保留历史记录，不作为当前新Workflow自动场景委派。'))
result=dict(statistics_input_readiness='StatisticsInputReadiness.json',global_behavior_profile='GlobalBehaviorProfile.json',
    finding_discovery_summary='FindingDiscoverySummary.json',global_finding_candidates=findings,
    candidate_finding_queue='CandidateFindingQueue.json',observations_not_promoted=obs,candidate_case_index=[case],
    diagnosis_input_adapters=[adapter],gate=gate,professional_control_commit=LOCKED)
save('FeatureGlobalBehaviorProfilingResult.json',result)
save('G_WORKFLOW_COMPLETION.json',dict(G1='同版绑定/字段可统计性已核，PARTIAL不伪造不可见内部值',
    G2='D008 ST01-ST18复用，D015-ST01..04事先登记必要增量口径',
    G3='完整对象/事件/状态/生命周期/转化剖面复用，增加当前公开并发/身份关系语义',
    G4='原27项结构事实复用，新4项业务语义检查全量实做，未见新冲突',
    G5='原SYMBOL/YEAR/SESSION/OPENING分层复用，补并发YEAR/SESSION及成员组合层',
    G6='适用业务面发现全部完成，1个Owner候选进D，8项未升级，3处不可见/范围边界',
    G7='原生DiagnosisInputAdapter兼容证据包及CandidateCaseIndex已形成，无根因预填',
    G8='DIAGNOSIS_REQUIRED，原manager后继Q/单finding D先LogicLocalization',
    discovery_completed=True,diagnosis_completed=False,formal_behavior_modified=False,FeatureRelease=False,workers=[]))
save('INPUT_BINDING.json',dict(run_id=RUN,call_id='C0034',delegation_id='D015',executor='codex:'+RUN+':executor:E1',
    assignment_ref=json.loads(PACKET.read_text())['delegation_ref'],invocation_ref=json.loads(PACKET.read_text())['invocation_ref'],
    professional_control_commit=LOCKED,locked_skill_ref=ref(LOCKED,'skills/reasonableness-analysis/feature-global-behavior-profiling/SKILL.md'),
    owner_source_ref=owner,source_ref_count=audit['count'],current_result_binding=binding,
    feature_code_version=B['code_version'],parameter_version=B['parameter_version'],permitted_operations=['run_result_statistics_analysis_write','run_record_write'],
    workspace=str(BASE),record_branch='codex/oi-f800-stat-20261122-01',workers=[],
    U_X_prior_G_and_31table_readback_reused=True,native_feature_run=False,prior_G_rerun=False,S1_S2_repeated=False,
    logic_localization_performed=False,root_cause_or_fix_preassigned=False,formal_behavior_modified=False,FeatureRelease=False))
print(json.dumps(dict(discovery_pass_complete=True,business_surfaces=len(surfaces),candidates=len(findings),owner_assessment='PROMOTED_TO_D',
    observations_not_promoted=len(obs),remaining_boundaries=len(remaining),gate=gate['status'],professional_control_commit=LOCKED),ensure_ascii=False))
