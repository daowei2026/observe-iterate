"""D006 原Skill诊断材料；只消费有效D005结果与本C只读/纯函数证据。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import csv,json,subprocess

ROOT=Path(__file__).resolve().parent
PRIOR=ROOT.parent/'D005'
RUN='OI-F800-STAT-20261122-01'
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c'
FRP='be57d6752c9d43d10f1d670e1d2993bb8153ea7c'
PRIORCOMMIT='38e2af72be826a1e98fd7f5d4522c50d218750f3'
def load(p):return json.loads(p.read_text())
def write(n,v):(ROOT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def table(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def prior(n):return f'daowei2026/observe-iterate@{PRIORCOMMIT}:longrun/runs/{RUN}/professional/D005/{n}'
expect=load(ROOT/'FrozenExpectation.json')
probe=load(ROOT/'PNV_INPUT_PROBE.json')
binary=load(ROOT/'BINARY_BOUNDARY_PROBE.json')
source=load(ROOT/'SOURCE_EVIDENCE.json')
audit=load(ROOT/'SOURCE_REF_AUDIT.json')
scope=load(ROOT/'coverage_probe_scope.json')
native=table(ROOT/'NATIVE_COVERAGE_REPLAY.csv')
controls=table(ROOT/'NATIVE_COVERAGE_CONTROLS.csv')
viol=table(PRIOR/'profile/violations_complete_flag_with_input_price_gap.csv')
old=table(PRIOR/'comparison/price_gap_baseline.csv')
assert probe['completed'] and binary['completed'] and len(probe['symbols'])==3
assert all(s['rows']==49683 and s['missing_rows']==69 and s['exported_close_equal'] and s['raw_encoded_nan_bits']==['0x7ff8000000000000'] and s['uti_step_values']==[600] and s['self_calendar_comparison']['present']==0 for s in probe['symbols'])
assert all(s['results'][0]['prices_equal'] and s['results'][-1]['prices_equal'] for s in binary['results'])
assert source['frp_head']==FRP and source['frp_clean'] and len(source['source_files'])==16
assert audit['count']==51 and audit['exact_objects_available'] and audit['owner_original_byte_equal'] and audit['packet_invocation_equal']
assert len(controls)==8 and all(x['passed']=='True' for x in controls)
modes=['actual','intervention','proposed_input_missing_intervention']
maps={m:{int(x['uti']):x for x in native if x['mode']==m} for m in modes}
assert all(len(x)==1672 for x in maps.values())
cases=[]
for row,before in zip(viol,old):
    u=int(row['known']);assert row['revision']==before['new_revision']
    assert before['old_flag']==before['new_flag']==row['groupCoverageIncomplete']=='0'
    flags={m:int(maps[m][u]['domain_coverage_incomplete']) for m in modes}
    assert flags==dict(actual=0,intervention=1,proposed_input_missing_intervention=1)
    cases.append(dict(life=row['life'],revision=row['revision'],timestamp=row['timestamp'],known=u,
        native_D005_flag=0,old_baseline_flag=0,actual_coverage_replay=0,
        source_failure_intervention=1,input_missing_intervention=1,
        per_symbol_actual_missing=69,case_is_published_D005_output=True))
assert len(cases)==8 and len({r['life'] for r in cases})==5 and len({r['known'] for r in cases})==6
resumed=93715799;recovered=resumed+480000
for mode in modes[1:]:
    assert int(maps[mode][93673799]['domain_coverage_incomplete'])==0
    assert int(maps[mode][93674399]['domain_coverage_incomplete'])==1
    assert int(maps[mode][recovered-600]['domain_coverage_incomplete'])==1
    assert int(maps[mode][recovered]['domain_coverage_incomplete'])==0
    assert float(maps[mode][recovered]['rb_coverage_from'])==resumed
with (ROOT/'DIAGNOSED_CASES.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(cases[0]),lineterminator='\n');w.writeheader();w.writerows(cases)
evaluation=dict(completed=True,finding_id='F800-GF-002',formal_feature_executed=False,scope=scope,
    actual_function_calls=['be57 klineForwardCoverage','be57 advanceMaterial','be57 accumulateForwardCoverage (via advanceMaterial)'],
    modes={m:len(v) for m,v in maps.items()},published_cases=cases,
    checks=dict(raw_pnv_3_symbols_pass=True,binary_boundary_controls_passed=12,native_controls_passed=8,
        same_8_published_flags_reproduced=True,both_failure_interventions_incomplete_at_all_8=True,
        pre_gap_complete=True,first_missing_incomplete=True,restoration_at_94195799=True),
    limitation='独立纯覆盖子链重放，不运行buildKLineGroupSource的Reflex图、不生产F候选/UUID，也不声称测得修后完整Revision/Life总量；实际入口弃价与无过滤由准确源码链证明。')
write('ExperimentEvaluation.json',evaluation)

parameters=dict(suspected_parameters=['observation_multiple=800','delta=600','固定2Δ=1200','freq=5m','units_per_open_minute=120','units_per_calendar_tick=1','6Δ等待/修订尾部','18Δ handoff','ScaleTurn上游选择参数'],
 parameter_consumers=[
  dict(parameter='800×600',definition='GroupCandidateTypes.hs:groupObservationDuration',consumers=['GroupCandidateMaterial.hs:covered/eligible','GroupCandidateEvolution.hs:formationQuestions/deadline'],effect='改变观察期限和连续覆盖所需长度；不参与报价有效性或CoverageCondition分类'),
  dict(parameter='delta=600 / hardcoded 2',definition='FormationProfile / GroupCandidatePairs.hs:assessPair',consumers=['pair temporal distance <= 2*formationDelta'],effect='改变pair资格；不改变缺价事件被发行Observed这一事实'),
  dict(parameter='freq/Calendar units',definition='GroupCandidateKLineInput.hs:klineUTIStep/groupKLineEvents',consumers=['源Int64相邻步长600','报价位置商及Clock'],effect='同频率实际步长精确为600；缺价前中后UTI仍真实相邻，修改步长会错断有限价正常流且不表达缺价区别'),
  dict(parameter='hardcoded 6,18',definition='Material waiting / Evolution revisionEnd / Decisions handoff',consumers=['6Δ未知Clock等待','deadline+6Δ修订尾部','revisionEnd+18Δ交接'],effect='位于覆盖分类后或平行职责，不能使NaN发行InputMissing'),
  dict(parameter='ScaleTurn相关参数',definition='完整配置sources[*].input.scale_turn',consumers=['上游转折/锚点选择'],effect='可改变候选输入和发行人群；正常coverage每拍仍直接取KLine，不能修复丢失价格有效性的信息')],
 earliest_business_divergence='GroupCandidateKLineInput.hs:advance把(价格,UTI,位置,Clock)解构为(_,known,_,u)，无条件Observed并更新previous；进入Material前已丢失有效观测与缺价区别。',
 feasibility_status='PROVEN_NOT_ADJUSTABLE',
 feasibility_evidence=[
  '在当前已明确配置能力内，无任何参数控制有限价格检测或失败分类；800、600、2Δ又由Owner固定。',
  '即使不诉诸固定值约束，两个无Turn流在相同UTI/Clock上仅价格不同（有效值/NaN）也会被当前adapter投影为相同frameCoverage，Material对所有参数收到同样输入，不能同时满足有限价可完整、真实缺价须断开的区别。',
  '将观察期拉长到超出全部历史会把正常流也标不完整；缩短期使部分窗口不再包含缺口仅改变预期适用位置；改变频率/对象域/日历则改变问题或破坏正常相邻对照。均非修复当前固定实例。',
  '原生同一800×600重放仅更改缺价分类即使8/8从0变1，且满窗恢复；Material已有能力处理SourceFailure/InputMissing，无需标定。'],
 upstream_dependency='真实PNV缺口存在；恢复原数据可能消除本样本暴露条件，但不补足adapter对未来缺价的表达能力。未确定数据生成/供应端缺失原因。',
 unresolved_constraints=['修后全图发行、Revision/UUID和下游影响须Owner批准后新版本完整X/G实测；本C不求解新参数或改现有配置。'],
 next_route='现有合同已明确缺价断开：实现修正角色，先由原manager提交F800-MP-002获Owner明确确认；本案无需参数标定或重定义业务预期。')
write('ParameterRepairability.json',parameters)

def stage(name,inp,rule,state,out,actual,confirm,version,loss):
 return dict(stage=name,Input=inp,Rule=rule,State=state,Output=out,ActualTime=actual,ConfirmTime=confirm,Version=version,PossibleInformationLoss=loss)
chain=[
 stage('A 原始PNV/Calendar对齐','SOF.pnv_dir/5m/{rb,hc,i}_night_end_at_2300；AtSelf对照',
  '实际文件本就编码NaN；KDataLoader及native loadBitsDba不补值；不能把Calendar存在的时格当有效报价',
  '69格OHLC全NaN、volume=0；self对应69时刻无记录，前后同值报价存在',
  'close=NaN，closeUti/closeTs有效且步长600','2023-03-10 21:05至2023-03-13 15:00，UTI93674399..93715199',
  '文件是本次已冻结SOF历史观测，不为每个缺失记录发明确认时间','实际D005同SOF物理文件SHA见PNV_INPUT_PROBE；BINARY_BOUNDARY_PROBE',
  '消费数据已无价格；其上游为何无记录未定位，不能凭缺失推断市场休市或实际成交情况'),
 stage('B native载入与事件调度','原PNV Bar及closeTs历史轴','Tis.loadKLineEvent→lookupHistoryData→mergeGroupHistoryData→pushAlways；不按价格过滤',
  '每个有效时间位置被调度；transEBar/close字段原值映射','包含NaN close的KLine Tick与同拍有效UTI',
  'Bar closeTs原时刻','KLine同拍closeUti，作为当前known；没有额外确认延迟',
  'D005冻结runtime源码/接口和binary指纹，SOURCE_EVIDENCE',
  '本阶段不修补NaN、不前向填充；不能以CSV行存在单独证明事件，故已核调度实现'),
 stage('C 正常F KLine适配（最小责任）','groupKLineEvents生成(price,exactUTI,position,Clock)',
  'advance弃price；klineForwardCoverage只用Int64 UTI是否相邻，恒CoverageObserved，previous恒更新',
  '69个缺价时刻仍接600步长相邻边','对三个对象连续的Observed覆盖，缺价区别丢失',
  'known沿原UTI，Calendar Clock u=UTI','同拍，不把缺价变成迟到Turn/未来确认',
  'daowei2026/frp@'+FRP+':GroupCandidateKLineInput.hs#advance',
  '实际缺价→成功观测的错误分类；最早可局部修正的业务责任阶段'),
 stage('D Material覆盖累积','三个固定对象的Observed边；域complete=true、coverage=[]',
  'accumulateForwardCoverage连接真实相邻Observed；covered要求from<=u-480000且through>=u，或明确Inapplicable',
  '输入未带InputMissing/SourceFailure，连续区间跨过缺价；无未知Clock等待',
  'materialCoverageIncomplete=False','每次当前Calendar进展u','frameKnown为同拍源UTI',
  'daowei2026/frp@'+FRP+':GroupCandidateMaterial.hs#covered/accumulateForwardCoverage',
  '依据收到的条件按规则执行；已不能从ObjectCoverage恢复被C丢弃的价格有效性'),
 stage('E 观点/保存/独立读回','materialCoverageIncomplete=False',
  'Evolution将Material标记装入candidateDomainIncomplete；Storage编码Bool为0/1，OnlyRead独立导出',
  '8个已发布Revision/5Life/6时刻均为0；旧base同位置8/8也是0',
  'groupCoverageIncomplete=0，DIAGNOSED_CASES精确Life/Revision可追溯',
  '使用观点成员的原actual/confirm，不以当前known替代转折actual',
  '93727799..94102199六个发行known，均在缺口仍处800Δ窗的位置',
  prior('FeatureRunResultBinding.json')+'；'+prior('profile/violations_complete_flag_with_input_price_gap.csv'),
  '没有读回层反转标记证据；完整候选发行影响未在本C重跑。')]
explanations=[
 dict(id='H1',explanation='CSV重建产生空行，真实源价格有效',prediction='原PNV相同位置为有限价或导出经过reindex/padding',check='物理DBA位值/头部坐标、DataFrame数组和导出比较',result='排除：实际消费PNV含NaN，49683行导出同轴同close；self无69位置且边界对照相等'),
 dict(id='H2',explanation='已有Calendar/domain不适用豁免',prediction='当前域或正常分支提供这些对象/区间的CoverageInapplicable或既定缺价即豁免规则',check='完整配置及实际GroupKLineConfiguration代码分支和覆盖枚举',result='排除本固定实例：完整rb/hc/i域无豁免，正常路径只发Observed；Calendar有时格不构成缺价豁免'),
 dict(id='H3',explanation='NaN行在进入F前已被过滤，F只见真实间隙',prediction='native历史轴或close映射有有限价筛选；实际仅收到两端事件',check='Tis加载、历史调度、Host pushAlways、wrapTickEvent、merge close/UTI',result='排除：按每个closeTs发Bar，映射不筛NaN；若真过滤，be57准确步长本可断开，这不是现有路径'),
 dict(id='H4',explanation='覆盖只承诺时间时格存在，不承诺有效观察',prediction='存在预先定义且与缺价断开合同可协调的不同coverage含义',check='FrozenExpectation原文、Material既有缺价/失知/间隙断开注释及Coverage条件',result='排除作为当前合同解释：单有UTI是时间事实，不能取消已冻结缺价条件；未改写原预期'),
 dict(id='H5',explanation='正常KLine适配丢弃缺价信息，恒发行Observed',prediction='实际源有NaN但正常分支不检查price；标失败反事实只改分类便使Material断开',check='准确源码+1672拍三模式原生函数重放+8项控制',result='确认：8/8原观点覆盖标记可复现；两种失败类别均变不完整，恢复满800Δ才完整'),
 dict(id='H6',explanation='be57数值相邻修复引入新回归',prediction='同自然Life/known旧base无该flag=0现象',check='已有效D005自然对象基线比较8行',result='排除：8/8旧base也为0；当前新识别的既存缺陷，不重新打开GF001')]
facts=[
 dict(fact='当前D005完整X、独立31表读回、G有效；当前配置800/600、2Δ和精确版本绑定未变',evidence=[prior('FeatureRunResultBinding.json'),prior('GlobalProfileGate.json'),'INPUT_BINDING.json']),
 dict(fact='GF002观察量8Revision/5Life/6known；每窗801点，三品种各有同一69个close缺值；8/8旧base已存在',evidence=[prior('MISSING_INPUT_WINDOW_VALIDATION.json'),prior('comparison/price_gap_baseline.csv'),'DIAGNOSED_CASES.csv']),
 dict(fact='当前源PNV明确存NaN位0x7ff8000000000000，非导出临时占位；AtSelf对应69时刻均缺记录，前后值和时间能对上',evidence=['PNV_INPUT_PROBE.json','PNV_GAP_EXCERPT.csv','BINARY_BOUNDARY_PROBE.json']),
 dict(fact='native读数据与调度未滤NaN；当前正常adapter弃price、恒Observed、恒更新previous',evidence=['SOURCE_EVIDENCE.json']),
 dict(fact='当前固定域无不适用豁免；Material已有缺价/失败断开能力',evidence=['SOURCE_EVIDENCE.json','NATIVE_COVERAGE_CONTROLS.csv']),
 dict(fact='原生覆盖子链三模式各1672拍；8/8实际模式=0，两种缺价干预=1；输入恢复后首个完整点94195799',evidence=['ExperimentEvaluation.json','NATIVE_COVERAGE_REPLAY.csv']),
 dict(fact='GF001已在D005新完整结果关闭，D006不修改其判定；本C无正式生产、源采用、Q/V或WALL执行',evidence=[prior('FindingDisposition.json'),'WORKFLOW_COMPLETION.json'])]
diagnosis=dict(diagnosis_id='F800-DIAG-002',finding_id='F800-GF-002',expectation_id=expect['expectation_id'],expectation_version=expect['version'],
 discrepancy_statement='在固定rb/hc/i、5m、night_end_at_2300正常KLine输入的800Δ窗内，实际消费PNV有69个非豁免缺价点；8个已发布观点却为groupCoverageIncomplete=0。条件前件经原始DBA/AtSelf/当前合同核验成立。',
 business_impact='完整覆盖标记对5/480 Life的8/1534观点给出过强保证（1.0417% Life；0.5215% Revision；完整标记1526中占0.5242%）。覆盖使用者可能把含真实缺价的观察窗当完整；未量化Q/V实际业务损失，也未宣称方向/转折正文错误。',
 confirmed_facts=facts,processing_chain=chain,competing_explanations=explanations,
 ruled_out_explanations=['H1','H2','H3','H4','H6'],remaining_explanations=[
  dict(id='UPSTREAM_ORIGIN',status='非根因竞争项，源数据缺失原因仍未定',detail='为何self PNV在69时刻没有行情、Calendar PNV生成端何时/为何补NaN，当前未追溯供应端；不影响缺价作为实际输入及adapter错误分类的定位，不提交Owner猜事实。')],
 discriminating_checks=['PNV_INPUT_PROBE.json','BINARY_BOUNDARY_PROBE.json','SOURCE_EVIDENCE.json','ExperimentEvaluation.json'],
 current_localization=dict(primary_stage='C 正常KLine→FormationFrame适配',classification='ImplementationMismatch',
  responsibility='GroupCandidateKLineInput.hs:buildKLineGroupSource.advance在有效UTI上丢弃价格有效性并恒发CoverageObserved；不是Material不认识失败、读回反转或800数值太大。',
  earliest_trigger='输入A已有缺价；最早合同责任偏差为C把无价格的Calendar时格当成功观测。',
  conditional_expectation='已成立，FrozenExpectation原件未改写',regression_class='本轮新识别的既存缺陷，旧base同位置8/8已存在'),
 parameter_repairability=parameters,
 confidence=dict(level='HIGH',basis='物理文件、边界对照、准确入口/调度代码和实际原生Material函数的可区分重放相互印证',
  limits=['未暴露原正式运行的逐拍frame内部轨迹；通过源码和当前库纯函数重放定位，未伪装为正式引擎录制。','原始缺失供应端成因及正式修后候选/Revision总量尚未确定。']),
 next_route='原manager消费本D006；按L0将新F800-MP-002及diff/影响/验证方案提交Owner确认。批准后方可实施、提交/采用新版本并完整X/31表读回/G复验；当前D005原件保持，不提前释放。')
write('DiagnosisReport.json',diagnosis)
experiment=dict(experiment_id='F800-MDE-002',expectation_id=expect['expectation_id'],finding_id='F800-GF-002',
 question='公开空OHLC是否实际非豁免缺价，以及最早为何被当完整覆盖？',
 ordered_checks=[
  dict(order=1,cost='只读已有8观点/3输入表与旧base，无新生产',evidence=prior('MISSING_INPUT_WINDOW_VALIDATION.json'),observation='69点均在8个801点窗口；8/8旧base也为0'),
  dict(order=2,cost='限定三品种七个已知PNV文件指纹+自日历2字段对照，未搜索数据树',command='probe_inputs.py 经D005/run_in_runtime.py执行',evidence='PNV_INPUT_PROBE.json',observation='三品种实际NaN69、self无69位置；不是CSV重建'),
  dict(order=3,cost='标准库mmap只读头部和12个边界点',command='python probe_binary_boundaries.py',evidence='BINARY_BOUNDARY_PROBE.json',observation='缺失位在原文件，前后self与Calendar有限价相同；排除self时间轴整体错位'),
  dict(order=4,cost='仅16个相关源码文件及实际配置',command='capture_source_evidence.py',evidence='SOURCE_EVIDENCE.json',observation='native事件无过滤；当前adapter弃价；无豁免分支；Material有失败类别'),
  dict(order=5,cost='同当前库三个纯函数模式，各1672拍×3对象；无Feature/引擎/共享生产写入',command='stack --stack-yaml <D004 current runtime>/edh-universe/stack.yaml exec -- runghc -package=frp NativeCoverageProbe.hs coverage_probe_input.csv',evidence='NATIVE_COVERAGE_REPLAY.csv',observation='实际Observed模式复现8个0；SourceFailure和InputMissing干预在8位置均为1，94195799恢复0'),
  dict(order=6,cost='8个有区分性的原生覆盖控制',command='同一stack exec runghc -package=frp NativeCoverageControls.hs',evidence='NATIVE_COVERAGE_CONTROLS.csv',observation='冷启动、无Turn正常全窗、单对象失败/缺价/失知、真实UTI间隙和显式不适用均符合既有合同')],
 changed_variable='仅缺价事件的CoverageCondition及其previous成功邻接状态；UTI、Clock、800、600、固定域均相同。',
 pre_registered_discrimination='若真实源有效/既有豁免成立则拒绝GF002；若源缺价且adapter丢弃区别、失败分类使Material按原约束断开则定位adapter。条件预期在D005已冻结，本C不由结果新增阈值。',
 result='后者成立，最小责任阶段已定位；不需要扩大正式统计或盲调参数。',
 implementation_boundary=evaluation['limitation'],
 execution_issues=[dict(attempt='input probe 1/2',result='失败，DbArray要求自有dtype包装或字符串，numpy类型与numpy.dtype均不适用',resolution='查实际DbArray接口后改用f8字符串；失败日志完整保留，第三次退出0'),dict(attempt='ghc-pkg field 1',result='多字段命令未逗号分隔而syntax error',resolution='改用id,import-dirs,library-dirs，成功记录实际包路径；不改环境/Feature')],
 evidence='ExperimentEvaluation.json')
write('MinimalDiscriminatingExperiment.json',experiment)
issue=dict(issue_id='F800-ISSUE-002',finding_id='F800-GF-002',diagnosis_id=diagnosis['diagnosis_id'],classification='ImplementationMismatch',
 secondary_classification=dict(type='DataQualityIssue',scope='实际消费PNV确实无价格；供应/生成侧原因未定位，不能承诺修好数据即修好adapter'),
 excluded_classifications=dict(BusinessRuleInsufficiency='已有缺价断开合同和失败枚举，并非本次新增业务规则',InputPurposeMismatch='正常KLine可以用于该固定观察目的，失败须保留为失败',UnresolvedTradeoff='没有必须由Owner裁决的目标取舍事实缺口'),
 trigger='normal KLine close为NaN且closeUTI有效/相邻；三对象2023-03-10夜盘至03-13日盘各69行真实样本',
 expected='该对象覆盖断开；恢复首个有效报价后从新成功点累计800Δ，不以时格存在代替观测成功',
 actual='无条件Observed连接跨过缺价，8个真实观点flag=0',
 minimal_responsibility=diagnosis['current_localization'],
 parameter_repairability='PROVEN_NOT_ADJUSTABLE，详见ParameterRepairability.json',
 business_impact=diagnosis['business_impact'],
 reproduction=['probe_inputs.py','probe_binary_boundaries.py','NativeCoverageProbe.hs','NativeCoverageControls.hs','DIAGNOSED_CASES.csv'],
 proposed_resolution='见F800-MP-002：正常adapter按有限close决定Observed/InputMissing，失败时清previous，Calendar进展照常；正式改变待独立Owner确认。',
 fix_applied=False,approval_from_MP001_does_not_cover_this_change=True,
 next_route='原manager按L0形成Owner修改确认；批准后由实现修正角色实施，保持GF001及精确步长合同。')
write('RequirementOrImplementationIssue.json',issue)
write('OwnerDecisionApplicability.json',dict(owner_decision_packet_applicable=False,
 reason='本案技术事实已由只读对照和最小重放解决；现有冻结覆盖合同明确，没有两种业务目标的未决取舍。故不造OwnerDecisionPacket，也不请Owner猜NaN或Calendar事实。',
 modification_confirmation_required=True,proposal_id='F800-MP-002',
 distinction='Owner确认新正式行为修改来自原FULL_ASSIGNMENT/L0边界，与Skill第三类业务取舍决策不同；本E1仅提交可审阅提案，由原manager发起确认。'))
impact=dict(impact_id='F800-MP-002-IMPACT',proposal_id='F800-MP-002',base_frp='daowei2026/frp@'+FRP,
 source_change='GroupCandidateKLineInput.hs:advance三处，见未应用diff；不改数据/正式配置/对外字段。',
 unchanged_intent=['observation_multiple=800','delta=600','2Δ=1200','Int64源UTI精确相邻步长','缺口/冷启动/恢复前不得倒灌覆盖','既有actual/confirm/known职责','F-only rb/hc/i 5m 2021—2023及同SOF/Calendar'],
 data_contract=dict(schema_or_field_change=False,new_saved_product=False,new_source_owner=False,
  semantic_effect='groupCoverageIncomplete在真实缺价窗按既有含义更保守；不是字段结构变更。',
  identity_effect='该标记参与候选正文和稀疏发行变化；Revision数量、发行时点和UUID/exact链可能变化，不能从8样本推算全量结果；新运行身份需重新绑定、独立读回。'),
 upstream=dict(PNV='保持冻结输入原样；不回填、不重建、不采纳未经确认的数据修复',ScaleTurn='不修改其规则或当前配置；候选Turn内容预期不因本局部代码主动改变，但须完整运行对比',Calendar='保留有效Clock/UTI进展，不能删除缺价时格以掩盖800Δ观察义务'),
 downstream=dict(F='直接改变其正常覆盖输入，需完整复验',Q='共享正常适配路径，存在行为影响可能；Q现有另一路数值边界限制继续传递。本Run不运行Q/V、不签Q释放，后续使用前须新依赖版本/语义核对',V='通过F/Q证据受影响，未验证实际业务后果',WALL='无授权/无改动'),
 understanding_update='若批准并实施，只补当前版本变化、覆盖分类/依赖语义与结果绑定，不重做已接受的完整Feature Understanding。',
 validation_plan_ref='ModificationProposal.json#validation_plan')
write('ContractAndDependencyImpact.json',impact)
proposal=dict(proposal_id='F800-MP-002',status='PROPOSED_NOT_AUTHORIZED_NOT_APPLIED',finding_id='F800-GF-002',
 problem=diagnosis['discrepancy_statement'],reason_for_new_confirmation='F800-MP-001仅批准准确UTI相邻修复及复验；此次新增close有效性覆盖分类及其previous重置，超出原批准。',
 base=dict(frp='daowei2026/frp@'+FRP,tis='daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767',configuration_sha256='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'),
 concrete_change=[
  '在buildKLineGroupSource.advance保留同拍close价格；validPrice = 非NaN且非Infinity。有效有限close保持现有Observed及准确UTI相邻规则。',
  'close非有限时为该对象发CoverageInputMissing Nothing Nothing，previous成功邻接状态清空；不把零量本身定义成缺价，不根据有无Turn判断是否观测。',
  '缺价拍继续沿原有效UTI/Clock推进frame；不填价、不抛弃Calendar时格、不抹除已有Turn/失知状态，不改exactUTI对非法时钟的原处理。',
  '恢复首个有效close只发行当前成功点，后续真实600步长再累计；不跨缺口回接历史。'],
 reviewable_diff='F800-MP-002.proposed.diff',diff_applied=False,diff_compiled_or_integration_tested=False,
 evidence_before_approval=['DiagnosisReport.json','ExperimentEvaluation.json','NATIVE_COVERAGE_CONTROLS.csv','ParameterRepairability.json'],
 validation_plan=[
  dict(order=1,type='真实adapter分类回归',cases=['同UTI轴有限close与NaN/±Infinity的成对输入','覆盖warm后单缺价/连续缺价','只有一个固定成员失败','有限close且volume=0/无Turn仍Observed'],
   acceptance='必须执行正常KLine→frame分类位置，不能仅手造SourceFailure来代替分类测试；有效Clock仍推进，失败清previous，恢复先点后边。'),
  dict(order=2,type='既有覆盖/几何边界回归',cases=['GF001准确UTI相邻/真实步长缺口/冷启动/2Δ不变','失败/失知/明确不适用、无Turn观察、恢复满800Δ的前/等号边界','revision尾部/旧r资格与稀疏发行引用完整性'],acceptance='当前规则保持，缺价断开不回退已修GF001；测试失败不得采用。'),
  dict(order=3,type='代码提交与采用',acceptance='Owner明确批准后仅在Run授权工作区实施、回归、提交/推送FRP，并记录新code/binary/config/dependency binding；不沿用be57结果冒充新版本。'),
  dict(order=4,type='完整正式X及独立读回',acceptance='真实单写者+重型flock，完整rb/hc/i、5m、2021—2023、同SOF/night2300、800/600与2Δ；独立31表OnlyRead/字段哈希/引用及新身份读回。不以子链重放替代正式运行。'),
  dict(order=5,type='原Skill全量G复验',acceptance='重跑新版本完整G，复验8位置的对应自然对象和冷启动/GF00122+8控制；量化480基线自然Life/1534Revision/1216发行的真实变化及exact链，不能预设新计数。检查缺价窗flag冲突全量0，并保留场景问题及Q限制。'),
  dict(order=6,type='释放与依赖',acceptance='由原manager按原L1消费新X/G/问题处置后签FeatureReleaseGate/适用ReleasePackage；无批准或未通过前保留当前结果与诊断，勿提前释放。')],
 impact_ref='ContractAndDependencyImpact.json',
 risks_and_limits=['纯覆盖干预不证明完整修后发行/UUID不变。','共享适配代码可能影响Q，不能宣称Q/V已验证。','实际输入缺失供应端成因未修复，本提案只保证缺失不被称作完整。'],
 requested_authorization='请原manager将此准确提案、diff、影响及验证方案交Owner，明确是否批准该局部修正、回归、提交/推送采用及新完整F X/读回/G；本C未发Owner问题，也未实施。')
proposal.update(
 finding_ref=prior('GlobalFindingCandidates.json')+'#F800-GF-002',
 current_behavior=diagnosis['discrepancy_statement'],proposed_change=proposal['concrete_change'],
 why_this_stage='正常KLine适配是进入Material前最早丢弃价格有效性的责任边界；Material已有InputMissing/SourceFailure语义，局部修正可保留准确UTI步长和全部下游字段。',
 alternatives=[
  dict(option='修复正常KLine覆盖分类（本提案）',preserves='既有有效观测/缺价断开合同及冻结参数/范围',cost='需真实适配回归、代码采用及完整新X/G，发行身份变化须实测'),
  dict(option='仅修PNV历史数据',preserves='可消除此批实际缺价；须另核来源事实及输入版本',limitation='不能使adapter识别未来缺价；本C未定位供应端原因，不能擅自补值或采用修数据'),
  dict(option='标定800/600或改域/Calendar',limitation='不表达有限价/缺价区别；改变固定任务或掩盖问题，ParameterRepairability已给不可调证明'),
  dict(option='重定义coverage只代表时间时格',limitation='需另立业务目的/新预期，违背当前冻结缺价合同；非本技术修正提案')],
 expected_effect='在同一原始缺价输入和相应自然对象/known，覆盖应不完整；纯子链8/8已支持该预测。正式修后Life/Revision/发行总量及UUID不预设，须完整X/G实测。',
 possible_side_effects=impact['data_contract']['identity_effect']+' '+impact['downstream']['Q'],
 files_or_parameters_to_change=['src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs（仅advance价格覆盖分类与previous成功状态）','新增有必要的真实适配回归；不改正式参数、硬编码常量、PNV、保存schema或业务范围'])
write('ModificationProposal.json',proposal)
write('FindingDisposition.json',dict(finding_id='F800-GF-002',diagnosis_id='F800-DIAG-002',status='CONFIRMED_IMPLEMENTATION_MISMATCH',
 conditional_premise='VERIFIED_FOR_CURRENT_FIXED_INSTANCE',closed=False,fix_applied=False,preexisting=True,
 evidence=['DiagnosisReport.json','PNV_INPUT_PROBE.json','BINARY_BOUNDARY_PROBE.json','ExperimentEvaluation.json'],
 new_proposal='F800-MP-002',next_route=diagnosis['next_route'],
 preserved_GF001=prior('FindingDisposition.json'),preserved_D005_gate=prior('GlobalProfileGate.json'),
 no_new_feature_release_gate_issued=True))
steps=[('S1','复述准确偏差及影响'),('S2','逐阶段Input/Rule/State/Output/ActualTime/ConfirmTime/Version/InformationLoss'),
 ('S3','事实和竞争解释分列'),('S4','诊断树及可区分预测'),('S5','只读/源码/对照/小重放的低成本检查'),
 ('S6','最小责任定位及参数能力初筛'),('S7','核原预期适用性：条件前件成立，无需改写冻结版本'),('S8','实现修正/独立MP与适用Owner决策边界路由')]
write('WORKFLOW_COMPLETION.json',dict(skill_ref=f'daowei2026/observe-iterate@{PIN}:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md',
 steps=[dict(step_id=k,description=v,completed=True) for k,v in steps],
 native_outputs=['DiagnosisReport.json','MinimalDiscriminatingExperiment.json','RequirementOrImplementationIssue.json'],
 optional_owner_decision='不适用，见OwnerDecisionApplicability.json',
 completion_boundary='D006诊断工作完成；GF002修复、新X/G、Feature释放与manager消费不属于已完成。'))
validation=dict(completed=True,checked_at=datetime.now(timezone.utc).isoformat(),
 exact_refs=51,dispatch_blob_match=True,raw_pnv_probe=True,binary_controls=12,native_controls=8,native_replay=dict(modes=3,rows_each=1672,diagnosed_cases=8),
 frozen_expectation_unchanged=True,primary_issue='ImplementationMismatch',feasibility_status='PROVEN_NOT_ADJUSTABLE',
 formal_feature_run=False,source_modified=False,source_commit_or_push=False,proposal_applied=False,
 previous_X_G_and_GF001_preserved=True,workers_empty=True,workflow_steps_complete=True,
 previous_gate_not_overwritten=True,release_not_claimed=True,owner_approval_not_extended=True)
write('VALIDATION.json',validation)

report=f'''# D006｜GF-002条件覆盖诊断与独立修改提案

GF-002已确认是正常KLine适配的既存实现偏差。当前实际消费的PNV中，三品种各69个位置确实没有有效价格；当前固定域无不适用豁免。适配器却丢弃close有效性、仅按有效且相邻的UTI恒发行CoverageObserved，使8个已发布观点的`groupCoverageIncomplete=0`。这不是本次CSV临时补空、读回反转、800参数标定问题或be57新引入的回归。

本C完成D006原Skill诊断并提出 **F800-MP-002**；未实施、提交或采用Feature改变，未重跑有效X/G。原GF001关闭结论和D005全部原件保留。新正式行为改变须由原manager携本提案向Owner取得独立确认，MP001批准不外延。

## 准确输入与授权

- 委派：`daowei2026/observe-iterate@f076db5afb51cc6b02502007713d7f83be97b9ad:longrun/runs/{RUN}/delegations/D006/DELEGATION.json`，C0014，原E1，workers=[]。
- 方法：`daowei2026/observe-iterate@{PIN}:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md`；本次亲自读取，既有适用补充沿准确版本复用。FULL_ASSIGNMENT及Owner最新原文按原件读取，51项exact来源和远端I/D blob匹配见审计。
- 冻结预期`F800-INV-COVERAGE-GAP-002`原文见FrozenExpectation.json；先核前件而非预置NaN必然是缺陷。D005适配包`F800-DA-D005-complete_flag_with_input_price_gap`保持原文。
- 当前FRP `{FRP}`、TIS `2f460d663d821cf2ba25555eda13e78b697d0767`，配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；800、delta600、2Δ=1200和原SOF/Calendar/范围保持。
- 只在BASE本D006产物目录和Run记录分支写诊断/记录；没有新正式生产、源代码写入、源采用/推送、Q/V或WALL工作。

## 结论依据与边界

1. 直接读取SOF的三个实际Calendar PNV目录，与D005导出的49,683行逐一核同轴/close相同。每品种69行OHLC全NaN，close物理编码为`0x7ff8000000000000`，UTI仍按600相邻。自日历PNV在这些69时刻没有记录；缺口前后有限报价均存在且与Calendar文件相同。另用标准库mmap独立核12个边界点，排除自日历时间轴整体错位。证据：PNV_INPUT_PROBE、BINARY_BOUNDARY_PROBE、PNV_GAP_EXCERPT。
2. 真实读取链为PNV→native Bar→closeTs逐拍历史调度→close/closeUti同拍事件；此链未过滤NaN。当前配置为complete=true的rb/hc/i固定域、coverage=[]，实际正常KLine分支没有不适用豁免。Material既有合同要求缺价/失知/未观察间隙断开，不能以Calendar时格存在取消该合同。16个窄范围源码/消费点及当前库接口指纹见SOURCE_EVIDENCE。
3. 最小责任阶段是`GroupCandidateKLineInput.hs:buildKLineGroupSource.advance`：它将报价解构为`(_,known,_,u)`，丢弃价格，只以UTI调用恒Observed的`klineForwardCoverage`，并恒更新previous。Material有合法InputMissing/SourceFailure处理能力，但在收到frame前已失去该区别；观点/保存按收到的标记表达。
4. 使用同一be57已安装原生库的实际`klineForwardCoverage`、`advanceMaterial`（含真实累积函数），三模式各重放1,672拍×3对象。实际Observed模式复现8/8已发布flag=0；仅把缺价分类改为SourceFailure或提案的InputMissing并清邻接状态，两模式8/8均为不完整。恢复首个有效点为UTI93715799，满480000后UTI94195799才重新完整。8项控制验证冷启动、无Turn正常流、单对象失败/缺价/失知、真实间隙和明确不适用。
5. 已有旧base同自然对象/known比较8/8也是0，因此是本轮新识别的既存缺陷，未重新打开GF001。当前受影响8/1534 Revision（0.5215%）、5/480 Life（1.0417%）、6个known，完整标记1526中占0.5242%。未量化Q/V损失，不据此断言转折正文或所有业务判断错误。

纯函数重放仅验证覆盖子链，不运行Reflex生产图、不生成新候选/UUID，也不是修后完整正式结果。原正式运行未暴露逐拍frame轨迹；入口分类由准确源码证明，后果由原生子链重放验证。上游行情为何缺失仍未追溯至供应/生成端；该事实缺口不影响adapter把实际缺价错称成功观测的定位。

## 参数能力与后继

ParameterRepairability状态为`PROVEN_NOT_ADJUSTABLE`，仅针对当前已明确参数能力。800×600控制期限；2Δ控制pair贴近；freq/Calendar换算控制UTI步长；6Δ/18Δ控制等待/修订/交接；它们均不消费价格有效性。相同UTI/Clock、无Turn且仅价格有限/NaN不同的输入，会被当前适配投影成相同覆盖，对所有这些参数不可区分。拉长至所有窗口均不完整或改变域/Calendar/范围是掩盖或改变问题，不能修复当前合同；无需盲调或正式参数标定。

RequirementOrImplementationIssue主类为ImplementationMismatch；实际PNV缺价是并存数据质量事实，供应端原因未定位。没有尚待Owner选择的业务目标取舍，因此不造OwnerDecisionPacket；OwnerDecisionApplicability说明了这一点。新正式行为确认则按FULL_ASSIGNMENT/L0单独执行。

F800-MP-002附未应用的可审阅diff：正常适配保留close；有限价沿原精确UTI规则Observed，非有限价发CoverageInputMissing并清previous，Clock进展仍保留；恢复先成功点后相邻边。不按零量或无Turn判失败，不填价，不改800/600/2Δ、配置/域/范围或对外schema。验证方案要求真实适配分类回归、原GF001/覆盖边界回归、批准后提交采用新FRP并完整三年X、31表独立读回及原Skill全量G，实测Revision/发行/UUID链变化。

共享正常适配可能影响Q；Q另一路数值边界限制继续保留。本Run不运行或释放Q/V。无新FeatureReleaseGate/ReleasePackage；原D005 GlobalProfileGate=DIAGNOSIS_REQUIRED保持原件，由manager消费诊断和批准后的后继成果按原L1处理。

## 原Owner要求的进度

| 项目 | 当前准确状态 |
|---|---|
| D001 | 已接受；未重做完整Feature Understanding |
| X是否开始 | D005新be57完整正式X已完成且有效，本C不重复 |
| 复用/新生产 | 复用D005合法结果及独立31表读回，不把存在目录当可复用证明 |
| 正式进程 | D005真实进程已退出0并释放生产锁；本C未启动Feature |
| 当前结果目录 | `{load(PRIOR/'FeatureRunResultBinding.json')['result_identity']['full_dir']}` |
| G全量统计 | D005 G1—G8已完成有效，26项结构检查0冲突，GF002本候选8点已在本C诊断；未重统计 |
| 当前阻断/后继 | D006诊断无事实阻断，工作已完成；正式修正待新MP002明确批准和新委派，当前不释放Feature |

## 原生交付与验证

DiagnosisReport、MinimalDiscriminatingExperiment、RequirementOrImplementationIssue、ParameterRepairability、ModificationProposal、ContractAndDependencyImpact，以及8个精确Case和输入/原生重放证据均在本目录。WORKFLOW_COMPLETION逐项对应原Skill步骤；VALIDATION记录实际检查。原V2 Return须先发布本专业结果并远端回读，再引用已有exact提交单独发布，回原manager。完整CLI与Codex manager身份的既有不兼容边界会如实记入Return校验；不改锁定gate、不伪造controller receipt。
'''
(ROOT/'EXECUTOR_REPORT.md').write_text(report)
(ROOT/'VALIDATION.md').write_text('''# D006核验边界

准确D006/C0014与当前Run Binding、锁定Skill/补充、Owner原文、D005有效X/G共51项exact来源已核；远端D/I blob与记录分支匹配。条件预期原件未改。

本C只读当前物理PNV、源码和有效结果；3品种69个缺价位置及12个物理边界核验通过。原生库覆盖三模式各1672拍，8个原观点位置实际模式为0，两失败干预为1；8个覆盖控制均通过。仅诊断纯函数链，不冒充正式Feature或修后全图测试。

Feature源码仍为干净be57，正式二进制/配置/结果沿D005原绑定。提案diff未应用、未编译或做真实适配整合回归，不存在本C源代码提交/推送/新生产。原GF001与D005 Gate不改，未签FeatureReleaseGate。改行为需独立MP002确认，旧MP001批准不外延。

Return发布阶段将使用未改的87b锁定schema及gate内validated/pro_state/object_ref_fields，并核真实I/D/Binding/权限/先行专业提交。旧版完整validate-executor-return的binding()硬编码chatgpt manager，与本Run Codex manager不兼容；不会伪造完整CLI通过或独立controller receipt。
''')
print(json.dumps(dict(diagnosis_id='F800-DIAG-002',conditional_premise='VERIFIED',classification='ImplementationMismatch',parameter_repairability='PROVEN_NOT_ADJUSTABLE',cases=len(cases),proposal='F800-MP-002',formal_feature_run=False,workflow_steps=8),ensure_ascii=False))
