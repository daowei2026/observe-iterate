# D003｜C Skill 工作委派：CommonPriceTurnGroupCandidatesFrp 展示方式准备

本 D 仅绑定一次具体 Skill 工作与已经存在的真实输入和产物，不重新规定专业方法、业务预期、展示方案、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `delegation_id`：`D003`
- `issuer_call_id`：`C0006`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `recipient`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `parent_task_id / work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-C`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-C`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/SKILL.md`
- 内部 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/IO_SPEC.md`

本项专业工作由接收者亲自完整读取并采用上述 Skill 原件。

## 3. 外层任务已经提供的事实

- 本次特征名称：`CommonPriceTurnGroupCandidatesFrp`（F）。
- 特征代码版本：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；正常 Python 包装与实例构造版本：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次特征实例：在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下，按已给 `make_features(...)` 完整参数构造后，只取返回的第一项 `f`；对象为 `rb / hc / i`，源尺度为 `5m`。完整构造和参数以第 4 节所列精确原件为准，不以本段摘要替代。
- 本 Run 完整范围为观察材料准备 A～E，并以 E 交付结束；Q、V、合理性分析、历史成果预接受及输入排除的全历史 producer 重跑不在范围内。
- 经 Owner 更正并由资源绑定核实的实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。当前第二 executor 和 Worker 尚未物理绑定。

## 4. 当前输入与适用原始文件

### 4.1 Run、Workflow 与业务输入

- Owner GO 与工作区更正：`daowei2026/observe-iterate@74ed0b11552f73b03e55e3e324f8325889730b52:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 外层 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md`
- 唯一业务输入：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- C0006 原任务：`daowei2026/observe-iterate@2b27f96a60442f415a27031f0cd9bf9ca315b2fa:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0006/FULL_ASSIGNMENT.md`
- C0006 Invocation：`daowei2026/observe-iterate@0871e3e654e2aaa5e0c7e10d85ba73c2b26be605:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0006/INVOCATION.json`

### 4.2 本次实例原件

- 本 Run 的实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- F 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- F 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

### 4.3 A 当前有效专业产物

- D001：`daowei2026/observe-iterate@d1ef9eda82e6dd536959fde76e445d635430ded9:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D001/DELEGATION.json`
- C0003 executor Return：`daowei2026/observe-iterate@d57377780714f737961fd6e8487f5eaf38ea0889:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0003/PRO_RETURN.json`
- A 完整专业报告：`daowei2026/observe-iterate@01fd95ac2af9585eb051af6548fc6163f52a4311:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0003/PROFESSIONAL_REPORT.md`
- A 原生产物：`daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`

### 4.4 B 当前有效专业产物

- D002：`daowei2026/observe-iterate@b543f4b91482716577ebc0b59f786b5ab45aba61:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D002/DELEGATION.json`
- C0005 Invocation：`daowei2026/observe-iterate@9a9fe93805193df4a2e9b93625b68f41d365719a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0005/INVOCATION.json`
- C0005 executor Return：`daowei2026/observe-iterate@f4f82a780b7549f56b78f4b76e8f784532baf655:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0005/PRO_RETURN.json`
- B 完整专业报告：`daowei2026/observe-iterate@3b7483b13eb25bb68a6b6955e3c63a1d996061df:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0005/PROFESSIONAL_REPORT.md`
- B 原生产物：`daowei2026/observe-iterate@6f1ee9eb4595254845d3b228a146ad68cabc64e0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`

B 已按原生 Skill 报告完整，D002 无剩余续作。其当前有效位置记录为 `OI-U2-F-OBS-20261118-01-B-POS-001`；该记录继续保留给后续 D 阶段正式绑定。C 阶段对 B 最终位置的处理边界直接遵循第 2 节所列 C Skill 原件。

### 4.5 锁定 CAEGraph 原件

- 使用手册：`daowei2026/uplot@e6.2:CAEGraph使用手册.md`
- 手册不足时所需的对应类、参数、示例和源码：以同一锁定版本 `daowei2026/uplot@e6.2` 为准，并由本项 Skill 按其原生 Workflow 处理。

## 5. 已有上游真实产物

A 与 B 阶段均已经形成当前有效的本 Run 原生产物；C、D、E 尚无本 Run 已完成专业产物。没有已发 Worker 工单。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 C Skill 的原生合同，不另设专业方法、展示方案、Worker 返回处理或验收要求。
- 实际回交对象：`chatgpt:OI-U2-F-OBS-20261118-01:manager`；回交时保持 `work_item_id=OI-U2-F-OBS-20261118-01-WI-C`、`stage_instance_id=OI-U2-F-OBS-20261118-01-M-C` 和 `delegation_id=D003`。
- 一次调用不足以完成本项 Skill 时，继续原 `D003` 与原工作项，并引用已经形成的真实产物和当前续接点。
