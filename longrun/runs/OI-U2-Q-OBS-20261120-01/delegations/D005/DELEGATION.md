# D005｜E Skill 工作委派：PostTurnGroupDirectionalOrganizationFrp CAEGraph 执行／运行

本 D 只绑定一次完整 E Skill 工作、当前有效 A～D 产物、真实环境与既有授权包络，不重新规定专业方法、Worker 工单、问题分类规则、取数清单或专业验收条件。E 内部专业判断、W1／W2 的触发和实际回交处理均由接收者依原 E Skill 决定。

## 1. 委派身份

- `run_id`：`OI-U2-Q-OBS-20261120-01`
- `delegation_id`：`D005`
- `issuer_call_id`：`C0010`
- `issuer`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `recipient`：`chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`
- `parent_task_id / work_id`：`OI-U2-Q-OBS`
- `business_case_id`：`U2-FQV-Q`
- `work_item_id`：`OI-U2-Q-OBS-20261120-01-WI-E`
- `stage_instance_id`：`OI-U2-Q-OBS-20261120-01-M-E`

这里的 `executor:E1` 是本 Run 已绑定的 Skill 执行 Chat 身份；E Skill 原文件中的 `E1` 是其内部第一步“建立最小运行基准”，二者不得混同。

## 2. 本次完整 E Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/SKILL.md`
- 专业 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/IO_SPEC.md`
- Worker 派单合同：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md`
- W1 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/RUN_REPAIR_ORDER_TEMPLATE.md`
- W2 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/DATA_EXPORT_ORDER_TEMPLATE.md`
- 通用 Worker 工单模板：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/templates/WORKER_ORDER.md`

接收者应亲自完整读取并采用上述原件。E 的内部步骤不另立 D；具体 W1／W2 工单只能由本次 E Skill 执行 Chat 按原 Skill 与当前合法授权形成。

## 3. Run、外层输入与范围

- Owner GO：`daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md`
- Binding：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json`
- Resource Binding：`daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_RESOURCE_BINDING.json`
- F 完成与 Q 不继承阶段成果／uplot 例外的记录：`daowei2026/observe-iterate@f02e4f7373c411ea6614ae927b23504a173aef77:longrun/runs/OI-U2-Q-OBS-20261120-01/F_COMPLETION_HANDOVER.json`
- 外层 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/02_L1_观察材料准备流程.md`
- 完成全景协议：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:control/06_业务完成全景与更新协议.md`
- 唯一 Q 业务输入：`daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md`
- C0010 原任务：`daowei2026/observe-iterate@d5c8a0b25758c5c72f2fb16526abaef820cc42a0:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0010/FULL_ASSIGNMENT.md`
- C0010 Invocation：`daowei2026/observe-iterate@79762026934934c63576e3346fa22af1b9e5884b:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0010/INVOCATION.json`

本 Run 只执行 Q 自身的 A～E，并以 E 观察材料交付结束。目标仍是正常 `make_features(...)` 返回的第二项 `q`：`PostTurnGroupDirectionalOrganizationFrp`；准确 `f` 只作为 Q 的必要上游。V、合理性分析、S/U2/U3、参数标定、收益判断、资金配置和未经另行授权的全历史 producer 重跑均不在范围内。F 的既有阶段成果和 uplot 例外不自动成为 Q 的阶段成果或授权。

实际 Linux 工作区为 `/dwdhome/fy/BASE_E6_2_copy`。Resource Binding 仍记录：尚无 Q 物理 Worker，首次合法 W 前由主控创建并核验 Q 专用 Codex Chat、实际线程及共享写面。

## 4. 当前有效 A～D 专业结果

### A｜特征事件级 occurrence 理解

- 完成 Return：`daowei2026/observe-iterate@06b3f5d12218004bfc37c828866d6066e475ae84:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PRO_RETURN.json`
- 同源格式补正 Return：`daowei2026/observe-iterate@9ffe7977837c99ddc26549164f33c9c738f68b64:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0003/PRO_RETURN.json`
- 专业报告：`daowei2026/observe-iterate@23aab75c3415fe247e91f78a4079dfc8a80bfa57:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0002/PROFESSIONAL_REPORT.md`
- 人读产物：`daowei2026/observe-iterate@bf50bbe5c9447cb992af547e3f5f95f7465cae88:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- 机读产物：`daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

### B｜观察位置准备

- 完成 Return：`daowei2026/observe-iterate@9d92e381c6f63414d1dcb0945823df0628804984:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PRO_RETURN.json`
- 专业报告：`daowei2026/observe-iterate@39126d7ced7cc8190272e45e7ff0590bdc99b968:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0005/PROFESSIONAL_REPORT.md`
- 人读产物：`daowei2026/observe-iterate@98fd297509d1d8f521711d78414995d0aa0a2965:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`
- 机读产物：`daowei2026/observe-iterate@1214b9580f9a8b455d5df7524335e614058f2a69:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.json`

### C｜展示方式准备

- 完成 Return：`daowei2026/observe-iterate@250de2d20b17e9e531bcf92f45897269a9e460a1:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0007/PRO_RETURN.json`
- 专业报告：`daowei2026/observe-iterate@38e1234c0ca49d899c7edc963c3eb6867442dd2e:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0007/PROFESSIONAL_REPORT.md`
- 人读总产物：`daowei2026/observe-iterate@63df2581a1996d4356752f32c2ee5c64fa79fb1f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.md`
- 机读总产物：`daowei2026/observe-iterate@42a603fc8d209ea1bed7870c7b298f99a2785782:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.json`
- C1：`daowei2026/observe-iterate@781865309218623fecb355a2c6bb826de08cf735:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C1_DISPLAY_INFORMATION.json`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@85b41da60713f7ed2824b104bff614478c0f9371:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED.html`
- C2 预览生成器：`daowei2026/observe-iterate@5a1ecd7efaa4c176b262a0104fd2d87f79f6e4f3:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_preview.py`
- C3 可注入代码：`daowei2026/observe-iterate@435c2ed129ba7596b9d5a102bc0d8bf6104729ba:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_injectable.py`
- C3 注入合同：`daowei2026/observe-iterate@747ce755d95e9354dd13209c41ba053d219febe1:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C3_INJECTION_CONTRACT.md`

### D｜CAEGraph 定义集成

- 原 D004：`daowei2026/observe-iterate@5152b1a05f532f59ebf27829682395a16938644e:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D004/DELEGATION.json`
- 完成 Return：`daowei2026/observe-iterate@5cd5d38fcc61176dca8ff566364ecd7ebfa7fd7d:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0009/PRO_RETURN.json`
- 专业报告：`daowei2026/observe-iterate@91fe9d8768d528a2ff616917a42412afb25fcc8a:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0009/PROFESSIONAL_REPORT.md`
- 人读集成记录：`daowei2026/observe-iterate@3b3df7d4509860be1d43233736aecfb264732585:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_CAEGRAPH_DEFINITION_INTEGRATION.md`
- 机读集成记录：`daowei2026/observe-iterate@546e457983c7d3e00378eea26872e605d79f8e20:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_CAEGRAPH_DEFINITION_INTEGRATION.json`
- 定义级检查：`daowei2026/observe-iterate@78b306ae3dba130b4bd1015befdebe19090ac728:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_DEFINITION_CHECKS.json`
- E 可执行入口：`daowei2026/observe-iterate@9e03c89211ec4665763e1f609b37483c80c72930:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_definition.py`
- common／合同：`daowei2026/observe-iterate@3dc03ecfea52d38fa7ce965d17710f0ebb7b4021:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_common.py`
- locked-table support：`daowei2026/observe-iterate@cf6a5d496f6b3bfafdadcbd7f11f30a5a182b158:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_support.py`
- member adapter：`daowei2026/observe-iterate@0fcb881f99c4035dc81de154f34d86e6994b1227:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_members.py`
- exact occurrence adapter：`daowei2026/observe-iterate@dcdf9949f1297f854dbd852f75a9f39ef268b72b:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter.py`
- lifecycle／state plotters：`daowei2026/observe-iterate@eac1cb3342ff92961bf8055ac4c04042b94aeed4:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_base.py`
- member plotters：`daowei2026/observe-iterate@23fcb47fff8494df138445fc5ee705fe43a36764:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_member.py`
- audit／assembly：`daowei2026/observe-iterate@6ffa0e4b6ebb394f61fcb52277f7c27c69fd35b9:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_build.py`
- plotter exports：`daowei2026/observe-iterate@af96601fe525f2e6059ae3bd976b3b19de3060e7:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters.py`

D004 已由原 executor 报告完整，定义编号为 `Q-CAEGRAPH-D004-v1`，无 Worker、无剩余 D 范围，也没有进入 E。定义级检查通过；目标工作区真实依赖导入、正式 F/Q 读取、真实 adapter invariants、HTML／DynStd／hover／JS／PlotDataTree、性能和页面业务核对均明确属于 E，当前没有被冒充完成。

## 5. 当前执行对象与现有输出约定

D 完整定义已绑定：

```text
TA_updto20240229_DBA / steel / night_end_at_2300
5m / rb,hc,i / DirectionUp
PlotSet: 2021-01-01 00:00:00 → 2022-12-31 23:59:59
```

D 的默认模式只读既存准确 F/Q 产品，不暗中重跑；如果准确实例不存在正式产品，应明确失败。任何全期 producer 重跑仍不在当前任务授权范围内。

D 原产物已经约定候选输出位于本 Run 的 E 路径：

```text
longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH.html
longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH_DATA/
```

以上只是当前有效 D 输入与输出位置事实，不替代 E 自己依原 Skill 建立运行／核图基准、消费真实运行事实、核图、形成正式取数准入及核对正式数据。

## 6. 操作授权包络

当前 Binding 已有、且本 D 传递给本次 E Skill 的 operation 为：

```text
run_record_write
caegraph_run_and_repair
caegraph_data_export
```

允许写面并集为：

```text
longrun/runs/OI-U2-Q-OBS-20261120-01/**
/dwdhome/fy/BASE_E6_2_copy/**
```

具体 W 仍必须匹配当前 Binding 中同 operation、同 execution context、同 allowed_writes 与 authority_quote，并由主控在真实派发时逐单核验。本节只传递既有授权包络，不设计、签发或假定任何具体 Worker 工单。

## 7. 本项专业输出与回交

- 本项专业输出、阶段状态和完成条件直接遵循第 2 节所列完整 E Skill 原生合同。
- 实际回交对象：`chatgpt:OI-U2-Q-OBS-20261120-01:manager`。
- 回交时保持 `delegation_id=D005`、`work_item_id=OI-U2-Q-OBS-20261120-01-WI-E`、`stage_instance_id=OI-U2-Q-OBS-20261120-01-M-E`。
- 一次调用不足以完成 E 时，继续原 `D005` 与原工作项／阶段实例，并引用已经形成的真实 E 产物和当前续接点；不得为 E 内部步骤另造新的 Skill D。
