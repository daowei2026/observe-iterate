# 方法探索期：准备与实际运行接续

本指南只负责运行接线，不定义固定专业方法，也不是Owner GO。专业背景见 professional/README.md；探索材料见 professional/exploration/README.md。

## 1. 持续运行职责与唯一管理工作面

Owner提供整体业务意图、反馈和授权；Management Pro持续理解探索背景、历史实践及当前输入，决定并派发下一项具体专业工作；Professional Pro按本轮真实委派执行并交付；Management Pro消化结果、更新认识并安排下一轮。当前方法尚在摸索，不要求每轮重复固定流程，也不把探索说明直接视为任务授权。

**动态管理工作面统一位于当前Run的 runs/<RUN_ID>/：**
- 每轮管理判断和安排记录在 reviews/management-Rxxxx/DECISION.md，并按原协议形成管理回交。
- 00_长程推进地图.md持续表达整体目标、真实成果、重要剩余和后继。
- 01_当前任务.md表达当前正式任务及其完整范围、输入、交付和授权。
- README.md提供Owner查看入口；provenance/turns/Rxxxx/保存正式身份及回交记录。

Management Pro依据真实变化维护地图和当前任务，不要求每次管理调用都机械修改它们；若只是复看且整体状态/当前任务没有改变，可只记录本轮DECISION及回交。**不在professional目录另建current_work、CURRENT_EXECUTION或TASK_ROUTER来重复维护任务、进度或路由。** 通用角色路由、管理职责、接收、去重和回交格式沿现有运行协议执行，本次不另建一套。

## 2. 新旧隔离与复用

- 专业及运行仓：daowei2026/observe-iterate@fy/feature-based-case-observation；启动时锁定实际完成提交。
- 操作仓：复用既有有权cgpterm环境及工具；现场checkout、Skill和实际权限以记录为准。
- 稳定work_id为BI-01，继续使用CASE_OBSERVATION模式；每个真实Run独立身份。模式名不代表固定的两层研究Gate。
- 设备、Worker、调度、身份、发送收取和回交协议按原机制复用；不因换方法扩大权限或隐藏仍在途的旧动作。
- 旧CO-01、GO、管理决定、预算、R序列、接收、等待和未完图面责任不复制到新Run，也不宣告旧Run已完成或停止。

## 3. 数据到齐后的必要准备

先核本次正式特征交付、品种/范围、尺度配置、方向字段、实际点/确认点、线段和当前部分语义，以及图数入口。首次画图的Owner设想和aidata使用参考见 professional/exploration/03_TOOLING_AND_DATA_USAGE.md。已适用的正式交付和core可复用；只补本轮实际缺少的内容，不重跑全套环境测试、不默认旧参数。

Management Pro将真实输入、当前业务问题、责任角色及交付范围纳入本Run的正式管理任务；数据到齐本身不自动派发或启动。按既有M-START/BOOTSTRAP、Workmap/Binding/Intake机制办理真实Owner授权和管理采用，不从旧Run复制已采用状态。

runtime/config/WORKMAP_BINDING.json目前为NOT_CONFIGURED准备状态。真实采用时由有权管理按本次准确来源填入独立Run身份；owner_sources、rule_paths指向本分支探索背景、真实Run任务及现有运行协议，不引用professional下的平行任务文件。原工具要求的任务、快照、Intake和校验真实完成后才可ADOPTED。

bi01_run_gate.py显式传真实 --run-id；非默认Binding同时传 --binding，与workmap_gate的snapshot/check/dispatch使用同一来源。保留原独立审查条件，不因本次探索省略应有资格，也不把当前工作设想升级为额外Reader前置。

主控只装配有权任务、发送收取和记录，不代写业务场景；专业者实际读取本轮承重材料和数据。GitHub全文与手机短指引、两份Return及去重继续沿既有合同；不因分支创建重新安装所有依赖。

## 4. 多轮探索与管理接续

每轮由Management Pro结合Owner最新反馈、探索背景、当前Run地图和前轮真实成果，判断下一项最值得做的专业工作。当前同向大尺度背景、中尺度观察及两层过程只是可供本轮采用或修正的设想，不要求每轮都完整重复，也不把“先第一层通过、再第二层通过”固化成Gate。

Professional Pro可在正式授权范围内开展实际特征观察、提出和修正业务设想、报告工具或数据缺口；必要技术工作由原签发Pro按现有机制委派Worker，结果先回原签发者消费。Owner可随时看图交流，反馈按现有任务修订和管理机制处理。管理复看关注真实业务发现、候选规律、当时可知信息、后续品种判断及其修订，不以流程文件、数据取得或图能打开代替业务进展。

如果当前设想受阻，管理应根据实际发现安排继续、修正或换框架；不无限润色不成立的设想，也不自动扩成全面场景分类、平台建设或专用Agent。多轮实践证明某些做法稳定有效后，再考虑固定专业规范或Agent。

有权主体决定实际启动和后继。数据到齐、文档提交或工具准备完成都不自动构成GO。旧故障按本次是否实际依赖判断，不自动继承阻塞，也不假称已经恢复。
