# W04：修复概览冻结big范围阴影，并实际核对四例辨别故事的图面

order_id: BI01-CO-01-W04-OVERVIEW-SHADOWS-AND-STORY-VIEW
work_order_id: BI01-CO-01-W04-OVERVIEW-SHADOWS-AND-STORY-VIEW
parent_task_id: BI01-CO-01-CASE-RESEARCH-01
work_id: BI-01
run_id: BI-01-CO-01
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-01:professional
issuer_invocation_id: BI01-CO-01-R0013-e7e3db9f05
issuer_assignment_token: 8d8f62f310e444221d56efc34755fe63
return_to: chatgpt:BI-01-CO-01:professional
cycle_id: owner-change-20261028

本单由原执行Pro签发；提交不表示已经派工、修复或实际打开。父任务仍是同一四例的两项产出，不由本单改成单纯修工具。**W02/W03已完成，正式行情与原五图复用，不重新取数。** 技术结果必须回原签发Pro消费，不直接替代业务/管理接收。

<a id="authority"></a>
## 1. 已采用授权与真实执行环境

本次具体授权来自：

`daowei2026/observe-iterate@dd89be6e93ad758385cf0e3a15bc9363cb87f2b0:runs/BI-01-CO-01/OWNER_CHANGE_20261028.md::full`

采用决定：`34189351253d7355986b2516e555aaadfd540829:runs/BI-01-CO-01/reviews/management-R0012/DECISION.md::full`；当前完整任务及新Binding：`da7f038e97e5ba9639886ed0a6e146ad59912d15:runs/BI-01-CO-01/01_当前任务.md`。方法/交付/aidata约束统一为dd89的`professional/case_observation/`。这是原授权内修正，不再申请同一GO，不重新启动Reader或M-START。

沿既有Worker thread **01a17dd7-5033-7e63-b7a2-edd90b691c33**，预期聊天工作区`/dwdhome/fy/cgpterm`。业务执行环境`/dwdhome/fy/BASE_E6_2`，观察仓既有checkout`/dwdhome/fy/observe-iterate-bi01-co-01`。开工核当前实际路径、分支、版本及影响本单的本地差异；保留共享修改，不切换/回退到历史f58，不另建分支，不无关递归审计。Worker发送/执行身份真实记录，不借本Pro token冒充Worker invocation。

观察仓仅写现有分支`fy/multisymbol-case-observation-20261027`下本批`artifacts/batch-01/aidata/w04/`的修正脚本/新调用和显示证据，以及本单`artifacts/worker-BI01-CO-01-W04-OVERVIEW-SHADOWS-AND-STORY-VIEW/`正常回交。原W02/W03数据、manifest、旧COMBINED_PAGE和旧运行报告冻结，不改成新执行事实。必要适配脚本在w04保存新版本，不覆盖旧证据来历。

**若确需工具源码，只允许aidata中与本次概览阴影直接相关的页面组装、范围坐标转换及其必要局部验证。** 使用现场既有实际工作分支，准确记录/提交实际改动；不改uplot/frame/tis/frp、全局注册、安装依赖、部署或共享服务，不做URL路线改造或新平台。普通调试和单内局部修通连续做，不逐错误新增审批；真实超权仅限制对应动作，带准确原因回原Pro，不越权绕过。

## 2. 必读输入与可直接消费的四例故事

本单签发前的共同研究快照为：

`daowei2026/observe-iterate@0b95b59237054eff3b001dd14b784052208a94e2`

按本单实际需要读取：

- `runs/BI-01-CO-01/artifacts/batch-01/research/STORY_VISUAL_CHECKS.md::full`：四例承重关系、具体视口、判断分界、失败段和核验要求；
- 同批`cases/CO01-C01.md`至`CO01-C04.md`的`#anticipatory-story`：本次实际形成的完整辨别故事，不让Worker预设答案；涉及精确事实再读各例对应原行链接；
- 同批`research/R0013_JUDGMENT_CHECKS.json`：本Pro实际源值投影计算及边界，只在对照数值需要时读，不重跑全历史。

专业正文已补，阴影与图面尚未实核。技术者可以报告某关系难以辨认或某句不符源值，但不能替专业者更换目标/赢家、代写市场结论或因画图方便删除反证。无必要不读全部历史runs、旧ZIP、U2/U3源或无关运行工具。

## 3. 冻结图数与缺失原因，不能只修其中一半

正式W03输入锁定`1f7e4b441c2c0381790393fc46e61bc63c93171c`，run=`bi01_co01_w03_cases_20261028_5e4fa62eaf`。四个范围的原始来源已由本Pro实际读取：

`1fa38c7a3a084a5a364437b21b6a3041b9ca0738:runs/BI-01-CO-01/artifacts/batch-01/aidata/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/manifest/timespan_index.csv::full`

blob=`809bd1aa9a07b12f57dea5f96f2689e0fcc83868`。这四行的`start_uti/end_uti`目前实存日期字符串，不是数值UTI：

| Case | 冻结node | 原请求边界 | Case PlotSet |
|---|---|---|---|
| CO01-C01 | big_000001 | 2021-02-01 → 2021-04-07 | case_CO01_C01 |
| CO01-C02 | big_000002 | 2021-07-01 → 2021-10-15 | case_CO01_C02 |
| CO01-C03 | big_000003 | 2022-04-01 → 2022-06-24 | case_CO01_C03 |
| CO01-C04 | big_000004 | 2023-06-01 → 2023-10-12 | case_CO01_C04 |

本Pro已全文读取的原组合程序：

`1fa38c7a3a084a5a364437b21b6a3041b9ca0738:runs/BI-01-CO-01/artifacts/batch-01/aidata/w03/build_native_combined.py::full`

blob=`d42c80aea83c8b251ce8158669c8a528dbba4636`。实际代码从W02恢复overview PlotSet，放入`TestCAE1 → CAEGraph → GMap(5 PlotSets)`，并没有继承原AidataRunOverviewCAE布局后的范围标记与显隐逻辑。R12另已定位aidata f58的`AidataRunOverviewCAE.layout/_mark_review_scope`和数值转换跳过日期字符串的问题；现场对相关调用链定向复核即可，不重新全库诊断。

因此必须同时解决：**组合页实际消费四个W03范围并在正常布局/恢复路径中显示；日期范围按本次Context/日历变成该图使用的UTI。** 只改一个未被组合页调用的helper，或只在当前进程临时加BoxAnnotation，不算修复。

还有一个明确的旧路径风险：原脚本发现COMBINED_PAGE已有相同run/request/index hash便直接打印旧结果并return。重新看到6148或旧JSON不证明新阴影生成。新修正使用独立w04输出，记录实际重建/合法更新及持久对象；不得删旧证据以求走过缓存。

## 4. 局部实现应达到的结果

沿既有能力，令完整概览能够获得并持久恢复四个显式范围及Case/node对应。优先复用aidata已有标记/显隐能力和正常页面组织；必要局部源码适配限本单授权。具体可用参数和保存方式以真实现场API为准，不凭本单创造不存在的函数或新类注册。

范围转换使用与正式W03相同的Context、`night_end_at_2300`日历和已采用日期边界语义。记录原日期、转换函数/入口、数值UTI及显示对应。不要直接用Unix时间，不把首末有效K线时点或核心起止当阴影边界，不猜结束日全天包含或机械追加一天。四个范围应与冻结index一致、顺序有效、可对应Case；解析失败要显式回交，不悄悄丢掉一个范围。

复用完整2021起W02概览及四例30m/mid，既有对象rb/hc/i、数据/日历绑定不变。旧统一原生URL`http://192.168.11.40:5006/cae?node_id=6148`本身没有被判定错误。合法地更新现有对象或形成新的原生对象均可，交准确实际URL及旧新对应；**不为保持或改变端口/路径改造平台**。仍为一个完整页面，不用四个独立链接或截图替代。

图例颜色主要区分品种；范围标记与判断时点不要混成同一种含义。通过现有配置做必要定位或合理缩放即可，不追加复杂图形设计。若正常持久化必须越出授权改动共享框架/注册/部署，保存真实卡点和已有成果回原Pro，不通过仅当前进程有效的临时补丁宣称成功。

## 5. 真实核验，不以代码提交、URL或数量代替

先核原始范围→实际坐标→最终布局对象/标签对应，再实际打开完整页看四个阴影。沿正常入口至少做一次不依赖当前构建进程临时对象的重新打开，确认保存后的正常恢复仍有阴影；记录真实操作方式，不宣称未运行的服务重启。

在全范围和相关局部缩放下核边界不漂移、Case对应不串、显示宽度合理、不遮挡承重行情；实际使用既有或本次最小必要范围显隐能力，记录隐藏/恢复后的结果。显隐不应删除行情/转折、改变冻结范围或破坏其他Case。仅模型中存在四个Annotation而像素不可见也不能填通过。

按STORY_VISUAL_CHECKS逐例实际检查：

- C01：3月15日以前的不同恢复、随后hc失效、22日后的重新判断及i反弹。不能只给月底hc较强截图。
- C02：9月9日以前两次共同恢复/回落的不同保留，以及之后钢材的两次损害与10月反例。
- C03：5月23日以前i的大反向和重新恢复，之后再次回落与延伸并存、6月失效。
- C04：8月21日以前的新相对状态，21日后的结果、24—29日连续守位版本失败，以及9月后续。0.09个百分点及0.5价格单位不作为肉眼明显差异的主证据。

记录各例实际URL/PlotSet、视口范围、三品种是否共同可读、必要hover或字段定位、关键关系是否可辨、失败/部分可辨项。视口变动时ratio重新基准化应被说明，不能拼接不同基数比较。mid实际点不等于当时已确认；closeTs/closeUti_ts已有差异保留，本单不修整个行情日历或历史发布语义。

截图/浏览器日志只作真实运行与查看证据，须具名实际查看者；不能写成本Pro或Owner看过。无实看/打不开/关系仍不清楚均如实记录，不为完成单子统一填PASS。必要调整在本单现有图配置范围内连续做，不能改原数据或研究结论制造可见差异。

## 6. 回交实物及写面

在`artifacts/batch-01/aidata/w04/`交实际修正脚本/必要局部源码diff与相应工具仓真实commit、运行说明、冻结范围到坐标到图对象的准确映射、实际新旧URL关系、正常恢复及缩放/显隐检查、四例故事图面观察和证据。无需为了没有源码修改而制造工具仓commit；确有源码修改则给实际版本及影响范围，不只交本机路径。

实际输入/调用记录另存`W04_INPUT_AND_CALLS.md`，说明哪些原产物被复用、这次执行了什么及没有执行什么。原W02/W03输出不修改，不复制几千根行情来伪装新交付，不把w04脚本准备记成aidata已运行。日志脱敏，不提交凭据/共享工作区。涉及部分失败时，准确交已完成、未完成、影响和原单内可继续事项。

Worker正式回交路径固定为：

`runs/BI-01-CO-01/artifacts/worker-BI01-CO-01-W04-OVERVIEW-SHADOWS-AND-STORY-VIEW/FULL_RESPONSE.md`

开头保留本单`order_id/work_order_id/work_id/run_id/issuer_role/issuer_ref/issuer_invocation_id/return_to`准确对应，另列真实Worker执行身份与时间。不要重演W02缺order_id导致机械补登记，也不以原签发者token冒充Worker自己的执行身份。必要VALIDATION及现场实际证据按正常机制交回。

## 7. 返回后的完整责任

技术结果仅回`chatgpt:BI-01-CO-01:professional`。原Pro消费阴影坐标、真实页面恢复与各例可读性，对未清楚或不支持的故事作必要修正，更新同一Owner入口，再交原管理按dd89新要求接收。Worker技术成功不代替逻辑合理性，也不自动结束父任务。

研究已在本轮同时推进，不能再等待阴影才开始四例补研究；本单也不要求重新审核全部旧数据/工具。收到实际成果前，当前新图面状态仍是未核，不能沿R0011旧接收收工。投入复看按原起点及新cycle继续，非本单审批前置；本单提交不表示已派Worker或管理消息。
