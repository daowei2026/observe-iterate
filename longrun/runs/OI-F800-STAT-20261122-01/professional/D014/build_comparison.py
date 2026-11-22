"""原S2七个冻结案例逐过程判断；只读已接受材料，不构造Feature或图。"""
from common import *
from collections import Counter
from datetime import datetime
import uuid

fz = read_json(FROZEN, f'{PREFIX}/professional/D013/FrozenExpectationSet.json')
cs = read_json(FROZEN, f'{PREFIX}/professional/D013/CaseReviewSet.json')
expectations = {e['case_id']: e for e in fz['expectations']}
mapping, formal = formal_all()
data = {k: v['data'] for k, v in formal.items()}
price_ids = dict(rb='p1040', hc='p1168', i='p1296')
group_data = data['p1531']
frozen_ref = pro_ref('D013', 'FrozenExpectationSet.json', FROZEN)
material_ref = pro_ref('D012', 'ObservationMaterialPackage.json')
understanding_ref = pro_ref('D008', 'CurrentFeatureUnderstandingPackage.json', U)
html = BASE/'artifacts'/RUN/'caegraph-E/f800.html'
time_basis = dict(calendar='night_end_at_2300', timezone='Asia/Shanghai', sampling='5m',
    native_unit='CalendarUTITick', ticks_per_open_minute=120, delta=600, two_delta=1200,
    observation_width=480000, revision_tail=3600, handoff_tail=10800,
    actual='原转折所在坐标；不以K线x中点替代',
    confirm='逐条分列几何C与selected-known，另列T点pointKnownFrom',
    observed='本C对construction_snapshot的真实读图/原值读取时间，不伪作运行时as-of观测')

notes = {
1: dict(
 raw='原价先共同回落再反弹：2021-01-06 10:55→11:00→11:05，rb close 4319→4299→4312，hc 4473→4457→4466，i 1021.5→1015→1017。到各自几何C时rb4397/hc4602/i1051.5。其后仍有别的涨跌，窗口尾close为4303/4369/1044，不把旧谷点持久可引用当行情永久向上。',
 why='三个原始价格的共同谷点明确，上游实际T同刻而知识异步，是正例；两/三成员输出不先用作市场真值。',
 aligned=[
  '三处原价谷点及独立selected均指向72098999。rb/hc的几何C为09:50，selected-known为09:55；i几何C为11:30，selected-known为午休后的13:35。公开两成员首版在09:55、三成员首版在13:35，没有把这两次知识说成两次新谷点；内部每拍保留材料不在此证明范围。',
  '原价反弹与已选对象资格相符。两成员row2和三成员row3的所有已发行Required四项均CoordinateSupports，距离0；P/T/C原值分别保留。row4两成员Subsumed、CoveredBy指向三成员Life，previous指回本Life前版；不是把两Life机械合并。局部Supported与早期coverageIncomplete=1并列，到Jan19仅coverage变0，未改原谷点身份。',
  '两Life原anchor/deadline/revisionEnd不变。Jan21 22:25 groupClosed=1，三成员ClosedSupported、两成员仍Subsumed；22:55 participationDutyClosed=1。handoffEnd为原r+10800，未用它延长F修订责任。公开本Life没有后续重启；不由稀疏观点补每拍状态。'],
 scope='只支持本次共享谷点的公开身份、异步知识、Required、覆盖关系及有限责任表达；不证明全800窗口的每拍材料/漏报或交易用途。',
 maturity='公开过程已闭合且可逐exact复核；内部全轨迹仍MISSING。',
 divergence='在本次可读的发生、更新、覆盖关系和终止链未见与冻结预期相冲突的第一步；未公开的逐tick准入/原生coverage区间不能据此定位或宣布完全正确。'),
2: dict(
 raw='i原价从Jan4 13:35的996升至21:15的1034，邻近21:10为1029、21:20为1030，随后Jan5 09:35为1021。独立selected确认该峰，rb/hc下一夜已选峰分别在Jan5 21:45/21:40，不能当成Jan4的同时峰。冻结窗口尾i为1044，历史峰的局部形状不要求此后永不再涨。',
 why='i的真实已选峰存在，但独立rb/hc已选实际轴在±1200内均无对应T；当前共同资格负例。',
 aligned=[
  'i峰actual72032399、几何C72049199、selected-known72049799均可从独立投影还原；原价先上升再回落。确认时点不作为共同实际轴。',
  '独立rb/hc完整已选投影中，最近前点实际差28200，后点差45000/44400，均超过1200；没有第二对象的时间前提。完整1538个已发行观点中该i Turn成员查询为空，未见强拼晚峰或单成员共同组。此空是限定查询的ValidEmpty，未成组pair的Required/首阻断是NOT_EXPOSED。',
  '该上游历史记录仍在；本组合无已发行F Life，因此没有可要求的F终止。没有虚构Withdrawn/Closed或将别的附近Life归本峰。'],
 scope='只支持该i具体Turn未被无第二对象地拼成共同组；不外推所有i低参加率合理，也不声称实际内部TimeVeto已读到。',
 maturity='共同资格负例的独立时间前提和公开不拼组已可判；未成组内部阶段MISSING。',
 divergence='未观察到适用条件成立后的输出冲突；未成组pair本次内部枚举/Required/首阻断不可见，不能从无组定位实际拒绝步骤。'),
3: dict(
 raw='首根5m OHLC逐值从原表填入；首根内价格变化与左侧完整尺度前史是否可用分开，不由首点同刻推出已证实共同峰谷。',
 why='三品种首锚点同刻，是初始化误报候选；要检验不足是否被如实保留，不预设候选存在即误报。',
 aligned=[
  '首锚点72004199确在图左界，各自几何C/selected异步。初始首版row0在Jan4 10:05，成员方向/类型Unavailable、CandidateMember，局部Incomplete、coverageIncomplete=1；未伪称三处确定共同转折。完整尺度前史仍缺，不能反推初始化一定合理或一定错误。',
  '公开三对Required仅Time支持、距离0，Direction/Type/Bend分别Unresolved，gap为DirectionUnavailable/TurnTypeUnavailable/SelectedAnchorUnavailable；memberP始终为空。到Jan19 14:45 coverageIncomplete=0仍是Incomplete，未用时钟或coverage恢复补造方向/类型/P。',
  'Jan19 14:45 groupClosed=1、ClosedInsufficient；21:15 dutyClosed=1；previous串联同Life且原a/d/r不变。到期没有改成Supported，没有把不足过程当Pending无限延长。'],
 scope='只支持初始化不足表达、状态独立和有限闭合；原市场在图外是否存在可用前史仍MISSING，不认定所有初始化候选该删或该保留。',
 maturity='不足表达与有限结束已闭合；完整共同转折真值没有材料形成判断。',
 divergence='公开链未出现冻结预期所说的虚假提升；因左侧完整尺度前史不可得，无法对图外真实共同转折成立与否定位第一业务分歧。'),
4: dict(
 raw='rb在Feb10 09:45→09:50→09:55 close为4341→4340→4341，i在09:55→10:00→10:05为1021.5→1020.5→1023.5。两处谷点相差10开放分钟。春节前后价格继续变化；Feb18几何C时rb4506、i1079.5，知识跨日历假期到达，不是将原谷点搬到Feb18。窗口末rb4644/i1074.5。',
 why='这对真实谷点处于当前2Δ包含等号边界，用来核actual/知识与有限责任；不评价边界最优性。',
 aligned=[
  '独立selected与原价谷点一致：rb actual73127399、i73128599，差1200；i选中09:10，rb09:50。首版row44在Feb18 09:50，未以墙钟节假日或T点pointKnownFrom替代selected-known。',
  'row44 Required的Time/Direction/Type/Bend分别实读CoordinateSupports、NoGap/NoVeto，pairDistance=1200。memberP及T/C逐成员保留，未只凭Supported反填关系。此等号边界未被误排除，其他三项支持也有公开原值。',
  '原anchor73127399，deadline73607399、r73610999全程保持；Mar5 09:30 ClosedSupported且groupClosed=1，10:00 dutyClosed=1。previous同Life串联，不因确认迟到延长问题。'],
 scope='只支持此恰2Δ组合的公开资格和有限过程；不证明所有边界分支、800最优或逐tick准入事实。',
 maturity='本对已闭合、公开四项与时序可判；内部保留轨迹MISSING。',
 divergence='未见等号被拒、actual被确认替代或责任延长；内部准入全轨迹不暴露，不能对更早未发行阶段定位分歧。'),
5: dict(
 raw='Feb22 i在09:05 close1133，09:10回1130；hc09:15为4839，09:20到4856，再09:25回4848。两个峰真实存在但先后相差15开放分钟；各自几何C为09:15/10:00、selected-known为09:20/10:05。窗口末hc4824/i1105。',
 why='原价和独立已选记录给出1800tick而非1200；检验Owner明文长观察窗口不扩大2Δ。',
 aligned=[
  '原价先后两个峰与独立selected身份一致，actual73231799/73233599保持；不由知道得较晚把两峰说成同步。',
  '冻结实际间距1800>1200，公开1538观点中包含这两个具体Turn的组合查询为空。hc该Turn在rows54/89/90可另有成员关系，不能要求所有附近输出为空。实际未成组pair Required未暴露，时间不符合是原actual与Owner常量的对照判断，不是已读到本次TimeVeto。',
  '本对没有共同Life/终止记录，未补造该组合生命周期，也没有回写原峰去解释其他组。后续其他Turn必须按自身身份另看，本C不新挑场景。'],
 scope='支持Owner 2Δ在本对公开输出中未被800放宽；不评价各自参与其他组合的全部行为，也不定位实际首阻断。',
 maturity='Owner明文时间界与公开不合组已可判；内部拒绝轨迹MISSING。',
 divergence='未见以两未变actual突破2Δ的共同输出；未形成组合的原生Required/首阻断NOT_EXPOSED，不能定位其内部第一次拒绝。'),
6: dict(
 raw='June30 10:00→10:05→10:10，rb close3757→3758→3754，i820.5→822→821，局部共同峰真实。到i几何C为798.5，到rb几何C为3722，7月7日09:05 rb3727；中途反复振荡，rb有再触/超过旧峰的价格，不能当单调下降或当7月7日新峰。窗口末rb3725/hc3832/i814.5。',
 why='此旧共同峰在rb很晚选中后仍出组，是长迟到误报候选；检验历史/知识和责任表达，不先以迟到定错。',
 aligned=[
  '两原actual均96674999（June30 10:05），i几何C/known为July3 09:25/09:30，rb为July6 23:00/July7 09:05。首公开row1468在rb selected-known96874799；比原峰晚199800tick=1665开放分钟，但保留原峰而非准入日。公开首版无未来selected提前；内部as-of全轨迹未提供。',
  '两成员DirectionDown/SourcePeakTurn，四项Required均CoordinateSupports、distance0；成员仅i/rb，未把hc别处峰拼入。原a/d/r和admissionKnown分别保留；后续previous指向本Life前版，没有用晚知道重锚定。期间价格再触T本身不构成冻结的新否决规则；是否太晚无用缺Owner判据，另列AMBIGUOUS。',
  'July17 21:45 groupClosed=1/ClosedSupported，22:15 dutyClosed=1；原a96674999、d97154999、r97158599不变。h97169399是handoffEnd，不是F责任继续到h；静态a→d/d→r载带明确非as-of回放，不能因载带从旧a开始判前视。'],
 scope='支持该历史候选在公开输出中的实际/知识/身份/有限责任表达；不证明延迟输出有交易价值或800整体充分合理。',
 maturity='公开历史表达和终止闭合；下游效用AMBIGUOUS，内部全轨迹MISSING。',
 divergence='可读链未见换actual、提前发行或无限延续；内部as-of轨迹缺失且“太晚无价值”没有Owner判据，无法将其定位为第一次业务分歧。'),
7: dict(
 raw='May25 14:55→15:00→21:05，rb close4517→4524→4459（15:00 high4530），i846.5→847.5→836（high849.5）；同时原价局部峰后确有回落。附近有更早更大尺度转折，不能仅凭图中附近蓝点当作这两根原价的已选T。',
 why='原始局部共同形状是实见，但指定尺度资格未成立，是当前F共同层覆盖外案例，不是两个已合格输入被漏掉。',
 aligned=[
  '原价两品种同刻局部峰可复核，独立selected完整投影按actual_ts查询May25 15:00，rb/i均为空。原始形状成立与F输入资格成立分开；不从成员表反造上游。',
  '当前F承接指定已选Turn，不直接从raw close另造所有局部峰；这两峰无对应指定selected，F共同资格比较NOT_APPLICABLE。附近输出/已选点按自己的actual解释，不能按视觉接近移到15:00。',
  '无这对合格输入的已发行Life，不补造必须终止的对象。若未来有效材料推翻无尺度资格前提，须另起S1版本，不修改本v1；本C不诊断上游选择算法。'],
 scope='当前F共同层NOT_APPLICABLE；范围说明有实证。上游是否应选择此局部峰不在本D判断范围。',
 maturity='当前公开资格边界可判；全原始真值与上游该不该选未作判断。',
 divergence='当前F共同层适用前提不成立，因此不存在该层可定位的预期失败；上游未选原因没有材料且属于另一问题，不称其为当前F第一分歧。')}

def decode(row, prefix=''):
    if row[prefix+'idForm'] == 1:
        return str(uuid.UUID(int=(int(row[prefix+'idHigh']) << 64) | int(row[prefix+'idLow'])))
    return row[prefix+'idText']

def bar(s, idx):
    d = data[price_ids[s]]
    return dict(row_index=idx, **{k:d[k][idx] for k in ['ts','open','high','low','close','volume']})

def raw_summary(c, rb):
    result = []
    for layer in rb['raw_market_readback']:
        s=layer['symbol']; d=data[price_ids[s]]
        rows=list(range(layer['row_start'],layer['row_end']+1))
        lo=min(rows,key=lambda i:d['close'][i]);hi=max(rows,key=lambda i:d['close'][i])
        critical=layer['critical_points']
        extra=[]
        if c['case_id'].endswith('002') and s in ('rb','hc'):
            ts='2021-01-05 21:45' if s=='rb' else '2021-01-05 21:40'
            j=d['ts'].index(ts);extra=[bar(s,k) for k in (j-1,j,j+1)]
        segment=None
        if c['case_id'].endswith('006') and s in ('rb','i'):
            between=[i for i in rows if '2023-06-30 10:05'<=d['ts'][i]<='2023-07-07 09:05']
            segment=dict(scope='只在冻结原峰到组合知识到齐之间的原价路径',
                first=bar(s,between[0]),last=bar(s,between[-1]),
                lowest_close=bar(s,min(between,key=lambda i:d['close'][i])),
                highest_close=bar(s,max(between,key=lambda i:d['close'][i])))
        result.append(dict(symbol=s,source_ref=layer['source_ref'],row_interval=[rows[0],rows[-1]],
            rows=len(rows),first=bar(s,rows[0]),last=bar(s,rows[-1]),
            lowest_close=bar(s,lo),highest_close=bar(s,hi),critical_points=critical,
            extra_frozen_window_bars=extra,actual_to_known_price_process=segment,
            selection_note='只在冻结案例窗口还原原价；极值是close路径摘要，不是新增尺度算法/阈值。'))
    return result

def group_step(g):
    q=g['group']; part=g['participation']
    return dict(stage='已发行公开候选观点',timestamp=q['timestamp'],native_known=q['groupKnownFrom'],
        actual_anchor=q['groupAnchor'],original_anchor=q['groupOriginalAnchor'],
        original_deadline=q['groupOriginalDeadline'],deadline=q['groupDeadline'],
        original_revision_end=q['groupOriginalRevisionEnd'],revision_end=q['groupRevisionEnd'],
        identity=dict(life=g['life'],revision=g['revision'],full_parent=g['full_parent'],row_index=g['row_index']),
        local_basis=q['groupLocalBasis_name'],observation=q['groupObservation_name'],
        coverage_incomplete=q['groupCoverageIncomplete'],group_closed=q['groupClosed'],
        members=g['members'],member_P=g['member_P'],member_P_clock=g['member_P_clock'],required=g['required'],
        previous=[dict(raw=r,life=decode(r,'referenceLife_'),revision=decode(r,'referenceRevision_')) for r in g['previous']],
        covered_by=[dict(raw=r,life=decode(r)) for r in g['covered_by']],overlaps=g['overlaps'],
        participation=part,source=g['source_ref'],
        location=dict(row_index=g['row_index'],full_parent=g['full_parent'],children='按完整父坐标/child_id_3等逐层配对'),
        occurrence_semantics='timestamp/occurrence/record_id/child_id_2为本次公开父坐标；同刻不同观点不混合，未发行拍不填零。')

common_limits=[
    'U仍PARTIAL：内部逐tick材料准入/保留、未成组pair全枚举和原生首阻断NOT_EXPOSED。',
    '原生连续coverage区间未暴露；coverageIncomplete字段只支持本次公开观点所声称的状态，不独立证明每拍覆盖。',
    '图与正式数据是同源不同视图，不算两份独立证据；独立上游指非从F成员逆推的原上游投影。',
    'construction_snapshot为静态历史投影，不是完整as-of回放；几何C、T点known和selected-known不能混同。',
    '判断仅覆盖冻结7例当前版本实例，非全800合理性、全量真值、参数最优性或Feature释放结论。']
casebook=[];packages=[];divergences=[];routes=[]
for c in cs['cases']:
    cid=c['case_id']; n=int(cid[-3:]); e=expectations[cid]; note=notes[n]
    rb=json.loads((ROOT/f'case_readback/{cid}.json').read_text())
    raw=raw_summary(c,rb)
    # 初始OHLC以原表逐值写入，人工文字不替代证据。
    if n==3:
        values='，'.join(f"{r['symbol']}="+'/'.join(str(r['first'][k]) for k in ['open','high','low','close']) for r in raw)
        note['raw']='首根5m原价OHLC（open/high/low/close）为'+values+'。首根内有价格变化，但图左界前完整尺度转折前史不可得。随后hc09:30 close4432再回4438，rb/i10:00为4318/993；不同发展不能由首点同刻推出已证实共同峰谷。'
    primary='NOT_APPLICABLE' if n==7 else 'SUPPORTS'
    steps=[group_step(g) for g in rb['observed_public_group_process']]
    alignment=[];items=[]
    for i,(expected,interpretation) in enumerate(zip(e['expected_feature_process'],note['aligned']),1):
        event_rows=[g['row_index'] for g in rb['observed_public_group_process']]
        location=dict(case_readback=f'case_readback/{cid}.json',group_rows=event_rows,
            raw_row_intervals=[dict(symbol=r['symbol'],rows=r['row_interval']) for r in raw],
            independent_selected_rows=[dict(source_id=t['source_id'],row=t['row_index']) for t in rb['independent_selected_readback']],
            section='raw_market_readback / independent_selected_readback / observed_public_group_process / specific_public_lookups')
        status='SUPPORTS' if n==7 and i==1 else primary
        evidence_id=f'F800-S2-C{n:03}-P{i}'
        al=dict(step_id=f'{cid}-STEP{i}',expected_verbatim=expected,phase=['发生','发展','结束'][i-1],
            raw_precondition='原价/独立selected见原始链；成立与否按本步解释，未借F存在决定。',
            intermediate_and_output=interpretation,identity_preserved='无组不虚构Life；有组按full_parent/Life/Revision/previous逐版核对。',
            evidence_status=status,earliest_conflict_observed=False,
            downstream_propagation='未确认第一冲突，不虚构其下游传播或新的独立分歧。',evidence_id=evidence_id,location=location)
        alignment.append(al)
        items.append(dict(evidence_id=evidence_id,source=list(dict.fromkeys([r['source_ref'] for r in raw]+[material_ref,
            pro_ref('D012','formal_data/source_p1531.json.gz')]+[pro_ref('D012',f"formal_data/source_{t['source_id']}.json.gz") for t in rb['independent_selected_readback']])),
            location=location,actual_time=[dict(symbol=t['raw']['symbol'],native=t['raw']['actual'],time=t['raw']['actual_ts']) for t in rb['independent_selected_readback']],
            confirm_time=[dict(symbol=t['raw']['symbol'],geometric=t['raw']['confirmation_ts'],selected_known=t['raw']['known_ts'],point_known=t['raw']['raw_known']) for t in rb['independent_selected_readback']],
            evidence_status=status,observation=interpretation,interpretation='对应冻结原文第'+str(i)+'步，仅限明示的可读范围。',
            alternative_explanations=['图中背景邻近对象按真实成员actual排除；局部状态与coverage独立；不以同源图表重复计证。'],
            data_quality=dict(versions_match=True,formal_stage='construction_snapshot',missing_close=0,duplicates=0,
                full_parent_retained=True,internal_trajectory_exposed=False)))
    intermediate=[]
    for i,expected in enumerate(e['expected_intermediate_decisions'],1):
        intermediate.append(dict(expected_verbatim=expected,
            observed_public='逐观点members/Required、P/T/C、previous/CoveredBy/participation见实际链；无组只有独立已选坐标与公开查询，不补造Required。',
            scope='公开已发行的原值；J1/J3/原生连续coverage的未公开部分单列缺口',
            evidence_status='NOT_APPLICABLE' if n==7 else 'SUPPORTS',evidence_refs=[f'F800-S2-C{n:03}-P2']))
    missing=[]
    if n in (1,2,4,5,6):
        missing.append(dict(evidence_id=f'F800-S2-C{n:03}-M1',source=understanding_ref,
            location='U.unconfirmed_items及本案例公开数据的暴露边界',actual_time=None,confirm_time=None,
            evidence_status='MISSING',observation='未取得本例内部逐tick准入/保留、未成组pair全枚举/首阻断或原生连续coverage区间。',
            interpretation='不能补足内部运行轨迹、完整as-of或对未建组pair宣称实际TimeVeto；不取消独立坐标与公开发行行为可判部分。',
            alternative_explanations=['公开不合组可与多种内部拒绝/未枚举路径兼容，首阻断不能由结果唯一反推。'],
            data_quality='NOT_EXPOSED，不是查询空表/0。',gap_request_refs=['F800-S2-G001']+(['F800-S2-G002'] if n in (1,4,6) else [])))
    if n==3:
        missing.append(dict(evidence_id='F800-S2-C003-M1',source=material_ref,location='首根之前完整尺度前史及memberP缺口',actual_time='2021-01-04 09:05:00以前',confirm_time=None,
            evidence_status='MISSING',observation='首根OHLC存在，左侧完整转折前史与有效P/方向/类型在当前材料不可得。',
            interpretation='只核不足是否诚实表达；不能判市场真实共同转折已成立/未成立，更不将InsufficientHistory当Feature失败。',
            alternative_explanations=['图外可能有其他有效前史，但本C未获同版已接受材料。'],data_quality='缺前史与明确Unavailable，不是价格序列完全没有数据。',gap_request_refs=['F800-S2-G003']))
        missing.append(dict(evidence_id='F800-S2-C003-M2',source=understanding_ref,location='原生coverage连续区间',actual_time=None,confirm_time=None,
            evidence_status='MISSING',observation='只实读到coverageIncomplete从1到0的公开版本；连续区间未公开。',
            interpretation='不能独立证明内部每拍完整覆盖，保持局部不足与公开coverage分列。',alternative_explanations=[],data_quality='NOT_EXPOSED',gap_request_refs=['F800-S2-G002']))
    ambiguous=[]
    if n==6:
        ambiguous.append(dict(evidence_id='F800-S2-C006-A1',source=frozen_ref,location='E006.ambiguous_conditions及实际1665开放分钟迟到',actual_time='2023-06-30 10:05:00',confirm_time='2023-07-07 09:05:00',
            evidence_status='AMBIGUOUS',observation='实际共同峰到组合首知识相隔199800tick=1665开放分钟；期间rb曾再触/高于旧峰。',
            interpretation='历史解释准确与下游实时有用性是不同判断；没有Owner效用/最大可用延迟判据，不判必然误报或有用，不新增单调/不再触T否决。',
            alternative_explanations=['可作历史结构说明','对实时机会可能已过晚；需下游目标/Owner判据才可分辨'],data_quality='价格和时序可得，业务价值判据未确定。'))
    not_applicable=[]
    if n==7:
        not_applicable.append(dict(evidence_id='F800-S2-C007-N1',source=[understanding_ref,frozen_ref],location='BO2输入资格及E007',
            actual_time='2022-05-25 15:00:00',confirm_time=None,evidence_status='NOT_APPLICABLE',
            observation='rb/i该原价时刻无对应指定尺度selected实际T；没有两个已取得当前F输入资格的Turn。',
            interpretation='当前F形成/更新/终止比较不适用，不进入F漏报/失败队列；上游应否选择仍在范围外。',
            alternative_explanations=['局部原价峰与其他时刻更大尺度Turn可同时存在'],data_quality='全独立已选投影限定精确时刻查询为空。'))
    items+=missing+ambiguous+not_applicable
    divergence=dict(case_id=cid,expectation_id=e['expectation_id'],unit_ref=None,time=None,expected=None,observed=None,
        located=False,reason=note['divergence'],
        examined_units=['BO2','J2','J4','J5'] if steps else ['BO2','J2'],
        not_located_is_not_a_pass_for_unexposed_stages=True)
    divergences.append(divergence)
    judgment=dict(primary_state=primary,primary_scope=note['scope'],maturity=note['maturity'],
        supports=[x['evidence_id'] for x in items if x['evidence_status']=='SUPPORTS'],
        counters=[],missing=[x['evidence_id'] for x in missing],ambiguous=[x['evidence_id'] for x in ambiguous],
        not_applicable=[x['evidence_id'] for x in items if x['evidence_status']=='NOT_APPLICABLE'],pending=[],
        score=None,score_note='各独立声明分列；无总分，SUPPORTS不吞并缺口/歧义。',
        next_route='RETURN_TO_ORIGINAL_MANAGER_WITH_SCOPE_AND_GAPS')
    package=dict(comparison_id=f'F800-S2-ECP-{n:03}',business_intent=e['statement'],expectation_id=e['expectation_id'],
        expectation_version=e['version'],expectation_origin=e['origin'],scenario_id=cid,
        frozen_expectation_ref=frozen_ref,frozen_statement_verbatim=e['statement'],
        data_binding=dict(feature_ref=cs['feature_ref'],observation_material_ref=material_ref,
            accepted_html_sha256=sha(html.read_bytes()),formal_graph_data=pro_ref('D012','FORMAL_GRAPH_DATA.json'),
            formal_stage='construction_snapshot',case_material_index=pro_ref('D013','CaseMaterialIndex.json',FROZEN),
            preflight='ScenarioEvidencePreflight.json',readback=f'case_readback/{cid}.json'),
        time_basis=time_basis,parameter_version=cs['parameter_version'],evidence_items=items,judgment=judgment,
        applicability_boundary=dict(current=note['scope'],frozen_conditions_verbatim=e['applicable_conditions'],
            non_applicable_verbatim=e['non_applicable_conditions'],explicit_non_goals_verbatim=e['explicit_non_goals'],
            material_limits=common_limits),
        confidence=dict(public_facts='高：同版原值与完整父坐标可回读；独立原行情/上游交叉核对',
            business_inference='Owner仅E005为明文；其他六项仍为有出处的业务推导',
            unexposed_or_utility='未形成确定判断，不借公开一致性提升'),
        earliest_business_divergence=divergence,next_action='保留当前范围/成熟度回原manager；缺口交材料路线，当前无合格偏差送S3。')
    save(f'evidence_packages/{package["comparison_id"]}.json',package)
    packages.append(package)
    casebook.append(dict(case_id=cid,case_type=c['case_type'],symbol=c['symbol'],start_time=c['start_time'],end_time=c['end_time'],
        raw_market_process=[dict(stage='原价过程',narrative=note['raw'],why_case_type=note['why'],price_process=raw),
            dict(stage='独立上游过程',records=rb['independent_selected_readback'],specific_queries=rb['specific_public_lookups'],
                scope='原上游同版已选投影，独立于F成员逆推；不是全部原始转折真值。')],
        expected_feature_process=e['expected_feature_process'],expected_intermediate_decisions=e['expected_intermediate_decisions'],
        expected_expectation_id=e['expectation_id'],expected_version=1,expected_origin=e['origin'],
        observed_feature_process=[dict(stage='上游/当前阶段输入',records=rb['independent_selected_readback'],
            specific_public_queries=rb['specific_public_lookups'],feature_ref=cs['feature_ref'],parameter_version=cs['parameter_version'])]+steps+
            [dict(stage='未暴露环节',limits=common_limits)],
        process_alignment=alignment,intermediate_decision_alignment=intermediate,
        earliest_business_divergence=divergence,material_limits=common_limits,
        current_judgment=judgment,evidence_comparison_package=f'evidence_packages/{package["comparison_id"]}.json'))
    routes.append(dict(case_id=cid,comparison_id=package['comparison_id'],primary_state=primary,
        eligible_for_skill3=False,criteria=dict(
            intended_coverage=n!=7,business_conflict_observed=False,business_impact_of_conflict='未证明存在冲突，无法指认明确失败后果',
            repeated_or_severe_conflict=False,material_gaps_not_used_as_failures=True,
            traceable_public_stage=True,diagnosis_value='当前没有可区分根因的确定业务冲突；先保留材料/价值边界'),
        route='OUTSIDE_CURRENT_COVERAGE' if n==7 else 'SCOPED_SUPPORT_WITH_REMAINING_LIMITS',
        missing_route='ObservationGapRequests.json' if missing else None,
        ambiguity_route='OpenQuestions.json' if ambiguous else None,
        reason='未同时满足原Skill步骤8，不将候选标签、空查询、材料不足或价值歧义升级为正式偏差。'))

save('ScenarioProcessCasebook.json',dict(casebook_id='F800-S2-D014-CASEBOOK-v1',feature_ref=cs['feature_ref'],
    parameter_version=cs['parameter_version'],observation_material_ref=material_ref,frozen_set_ref=frozen_ref,
    time_basis=time_basis,cases=casebook,created_at=now(),case_selection_changed=False,expectation_rewritten=False))
save('EvidenceComparisonPackage.json',dict(package_set_id='F800-S2-D014-ECP-v1',packages=packages,
    schema_note='每例保留原S2 6.2所有兼容字段；逐声明状态，不用总分；可直接供原Skill3引用但本轮未送诊断。'))
save('EarliestBusinessDivergence.json',dict(cases=divergences,located_divergences=[],
    conclusion='可读范围未观察到确定首次业务冲突；不适用/缺口/价值歧义分别保留，不宣称全链无偏差。'))
gaps=[
 dict(gap_id='F800-S2-G001',case_ids=['F800-S1-C'+f'{n:03}' for n in [1,2,4,5,6]],
      unit_refs=['J1','J2','J3'],evidence_state='MISSING',missing='本次内部逐tick材料准入/保留、未成组pair枚举与首阻断的真实运行记录。',
      requested_material='若要继续回答内部as-of或实际首阻断：提供同39f/参数/运行、仅这些冻结Turn/组合范围的原生准入/保留/Required/阻断位置及完整身份/actual/known；没有原生暴露则明确NOT_EXPOSED。',
      affected_judgment='不能定位无组的内部拒绝，也不能证明每拍从未使用未来知识；公开发行时序与独立资格比较不受此缺口替代。',
      route='OBSERVATION_MATERIAL',blocks_current_public_comparison=False,
      execution='请求是条件后继信息，非本C重跑M/Feature或改监测代码的授权；不以重复已知缺口制造新生产。'),
 dict(gap_id='F800-S2-G002',case_ids=['F800-S1-C'+f'{n:03}' for n in [1,3,4,6]],
      unit_refs=['J4'],evidence_state='MISSING',missing='当前案例的原生连续coverage区间/缺失有效性逐tick轨迹。',
      requested_material='若要独立确认全窗每拍覆盖：提供同运行且限定这些原anchor到r的原生coverage区间、边界原因与known语义；当前公开0/1不替代区间。',
      affected_judgment='只可读公开coverageIncomplete转换，不能据其0声称原生全窗已逐拍独立验证。',
      route='OBSERVATION_MATERIAL',blocks_current_public_comparison=False,
      execution='保持U PARTIAL及材料限制；本C未发新生产/重导图数据。'),
 dict(gap_id='F800-S2-G003',case_ids=['F800-S1-C003'],unit_refs=['BO2','J2'],evidence_state='MISSING',
      missing='Jan4首根以前足以判尺度P/方向/类型的已接受完整前史。',
      requested_material='仅在要判断初始化共同转折真实成立性时，提供同品种/Calendar/尺度的有效前史与P/方向/类型来源、known边界及与当前运行绑定；若原生没有则保留不足。',
      affected_judgment='本C可确认不足被表达并有限结束，不能判断图外原市场完整转折真值。',
      route='OBSERVATION_MATERIAL',blocks_current_public_comparison=False,
      execution='不回填不存在的P/方向，不以缺历史直接要求删除候选或判Feature失败。')]
for gap in gaps:
    gap['case_id']=gap['case_ids'][0]
    gap['missing_field_or_view']=gap['missing']
    gap['why_needed']=gap['affected_judgment']
    gap['return_to']='OBSERVATION_MATERIAL_PREPARATION'
save('ObservationGapRequests.json',dict(requests=gaps,mandatory_rebuild_requests=[],
    note='对照中确实影响更强声明的缺失按原Skill分流；当前不重跑已有效的U/M，不将条件材料请求伪作未完成当前公开对照。'))
save('EvidenceInducedCandidates.json',dict(candidates=[],reason='本次没有出现推翻冻结适用条件或需另立新预期的新事实；保留S1 v1。已知效用歧义/原生未暴露属于原有限制，不重复包装成新候选。',
    frozen_ref=frozen_ref,revision_performed=False))
save('ScenarioFindingCandidates.json',dict(candidates=[],route_assessments=routes,
    conclusion='没有同时满足原Skill步骤8的当前覆盖内明确业务冲突；不以原误报候选标签直接送Skill3。'))
save('DiscrepancyQueue.json',dict(queue=[],reason='没有可定位且材料充分的明确业务分歧；本轮未执行S3。',
    routing_source='ScenarioFindingCandidates.json',first_divergence_groups=[]))
save('CrossCasePatterns.json',dict(repeated_first_divergences=[],context_patterns=[
    dict(case_ids=['F800-S1-C001','F800-S1-C004','F800-S1-C006'],unit_refs=['J2','J5'],
        observed='原实际T与异步selected知识、原责任边界分别保留，公开发生/闭合可追溯。',classification='重复的有界支持，非重复缺陷'),
    dict(case_ids=['F800-S1-C001','F800-S1-C003'],unit_refs=['J4'],
        observed='早期coverageIncomplete=1与不同局部依据并列；coverage变0不自动把Incomplete变Supported。',classification='独立状态分列的公开支持，非完整coverage机制证明'),
    dict(case_ids=['F800-S1-C002','F800-S1-C005'],unit_refs=['BO2','J2','J3'],
        observed='独立actual资格不成立且公开查询无相应组合；原生未成组pair/首阻断均不可见。',classification='限定负例输出支持与重复材料限制，非推断共因')],
    reason='无确定首次分歧可按对象/时期/来源归并；以上只记录重复观察，不查根因/统计相关机制。'))
save('ActualCaseCoverage.json',dict(frozen_case_type_coverage_ref=pro_ref('D013','CaseTypeCoverage.json',FROZEN),
    actually_compared_case_ids=[c['case_id'] for c in cs['cases']],
    actual_types=dict(Counter(c['case_type'] for c in cs['cases'])),
    potential_false_negative='S1原有界筛查NO_CASE_FOUND；本C未重新筛选，未形成冻结漏报例，不能据此证明没有漏报。',
    output_false_positive='两个原误报候选均已实际对照；候选标签不预设COUNTERS，初始化不足表达与迟到历史表达分别受有界支持。',
    outside_current_coverage='C007当前F形成层NOT_APPLICABLE，不进入Feature失败队列。',
    universal_coverage_claim=False))
save('OpenQuestions.json',dict(new_owner_requests=[],new_blocking_questions=[],
    retained_s1_open_questions_ref=pro_ref('D013','OpenQuestions.json',FROZEN),
    current_ambiguity=[dict(case_id='F800-S1-C006',state='AMBIGUOUS',
        question='1665开放分钟迟到的历史共同峰，对预定下游是否仍有用？',
        reason='缺具体下游用途/效用判据；历史表达准确不能回答实时机会价值。',
        disposition='如后继释放需要该判断，由原manager组织业务判据；不是Owner已接受的暂缓，当前不扩大D014范围。')],
    retained_boundaries=['i低参与率仅本C002具体负例受支持，不能解释所有未参加位置。',
        '800整体充分性/效用、全量漏报真值和罕见分支仍未被这7例证明。',
        'S1的POTENTIAL_FALSE_NEGATIVE有界NO_CASE_FOUND保持原义，不改成普遍无漏报。']))
save('S2_HANDOFF.json',dict(run_id=RUN,delegation_id='D014',call_id='C0031',executor='E1',
    professional_state='REPORTED_COMPLETE',completed_scope='原S2七个冻结案例的公开可读三过程还原、对齐、逐预期判断及限制/后继分流',
    primary_case_states={p['scenario_id']:p['judgment']['primary_state'] for p in packages},
    no_score=True,located_business_divergences=0,skill3_candidates=0,
    observation_gap_requests=[g['gap_id'] for g in gaps],evidence_induced_candidates=0,
    unresolved='原生轨迹/首阻断/coverage和初始化前史MISSING；迟到效用AMBIGUOUS；覆盖外NA及有界NO_CASE_FOUND不扩张。',
    next_actor=f'codex:{RUN}:manager',next_action='接收D014后按原流程处理剩余业务边界/后继；无S3缺陷不等于FeatureRelease。',
    feature_release_signed=False,parent_run_completed=False,manager_consumed=False,
    workers=[],new_threads=[],other_chat_messages=[],source_feature_modified=False,
    graph_rebuilt=False,formal_data_reexported=False,frozen_v1_modified=False))
visual=json.loads((ROOT/'S2_BROWSER_REVIEW.json').read_text())
save('VISUAL_REVIEW_NOTES.json',dict(reviewed_at=now(),reviewer='E1',actually_viewed_screenshots=[w['screenshot'] for w in visual['windows']],
    findings=[
        '12张原窗口/局部截图均亲自查看：原价/上游/知识轴与稀疏exact、有限责任末段可见。',
        'C001两/三成员和C003初始化的稀疏行仅作定位，状态结论取对应全父坐标JSON。',
        'C002/C005/C007取消原生选择后下方表格/明细仍保留上一选择上下文（分别可能是C001/C004/C006）；这些明细不是负例/覆盖外案例的对象证据。无组结论来自精确原值查询，不从背景表或截图空白推断。',
        'C004跨春节用开放Calendar的actual与selected分读；C006历史载带不可当as-of提前生效。',
        '截图上下文不独立计证，不修改已接受HTML或将残留明细升级为本Feature业务缺陷。'],
    source_html_unchanged=visual['source_html_unchanged'],source_values_edited=False))

print(json.dumps(dict(cases=len(casebook),packages=len(packages),
    published_group_views=sum(len(c['observed_feature_process'])-2 for c in casebook),
    primary_states=dict(Counter(p['judgment']['primary_state'] for p in packages)),
    atomic_states=dict(Counter(x['evidence_status'] for p in packages for x in p['evidence_items'])),
    gaps=len(gaps),skill3_candidates=0),ensure_ascii=False))
