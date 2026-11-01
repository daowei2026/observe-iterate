# 方法探索期：准备与实际运行接续

本指南只负责运行接线，不定义固定专业方法，也不是Owner GO。当前专业项目入口见 [professional](../../professional/README.md)；背景与当前设想见 [exploration](../../professional/exploration/README.md)；当前任务准备稿见 [TASK_001](../../professional/current_work/TASK_001.md)。

## 1. 持续运行职责

Owner提供整体业务意图、反馈和授权；Management Pro持续理解探索背景、历史实践及当前输入，决定并派发下一项具体专业工作；Professional Pro按本轮真实委派执行并交付；Management Pro消化结果、更新认识并安排下一轮。当前方法尚在摸索，不要求每轮重复固定流程，也不把探索说明直接视为任务授权。

## 2. 新旧隔离与复用

- 专业及运行仓：`daowei2026/observe-iterate@fy/feature-based-case-observation`；启动时锁定实际完成提交。
- 操作仓：复用既有有权cgpterm环境及工具；现场checkout、Skill和实际权限以记录为准。
- 稳定work_id为BI-01，继续使用CASE_OBSERVATION模式；每个真实Run独立身份。
- 设备、Worker、调度、身份、发送收取和回交协议按原机制复用；不因换方法扩大权限或隐藏仍在途的旧动作。
- 旧CO-01、GO、管理决定、预算、R序列、接收、等待和未完图面责任不复制到新Run，也不宣告旧Run已完成或停止。

## 3. 数据到齐后的必要准备

先核本次正式特征交付、品种/范围、尺度配置、方向字段、实际点/确认点、线段和当前部分语义，以及图数入口。首次画图的Owner设想和aidata使用参考见 [工具数据说明](../../professional/exploration/03_TOOLING_AND_DATA_USAGE.md)。已适用的正式交付和core可复用；只补本轮实际缺少的内容，不重跑全套环境测试、不默认旧参数。

当前TASK_001是准备稿。数据到齐后由Management Pro补入真实输入、业务问题、角色责任、Run身份及交付范围，再按既有M-START/BOOTSTRAP、Workmap/Binding/Intake机制办理真实Owner授权和管理采用。不得从旧Run复制已采用状态。提交或数据到齐不自动启动。

## 4. 多轮探索

每轮任务由管理结合最新成果具体安排。专业者可在授权范围内修正当前设想、形成业务发现；重大业务范围或权限变化回管理处理。Worker只处理有明确必要的取数、图面或字段工作，结果回原签发Pro消费。管理复看关注是否推进特征对象理解、现象辨认、候选规律和后续品种判断，而非只检查流程文件、数据取得或图能打开。

只有多轮实践证明方法稳定后，才考虑固化专业规范或专用Agent。旧故障按本次是否实际依赖判断，不自动继承阻塞，也不假称已经恢复。
