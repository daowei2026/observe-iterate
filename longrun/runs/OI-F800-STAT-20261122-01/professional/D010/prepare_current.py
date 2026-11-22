from pathlib import Path
import hashlib
import json

R=Path(__file__).resolve().parent
def save(n,v):(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
PRO='daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/OI-F800-STAT-20261122-01/professional/D008/'
browser=json.loads((R/'BROWSER_v4.json').read_text())
checks=json.loads((R/'CODE_VALIDATION.json').read_text())
assert checks['status']=='PASS' and not browser['console'] and not browser['external_requests']
panels=[
 dict(面板编号='P-PRICE-{symbol}',角色='输入/原价主图',信息=['C1-01','C1-02','C1-03'],时间轴='同一交易日历UTI；实际/几何确认取已确认各字段',纵轴='各品种独立原价，不标准化',顺序=1,布局类='PerSymFigs',图元=['KPriceLine','Rct实际点','Selected T/C及同记录T→C段']),
 dict(面板编号='P-INPUT-KNOWN',角色='前部输入附图',信息=['C1-03'],时间轴='ScaleTurn原事件已知轴；不由几何确认推断',纵轴='symbol序号+0.15×round；仅显示派生',顺序=2,布局类='AllSymsFig.persym_plots',图元=['MulFieldsGlyphs x marker；原值hover']),
 dict(面板编号='P-OUTPUT',角色='业务主输出附图',信息=['C1-04','C1-06','C1-07'],时间轴='groupKnownFrom稀疏发布；a/d/r为同一修订携带的界限',纵轴='稳定修订显示序号，不编码状态',顺序=3,布局类='AllSymsFig.sym_plots（仅提供合法上下文，全局数据不按首品种过滤）',图元=['MulFieldsGlyphs exact发布点','MulSegPlot a→d/d→r；只裁剪显示']),
 dict(面板编号='P-EXACT-DETAIL',角色='身份/独立状态及原值明细',信息=['C1-04','C1-05','C1-06','C1-07','C1-08','C1-09','C1-10'],时间轴='跟随所选exact修订，不另定义时间轴',纵轴='无',顺序=4,布局类='既有Bokeh Select/DataTable/Div与原生CDS组合',图元=['Life/Revision/完整父坐标','独立basis/observation/coverage/closed/duty列','全部已发行子表/非组根metadata原值JSON文字'])]
glyphs=[
 dict(图元编号='G-K',来源信息='C1-01',横纵轴='开闭UTI/原始OHLC',视觉语义='原价K线',hover图例='OHLC/volume/ts；图例可显隐',显示派生='无标准化/补NaN'),
 dict(图元编号='G-TC',来源信息=['C1-02','C1-03'],横纵轴='Rct/Selected实际及C几何位置；各原始价',视觉语义='Rct灰x、T蓝圆、C紫菱形、T→C同记录连接',hover图例='原值JSON/turn/round/P/T/C/上游事件等实际注入内容',显示派生='必要时只对段显示端点裁剪，不改原坐标；历史位置投影非as-of回放'),
 dict(图元编号='G-SELECTED-KNOWN',来源信息='C1-03',横纵轴='上游known；symbol+round显示偏移',视觉语义='输入被选已知点，不用价格重放',hover图例='同一上游记录完整原值，round/turn可追溯',显示派生='symbol序号+0.15×round，原值在hover'),
 dict(图元编号='G-REVISION',来源信息=['C1-04','C1-06'],横纵轴='groupKnownFrom；唯一修订显示行',视觉语义='每个完整父坐标一个稀疏点，不连成状态线',hover图例='Life/Revision/父键/known/basis/observation/coverage/formationClosed/dutyClosed[]/admission[]/a,d,r',显示派生='按known及完整父坐标排序，绝不按UUID排序；同刻不平移时间、不合并'),
 dict(图元编号='G-WINDOW',来源信息='C1-07',横纵轴='同修订a→d与d→r；同修订行',视觉语义='当前观点携带的窗口，不代表持续材料/状态',hover图例='全局无品种前缀；原始及original窗口字段、裁剪标记在exact明细',显示派生='只裁剪视区，原始端点不变；不得从几何线段推导coverage区间'),
 dict(图元编号='G-DETAIL',来源信息=['C1-05','C1-08','C1-09','C1-10'],横纵轴='无',视觉语义='精确引用/全部公开子行原值，空列表原样',hover图例='图点/表/下拉共用同一source，保留所有child层级；关系target的原始exact编码可追溯',显示派生='主UUID只解码表示；原始64位数嵌入JSON文本，不用JS数值解析')]
save('C2_CURRENT_EXPECTATION.json',{'当前预期编号版本':'F800-C2-v4','FeatureUnderstandingPackage引用':PRO+'CurrentFeatureUnderstandingPackage.json','理解状态':'PARTIAL（原状态保持）',
 '页面与阅读路径':'各品种原价及实际/确认输入→上游已知轴→跨品种候选exact修订及携带界限→独立状态与全部公开原值明细。',
 '面板定义':panels,'图元定义':glyphs,
 '基准转换和交互':{'原价':'逐品种独立价格轴，std_method=None，所有其他dynstd_method=False。',
    '时间':'同一PlotCtx共享x_range；UTI按注入SOF/calendar标成时间。原事件timestamp与payload位置分别保留。',
    '显示派生':'修订序号、输入symbol/round偏移和线段裁剪；均不改业务字段，原值明细保持。',
    '交互':['缩放/平移/重置','图例显隐','每图十字线','原值hover','点/表/下拉共用exact选择，明细显示完整父子坐标'],
    '损失':'未提供全局有向关系拓扑或自动跨多源高亮；精确成员/Previous/Required/替代覆盖/Bridge保留在原值明细，损失一眼连线浏览便利，不损失已发行字段/身份。'},
 '当前原型代码引用':['preview.py','current_impl.py','archive/current_impl_v4.py'],
 '当前预期HTML引用':'html/current.html','唯一当前HTML':True,'当前HTML_SHA256':sha('html/current.html'),
 '首版档案':'html/first.html + C2_FIRST_EXPECTATION.json；archive/round1.html/round2.html仅为迭代证据，不是另一个最终预期。',
 '样例预览绑定':'PREVIEW_BINDING_v4.json；6条修订、所有业务值/身份合成。SOF只提供交易日历。',
 '当前允许变化':['D正式绑定B品种/时间/位置或每个多尺度位置','正式外层instance、reader/context/SOF与字段映射','真实曲线、点数、坐标范围与字段值/现有原值列','依据实际输入的图宽/时间标签频率'],
 '当前必须保持':['C1选中信息及NOT_EXPOSED边界','逐品种原价/输入已知轴/主输出/精确明细阅读路径','不以actual/几何confirm替代发布known或上游selected known','独立状态各列，不从closed/Subsumed推断退出活跃','同刻观点完整父键与每层child坐标，不按known单独合并','只画稀疏发布与明确标识的携带窗口，不伪造逐tick轨迹','原值/显示派生/裁剪明确分离，精确ID无损'],
 '实际核看证据':['BROWSER_v4.json','screenshots/current.png','screenshots/current-selected.png'],
 '当前已接受':'当前范围可接受；未解决工具能力缺口为空，原理解/数据不可暴露限制继续传递。'})

reviews=json.loads((R/'C2C_FIRST_REVIEW.json').read_text())['items']
rounds=[]
for item in reviews:
 i=item['复杂点编号']
 evidence={'CP01':'utlv2.py:1244–1441原生点；utkv2.py共享x_range；显示行保持不同父键',
           'CP02':'MulSegPlot:854–1000、原U ST1–ST4/J5；只携带界限和独立原值',
           'CP03':'PerSymFigs/AllSymsFig、MulFieldsGlyphs/MulSegPlot；各位置分别绑已确认字段',
           'CP04':'pfw.py默认hover/PlotDataNode；既有Bokeh HoverTool/DataTable/Select/Div及CustomJS组合',
           'CP05':'PlotCtx时间范围、live_feat_data/uti_slice；预先显示裁剪并保留raw'}[i]
 rounds.append(dict(复杂点编号=i,要保留的业务信息=item['要保留的业务信息'],当前HTML中的问题=item['当前HTML中的问题'],轮次=1,
    候选展示表达=item['候选表达'],已核实的CAEGraph能力=evidence,判断类型='使用方式问题／换表达可实现',本轮决定='采用并同步v2原型/预期/HTML',
    语义损失='无原值/身份损失；关系用明细替代全图连线，损失浏览便利。' if i=='CP04' else '不丢原字段；显示行/偏移/裁剪均明示。',
    展示预期修订='见当前面板与图元定义',HTML更新引用='archive/round1.html',原型代码更新引用='archive/current_impl_v2.py',
    实际查看='BROWSER_v2.json + screenshots/round1-selected.png',当前状态=('第一轮表达已落实，图例/精确身份/选择继续后续轮次' if i=='CP04' else '已解决；v4再次核看保持')))
rounds.append(dict(复杂点编号='CP04',要保留的业务信息='全局归属、精确身份与控件所选修订一致',当前HTML中的问题='v2输出图例带rb上下文前缀；原生主组身份可为UUID high/low，不能假设idText必有值；表格reorderable有jQuery依赖提示。',
  轮次=2,候选展示表达='去上下文品种前缀；无损UUID表示解码、原字段全保留；表格不用列重排。',已核实的CAEGraph能力='原生图例对象及Bokeh 3.6 LegendItem/StringSpec、DataTable既有属性；D008已接受的exact编码形状。',
  判断类型='使用方式问题',本轮决定='同步v3；浏览器发现图例裸字符串被当字段名，不能接受，进入下一轮。',语义损失='未接受错误版本；原始身份始终保留。',
  展示预期修订='仅全局图例/身份表示/原值保留',HTML更新引用='archive/round2.html',原型代码更新引用='当轮current_impl.py已同步生成v3；未保留独立v3源快照，保留round2 HTML、浏览器与截图；当前v4源快照另存',实际查看='BROWSER_v3.json + screenshots/round2-selected.png（3条Invalid field错误）',当前状态='继续处理'))
rounds.append(dict(复杂点编号='CP04',要保留的业务信息='全局图例正常且选择状态一致',当前HTML中的问题='v3图例显示Invalid field；v2/v3图点选择时下拉未同步。',轮次=3,
  候选展示表达='按Bokeh自身legend_label实现使用literal value；选择回调双向同步并阻止重复回写。',
  已核实的CAEGraph能力='本机Bokeh 3.6 plotting/_legends.py:113–122；bokeh-widgets.js SelectView（DOM option以label显示/映射模型value）；均为既有使用API。',
  判断类型='使用方式问题',本轮决定='采用v4并实际重开核看；0 console/0外部请求，真实下拉操作选择第3行，图点与明细保留SYN-Life-B/SYN-B-r1。',
  语义损失='无；不新增uplot工具。',展示预期修订='全局图例文字与选择同步，其余v2结构保持。',HTML更新引用='html/current.html',原型代码更新引用='archive/current_impl_v4.py',实际查看='BROWSER_v4.json + screenshots/current-selected.png',当前状态='已解决'))
save('C2_COMPLEX_POINT_ROUNDS.json',{'各轮记录':rounds,'当前预期':'F800-C2-v4','当前HTML':'html/current.html','真实新增工具能力缺口':[],'未伪造的原输入限制':['PARTIAL U','逐tick准入/失败组合/first blocker/原生coverage区间NOT_EXPOSED'],'循环停止理由':'当前选定表达保留C1已确认且可用的业务信息，真实预览/交互与代码级合同检查通过。'})
save('CAEGRAPH_CAPABILITY_GAPS.json',{'真实未解决工具能力缺口':[],'已经排除的使用问题':['跨品种list在无symbol附图的currTarget限制，用既有AllSymsFig上下文组合解决，未改工具。','默认hover缺身份，以已存在CDS/HoverTool/明细组件组合保留。','同刻同basis重叠，以显示行保留多个exact记录，不改时间。','不采用无可运行例的OneToGroupPointPlot凭空承诺。'],
 '非工具缺口':['输入U为PARTIAL，未暴露内部轨迹不在C补造。','当前采用明细表达exact关系；未承诺全图拓扑或自动跨来源高亮。'], 'uplot_repository_changed':False,'new_uplot_API_added':False})
save('C3_CODE_RESULT.json',{'代码编号版本':'F800-C3-v1','Python代码引用':'display_code/caegraph_display.py','对应C2当前预期版本':'F800-C2-v4','代码来源':'archive/current_impl_v4.py逐字整理为C3；current_impl.py重导出同一实现，未生成第二份HTML。',
 '实例位置字段注入合同':'INJECTION_CONTRACT.json','字段模板':'FIELD_MAP_TEMPLATE.json','预览实例绑定':'PREVIEW_BINDING_v4.json',
 '是否固化外层实例':'否','是否固化B最终位置':'否','CAEGraph类映射':{'入口':'CAEGraph/PlotSet','原价':'PerSymFigs/KPriceLine','输入':'AllSymsFig/MulFieldsGlyphs/MulSegPlot','输出':'AllSymsFig/MulFieldsGlyphs/MulSegPlot','原值交互':'原生PlotDataNode/CDS+底层既有Bokeh组件组合'},
 '与C2当前HTML核对':'同一实现文件字节一致；同一页面/面板/图元/语义。C3检查只建内存样例模型，不另生成预期HTML。',
 '代码级检查':'CODE_VALIDATION.json','代码SHA256':sha('display_code/caegraph_display.py'),'检查数':checks['check_count']})
save('CAEGraphDisplayPreparationResult.json',{'FeatureUnderstandingPackage引用':PRO+'CurrentFeatureUnderstandingPackage.json','外层实例引用':PRO+'FeatureRunResultBinding.json','输入理解状态':'PARTIAL（没有升级）',
 'C1待展示信息清单':'C1_INFORMATION_LIST.json','C2A阅读能力核实':'C2A_MANUAL_READING.json','C2第一版展示预期':'C2_FIRST_EXPECTATION.json','C2第一版HTML':'html/first.html',
 'C2当前展示预期':'C2_CURRENT_EXPECTATION.json','C2当前预期HTML':'html/current.html','唯一当前预期HTML':True,'C2复杂点处理记录':'C2_COMPLEX_POINT_ROUNDS.json',
 'C3可注入展示代码':'display_code/caegraph_display.py','实例位置字段注入合同':'INJECTION_CONTRACT.json','能力缺口':'CAEGRAPH_CAPABILITY_GAPS.json','未解决工具能力缺口':[],
 '阶段状态':'完整','本阶段未完成项':[],'后继':'原manager消费C后再按原流程签D正式集成、E核图/正式取数及适用S1/S2。',
 '未代签':['D完整定义','E最终图/正式数据','ObservationMaterialPackage DATA_READY','正式场景案例/冻结预期','FeatureReleaseGate/ReleasePackage'],
 '保留边界':['当前有效X/G/B不重做','原四问题/七candidate-only来源保持','Q共享影响及独立数值边界保留','F-only，不运行/释放Q/V、不改WALL M001','无Worker/新线程/其他聊天消息']})
print('C2当前预期/真实迭代及C3原生结果完整，检查数',checks['check_count'])
