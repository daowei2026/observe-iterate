# BI01-FO01-N-UPLOT-NOTEBOOK-PLATFORM-04｜新Uplot Notebook画通与正常平台同节点交付

work_id: BI-01  
run_id: BI-01-FO-01  
order_id: BI01-FO01-N-UPLOT-NOTEBOOK-PLATFORM-04  
issuer_role: professional  
issuer_ref: chatgpt:细节叙事生成_金标:BI01-FO01-执行  
issuer_invocation_id: BI01-FO-01-R0011-20261022T145041Z-c822c94f  
issuer_assignment_token: BI01-FO-01-N-NOTEBOOK-PLATFORM-7597f171450b4ee0bb69391af4e0a637

<a id="authority"></a>
## 1. 当前权力与任务

本单由上述执行Pro实际签发，供既有合法人工委派渠道交具有现场访问能力的Worker，真实结果返回原执行Pro。当前Task/Binding为 `observe-iterate@4123b6b0d5f53e38029bca56b6ab9fa1dc4afa17:runs/BI-01-FO-01/01_当前任务.md#technical-work`，管理R10采用 `fdbe0efd58cd11d40ebadaa4e2e58f5571c0f527:reviews/management-R0010/FULL_RESPONSE.md`（完整路径在本run下），方法5470e43d的README/00/01/02/04/BOUNDARY_UPDATE及原03，Owner完整纠正698b229。

原Worker02及03已经结束。本单不重复旧载荷、不恢复旧在途；不恢复Owner暂停的Root Goal、计时器、自动任务、常驻轮询。发布不等于派达或执行。只处理同一具名N完整观察内已经明确的技术责任，不扩成完整U2/U3、收益预测或资金动作。

**工作2由原Pro负责真实新画法及其判断，本单承担受委派现场执行；工作3消费适用的新画法完成平台/正式数据衔接。**不得再把Notebook画通推给工作3，或用技术PASS代替Pro接受。两者相连且可往返；平台必要入口事实可先核，一项适用画法画通即可用于工作3，不等全部Case、品种或图数齐备。

<a id="inputs"></a>
## 2. 已有真实资料与候选实物

本轮目录 `runs/BI-01-FO-01/artifacts/professional-R0011/` 的 FULL_RESPONSE.md、DISPLAY_PLAN.json、N_observation_R0011.ipynb、verify_r0011.py、CHECK_RESULTS.json 为本单专业输入，准确提交取本轮最终RETURNS的artifact_refs，不从聊天摘要重造。场景配置版本 `0.3.0-r0011-candidate`，不冒称aidata画法配置已经升级。Notebook首次在Pro沙箱执行，仅预检成功运行并报错：缺少mquant、ipywidgets；后续图形/交互未执行。保留该原失败记录；Worker产出新的实际执行版本，不改写原历史失败。

W02固定数据为 `observe-iterate@081e31241a0c88e47631f80a8b9b8dd43b2b569c:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/`；W03固定原表为 `d04f3b08892ccf334a06028f3caab994743566a0:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/`。

W03已经补齐i三个K35360400/35361000/35361600及hc末拍原rhythm/intervals、454条行情。**不再重取这些整批资料来证明取数完成。**本轮Pro已消费原表，并独立从hc前24条close得到14次严格新高和与正式一致的最后六间隔；i waiting=0只表示局部重启，尚无last_update，ratio仍缺。原数据可核来源复用；所有旧图，包括W03四页，仍不采用为工作2成果。

已知aidata参考基线 `b044ad9c92ffc98ee1ac7aec829e3673c126c846`，原工作分支fy/bi01-fo01-n-readability-r0009。实际现场新执行须另核HEAD、有效文件、导入路径、dirty状态并先读该版README，再读所需输入/开发合同；不要用main文档暗换现场。uplot手册参考0a4fcd54059782572a3f7e82fad041121e8c65ad；历史实际uplot13badc6c且pfw.py等有既有dirty，不能仅记HEAD就称干净锁定，也不能清理或提交他人成果。

正式N沿原完整实例：协调仓a6f5025e的R30 ACTUAL_RUN_CONFIGURATION.json原件、rb/hc/i三sources、5m、night_end_at_2300、TA_updto20240229_DBA、MedianTwoWindowV1、N6/LOO3、normalization=null、compact_history=true、core.v2。TIS修后3ff34c72、FRP5154c407、workerADT cd5c307d保持只读；完整原件必要时取得，不能按摘要装配删source的新产品。正式产品目录仍为：

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/fb2007d71be1e620801457424d6dea8b4/func
```

目录本身不是已读取证明；优先复用已交正常OnlyRead原件。确需更完整连续发生或上游时，使用正常具名read_session/read_at_knowledge等、显式OnlyRead、限定真实需要，不重生成历史N。

<a id="notebook"></a>
## 3. 工作2：重新成图、Notebook执行和必要交互

### 3.1 候选代码的使用与限制

候选Notebook从本地Git指定提交读取正常导出的原表与行情，恢复多表索引、保留64位Life，然后新调用正常投影/布局能力和show。b044的build_uplot_layout实际调用CAEGraph(...).layout()；可以核源复用读取和图元helper，但必须由本轮实际代码重新绘图，不能加载旧HTML/PNG/iframe或以重存旧输出代替。

现场应检查候选实际依赖及接口兼容，补齐正常Jupyter运行条件并真实执行。候选的预检失败是Pro环境事实，不证明现场环境不可用。不要无权安装/升级共享运行环境或修改保护仓库；优先既有合适kernel及有权独立环境。若需要用户/管理员权限，报告具体阻断，继续不依赖它的工作。

Notebook可按实际反馈修改，重要业务选择见下，不能把候选三切点、23绑定、两列或固定页数当验收配额。DISPLAY_PLAN中的颜色/K/来源/场景约束由当前Notebook实际读取；真实绘图配置仍须形成明确可修订原件，记录实际调用对应。候选只做稀疏点比较，不能用它缩减完整任务的演变观察责任。

### 3.2 本轮已决定的业务画法与检验问题

**rb确认与双窗变化。**价格主图保留原5m OHLC淡背景与close；实际端点和确认点用不同形状/说明，不改变源方向。完成统计近期/此前分别画、保留真实知识时间，不用change一个数替代；working净推进/逆向量和效率与完成窗分开。选定K只用当时合法成员、引用基础和原行情，不带K后记录；页首标当时/末次状态，不把最终down套全段。

三处已取K103150800/103151400/103315800可作为核验起点，不是唯一允许时点。稀疏K只画实际点，不能在未取得的中间发生上造水平保持或连续斜线。确需连续演变，复用可恢复的正式发生/原表及必要正常补读，保留Life/start/方向/资格变化及缺口；旧plot_view_data仅作显示参考，不能成为正式演变依据。声明实际覆盖，不以旧窗口基础时间推断整段未变。

**i缺价和部分恢复。**同一working保留进度/年龄；efficiency/counter缺件不是零，waiting真实0不是ratio0。恢复局部起点35361000、local_count0、last_update缺、分母缺应可辨认，不能把0标成“新极值信号”。下一拍9.5/600与前拍12/0对比。原价缺口不硬连，不把正常休市无采样与已记录缺价混同。候选目前原状态表只辅助核查，须实际把上述重要差异表达在图中；不能用表格替代主要展示责任。

**hc极值等待。**用原close而非high解释极值；需要时标出103057800/3952及末拍3904，等待258000与原分母600/ratio430一起说明。13:40影线high3959但close3946，不能用影线创新高判正式last_update错误。是否为hc另设图由可读解释需要决定，不强制每Case一图。

所有品种色只编码身份；性质用线型、形状、位置、分图和文字。price/ratio/CalendarUTITick不混轴或价格DynStd；waiting不截[0,1]。缺/零/未成熟/未调用/失败分别表达。图例不遮点、单值有非退化range及可读单位、标签不成黑带，随缩放仍可用。不要默认展示全部指标/MAD/LOO中间值；LOO并列不是重要性排名。

### 3.3 真正执行和打开

交付新的`.ipynb`，包含真实代码、实际配置、正式输入入口、正常参数、有效版本/导入路径，保留真实执行输出及失败/修复。实际在可用Jupyter环境从新kernel执行适用单元；nbconvert退出0、上传文件、Python生成Bokeh模型都不能独自证明浏览器交互。

在实际Jupyter前端打开，测本次需要的K选择、hover、缩放/平移/复位和图例操作；核值/来源/状态随选择改变，同进程不同K/range不串用。记录操作者、动作、预期/实际结果和限制，不要求PNG作为交付。HTML可辅助，不是主交付或旧图恢复通道。

给出实际Notebook绝对路径、kernel/依赖、打开方法及确实存在的Jupyter入口。不得猜私网IP或URL；GitHub不运行Bokeh JS的事实须明确。Worker技术看图/交互与Pro本人判断分开，结果回原Pro实际消费；前端不向Pro可达时说明具体限制，不代签Pro已看。

<a id="platform"></a>
## 4. 工作3：同run平台页面与board正式数据

可提前核平台与输入合同，但使用适用的新画法消费到正常入口：

```python
from mquant.aidata.api import (
    build_chart_run, build_big_world_chart_pages, build_board_run,
)
run = build_chart_run(run_brief_input)
pages = build_big_world_chart_pages(run, run_brief_input=run_brief_input, save=True)
board = build_board_run({**run_brief_input, "run_id": run.run_id}, reuse_core=True)
```

这是已核到的公开入口形状，实际参数/返回值仍按现场版本；不是已运行证据。已有有效core可有据复用，不要求机械重跑三个完整计算。按具体观察问题使用人工窗口或真实定位特征，节点显式范围冻结；不照搬30m/1m/5s默认布局导致本N原5m口径改变，不强制全部层级或全数据导出。不同问题需要多个run时分别保持各自三入口链同run及节点身份，不以跨run同名节点等同。

以至少一个实际适用新画法接入，继续本单已明确相关工作；不是交一个URL就主动收工。记录真正运行的chart/pages/board、其返回和必要复用依据。取得正常Trier/CAE节点report_url后实际打开，检查业务图层、版本、K/range和身份，不以HTTP200或URL存在代替图层成功。独立HTML、PNG、临时localhost不是平台结果；不创建自有Host或新平台。

board的feature_slices/来源索引/delivery是工作4主正式来源。N薄表可能跨保存时点引用旧基础，不能只按基础timestamp落不落在node范围决定是否遗漏。应核rows/origins/revisions/window/working/binding及所需metrics/member/rhythm；通用切片不足时用正常OnlyRead/as-known原件作同node明确补充，保留来源和适用K，不新算N。将正式数据与n_display/*、plot_view_data严格分开；显示缓存可以运输但不升级正式身份。

配置按需放入aidata/feature_configs，已有正确文件不无意义重交；实际平台调用必须消费同版画法。若现有接口不能表达多表/附图，沿直接生产者和消费者作必要最小衔接；不以另造一个内部函数但主路径不调用宣称完成。画法问题回工作2，定位/注册/正式交付问题由工作3处理。

<a id="permissions"></a>
## 5. 写权与相连排障

若需要改aidata，先核真实工作树、HEAD及他人修改，**新建独立工作分支**。拟名fy/bi01-fo01-n-notebook-platform-r0011仅供选择，当前未创建；同名已存在时不抢写，使用合法无冲突工作区。只读uplot/TIS/FRP/workerADT/core/SDK，不覆盖他人dirty，不提交其修改。

本单授权范围是上述N Notebook正常调用、场景/配置、必要正常取数及最小显示/平台/切片衔接、运行验证和相连普通排障。可跨必要文件连续完成，不逐错误请批。重大公共行为、平台反序列化需新增受保护外仓注册、权限或业务定义变化，给准确位置/调用/受影响消费者，交原Pro/管理协调原责任者；仅暂停受影响部分。

不得在observe-iterate建立第二绘图库、缓存平台、全历史档案、Host或自动控制机制。专业成果目录可以保存本次Notebook、配置、数据引用及技术证据，但不能复制正式N算法。缺方法不能称待校准，缺调用不能称等数据，缺环境不能称市场Pending。

<a id="return"></a>
## 6. 回交、持续责任与未执行

回交原执行Pro，建议目录 `runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-UPLOT-NOTEBOOK-PLATFORM-04/`，这是目标而非已存在事实。真实结果分别包含：已执行Notebook及实际打开方法、必要展示配置与代码对应、环境/版本及有效dirty差异、正式来源和图用投影关系、所测交互和技术观察；平台三入口实际调用或有据复用、同run/node/范围、实际report_url与打开结果；board正式切片/索引/delivery及必要N多表/as-known补充；失败、修复范围和全部未完。

不用旧61/41/27测试数字代替新Notebook/平台工作；也不以测试数、图数、文件数判完成。原本已验证的数据不机械重读；现场新增数据/模型/视觉各自标主体与资格。可靠数据可先交Pro继续分析，不等整包，但不因一个局部成功放弃本单已明确的相关未完。

整体专业任务的更多普通/反例/边界分析、参数判断、Pro实际新图接受、修订复查和管理完整接收仍由原责任者承担，技术单不取消它们。无法完成时交具体输入/调用/错误、实物和恢复条件，不假造成功或预签接受。

**当前状态：Pro已签发；未派达、未接单、未开始现场执行；拟分支/Notebook成功输出/平台URL/board包均未建立。**
