# BUSINESS_PROGRESS｜QT 与成交口径已修订，继续具名复盘读口研究

## 一、当前任务与整体情况

目标仍是从原批盘口—成交演化中取得对业务设计有价值、有证据的迭代依据。当前**部分达成**：已有 N1、N2 两项有充分依据的有界组合需求；本轮新 QT 与成交数据已实际进入研究，修订了旧入口判断和成交用法，未新增独立迭代点。发现数量和单项回交完成都不替代整体达成。

Owner 最新提示中的“成交情况，可能要以 trade_volume 为主”已由专业工作落实为：以该字段描述**平台记录总成交背景**。它不能直接代表同价方向消耗或真实净撤单，且与旧 raw 同源，不是一份新增独立成交真值。准确 Owner 原文：daowei2026/observe-iterate@cd6b79d09796b515dc630e86a24130f7b67bec82:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/owner/RESUME_20261126_VOLQUANT_TRADE_VOLUME.md。

当前还有可执行且有价值的问题：将已有时钟、可见状态和记录成交放到一个实际具名复盘/研究读口，检验它能否清楚回答当时面对的流动性、过程阶段与期间成交背景，并判断最小需要改变什么。父任务继续，下一项不重复代理数值统计。

## 二、实际开展的工作与结果

| 业务工作 | 实际做了什么 | 业务认识/结果 | 当前状态与入口 |
|---|---|---|---|
| 过程时钟与形成材料 | 核相容正式历史、业务端点/闭合/发布可得性及现有复盘读口 | N1：需要按实际时钟与材料可得性组合阅读，避免把业务区间端点当作已闭合时刻 | 已形成有界设计依据；daowei2026/observe-iterate@83abc94304fe4f00419848a2010a143946011ca2:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EXECUTOR_REPORT.md |
| 当前可见量与角色 | 核重新接触过程、同对象/核心价/切点、可见性和已有属性可恢复范围 | N2：当前可见量/状态应关联对象及参考价、时点角色；有时旧属性已能恢复量 | 已形成有界组合依据；daowei2026/observe-iterate@fb278b545bdfb21311dc8b40a41287436bcaf975:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/EXECUTOR_REPORT.md |
| 新 QT 关联与旧入口判断 | 对齐原 148 窗，核正式交易日/实际参数及 96 个选中阈值；回查旧 R1 | 旧 28 个关键切点无当前 Wall 的案例，在所检区间始终低于 QT，不能据此认定大挂单漏检 | 已修订旧推断；daowei2026/observe-iterate@84ab5f17f33ba52222529f3ddf7da4ea8d891e8d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EXECUTOR_REPORT.md 第 1–2 节 |
| 总成交与正式交互 | 核 4,526 occurrence、相容代理路径、1,627 条完整总量轨迹及六个真实过程 | 盘口命中代理与平台记录总量有实际差别，期间也必须对应；不能把它们混称真实消耗 | 实际源内研究完成；daowei2026/observe-iterate@84ab5f17f33ba52222529f3ddf7da4ea8d891e8d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EXECUTOR_REPORT.md 第 3–4 节 |
| 最小信息及现有联合表达 | 六例之外再对 18 PG 附接已有总成交，检查实际联合历史和压力算式限制 | 正确关联已有总量能承载记录背景；未证明必须新增 P1 数值、标签或实际 P2 误读 | 本轮新增独立迭代点 0；daowei2026/observe-iterate@84ab5f17f33ba52222529f3ddf7da4ea8d891e8d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EXECUTOR_REPORT.md 第 5–6 节 |
| 下一项实际研究 | 已签发具名 MarketMicrostructureEvidence 读口的联合使用与最小设计取舍任务 | 将 N1/N2 与正确成交期间落实到真实读口问题；既有信息能回答时也据实交付 | 已正式组织，等待物理派达；daowei2026/observe-iterate@52ca9acd6e2923e6e0f852f2d66ed5fabf5f01a6:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/delegations/D005/DELEGATION.md |

## 三、重要认识与后续处理

| 认识/问题 | 业务意义 | 证据、限制或反例 | 当前判断及下一步 |
|---|---|---|---|
| 低量过程没有当前 Wall | 无事件本身不足以支持大挂单入口改动 | 28 例所检区间最大 q/QT=0.864007；唯一 same-core 例另有实际对象；触及 QT 也非 Wall 充分条件 | 撤回无据漏检推断，保留量变事实；不重复量比或仅凭无事件立新对象 |
| 两种成交期间 | 正式累计代理与初始快照后的流动性变化回答不同问题 | 正式 C 从 start tick 计入，比较用 [start,cut]；I→R 用 (start,cut] | 作为实际读口联合使用必须保留的语义，不能互换 |
| 代理与记录成交差别 | 可见活动大不等于真实承受同量成交 | 1,627 条条件轨迹中 518 条 C>记录总量；43 条 C>0/V=0 中 i 的 42 条集中一 PG/Wall/日期块；普通 hc 反例 C 仅为 1 | 只能报告条件事实，不把数值不等都包装成严重损失或总体频率 |
| 现有联合材料有能力 | 不能由一个 Absorb 指标未含总量，断言全部正式材料无法区分 | T01/T02 近似量变对照的 Formation/Build/F4 历史不同；raw 总量本来可得，研究压力和也不总能恢复总量 | 本轮属于已有信息使用及旧 R3 的实际联合核查，不重计新点 |
| 真实消耗与净撤减 | 仍不能从 L1 和同源代理确认订单归属 | 定点原生值一致并不认证 feed 单位、单双边、覆盖和同步；方向字段仍为盘口预测 | 保留未决，需适合原批的独立证据；不阻断记录背景研究 |
| N1/N2 的适用层次 | 已能支持复盘/叙事读口组合设计的下一步讨论 | 不等于 P1 必增字段；未取得对应实际消费者证据时不能认定 P2 行为错误 | 在具名现有读口实做联合阅读及有价值时的最小信息/代价试查，不预定新缺口 |

QT 与新旧 raw 的匹配、正式 producer/Wall/occurrence 以及 162 个原生点的核对，已经解除对应的具体旧缺件，不能继续照抄“材料一概不可识别”。旧 Run 与所有冻结原件保留，只修订受到新证据影响的推断。

## 四、可直接查看的当前成果

| 产出 | 内容与业务用途 | 有效范围/版本 | 准确入口 |
|---|---|---|---|
| 本轮完整研究 | QT 修订、成交期间、六个真实过程、联合表达、试查、未决及后继 | 原 148 Tick 窗、rb/hc/i；匹配的冻结正式历史 | daowei2026/observe-iterate@84ab5f17f33ba52222529f3ddf7da4ea8d891e8d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EXECUTOR_REPORT.md |
| 证据与来源 | 重放研究表/图/程序、真实对象和切点、版本及定点核对 | 具体证据成熟度以报告为准 | daowei2026/observe-iterate@1dbbaa1916d13d93cbad113fef4a75fb77940f9d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EVIDENCE_INDEX.md；daowei2026/observe-iterate@86cb7b648cf5917f5c6e5c3b2b06041fde0784d8:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/SOURCE_INDEX.json |
| 结果与研究处置 | 实际覆盖、计数、旧认识修订及每项处理 | 条件范围；非总体频率/预测认证 | daowei2026/observe-iterate@4fddedfecbdde8bfb64ac86e06748b30ebb5c03b:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/report/RESULT.json；daowei2026/observe-iterate@3ce7f51cc84d86b081107712a5f092c7542de5f4:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/report/RESEARCH_DISPOSITION.csv |
| 既得设计输入 | N1 与 N2 的真实案例、反例、边界和设计位置 | 有界复盘/叙事组合需求 | daowei2026/observe-iterate@83abc94304fe4f00419848a2010a143946011ca2:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EXECUTOR_REPORT.md；daowei2026/observe-iterate@fb278b545bdfb21311dc8b40a41287436bcaf975:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/EXECUTOR_REPORT.md |
| 下一项工作 | 具名读口联合信息使用，实际判断有无必要改变及最小代价 | 原范围和授权，独立研究、生产只读 | daowei2026/observe-iterate@52ca9acd6e2923e6e0f852f2d66ed5fabf5f01a6:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/delegations/D005/DELEGATION.md |

## 五、限制与下一步

E1 下一步从现有 MarketMicrostructureEvidence 复盘/研究读口出发，以真实过程核它目前如何使用对象、时钟、可见状态和记录成交；已有联合信息足够时交付正确用法，有具体业务混淆时追到第一处限制，并在有价值且可行时实际试查少量最小信息及稀疏化代价。不会因缺少可选的实际 P2 产物而停止全部研究，也不会把研究读口自动当作生产消费者。

本批是选择性、已多次暴露且过程相关的窗口。追加案例如无未暴露过程，应如实标明；不声称严格留出、全市场发生率、预测/因果关系或生产改进率。真实消费行为和生产成本须有各自证据，当前未认证。

原 148 窗及 rb/hc/i 边界、生产/数据库/公共上游只读继续有效，不新增行情、重产或恢复源 Chat。旧 D003 已替代且从未派达；已完成工作与冻结包均保留。当前没有需要 Owner 再审批或必需帮助的实质阻碍。

技术恢复入口：[TASK_PROGRESS.md](TASK_PROGRESS.md)。最近更新：2026-11-26 14:51:18 UTC；最新已核实成果为上列 C0007 完整专业回交。前一规范业务视图保留：daowei2026/observe-iterate@d359f8ba7031b756724fd95f274eb5e47ec93260:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/business_control/BUSINESS_PROGRESS.md。
