"""本D原生记录；输入复用已接受U/X/G/B，不重新解释Feature。"""
from pathlib import Path
import hashlib
import json
from datetime import datetime,timezone

R=Path(__file__).resolve().parent
B=R.parent
RUN='OI-F800-STAT-20261122-01'
PIN='87b951bbd15078a2d6353bdd24afe0d8f19c845c'
PRO='daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/'+RUN+'/professional/D008/'
def save(name,data): (R/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
bind=json.loads((B/'D009/INPUT_BINDING.json').read_text())
bind.update(checked_at=datetime.now(timezone.utc).isoformat(),delegation_ref='daowei2026/observe-iterate@a33dc91d08a4e888d08af71b6a1769a0db06ae8a:longrun/runs/'+RUN+'/delegations/D010/DELEGATION.json',
    formal_feature_run_in_D010=False,global_statistics_rerun_in_D010=False,feature_semantics_reinvestigated=False,
    heavy_resource_policy='只读结果/日历与隔离HTML/代码，不做正式生产、共享缓存/数据库写入；未申请或声称持有生产flock。')
for k in ('formal_feature_run_in_D009','global_statistics_rerun_in_D009'):bind.pop(k,None)
bind['accepted_B_ref']='daowei2026/observe-iterate@4d429ccb310452467b78b09802c48c9adbc47be5:longrun/runs/'+RUN+'/professional/D009/ObservationPositionPreparationResult.json'
bind['B_not_reselected']=True
save('INPUT_BINDING.json',bind)
save('METHOD_LOCK.json',{'call_id':'C0023','delegation_id':'D010','workers':[],
 'skill_ref':f'daowei2026/observe-iterate@{PIN}:skills/observation-material-preparation/caegraph-display-preparation/SKILL.md',
 'companions':[f'daowei2026/observe-iterate@{PIN}:skills/observation-material-preparation/caegraph-display-preparation/{n}.md' for n in ('WORKFLOW','IO_SPEC')],
 'uplot_ref':'daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md',
 'manual_sha256':'f7dd1061a2b170ec4cfb0a508afd737e195e7ec16db269e5655b63dc06591c19',
 'scope':'原C1/C2A/C2B/C2C/C2D/C3，后续D/E正式绑定；未修改Skill、uplot或F行为。',
 'allowed_operations':['run_result_statistics_analysis_write','run_record_write'],'owner_original_sha256':'a9c626ec667171e7f4605b853d360597a471d6bc82002574f938ab4d269058eb'})
items=[]
def item(i,source,role,include,why,positions,identity,values,relationship,status):
 items.append(dict(信息编号=i,来源对象事件中间判断编号=source,业务角色=role,是否纳入展示预期=include,展示或不展示理由=why,
   已确认的位置字段=positions,已确认的身份引用字段=identity,原值字段=values,形成业务主输出的关系=relationship,运行结果可用状态=status))
item('C1-01',['O1'],'输入','是','原价和有效/缺值样本是转折来源；不做跨品种隐式标准化。',['KLine事件timestamp','openUti/closeUti'],['对象symbol','原始事件轴'],['open','high','low','close','volume'],'价格→Rct→ScaleTurn；缺close不能补前值。','AVAILABLE')
item('C1-02',['BO1','R1'],'输入','条件展示','上游实际Rct已独立导出；仅作为已暴露原始输入，不视作完整市场转折分母。',['实际T','几何C','上游事件timestamp'],['symbol','上游Turn exact/事件坐标'],['Rct实际价与确认价'],'原始turn经选择形成BO2。','AVAILABLE')
item('C1-03',['BO2','O2','R1'],'输入','是','区分实际/几何确认/上游被选已知；value1/value2保留round，不用F成员表补出未参加的turn。',['actual/T','geometry C','ScaleTurn原事件轴selected-known','P/T/C pointActual与pointKnownFrom'],['symbol','Turn Life/Revision exact','round','完整上游事件坐标'],['T/C价格','方向/类型/状态'],'同一turn可加入多组，已知晚于实际不回填发布。','AVAILABLE')
item('C1-04',['BO3','O4','R3'],'业务主输出','是','每个已发行候选组修订为主输出；图只显示稀疏发布，不插值逐tick状态。',['publication timestamp','groupKnownFrom'],['group Life/Revision idText','timestamp/occurrence/record_id/child_id_2'],['groupLocalBasis','groupObservation','groupCoverageIncomplete','groupClosed'],'BO2组合→BO3 exact revision；无变化tick不发行。','AVAILABLE')
item('C1-05',['BO2→BO3','O4'],'中间处理结果','是','从主输出追到确切成员，保留成员重用、撤回与round。',['memberActual','memberConfirmation','memberKnownFrom','memberT/C pointActual/pointKnownFrom'],['完整父坐标+所有child层级','memberObject','memberTurn/Source exact'],['memberPrice','memberStatus','memberRetracted','memberRound'],'成员与group按完整父前缀关联，不能按timestamp或known单独合并。','AVAILABLE')
item('C1-06',['ST1','ST2','ST3','ST4'],'状态','是','依据/观察/覆盖/形成关闭/责任关闭分别保留，不把Subsumed或closed解释成退出活跃。',['groupKnownFrom','participationDecisionKnown'],['exact group修订及对应participation子行'],['groupLocalBasis','groupObservation','groupCoverageIncomplete','groupClosed','participationDutyClosed'],'解释同一修订的独立状态，内部active逐tick轨迹仍未暴露。','PARTIAL')
item('C1-07',['J5','BO3'],'关键判断','是','展示当前修订携带的窗口界限及冻结准入，用显式裁剪与明细保留原值。',['OriginalAnchor/Deadline/RevisionEnd','Anchor/Deadline/RevisionEnd','participationAdmissionKnown','participationQuestionAnchor/Deadline/RevisionEnd','participationHandoffEnd'],['Life+Revision','participationAdmission/Candidate definitionexact'],['原始及当前界限UTI','DutyClosed'],'800窗口、6Δ责任尾和18Δ移交不是逐tick材料存在区间。','AVAILABLE')
item('C1-08',['R3','R4'],'关键判断','是','Previous/Alternative/CoveredBy/Bridge按exact目标保留；页面以精确明细优先，不合并Life。',['关系发布timestamp/known','exact被引用修订'],['各关系的Life/Revision','全部父子坐标'],['previous/alternative/coveredBy/bridge所有已发行字段'],'重用成员、严格超集和覆盖不代表相同对象。','AVAILABLE')
item('C1-09',['J2'],'中间处理结果','条件展示','只在主输出明细读已发行Required/Distance，非全pair验证矩阵。',['父组发布位置'],['pairLeft/Right exact及所有child坐标'],['RequiredVerdict/Gap/Veto四维','distanceValue'],'解释当前候选发行依据；未成组pair/失败组合不补画。','PARTIAL')
item('C1-10',['O3'],'输入','条件展示','首个publication可能仅definitions；保留原始表/空表状态，不造候选点。',['wrapper事件timestamp/occurrence'],['definition exact','root坐标'],['definitions'],'方法/尺度/范围元信息进入明细与绑定，不做一表一面板。','AVAILABLE')
item('C1-11',['J1','J3','J4'],'中间处理结果','否','逐tick材料准入、失败枚举、first blocker和原生coverage区间NOT_EXPOSED；图仅保留已发行coverage flag。',[],[],[],'不得用示意/几何推算冒充F原生轨迹。','NOT_EXPOSED')
item('C1-12',['BO1外全集','独立selected_time','groupCreateTime'],'输入','否','全市场未识别转折分母未暴露；独立selected_time/groupCreateTime不存在，不构造伪原生字段。',[],[],[],'上游导出不等于全市场全集；首次Life/冻结admission可在明细阅读，不改名成原生创建字段。','NOT_EXPOSED')
save('C1_INFORMATION_LIST.json',{'FeatureUnderstandingPackage引用':PRO+'CurrentFeatureUnderstandingPackage.json','理解状态':'PARTIAL','信息清单':items,'完整Schema引用':PRO+'PUBLIC_TABLE_SCHEMA.json','边界':'合成样例只演示布局；不补造未暴露业务轨迹，不选正式正反例。'})
save('C2A_MANUAL_READING.json',{'手册版本':'daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md',
 '亲自直接阅读':True,'远端原件核对':'REMOTE_DISPATCH_READBACK.json',
 '已读章节':[{'章节':'文档说明/名词定义/相近多品种组合示例','行':'4–32,87–227'}, {'章节':'构建链/CAEGraph/PlotSet','行':'372–461'}, {'章节':'布局快速选择及AllSymsMainFig/AllSymsFig/PerSymFigs/PerSymFigSet/MainFig/SubFig/OneFig','行':'463–606'}, {'章节':'绘图快速选择/KPriceLine','行':'607–683'}, {'章节':'VBar/MulFieldsGlyphs/MulSegPlot/SegsPlot/TextPlot及旧绘图类的限制','行':'708–1020'}, {'章节':'BaseFigSet/BasePlotter及类关系','行':'1255–1350'}],
 '候选布局类':[{'类':'AllSymsMainFig','判断':'支持多品种同轴；本预期保留原价，量纲不同，不作共同价格轴。'}, {'类':'PerSymFigs','判断':'采用逐品种独立原价纵轴、同一UTI横轴。'}, {'类':'PerSymFigSet','判断':'可选逐品种主附图；本任务核心输出跨品种，集中附图更直接。'}, {'类':'SubFig','判断':'采用共同业务输出及必要输入附图。'}],
 '候选绘图类':[{'类':'KPriceLine','用途':'std_method=None原价'}, {'类':'MulFieldsGlyphs','用途':'多位置点、离散稀疏修订'}, {'类':'MulSegPlot/SegsPlot','用途':'同记录端点/携带界限，须核实裁剪'}, {'类':'TextPlot/VBarPlot','用途':'标签/离散量；无必要不造额外面板'}, {'类':'OneToGroupPointPlot','用途':'手册无实际可用例，不能仅凭类名承诺避碰/精确引用交互'}],
 '补查源码':[{'文件':'utlv2.py','行':'54–62,621–808,854–1000,1244–1597','核实':'实际API参数、currTarget多品种字符串要求、K线及点/段数据生成、PlotSet/CAEGraph的上下文/布局'}, {'文件':'utkv2.py','行':'44–225,290–330','核实':'共享x_range、独立figure、图例click_policy=hide'}, {'文件':'pfw.py','行':'172–320,468–590,730–897','核实':'时间转换、数据裁剪、默认hover只有时间和值、LiveUpdater/只读provider入口'}],
 '已确认能力':['原价K线与点/段组合','PerSymFigs+SubFig共享同一x_range','图例显隐与缩放','只读DataFrame provider，不运行真实Feature'],
 '尚未核实能力':['复杂同刻多修订身份/字段明细交互，需在C2C/D实际预览后核实','边界裁剪与原始值同时保留，需真实原型验证'],
 '未修改uplot':True})
save('OUTER_INSTANCE_USE.json',{'是否读取外层实例':'是（只读已接受结果绑定、Schema及极小公开表样例；未调用真实Feature）',
 '实例引用与版本':PRO+'FeatureRunResultBinding.json','使用目的':['字段/表形状核实','当前版本与共享Package映射核对'],
 '读取内容':['完整PUBLIC_TABLE_SCHEMA','occurrences/groupMembers/groupFormationParticipation各首行的公开坐标及状态形状'],
 '与共享字段映射核对':'一致；PARTIAL U和不可暴露内部轨迹限制保留。','是否进入C3正式代码':'仅instance+reader+context参数；不固化对象、SOF/运行目录/运行状态。',
 '预览实例绑定':'无真实实例；preview.py使用合成数据，SOF仅提供交易日历坐标。',
 'D需要替换的内容':['外层instance与只读reader','context/SOF','B位置symbols/start/end/calendar','原始字段/枚举/表及child映射']})
save('SOURCE_RETENTION.json',{'四项问题引用':PRO+'ScenarioQuestionQueue.json','七项candidate_only来源引用':PRO+'CandidateCaseIndex.json',
 'B来源对齐引用':'daowei2026/observe-iterate@4d429ccb310452467b78b09802c48c9adbc47be5:longrun/runs/'+RUN+'/professional/D009/PositionSourceAlignment.json',
 '未选择正式案例':True,'未冻结业务预期':True,'预览未绑定候选索引':True,'未修改有效X_G_B':True})
save('C2_FIRST_EXPECTATION.json',{'第一版预期编号版本':'F800-C2-v1','页面与阅读路径':'逐品种原价/输入多位置→跨品种候选稀疏发布',
 '主图附图和明细':['PerSymFigs：每品种原价K与T/C/上游已知点','SubFig：groupKnownFrom上的依据编码点'],
 'C1信息映射':{'价格面板':['C1-01','C1-03'],'输出附图':['C1-04','C1-06'], '尚需完善':['C1-02','C1-05','C1-07','C1-08','C1-09','C1-10']},
 '已确认的位置关系表达':'T/C/上游known分别取同一selected记录；候选点用发布known，不回填actual。',
 '图元图例hover交互':'KPriceLine+MulFieldsGlyphs，默认hover时间和值，共享横轴/legend显隐。',
 '使用的CAEGraph能力':'C2A已确认PerSymFigs/SubFig、KPriceLine/MulFieldsGlyphs、PlotSet/CAEGraph',
 '原型代码引用':'archive/prototype_v1.py','第一版HTML引用':'html/first.html','样例数据与预览绑定':'PREVIEW_BINDING_v1.json；所有业务值合成，非B/正式场景。'})
print('原生C1/C2A与首版预期记录已形成')
