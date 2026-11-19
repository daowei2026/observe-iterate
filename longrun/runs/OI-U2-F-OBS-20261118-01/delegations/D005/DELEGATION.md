# D005｜E Skill 工作委派：CommonPriceTurnGroupCandidatesFrp CAEGraph 执行／运行（C0018 合法续接版本）

本文件是原 `D005 / WI-E / M-E` 的合法续接版本，不是新的专业任务或新的 Delegation identity。原 C0011 签发历史、原 D005 版本、W001/W002 结果以及 C0016/C0017 历史均保留。本版本只纳入已经发生的真实 E 结果、Owner 对 OR001 第一项的既有选择指令采用记录和新 Binding，并同步同一 D005 的机读授权包络；不重新规定专业方法、展示预期、Worker 返回处理或专业验收条件。

## 1. 委派身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `delegation_id`：`D005`
- `issuer_call_id`：`C0018`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `recipient`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `parent_task_id / work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`

原始签发历史：

- 原 D005 正文：`daowei2026/observe-iterate@ae52648476dd7f9c1547e76059306dad2a686853:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.md`
- 原 D005 JSON：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 原 C0011 签认：`daowei2026/observe-iterate@d6dc3e0368334b77081d56940cbdfa0f9ecf2d5a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0011/PRO_RETURN.json`

本次只由 C0018 对同一 D005 的当前续接版本和新授权包络重新签认；Delegation、工作项和阶段实例身份均未改变。

## 2. 固定 E Skill

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/SKILL.md`
- 专业 Workflow：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/IO_SPEC.md`
- Worker 派单合同：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/WORKER_DELEGATION.md`
- W1 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/RUN_REPAIR_ORDER_TEMPLATE.md`
- W2 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/DATA_EXPORT_ORDER_TEMPLATE.md`
- 通用 Worker 工单模板：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/templates/WORKER_ORDER.md`

本项专业工作仍由原 executor:E1 亲自完整读取并采用上述原件。E 内部步骤不另立 D；工单由原 E1 依据完整 E Skill 和内部 Workflow 签发。

## 3. 外层任务与范围事实

- 本次对象仍为 `CommonPriceTurnGroupCandidatesFrp`（F），即正常 `make_features(...)` 返回的第一项 `f`。
- 特征代码版本为 `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；Python 包装与实例构造版本为 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`。
- 本次实例仍为 `TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i`；完整构造与参数以第 5 节精确原件为准。
- A、B、C、D 均已形成并被 manager 消费为本 Run 当前有效专业产物。D 的稳定定义身份仍为 `OI-U2-F-OBS-20261118-01-D-CAEGRAPH-V1`。
- 本 Run 只完成 F 的 A～E，并以 E 观察材料交付为终点。Q 仍按 Owner 最新安排不继续，V 未启动；合理性分析、历史成果预接受及输入排除的全历史 producer 重跑均不在本 Run 范围内。
- 实际 Linux 工作区仍为 `/dwdhome/fy/BASE_E6_2_copy`。

## 4. E 当前真实专业状态

### 4.1 已发生的 E 续作

原 executor:E1 已在原 D005 下签发并正式消费 W001、W002：

- W001 Return：`daowei2026/observe-iterate@7beda1b54e7777b5b4f86ef6174376570e4c8b1a:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/WORKER_RETURN.json`
- W002 Return：`daowei2026/observe-iterate@08f9944755ac4ba8786249edb25ea4f5b5cab555:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/WORKER_RETURN.json`

两个工单的结果均为 `STOP`，原 Worker 已结束，当前没有 Worker 工单在途。

当前有效专业状态原件：

- C0016 当前有效 Return：`daowei2026/observe-iterate@4e0087f355313eb71914ad7d5d568737ae2f8fd6:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PRO_RETURN.json`
- C0016 完整专业报告：`daowei2026/observe-iterate@d7f834bf5d9c060af5602dea92c87521f4da5a04:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PROFESSIONAL_REPORT.md`
- E2 原生分类：`daowei2026/observe-iterate@56ecda308a8ef02ec9848d44ff7bae78c0a56118:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W002_RESULT_CLASSIFICATION.md`
- C0017 协议补正 Return：`daowei2026/observe-iterate@02331f1a4c84746a3e2a4d69dc9373a710ae47b7:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0017/PRO_RETURN.json`
- C0017 协议补正报告：`daowei2026/observe-iterate@75e5bd041e4d6e7a62732bf3cade2626e6471faa:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0017/PROFESSIONAL_REPORT.md`

C0017 只把 C0016 的非法枚举同源补正为 `WAITING_OWNER`；C0016 完整报告、W002 消费结论、E2 分类和 OR001 均未改变。旧拒绝原件继续保留在 Git 历史中。

### 4.2 当前专业分类与未完成边界

E2 原生分类仍为：

```text
RUNTIME_IPC_CAPABILITY_AND_AUTHORITY_GAP
```

W001 的 Landlock 阻断了平台导入所需的临时 POSIX semaphore；W002 在尝试私有 user/mount namespace 时因写 `/proc/self/uid_map` 被拒绝，尚未进入 namespace 内部。W002 中 SemLock probe 和 D 的尝试次数均为 0。

当前仍没有：

- 候选 HTML；
- 图接受；
- E4 正式取数准入；
- W2 正式导出；
- 正式图数据；
- E5 一致性核对；
- E6 观察材料交付。

因此 E、D005、WI-E、M-E 和整个 Run 均未完成。上述专业分类及后继处理继续由 E Skill 原生结果决定，manager 不重判 B/C/D 或专业完成条件。

## 5. Owner 采用记录与当前授权来源

### 5.1 原请求与既有选择指令采用

- OR001：`daowei2026/observe-iterate@6f2fb38d8ff7e45c1ae6e234eaf2c95b215ee4a9:longrun/runs/OI-U2-F-OBS-20261118-01/owner_requests/OR001/REQUEST.md`
- Owner 第一项采用记录：`daowei2026/observe-iterate@1e6392ad185c9be31367f0001f82e83aa53ad14e:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_OR001_FIRST_OPTION_ADOPTION_20261119.md`

采用记录保留 Owner 原话“碰到需要我处理的问题，先选第一项”，并据此采用 OR001 第一项 A；它不伪称新收到了一次逐字 INI 确认。

### 5.2 当前 Binding、Resource 与注册索引

- 当前 Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 当前 Resource Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 注册索引：`daowei2026/observe-iterate@56b09ffca6144ef9b67a9b2a7136ff0810c959eb:longrun/controller/RUN_REGISTRY.json`
- Worker 物理绑定证据：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`

新的 operation-specific grant 为：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

`authority_quote` 中继续逐字限制 `/dev/shm` 仅用于本 Run CAEGraph 运行进程树临时创建和删除 Python multiprocessing 的 `sem.*`，并排除任意共享内存 payload、sudo、mount 绕过、平台源码 patch、F producer、Q/V 和据此启动正式数据导出。

`caegraph_data_export` grant 没有扩大，仍只允许 `/dwdhome/fy/BASE_E6_2_copy/**`。截至本版本签发时，没有依据新 grant 签发新的 W，也没有据此运行 D 或执行正式导出。

## 6. C0018 与固定来源

- C0018 完整任务：`daowei2026/observe-iterate@6c4582d3c59389e35999aba8d24d5a068084d7c9:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0018/FULL_ASSIGNMENT.md`
- C0018 Invocation：`daowei2026/observe-iterate@f8582d52b6af29b511c360025b86e0adc642dad0:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0018/INVOCATION.json`
- 主控固定来源：`daowei2026/cgpterm@5461c6e51e73d011028afd8b41a0c5c340541df5:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`
- 业务 Workflow／Skill 固定来源：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288`

## 7. 适用业务输入、实例与上游产物

### 7.1 唯一业务输入与实例

- 唯一业务输入：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- 实例读取脚本：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- 需求与实现索引：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md`
- 正常 `make_features(...)` 构造：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 完整展开实例参数：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`
- F Python 包装与正式读取接口：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`

### 7.2 A／B／C／D 当前有效产物

- A：`daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- B：`daowei2026/observe-iterate@6f1ee9eb4595254845d3b228a146ad68cabc64e0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`
- C：`daowei2026/observe-iterate@bcb94cc298d0a20049a2a52fdf7fe577137e7bde:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/CAEGRAPH_DISPLAY_PREPARATION.md`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- C3 可注入代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- D 集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- D 完整定义脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- D 定义级检查：`daowei2026/observe-iterate@37f81088985ff3f1d8c2e7fa409db7529586073f:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/DEFINITION_CHECKS.json`

### 7.3 锁定 CAEGraph／uplot

锁定版本仍为 `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad`，包括 `CAEGraph使用手册.md`、`__init__.py`、`utlv2.py`、`utkv2.py`、`pfw.py`、`pdt.py` 和 `multiscale.py`。

## 8. 同一 D005 的当前操作授权包络

当前 D005 允许的操作类别仍为：

```text
run_record_write
caegraph_run_and_repair
caegraph_data_export
```

本 D 的机读 `allowed_writes` 是当前三类操作在已采用 Binding 下的写面并集：

```text
longrun/runs/OI-U2-F-OBS-20261118-01/**
/dwdhome/fy/BASE_E6_2_copy/**
/dev/shm/sem.*
```

任何后续 W 仍必须同时满足：

1. W 的 `operation` 属于本 D 的 `permitted_operations`；
2. W 的写面是本 D `allowed_writes` 的子集；
3. W 的 operation-specific grant 被当前 Binding 中同 operation、同 execution context、同 `authority_quote` 的 grant 覆盖。

因此 `/dev/shm/sem.*` 只可用于 `caegraph_run_and_repair` 的现行 grant，不能据此扩大 `caegraph_data_export`。本节只同步 V2 授权包络，不替代 E Skill 的专业工单形成、结果消费或完成判断。

## 9. 本项专业输出与回交

- 本项专业输出、状态和完成条件继续直接遵循第 2 节所列 E Skill 原生合同，不另设专业方法、展示预期、Worker 返回处理或验收要求。
- 后续仍由原 `chatgpt:OI-U2-F-OBS-20261118-01:executor:E1` 继续同一 `D005 / OI-U2-F-OBS-20261118-01-WI-E / OI-U2-F-OBS-20261118-01-M-E`。
- 实际回交对象仍为 `chatgpt:OI-U2-F-OBS-20261118-01:manager`。
- 一次调用不足以完成 E 时，继续原 D005 与原工作项，并引用已经形成的真实 E 产物和当前续接点。
