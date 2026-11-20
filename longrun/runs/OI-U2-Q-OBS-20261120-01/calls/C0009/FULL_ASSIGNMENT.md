# C0009｜正式执行 D004：Q 的 D Skill

[OI-U2-Q-OBS-20261120-01-C0009]
invocation_token=631516d6330741629aa29813c402ed85

你是本 Run 已绑定的原独立 Skill 执行 Chat executor:E1。本次按原 manager 在真实 C0008 Return 中签认的 D004 执行一项 D Skill 工作；A、B、C 已由原manager正式消费，不重跑。请完整读取并按原委派指定的 D SKILL、IO_SPEC、集成参考及适用原件实际执行；专业方法、原生输出、完成判断和内部 Worker 处理由原 Skill 决定。主控仅转派原已签工作，不补充专业方法、业务预期、执行约束或额外验收条件。

## 真实委派和来源

- D004 JSON：daowei2026/observe-iterate@5152b1a05f532f59ebf27829682395a16938644e:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D004/DELEGATION.json
- D004 正文：daowei2026/observe-iterate@aac469933a6d54eb03ca690e0029769f8ece46fb:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D004/DELEGATION.md
- 签发者真实 C0008 Return：daowei2026/observe-iterate@e3b200fe296e89825161e086ce49b2ee84e6329f:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0008/PRO_RETURN.json
- 当前 TASK_PROGRESS：daowei2026/observe-iterate@f4c1542843ba15b887fd2a9ae23eb9bc6dd31a36:longrun/runs/OI-U2-Q-OBS-20261120-01/business_control/TASK_PROGRESS.md

本次工作身份为原 D004 / OI-U2-Q-OBS-20261120-01-WI-D / OI-U2-Q-OBS-20261120-01-M-D；回交原 manager chatgpt:OI-U2-Q-OBS-20261120-01:manager。一次调用不足时按真实结果续原 D004 和原工作项，不把部分结果称为完整。

V2 回交完整采用 observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288 的 PRO_EXECUTOR_GUIDE、LONGRUN_PROTOCOL_V2 和 longrun_schema_v2.json，保持真实 C0009 调用身份、原 D004 和准确不可变引用。

以下原 manager 委派逐字转交，其专业内容不由主控修改。

## D004 正文（原文）

# D004｜D Skill 工作委派：PostTurnGroupDirectionalOrganizationFrp CAEGraph 定义集成

本 D 仅绑定一次具体 Skill 工作与已经存在的真实输入和产物，不重新规定专业方法、展示预期、Worker 返回处理或专业验收条件。机器身份、操作授权和实际发送状态以本 Run 的 V2 记录及主控核验为准。

## 1. 委派身份

- `run_id`：`OI-U2-Q-OBS-20261120-01`
- `delegation_id`：`D004`
- `issuer_call_id`：`C0008`
- `issuer`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `recipient`：`chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `parent_task_id / work_id`：`OI-U2-Q-OBS`
- `business_case_id`：`U2-FQV-Q`
- `work_item_id`：`OI-U2-Q-OBS-20261120-01-WI-D`
- `stage_instance_id`：`OI-U2-Q-OBS-20261120-01-M-D`

## 2. 本次 Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-definition-integration/SKILL.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-definition-integration/IO_SPEC.md`
- CAEGraph 仓库结构与定义集成参考：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/references/CAEGraph仓库结构与定义集成参考.md`

D 是该 Skill 定义的单一集成动作，没有内部 Workflow 节点。本项专业工作由接收者亲自完整读取并采用上述原件。

## 3. 外层任务已经提供的事实

- 本次目标特征为 `PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织），即正常 `make_features(...)` 返回的第二项 `q`。
- 特征代码版本为 `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；Python 包装与正常实例构造版本为 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次实例在 `TA_updto20240229_DBA`、`steel`、`night_end_at_2300` 下构造，实际对象为 `rb / hc / i`，尺度为 `5m`，方向为 `up`；完整参数和接线以第 4 节精确原件为准。
- `q` 经 `PostTurnGroupDirectionalOrganizationFrp.from_formation(f, ...)` 从准确 F 与原价／Calendar 输入构造。F 只作为 Q 的必要上游依赖；不重开 F 的独立 A～E，也不把 F 历史阶段成果或现有 uplot 例外计入 Q。
- A 已形成当前有效的 Q occurrence、身份、修订、位置、字段和处理关系；B 已形成普通默认位置合同：`TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i / 2021-01-01～2022-12-31`；C 已形成当前唯一预期 HTML、可注入 CAEGraph 代码和注入合同，且无阻塞 capability gap。
- C 当前唯一预期 HTML 是后续 D/E 的展示核对基准，但它使用确定性示意数据，不是实际 Q 运行结果。C3 没有硬编码外层 Q 实例或 B 最终位置。
- 本 Run 完整范围仍为 Q 自身的观察材料准备 A～E，并以 Q 的 E 观察材料交付结束；V、合理性分析、S/U2/U3、参数标定、收益判断、资金配置及未经授权的全历史 producer 重跑不在范围内。
- Owner 确认的实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。D Skill 本身不派 Worker、不运行最终图；当前也没有 Q Worker 工单或被接受的 Worker 回交。

## 4. 当前输入与适用原始文件

### 4.1 Run、Workflow 与业务输入

- Owner GO：`daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json`
- 资源绑定：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json`
- F 完成与 Q 不继承阶段成果／uplot 例外的记录：`daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/F_COMPLETION_HANDOVER.json`
- 外层 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md`
- 唯一 Q 业务输入：`daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md`
- C0008 原任务：`daowei2026/observe-iterate@9a82762c75f2cae9e34eb04bb09670864b248ab3:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0008/FULL_ASSIGNMENT.md`
- C0008 Invocation：`daowei2026/observe-iterate@554b97a7cf2e3f6c1e594d67c42e2cff0532ee3e:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0008/INVOCATION.json`

### 4.2 本次实例与实现原件

- 本批实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造原件：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- Q 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs`
- Q 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py`
- Q 的正式字段路径与层次：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/_U2DirectionalOrganizationFields.py`
- 必要上游 F 的 Haskell 主实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- 必要上游 F 的 Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

### 4.3 A 当前有效专业产物

- 原 D001：`daowei2026/observe-iterate@2944f650baf779308fcc7fa92d20c6b0b4ca0e71:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D001/DELEGATION.json`
- C0002 合法 executor Return：`daowei2026/observe-iterate@06b3f5d12218004bfc37c828866d6066e475ae84:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PRO_RETURN.json`
- C0003 同源格式补正 Return：`daowei2026/observe-iterate@9ffe7977837c99ddc26549164f33c9c738f68b64:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0003/PRO_RETURN.json`
- A 完整专业报告：`daowei2026/observe-iterate@23aab75c3415fe247e91f78a4079dfc8a80bfa57:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PROFESSIONAL_REPORT.md`
- A 人读原生产物：`daowei2026/observe-iterate@bf50bbe5c9447cb992af547e3f5f95f7465cae88:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- A 机读原生产物：`daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

### 4.4 B 当前有效专业产物

- 原 D002：`daowei2026/observe-iterate@49f531848911d3e05149009291e6b20185563b4f:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D002/DELEGATION.json`
- C0005 executor Return：`daowei2026/observe-iterate@9d92e381c6f63414d1dcb0945823df0628804984:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PRO_RETURN.json`
- B 完整专业报告：`daowei2026/observe-iterate@39126d7ced7cc8190272e45e7ff0590bdc99b968:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PROFESSIONAL_REPORT.md`
- B 人读原生产物：`daowei2026/observe-iterate@98fd297509d1d8f521711d78414995d0aa0a2965:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`
- B 机读原生产物：`daowei2026/observe-iterate@1214b9580f9a8b455d5df7524335e614058f2a69:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.json`

### 4.5 C 当前有效专业产物

- 原 D003：`daowei2026/observe-iterate@21af7c3695dfa60eb3e5ad0bed980de2422be292:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D003/DELEGATION.json`
- C0007 executor Return：`daowei2026/observe-iterate@250de2d20b17e9e531bcf92f45897269a9e460a1:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0007/PRO_RETURN.json`
- C 完整专业报告：`daowei2026/observe-iterate@38e1234c0ca49d899c7edc963c3eb6867442dd2e:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0007/PROFESSIONAL_REPORT.md`
- C 人读总产物：`daowei2026/observe-iterate@63df2581a1996d4356752f32c2ee5c64fa79fb1f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.md`
- C 机读总产物：`daowei2026/observe-iterate@42a603fc8d209ea1bed7870c7b298f99a2785782:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.json`
- C1 待展示信息：`daowei2026/observe-iterate@781865309218623fecb355a2c6bb826de08cf735:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C1_DISPLAY_INFORMATION.json`
- C2 第一版预期 HTML：`daowei2026/observe-iterate@36f88213832fe1ea90b29cecd47c0825e50ddf34:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED_V0_1.html`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@85b41da60713f7ed2824b104bff614478c0f9371:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED.html`
- C2 确定性预览生成器：`daowei2026/observe-iterate@5a1ecd7efaa4c176b262a0104fd2d87f79f6e4f3:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_preview.py`
- C3 可注入 CAEGraph 代码：`daowei2026/observe-iterate@435c2ed129ba7596b9d5a102bc0d8bf6104729ba:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_injectable.py`
- C3 注入合同：`daowei2026/observe-iterate@747ce755d95e9354dd13209c41ba053d219febe1:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C3_INJECTION_CONTRACT.md`

C 已按原生 Skill 报告完整，D003 无剩余续作。C2 当前唯一 HTML 是 D/E 的展示核对基准；两版 HTML 均为确定性示意，不是实际 Q 运行结果。

### 4.6 锁定 CAEGraph／uplot 原件

- 使用手册：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`
- 正式导出：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:__init__.py`
- 绘图类与顶层配置：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:utlv2.py`
- 布局组织：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:utkv2.py`
- `PlotCtx`／绘图上下文：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:pfw.py`
- 构图数据树：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:pdt.py`
- 动态标准化前端路径：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:dynstd.js`
- 纵轴适配前端路径：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:fit_y_range.js`
- 多尺度实现：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:multiscale.py`

## 5. 已有上游真实产物

A、B、C 均已形成本 Run 当前有效专业产物。C0007 Return 为 `REPORTED_COMPLETE`，零 Worker、无原 D 剩余续作。D、E 尚无本 Run 已完成专业产物，也没有已发或已接受的 Worker 工单／回交。

## 6. 本项专业输出与回交

- 本项专业输出、状态和完成条件直接遵循第 2 节所列 D Skill 的原生合同，不另设专业方法、展示预期、Worker 返回处理或验收要求。
- 实际回交对象：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`；回交时保持 `work_item_id=OI-U2-Q-OBS-20261120-01-WI-D`、`stage_instance_id=OI-U2-Q-OBS-20261120-01-M-D` 和 `delegation_id=D004`。
- 一次调用不足以完成本项 Skill 时，继续原 `D004` 与原工作项，并引用已经形成的真实产物和当前续接点。


## D004 机读委派（原文）

```json
{
  "schema": "longrun-delegation/v2",
  "run_id": "OI-U2-Q-OBS-20261120-01",
  "delegation_id": "D004",
  "issuer_call_id": "C0008",
  "issuer": "chatgpt:OI-U2-Q-OBS-20261120-01:manager",
  "recipient": "chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1",
  "return_to": "chatgpt:OI-U2-Q-OBS-20261120-01:manager",
  "task_ref": "daowei2026/observe-iterate@aac469933a6d54eb03ca690e0029769f8ece46fb:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D004/DELEGATION.md",
  "business_context_ref": "daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md",
  "input_refs": [
    "daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md",
    "daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json",
    "daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json",
    "daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/F_COMPLETION_HANDOVER.json",
    "daowei2026/observe-iterate@9a82762c75f2cae9e34eb04bb09670864b248ab3:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0008/FULL_ASSIGNMENT.md",
    "daowei2026/observe-iterate@554b97a7cf2e3f6c1e594d67c42e2cff0532ee3e:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0008/INVOCATION.json",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/LONGRUN_PROTOCOL_V2.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/professional/PRO_EXECUTOR_GUIDE.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-definition-integration/SKILL.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-definition-integration/IO_SPEC.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/references/CAEGraph仓库结构与定义集成参考.md",
    "daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py",
    "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md",
    "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py",
    "daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json",
    "daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs",
    "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py",
    "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/_U2DirectionalOrganizationFields.py",
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
    "daowei2026/observe-iterate@21af7c3695dfa60eb3e5ad0bed980de2422be292:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D003/DELEGATION.json",
    "daowei2026/observe-iterate@250de2d20b17e9e531bcf92f45897269a9e460a1:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0007/PRO_RETURN.json",
    "daowei2026/observe-iterate@38e1234c0ca49d899c7edc963c3eb6867442dd2e:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0007/PROFESSIONAL_REPORT.md",
    "daowei2026/observe-iterate@63df2581a1996d4356752f32c2ee5c64fa79fb1f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.md",
    "daowei2026/observe-iterate@42a603fc8d209ea1bed7870c7b298f99a2785782:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.json",
    "daowei2026/observe-iterate@781865309218623fecb355a2c6bb826de08cf735:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C1_DISPLAY_INFORMATION.json",
    "daowei2026/observe-iterate@36f88213832fe1ea90b29cecd47c0825e50ddf34:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED_V0_1.html",
    "daowei2026/observe-iterate@85b41da60713f7ed2824b104bff614478c0f9371:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED.html",
    "daowei2026/observe-iterate@5a1ecd7efaa4c176b262a0104fd2d87f79f6e4f3:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_preview.py",
    "daowei2026/observe-iterate@435c2ed129ba7596b9d5a102bc0d8bf6104729ba:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_injectable.py",
    "daowei2026/observe-iterate@747ce755d95e9354dd13209c41ba053d219febe1:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C3_INJECTION_CONTRACT.md",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:__init__.py",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:utlv2.py",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:utkv2.py",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:pfw.py",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:pdt.py",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:dynstd.js",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:fit_y_range.js",
    "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:multiscale.py"
  ],
  "expected_outputs": [
    "按所引用 D Skill 的原生输出及完成条件形成并回交本项 Skill 专业结果"
  ],
  "permitted_operations": [
    "run_record_write"
  ],
  "allowed_writes": [
    "longrun/runs/OI-U2-Q-OBS-20261120-01/**"
  ]
}
```
