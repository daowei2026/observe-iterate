# C0007｜正式执行 D003：Q 的 C Skill

[OI-U2-Q-OBS-20261120-01-C0007]
invocation_token=c18943fb21dc452c807fdd6a388a4731

你是本 Run 已绑定的原独立 Skill 执行 Chat executor:E1。本次按原 manager 在真实 C0006 Return 中签认的 D003 执行一项完整 C Skill 工作。A、B 已被原manager消费，不重跑。请完整读取并按原委派指定的 C SKILL、WORKFLOW、IO_SPEC 及适用原件实际执行；专业方法、原生输出、完成判断及内部 Worker 处理依原 Skill。主控仅转派原已签工作，不补充专业方法、业务预期或额外验收条件。

## 真实委派和来源

- D003 JSON：daowei2026/observe-iterate@21af7c3695dfa60eb3e5ad0bed980de2422be292:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D003/DELEGATION.json
- D003 正文：daowei2026/observe-iterate@f9f3e7de43ea1d92e44386612ad4b92fb2439e43:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D003/DELEGATION.md
- 签发者真实 C0006 Return：daowei2026/observe-iterate@7fca4206fea0215bf8474f119e834b312f02cab4:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0006/PRO_RETURN.json
- 当前 TASK_PROGRESS：daowei2026/observe-iterate@47470c29603c367f9a546b9966299ad2b9af3d4d:longrun/runs/OI-U2-Q-OBS-20261120-01/business_control/TASK_PROGRESS.md

本次工作身份为原 D003 / OI-U2-Q-OBS-20261120-01-WI-C / OI-U2-Q-OBS-20261120-01-M-C；回交原 manager chatgpt:OI-U2-Q-OBS-20261120-01:manager。一次调用不足时按真实结果续原 D003 和原工作项，不把部分结果称为完整。

V2 机读回交完整采用 observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288 的 PRO_EXECUTOR_GUIDE、LONGRUN_PROTOCOL_V2 和 longrun_schema_v2.json，保持真实 C0007 调用身份、原 D003 和准确不可变引用。

以下原 manager 委派逐字转交，其专业内容不由主控修改。

## D003 正文（原文）

# D003｜C Skill 工作委派：PostTurnGroupDirectionalOrganizationFrp 展示方式准备

本 D 仅绑定一次具体 Skill 工作与已经存在的真实输入和产物，不重新规定专业方法、业务预期、展示方案、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-Q-OBS-20261120-01`
- `delegation_id`：`D003`
- `issuer_call_id`：`C0006`
- `issuer`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `recipient`：`chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `parent_task_id / work_id`：`OI-U2-Q-OBS`
- `business_case_id`：`U2-FQV-Q`
- `work_item_id`：`OI-U2-Q-OBS-20261120-01-WI-C`
- `stage_instance_id`：`OI-U2-Q-OBS-20261120-01-M-C`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/SKILL.md`
- 内部 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/IO_SPEC.md`

本项专业工作由接收者亲自完整读取并采用上述 Skill 原件。C1、C2、C3 是该 Skill 的内部 Workflow，不拆成多个 D。

## 3. 外层任务已经提供的事实

- 本次特征名称：`PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织）。
- 特征代码版本：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；正常 Python 包装与实例构造版本：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次特征实例：在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下，按已给 `make_features(...)` 完整参数构造后，只取返回的第二项 `q`；对象为 `rb / hc / i`，尺度为 `5m`，方向为 `up`。完整构造和参数以第 4 节所列精确原件为准，不以本段摘要替代。
- `q` 经 `PostTurnGroupDirectionalOrganizationFrp.from_formation(f, ...)` 从准确 F 与原价／Calendar 输入构造。F 只作为 Q 的必要上游依赖；本 Run 不执行 F 的独立 A～E，也不把 F 历史阶段成果或现有 uplot 例外计入 Q。
- A 已形成当前有效的 Q occurrence 理解；B 已形成当前有效的普通默认位置合同。C 对 B 最终位置的处理边界直接遵循本 D 第 2 节所列 C Skill：C 不绑定 B 最终位置，B 的位置产物保留给后续 D 正式注入。
- 本 Run 完整范围为 Q 的观察材料准备 A～E，并以 Q 的 E 交付结束；V、合理性分析、S/U2/U3、参数标定、收益判断、资金配置及未经授权的全历史 producer 重跑不在范围内。
- Owner 确认的实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。所有本 Run 新业务产物与记录仅写 `longrun/runs/OI-U2-Q-OBS-20261120-01/**`；本 C Skill 当前没有 Worker 工单。

## 4. 当前输入与适用原始文件

### 4.1 Run、Workflow 与业务输入

- Owner GO：`daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json`
- F 完成与 Q 不继承阶段成果／uplot 例外的记录：`daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/F_COMPLETION_HANDOVER.json`
- 外层 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md`
- 唯一 Q 业务输入：`daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md`
- C0006 原任务：`daowei2026/observe-iterate@c74e388faff999ab085cf770df1c59e823b57be4:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0006/FULL_ASSIGNMENT.md`
- C0006 Invocation：`daowei2026/observe-iterate@0ffbc851d5f772d27739afe3b1effe0a28d8ac50:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0006/INVOCATION.json`

### 4.2 本次实例与实现原件

- 本批实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- Q 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs`
- Q 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py`
- 必要上游 F 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- 必要上游 F 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

### 4.3 A 当前有效专业产物

- 原 D001：`daowei2026/observe-iterate@2944f650baf779308fcc7fa92d20c6b0b4ca0e71:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D001/DELEGATION.json`
- C0002 合法 executor Return：`daowei2026/observe-iterate@06b3f5d12218004bfc37c828866d6066e475ae84:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PRO_RETURN.json`
- C0003 同源格式补正 Return：`daowei2026/observe-iterate@9ffe7977837c99ddc26549164f33c9c738f68b64:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0003/PRO_RETURN.json`
- A 完整专业报告：`daowei2026/observe-iterate@23aab75c3415fe247e91f78a4079dfc8a80bfa57:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PROFESSIONAL_REPORT.md`
- A 人读原生产物：`daowei2026/observe-iterate@bf50bbe5c9447cb992af547e3f5f95f7465cae88:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- A 机读原生产物：`daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

A 已按原生 Skill 报告完整，D001 无剩余续作。其当前有效边界包括：Q 的业务主输出为 `DirectionalOccurrence` 与显式生命周期收口 `DirectionalDutyEnd`；一版 Q occurrence 对应一个 F candidate Life 的完整组观点并保存 Q 自身 `Life / Revision / Previous` 与准确 F candidate 引用；成员记录只是该 Q occurrence 的嵌套 payload；Q 的正式发表 firing、`directionalKnown`、成员 Turn actual／confirmation／known、endpoint 与 Calendar 位置不得混同；无新 Q occurrence 不等于失败或责任结束。完整事实以所列两份 A 原生产物为准。

### 4.4 B 当前有效专业产物

- 原 D002：`daowei2026/observe-iterate@49f531848911d3e05149009291e6b20185563b4f:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D002/DELEGATION.json`
- C0005 executor Return：`daowei2026/observe-iterate@9d92e381c6f63414d1dcb0945823df0628804984:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PRO_RETURN.json`
- B 完整专业报告：`daowei2026/observe-iterate@39126d7ced7cc8190272e45e7ff0590bdc99b968:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PROFESSIONAL_REPORT.md`
- B 人读原生产物：`daowei2026/observe-iterate@98fd297509d1d8f521711d78414995d0aa0a2965:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`
- B 机读原生产物：`daowei2026/observe-iterate@1214b9580f9a8b455d5df7524335e614058f2a69:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.json`

B 已按原生 Skill 报告完整，D002 无剩余续作。其当前位置合同为普通默认：`TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i / 2021-01-01～2022-12-31`。该合同继续保留给后续 D 阶段正式绑定；C 阶段不得把它固化为 C3 的最终位置。

### 4.5 锁定 CAEGraph 原件

- 使用手册：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`
- 手册不足时所需的对应类、参数、示例和源码：以同一锁定版本 `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad` 为准，并由本项 Skill 按其原生 Workflow 处理。

## 5. 已有上游真实产物

A 与 B 阶段均已经形成当前有效的本 Run 原生产物；C、D、E 尚无本 Run 已完成专业产物。没有已发或已接受的 Worker 工单／回交。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 C Skill 的原生合同，不另设专业方法、展示方案、Worker 返回处理或验收要求。
- 实际回交对象：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`；回交时保持 `work_item_id=OI-U2-Q-OBS-20261120-01-WI-C`、`stage_instance_id=OI-U2-Q-OBS-20261120-01-M-C` 和 `delegation_id=D003`。
- 一次调用不足以完成本项 Skill 时，继续原 `D003` 与原工作项，并引用已经形成的真实产物和当前续接点。


## D003 机读委派（原文）

```json
{
  "schema": "longrun-delegation/v2",
  "run_id": "OI-U2-Q-OBS-20261120-01",
  "delegation_id": "D003",
  "issuer_call_id": "C0006",
  "issuer": "chatgpt:OI-U2-Q-OBS-20261120-01:manager",
  "recipient": "chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1",
  "return_to": "chatgpt:OI-U2-Q-OBS-20261120-01:manager",
  "task_ref": "daowei2026/observe-iterate@f9f3e7de43ea1d92e44386612ad4b92fb2439e43:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D003/DELEGATION.md",
  "business_context_ref": "daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md",
  "input_refs": [
    "daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md",
    "daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json",
    "daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json",
    "daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/F_COMPLETION_HANDOVER.json",
    "daowei2026/observe-iterate@c74e388faff999ab085cf770df1c59e823b57be4:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0006/FULL_ASSIGNMENT.md",
    "daowei2026/observe-iterate@0ffbc851d5f772d27739afe3b1effe0a28d8ac50:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0006/INVOCATION.json",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/LONGRUN_PROTOCOL_V2.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/professional/PRO_EXECUTOR_GUIDE.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/SKILL.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/WORKFLOW.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/IO_SPEC.md",
    "daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md",
    "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py",
    "daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json",
    "daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs",
    "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py",
    "daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs",
    "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py",
    "daowei2026/observe-iterate@2944f650baf779308fcc7fa92d20c6b0b4ca0e71:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D001/DELEGATION.json",
    "daowei2026/observe-iterate@06b3f5d12218004bfc37c828866d6066e475ae84:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PRO_RETURN.json",
    "daowei2026/observe-iterate@9ffe7977837c99ddc26549164f33c9c738f68b64:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0003/PRO_RETURN.json",
    "daowei2026/observe-iterate@23aab75c3415fe247e91f78a4079dfc8a80bfa57:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PROFESSIONAL_REPORT.md",
    "daowei2026/observe-iterate@bf50bbe5c9447cb992af547e3f5f95f7465cae88:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md",
    "daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json",
    "daowei2026/observe-iterate@49f531848911d3e05149009291e6b20185563b4f:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D002/DELEGATION.json",
    "daowei2026/observe-iterate@9d92e381c6f63414d1dcb0945823df0628804984:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PRO_RETURN.json",
    "daowei2026/observe-iterate@39126d7ced7cc8190272e45e7ff0590bdc99b968:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PROFESSIONAL_REPORT.md",
    "daowei2026/observe-iterate@98fd297509d1d8f521711d78414995d0aa0a2965:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md",
    "daowei2026/observe-iterate@1214b9580f9a8b455d5df7524335e614058f2a69:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.json",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md"
  ],
  "expected_outputs": [
    "按所引用 C Skill 的原生输出及完成条件形成并回交本项 Skill 专业结果"
  ],
  "permitted_operations": [
    "run_record_write"
  ],
  "allowed_writes": [
    "longrun/runs/OI-U2-Q-OBS-20261120-01/**"
  ]
}
```
