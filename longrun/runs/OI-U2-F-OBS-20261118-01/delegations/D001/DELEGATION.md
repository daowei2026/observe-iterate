# D001｜A Skill 工作委派：CommonPriceTurnGroupCandidatesFrp occurrence 理解

本 D 仅绑定一次具体 Skill 工作与已经存在的输入，不重新规定专业方法、业务预期、展示方案、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `delegation_id`：`D001`
- `issuer_call_id`：`C0001`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `recipient`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `parent_task_id / work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-A`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-A`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md`
- 内部 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/IO_SPEC.md`

本项专业工作由接收者亲自完整读取并采用上述 Skill 原件。

## 3. 外层任务已经提供的事实

- 本次特征名称：`CommonPriceTurnGroupCandidatesFrp`（F）。
- 特征代码版本：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；正常 Python 包装与实例构造版本：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次特征实例：在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下，按已给 `make_features(...)` 完整参数构造后，只取返回的第一项 `f`；对象为 `rb / hc / i`，尺度为 `5m`。完整构造和参数以本节下列精确原件为准，不以本段摘要替代。
- 本 Run 完整范围为观察材料准备 A～E，并以 E 交付结束；Q、V 和合理性分析不在本 Run 范围内。历史产物不作为本 Run 已完成的 A～E 结果；输入排除的全历史 producer 重跑不在本项工作内。
- 经 Owner 更正并由资源绑定核实的实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。本 A Skill 当前没有 Worker 工单。

## 4. 当前输入与适用原始文件

### 4.1 Run 与业务输入

- Owner GO 与工作区更正：`daowei2026/observe-iterate@74ed0b11552f73b03e55e3e324f8325889730b52:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- C0001 原任务：`daowei2026/observe-iterate@261530be6662e60a71bccc89c658819d69b2755a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0001/FULL_ASSIGNMENT.md`
- 唯一业务输入：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`

### 4.2 实例构造与代码原件

- 本 Run 的实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- F 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- F 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

## 5. 已有上游真实产物

无。本 D 是本 Run 首项 Skill 工作；截至签发时，A～E 均没有本 Run 的已完成专业产物，也没有已发 Worker 工单。上述历史材料和源码只作为本项输入与证据来源，不作为 A 已完成结果。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 A Skill 的原生合同，不另设最小证据、专业验收或 Worker 返回处理要求。
- 实际回交对象：`chatgpt:OI-U2-F-OBS-20261118-01:manager`；回交时保持 `work_item_id=OI-U2-F-OBS-20261118-01-WI-A`、`stage_instance_id=OI-U2-F-OBS-20261118-01-M-A` 和 `delegation_id=D001`。
- 一次调用不足以完成本项 Skill 时，继续原 `D001` 与原工作项，并引用已经形成的真实产物和当前续接点。
