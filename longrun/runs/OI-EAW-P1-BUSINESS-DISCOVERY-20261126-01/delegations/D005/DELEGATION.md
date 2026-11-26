# D005｜具名复盘读口的联合信息使用与最小设计取舍

run_id=OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01
delegation_id=D005；issuer_call_id=C0008。
issuer / return_to=codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01:manager
recipient=codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01:executor:E1
原 E1 threadId=01a21621-ae67-7471-9ed7-a47e4415d510；沿用原线程，CODEX_NATIVE_DIRECT、gpt-6.1-sol/max、workers=[]、AUTONOMOUS。

## 任务原意与这次实际工作

原目标是从本批盘口—成交演化中取得对业务设计有价值、有证据的迭代依据。D001/D002 的 N1/N2 已成立为有界复盘/叙事组合需求；D004 已用实际 QT 和记录总成交修订旧认识，但没有新增独立迭代点。不能把 D 完成或发现数当父任务完成，也不能反复统计同源代理制造继续的理由。

本次从**现有 MarketMicrostructureEvidence 复盘/研究读口**出发，实际解决原任务 §§6–7 仍可推进的问题：在同一对象及切点，如何使用既有的过程时钟、当前可见状态和记录总成交，才足以回答当时面对什么流动性、过程处于何阶段、期间发生多少平台记录成交、哪些只是盘口命中代理或可见活动？哪些问题现有联合信息已能回答，哪些确需一个有业务价值的组合改变，最小需要保留什么、放在哪里、代价怎样？

具名起点来自 D001 已取得的 `calls/C0002/sources/market_microstructure_evidence.py` 及其实际读入/视图路径，准确版本和证据入口见 N1 EVIDENCE_INDEX；D004 的总成交试查及新 QT 导出可作已有输入。先核实这一读口实际可读材料、版本和用途，不能把它自动当作已发布 FRP/P2 消费者或整个产品。若材料显示该读口已能充分回答某问题，记录正确用法和反例，不把不存在的缺口立项。对实际使用行为的判断须有对应产物/记录；没有时保留为研究读口的设计输入。普通专业取舍由 E1 依据实际结果直接处理。

## 如何承接已有结果

- N1：业务区间端点、闭合/发布时点和 Formation 材料可得性需要按原语义联合阅读。已有生产字段及历史不等于具名读口已保留这些关系。
- N2：当前可见量及可见状态必须关联对象、侧、核心价和源切点；活动基线有自己的价位、期间和角色。部分旧属性已可恢复数量，不能笼统声称 P1 缺库存。
- D004：以 trade_volume 描述**平台记录总成交背景**有依据；它与旧 raw 同源，不是新增独立方向真值。正式代理累计比较用含起点期间，初始快照后量变用不含起点期间，实际按源码/输入语义核定，不能混用。不得把总量、方向压力、同价消耗和可见活动混成一项。
- 三者在具体读口怎样联合使用、是否仍存在影响实际叙事的问题、按需关联与稀疏表达的取舍尚有可执行空间。本次据真实案例做出来，不仅再写需求名单或改写旧报告。按原 §7，有价值且可行时在独立研究表试查少量最小信息；不实现完整新算法或改动生产。
- 案例/对照/反例、补充范围和程序由 E1 按原任务证据要求选择；能复用就复用，需要新的同批过程时优先选择未用于该线索形成的过程，并如实记录先前暴露及相关性，不包装严格留出。没有新增价值时可以据实回交，新增点数不是本 D 的门槛。

## 当前有效认识及边界

旧 28 个无当前 Wall 的 R1 案例在所检区间始终低于实际 QT，不支持以其宣称大挂单入口漏检；唯一 same-core 案例另有实际对象。不要重复这组量比，也不要仅以无事件要求新对象。真实方向/同价消耗/净撤减仍缺独立计量覆盖和归属证据；更多同源代理或事件不能解除这一限制。D004 已实际核过相容的正式历史，不能将某一单项不含总成交当作 P1 全链缺失。

仅原 148 个 Tick 窗口、rb/hc/i；新 QT 根仍是同批补充，不扩至其他尺度或新增行情。新旧原始输入已在 D004 核为同源一致，可复用事实而不重扫整个冻结包。实际 TIS 版本保持 receipt 的 Git 部分加逐源 source-sha256，不能用工作树 HEAD、参考代码或新目录事件表替换正式来源。新 QT/参数关联事实也不等于 feed 单位、单双边和覆盖认证。

源数据和现有生产/公共上游/数据库只读，不运行或重产生产特征，不改变参数，不恢复源 Chat，不借其他 Run/线程施工。研究试查写新独立产物，旧 Run、本 Run C0002/C0004/C0007 冻结包及 D003 历史均保留；D003 已 SUPERSEDED 且从未派达，不执行。D001/D002/D004 已到回交节点，不重派。

## 有意义的回交节点与产出依据

依原任务 §§6–7、8.3–8.5，取得这一个具名读口问题的真实业务判断：实际案例与反例、现有联合信息的能力和限制、具体设计位置/是否值得改变、有用时最小信息试查与稀疏化代价。未实测生产成本只给有依据的研究范围，不冒称部署效果。已有信息能回答的结论同样交付；新发现只按实际证据成熟度表述。保留可重放入口、必要研究表/程序/图与来源，不增加统一文档清单或管理验收。

达到上述有后继选择价值的节点后向原 Manager 回交实际完成、整体达成程度、未决及影响、已经尝试的办法、下一步价值或有据收束/具名恢复条件；D 的 REPORTED_COMPLETE 不替代父目标。授权内普通方法直接实施，不新增常规 Owner 审批或待审批分析计划。需要真实外部帮助时依 TASK_WORK_PRACTICE 说明具体已发生问题，其他有价值工作继续。

## 精准原件与只读入口

- 当前 C 原件：daowei2026/observe-iterate@56dad0cc4eeb238518957de3193d9dadd594b2c1:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0008/FULL_ASSIGNMENT.md
- 原任务：daowei2026/observe-iterate@ff45aab0c8e66e4feb552b2c8a632210d9b58b56:ai_chat/业务有效性/EAW_P1_挂单成交演化_迭代点发现任务_V0.4_长程执行版_20261125.md
- Owner GO：daowei2026/observe-iterate@6bcd182071c0aa42db2fb67e1fa8b01c1c90862e:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/OWNER_START.md
- Owner 最新补充：daowei2026/observe-iterate@cd6b79d09796b515dc630e86a24130f7b67bec82:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/owner/RESUME_20261126_VOLQUANT_TRADE_VOLUME.md
- D004 完整回交：daowei2026/observe-iterate@9d7b3e2376de8b7c54340df849252015203068ed:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/PRO_RETURN.json
- D004 报告：daowei2026/observe-iterate@84ab5f17f33ba52222529f3ddf7da4ea8d891e8d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EXECUTOR_REPORT.md
- D004 证据与来源：daowei2026/observe-iterate@1dbbaa1916d13d93cbad113fef4a75fb77940f9d:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/EVIDENCE_INDEX.md；daowei2026/observe-iterate@86cb7b648cf5917f5c6e5c3b2b06041fde0784d8:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/SOURCE_INDEX.json
- D004 结果与处置：daowei2026/observe-iterate@4fddedfecbdde8bfb64ac86e06748b30ebb5c03b:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/report/RESULT.json；daowei2026/observe-iterate@3ce7f51cc84d86b081107712a5f092c7542de5f4:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/report/RESEARCH_DISPOSITION.csv
- D004 冻结完整性入口：daowei2026/observe-iterate@04085a7fd63143509c88a574a36c6621b6ae28d5:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/ARTIFACT_INDEX.json；daowei2026/observe-iterate@468a4c4cb72c7b1754ce3b5b70e03ca1ee793a78:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0007/report/LOCAL_VERIFICATION.json
- N1 报告/证据：daowei2026/observe-iterate@83abc94304fe4f00419848a2010a143946011ca2:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EXECUTOR_REPORT.md；daowei2026/observe-iterate@77f11f6e5ea4de5ad9e0be1caa3d1312bf4e84c3:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EVIDENCE_INDEX.md
- N2 报告/证据/来源：daowei2026/observe-iterate@fb278b545bdfb21311dc8b40a41287436bcaf975:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/EXECUTOR_REPORT.md；daowei2026/observe-iterate@8daeaa2906a1a138ce204057747358a31ecf62c8:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/EVIDENCE_INDEX.md；daowei2026/observe-iterate@70a8d15514ec63149ae9d5592fbe48ed47b065ee:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/SOURCE_INDEX.json
- C0007 本地研究根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261126-01/calls/C0007/`；主控 exact 副本 `/dwdhome/fy/cgpterm/artifacts/eaw-discovery-controller-20261126/verified-C0007/`。
- 新只读数据根：`/home/dw/.codex/visualizations/2026/11/16/01a1e335-cd15-7f72-a7d9-f53c52feb09e/gallery/steel-ticks-qt-20261126/`；入口定位/原数据 Chat 以 Owner 恢复及 C0007 SOURCE_INDEX 为准，Chat 只读。

固定协议/角色/方法采用 observe-iterate@ff45aab0c8e66e4feb552b2c8a632210d9b58b56；controller Skill 为 cgpterm@0f029333a7fc4b568b5e49a77a5c8ab185baa336。协议、执行指南和方法准确 refs 在本 D JSON input_refs；E1 已实际读过且仍适用的原件可复用，实际需要的新增/变化内容亲读。

## 权限、发布和运输

Owner 原 grant：
`operation=eaw-business-discovery-research-and-publish execution_context=/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2,daowei2026/observe-iterate:feat/statistics-driven-feature-closure-v0.3-20261122:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/`

仅使用该 operation 和两项 allowed_writes；Personal 连接 link_6ab37f74c7288191a52eb23d2ca1e2c8。已有 Git 文件用当前 blob SHA 条件更新，冲突先重读；不并行写。E1 的必要成果与真实 V2 Return 在获准本 Run 前缀发布并 exact 回读后，明确交回 Git 写任务，无在途/UNKNOWN 写。Registry/主控 Chat 归档由 controller 维护。规范 business_control 双进度由 Manager 消费后更新，E1 可提供实际业务摘要。

本 D 由 Manager 正式签发；此处不声称物理派达。controller 核 C0008 真实回交和物理 turn 结束、单写者及授权后，仅原路派给原 E1。无 Workers、无借用线程。
