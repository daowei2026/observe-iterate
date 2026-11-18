# D002｜B Skill 工作委派：CommonPriceTurnGroupCandidatesFrp 观察位置准备

本 D 仅绑定一次具体 Skill 工作与已经存在的输入，不重新规定专业方法、业务预期、展示方案、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `delegation_id`：`D002`
- `issuer_call_id`：`C0004`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `recipient`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `parent_task_id / work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-B`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-B`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/SKILL.md`
- 当前用法说明：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/IO_SPEC.md`
- 高频多尺度参考：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md`

本项专业工作由接收者亲自完整读取并采用上述 Skill 原件。

## 3. 外层任务已经提供的事实

- 本次特征名称：`CommonPriceTurnGroupCandidatesFrp`（F）。
- 特征代码版本：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；正常 Python 包装与实例构造版本：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次特征实例：在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下，按已给 `make_features(...)` 完整参数构造后，只取返回的第一项 `f`；对象为 `rb / hc / i`，尺度为 `5m`。完整构造和参数以第 4 节所列精确原件为准，不以本段摘要替代。
- 唯一业务输入没有额外指定 B 的品种集、时间范围或样例位置；B 应消费本次实例、A 当前有效产物和自身完整 Skill 原件形成本阶段结果。
- 本 Run 完整范围为观察材料准备 A～E，并以 E 交付结束；Q、V、合理性分析及输入排除的全历史 producer 重跑不在范围内。
- 经 Owner 更正并由资源绑定核实的实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。本 B Skill 当前没有 Worker 工单。

## 4. 当前输入与适用原始文件

### 4.1 Run、Workflow 与业务输入

- Owner GO 与工作区更正：`daowei2026/observe-iterate@74ed0b11552f73b03e55e3e324f8325889730b52:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 外层 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md`
- 唯一业务输入：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- C0004 原任务：`daowei2026/observe-iterate@4f057b74dd7e7bcc3f9336ed39ca760a4fb30264:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0004/FULL_ASSIGNMENT.md`

### 4.2 本次实例原件

- 本 Run 的实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`

### 4.3 A 当前有效专业产物

- D001：`daowei2026/observe-iterate@d1ef9eda82e6dd536959fde76e445d635430ded9:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D001/DELEGATION.json`
- C0003 Invocation：`daowei2026/observe-iterate@937bb43a2ad4e8b959d0dc80725545c2f3ad96a4:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0003/INVOCATION.json`
- C0003 executor Return：`daowei2026/observe-iterate@d57377780714f737961fd6e8487f5eaf38ea0889:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0003/PRO_RETURN.json`
- A 完整专业报告：`daowei2026/observe-iterate@01fd95ac2af9585eb051af6548fc6163f52a4311:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0003/PROFESSIONAL_REPORT.md`
- A 原生产物：`daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`

A 已按原生 Skill 报告完整，D001 无剩余续作。其当前有效边界包括：F 的主 occurrence 是候选 Life 的新 revision；业务发表／可知位置使用 `groupKnownFrom`；成员 actual、confirmation、known 与候选 known 不得混同；当前公开读取接口未暴露 `groupFormationParticipation` 嵌套字段。完整事实以所列 A 原生产物为准。

## 5. 已有上游真实产物

A 阶段已经形成本 Run 当前有效的 `FEATURE_OCCURRENCE_UNDERSTANDING.md`，可供本 B Skill 消费。B、C 之外的 D、E 尚无本 Run 已完成专业产物；没有已发 Worker 工单。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 B Skill 的原生合同，不另设最小证据、专业验收或 Worker 返回处理要求。
- 实际回交对象：`chatgpt:OI-U2-F-OBS-20261118-01:manager`；回交时保持 `work_item_id=OI-U2-F-OBS-20261118-01-WI-B`、`stage_instance_id=OI-U2-F-OBS-20261118-01-M-B` 和 `delegation_id=D002`。
- 一次调用不足以完成本项 Skill 时，继续原 `D002` 与原工作项，并引用已经形成的真实产物和当前续接点。
