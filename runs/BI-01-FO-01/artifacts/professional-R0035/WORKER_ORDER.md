# BI01-FO01-N-BOUNDED-DISPLAY-09｜有限共用展示增量实施、真实验证及具名工作3接入

work_id: BI-01  
run_id: BI-01-FO-01  
order_id: BI01-FO01-N-BOUNDED-DISPLAY-09  
issuer_role: professional  
issuer_ref: chatgpt:细节叙事生成_金标:BI01-FO01-执行  
issuer_invocation_id: BI01-FO-01-R0035-20261024T185441Z-1c7e5a8c  
issuer_assignment_token: BI01-FO-01-N-BOUNDED-IMPLEMENTATION-0e1a689f4af8442eaac021673425cef9  
return_to: chatgpt:细节叙事生成_金标:BI01-FO01-执行

<a id="authority"></a>
## 1. 真实授权与完整目标

依据[当前完整任务@78cc9a81](https://github.com/daowei2026/observe-iterate/blob/78cc9a813777b9996d365f8242fc6ca318066972/runs/BI-01-FO-01/01_当前任务.md)、[M34完整采用及签发@397a4da5](https://github.com/daowei2026/observe-iterate/blob/397a4da5f88ca6f455a033c27ffb2b4ac82f12e5/runs/BI-01-FO-01/reviews/management-R0034/FULL_RESPONSE.md)，由原执行Pro签发本单。完整专业依据为[P32@16e14ad0](https://github.com/daowei2026/observe-iterate/blob/16e14ad08f5c283c6c045d532411c583307d4604/runs/BI-01-FO-01/artifacts/professional-R0032/FULL_RESPONSE.md)，特别D—I；先取得正文，不能用本单或管理摘要替代。

**这是一张实际实施/验证单，不是再次调查方案是否应当开始。**在aidata自己的新独立分支/工作树中，将既有独立配置、共用解析和Uplot组合补成当前N切面所需的有限能力，并使真实Notebook与正常页面消费者调用同一路径。交实际代码、配置、测试/恢复、真实新Notebook及交互；在真实采用和原权限满足时继续具名正常平台与同节点正式数据。结果先回本签单Pro，由Pro消费后交管理接收。

整单覆盖配置→读取/准备→解析/恢复→共用组合→Notebook/正常页面→正式切片/图引用的直接依赖。普通工程错误在单内连续修通，不逐字段、文件或TypeError请管理重批；不以rb首张图、一个纯函数测试或提交一个helper作为完成点。M34并行协调公共采用责任，未授权共享写入只限制该操作，不能冻结独立分支主体。

不实施独立N CAE、返回任意整页layout的伪通用provider、任意import/回调执行器、完整场景语言或全多面板工作台；不恢复W04—W08或R30旧载荷。正式工作4不在本单，技术PASS不放行观察或代替专业/管理认可。

<a id="inputs"></a>
## 2. 固定起点、来源和第一批范围

### 2.1 使用版本和真实现场

- 工作2实现基线：`daowei2026/aidata@8a08300cb70a610401424bedadb42e9dcde13e71`。先读README，再读DEVELOPMENT_GUIDE的独立配置/输入合同完整适用节、RUN_BRIEF_INPUT_CONTRACT及实际相连实现。
- W07已有接入：`daowei2026/aidata@cbd0a1f9bf92d9d65e0ad00bfd1a9e3afb7c2cf0`。保留其中正确选择/读回、冻结范围、正式依赖和时间修正；撤下本单指定的共享N默认键与特有整页路径。cbd是既有代码，不是整包应上线的许可。
- 场景与实际代码：`observe-iterate@351d88cf6d669b32bb245882494769cc9d14f42b:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-W05-SCOPE-READABILITY-06/`的DISPLAY_PLAN.json、N_observation_Worker06.ipynb、notebook_source/W06_executed/NOTEBOOK_SOURCE.md及已有准确索引。场景0.3.2-worker06，实际配置是aidata8a的0.2.4-worker06；PLAN的e8aaa464仅参考基线。原Notebook blob58f7b27b37bc2db9582a9b24460f6f3e62a6bf41、执行e333；不把旧执行输出复制成此次新执行。
- 上游认可：M21 `7aaefeb5d80c0b2e4460bf03a4723a252567fea5:.../reviews/management-R0021/FULL_RESPONSE.md#accepted-work2`及P20 `00608f7df6eac8ee44e04f08a8ddbcd699abc08c:.../artifacts/professional-R0020/FULL_RESPONSE.md`。这里及下文省略号均为`runs/BI-01-FO-01`，不是另一个路径。
- 正式数据原件：W02 `081e31241a0c88e47631f80a8b9b8dd43b2b569c:.../artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/`；W03 `d04f3b08892ccf334a06028f3caab994743566a0:.../artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/`。先复用W07已核缓存/原件引用，不重新整批取数。
- 已冻结平台/board材料：W07 `9aa0fe91e4c37a4d983ebd62aea0b5c45755206a:.../artifacts/worker-BI01-FO01-N-PLATFORM-BOARD-07/`的SOURCES、API_RESULTS、PERSISTED_CAE_READBACK和board_delivery；P25 `617958eb11c1096f437e5b54cae92281860b346b:.../artifacts/professional-R0025/FULL_RESPONSE.md`已完成该数据的具名专业消费。不要重做整包消费充进度。
- 已证兼容边界：W08 `b3d9dbf50d53596162d14174cdb1c0ed5d1fa603:.../artifacts/worker-BI01-FO01-N-CONSUMER-CONTRACT-08/`。普通默认N空键进入fason、ppid变化、活动Trier原16键及加载顺序反例直接沿用，仅验证本次最终候选，不重跑整批调查。
- uplot手册参考`0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`；实际运行版本/文件和已有dirty单独记录，不能拿手册SHA代运行身份。

历史现场目录为`/dwdhome/fy/BASE_E6_2/mquant`，W07工作树`aidata-bi01-fo01-n-platform-board-r0022`，观察仓`/dwdhome/fy/observe-iterate-bi01-fo-01`，run根在该仓`artifacts/bi01-worker07-runs/`。它们只是准确历史定位，执行者须核实际存在/权限、解释器、导入文件和有影响的工作树差异。先在aidata建立本单独立分支再改，不在共享默认工作树直接施工，不清理/覆盖他人dirty。分支名和实际HEAD由执行结果记录，本单不伪造已建分支。

### 2.2 第一批具名对象及不能改变的读法

三个原aidata run前缀为`BI01-FO01-W07-20261024T0028-`。

|run/node；旧CAE|正式知识身份|原价与显示范围|必须保持的效果|
|---|---|---|---|
|rb/big_000001；6128|K103315800；Node b340dc6c-c135-462b-b6e0-04d24622c180；revision cfd51328-e2cf-4360-8314-20c9238e93fb；binding1/window37926/working37943|100443000..103315800，完整已供4789行|两完成窗与当前前缀分开，actual端点和确认位置分开，原5m路径/行情不替换成默认30m|
|rb/big_000002；6129|与上行同K及正式对象|显示103140000..103315800，294行；原价关联仍用完整4789行|切换视口不换成员、不重算统计；视域省略不当源缺价；不是另一个独立市场样本|
|i/big_000001；6130|K35361000；Node9410abda-b111-442d-aa25-6b99da2afeb6；revision1d82177d-6e82-44fd-b4b8-8cb899a94e28；working Life5727e951-20b6-4a82-8c52-fc3a32f686cc|35339400..35361000，37行、24条close缺值|12推进、42000年龄、waiting0与缺路径/效率/比值分母分开；真零不消失，缺量不填0，原价缺口不连补|
|hc/big_000001；6131|K103315800；Node6f92034c-bd94-4d3f-8b7c-6c69e24959ff；revision76d5cfc3-f505-4b62-89b8-b081aedb90f0；binding3477/window37914/working37915|103044000..103315800，454行|45/97价差与258000/600时间量、430比值分轴；close3952、下一根close3946/high3959、末拍3904的真实字段/时间注记保持|

表中数值是已核历史输入/验收对照，不是本单新市场结论或生产期望常量。实际比较回到原字段、kind、地址及状态，不能硬编码这些数字使测试通过。i与rb/hc非同期，不跨品种按原价排名。

生产实例、N参数/方法/正式输出不改；6＋6不是固定日数，working不是完整样本，CalendarUTITick不叫秒/bar，430不是概率。原TIS/FRP正常读者及精确源版本按当前任务保留。需真正补读才正常OnlyRead并保持完整sources；to_df拒绝不构成改产品或重算N理由。

<a id="display-decisions"></a>
## 3. 由Pro明确的本次画法与实现边界

本单首先机械保真重承载已认可含义，不让Worker重新选业务信息。各品种颜色沿W06稳定配色，完成/未完成、系列性质用原线型/形状/面板区别。没有新需求不画MAD、全部六项中间指标或LOO排名。

保留原5m OHLC及close路径的价格主图、已知成员actual端点/确认标记、完成窗效率、working净推进/逆向量及working效率读数。沿W06的rhythm与waiting_time选择；i另保留duration，以使整体年龄与局部等待不混同。下列对应是把现有具体图层接入共用能力的实施要求，不是另造一个生产指标：

|原图层/信息|面板/坐标意义|横轴与状态|
|---|---|---|
|close_path、selected_*边界/端点/confirmation、具名close/high参考点|原价格水平；与同源K线同坐标，不归一化|绑定Calendar实际位置；确认使用自身确认时价；缺端点价不补造，范围外省略和源缺分开|
|completed_recent_updates / completed_previous_updates|已完成两窗效率，ratio原值|x=K，仅一切点；不让长价窗挤成右端不可读点；原basis保存时间另保留|
|working_progress_points / working_counter_points|沿原方向净推进、累计最大逆向量，price差值而非价格水平|x=K；不套价格平移标准化、不与约3800的价格水平共轴；零值和负推进合法|
|working_efficiency_points|当前未完成前缀效率，非已完成样本|x=K；无数值保留原原因，不用空白暗示零/未发生|
|waiting_ratio_points|局部等待倍数，ratio|x=K；可超过1，430不能截成概率；缺分母和局部真零区别|
|working_waiting_points / interval_median_points|CalendarUTITick原值|x=K；正式分母从原rhythm/intervals取得，不由比值倒算|
|i的working_duration_points及原选定duration视图|当前过程年龄与相应时长，CalendarUTITick|x=K；整体过程起点不被局部恢复时点替代，不能把42000误读为恢复后等待|

单K数轴的留白、网格列宽、文字安放属于机械布局，可按现有已测形式实现；留白不添加K后数据，pan/zoom/reset不得压成退化y范围。HC先在已认可2300×1400、DPR1及1800px图宽/两侧栏状态核新消费者，不把任意窄屏适配扩成任务。所有值/状态应在正常视口能理解，不靠长表遮盖图形失职。

W06还含其他K选择和稀疏比较代码；代码存在不扩大M21认可。此次Notebook保留已有准确代码谱系和必要交互，但平台初批只使用上表范围。保留或验证其他选择时分别标未获用途认可，三点不补保持线。新组合器不生成时序、插值、事件或修订；领域准备器仅按真实发生给合法点/有界区间。

改变必要信息、量纲、actual/confirmation、缺失含义、实质交互或适用范围时，先把具体影响与建议交Pro，由管理处理受影响用途；纯机械重承载在本单连续修通，不另设四阶段或每幅图的固定批准门。

<a id="implementation"></a>
## 4. 贯通真实生产者和消费者

### 4.1 有限opt-in声明及正常保存恢复

保持原简单配置的point/line/segment、group标签和原Feature接口。为确需扩展的配置明确面板引用、坐标/变换、行情窗或单K作用域、数值外状态及源角色；未知能力、悬空/冲突面板、语义不相容的轴不得静默降级。不能仅因unit相同就把price水平和价差并轴，也不能把所有旧group自动变成SubFig。

贯通`normalize_evidence_features`、`normalize_anchor`/plot、`resolve_run_evidence`、registry/anchor_registry及实际缓存/持久索引，避免新字段只在源配置中存在。具体字段名、内部函数拆分由实现确定，交付实际定义和调用；本单不把未实现的schema伪称现有API。优先沿原`evidence_features`和明确的run配置关系恢复新opt-in，不给普通共享类新增默认N空键或另一个全局空占位。

先以正常Fao构造/序列化/恢复核具体可行结构，再贯通真实渲染，普通调用原16键/fason/ppid不变。若确切嵌套合同不能承载，给最小输入、异常、实际消费者和最小有版本建议；普通编码/参数问题先自主修通，承重合同不可满足才回Pro/管理。不得自动转独立CAE或修改框架忽略未知键。

选择身份保留生产N、symbol、Life/K/exact、视图/配置版本和必要可选信息，原source缓存可以共享；已经裁过显示范围的投影/图元不能在rb full/local之间错误复用。同价窗的不同K也不能串值。改变视口不改原查询成员/正式数值，不能为防缓存问题无差别重复读全原表。

### 4.2 N领域准备与共用组合真正分开

继续使用正常N读者或准确缓存选K、解引用、保留原状态、行情和既有显示投影；原UInt64身份不得转float，spec按kind而非列表位置关联。保留`normal_node_behavior.py`中正确原件校验、固定选择、bundle_for_node及正式依赖职责；不要整模块删除。

从原`build_uplot_layout`及配置中提取机械MainFig/SubFig/PlotSet、轴范围、图例/状态文字布局为实际共用组合入口。它只消费已提供的视图、声明和解释，不出现N窗口地址、knownness枚举判义或生产公式。N准备器不返回一整页任意layout；原N Notebook入口应改为调用同一共用组合，不平行维护旧机械实现或换名藏入helper。

`evidence_plot.py`的原值hover、坐标别名、图元样式及正常读取尽量复用。原价格叠加继续原变换；显式ratio/CalendarUTITick/价差路径不得无条件dynstd/fit到价格轴。空DataFrame不能直接吞掉已提供的缺失说明，不能用假数值行或填0制造可画点。状态原因由N解释，通用层只安放和显示。

### 4.3 单一选择区分正式源与图用投影

一份观察选择应能展开原正式证据、显示视图及它们的关系，不让人另写一份易失配的展示清单。原生Feature/df_key/view_id合同保持；N的`n_display/*`明确为显示投影，不能因为包装成Feature就在`feature_slicer`、`feature_slices/`、正式delivery中冒充正式N。

实际将源角色贯通解析结果、索引、slicer及交付：显示数值保留可追原件的映射，只供核图；board主证据仍取原正常表、原时间和必要较早基础，不能简单跳过display后把N正式来源一并丢掉。P25已核i节点外window、rb较早binding、hc原间隔等依赖必须仍可取得。源选择说明可以复用W07原件，不把显示迁移做成全量重导或第二套引用平台。

### 4.4 真实公共入口及旧机制退出

必须改接`build_big_world_chart_pages`、其参数生产者/恢复、`AidataBigWorldReviewCAE.layout`及本次实际使用的`render_review_nodes`/render_bridge等消费者。Notebook、隔离正常页面layout和后续共享平台使用同一解析/组合能力；增加新函数但公开入口仍调用旧N整页分支不算完成。

在本单aidata分支中，从普通类声明删除全局`normal_node_behavior_manifest`及其无N空键注入和N整页提前返回；追直接调用/专属测试，移除只为被替换路径存在的职责。正确N选择/源读取/原表补充可以继续被领域准备调用；普通16键、fixed_input和无扩展配置正常路径不动。旧共享部署、旧DAO及历史代码提交不修改。

旧服务可能拒绝也可能忽略新语义，保持16键并非无发布要求。不得在尚不具能力的真实服务上生成/宣布可用链接以试图“让页面自己加载新代码”。本单隔离正常恢复/layout可不写DAO验证；真实共享采用按第6节，不以新进程成功代替活动服务。

<a id="verification"></a>
## 5. 实施中的必要验证及实物

验证与修通连着做，不按以下条目机械拆工单，也不以测试数量定义完成。

**普通配置及普通持久合同。**使用既有ScaleTurn点/线、BlkThick同表dense/fight准确小夹具，核view展开/显式选择、缓存共享、原值hover、图元样式和不同切片身份；不生产第二个复杂特征。对最终候选相同安全输入做真实普通16键、fason/ppid及正常恢复对照。无扩展配置不被强迫增加新字段，fixed_input等旧合法路径不被误删。

**扩展声明的端到端与反例。**真实新opt-in经过配置→解析→索引/保存→冷进程正常恢复→共用layout；核声明未丢失、消费者确实选择新能力。未知能力、悬空面板、冲突坐标、错误源角色应明确失败；普通K/缓存对照可复用已有准确切点，不造新市场样本。若固定选择或权限不合法，在数据/DAO写入前失败，而不是先写再改。

**真实N保真。**使用第2—3节原件与所选范围，检查原字段→显示视图→实际图层的相连一致，rb full→local→full前后统计/身份不变，i真零与各缺项、hc正式分母与close/high分工保持；检查最终坐标轴及必要交互后的范围，不能只打印初始配置。已有其他K只作具名回归/工作2准备，不扩平台认可。缺价不补、选K后不泄漏未来、同bar close不改实时知识资格。

**实际新Notebook及交互。**交运行完成的`.ipynb`、实际配置和打开方法，记录真实kernel/解释器、导入路径/有效源码与执行标识；Notebook以正常Uplot显示新组合结果，不嵌旧HTML/PNG。实际操作rb范围切换及适用选择器、hover/图例、平移缩放复位，定向核HC已认可视口和i空态可读性。记录操作人/实际结果/范围，技术验核不替Pro判断。HTML仅辅助，PNG不是主交付或逐Case要求，GitHub可预览不冒称JS可交互。

**实际三入口及同节点图数。**原chart core可有据复用，不重定位；正常页面factory的隔离恢复及版本准备先完成，真实平台调用依第6节权限。`build_board_run`在同run/node复用原正式切片/依赖并按实际需要更新图引用，不机械重跑三遍/全量导出。保留配置版本、正式源/显示作用域、目标图层与对应数据。最终只有真正打开目标图层和必要交互的正常report_url才可称工作3图完成；HTTP200、DAO id、代码PASS均不足。

**完整回交，不扩大到全仓验收。**给实际候选commit/分支及相连文件、采用的配置合同/正常调用、测试命令和结果/失败、已执行Notebook与数据入口、所核图层/交互、真实平台与board对应或具体阻断。新调用所需的重要依赖一并修通，禁止为显得完整清理无关历史/全console/全环境。判断没有实际发生的事项明确写未执行。

<a id="platform"></a>
## 6. 共享采用、正常注册与旧视图保护

M34已在`#platform-adoption-request`承担共享采用/权限协调，当前没有新增共享发布授权事实。本单不授权切换共享checkout、重启或注入Trier/Bokeh、改认证、修改TIS/FRP/workerADT/core/SDK/uplot，亦不预设活动进程已经采用候选。现场工具能操作不等于原权限成立。

独立分支、隔离正常恢复/layout、新Notebook及正式数据核验先连续完成。实际候选足够清楚时，尽早回交确切commit、所需正常加载/读取权限、已证兼容与剩余，供原Pro消费并交管理协调；其他合法部分继续，不等部署回复才开始代码，不空回“请部署”而无候选。

真实采用后、由具备原权限者才可进行该配置的正常注册/图引用更新。沿用原三run/四frozen node，不预填新id，不擅改全局DAO。尤其核`createUniqueWithFao`的创建/复用和`_refresh_created_node_params`的实际写回：在任何更新前拒绝覆盖6128—6131的原类/17键参数及原失败记录；不能删除旧字段假称原页修好。若正常注册命中受保护旧id或不能保证原记录不变，停止该次写入并交准确冲突与正常区分建议，不能先写后补证，也不能无限重试堆新节点。

允许的图引用新版本来自M34#view-policy，不是R30独立CAE迁移授权。原packet/提交保留；新页实际打开目标图层后才更新当前可用引用，记录同run/node/K/exact/配置/consumer及旧页关系。纯图引用改变不重算N；旧URL是否可用照实保留，注册成功但页面失败仍不通过。

原日志事件的敏感值不复述、不提交Git。日志只输出白名单安全字段，原认证处置交原责任者私下处理，不顺带扩成安全工程或推定全数据无效。

<a id="delivery"></a>
## 7. 回交位置、真实停止条件及接续

工程成果在aidata自己的实际独立分支；技术及图数实物定位回：
`runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-BOUNDED-DISPLAY-09/`。

完整报告说明代码/配置、运行及证据资格，交实际新Notebook、必要验证和准确源/图引用；原包只引用，不重传整个W06/W07/W08。可以按实际实物组织文件，不规定文件或图数，不增加公共控制表；回交的机器格式沿本run原Worker协议，不自创调度协议。

**回交给原签单Pro，不直接让管理代接技术结果。**原Pro核实际实现、数据、画法与新消费者，对具体工程缺件沿本单返修；成果达到具名可靠范围即交管理接收，不等EFFORT。管理需要另外的限定现场核验时另签自己的单，不由本单自签独立通过。

真实共享权限缺失时交候选和已完成的全部合法实物、准确受限操作/责任/恢复条件；这不取消其余未完，也不是以一个局部测试完成主动停止。真正业务/合同不可满足或需受保护变更时给证据和建议回Pro/管理，不自行改目标。正式工作4、交易结论、参数最优或整项BI-01完成不在本单授权。

签发事实：**本单已由原Pro签发；本次没有派达、接单、执行、创建aidata分支或共享采用的事实。**后续状态以真实机制和执行记录为准，不把文档发布当已运行。
