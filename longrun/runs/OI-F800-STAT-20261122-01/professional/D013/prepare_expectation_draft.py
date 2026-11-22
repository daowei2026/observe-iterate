"""依据已亲自读取的真实过程写S1候选预期；不作S2支持/反证判断。"""
from common import *

assert not (ROOT/'FREEZE_MANIFEST.json').exists(), '冻结后须另立修订版本，不能重写v1'
u_ref=pro_ref('D008','CurrentFeatureUnderstandingPackage.json',U)
material_ref=pro_ref('D012','ObservationMaterialPackage.json')
target_ref=ref('92cec836b1471471bd886a51a66123918ca9b275',f'{PREFIX}/business_control/TASK_PROGRESS.md')
owner_ref=ref(LOCKED,'task-inputs/wall-f-parallel-closure-20261122/F_BASE_RUN_INPUT.md')
parameter='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
groups=json.loads((ROOT/'exploration/group_index.json').read_text())
turns=json.loads((ROOT/'exploration/selected_turn_index.json').read_text())
pool=json.loads((ROOT/'CandidateCasePool.v1.json').read_text())
figures=dict(rb='p1040',hc='p1168',i='p1296')
selected=dict(rb='p1098',hc='p1226',i='p1354')
known=dict(rb='p1424',hc='p1438',i='p1451')
group_source=pro_ref('D012','formal_data/source_p1531.json.gz')
base_limits=[
    'U仍PARTIAL；逐tick材料准入、未成组pair全集、首阻断及原生coverage区间NOT_EXPOSED；不从代码补本次运行值。',
    'K线图元x是显示中点，x_l/x_r为宽度边；原价按ts阅读，actual/confirm/selected-known用独立上游raw原值，不把显示坐标当native actual。',
    'Life/Revision+完整父坐标定位观点；Rct更新行、T/C/known重复表达、关系和修订不增加独立业务对象或独立证据份数。',
    '原三品种69缺close、空可选分支和裁剪如实保留；若具体位置缺必要值，S2须MISSING/AMBIGUOUS或回M，不能补零。',
]

specs=[
 dict(n=1,type='CLEAR_POSITIVE',symbols=['rb','hc','i'],start='2021-01-04 09:05:00',end='2021-01-22 13:35:00',
  window='jan-common-and-start',candidates=['INDEX-F800-SQ-001-C2','INDEX-F800-SQ-003-C2'],
  lives=['8f776a81-a7bc-4c93-965b-0f1534b574c4','6dd1661e-678e-48a8-809f-68243658b3b0'],
  turns=['rb/value1/72133799','hc/value1/72133799','i/value1/72143999'],units=['BO2','BO3','J2','J4','J5'],
  primary='共同实际谷点在异步确认/选中后能否保持同一原问题的可解释候选；两成员与三成员关系不能被算作多个独立市场转折。',
  reason='三条真实原价曲线在同一2021-01-06 11:00谷点反弹；已选T/几何C/知识轴可分读，且两成员和三成员exact/覆盖关系可定位，能区分同步实际过程与同步可知。',
  raw='2021-01-05夜盘高点后，rb/hc/i在2021-01-06 11:00分别到4299、4457、1015后回升。i之后有更多摆动，不能据其摆动数自动要求更多共同组。rb/hc的几何确认到2021-01-07 09:50，i为11:30；selected-known分别09:55和13:35。',
  presence='公开选址事实：两成员Life 6dd1661e…首见09:55，三成员Life 8f776a81…首见13:35；同原实际谷点有多个exact观点。此为定位信息，不是S2支持结论。',
  statement='在这次三品种清楚的共同实际谷点，允许确认/尺度选中异步到达后形成可回溯的共同候选；不得把晚知道误作晚发生，也不得将共享成员的两/三成员解释当成多个独立市场谷点。',
  rationale='共同转折描述的是原市场谷点的跨对象对应，而非要求所有确认同拍；对下游有用的候选须保留原实际位置、迟到知识和解释间关系。该理由来自市场过程与当前目标，不以当前Supported标签为前提。',
  conditions=['当前rb/hc/i独立尺度记录确实对应2021-01-06 11:00的三处谷点，且适用方向/类型及P/T/C关系支持。','原公开记录与当前39f/参数/Calendar一致；无该点必要行情缺失。'],
  process=['发生：各原价先出现谷点；在所需独立尺度/知识条件可得前，不声称已经实时识别整个三成员候选。','发展：先具备两成员再补入第三成员时，允许分别保留具体成员组合及其exact/覆盖关系；不凭图上重叠合并Life。','结束：候选沿其冻结的原问题期限关闭观察和修订责任，保留已发行历史；不因单个局部谷点继续被引用而无限重启同一观点。'],
  intermediate=['J2：逐对时间、方向、类型、P/T/C应针对同一具体Turn检查，不能只凭线形相似或三个数量。','J4：局部共同谷点成立与完整域覆盖分列；早期材料不满全窗时不能把局部Supported等同于coverage完整。','J5：用previous、CoveredBy/Overlaps及participation区分修订、严格超集和不同市场对象。'],
  supports=['原实际谷点及上游资格相符；输出保留正确T/C/selected-known，且两/三成员关系和有限期限可追溯。'],
  falsifiers=['在材料充分、所需关系支持时仍把三品种实际谷点拆成互不相关且无解释的对象，或把未来selected知识提前使用。','把共享成员超集解释当作额外独立共同转折，或将局部支持隐瞒为全域完整。'],
  ambiguous=['若某对P/T/C本身缺失或必要方向不可判，只能未决，不能据三条原价同时反弹强判Supported。'],
  nong=['不规定候选数量真值、交易方向收益或要求每次i摆动都配对。'],
  unknown=['初始化到全域完整的原生逐tick覆盖区间未公开，不能据图反造。']),
 dict(n=2,type='CLEAR_NEGATIVE',symbols=['rb','hc','i'],start='2021-01-04 13:35:00',end='2021-01-22 13:35:00',
  window='jan-isolated-i',candidates=['INDEX-F800-SQ-001-C1'],lives=[],turns=['i/value1/72049199'],units=['BO2','BO3','J2'],
  primary='i的独立峰点未参加F是否可以是共同对象资格不适用，而不是由低参加率直接认定漏报。',
  reason='i在2021-01-04 21:15有清楚独立峰；rb/hc的当前已选峰在下一夜21:45/21:40，原价和独立上游可对照，能排除“所有i选中都应参加共同组”的竞争解释。',
  raw='i从984.5附近上涨至2021-01-04 21:15的1034后回落；同段rb/hc并没有在该分钟形成对应的当前已选峰，其后被选峰分别为2021-01-05 21:45的4423和21:40的4572。',
  presence='完整公开已发行组成员定位未发现i/value1/72049199；这不是本次运行的native首阻断轨迹，也不等于该时段整体无任何F输出。',
  statement='若只有i这处当前尺度峰、没有第二个对象在当前贴近条件下的对应已选转折，则不应为了提高i参加率而把异步的rb/hc峰拼成共同组。',
  rationale='共同对象至少要求不同对象之间的具体对应，单品种本身再清楚也不能推出跨对象共同性；以原价和独立上游判断适用性，不以F没有输出本身证明合理。',
  conditions=['独立上游完整读取确认该i峰在当前实例已选，且在适用实际贴近范围没有第二对象的对应已选转折。','将时间按night_end_at_2300开放交易Calendar处理，不能用确认时点邻近替代实际转折邻近。'],
  process=['发生：i形成并确认自己的尺度峰，属于上游业务对象。','发展：没有第二个适用对象时，不创建只由i支撑的共同组，也不把下一夜别的实际峰移到本峰。','结束：继续保留i的上游历史；本组合不存在需要伪造的F组终止事件。若后来取得真正符合条件的另一个Turn，应以真实新条件重新判断。'],
  intermediate=['J2：先核独立上游actual/方向/类型和跨对象对应；未建组pair没有公开Required行时，不补造实际TimeVeto或first blocker。'],
  supports=['独立行情与上游说明本峰是孤立共同资格负例，且没有用其他晚峰制造以此i峰为成员的共同组。'],
  falsifiers=['原始/上游证据确有同范围合格第二对象，却仅凭i低参加率被排除；或无第二对象仍声称已形成共同组。'],
  ambiguous=['完整上游、时间或方向任一缺失时，“没找到组”只能作为缺失线索，不能判正确负例。'],
  nong=['不要求每个上游i峰有F，也不以本例证明i全部未参加位置合理。'],
  unknown=['未建组的逐tick枚举资格/首阻断未暴露；本例不承诺定位其native第一责任点。']),
 dict(n=3,type='OUTPUT_FALSE_POSITIVE_CANDIDATE',symbols=['rb','hc','i'],start='2021-01-04 09:05:00',end='2021-01-19 21:15:00',
  window='jan-start-anchor',candidates=['INDEX-F800-SQ-004-C1'],lives=['caee906a-9759-466f-bf4a-805293f3da5d'],
  turns=['rb/value1/72010799','hc/value1/72007199','i/value1/72010799'],units=['BO1','BO2','BO3','ST1','J2','J4'],
  primary='冷启动共同时间锚点是否被误读为已观察充分的三品种共同转折。',
  reason='三品种首个锚点同在数据左边界09:05，缺左侧价格过程；随后hc下行而rb/i上行。主输出存在使其值得作为误报候选审查，但候选存在不等于其已错误确认。',
  raw='观察图从2021-01-04首根5m K线开始；该根OHLC提供根内价格，未提供首锚点以前完整的前一尺度转折过程。hc首锚4460后下移，rb4294和i984.5相对几何C上移；单凭同刻首锚不能阅读出完整共同峰/谷。',
  presence='选址时原Life caee906a…可定位，首exact为Incomplete/Open，成员方向/类型Unavailable；这些标签仅记录所选输出，不在S1据此关闭误报疑问。',
  statement='缺少转折左侧历史、方向和类型尚不足时，初始化锚点最多作为明确不充分的候选；不能仅因三品种首点同刻就声称已证实共同转折或完整域覆盖。',
  rationale='市场转折需要前后过程，数据起点的机械同刻并非独立共同性证据；不充分候选与错误确认应分开，避免把初始化结果数量本身判错。',
  conditions=['当前公开记录表明这些点为观察左边界锚点，必要前史/方向/类型不可用。'],
  process=['发生：如保留初始化解释，须保留其不足性与原锚点身份，不回填不存在的前史。','发展：只有新的真实材料解决对应条件才可提高局部依据；Calendar前进或coverage恢复本身不补出方向/类型。','结束：若不足一直未解决，到有限观察/责任边界保留不充分历史结果；不能用到期自动改写成已支持共同转折。'],
  intermediate=['J2：公开Required的gap/方向/类型及成员Unavailable应可追溯，不填虚假P或零方向。','J4：coverage和局部依据独立；coverage由不完整变完整不自动成为市场共同转折证据。'],
  supports=['初始化不足被持续明确表达，未把同刻首点当确定共同转折，且有限期限后不继续假装开放新证据。'],
  falsifiers=['在必要前史仍不可用时仅凭时钟/初始同刻把它提升为确定共同转折，或补造方向/峰谷证据。'],
  ambiguous=['如果另有已接受前史或可靠初始化定义，本例适用条件应重检；S1不把当前图外历史缺失当业务反证。'],
  nong=['不要求删除所有Incomplete候选；不把本例候选标签直接升级CONFIRMED缺陷。'],
  unknown=['本范围外左侧市场过程不可从本材料补造；framePatches/scopeEnded稀有分支不在此例证明。']),
 dict(n=4,type='PARAMETER_BOUNDARY',symbols=['rb','i'],start='2021-02-09 14:05:00',end='2021-03-05 10:00:00',
  window='feb-2delta',candidates=['BOUNDARY-IN-1200'],lives=['7097f790-78d4-4458-a2cd-fe0eba59de7d'],
  turns=['rb/value1/73153799','i/value1/73148999'],units=['BO2','BO3','J2','J5'],
  primary='actual恰2Delta的共同谷点，不能被很长的确认间隔或春节闭市墙钟时长替代判断。',
  reason='rb于2021-02-10 09:50、i于10:00到谷点，相差1200UTI；尺度知识分别到春节后2021-02-18，能分离actual贴近、确认迟到和800观察责任。',
  raw='rb谷点4340、i谷点1020.5发生于2021-02-10 09:50/10:00，随后均抬升；图中的T到C跨过闭市，不应把墙钟跨春节误读为actual不贴近。',
  presence='原Life 7097f790…及其首/到期/责任末三exact可定位；公开成员actual相差1200，source p1531行44/71/72。',
  statement='这对恰在当前2Delta边界的实际谷点，在方向/类型和P/T/C适用时应保有共同候选资格；确认知识较晚不应把actual距离改为确认距离。',
  rationale='当前共同性允许有限交易时间滞后；边界例分离实际同步关系与认识延迟。800只为晚知道提供有限观察机会，不能重新定义这两种时间。',
  conditions=['原价和独立尺度确认这两处谷点；native actual为73127399与73128599，差1200当前CalendarUTITick。','其余必要关系支持且知识在允许的有限窗口到达；包含等号的现有贴近合同仍有效。'],
  process=['发生：先保留两处真实谷点与不同可知时点；未到所需知识前不提前声称成组。','发展：在其余条件成立时，不因恰达2Delta或墙钟跨春节直接失去共同资格；保留原actual和选中知识。','结束：按原冻结期限结束观察/修订责任；确认迟到不把有限责任改成无限延续。'],
  intermediate=['J2：actual距离1200与其余三项分开；参考当前U的贴近合同，不从Supported反推必要关系。','J5：原问题deadline/r及准入保持原含义，不能把selected晚到当作新actual。'],
  supports=['恰2Delta的资格未被误排除，实际/确认/可知分别可追溯，有限责任保持。'],
  falsifiers=['适用且必要材料充分时，仅因距离等于1200或墙钟跨节假日而排除；或把确认时点当成原谷点。'],
  ambiguous=['若P/T/C或方向有独立否决，只能区分时间支持与其他否决，不应要求时间条件单独保证成组。'],
  nong=['不是参数标定或800最优性结论；不据一个边界例证明所有迟到都合理。'],
  unknown=['原未发行pair全集不公开；本例只要求被发行组合的已暴露Required可核。']),
 dict(n=5,type='PARAMETER_BOUNDARY',symbols=['hc','i'],start='2021-02-19 14:50:00',end='2021-02-23 11:00:00',
  window='feb-outside-2delta',candidates=['BOUNDARY-OUT-1800'],lives=[],
  turns=['hc/value1/73238399','i/value1/73232999'],units=['BO2','BO3','J2'],
  primary='800不得把15开放分钟的实际峰点变成2Delta贴近共同组。',
  reason='两个真实已选峰的actual为2021-02-22 09:05与09:20，1800UTI，紧邻当前1200贴近界外，适合与边界内谷点分开审查。',
  raw='i在2021-02-22 09:05到1133，hc在09:20到4856，随后都下移；相似峰形并不能取消实际15开放分钟的先后差。',
  presence='完整公开组成员中未找到同时含这两个Turn的组合；可有各自参加别的组，不得把“此组合无输出”改写成这时刻F全空或nativeTimeVeto已记录。',
  statement='保持Owner锁定的2Delta贴近条件：即使observation_multiple=800，也不能仅因这两个峰都能在长观察窗被知道，就把相差15开放分钟的这对actual当作当前2Delta共同组。',
  origin='OWNER_EXPLICIT',source=owner_ref,
  rationale='原输入§2明确800只进入观察/首次准入与有限责任，actual转折间2Delta不变；Delta=600=5开放分钟，因此本对1800超出1200。此处不提出新业务阈值。',
  conditions=['相同Calendar与单位；actual确为73231799与73233599，且成员身份没有修订为其他实际位置。'],
  process=['发生：分别保留各自真实峰和上游资格。','发展：长窗口可等待知识，但不能让这两个相差1800的原actual成为当前2Delta组合；允许它们分别与别的合格Turn构成组。','结束：不伪造本不成立组合的Life/终止；后续新观点如实际坐标变化，须保留新事实及版本，不回写原峰。'],
  intermediate=['J2：预期本组合的时间贴近不支持；未建组pair的native Required若无公开行，不填实际TimeVeto/首阻断。'],
  supports=['不以800重定义本对同步性，各自上游/其他组身份和时序仍正确。'],
  falsifiers=['以这两个未变actual为成员，却只因800而按2Delta贴近声称该共同组合成立。'],
  ambiguous=['若实际成员是不同Turn或坐标已合法修订，不能用原1800差直接判该另一个组失败。'],
  nong=['不要求这两个品种在整个窗口都无F输出；不把相似原价峰定义为新的15分钟规则。'],
  unknown=['组合未建组的原生首阻断未公开；不得从未输出反填失败轨迹。']),
 dict(n=6,type='OUTPUT_FALSE_POSITIVE_CANDIDATE',symbols=['rb','hc','i'],start='2023-06-29 09:40:00',end='2023-07-18 10:45:00',
  window='june-july-late',candidates=['INDEX-F800-SQ-003-C1'],lives=['32457584-509d-4e7f-a0ea-6f8ac067c66e'],
  turns=['rb/value1/96874199','i/value1/96711599'],units=['BO2','BO3','J1','J2','J5'],
  primary='最大迟到代表能否作为原共同峰的历史候选解释，而不是被误读为识别当日新的共同峰或当前交易机会。',
  reason='SQ003最大迟到候选在真实图中可读：rb/i原峰同刻，但其间已经反复振荡且知识差异很大；比普通迟到更能区分“晚知道同一旧峰”与“无限延长/新峰拼接”。',
  raw='rb3758与i822的原峰都在2023-06-30 10:05。此后两条原价经历多次回落/反弹，hc的后续尺度峰在别处；i几何确认2023-07-03 09:25、selected09:30，rb几何确认2023-07-06 23:00、selected2023-07-07 09:05。',
  presence='原Life 32457584…在2023-07-07 09:05首发行，actual锚点仍为96674999；后续exact到2023-07-17责任末。此选址事实不等于S1已证明长迟到业务合理。',
  statement='长迟到若仍表达2023-06-30同刻原峰，应以原actual、各自确认/selected和有限原问题准确呈现；不能把7月7日才知道的旧共同峰宣称为7月7日新发生的同步转折，也不能仅因识别迟到或后来振荡就直接判该历史候选为误报。',
  rationale='历史共同性与实时可用性不同。800可以容纳认识延迟，但有用的输出需诚实说明它指向哪个原市场过程和何时才可知；当前目标没有给出“迟到超过多少即无意义”的Owner业务阈值。',
  conditions=['两成员实际峰和具体尺度记录仍是冻结的这两个Turn；知识在当前800有限观察窗内可得，且其他关系适用。'],
  process=['发生：原市场在6月30日出现两品种同刻峰；i先知道、rb后知道，在必要知识到齐前不回填实时已成组。','发展：晚准入时保留原锚点和既有责任期限；后续观点应可追溯同Life/previous，不因晚知道改造成别的当日新峰。','结束：原观察期限与修订责任分别到界关闭，历史仍可追溯；新知识不得无限延长旧问题，也不以时钟每拍制造新共同对象。'],
  intermediate=['J1/J2：只有公开选中材料及已发行组Required可核；不能反造完整保留/枚举轨迹。','J5：分读originalAnchor/Anchor、admissionKnown、deadline/revisionEnd/handoff与duty；hand off不当作F原修订责任延长。'],
  supports=['旧共同峰被准确作为迟到历史解释，知识/实际时间和有限责任区分清楚，没有错拼hc别处峰或伪装成当前新机会。'],
  falsifiers=['材料充分时，主输出或对外解释把原actual换成晚准入当天、提前使用rb未来知识，或把旧有限问题无限延长。'],
  ambiguous=['“识别得太晚所以一定没有业务价值”缺Owner判据；仅此价值判断应未决，不能在S1伪造阈值。','中途价格再触T不自动成为新增否决规则，需按现有明确关系和证据另判。'],
  nong=['不评价交易收益或当前机会；不因后来振荡新增“必须保持单调”的规则；不认定800最优或提出调参。'],
  unknown=['迟到多少仍有下游价值尚无独立Owner阈值；这是限制，不是Owner已接受暂缓。']),
 dict(n=7,type='OUTSIDE_CURRENT_COVERAGE',symbols=['rb','hc','i'],start='2022-05-24 14:00:00',end='2022-05-27 14:00:00',
  window='may-raw-independent',candidates=['RAW-06'],lives=[],turns=[],units=['BO1','BO2','BO3','J2'],
  primary='原价同步局部峰不具当前尺度输入资格时，不能直接把F未表达该细粒度过程判为漏报。',
  reason='完全从原始close独立选出的同步局部峰，之后才查selected和F；能反驳仅从既有F输出挑案例的偏差，并划出原价全部峰谷与当前F层输入的边界。',
  raw='2022-05-25 15:00，rb close4524（high4530）与i close847.5（high849.5）为本次±12根浏览窗的同步局部峰；其后明显回落，窗口里还叠着更早/更大尺度的P/T/C过程。此浏览窗仅排序，不定义Feature新尺度。',
  presence='两个该分钟原价峰在当前完整ScaleTurn已选T投影中都没有同刻记录；不是两条合格F输入已被证实丢失。邻近知识时点仍可有指向别处actual的组，不称全时段无F。',
  statement='当前F只承接指定尺度已选的具体转折；对这两个没有对应当前已选T记录的细粒度同步峰，不应要求F额外识别所有局部峰谷，也不能把它们未进入F直接列为当前F设计反证。',
  rationale='同步局部形状与已承诺的尺度共同对象不是同一分母；这是一处原始过程主动发现、但当前层资格不成立的真实边界，不据实现输出自证市场无共同波动。',
  conditions=['沿当前U对象合同，仅评当前F共同候选层；公开独立selected全范围确实没有该两峰的同刻T记录。'],
  process=['发生：记录原价局部共同波动，保留真实价格/分钟与上游更大尺度背景。','发展：在指定尺度资格未成立时，不要求F凭原始close另造新Turn或共同Life；如出现附近F输出，先查其真正成员actual。','结束：原局部峰后的回落不产生当前F必须终止的虚构对象；若后续新材料显示这两峰确已获尺度资格，应新版本回S1再确定适用性。'],
  intermediate=['BO2/J2：raw ts与独立selected.actual_ts按原值定位，不能把K线x中点当native actual，也不能从F成员表反造独立上游。'],
  supports=['证据对照明确标出当前层不适用及上游资格边界，未将局部形状直接当已确认F漏报。'],
  falsifiers=['如果新证据实际存在对应且合格的当前尺度T，本例“无尺度资格”的适用前提被推翻，应另立预期版本，不能继续用覆盖外掩盖。'],
  ambiguous=['上游应否选择这两个局部峰不由F的有无输出回答；本D不展开完整尺度算法或提出修改。'],
  nong=['不确认上游尺度算法对所有细粒度波动都合理；不把覆盖外场景判当前F失败。'],
  unknown=['全原始转折真值/上游未选首阻断没有被本材料证明；这里只确认公开已选投影无对应记录。']),
]

cases=[];expectations=[];locations=[]
for s in specs:
    cid=f"F800-S1-C{s['n']:03d}"
    selected_rows=[]
    for key in s['turns']:
        symbol=key.split('/')[0]
        i,t=next((i,t) for i,t in enumerate(turns[symbol]) if t['turn_id']==key)
        selected_rows.append(dict(symbol=symbol,turn_id=key,row_index=i,
            selected_T_source_ref=pro_ref('D012',f'formal_data/source_{selected[symbol]}.json.gz'),
            selected_known_source_ref=pro_ref('D012',f'formal_data/source_{known[symbol]}.json.gz'),
            actual=t['actual'],actual_time=t['actual_ts'],geometric_confirmation=t['confirmation'],
            geometric_confirmation_time=t['confirmation_ts'],selected_known=t['known'],selected_known_time=t['known_ts'],
            point_known=t['raw_known'],price=t['price'],identity_role=t['turn_id_role']))
    rows=[g for g in groups if g['life'] in s['lives']]
    source_refs=[material_ref,pro_ref('D012','FORMAL_GRAPH_DATA.json'),u_ref,
        *[pro_ref('D012',f'formal_data/source_{figures[symbol]}.json.gz') for symbol in s['symbols']]]
    source_refs.extend(x['selected_T_source_ref'] for x in selected_rows)
    source_refs.extend(x['selected_known_source_ref'] for x in selected_rows)
    if s['n']==2:
        source_refs.extend(pro_ref('D012',f'formal_data/source_{k}.json.gz') for k in selected.values())
    if s['lives'] or s['n'] in (2,5):source_refs.append(group_source)
    if s['n']==7:source_refs.extend(pro_ref('D012',f'formal_data/source_{k}.json.gz') for k in selected.values())
    case=dict(case_id=cid,status='READY_FOR_EXPECTATION',case_type=s['type'],symbol=s['symbols'],
        start_time=s['start'],end_time=s['end'],timezone='Asia/Shanghai',calendar='night_end_at_2300',sampling='5m',
        related_reasonableness_units=s['units'],primary_judgment_target=s['primary'],selection_basis=s['reason'],
        raw_market_description=s['raw'],output_presence=s['presence'],
        required_intermediate_fields=(['KLine.ts/open/high/low/close（保持缺值）','ScaleTurn.actual/confirmation/known/raw_known（四者分列）',
            'revision_source.raw.group + 完整parent + Life/Revision',
            'occurrences_groupMembers（已发行组公开成员，保留exact）'] if s['n'] in (2,5) else
            ['KLine.ts/open/high/low/close（保持缺值）','独立ScaleTurn实际T/几何C/selected-known原事件',
             *(['occurrences.groupLocalBasis/Observation/CoverageIncomplete/Closed',
                'occurrences_groupRequired及_pairDistance','occurrences_groupFormationParticipation及previous/CoveredBy/Overlaps'] if s['lives'] else [])]),
        source_refs=list(dict.fromkeys(source_refs)),candidate_ids=s['candidates'],
        material_locator='CaseMaterialIndex.json#'+cid,
        viewport_refs=[f"screenshots/{s['window']}.png"]+(
            ['screenshots/march-boundary-close.png'] if s['n']==4 else
            ['screenshots/jan-common-and-start.png'] if s['n'] in (2,3) else []),
        material_limits=base_limits,
        selection_is_not_evidence_verdict=True)
    cases.append(case)
    conditions=s['conditions']
    needed=[dict(source_ref=x,location='按CaseMaterialIndex中的原行号/Turn/完整父坐标取原值；同源图与表不计双份独立证据') for x in case['source_refs'] if '/formal_data/' in x]
    expectations.append(dict(expectation_id=f"F800-S1-E{s['n']:03d}",version=1,status='READY_FOR_EXPECTATION',case_id=cid,
        statement=s['statement'],origin=s.get('origin','BUSINESS_INFERRED'),source_ref=s.get('source',material_ref),
        derivation_refs=[target_ref,u_ref,owner_ref],derivation_reason=s['rationale'],
        applicable_conditions=conditions,non_applicable_conditions=['版本/实例/Calendar不一致。',
            '原价/独立上游或必要中间字段缺失，无法确认本例所列适用条件。'],
        expected_feature_process=s['process'],expected_intermediate_decisions=s['intermediate'],
        support_conditions=s['supports'],falsifier_or_counterevidence=s['falsifiers'],
        ambiguous_conditions=s['ambiguous'],explicit_non_goals=s['nong']+['不执行Q/V/WALL，不做全量业务真值或Feature释放结论。'],
        evidence_needed=needed,known_unknowns=s['unknown']+base_limits[:1],
        confidence=dict(raw_position='高：来源及场景位置可复核',business_expectation='中：候选预期待Skill2支持/反证，Owner明文常量按原文适用'),
        owner_decision_required=False,owner_authority_note='冻结候选可交对照不等于Owner接受所有推导；若后续欲改正式行为或参数，须依原流程新确认。'))
    locations.append(dict(case_id=cid,accepted_html_sha256='df4076f642d4d2b2ac7a6f8cc02899d9cf70e20dd8beb313e347e7545279b450',
        data_stage='construction_snapshot',group_source_ref=group_source,group_rows=rows,
        independent_selected_rows=selected_rows,
        price_sources={symbol:pro_ref('D012',f'formal_data/source_{figures[symbol]}.json.gz') for symbol in s['symbols']},
        browser_window_id=s['window'],case_start=s['start'],case_end=s['end'],
        negative_lookup_scope='仅完整已接受1538组公开成员与独立1859条选中T投影；不代表native未成组pair全轨迹。'))

save('draft/CaseReviewSet.READY.json',dict(case_set_id='F800-S1-D013-CS',version=1,status='READY_FOR_EXPECTATION',
    prepared_at=now(),feature_ref=dict(name='CommonPriceTurnGroupCandidatesFrp',frp='39f02ec4548e68ba8dbd30061afc870546000994',tis='2f460d663d821cf2ba25555eda13e78b697d0767',understanding_ref=u_ref),
    parameter_version=parameter,observation_material_ref=material_ref,review_target_ref=target_ref,
    review_target_section='CurrentReviewTarget',cases=cases,material_limits=base_limits))
save('draft/ScenarioExpectationSet.READY.json',dict(expectation_set_id='F800-S1-D013-EXPECTATIONS',version=1,
    status='READY_FOR_EXPECTATION',prepared_at=now(),parameter_version=parameter,
    case_review_set_ref='CaseReviewSet.json',observation_material_ref=material_ref,expectations=expectations,
    evidence_comparison_performed=False,freeze_policy='正式对照后的新想法另立REVISED版本；不无痕回写本v1。'))
save('CaseMaterialIndex.json',dict(created_at=now(),origin='接受的正式图数据只读定位，非重导出/复算',cases=locations))
save('CaseTypeCoverage.json',dict(case_set_id='F800-S1-D013-CS',version=1,
    types=[dict(case_type=t,status='HAS_QUALIFIED_CASE',case_ids=[c['case_id'] for c in cases if c['case_type']==t])
        for t in ['CLEAR_POSITIVE','CLEAR_NEGATIVE','OUTPUT_FALSE_POSITIVE_CANDIDATE','PARAMETER_BOUNDARY','OUTSIDE_CURRENT_COVERAGE']]+[
        dict(case_type='POTENTIAL_FALSE_NEGATIVE',status='NO_CASE_FOUND',case_ids=[],
            considered_candidate_ids=[f'RAW-{i:02d}' for i in range(1,10)]+['INDEX-F800-SQ-001-C1'],
            reason='先由三品种原价独立提出九处同步局部峰谷，再查当前selected和公开共同组。七处双侧具有同刻selected且能定位共同组；另两处至少一侧无当前同刻selected（RAW-06双侧均无，RAW-09仅i有）。详细浏览RAW-06及i孤立峰，不将无资格/无第二对象改称F漏报。当前没有材料充分且属于本层资格的正式漏报场景。',
            scope_limit='九处是有界浏览初筛，不是全原始转折真值。三年总览/有代表性窗口及数据筛查不证明不存在其他漏报；未公开native枚举首阻断不补造。')],
    sample_size_reason='七案例分别区分共同性、孤立上游、初始化不足、2Delta边界内外、长迟到解释和未获尺度资格的原价共同波动；没有固定各类配额，不为凑漏报类型强造案例。'))
save('ObservationGapRequests.json',dict(requests=[],current_scope='本冻结集只要求已暴露原价、独立选中T/C/known、已发行组及其公开中间字段；当前足以写预期。',
    preserved_missing='内部逐tick枚举/未成组pair/首阻断/原生coverage区间仍NOT_EXPOSED。',
    return_condition='若Skill2为具体预期需要这些尚缺的实际字段，应按case/unit具名回OBSERVATION_MATERIAL_PREPARATION；当前不靠代码推运行值，也不无条件重做M/U/X/G。'))
questions=read_json(U,f'{PREFIX}/professional/D008/ScenarioQuestionQueue.json')
links={'F800-SQ-001':['F800-S1-C001','F800-S1-C002','F800-S1-C005','F800-S1-C007'],
       'F800-SQ-002':['F800-S1-C001','F800-S1-C006'],
       'F800-SQ-003':['F800-S1-C001','F800-S1-C004','F800-S1-C005','F800-S1-C006'],
       'F800-SQ-004':['F800-S1-C003']}
save('OpenQuestions.json',dict(original_question_ref=pro_ref('D008','ScenarioQuestionQueue.json',U),
    original_questions_unchanged=questions,
    this_S1_handling=[dict(question_id=q['question_id'],case_ids=links[q['question_id']],
        disposition='保持原SCENARIO_INTERPRETATION_QUESTION，未判缺陷/未关闭/未编造Owner接受暂缓；冻结适用预期后交Skill2。',
        extra_limit=('时期/Session数量没有业务真值，本冻结集不制定数量或密度配额。' if q['question_id']=='F800-SQ-002' else
                     '稀有framePatches/scopeEnded输入本实例不具，不以零频次判分支错误。' if q['question_id']=='F800-SQ-004' else
                     '长迟到的实时价值及所有未参加Turn的业务真值尚不能由本S1或结构G证明。')) for q in questions],
    additional_questions=[dict(id='F800-S1-OQ-001',question='若后继要按迟到程度评下游实时价值，当前无Owner明确业务可用时限；不能把4000开放分钟自动等于价值保证。',
        impact='不阻断本S1冻结历史共同性/诚实时序预期；若建议新阈值/正式行为改变，再走原诊断/Owner确认。')],
    owner_decision_requested=False))
print(json.dumps(dict(draft_cases=len(cases),draft_expectations=len(expectations),origins={x:sum(e['origin']==x for e in expectations) for x in ('OWNER_EXPLICIT','BUSINESS_INFERRED')},six_types_considered=True),ensure_ascii=False))
