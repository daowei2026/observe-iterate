# D001｜A Skill 工作委派：PostTurnGroupDirectionalOrganizationFrp occurrence 理解

本 D 仅绑定一次具体 Skill 工作与已经存在的输入，不重新规定专业方法、业务预期、展示方案、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-Q-OBS-20261120-01`
- `delegation_id`：`D001`
- `issuer_call_id`：`C0001`
- `issuer`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `recipient`：`chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `parent_task_id / work_id`：`OI-U2-Q-OBS`
- `business_case_id`：`U2-FQV-Q`
- `work_item_id`：`OI-U2-Q-OBS-20261120-01-WI-A`
- `stage_instance_id`：`OI-U2-Q-OBS-20261120-01-M-A`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md`
- 内部 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/IO_SPEC.md`

本项专业工作由接收者亲自完整读取并采用上述 Skill 原件。

## 3. 外层任务已经提供的事实

- 本次特征名称：`PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织）。
- 特征代码版本：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；正常 Python 包装与实例构造版本：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次特征实例：在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下，按已给 `make_features(...)` 完整参数构造后，只取返回的第二项 `q`；其类型应为 `PostTurnGroupDirectionalOrganizationFrp`，对象为 `rb / hc / i`，尺度为 `5m`。完整构造和参数以本节下列精确原件为准，不以本段摘要替代。
- `q` 由准确的 `f` 经 `PostTurnGroupDirectionalOrganizationFrp.from_formation(f, ...)` 构造。F 只作为 Q 的必要上游依赖；本 Run 不执行 F 的独立 A～E，不把 F 历史交付或阶段成果计入 Q 的完成范围，也不把 F 输出冒充 Q 主输出。
- F 的独立 Run 已由 Owner 记录为 `DATA_READY`；该事实只说明当前顺序使用的工作区背景，不构成本 Run 的 Q 阶段产物。F 的现有 uplot 运行例外不自动授予 Q。
- 本 Run 完整范围为 Q 的观察材料准备 A～E，并以 Q 的 E 交付结束；V、合理性分析、S/U2/U3、参数标定、收益判断、资金配置及未经授权的全历史 producer 重跑不在范围内。
- Owner 确认的本 Run Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。所有本 Run 新业务产物和运行记录写入 `longrun/runs/OI-U2-Q-OBS-20261120-01/**`；本 A Skill 当前没有 Worker 工单。

## 4. 当前输入与适用原始文件

### 4.1 Run 与业务输入

- Owner GO：`daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json`
- F 完成与 Q 不继承阶段成果／uplot 例外的记录：`daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/F_COMPLETION_HANDOVER.json`
- C0001 原任务：`daowei2026/observe-iterate@e903bcd0192a892d9b64d0ba9a9310234e40879d:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0001/FULL_ASSIGNMENT.md`
- C0001 Invocation：`daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0001/INVOCATION.json`
- 唯一 Q 业务输入：`daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md`

### 4.2 实例构造、Q 实现与 F→Q 输入合同原件

- 本批实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- Q 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs`
- Q 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py`
- 必要上游 F 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- 必要上游 F 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

## 5. 已有上游真实产物

本 Run 的 Q A～E 均无已完成专业产物。本 D 是本 Run 首项 Skill 工作；截至签发时，没有 Q 的阶段产物，也没有已发 Worker 工单。F 的完成记录、历史结果、源码及索引仅作为 Q 必要上游关系和代码／实例定位来源，不作为 Q 的 A 阶段完成结果。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 A Skill 的原生合同，不另设最小证据、专业验收或 Worker 返回处理要求。
- 实际回交对象：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`；回交时保持 `work_item_id=OI-U2-Q-OBS-20261120-01-WI-A`、`stage_instance_id=OI-U2-Q-OBS-20261120-01-M-A` 和 `delegation_id=D001`。
- 一次调用不足以完成本项 Skill 时，继续原 `D001` 与原工作项，并引用已经形成的真实产物和当前续接点。
