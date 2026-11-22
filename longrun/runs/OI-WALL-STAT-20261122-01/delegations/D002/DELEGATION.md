# D002｜WALL 正式结果绑定与全量行为统计

- `run_id / delegation_id / issuer_call_id`：`OI-WALL-STAT-20261122-01 / D002 / C0003`
- `work_id / business_case_id`：`OI-WALL-STAT-20261122 / WALL-STATISTICS-CLOSURE`
- `issuer / return_to`：`codex:OI-WALL-STAT-20261122-01:manager`
- `recipient`：本 Run 已回交过 D001 的 `codex:OI-WALL-STAT-20261122-01:executor:E1`
- `work_item_id`：`WALL-X-G-CURRENT`；采用 L0 的 `WALL-X-01 → WALL-G-01`。
- profile：`CODEX_NATIVE_DIRECT`；`workers=[]`；不签 W，物理送达由 controller 核实。

本项 Skill 工作为 G：

`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/feature-global-behavior-profiling/SKILL.md`

按该原件读取同目录、同提交的 `WORKFLOW.md`、`IO_SPEC.md`，采用补充：

`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md`

先履行既定 L0 X，取得本 Run 正式 `FeatureRunResultBinding`，随后连续执行上述 G；X 是实际动作，不是新增 Skill。X 的正式执行授权见同目录 `EXECUTION_AUTHORIZATION.md`，机器操作及写面以本 D 的原 V2 JSON 和原 Binding 为准。X/G 的依赖、输入就绪判断、专业方法和完成条件均取原件：

`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md`

单份业务输入及正式代码、默认参数、rb/m、2021 全年、Calendar 和工作区全部继续锁定：

`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:task-inputs/wall-f-parallel-closure-20261122/WALL_BASE_RUN_INPUT.md`

最新 Owner 继续指令为下列已发布原件中逐字保留的 Owner 段，尤其是第 1—3、5—6 项：

`daowei2026/observe-iterate@64469aed9f7205736ac33ea17d38552226c39742:longrun/runs/OI-WALL-STAT-20261122-01/calls/C0003/FULL_ASSIGNMENT.md`

当前已消费的上游输入：

- 真实 executor Return：`daowei2026/observe-iterate@b30d4423e1531e07405558350a3be184afda2788:longrun/runs/OI-WALL-STAT-20261122-01/calls/C0002/PRO_RETURN.json`
- 理解包：`daowei2026/observe-iterate@b6df1743e44ac0447cfa0ec3c6bcbbf0ce8544d3:longrun/runs/OI-WALL-STAT-20261122-01/artifacts/D001/FEATURE_UNDERSTANDING_PACKAGE.md`
- 同提交 C0002 的 `checks/LOCKED_SOURCE_OBSERVATION.json`、`checks/DECLARED_DEFAULT_PARAMETERS.json` 是既有观察和静态默认值证据，不冒充实际加载或 ppdict 读回。

manager 已按最新 Owner 的本轮最小核对范围接收 D001 已完成内容；原包的 `PARTIAL`、原 Return 的 `IN_PROGRESS` 和 U-C1..5 具名缺口均保留。按包第 8 节可用范围进入 X；加载／参数／输入处理和物化读回缺口随 X 的绑定及 G 的原生输入就绪工作取得证据，不重复整套 Feature Understanding。

输出直接采用 L0 X 的 `FeatureRunResultBinding` 和 G Skill 的原生输出合同。以原 D002 身份通过 V2 PRO_RETURN 回交原 manager，附已完成范围、真实结果和剩余范围；进度按最新 Owner 第 6 项分别报告。当前只签发工作，不声明 X、生产进程、结果复用或 G 已发生。
