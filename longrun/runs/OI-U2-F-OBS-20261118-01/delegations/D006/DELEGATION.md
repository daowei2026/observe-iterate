# D006｜重新开始 E Skill：CommonPriceTurnGroupCandidatesFrp CAEGraph 执行／运行

本 D 依 Owner 同 Run 重启指令重新签发一次完整 E Skill 工作。它使用新的 Delegation、工作项和阶段实例，不继续原 `D005 / WI-E / M-E / W005` 执行链；A～D 的本 Run 正式成果继续有效。本 D 只绑定任务身份、固定 E Skill、适用文件、真实有效 A～D／Owner 输入和回交对象，不另写专业方法、具体 Worker 工单、展示预期或额外验收 Gate。

## 1. 工作身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `delegation_id`：`D006`
- `issuer_call_id`：`C0022`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `recipient`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `parent_task_id / work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E-R1`
- 预定独立物理执行 Chat：`FOBS-1119-E2`；其真实创建、绑定与发送由主控另行核实。D006 发布本身不等于已经物理送达。

这里的 `executor:E2` 是新 Skill 执行 Chat 的逻辑身份；E Skill 原文件中的 `E1` 是该 Skill 的内部第一步“建立最小运行基准”，二者不得混同。

## 2. 本次完整 E Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/SKILL.md`
- 专业 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/IO_SPEC.md`
- Worker 派单合同：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md`
- W1 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/RUN_REPAIR_ORDER_TEMPLATE.md`
- W2 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/DATA_EXPORT_ORDER_TEMPLATE.md`
- 通用 Worker 工单模板：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/templates/WORKER_ORDER.md`

接收者应亲自完整读取并采用这些原件。E 内部步骤不另立 D；具体 Worker 工单由本次 E Skill 执行 Chat 依原 Skill 与内部 Workflow 形成。

## 3. Owner 本次重启输入与旧链收束

以下原件是本次 Owner 输入的权威原文和主控有据记录，必须完整读取；本 D 不以摘要替代或改写 Owner 的修复设计边界：

- Owner E 重启原文：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_E_RESTART_20261119.md`
- 主控采用变更：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/E_RESTART_CONTROLLER_ADOPTION.json`
- 旧 E 链收束事实：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/E_RESTART_OLD_CHAIN_CLOSURE.json`
- 当前 Binding：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 当前 Resource Binding：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- C0022 完整任务：`daowei2026/observe-iterate@03a0a62d041c5c746ccd38d4a8dcc77b25271c4a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0022/FULL_ASSIGNMENT.md`
- C0022 Invocation：`daowei2026/observe-iterate@426e453c448dc871e6a879df94af912de37a1e51:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0022/INVOCATION.json`

有据边界：原 D005 与旧 C0021 执行链已被 Owner 替代；W005 真实未发送并记为 `NOT_SENT → SUPERSEDED`；W001～W004 的真实 `STOP` 历史和全部旧产物保留，但不构成本次 D006 的执行方案，也不证明 E 完成。

## 4. 外层业务输入和范围

- 唯一业务输入：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- 本 Run 实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 Python 构造入口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- F 的 Haskell 实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- F 的 Python 包装／读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`
- 锁定 CAEGraph 手册：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`

本次对象仍只取正常 `make_features(...)` 返回的第一项 `f`，实例为 `TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i`。实际 Linux 工作区仍为 `/dwdhome/fy/BASE_E6_2_copy`。本 Run 只完成 F 的 A～E 并以 E 交付结束；Q 继续暂停，V 未启动，不做合理性分析，不执行输入排除的全历史 producer 重跑。

## 5. 当前有效 A～D 上游结果

### A｜Occurrence 理解

- 完成 Return：`daowei2026/observe-iterate@d57377780714f737961fd6e8487f5eaf38ea0889:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0003/PRO_RETURN.json`
- 原生产物：`daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`

### B｜观察位置

- 完成 Return：`daowei2026/observe-iterate@f4f82a780b7549f56b78f4b76e8f784532baf655:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0005/PRO_RETURN.json`
- 原生产物：`daowei2026/observe-iterate@6f1ee9eb4595254845d3b228a146ad68cabc64e0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`

### C｜展示方式

- 完成 Return：`daowei2026/observe-iterate@93478a76f6b751b8f712a8885322b45927a8a729:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0008/PRO_RETURN.json`
- C 原生产物：`daowei2026/observe-iterate@bcb94cc298d0a20049a2a52fdf7fe577137e7bde:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/CAEGRAPH_DISPLAY_PREPARATION.md`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- C3 可注入代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`

### D｜定义集成

- 完成 Return：`daowei2026/observe-iterate@6c88b6e905281e24ac9526f15277464af79ef31b:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0010/PRO_RETURN.json`
- 集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- 完整定义脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- 定义级检查：`daowei2026/observe-iterate@37f81088985ff3f1d8c2e7fa409db7529586073f:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/DEFINITION_CHECKS.json`

A～D 不重跑；新 E 执行 Chat 从这些本 Run 正式成果和本次 Owner 原文建立自己的 E Skill 内部运行基准。

## 6. 操作授权包络

本 D 的机读授权与当前 Binding 对齐，允许的 operation 为：

```text
run_record_write
caegraph_run_and_repair
caegraph_data_export
```

允许写面并集为：

```text
longrun/runs/OI-U2-F-OBS-20261118-01/**
/dwdhome/fy/BASE_E6_2_copy/**
/dev/shm/sem.*
```

具体 W 仍必须满足当前 Binding 的同 operation、同 execution context、同 `authority_quote` 覆盖，并由主控在真实派发时逐单核验。本节只传递现行授权包络，不设计或签发任何具体 Worker 工单。

## 7. 本项输出与回交

- 本项专业输出、阶段状态和完成条件直接遵循第 2 节完整 E Skill 原生合同。
- 实际回交对象：`chatgpt:OI-U2-F-OBS-20261118-01:manager`。
- 回交时保持 `delegation_id=D006`、`work_item_id=OI-U2-F-OBS-20261118-01-WI-E-R1`、`stage_instance_id=OI-U2-F-OBS-20261118-01-M-E-R1`。
- 一次调用不足以完成 E 时，继续原 D006 与本次新工作项／阶段实例，并引用已经形成的真实 E 产物和当前续接点；不得退回继续原 D005/W005。
