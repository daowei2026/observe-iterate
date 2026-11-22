"""从已通过的D定义检查形成原IO记录；不构图、不正式取数。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
import json
import subprocess

ROOT=Path(__file__).resolve().parent
RUN='OI-F800-STAT-20261122-01'
BASE=Path('/dwdhome/fy/BASE_E6_2_copy')
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'executor-records'
PACKET=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122')/RUN/'C0025-dispatch-packet.json'
P=json.loads(PACKET.read_text())
CHECK=json.loads((ROOT/'DEFINITION_CHECKS.json').read_text())
BOUND=json.loads((ROOT/'BOUND_INSTANCE_CHECK.json').read_text())
assert CHECK['all_passed'] and CHECK['native_feature_run_calls']==0 and not CHECK['final_graph_built']
def load(n):return json.loads((ROOT/n).read_text())
def write(n,x):(ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ref(d,n,c):return f'daowei2026/observe-iterate@{c}:longrun/runs/{RUN}/professional/{d}/{n}'
U=ref('D008','CurrentFeatureUnderstandingPackage.json','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca')
X=ref('D008','FeatureRunResultBinding.json','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca')
B=ref('D009','OrdinaryPositions.json','4d429ccb310452467b78b09802c48c9adbc47be5')
C=ref('D010','C2_CURRENT_EXPECTATION.json','ec747f4d460956bd1a91f59d0dcbaba6722ce750')
HTML=ref('D010','html/current.html','ec747f4d460956bd1a91f59d0dcbaba6722ce750')
C3=ref('D010','display_code/caegraph_display.py','ec747f4d460956bd1a91f59d0dcbaba6722ce750')
write('INPUT_BINDING.json',dict(run_id=RUN,call_id='C0025',delegation_id='D011',delegation_ref=P['delegation_ref'],invocation_ref=P['invocation_ref'],
    task_skill_ref=P['delegation']['task_ref'],record_base_head='9cd294ffc80bba7ebdbe8bb2889eb1bb77e826d2',
    record_branch=P['record_branch'],workers=[],permitted_operations=P['delegation']['permitted_operations'],
    allowed_writes=P['delegation']['allowed_writes'],owner_approval_ref=P['binding_adoption']['approval_ref'],binding_ref=P['binding_adoption']['binding_ref'],
    actual_current_instance=X,understanding_ref=U,position_ref=B,display_expectation_ref=C,expected_html_ref=HTML,display_code_ref=C3,
    exact_source_audit='SOURCE_REF_AUDIT.json',source_count=load('SOURCE_REF_AUDIT.json')['count'],
    local_inputs='inputs/目录为准确上游原件副本；base_parameters只抽取D001正常构造形参，无新业务参数',
    current_frp='39f02ec4548e68ba8dbd30061afc870546000994',current_tis='2f460d663d821cf2ba25555eda13e78b697d0767',
    configuration_sha256='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3',
    dependencies='DEPENDENCY_BINDING.json',source_data='SOURCE_DATA_BINDING.json'))

read_files=[
 ('__init__.py','全文','正式导出CAEGraph/PlotSet、布局、绘图及pdt；OptContext/CurrSymbol实际由utlv2可访问，不从frame误导入'),
 ('CAEGraph使用手册.md','1–103、372–480、630–850、1255–结束','本次顶层构建、普通多品种布局、K线/多字段点/段及基础链；具体参数仍以0a4源码为准'),
 ('utlv2.py','1–62、621–775、854–992、1244–1576','currTarget、KPriceLine、MulSegPlot、MulFieldsGlyphs、PlotSet、CAEGraph'),
 ('utkv2.py','1–336','BaseFigSet构造/finish、AllSymsFig、PerSymFigs：共享x_range、独立y_range、legend.hide、fit_y回调'),
 ('pfw.py','1–100、172–360、435–622、759–902','PlotCtx自然TSA/含结束UTI、截取、DataFrame到CDS、LiveUpdater/只读provider路径'),
 ('pdt.py','全文','PlotDataFolder.children、PlotDataNode.cds、数据形状/耗时树'),
 ('fit_y_range.js','全文','原价/输入图的视窗纵轴适配；只读CDS有限值，非价格标准化'),
]
snap=load('UPLOT_SOURCE_SNAPSHOT.json')
rows=[]
for path,lines,why in read_files:
 info=next(f for f in snap['files'] if f['source_path']==path)
 rows.append(dict(文件=path,已读范围=lines,本次理解=why,源码ref=f'daowei2026/uplot@{snap["commit"]}:{path}',sha256=info['sha256']))
write('REPOSITORY_UNDERSTANDING.json',{
 '仓库与版本':{'repository':'daowei2026/uplot','commit':snap['commit'],'tree':snap['tree'],'source_snapshot':'source/uplot','shared_dirty_worktree_modified':False},
 '已读文件':rows,
 '正式导出与导入路径':'CAEGraph/PlotSet/PerSymFigs/AllSymsFig/KPriceLine/MulFieldsGlyphs/MulSegPlot从mquant.uplot正式导出；OptContext/CurrSymbol沿utlv2实际导入链。本D bootstrap在单进程替换package路径到准确20文件快照，不改共享uplot。',
 'CAEGraph／PlotSet配置链':'build_bound_display→原C3.build_display→CAEGraph(Context=真实OptContext,plotsets=GMap)→layout→produce_widgets→CurrTradeSet(Context.sof)→PlotSet.plot；calendar=night_end_at_2300、blk=[rb,hc,i]、timespans为实际B的含端点UTI。',
 '布局类源码理解':'PerSymFigs逐品种建立CurrSymbol/CurrSymbolPable和独立原价fig；AllSymsFig.persym_plots在上游known图遍历全部品种；global output用sym_plots首品种只提供合法上下文，gf不按symbol筛选。ctx.x_range由首图建立后供全部fig引用。',
 '绘图类源码理解':{'KPriceLine':'feat.rerun().to_df→ctx.slice_natural_df；明确openUti/closeUti；保留NaN；std_method=None，避免fallback几何端点。','MulFieldsGlyphs':'GMap provider、dfkeys、xfields/yfields，timefieldtype=uti→PlotCtx.live_feat_data→CDS scatter；actual、confirmation、selected-known、groupKnownFrom分别绑定。','MulSegPlot':'同记录T→C及携带a→d/d→r；timefieldtype=uti，dynstd_method=False；原C3仅裁剪显示端点，保留原始坐标。'},
 '特征实例进入路径':'正常make_features基线F复制profile且只override800→真实CommonPriceTurnGroupCandidatesFrp；完整序列化与full_dir精确相同。reader接收该真实实例，E时只调用instance.run(CalType.OnlyRead)/to_dfs；D未调用。F公开表→C3内存InjectedFrames→绘图器feat。行情/Rct/selected使用同实例已验收物化源，校哈希，非新计算。',
 '位置进入路径':BOUND['boundary'],
 '数据到CDS路径':'C3.project保留原列并增加展示别名/__original_json；主组完整父键唯一，全部子表完整父前缀关联；InjectedFrames.to_dfs/to_df及rerun只读内存。KPriceLine直接切DF，点/段经PlotCtx.live_feat_data/LiveUpdater驱动同一内存provider，再gen_cols创建CDS并ctx.add_cds。',
 '构图数据树':'CAEGraph.layout(plot_roots=roots)→PlotDataFolder(plot_name)→plotset/位置folder→布局/品种folder→PlotDataNode。叶持真实CDS；C3 attach在同一cds补原值/身份，点表下拉共用source。E3通过后E4可从build_bound_display返回meta.roots叶cds正式导出；D未构造任何树或数据。',
 '动态与前端路径':{'DynStd':'本次不启用：K std_method=None，点/段dynstd_method=False；源码已核，不执行dynstd.js。','fit_y':'BaseFigSet._finish_fig按ctx.y_fits注册fit_y_range.js至共享x_range.start/end；output图关闭fit_y_range，其余原价/输入沿C2。','控件':'无prange/slider或server参数控件；LiveUpdater只为只读InjectedFrames执行更新；C3既有Bokeh Select/DataTable/Div/CustomJS在独立HTML中联动。','前端':'选择共享revision_source.selected.indices；JS把raw JSON作为经HTML escape的文字显示，不JSON.parse，不把uint64交JS浮点；图例hide、各图十字线、hover沿原C3。','多尺度与server':'不适用，B为普通明确三年位置；不使用multiscale/app/bkapp，不补建多尺度路径。'},
 '真实Feature读取源码':['TIS2f frp/CommonPriceTurnGroupCandidates.py全文：to_dfs/GroupCandidateReadSession/ENUMS；frp/U2CompactTables.py 67–125：F已有materialized读取；frp/U2CoreResults.py 142–188：_public保留timestamp+occurrence+全部child。','frame.lang.internal.base.run/_run_own/_run_with：OnlyRead选择write=False/read=True，缺文件直接报错，不转生产；同版已接受D008提供实际API读回证据。','frame.core.app.utils.opt_date_range、frame.core.data.KDataLoader及quant.core.ctx.OptContext.sof、m3sof.core.sof.tsa_of按实际源码核本次日期/SOF/日历链；17个实际依赖按内容锁。'],
 '尚待E运行确认':'E_PENDING.json；本D没有实际调用build_bound_display、原生reader、CAEGraph.layout、浏览器或HTML输出。'
})

corrections=[]
def correction(i,source,location,problem,before,after,basis,downstream):
 corrections.append({'问题编号':i,'来源':source,'原产物位置':location,'问题说明':problem,'是否能由D确定性纠正':'是','唯一修正依据':basis,'修正前':before,'修正后':after,'是否改变位置选择':'否','是否改变展示预期／HTML':'否','是否引入新业务判断':'否','证据与理由':basis+'；原始字段/上游原件不改，失败条件显式拒绝。','处理结果':'D直接确定性补齐并继续；不是认定上游业务语义错误','影响的下游绑定':downstream})
correction('D-BIND-01','B','OrdinaryPositions.json位置定义/缺口与限制','B明确把日期粒度/结束边界解析留给D，需接入PlotSet；不是重新选位置。','2021-01-01—2023-12-31日期标签',BOUND['boundary'],'同一真实F的SOF与frame.opt_date_range既有21:00/20:00规则；准确0a4 PlotCtx整数含端点。right-1取原period内最后一个交易标签，杜绝周末left+1扩入下一期。','OptContext/PlotSet.timespans/C3 position；72003600—101813399')
correction('D-BIND-02','C3','INJECTION_CONTRACT字段UTI检查/FIELD_MAP_TEMPLATE groups','原native六个a/d/r边界声明float64，C3要求整型UTI，需表示适配。','字段模板直接映射groupOriginalAnchor等原float64列','新增__uti_*别名；有限、abs<=2**53、本身为整数且回转相等后转int64；原float64列保留','准确PUBLIC_TABLE_SCHEMA的六float64字段+U已确认同一CalendarUTI轴+C3整型合同；1538行六字段兼容性检查通过。非有限/分数/超精度直接拒绝，不四舍五入。','FIELD_BINDING.groups六轴/C3窗口；定义适配不改Feature存储')
correction('D-BIND-03','C3','FIELD_MAP_TEMPLATE selected.round与原上游规范形状','模板已明示round_display但外层公开源round为value1/value2，D需接线。','round=value1/value2，round_display尚未提供','保留原round，新增round_display value1→0/value2→1；turn_id明确为公开源简化定位键','准确C2偏移=品种序号+0.15×round与TIS2f FirstRound=0/SecondRound=1；模板已有明确要求，不增新轮次或业务身份。','input-known偏移/原值hover；member native exact仍在完整children')
write('UPSTREAM_CORRECTIONS.json',{'上游确定性纠正记录':corrections,'原C3源码修改':False,'实际新增绑定':'以上是原D明确承接的机械补齐，不更改B/C原件或C2-v4','返回共享理解问题':[],'返回B问题':[],'返回C问题':[],'阻塞问题':[],'D本地检查修复':[{'attempt':1,'问题':'csv.DictReader表头保留UTF-8 BOM，错误认为缺symbol','处理':'检查器和实际reader明确utf-8-sig；原文件不改','保留':'attempts/01-*','业务位置或展示变化':False}]})

integration={
 'C3代码编号／版本':'F800-C3-v1','C3代码准确引用':C3,'C3代码SHA256':'e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0',
 'C2当前展示预期版本':'F800-C2-v4','C2当前预期HTML':HTML,'C2当前HTML_SHA256':'3a24ab08887ce5d948b229e7d37f63a4f9a669218b47110ad4385f737a7bdded',
 'FeatureUnderstandingPackage引用':U,'预览实例绑定':'原C2-v4所有业务值/SYN身份和2022短窗只为预期预览；D未导入preview.py或其样例DATA，未生成另一预期HTML。',
 '正式特征实例绑定':{'ref':X,'code':'definition/f800_definition.py::construct_instance','check':'BOUND_INSTANCE_CHECK.json','configuration':'inputs/configuration.json','instance':BOUND['instance']},
 'Feature／数据入口绑定':{'F':'read_bound_frames(instance,position)→精确目录fields哈希→instance.run(CalType.OnlyRead)→to_dfs全部31表；E时执行，D未调用。','价格/Rct':'同实例已验收D008 upstream的各symbol_kline/rct.csv，校各原哈希；保留NaN、事件timestamp和open/closeUti；不调用任何上游生产。','selected':'已接受D008 profile/scale_turns.csv的公开源13列投影，known再与原event timestamp对应Kline.closeUti核对；round显示编码；不把eligible_*_reference/first_block_screen/bend等G分析列升格原生F。','所有原生子表':'occurrences_*全部传入children，不取首个参与行，不丢更深child，不按known拼接；4张definitions族公开表原样含坐标进入metadata。','来源':'SOURCE_DATA_BINDING.json'},
 '普通位置绑定':{'ref':B,'requested_sof':{'sof_name':'TA_updto20240229_DBA','stk_tlist':'steel','startDay':'2021-01-01','endDay':'2023-12-31'},'actual_C3_position':BOUND['position'],'boundary':BOUND['boundary']},
 '多尺度位置绑定':None,
 '共享字段绑定':{'file':'FIELD_BINDING.json','groups':'full parent/Life+Revision无损uint64UUID解码、known、original/current a/d/r、basis/observation/coverage/closed分别进入点/携带窗口/明细。','children':'所有成员/P/T/C、Required/Distance、Previous/Overlaps/CoveredBy及Participation/Bridge原值按原坐标关联。','identity':'UUID整型字段保持原生uint64，C3 Python精确解码；原JSON文本不经JS解析；上游简化turn_id不是native exact。','state':'_name沿TIS2f正常reader ENUMS；原码保留，dutyClosed[]和formationClosed独立。','limits':'原U PARTIAL；逐tick材料/失败组合/first blocker/coverage区间未暴露；空子表NOT_PUBLISHED语义不改。'},
 'C3→D代码差异':{'C3_renderer_diff':[],'C3_renderer_byte_equal':True,'new_complete_definition':'definition/f800_definition.py','new_launcher':'run_definition.py','new_bound_field_map':'FIELD_BINDING.json','source_bootstrap':'单进程加载准确0a4快照，17实际依赖哈希锁；不改共享库。','C2标题':'原C3内页标题仍为F800 · C2当前展示预期；D不无痕改标题，真实绑定和历史投影在caption及HTML文档标题明确。'},
 '上游确定性纠正':'UPSTREAM_CORRECTIONS.json（D-BIND-01—03）','是否改变展示语义':'否','能力缺口处理':'C未解决工具缺口为空；沿已接受原值明细替代全局拓扑/跨源自动高亮；U/数据未暴露边界保留。'
}
write('DEFINITION_INTEGRATION_RECORD.json',integration)

pending=[
 {'编号':'E-01','待确认':'在同一锁定环境实际执行完整脚本，验证准确F OnlyRead/to_dfs、物化上游源和全部图层能成功进入原生CDS。','D已完成':'真实构造/配置/目录/fields/源哈希及字段声明、六坐标兼容性；未调用reader。','回流':'字段/实例/接线问题回D；若缺合法源只报缺失，禁止重生产。'},
 {'编号':'E-02','待确认':'真实三年149049根K线及1538修订的构图、独立HTML序列化、浏览器性能和实际可读性。','D已完成':'完整范围及C2结构在代码中；没有借合成预览代实际运行。','回流':'位置变更回B，展示语义变更回C，工程/API问题按E原Skill处理。'},
 {'编号':'E-03','待确认':'真实点/段数量与位置、同刻多观点分行、完整child/空表状态、NaN、无损exactID、边界裁剪及源值核对。','D已完成':'C3原码及原父键合同保持，Float64窗口加严格无损别名，不猜未暴露语义。','回流':'绑定问题回D，共享事实不清回U。'},
 {'编号':'E-04','待确认':'浏览器实际hover/点表下拉联动、图例、共享x_range/fit_y、十字线及console，核对D和唯一C2-v4 HTML。','D已完成':'准确0a4调用链及原C3 JS源码核实；D未开启浏览器或生成HTML。','回流':'以E真实运行判断，不能引用C合成浏览器证据代签本次E3。'},
 {'编号':'E-05','待确认':'E3实际核图通过后，E4从被接受运行meta.roots原生CDS正式导出图数据，E5核一致性，E6材料。','D已完成':'完整脚本暴露meta.roots；D没有图树/正式数据/最终HTML。','回流':'manager按原流程签发后继E；本D不签DATA_READY/场景预期/Release。'}
]
write('E_PENDING.json',{'仅由E真实运行确认的事项':pending,'D未完成核心绑定项':[],'本D真实运行证明':False,'E3核图':False,'E4正式图数据':False,'E5一致性':False})
expected_html=str(BASE/'artifacts'/RUN/'caegraph-E/f800.html')
output={
 '定义编号与版本':'F800-D-v1','阶段':'M-D','阶段状态':'完整',
 'Python脚本引用':'run_definition.py + definition/f800_definition.py + 逐字C3 definition/caegraph_display.py',
 '特征名称':'CommonPriceTurnGroupCandidatesFrp','特征实例引用':X,'FeatureUnderstandingPackage／B／C版本':{'U':U,'B':B,'C2':C,'C2_HTML':HTML,'C3':C3},
 'CAEGraph仓库版本':{'repo':'daowei2026/uplot','commit':snap['commit'],'snapshot':'UPLOT_SOURCE_SNAPSHOT.json'},
 '数据入口与位置绑定':'DEFINITION_INTEGRATION_RECORD.json、SOURCE_DATA_BINDING.json、BOUND_INSTANCE_CHECK.json',
 '展示与字段绑定':'FIELD_BINDING.json、原C3-v1；页面/图元/语义沿C2-v4',
 '上游问题处理记录':'UPSTREAM_CORRECTIONS.json；无未解决的B/C/U具名回流',
 'C3→D集成差异':'DEFINITION_INTEGRATION_RECORD.json、INTEGRATION_DIFF.md',
 'CAEGraph仓库理解记录':'REPOSITORY_UNDERSTANDING.json',
 '预期输出HTML路径':expected_html,'预期HTML当前是否存在':Path(expected_html).exists(),
 'E运行命令':'PYTHONDONTWRITEBYTECODE=1 bash /dwdhome/fy/BASE_E6_2_copy/run-python.sh /dwdhome/fy/BASE_E6_2_copy/artifacts/'+RUN+'/D011/run_definition.py --output-html '+expected_html,
 '定义级检查结果':'DEFINITION_CHECKS.json（10项通过；首次BOM检查失败档案保留）',
 '待E确认项':'E_PENDING.json','未完成项':[],'阻塞项':[],
 '完整状态解释':'按原D IO已核仓库调用链，真实实例/完整B位置/共享字段进入完整脚本且检查通过，可直接交E尝试运行；不表示E运行/核图/正式取数已完成。',
 '继承限制':{'U':'PARTIAL','内部轨迹':'NOT_EXPOSED','四问题七候选':'保持，仅candidate-only，D未选正式场景','Q/V/WALL':'未运行或放行，保留既有Q依赖边界','X/G':'D008有效成果复用，不重跑','原C0020审查':'继续引用，不重复形成'},
 '专业范围声明':{'formal_feature_run':False,'final_graph_built':False,'final_html_generated':False,'formal_graph_data_exported':False,'ObservationMaterialPackage_DATA_READY':False,'scenario_expectation_frozen':False,'FeatureReleaseGate_or_ReleasePackage':False,'workers':[]},
 'prepared_at':datetime.now(timezone.utc).isoformat()
}
assert not output['预期HTML当前是否存在']
write('CAEGraphDefinitionIntegrationResult.json',output)
(ROOT/'INTEGRATION_DIFF.md').write_text('''# C3→D 集成差异

原renderer `definition/caegraph_display.py` 与C3-v1逐字相同，SHA-256 `e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0`；没有重做图，没有改C2-v4或生成另一预期HTML。

| 原C接口/样例 | D实际绑定 | 依据/留痕 |
|---|---|---|
| instance未绑定；预览为SYN | 正常make_features的基线F复制profile，仅override800；真实F实例序列化/目录逐项核同D008 | construct_instance / BOUND_INSTANCE_CHECK |
| reader占位 | 真实F OnlyRead/to_dfs全部31表；行情/Rct/selected从同实例已接受物化入口只读并校哈希 | read_bound_frames / SOURCE_DATA_BINDING |
| context/SOF由调用方提供 | TA_updto20240229_DBA/steel，2021-01-01—2023-12-31；D008平台存储路由，D011日志 | bound_environment / OptContext |
| 样例2022短窗 | 原B明确rb/hc/i、5m三年；原SOF日期规则及真实Calendar解析为含端点UTI72003600—101813399 | D-BIND-01；原请求不缩短 |
| native Float64窗口与C3整型接口 | 原值不改，严格核验后增加六个__uti_*别名 | D-BIND-02；拒绝非有限/分数/精度丢失 |
| round_display示例占位 | value1/2原值保留，显示0/1；选中known来自原事件轴，不用几何C替代 | D-BIND-03 |
| group/children/metadata占位 | occurrences及所有26子表完整父键/child层级；其余4张definitions族原值进入metadata | FIELD_BINDING / 原Schema |
| 原G公开规范源含参考筛查 | 仅取公开源13列；不把eligible/first_block/bend等分析派生作为原生轨迹 | adapt_selected及元数据来源声明 |
| 旧共享uplot版本/脏工作树 | 单进程加载20文件准确0a4快照；17实际依赖内容锁 | run_definition.bootstrap |
| 原C3页面标题 | renderer内标题逐字保留，真实绑定/历史位置投影由caption及HTML文档title明确 | 不无痕调整C2页面/图元/交互 |

新增完整实例集成定义和启动器见Python文件；C3文本diff为空。各派生表示、源字段、显示语义及上游确定性补齐详见DEFINITION_INTEGRATION_RECORD/UPSTREAM_CORRECTIONS；无回流。E未来若需改变位置/展示/理解，按原Skill具名回流。
''')
(ROOT/'EXECUTOR_REPORT.md').write_text(f'''# D011 / C0025｜M-D CAEGraph定义集成

原E1亲自完成原D单一集成动作，阶段状态为**完整**，定义 `F800-D-v1` 已形成，可直接交E尝试运行。复用有效U/X/G/B/C，workers=[]；不重做D001理解，不重复生产/统计。

完整脚本为 `run_definition.py`、`definition/f800_definition.py` 及逐字保留的C3 renderer。真实CommonPriceTurnGroupCandidatesFrp正常构造，完整序列化配置、目录及fields身份核同D008：FRP39f、TIS2f、配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。instance传入真实只读reader；E时F经OnlyRead/to_dfs，公开上游用已接受D008物化源，不缺失回算。

B明确rb/hc/i、5m、2021-01-01—2023-12-31，原SOF/steel/Calendar。按既有SOF日期规则和真实Calendar解析为含端点UTI `72003600—101813399`，最后label是2023-12-29 15:00。原请求仍保留三年；没有按实际行情首末点缩短范围。原C2-v4唯一预期HTML及C3-v1准确字节保持，页面/图元/交互/语义未改。

D记录三项确定性补齐：B日历/结束端点；原native六个Float64窗口坐标到C3整型UTI的严格无损别名（原列保留）；value1/value2到显示round0/1。完整依据、前后、唯一性及无新业务选择见 `UPSTREAM_CORRECTIONS.json`。UUID原uint64及全部父键/child深度保留；31表中26个occurrences子表和4张definitions族均有明确接入，绝不按known合并。上游turn_id明确为公开源简化定位键，原生member exact在children；G参考筛查列不冒充F轨迹。

已亲读并按本次定义解释准确0a4导出、配置、布局/绘图、PlotCtx/DF/CDS、LiveUpdater/内存provider、pdt图数据树和实际fit_y/CustomJS前端路径；20文件快照不改共享脏uplot，17个实际依赖按内容锁。TIS冻结目录没有独立Git，按真实TIS仓库2f准确对象及已接受输入链文件核版本，未把父目录Git HEAD冒充TIS版本。详见 `REPOSITORY_UNDERSTANDING.json`。

**10项定义级检查通过**，含真实正常构造、参数/目录/fields、B日历端点、字段/父键/全部子表、1538行六坐标兼容性和错误拒绝、轮次接线与源哈希。首次检查器因CSV BOM误报缺symbol；修正utf-8-sig后复验，失败原件保留 `attempts/01-*`。检查进程禁止真实Feature.run和CAEGraph.layout，未调用reader/build_display、未生成最终HTML、图树或正式图数据。定义检查不是E运行/核图/取数。

原D无未完成核心项、阻塞或具名回流。E仍须真实运行、核图对照D/C2-v4、再从被接受图树正式取数并核一致性，见 `E_PENDING.json`。原U PARTIAL、未暴露轨迹、四问题/七candidate-only和Q边界保留；D未冻结场景预期、未代签材料DATA_READY或FeatureRelease。

Owner要求的连续状态：D001已接受；X在D008已实际新生产完成，历史producer2050192/native2050491均结束；结果目录沿 `inputs/FeatureRunResultBinding.json` 的准确full_dir；G已完整完成且有效、两finding已关闭、PASS_TO_SCENARIO_REVIEW。本D不启动正式Feature进程或重跑X/G，当前D无阻断，E尚待原manager按既有流程签发。

专业发布与V2 Return按两次独立提交回原manager。仅本D/C0025交付完成，不表示manager已消费、父Run或业务释放完成。原gate/schema适配及实际核验边界见 `VALIDATION.md` 和本C `RETURN_VALIDATION.json`。
''')
(ROOT/'VALIDATION.md').write_text('''# D011验证边界

`DEFINITION_CHECKS.json`是原D IO要求的定义检查，非另设专业Gate；10项通过。真实Feature.run/CAEGraph.layout在检查进程强制禁止；只构造参数、核日历/源字节/字段和源六坐标兼容性。没有运行最终定义、浏览器核图或正式图数据，E才可形成这些证据。C合成浏览器结果仅作为既有预期，不代本次E。

原87b的longrun_gate.py及schema保持原字节。原CLI binding()固化ChatGPT manager类型，与本Run既有CODEX_NATIVE_DIRECT/Codex Binding不兼容；沿前C已披露的做法，用原gate的validated、pro_state和object_ref_fields校验原schema/状态/ref，再独立核真实I/D/latest Binding/token/权限子集/workers空/专业manifest/准确发布对象。没有修改gate、伪造controller receipt或声称完整CLI门禁通过。本C具体结果以RETURN_VALIDATION.json为准。

专业产物先推指定记录分支，再远端按新commit逐字读取核心文件；Return后独立提交/推送并读回。只改本Run的professional/D011和calls/C0025，不改manager进度或签后继D。C0025 invocation_token仅做原件一致性校验，不进入专业报告。
''')
write('LOCAL_CHECK_REPAIRS.json',{'attempts':[{'attempt':1,'result':'FAILED','scope':'定义检查器selected表头','cause':'UTF-8 BOM保留在csv.DictReader的symbol列名','repair':'utf-8-sig，reader同样明确编码','evidence':'attempts/01-*','C2_or_B_changed':False},{'attempt':2,'result':'PASS','checks':len(CHECK['checks']),'evidence':'DEFINITION_CHECKS.json/DEFINITION_CHECKS.log'}]})
print('Native D output and integration records generated; status=完整; no E execution.')
