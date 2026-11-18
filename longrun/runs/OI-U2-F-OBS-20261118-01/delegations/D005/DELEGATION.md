# D005｜E Skill 工作委派：CommonPriceTurnGroupCandidatesFrp CAEGraph 执行／运行

本 D 仅绑定一次完整 E Skill 工作与已经存在的真实输入和产物，不重新规定专业方法、展示预期、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `delegation_id`：`D005`
- `issuer_call_id`：`C0011`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `recipient`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `parent_task_id / work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/SKILL.md`
- 专业 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/IO_SPEC.md`
- Worker 派单合同：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md`
- W1 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/RUN_REPAIR_ORDER_TEMPLATE.md`
- W2 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/DATA_EXPORT_ORDER_TEMPLATE.md`

本项专业工作由接收者亲自完整读取并采用上述 E Skill 原件。E 内部步骤不另立 D。

## 3. 外层任务已经提供的事实

- 本次对象为 `CommonPriceTurnGroupCandidatesFrp`（F），即正常 `make_features(...)` 返回的第一项 `f`。
- 特征代码版本为 `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；Python 包装与正常实例构造版本为 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次实例在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下构造，实际对象为 `rb / hc / i`，源尺度为 `5m`；完整构造和参数以第 4 节所列精确原件为准。
- A、B、C、D 均已形成本 Run 当前有效专业产物。D 的稳定定义身份为 `OI-U2-F-OBS-20261118-01-D-CAEGRAPH-V1`，已形成可交 E 尝试执行的完整脚本；D 没有运行真实平台图。
- 本 Run 范围仍为 F 的观察材料准备 A～E，并以本 E Skill 的观察材料交付结束；Q、V、合理性分析、历史成果预接受及输入排除的全历史 producer 重跑不在范围内。
- Owner 更正后的实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。当前 E1 已建立；第二 executor 与实际 Worker 物理绑定尚未建立，物理派发和权限由主控按 V2 核验。

## 4. 当前输入与适用原始文件

### 4.1 Run、Workflow 与业务输入

- Owner GO 与工作区更正：`daowei2026/observe-iterate@74ed0b11552f73b03e55e3e324f8325889730b52:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 外层 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md`
- 唯一业务输入：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- C0011 原任务：`daowei2026/observe-iterate@568827b19507b83b15d1402c7931073ac3b3de31:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0011/FULL_ASSIGNMENT.md`
- C0011 Invocation：`daowei2026/observe-iterate@6a7d9bde588d3ca973f0fd6281a5c54534002c29:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0011/INVOCATION.json`

### 4.2 本次实例与实现原件

- 本 Run 的实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- F 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

### 4.3 A／B／C 当前有效专业产物

- A 原生产物：`daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- B 原生产物：`daowei2026/observe-iterate@6f1ee9eb4595254845d3b228a146ad68cabc64e0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`
- C 原生产物：`daowei2026/observe-iterate@bcb94cc298d0a20049a2a52fdf7fe577137e7bde:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/CAEGRAPH_DISPLAY_PREPARATION.md`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- C3 可注入代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`

### 4.4 D 当前有效专业产物

- 正式 D004：`daowei2026/observe-iterate@2fc0cfc19eb48e1e820e7f51ab2996a968715956:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D004/DELEGATION.json`
- C0010 Invocation：`daowei2026/observe-iterate@35d0c95d000f8d31913087679bbff48b030f833a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0010/INVOCATION.json`
- C0010 executor Return：`daowei2026/observe-iterate@6c88b6e905281e24ac9526f15277464af79ef31b:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0010/PRO_RETURN.json`
- D 完整专业报告：`daowei2026/observe-iterate@b6757672cb326f57fdeff76c6fac401870dc7ecc:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0010/PROFESSIONAL_REPORT.md`
- D 完整集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- D 完整定义脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- D 定义级机读检查：`daowei2026/observe-iterate@37f81088985ff3f1d8c2e7fa409db7529586073f:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/DEFINITION_CHECKS.json`

D 已按原生 Skill 报告完整，D004 无剩余续作。D 的真实平台执行项明确为 `NOT_RUN_IN_D`，由本 E Skill 按其原生 Workflow 处理。

### 4.5 锁定 CAEGraph／uplot 原件

- 使用手册：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`
- 正式导出：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:__init__.py`
- 绘图类与顶层配置：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:utlv2.py`
- 布局组织：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:utkv2.py`
- `PlotCtx`／绘图上下文：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:pfw.py`
- 构图数据树：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:pdt.py`
- 多尺度实现：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:multiscale.py`

## 5. 已有上游真实产物

A、B、C、D 均已形成本 Run 当前有效专业产物。C0010 Return 为 `REPORTED_COMPLETE`，零 Worker、无原 D 剩余续作。E 尚无本 Run 已完成专业产物、执行与核图基准、Worker 工单、候选图、正式取数准入或正式数据。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 E Skill 的原生合同，不另设专业方法、展示预期、Worker 返回处理或验收要求。
- 实际回交对象：`chatgpt:OI-U2-F-OBS-20261118-01:manager`；回交时保持 `work_item_id=OI-U2-F-OBS-20261118-01-WI-E`、`stage_instance_id=OI-U2-F-OBS-20261118-01-M-E` 和 `delegation_id=D005`。
- 一次调用不足以完成本项 Skill 时，继续原 `D005` 与原工作项，并引用已经形成的真实产物和当前续接点。
