# EAW P1 接续研究｜C0010 累计成果交接索引

Run：OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01。本批在 C0010 有据有限收束，主要发现目标**部分达成、未完全达成**。累计两项有充分依据的有界复盘/叙事组合需求 N1/N2；D004、D005 新增独立迭代点均为 0，但分别取得实际口径修订和具名设计取舍。这里不将它们重计为额外发现，也不将程序、文件或 D 完成数量作为目标达成证据。

## 可交接的业务设计输入

| 设计输入 | 业务影响与当前最强依据 | 具体落点及下一轮设计问题 |
|---|---|---|
| N1：业务区间、闭合及形成材料可得时钟分开 | 有已接纳材料尚未闭合时，当前流动性/记录成交仍可读；最终段端点不等于当时已闭合。D001 有界依据保留，D005 增加具名投影/实际资产核查和联合试读 | MME Attack reader 未保留 closed_at、没有 Formation 读支，几何还会扩单 Tick；设计侧应保留原业务端点、producer 可得/闭合时点及 Formation.available_at 的关系，几何另列。未认证 FRP publication |
| N2：当前可见量/可见原因与对象、价位、切点及活动角色联合 | Wall 存续、最近活动基线与当前核心价的一档量各有角色；离开 L1/对象结束均不能填零。有些已有属性可恢复量，不能笼统称 P1 缺库存 | 在 MME/研究使用侧按 exact 实例、Wall、侧、核心价、源 cut 按需关联 L1；基线保留活动起点、参照价与年龄，物理观察价量与结束对象分开。无需为本次需求复制全局 dense 库存 |
| 成交背景的已有信息用法 | trade_volume 支持平台记录总量背景，不能替代同价消耗或独立方向。含起点与不含起点期间回答不同问题 | 原始输入可读时按明确期间聚合；代理累计仍带自身期间和语义。属于旧 R3/D004 认识的实际使用，不单独计点 |

N1/N2 保持有充分依据的**有界组合设计输入**，D005 另提供了初步使用试查和取舍依据。没有据此升级为全市场研发优先级、生产改进方案、P1 必增字段、实际 P2 错误或收益验证。设计细化先保持原时钟语义，再落实对象/源切点和期间的联合使用；这是具名读口的工作依赖，不是整个 EAW 的强制研发顺序。

## 真案例与反例入口

以下为已发布专业结果的归并，不是 Manager 新算：
- J03 / hc bid4805，2022-02-15 13:37:09：当前量297，活动基线249；已有1条接纳材料、下一 Tick 才闭合，记录 V 为323/快照后108。可同时读取阶段、当前流动性和记录背景。
- J06 / i bid727.5，2021-09-09 11:27:51：最佳 bid 已为727，核心价当前量未知；最近基线516有自己的7秒年龄，接纳6条材料但尚未闭合，记录 V528/526。不能把旧基线当当前量或把不可见填零。
- J09 / hc bid4260，2021-11-18 22:39:42.5→46：复见量276→3，最近 Build 基线21来自4258。J10 / hc ask4850，2022-02-24 13:44:08→11 则627→615，是近乎不变的反例。重接触并不必然意味着消退。
- J15 / i ask565.5，2021-11-02 11:15:34→37：27193→27165，C81580、记录V0；双资格6行仅3个底层 side/UTI。J16 / i ask758，2021-09-30 10:02:32.5→35.5：1367→629、C738、记录V1306/1040，没有该期间 F4 资格。它们完整联合历史本来不同，不是“全链仍盲”的新例。
- J13 / rb bid5600，2021-09-30 09:58:06：当前量1450、材料接纳但未闭合；从09:58:05起含起点 V1739，快照后454，相差的1285不可用于解释初始快照后的消耗。

准确对象、ppid、窗口、UTI、数量/时钟/期间和空值原因均在 [FOCAL_READOUT](https://github.com/daowei2026/observe-iterate/blob/b41bdadc75a16f99efbd8986bb7c4ffec22c48ba/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/FOCAL_READOUT.csv) 及各例 JOINT_CUTS。16过程/15 PG/12日期块；J01–J12 为本轮追加具名深入，J13–J16 桥接复用，先前批量/旧 Run 暴露保留，不称严格留出。

## 实际最小信息与代价

D005 核 96 份实际资产引用，48组/1,259行纯展示重放与实际导出共同字段一致。独立研究表在77指定查询正确取回当前量/可见原因及显式期间记录 V，仍需原对象、活动角色与 producer 时钟上下文。按需仅回答77查询，依赖 raw 可读，不冒称覆盖465个任意切点。

在所检465对象×切点：
- 仅数量/可见性变化保存219行，对记录 V 仍有238处差异。
- 数量或记录 V 变化保存450行才能同时精确，接近逐 Tick 的465行。
- 假设只按现有看图/几何边界取值后延用，保存179行，数量/状态差异118处、V差异274处；这不是实际产品错误率。
- 五列 CSV 载荷逐 Tick23914 bytes、量或 V 变化23252 bytes、77查询按需5441 bytes；不含身份、索引、源维护、传输或生产部署成本，不向多年/全市场外推。

因此现有研究使用侧优先按需联合读取；若将来真实要求脱离 raw 的任意切点离线读口，需重新明确精度与更新策略。准确实表：daowei2026/observe-iterate@727004a820c82d17f02bf082036e5e5f71fb048e:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/SPARSITY_SUMMARY.csv。设计取舍：daowei2026/observe-iterate@5c2877850a62f3a6967463ac7b68c447efecf745:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/DESIGN_DECISIONS.json。

## 已修订的旧判断与未决

D004 已用实际 QT 回查：旧28个无当前 Wall 的 R1 案例所检区间最大 q/QT=0.864007，均未达门槛，不支持称大挂单入口漏检。低量变化事实保留，是否另设对象仍需业务理由。新旧 raw 同源一致，新的 volquant 不等于独立方向或 feed 认证。

原 exact producer/Wall/相容 occurrence、QT交易日/参数、原生定点及准确期间等具体缺件已有进展，不再照抄旧不可识别。仍未认证 feed 单位/单双边/覆盖/同步、离开 L1 的旧价库存、独立方向/归属，真实同价消耗/净撤减保持 null；未取得实际 FRP/P2 发布/消费行为，不能报告其错误或收益。未确认生产 Bug。

旧 Run 已实际完成三入口、三组对照及 S01～S09，并补查第三入口独占11片段/17原区间；本 Run 接续解决正式链缺件及具名联合使用，没有重跑无关步骤。累计追加受选择性窗口和过程相关性限制，不能估计全市场比例或预测/因果关系。本批当前没有明确新增价值的立即后继，不宣称全部研究方向穷尽。

## 完整成果与复用入口

| 产物 | 准确原件与用途 |
|---|---|
| N1 原生报告/证据 | daowei2026/observe-iterate@83abc94304fe4f00419848a2010a143946011ca2:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EXECUTOR_REPORT.md；daowei2026/observe-iterate@77f11f6e5ea4de5ad9e0be1caa3d1312bf4e84c3:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EVIDENCE_INDEX.md |
| N2 原生报告/证据 | daowei2026/observe-iterate@fb278b545bdfb21311dc8b40a41287436bcaf975:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/EXECUTOR_REPORT.md；daowei2026/observe-iterate@8daeaa2906a1a138ce204057747358a31ecf62c8:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/EVIDENCE_INDEX.md |
| QT/总成交研究 | daowei2026/observe-iterate@84ab5f17f33ba52222529f3ddf7da4ea8d891e8d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EXECUTOR_REPORT.md；daowei2026/observe-iterate@1dbbaa1916d13d93cbad113fef4a75fb77940f9d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EVIDENCE_INDEX.md；daowei2026/observe-iterate@86cb7b648cf5917f5c6e5c3b2b06041fde0784d8:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/SOURCE_INDEX.json |
| 具名读口完整结果 | daowei2026/observe-iterate@837e16c72da03b5f327e341843c19e0b18d71a03:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/EXECUTOR_REPORT.md；daowei2026/observe-iterate@877172a09e6db708e76e4c35a39bee6e83826d8b:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/RESULT.json |
| 联合读表/设计取舍/稀疏实表 | daowei2026/observe-iterate@b41bdadc75a16f99efbd8986bb7c4ffec22c48ba:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/FOCAL_READOUT.csv；daowei2026/observe-iterate@5c2877850a62f3a6967463ac7b68c447efecf745:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/DESIGN_DECISIONS.json；daowei2026/observe-iterate@727004a820c82d17f02bf082036e5e5f71fb048e:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/SPARSITY_SUMMARY.csv |
| 重放、程序、案例与图 | daowei2026/observe-iterate@40ddc065bf0e0793852a6df83a0891a3cdc2a902:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/EVIDENCE_INDEX.md；daowei2026/observe-iterate@1af1fc357fca995ecb3bd9c71478df1f86d6d3d7:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/SOURCE_INDEX.json |
| 冻结索引与专业核查 | daowei2026/observe-iterate@0c6e952ccb9d7bad43a554e37160a08d4df0b7e1:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/ARTIFACT_INDEX.json；daowei2026/observe-iterate@52c3d94566ac4fa96b49e8cb28e44309239239fb:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/report/LOCAL_VERIFICATION.json |
| 真实专业回交 | daowei2026/observe-iterate@4a36847962a5cf45d0c2fa81575e860866043d10:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0009/PRO_RETURN.json |
| 旧 Run 成果/覆盖和结束事实 | daowei2026/observe-iterate@ff45aab0c8e66e4feb552b2c8a632210d9b58b56:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/RESULTS_INDEX.md，历史原件保留 |

本地 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261126-01/calls/C0009/`：`cases/CASE_READOUTS.md` 和 J01–J16 保存原输入/实际视图/正式历史/联合表；`figures/JOINT_READOUT_CASES.png/.pdf`、`SPARSITY_TRADEOFF.png/.pdf` 为实际图；`research/` 保存研究和核查程序。C0002/C0004/C0007 冻结包及旧 Run 保留。controller 已按冻结索引独立核532文件/2,791,729 bytes，11份正式原件及实际工具 commit 匹配；Manager 复用此运输完整性事实，未再全扫包。

本批有限收束和条件接续由 C0010 Manager 正式决定。当前不签 D006，不重派旧 D；未来具名消费者/离线精度需求、可认证原批计量归属材料或新的高价值原批反例到达后，按真实信息与授权接续。原148窗、rb/hc/i与生产只读边界不变。原始成果和准确专业等级以各 Executor 原件为准。
