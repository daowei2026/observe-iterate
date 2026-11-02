# 方法探索期：目标、管理实践与运行接续

本指南负责当前探索期的管理适配和运行接线，不取代业务来源：[00 最终投资业务目的](../../professional/exploration/00_BUSINESS_OBJECTIVE.md)、[06 当前长程任务直接目标](../../professional/exploration/06_EXPLORATION_STAGE_GOAL.md)、[05 Owner 完整初版过程](../../professional/exploration/05_OWNER_PROCESS_EXPLANATION.md)。[02 摘要](../../professional/exploration/02_CURRENT_WORKING_IDEAS.md) 不替代 05。

## 一、本任务的 Management Pro

当前首先要**组织 Owner 初版用例形成方式的真实实践，并根据专业实践迭代这一方式**。Management Pro 不能仅从最终选品种目标重新选一项容易验证的业务问题，而未说明为何偏离 Owner 已有做事过程。它负责恢复完整背景、确认已成/未完与依赖、安排具体专业实践、接收结果、判断实践得失、成本收益及下一轮。Professional Pro 负责真实特征与市场过程观察、初版用例、候选规律、反例及方法反馈，不应由管理在派发前替其做未经授权的新业务研究。

Owner 的 05 是当前**优先实践的初版设想**，尚非已验证的规律、两层固定 Gate 或唯一永恒框架。若真实结果指出原设想不适用，可以提出不同安排。管理应在有新增内容时明确区分：Owner 已有认识、已核实事实、Professional 的新发现与待证假说、Management 自己新增的解释和建议、需要 Owner 检查或决定的内容。重要新增分析要呈现 Owner；实质替换研究问题、主要过程和方向前先确认。不受影响的正常工作继续；Owner 不逐项审批普通取数、画图与可逆具体化。

## 二、动态管理工作面

新 Run 的动态成果统一放在 `runs/<RUN_ID>/`：

- `README.md`：Owner 阅读入口；
- `00_长程推进地图.md`：目的、原设想实践进展、已成成果、重要未完和下一责任；
- `01_当前任务.md`：本轮具体工作、与 Owner 初版过程的关系、实际输入/交付/授权；
- `reviews/management-Rxxxx/DECISION.md`：管理判断、真实反馈、重要新增分析、Owner 事项及后继；
- `reviews/WORKMAP_INTAKE_CURRENT.json` 和 `provenance/turns/Rxxxx/`：真实采用与身份/回交。

实际变化才更新地图、任务，不强制每次复看重复修改。专业背景仍在 `professional/exploration/`，不另建 `current_work`、`CURRENT_EXECUTION`、`TASK_ROUTER` 或平行的动态管理状态。

## 三、新 Run、数据和工具

稳定 `work_id=BI-01`、当前 `CASE_OBSERVATION`；真实新 Run 身份、Owner GO、当前专业任务、Binding/Intake 在启动时单独建立。旧 CO-01—04 的任务、Reader PASS、预算、在途和结论不自动继承；准确的历史工具和数据知识可定向复用，但不能冒充本 Run 的数据资格或现行决定。

首次应用当前特征时，按实际需要核品种、时间、尺度、方向、actual/confirm、转折点、线段和发展中部分；工具知识直接参考 [03](../../professional/exploration/03_TOOLING_AND_DATA_USAGE.md) 与已走通实践，勿无目的重新摸索所有接口。遇到历史事件首次可知性未完全实现，诚实限制相应结论，不默认把全面可见性工程作为初版观察的全部前置。数据/图到位也不自动启动任务。

新 Run 仍按 M-START/BOOTSTRAP、Workmap/Binding/Intake 与现行派发机制，依据真实 Owner GO 和 exact 版本执行。Binding 实际状态以采用版本文件为准，不将一条旧运行指南中的状态文字当作实时事实。主控只搬运已有权任务和真实发送状态，不代管理 Pro 选业务题。

## 四、Workmap Reader 与业务 Reviewer

Owner 已授权本次探索的**首次 Workmap Reader 不作为固定前置**。Management 首次建立真实地图、任务、采用决定和 Intake 后，可在适用 v2 Binding 明确采用 `reader_policy.mode=OWNER_OPTIONAL`、真实 Owner 来源及其 `NOT_REQUIRED` 理由时，不额外派独立 Reader，而直接执行所有原有机械检查和合法 Professional 派发。不能仅在派发里写 `requires_reader_check=false` 就假装已授权；也不能把 `NOT_REQUIRED` 记作 Reader PASS。

Owner 特别要求、主要研究意图严重分歧或高影响地图变化时，仍可签真实独立 Reader，其实际派发、冻结对象、回交和管理接收按原合同完成。业务成果的独立 Reviewer Pro 也按重要程度、具体可复核内容和投入收益选择，普通初版实践不默认每轮增加。已签必须审查的工作不能因本段自动豁免。

不取消管理 Intake、地图/任务与来源指纹、`INTAKE_STALE`、正式方法/任务资格、实际发送观察、双 Return、已签审查资格或重复发送保护。只移除未经必要性判断的默认额外 Pro 回合。

## 五、真实实践、反馈与迭代

Manager 优先组织 Professional 实践 05 的实际过程：沿时点可知信息寻找并观察大尺度共同背景如何形成/改变，检查中尺度贴近转折及线段是否有结构，再深入观察具体差异、形成用例和候选规律；依据实际发现可以往返、局部调整，不是逐项 Gate。

接收时同时核实际业务内容及原设想实践得失，明确新发现、新解释、限制、需补证据以及向 Owner 提交的修改建议。不能用“完成一个固定 T 的候选/无候选判断”、图可读或技术 PASS 冒充这套形成过程已走通。投资前瞻价值仍是重要目的，已有依据时应尝试后续判断与验证，不应无限停留于事后描述。

运行派发、管理触发、原专业续作和 Worker 返回沿现有 DR13/DR14、Overlay08/12/13 执行；不自行增设两道 Gate、固定产出数量、常驻 Reviewer 或专用 Agent。
