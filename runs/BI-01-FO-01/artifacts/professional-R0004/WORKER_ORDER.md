# BI01-FO01-N-AIDATA-01：正常 N 读回、展示接入与真实制图工单

<a id="authority"></a>
## 1. 本单身份、完整目的和执行边界

work_id: BI-01  
run_id: BI-01-FO-01  
order_id: BI01-FO01-N-AIDATA-01  
parent_task: BI01-FO-01-N-OBSERVATION-01  
issuer_role: professional  
issuer_ref: chatgpt:细节叙事生成_金标:BI01-FO01-执行  
issuer_invocation_id: BI01-FO-01-R0004-20261022T035604Z-55f1ff3f  
issuer_assignment_token: BI01-FO-01-N-OBSERVATION-86bbc21e26fd4d0583b6bfb9e38f7ac7  
技术接收角色：本 run 既有机制实际委派的 Worker Codex；技术结果返回上述执行 Pro，由执行 Pro 消费后向管理交业务结果。

**本单由本次执行 Pro 实际签发；发布不是已发送、Worker 已接单、已执行或管理已接受。**不虚构 Worker 聊天、进程或未来 invocation。本单服务既有完整专业任务，不另立阶段 Gate、不改变业务主体，也不使执行 Pro 退出完整责任。

直接授权来自 `daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md#plan`，当前任务为 `89aacaa9b8d7068a567b77c2ca078cb2939c347d:runs/BI-01-FO-01/01_当前任务.md`，采用依据为 `aeccf4c91b94a7f889f84970b37ab5048b9c07f6:runs/BI-01-FO-01/reviews/management-R0003/DECISION.md#adoption`。

当前业务问题：最近六个完成过程、此前六个完成过程和当前 working，分别怎样对应真实价格过程？把它们画出来后，是否会把历史完成统计误当当前走势、把端点位移误当波幅、把局部节律误当全程事实？本单取回能实际回答这些问题的图、数据、方法关系及技术核查，不要求证明收益预测、跨品种机会簇或完整 U2/U3。

TIS、FRP、公共 core/SDK 本单只读。允许本单所需正常读取、参数装配、具名多表关联、仅供展示的数据投影、aidata 现有入口调用与普通相连排障；不重写 N 算法，不建立 Episode 全历史档案、私有发布恢复设施或第二套绘图平台。发现保护面或公共行为必须改变时，只暂停受影响部分并给 Pro 准确证据，交管理协调原责任者。

<a id="sources"></a>
## 2. 必须使用的真实输入和版本

以下 `COORD` 是 `daowei2026/feature-refinement-implementation-agent-evolution`；`BATCH` 是 `agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/first-two-fao-20261017`。两者只是本单内的路径缩写，不是新数据身份。

|对象|准确来源及使用方式|
|---|---|
|现行专业方法|`observe-iterate@4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md`、01_OUTPUT_BASE_FORMAT、02_WORK_DETAILS、03_REUSE_FROM_V2、04_AIDATA_USE；保持四项可往返|
|完整实例|`COORD@a6f5025e8b082f8f11056e566a2a07abc49bb939:BATCH/ENGINEER_STORAGE_REDUCTION_R30/ACTUAL_RUN_CONFIGURATION.json`；取得完整 JSON 原件，不照本单摘要重造 sources|
|原读回记录|同 COORD/ref 下 `BATCH/ENGINEER_STORAGE_REDUCTION_R30/READ_REAL_N_01_BINDING.json`；只用于定位历史执行，不能充作本次读回|
|解释边界与历史样本|同 COORD/ref 下 `BATCH/MANAGEMENT_N_REASONABLENESS_RECEPTION_R33/FULL_RESPONSE.md`；不执行其原批次 R23 后继|
|正常接口|`daowei2026/tis@3ff34c72be8ef025f68e18b097fe7b8f1f472668:frp/U2NodeBehavior.py`、`frp/U2ThinNode.py`|
|正常构造与方法|`daowei2026/frp@5154c407249c130a6e048c8541b76dfdec3ea48c:src/Frp/Instance/ISL/Opportunity/U2/EpisodeBehaviorPipeline.hs`；具体疑问按 NodeBehavior、BoundedExecution、BoundedPath、BoundedEpisode 及 Episode 的直接函数核对|
|历史正常调用示例|同 COORD/ref 下 `BATCH/ENGINEER_STORAGE_REDUCTION_RECEPTION_R31/read_context.py`；目录名 R31，实际为后续工程材料。它明确使用 `rerun(CalType.OnlyRead)`；不可盲抄其另一旧配置文件或 Calendar 列表第一项|

已报告正式目录：

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/U2NormalNodeBehaviorFrp/9/0/d/3/7/a/4/fb2007d71be1e620801457424d6dea8b4/func
```

R0004 Pro 环境实际检查该目录、`/dwdhome/fy/BASE_E6_2/mquant/aidata` 和 `/dwdhome/fy/observe-iterate-share` 均不存在；这是 Pro 环境事实，不是 Worker 本机或原数据已丢失的证明。

实际旧行情生成程序是 FRP `84e5b68a07995fd80b78bad45670b6ad55595bdc`、TIS `f70fc4b2e67cb780ece871b2ac9ced5ac46d0a00`、worker `0037a811daa43de644b58ecf102d828617cb4f48`。后续 FRP 5154c407、TIS 3ff34c72、worker `cd5c307dcb3483ef76242b5c37177a969c5fcbd2` 不倒记成原生成程序。现场实际导入版本和文件路径另记，不因 git HEAD 看似正确就忽略 Python 导入到了其他 checkout。

初始实例维持 rb/hc/i、5m、night_end_at_2300、TA_updto20240229_DBA、core.v2、compact_history=true。完整三来源均保留，**单品种展示在读回后按真实 object/binding 选择，不通过删掉另外两个 sources 改写产品身份**。正常入口现行硬校验 N=6、LOO minimum=3，不能自行试 N=4/8 或恢复全历史以支持参数扫描。原 normalization=null；仅显示范围/图层变化不更改这些计算参数。

<a id="readback"></a>
## 3. 正常取数及关联要求

先核现场挂载、完整配置、实际导入的修后读者，以及正常 feature.product_definition()/full_dir 与本实例的对应。完整 sources 从 ACTUAL_RUN_CONFIGURATION 的 `配置.source.sources` 取得，不能手抄简略参数。上下文中的 SOF、对象和 Calendar 必须与原实例一致；历史示例的 `tuple(...)[0]` 不是本单允许猜 Calendar 的依据。地址不符时先核实例/环境，不改保存身份迁就现有目录。

正常入口已有 `from_sources`、`read_session`、`to_dfs(products=...)`、`iter_dfs`、`read_exact`、`read_at_knowledge`。读取现存结果采用明确 `CalType.OnlyRead`；历史实际示例中的 `feature.rerun(CalType.OnlyRead)` 可以作为正常用法参考，**禁止的是默认或强制重生成，不是机械禁止名字中含 rerun 的所有调用**。本单不授权重跑全历史生成来掩盖读者/配置问题。`to_df()` 明确不支持此产品。

先取得用于识别对象/范围/状态的必要表，再定向取窗口和 working。可在一次请求内复用正常 session 与元数据、分块读取，避免每幅图重新读全结果；这不是新建永久历史服务。

必须遵守实际关系：

```text
rows.window -> windows.address -> windows.binding -> bindings.address
rows.working（0 表示没有 working 基础）-> working_bases.address
working_bases.binding 与 window.binding 一致
specs 通过所属 binding + kind 解释 metrics.kind
成员/指标取该窗口自己的保存坐标
节律/间隔取该 working 基础自己的保存坐标
working_values 和六类 working 数值取本次发生自己的坐标
```

这些表按各自实际频率保存，不按 DataFrame 行号、列表下标或当前 record_id 固定假定对象。展示投影必须保留原发生坐标、地址关联、对象、方法和相关 exact 引用；物理地址本身不冒充业务身份。

`read_exact` 使用完整 book/kind/Life/revision；`read_at_knowledge` 使用明确 Life 和原整数知识时间。时间标签仅作候选定位，不凭日期猜 exact 或将 latest 修订倒填过去。处理同一标签多条发生时保留全部实际身份，不任取第一行。图中所选 As-Of 必须与读取结果一致。

状态按 `present/knownness/applicability/reason` 及原编码解释。公开 nullable 值保持空，真实零仍为零；不得在 CSV、JSON、图层转化中 fillna(0)。完成窗足十二成员不意味着每项指标都可用；不能剔除坏成员后补入更早好成员。working 不加入两侧已完成样本。

同范围行情优先经正常 U2MainlineKLineInput OnlyRead 取得原 close、open_uti、calendar_position、calendar_time；OHLC 可作背景，但 N 的原计算基底是 close。原数据 life 为 `/m3varI/var/L1_data/tick/map_kline_data/5m/{sym}_night_end_at_2300`，数据/Calendar revision 均保留原绑定。不要把本机路径相似等同于同一版本。

N 薄表并未承诺保存所有成员逐项原指标和全路径。已有正常结果可读则引用；需要检查的有限成员可按原起止、方向、原价与 Calendar 作**观察参考复算**并单独标识。参考值不冒充正式 Episode 产品，不要求恢复已撤的全历史档案。不能取得足够路径时，给出具体缺口，保留不依赖路径的可用结论。

<a id="display"></a>
## 4. 展示首版：画什么、如何避免误读

### 4.1 三类信息分开，但同一实例/观察点可相互定位

**价格与过程图。**以真实 5m close 为计算路径，K 线可作背景。最近六个和此前六个完成过程以不同线型/标记区分，编号按各自原业务顺序，working 另用未完成标记。端点连线只表达过程边界，不冒充实际行程。实际起止和确认/known_from 分别表达；过多标签放悬浮信息或同页表，不把全部字段挤在图内。所选 As-Of、working through、两窗各自最早起点/最晚终点必须可看见。单独标明“历史输入标签使用同 bar close，不是开盘瞬时已知”。

**完成窗统计。**展示六项指标的近期中位数、此前中位数、绝对差、近期未缩放 MAD、可用状态；按 price、CalendarUTITick、ratio 分轴或分表。`change` 不转写为变化百分比，`dispersion` 不称标准差。LOO 放可展开明细：基准、最大绝对移位、全部并列及逐槽值；不能画成六成员贡献重要性排名。支持按成员定位原价，但没有正式成员数值时明确参考复算来源。

**working 与节律。**独立展示方向、起点、through、duration、progress、efficiency、counter、waiting 和 waiting_ratio 及其状态。完成状态 Pending 与当前可用数值并存，不把整条 working 涂成“未生效”。节律单独说明最近六个极值更新间隔按此前3/近期3比较，显示实际分母、局部起点/次数及全程次数的可知性。waiting_ratio 不截到[0,1]；零分母按 NotApplicable 显示，缺价恢复的 waiting=0 不画成新极值确认。缺口不连线、不填价。

### 4.2 范围与大中小

长期概览用于导航覆盖、完成窗更新和可疑位置；它不替代观察十二个实际过程。中等范围优先覆盖所选两窗成员完整实际跨度、相关确认位置和 working 到 through；跨度很长时可分段/联动，不为塞进固定图宽截掉成员。局部范围用原 5m close 检查转折确认、过程切换、回撤或缺口恢复。

这里“大中小”是同一特征的显示范围，不自动变成三个不同频率的 N。若 aidata 现有缩放方式不能看清边界，按实际图修配置，不强套其默认全景。用于概览的降采样不进入路径算术；关键局部保留原采样。先画单品种，再按解释需要并列 rb/hc/i；原 price 未归一化，不作三品种绝对排名。

### 4.3 首轮候选位置与挑战

首个连贯位置优先 rb 在原标签 `2024-02-29 14:55` 附近：读真实发生和十二成员/working，检验“完成窗效率改善”能否与当前过程反向运动同时正确呈现。随后用相邻普通完成窗/同一 working 的前后实际输出挑战，避免只看末值。

按数据实际可得性继续处理下列已有线索，而不是等三个品种全部齐全才画一张：rb `2016-05-30` 的低完成窗效率与较高 working 效率；i `2021-10-21` 的中位效率1/MAD0；hc 末段实际长窗与较高等待倍数；i `2017-03-30 14:55` 至 `2017-03-31 09:00` 缺价恢复及其相邻位置；首次6+6成熟前后的样本资格。它们来自 R33，**本单不预判为缺陷，也不把其旧数字复制成本次读回值**。

这是具名起点，不是固定 Case 配额或六道 Gate。各位置的准确修订、完整成员范围和知识切点由正常读取确定；如原时间附近有多次发生，保留选择依据。初始展示若已能回答某问题，不机械堆重复图；若发现新问题，沿受影响依赖继续核查。

<a id="aidata"></a>
## 5. aidata 真实调用和有限写权

操作端报告 `/dwdhome/fy/BASE_E6_2/mquant/aidata`、HEAD `f58ea95c358b9ac31659c92b7bc20fe9bf7f8264`、分支 `codex/aidata-named-csv-features-20261019`。本 Pro 再次请求该 commit 的 README 返回 `404: No commit found`，不能声称已读。Worker 必须在实际现场核 checkout/HEAD/工作树状态并先读该版 README，再按本次需要读开发说明、run_brief 输入合同和已有实例。不用 main 文档暗换实际代码。

优先现成具名表/命名 CSV 投影和已有点、线、线段、文字/悬浮、分图机制；是否支持必须通过真实调用确认。投影只是图用数据，不另造生产 Feature。不要为了套 generic `.to_df()` 入口修改 N 读者。

确需修改 aidata 才能接入时，本单授权在其仓库从实际核实的基线**新建独立工作分支**后处理 N 多表图用输入及直接消费者所需的最小相连扩展。可采用新分支名 `fy/bi01-fo01-n-observation-r0004`；这是拟创建授权，不是存在或已检出的事实。若该名已有，不能占用覆盖，另取不冲突名称并记录真实 base/head。不得直接改原分支、覆盖他人工作树或改共享平台公共行为。仅有未接入真实调用的新函数不算修通。若所需变更越过本授权，回 Pro/管理，不擅改 TIS/FRP/core/SDK。

本单不要求将首版永久写入 feature_configs。成熟后是否沉淀由实际观察决定。无必要扩展则只用配置/投影，不为了有代码而改工具。

至少交付可访问图页/图文件、实际渲染证据及对应数据。页面存在、程序exit0、浏览器实际有目标图层、AI视觉看过图是不同事实；截图或图像必须是真实生成和打开的结果，不用示意图替代。截图应能识别品种、范围、As-Of与图层含义；数据文件应与所展示范围、成员和状态相符。

<a id="checks"></a>
## 6. 本次需要核什么，而非另做全面工程审计

围绕选定结果核：正常读者与实际导入版本；原实例地址/定义；对象/窗口/working 的关联；规格代码与定义，不按默认顺序配名字；成员时间及两窗无重复/working 不混入；图层端点/数值/缺口与对应正式表一致。

有限参考复算使用该成员完整原 close/Clock 范围，而非图上稀疏抽样或直线；两窗中位数、差和 MAD 按固定原成员计算，效率的中位数不能用两个中位数相除。逆向量是过程内累计最大不利回撤，不只看最后一拍。LOO 六个绝对移位并列是原六值中位数方法的可能必然结果，不强行选一个“最大贡献者”。

对时间和状态的检查同样具体：确认/known_from/as_of遵循原历史口径；实际点不提前当确认；休市后的 Calendar 增量由真实 Clock 核；缺价后端点可恢复而路径量仍缺失；局部计数不是全程计数。真实零、合法空、未成熟、缺价/缺Clock、未调用和读取失败分别记录。无实际差异就写该范围未发现差异，不升级为全特征正确率证明。

不要求重跑 R33 全部检查数量，也不把其 910/1200/97 项复制成本次已执行。不是每个市场分支都必须在本单制造一个合成 Case；合成检查若确有需要，与真实行情结果分别记。

<a id="delivery"></a>
## 7. 实物、失败与回交

在本 run `artifacts/` 下保存本单实际技术回交及图/数据定位，保留实际代码/配置和调用；大文件按既有可用交付渠道交付，不建立私有发布设施。回交须能让 Pro 恢复：实际输入/产品/读取版本；每个已做 Case 的对象、exact、As-Of、成员和选择理由；图与同范围数据；投影字段对应；实际调用/退出/异常；渲染与视觉检查各自发生到哪里；有限核验结果和所有重要未完。

不能只回“24表读取成功”或“已生成页面”。失败应报来源/路径、调用、字段/时间、错误和直接受影响结果，说明恢复条件。没有挂载是输入未取得；未调用是未执行；方法不支持是方法/接口缺口；不能都写成市场 Pending。某品种/图层失败不取消其他可靠部分，普通相连排障在本单范围内继续，不逐文件请批。

实际技术完成后将完整回交交 `chatgpt:细节叙事生成_金标:BI01-FO01-执行`，由该 Pro 看真实图、核解释、形成认识/反例并修订展示或参数。Worker 不自定资金或机会簇业务目标，不代签专业观察/管理接受。本单没有授予主控调度改造权。

当前发布状态：工单正文已签发；实际运输、Worker接收、现场OnlyRead、aidata调用、图层渲染和技术结果均须后续真实记录，本文件不预填。
