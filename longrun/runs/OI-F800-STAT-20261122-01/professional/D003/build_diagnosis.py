"""按锁定business-discrepancy-diagnosis合同整理本D原生交付。"""
from pathlib import Path
from datetime import datetime,timezone
import json,re

ROOT=Path(__file__).resolve().parent;PREV=ROOT.parent/'D002'
RUN='OI-F800-STAT-20261122-01'
PREF='daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/'+RUN+'/professional/D002/'
CODE='daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574:src/Frp/Instance/ISL/Opportunity/'
L0='daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md'
def load(p):return json.loads(p.read_text())
def clean_refs(d):
    if isinstance(d,list):return [clean_refs(x) for x in d]
    if isinstance(d,dict):return {k:clean_refs(v) for k,v in d.items()}
    if isinstance(d,str) and d.startswith(CODE):
        m=re.fullmatch(r'(.+\.hs):(\d[\d,\-]*)',d)
        if m:return dict(ref=m.group(1),line_range=m.group(2))
    return d
def write(n,d):(ROOT/n).write_text(json.dumps(clean_refs(d),ensure_ascii=False,indent=2)+'\n')
E=load(ROOT/'EXPERIMENT_RESULTS.json');H=load(ROOT/'HASKELL_PROBE_VALIDATION.json')
adapter=load(PREV/'DiagnosisInputAdapters.json')[0];expect=adapter['frozen_expectation']
assert E['published_flag_mismatches']==0 and E['diagnostic_changed_occurrences']==22 and H['four_controls_pass']
binding=dict(code_version=load(PREV/'FeatureRunResultBinding.json')['code_version'],
    parameter_version=load(PREV/'FeatureRunResultBinding.json')['parameter_version'],
    result_ref=PREF+'FeatureRunResultBinding.json',frozen_expectation_ref=PREF+'DiagnosisInputAdapters.json#F800-DA-001',
    time_basis=adapter['data_binding_and_time_basis']['time_basis'])
write('FrozenExpectation.json',expect)
write('EvidenceComparisonPackage.json',adapter['evidence_comparison_package'])
write('DiagnosticInputBinding.json',dict(**binding,source_adapter_ref=PREF+'DiagnosisInputAdapters.json',adapter_id=adapter['adapter_id'],
    selectors_preserved=['frozen_expectation','evidence_comparison_package','business_intent_ref','processing_chain_ref','relevant_code_or_requirement_refs','data_binding_and_time_basis'],
    frozen_expectation_reused_unchanged=True,evidence_package_reused_unchanged=True,evidence_relative_path_base=str(PREV),
    original_business_intent_ref=adapter['business_intent_ref'],original_processing_chain_ref=adapter['processing_chain_ref']))

chain=[]
def stage(id,inp,rule,state,out,actual,confirm,ref,loss):
    chain.append(dict(stage_id=id,Input=inp,Rule=rule,State=state,Output=out,ActualTime=actual,ConfirmTime=confirm,
        Version=ref,PossibleInformationLoss=loss))
stage('P1','三品种真实KLine close/closeUti，5m','同一个收盘事件取得价格与UTI；step=5×120=600',
    '无覆盖历史状态','known=round u；position=u/step；进展u=1×rawUTI','市场收盘原UTI','原事件timestamp/known',
    CODE+'U2/GroupCandidateKLineInput.hs:40-55','Double除法引入舍入；rawUTI仍恰为整数')
stage('P2','本次position/u与上一次position/u','只有position-p==1才声明上一原UTI到当前u的相邻边，否则只声明当前点',
    'previous=(position,u)','ObjectCoverage CoverageObserved [old,u]或[u,u]','原UTI端点','同拍已知',
    CODE+'U2/GroupCandidateKLineInput.hs:94-116','最早偏差：浮点归一化位置之差不能精确等1，真实相邻边被丢弃')
stage('P3','各对象本拍窄边、已有累计区间','相接边first<=oldThrough时累计；不相接时从当前片段重启',
    'objectCoverage Map Text ObjectCoverage','覆盖累计起点由72004199重置为78643799','当前u轴','同拍已接受材料',
    CODE+'U2/GroupCandidateMaterial.hs:92-102,122-132','按输入正确累计；无法恢复P2没有声明的相邻边，不能在此盲目合并真实缺口')
stage('P4','固定域累计区间与W=800×600','每对象first<=u-W且through>=u，且无未知Clock等待才完整',
    'materialCoverageIncomplete','假断点起直到u=79123799恢复前，导出缺覆盖','[u-480000,u]','本拍materialKnown',
    CODE+'U2/GroupCandidateMaterial.hs:53-89','错误重启需要再等4000开放分钟才累积足够窗口；这是传播而非新的根因')
stage('P5','当前材料覆盖标志、已有候选/边界','覆盖值变动使affected；body内保存当前materialCoverageIncomplete',
    'CandidateState、CandidateBody、previous exact','新候选Revision及candidateDomainIncomplete','组原问题/责任边界不变','candidateKnown=materialKnown',
    CODE+'U2/GroupCandidateEvolution.hs:63-104,117-142','错误材料状态进入正式观点，可能触发额外复评/修订；不是Pending或无输出')
stage('P6','同次已决定CandidateOccurrence','storeGroupOccurrence直接bool编码；正常薄publication保存；TIS字段直读',
    '正式历史不删除；当前public父坐标','groupCoverageIncomplete=0/1','不回贴actual','原publication timestamp/groupKnownFrom',
    CODE+'U2/GroupCandidateStorage.hs:75-83','没有发现reader、字段映射或序列化反转；1,546个公开值与P1-P5覆盖重放全部一致')

facts=[
 dict(id='F01',statement='D002准确版本、完整配置、正式范围、fields身份和独立31表回读继续有效；本D未新生产或替换实例',evidence=[PREF+'FeatureRunResultBinding.json','SOURCE_AUDIT.json']),
 dict(id='F02',statement='三品种各49,683个输入，raw closeUti步长全部为600；同实例KLine文件SHA与D002导出一致',evidence=['EXPERIMENT_RESULTS.json','diagnose_coverage.py']),
 dict(id='F03',statement='真实断点2021-08-31 21:45：78643199→78643799，整数差600；归一化131071.99833333334→131072.99833333332，Double差0.9999999999854481；三品种同拍各一次假断点',evidence=['SOURCE_FALSE_BREAKS.csv','HASKELL_DOUBLE_GUARD_PROBE.csv']),
 dict(id='F04',statement='源代码guard未包含800或delta；因guard失败发行[u,u]，正常累计区间由首输入72004199重启为78643799',evidence=['CODE_AUDIT.json','BOUNDARY_CONTROLS.csv']),
 dict(id='F05',statement='锁定覆盖方程重放与全部1546个正式观点flag一致，0差异；本D重放为derived，不冒充原生内部trace',evidence=['PUBLISHED_FLAG_RECONCILIATION.csv','EXPERIMENT_RESULTS.json']),
 dict(id='F06',statement='只在隔离方程中用原始整数UTI相邻关系替代浮点商差，恰好将22个冲突观点改为完整，涉及12Life/18时刻；8个冷启动flag保留',evidence=['DIAGNOSTIC_COUNTERFACTUAL_AT_PUBLISHED_LOCATIONS.csv','EXPERIMENT_RESULTS.json']),
 dict(id='F07',statement='Haskell真实Double执行确认断点前后正常相邻均通过、真实断点被原guard误拒绝；跳过一根的1200UTI真实缺口在两种判断下都不连续',evidence=['HASKELL_DOUBLE_GUARD_PROBE.csv','HASKELL_PROBE_VALIDATION.json']),
 dict(id='F08',statement='假断点后累计窗口于2021-09-16 11:25（u=79123799）才重新满800Δ；22个正式冲突均位于这段传播区间',evidence=['COVERAGE_RESTORATIONS.csv','BOUNDARY_CONTROLS.csv']),
 dict(id='F09',statement='正常KLine每个选中Turn总携带Just Clock，framePatches=[]且frameEnded=False；未暴露的内部计数器不作为观测数据',evidence=['CODE_AUDIT.json',CODE+'U2/GroupCandidateKLineInput.hs:77-116'])]

explanations=[
 dict(id='A',hypothesis='真实输入断点、缺价或夜盘Calendar跳跃',prediction='冲突窗口内应有非600UTI步长/缺价/不对齐',check='D002逐22窗有效性与本D输入SHA/全轴步长核对；日夜盘样本对照',outcome='RULED_OUT_FOR_THIS_FINDING',evidence=['SOURCE_FALSE_BREAKS.csv',PREF+'VALIDATION.json']),
 dict(id='B',hypothesis='冷启动未满800Δ',prediction='覆盖历史应在u-480000之后',check='22窗真实输入起点72004199远早于所需起点；另8个冷启动保持为1',outcome='RULED_OUT_FOR_22_NOT_FOR_8_CONTROLS',evidence=['BOUNDARY_CONTROLS.csv','EXPERIMENT_RESULTS.json']),
 dict(id='C',hypothesis='代码/参数/实例错绑，或reader把flag反读',prediction='绑定或重放的公开值会不一致',check='37项准确来源、6个锁定FRP文件与加载runtime字节一致；公开1,546flag与旧方程逐值一致；serializer与字段映射直传',outcome='RULED_OUT',evidence=['SOURCE_AUDIT.json','CODE_AUDIT.json','PUBLISHED_FLAG_RECONCILIATION.csv']),
 dict(id='D',hypothesis='未知Clock等待或正式修订导致合理不完整',prediction='有失知Clock/patch或Source失败证据',check='当前路径每Turn Just Clock、framePatches为空；恢复时刻完全由单一假断点+800Δ预测',outcome='RULED_OUT_IN_NORMAL_KLINE_BINDING',evidence=['CODE_AUDIT.json','COVERAGE_RESTORATIONS.csv']),
 dict(id='E',hypothesis='浮点归一化商的严格差值判断丢失连续边',prediction='整数步长600但Double商差不等1；单点重启应预测所有公开flag与恢复边界',check='Python锁定方程重放+真实Haskell四对照+仅替换guard的隔离反事实',outcome='CONFIRMED_DIRECT_CAUSE',evidence=['EXPERIMENT_RESULTS.json','HASKELL_DOUBLE_GUARD_PROBE.csv']),
 dict(id='F',hypothesis='原被冻结覆盖预期不适用或需业务取舍',prediction='应有不同固定域/时间语义的既有合同或有价值冲突',check='已冻结适用条件均满足；真实缺口对照不要求放宽覆盖；没有新业务目标或tradeoff',outcome='NO_EVIDENCE_REQUIRING_EXPECTATION_REVISION',evidence=[PREF+'DiagnosisInputAdapters.json','HASKELL_DOUBLE_GUARD_PROBE.csv'])]

experiments=[
 dict(experiment_id='F800-MDE-001',scope='DIAGNOSTIC_ONLY',question='是否确有source连续性判断失真，能否解释完整已发布偏差？',
    frozen_inputs=binding,minimum_additional_evidence='复用已有3×49,683个KLine的UTI列、1,546个已发表flag；只扫描覆盖方程，不重跑FRP或G',
    discriminating_predictions=dict(floating_cause='出现raw连续/浮点不连续，重放flag应全吻合',data_gap_cause='raw应有缺口；修正纯算术不能保留真实缺口对照'),
    procedure=['核对源字节与输入SHA','按原guard与accumulateForwardCoverage/covered方程派生覆盖状态','只对已发表位置对齐flag','在隔离副本方程中用整数UTI相邻判据','对真实断点前后及真实1200UTI缺口执行Haskell Double'],
    actual_results=E,haskell_results='HASKELL_PROBE_VALIDATION.json',
    interpretation='单一P2假断点足以解释全体22个finding位置和800Δ后的恢复；竞争解释被当前输入和四对照排除',
    limitations=['不是native内部trace，未声称读到了materialTotals','未重放完整候选枚举/身份/alternate引用，不据此宣布新正式组数/观点数','整数诊断判据仅验证锁定5m/120UTI的当前输入，不等于覆盖所有可配置市场/频率的正式修复实现'])]

repair=dict(suspected_parameters=['profile.observation_multiple=800','profile.delta=600','market.units_per_open_minute=120','market.units_per_calendar_tick=1','input.freq=5m','硬编码连续性==1、未知Clock/revision尾6Δ、handoff尾18Δ'],
    parameter_consumers=[
        dict(parameter='observation_multiple × delta',definition=CODE+'U2/GroupCandidateTypes.hs:19-26',consumers=[CODE+'U2/GroupCandidateMaterial.hs:55,63,75',CODE+'U2/GroupCandidateEvolution.hs:130-132'],effect='控制材料准入和覆盖窗/观察期限；不参与source商差guard'),
        dict(parameter='freq与units_per_open_minute',definition=CODE+'U2/GroupCandidateKLineInput.hs:43-53',consumers=[CODE+'U2/GroupCandidateKLineInput.hs:109-112'],effect='派生step=600和position；属已锁定输入尺度/Calendar单位，改变会影响上游与实际业务单位，不是允许试调的修复手段'),
        dict(parameter='units_per_calendar_tick',definition=CODE+'U2/GroupCandidateKLineInput.hs:53,77',consumers=[CODE+'U2/GroupCandidateMaterial.hs:55-77'],effect='进展及Clock换算，不修复position差guard'),
        dict(parameter='硬编码==1',definition=CODE+'U2/GroupCandidateKLineInput.hs:110',consumers=['覆盖相邻窄边判定'],effect='当前没有暴露连续性容差或精确离散步长策略；直接责任点'),
        dict(parameter='固定6Δ/18Δ',definition=CODE+'U2/GroupCandidateMaterial.hs:67',consumers=[CODE+'U2/GroupCandidateEvolution.hs:131',CODE+'U2/GroupCandidateDecisions.hs:56-59'],effect='后续等待/修订/交接；不参与source连续性，不能修复断点')],
    earliest_business_divergence='P2：guard失败，把正确[78643199,78643799]边降为[78643799,78643799]点',
    feasibility_status='PROVEN_NOT_ADJUSTABLE',
    feasibility_evidence=['在同一锁定输入、需保留当前业务对象的配置范围内，K/Δ不进入guard，无法改变该假断点',
        '真实正窗口合同下，断点重启first=u无法覆盖此前窗口；在当前W=480000及保持既有观察对象的窗口范围，first<=u-W为false。用极小W让浮点减法吞掉窗口，或把候选滤空来不发表，都不是原预期的修复',
        '以屏蔽候选或改变5m、单位、Calendar来避开发表不满足原冻结预期，且越过本轮硬输入',
        '能力结论只限当前暴露参数；不能扩大为实现不可修复。精确UTI相邻策略在隔离算术中恢复断点，并保留真实缺口'],
    upstream_dependency='K/Δ同时影响材料与组责任；freq/单位更改会改变上游坐标与业务尺度，本D不修改或试标定',
    unresolved_constraints=['正式实现需对支持的频率/单位验证精确步长策略，对非整数步长、Clock失知、真实间隙明确处理','修复改变覆盖正文与稀疏Revision序列，必须Owner确认后完整X/G；当前反事实不代替重跑'],
    next_route='IMPLEMENTATION_CORRECTION_AFTER_OWNER_MODIFICATION_CONFIRMATION')

impact=dict(affected_occurrences=22,occurrence_denominator=1546,occurrence_ratio=22/1546,affected_lives=12,life_denominator=480,
    affected_life_ratio=12/480,affected_publication_ticks=18,
    technical='正式groupCoverageIncomplete把已有成功连续观测误报为缺覆盖；source错误触发状态变动，影响候选修订正文及其发行条件',
    business='错误削弱候选观察覆盖可信度。无论某下游是否使用该字段，正式载荷与当前覆盖事实应自洽；未证明交易/收益损失，不升级为该类结论',
    prioritization='MEDIUM：可复现正式载荷正确性问题，比例1.423%观点/2.5%Life；应在本轮释放前处理或由Owner明确暂缓',
    effect_limit='未测量完整修复后总观点数、UUID链及下游效应；不承诺只少22个观点或保持全部历史ID')
report=dict(diagnosis_id='F800-DIAG-001',expectation_id=expect['expectation_id'],expectation_version=expect['version'],
    discrepancy_statement='在当前锁定三品种连续KLine且无未知Clock条件下，正式22个观点错误标记覆盖不完整；最早偏差是source归一化Double商差严格==1误拒绝真实600UTI相邻边。',
    business_impact=impact,confirmed_facts=facts,processing_chain=chain,competing_explanations=explanations,
    ruled_out_explanations=[x['id'] for x in explanations if x['id']!='E'],remaining_explanations=[],
    discriminating_checks=experiments,current_localization=dict(status='LOCATED',category='ImplementationMismatch',responsibility_layer='F：输入应用/覆盖状态形成（P2），数值实现误差',
        direct_responsibility_stage='GroupCandidateKLineInput.buildKLineGroupSource.advance.coverage guard',
        code_ref=CODE+'U2/GroupCandidateKLineInput.hs:109-112',downstream_propagation=['P3累计重启','P4等待800Δ覆盖','P5候选正文/发行','P6原样保存读取']),
    parameter_repairability=repair,confidence='HIGH：实际输入、Haskell Double、1,546个正式flag及22个反事实位置闭合；未把隔离派生trace冒充native内部观测',
    next_route='manager消费D003后，按L0 §7将ModificationProposal提交Owner确认；确认后另行委派实施回归，再X/G。此D不实施或发布正式代码改动。',
    ImplementationConformance=dict(arithmetic_execution='当前代码确实按写出的Double guard执行；reader/publication与其一致',
        intended_rule_conformance='数值guard不能可靠实现相邻原UTI的业务关系，因此与既定连续观测合同不符，归ImplementationMismatch'),
    BusinessReasonableness=dict(frozen_expectation='当前适用，保持原版本；不需要因实现舍入而弱化',value_tradeoff_required=False,
        interpretation_limit='本finding诊断不裁决800是否业务合理，也不处理原G四项场景问题'),
    data_binding_and_time_basis=binding,diagnosis_scope_complete=True,formal_repair_applied=False)
issue=dict(issue_id='F800-ISSUE-001',finding_ref=PREF+'GlobalFindingCandidates.json#F800-GF-001',diagnosis_ref='DiagnosisReport.json#F800-DIAG-001',
    issue_type='ImplementationMismatch',status='CONFIRMED_NOT_REPAIRED',title='KLine覆盖连续性用浮点商差严格相等产生假断点',
    direct_responsibility=report['current_localization'],reproduction=['SOURCE_FALSE_BREAKS.csv','HASKELL_DOUBLE_GUARD_PROBE.csv','PUBLISHED_FLAG_RECONCILIATION.csv'],
    business_impact=impact,scope='仅当前锁定F800 KLine入口已证明发生；其他入口/品种/尺度不外推为同样发生',
    no_behavior_change=True,required_authorization='依原L0 §7/Owner指令，正式实施、提交、推送或采用修复前需Owner确认',
    acceptance_criteria=['真实连续600UTI边跨131072归一化边界仍连续','真实缺口、冷启动、未知Clock/失败不能被桥接',
        '通过原有窗口/2Δ/责任边界合同回归；800、delta600及基线method.revision1保持批准范围',
        'Owner确认后，以新准确版本完整三年X及G证明该finding不再发生，并复核额外输出/身份影响'])
proposal=dict(proposal_id='F800-MP-001',finding_ref=PREF+'GlobalFindingCandidates.json#F800-GF-001',
    current_behavior='原始600UTI连续边经u/step转换后，跨浮点量级边界差值非精确1；P2发行点而非边，P3据此重启覆盖，正式22观点误报。',
    proposed_change='仅在正常KLine适配器用源UTI和该频率/Calendar的准确预期步长判定相邻边，避免对两个已除法归一化Double位置做严格差值相等；保留真实间隙、失知/失败与冷启动边界，不放宽覆盖窗口或2Δ。正式实现对非整数步长须显式校验/设计，不盲目round。',
    why_this_stage='P2是最早丢失真实边的阶段；P3严格合并规则正确，reader直读正确。改后续窗口、强制groupCoverageIncomplete=0或跨缺口合并只掩盖责任点。',
    alternatives=[dict(option='保持现状，Owner明确暂缓',consequence='保留22个错误观点及后续风险；不得宣布finding已修复'),
        dict(option='缩短800或调整delta',consequence='改变业务责任和材料准入，仍不能消除原始guard假断点；不推荐作为此实现问题修复'),
        dict(option='给Double商差加入容差',consequence='可在数学上避开本位置，但新增容差边界需验证不桥接真实间隙；相比原始UTI精确步长更难审计，不作为当前推荐')],
    expected_effect='当前输入的假断点被保留为真实相邻边；隔离方程上22个冲突flag转0且8个冷启动保留。完整修复后的正式观点数和UUID序列须重跑测量，现阶段不承诺。',
    possible_side_effects=['覆盖值与变化时刻改变会影响candidate affected/body比较、Revision发行及组间exact引用；随机ID不能跨Run强行等同',
        '步长策略需兼容获支持的Calendar单位和频率，真实空洞/Clock失知不能被误合并','F/Q共享适配器的下游影响应由实施/释放角色评估；本D未运行Q/V'],
    validation_plan=['实现前确认支持频率/单位的精确离散步长合同；保留本D四对照','实施后添加/运行有业务意义的数值边界、真实缺口、冷启动、未知Clock及原有观察窗/2Δ回归',
        '对象/状态/事件合同若变则只更新受影响U；否则直接锁新代码完整X、31表独立读回与G',
        '按原finding完整22位置及三年覆盖状态复验；新G检查状态、引用、密度及四个场景问题影响；不得用局部算术结果代替正式释放'],
    files_or_parameters_to_change=[dict(file='src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs',scope='正常KLine覆盖相邻边判定及必要局部状态载荷'),
        dict(file='适用的现有FRP测试入口（实施D具体确定）',scope='保护真实边与真实缺口的回归')],
    parameter_changes='本提案不建议改变批准的observation_multiple800、delta600、单位、范围、尺度或method.revision；版本与实例登记由后续批准实施D处理',
    diagnostic_support=['EXPERIMENT_RESULTS.json','HASKELL_PROBE_VALIDATION.json'],
    approval_status='NOT_REQUESTED_BY_EXECUTOR_PENDING_MANAGER_SUBMISSION',formal_patch_prepared=False,formal_change_applied=False,
    authority=L0+'#7',authority_quote='把候选 patch／候选参数提交、推送或登记为本 Run 当前版本',
    next_actor='原manager向Owner提交本具体提案；未经确认不得实施、提交/推送Feature代码或采用为当前正式版本')
disposition=dict(finding_id='F800-GF-001',observation=report['discrepancy_statement'],business_conflict=expect['statement'],
    direct_responsibility_stage=report['current_localization'],confirmed_facts=facts,competing_explanations=explanations,
    resolution_route='Owner确认后实现修正→X/G复验',resolution_status='DIAGNOSED_IMPLEMENTATION_MISMATCH_NOT_FIXED',
    cross_effects_to_check=proposal['possible_side_effects'],original_g_profile_unchanged=True,original_global_gate='DIAGNOSIS_REQUIRED',
    release_statement='本D诊断完成不代表finding修复、800标定或FeatureRelease。未经批准采用变化，当前D002结果仍是锁定ac版本的有效未修复历史。')
for name,value in [('DiagnosisReport.json',report),('MinimalDiscriminatingExperiment.json',experiments[0]),('RequirementOrImplementationIssue.json',issue),
                   ('ModificationProposal.json',proposal),('FindingDisposition.json',disposition),('ProcessingChain.json',chain),('ParameterRepairability.json',repair)]:write(name,value)
write('OWNER_DECISION_APPLICABILITY.json',dict(owner_decision_packet_required=False,
    reason='这是可由事实排除解释的数值实现偏差，无需要Owner选择的业务价值冲突；所以不生成OwnerDecisionPacket。正式行为改变的Owner确认仍依L0，不能混同为豁免。',
    modification_proposal='ModificationProposal.json',confirmation_required_before_formal_change=True))
write('WORKFLOW_COMPLETION.json',dict(skill='daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md',
    steps=[dict(step=i,completed=True,evidence=ref) for i,ref in [(1,'DiagnosisReport.json#discrepancy_statement'),(2,'ProcessingChain.json'),(3,'DiagnosisReport.json#confirmed_facts,competing_explanations'),
        (4,'DiagnosisReport.json#competing_explanations'),(5,'MinimalDiscriminatingExperiment.json'),(6,'DiagnosisReport.json#current_localization,parameter_repairability'),
        (7,'DiagnosisReport.json#BusinessReasonableness'),(8,'ModificationProposal.json; FindingDisposition.json')]],
    completed_at=datetime.now(timezone.utc).isoformat(),scope='单finding诊断、问题及具体修改提案完成；实施/Owner确认/新X/G/释放是后继，未代执行'))

text=f'''# D003｜F800-GF-001 偏差诊断报告

已按锁定 Skill 完成单 finding 诊断。结论为 **ImplementationMismatch**：`GroupCandidateKLineInput.hs:109–112` 用两个已归一化浮点商的差严格等于1来判断相邻，真实600UTI边跨浮点量级边界时被误判为断点。不是当前数据缺口、冷启动、错绑或reader反读。本D未修改正式Feature、参数或输入处理。

## 准确输入与范围

原D003：`daowei2026/observe-iterate@a7fc7d76e4950978c04edf2777a049fd28f1b0c6:longrun/runs/{RUN}/delegations/D003/DELEGATION.json`，C0007/E1，workers=[]，回原manager。37项准确来源逐字节与Git对象核对，最新Owner原文逐字核对，见 [SOURCE_AUDIT.json](SOURCE_AUDIT.json)。

原 F800-DA-001 的冻结预期 `{expect['expectation_id']}` / `{expect['version']}` 保持不变：{expect['statement']}。输入直接消费已接收D001与D002，不重做有效U/X/G。正式版本仍为FRP ac1927518ad6105f15ffbe37fea45e4be91ba574、TIS 2f460d663d821cf2ba25555eda13e78b697d0767；配置SHA `{binding['parameter_version']}`；rb/hc/i、5m、2021—2023、night_end_at_2300、TA_updto20240229_DBA/steel。正式目录与fields身份继续取原D002 FeatureRunResultBinding，未新生产。

## 可复现直接证据

2021-08-31 21:40到21:45，原UTI **78643199→78643799，差600**。代码step=5×120=600，而两个Double商为131071.99833333334与131072.99833333332，差 **0.9999999999854481**，所以 `position-p==1` 为False。三品种同拍各发生一次此假断点，跨过归一化2^17附近的表示精度边界。

源适配器因此声明`[78643799,78643799]`点，丢弃真实`[78643199,78643799]`相邻边。严格累计器正确地把它当不相接新片段，累计起点由72004199重启为78643799。之后直到u=79123799（2021-09-16 11:25）才再次积满480000UTI，即4000开放分钟。断点、相接累计、覆盖判定、候选发行、序列化/reader的逐阶段输入、规则、状态、时间和版本见 [ProcessingChain.json](ProcessingChain.json)。

独立Haskell Double小值实验结果：

| 对照 | 原商差guard | 原始UTI诊断判据 |
| --- | --- | --- |
| 断点前正常600UTI边 | True | True |
| 真实发生的600UTI数值边界 | False | True |
| 断点后正常600UTI边 | True | True |
| 跳过一根、相距1200UTI真实缺口 | False | False |

[HASKELL_DOUBLE_GUARD_PROBE.csv](HASKELL_DOUBLE_GUARD_PROBE.csv) 为当前真实执行结果。直接runghc先因缺libtinfo退出127；随后使用既有Stack环境运行同一独立脚本成功，没有安装系统库、编译或更改正式Feature。详见 [HASKELL_PROBE_VALIDATION.json](HASKELL_PROBE_VALIDATION.json)。

只读已有三品种UTI并重放锁定覆盖方程，在全部1546个已发表观点上，覆盖标志 **1546/1546一致、0差异**。仅在隔离方程中替换连续性guard，恰好改变原finding的22个观点、12个Life、18个时刻；8个冷启动标志保留，没有把所有flag强制清零。见 [EXPERIMENT_RESULTS.json](EXPERIMENT_RESULTS.json)、[PUBLISHED_FLAG_RECONCILIATION.csv](PUBLISHED_FLAG_RECONCILIATION.csv)、[DIAGNOSTIC_COUNTERFACTUAL_AT_PUBLISHED_LOCATIONS.csv](DIAGNOSTIC_COUNTERFACTUAL_AT_PUBLISHED_LOCATIONS.csv)。

这些是 **DIAGNOSTIC_ONLY派生重放**，不是未暴露的native内部trace；没有运行完整候选演化，不能据此宣布未来正式组数、观点数或UUID链。读取的输入文件SHA、6个FRP相关文件与加载runtime原件均核对，见 [CODE_AUDIT.json](CODE_AUDIT.json)。D002对22个窗口的三对象有效价格/801行连续UTI核验仍有效；本D未用缺价数据作反例。

## 竞争解释与责任

真实输入断点/夜盘跳跃与全轴600UTI步长不符；冷启动解释只适用于保留的8个对照，不适用于远离起点的22个位置；正常KLine每个Turn都携带Just Clock、patch为空，不是未知Clock等待；绑定、serializer和reader均与同一数据/方程相符。浮点guard假断点则同时预测了发生拍、累计起点、800Δ恢复边界及全部正式flag。逐项预测、检查、排除理由在 [DiagnosisReport.json](DiagnosisReport.json) 中。

ImplementationConformance与BusinessReasonableness分别报告：当前程序确实执行了写出的浮点guard，输出忠实反映其状态；但这个数值判据没有可靠实现已声明的相邻观测关系，因此属于实现不符。冻结覆盖预期在这些输入上仍适用，不因舍入而修改旧预期，也不产生新的业务取舍。未发现未决竞争解释；正式修复的通用实现与副作用验证仍是后继责任。

业务影响是22/1546=1.423%的正式观点把成功连续观测误报为缺覆盖，涉及12/480=2.5%的Life。该字段参与candidate affected/body比较，可能造成额外复评和修订；当前不估计完整修复后的总观点数、随机ID链或交易收益影响。按正式载荷正确性列为MEDIUM，释放前应修复验证或由Owner明确暂缓，不能因下游可能不读该字段而宣布无问题。

## 参数可修复性与具体修改提案

原生可修复性为 **PROVEN_NOT_ADJUSTABLE（限当前锁定输入及现有暴露参数）**。800与delta不进入source连续性guard；假断点让first=u后，无法覆盖此前真实正窗口。缩短K只缩短错误持续时间，不能恢复已丢失边；用极小W让浮点减法吞掉窗口、改变频率/单位或抑制候选，也不满足原预期。6Δ修订/等待、18Δ交接均在责任点之后。没有把“现有参数无解”扩大成“实现完全不可修复”；详见 [ParameterRepairability.json](ParameterRepairability.json)。本问题不应直接转盲目标定。

[ModificationProposal.json](ModificationProposal.json) 已准备为可审阅提案：在P2正常KLine适配器以源UTI及频率/Calendar的准确预期步长表达相邻，保留真实缺口/失知/冷启动边界；不改800、delta600、2Δ、正式范围或基线method.revision。其他频率/非整数步长须明确合同后实现，不能盲目round。当前没有准备、提交或推送正式候选patch，也未把诊断方程登记为正式版本。

提案列出保持现状、缩短K、浮点容差等替代及副作用；明确修复会影响稀疏Revision与exact引用。批准实施后先做数值边界/真实缺口/冷启动/Clock及原合同回归，再锁新版本完整X、31表独立回读和G，复验原22位置及全三年结构。局部算术通过不等于Feature释放。

正式行为改变须由Owner确认，依据 [原L0 §7](https://github.com/daowei2026/observe-iterate/blob/87b951bbd15078a2d6353bdd24afe0d8f19c845c/control-v0.3/01_L0_统计驱动的单特征闭环.md)：其§7.2将“正式 Feature 代码、业务规则和输出合同”及“把候选 patch／候选参数提交、推送或登记为本 Run 当前版本”列为确认后才能采用的改变。当前只回交分析、问题与提案，下一步由原manager提交Owner；本executor不代签批准。

没有需要Owner作价值取舍的第三类不确定性，故不生成OwnerDecisionPacket；这与正式修改仍需Owner确认是两回事。见 [OWNER_DECISION_APPLICABILITY.json](OWNER_DECISION_APPLICABILITY.json)。原G的4项场景问题不在本D范围，没有顺带裁决800是否合理。

## 当前交付与下一步

[DiagnosisReport.json](DiagnosisReport.json)、[MinimalDiscriminatingExperiment.json](MinimalDiscriminatingExperiment.json)、[RequirementOrImplementationIssue.json](RequirementOrImplementationIssue.json) 及提案均已完成；[FindingDisposition.json](FindingDisposition.json) 状态为DIAGNOSED_IMPLEMENTATION_MISMATCH_NOT_FIXED。原D002输出与GlobalProfileGate不改写。D003诊断职责完成，后继为manager消费→Owner修改确认→新D实施回归→X/G；不是已修复或FeatureRelease。

Owner七项进度：D001已接收；X已完成；准确结果来自D002一次新生产；原正式ts已运行结束、本C未启动Feature；目录仍为D002/store绑定实例；G1–G8已完成且未重复；本D无事实阻断，正式修复尚未授权。无Worker、无新委派、无跨线程发送，仅写授权工作区和本Run记录。专业结果先发布，再以已有exact提交形成C0007 PRO_RETURN，待原manager消费。
'''
(ROOT/'EXECUTOR_REPORT.md').write_text(text)
write('DIAGNOSIS_BUILD_AUDIT.json',dict(completed_at=datetime.now(timezone.utc).isoformat(),finding='F800-GF-001',diagnosis='F800-DIAG-001',
    classification='ImplementationMismatch',repairability='PROVEN_NOT_ADJUSTABLE',formal_behavior_changed=False,workers=[],owner_decision_packet_applicable=False))
print('NATIVE_DIAGNOSIS_ISSUE_EXPERIMENT_AND_MODIFICATION_PROPOSAL_WRITTEN')
