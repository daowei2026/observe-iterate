# D002｜B Skill 工作委派：PostTurnGroupDirectionalOrganizationFrp 观察位置准备

本 D 仅绑定一次具体 Skill 工作与已经存在的输入，不重新规定专业方法、业务预期、展示方案、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-Q-OBS-20261120-01`
- `delegation_id`：`D002`
- `issuer_call_id`：`C0004`
- `issuer`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `recipient`：`chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `parent_task_id / work_id`：`OI-U2-Q-OBS`
- `business_case_id`：`U2-FQV-Q`
- `work_item_id`：`OI-U2-Q-OBS-20261120-01-WI-B`
- `stage_instance_id`：`OI-U2-Q-OBS-20261120-01-M-B`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/SKILL.md`
- 当前用法说明：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/IO_SPEC.md`
- 高频多尺度参考：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md`

本项专业工作由接收者亲自完整读取并采用上述 Skill 原件。

## 3. 外层任务已经提供的事实

- 本次特征名称：`PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织）。
- 特征代码版本：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；正常 Python 包装与实例构造版本：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次特征实例：在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下，按已给 `make_features(...)` 完整参数构造后，只取返回的第二项 `q`；对象为 `rb / hc / i`，尺度为 `5m`，方向为 `up`。完整构造和参数以第 4 节所列精确原件为准，不以本段摘要替代。
- `q` 经 `PostTurnGroupDirectionalOrganizationFrp.from_formation(f, ...)` 从准确 F 与原价／Calendar 输入构造。F 只作为 Q 的必要上游依赖；本 Run 不执行 F 的独立 A～E，也不把 F 历史阶段成果或现有 uplot 例外计入 Q。
- 唯一 Q 业务输入没有额外指定 B 的品种集、时间范围或样例位置；B 应消费本次实例、A 当前有效产物和自身完整 Skill 原件形成本阶段结果。
- 本 Run 完整范围为 Q 的观察材料准备 A～E，并以 Q 的 E 交付结束；V、合理性分析、S/U2/U3、参数标定、收益判断、资金配置及未经授权的全历史 producer 重跑不在范围内。
- Owner 确认的实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。所有本 Run 新业务产物与记录仅写 `longrun/runs/OI-U2-Q-OBS-20261120-01/**`；本 B Skill 当前没有 Worker 工单。

## 4. 当前输入与适用原始文件

### 4.1 Run、Workflow 与业务输入

- Owner GO：`daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json`
- F 完成与 Q 不继承阶段成果／uplot 例外的记录：`daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/F_COMPLETION_HANDOVER.json`
- 外层 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md`
- 唯一 Q 业务输入：`daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md`
- C0004 原任务：`daowei2026/observe-iterate@b589218bfe431b9fde7d350c86b8092492ef2fc1:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0004/FULL_ASSIGNMENT.md`
- C0004 Invocation：`daowei2026/observe-iterate@b9cf27e08cfa14c56380dac263979d0f5fcc8848:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0004/INVOCATION.json`

### 4.2 本次实例原件

- 本批实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- Q Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs`
- Q Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py`

### 4.3 A 当前有效专业产物

- 原 D001：`daowei2026/observe-iterate@2944f650baf779308fcc7fa92d20c6b0b4ca0e71:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D001/DELEGATION.json`
- C0002 合法 executor Return：`daowei2026/observe-iterate@06b3f5d12218004bfc37c828866d6066e475ae84:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PRO_RETURN.json`
- C0003 同源格式补正 Return：`daowei2026/observe-iterate@9ffe7977837c99ddc26549164f33c9c738f68b64:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0003/PRO_RETURN.json`
- A 完整专业报告：`daowei2026/observe-iterate@23aab75c3415fe247e91f78a4079dfc8a80bfa57:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PROFESSIONAL_REPORT.md`
- 同源格式补正说明：`daowei2026/observe-iterate@46e78c7f1a3a71f4491a0154dfc91e0adefc00d3:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0003/FORMAT_CORRECTION.md`
- A 人读原生产物：`daowei2026/observe-iterate@bf50bbe5c9447cb992af547e3f5f95f7465cae88:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- A 机读原生产物：`daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

A 已按原生 Skill 报告完整，D001 无剩余续作。其当前有效边界包括：Q 的业务主输出为 `DirectionalOccurrence` 与显式生命周期收口 `DirectionalDutyEnd`；一版 Q occurrence 对应一个 F candidate Life 的完整组观点并保存 Q 自身 `Life / Revision / Previous` 与准确 F candidate 引用；成员记录只是该 Q occurrence 的嵌套 payload；Q 的正式发表 firing、`directionalKnown`、成员 Turn actual／confirmation／known、endpoint 与 Calendar 位置不得混同；无新 Q occurrence 不等于失败或责任结束。完整事实以所列两份 A 原生产物为准。

原 C0002 错误形状 Return 的不可变历史引用为 `daowei2026/observe-iterate@37548df36c05344854d2d6b2efe8ea94640323cf:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PRO_RETURN.json`；该历史只用于协议追溯，不改变 A 专业成果，也不构成另一业务阶段。

## 5. 已有上游真实产物

A 阶段已经形成本 Run 当前有效的 `FEATURE_OCCURRENCE_UNDERSTANDING.md` 与同源机读 JSON，可供本 B Skill 消费。C、D、E 尚无本 Run 已完成专业产物；没有已发或已接受的 Worker 工单／回交。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 B Skill 的原生合同，不另设最小证据、专业验收或 Worker 返回处理要求。
- 实际回交对象：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`；回交时保持 `work_item_id=OI-U2-Q-OBS-20261120-01-WI-B`、`stage_instance_id=OI-U2-Q-OBS-20261120-01-M-B` 和 `delegation_id=D002`。
- 一次调用不足以完成本项 Skill 时，继续原 `D002` 与原工作项，并引用已经形成的真实产物和当前续接点。
