# TASK_PROGRESS｜OI-U2-F-OBS-20261118-01 当前业务完成全景

> 当前快照边界：Owner 已在同一 Run 正式要求重新启动 E。A、B、C、D 的本 Run 正式成果继续有效，不重跑。旧 `D005 / WI-E / M-E / C0021 / W005` 执行链已按有据记录收束：D005 与 C0021 被替代，W005 真实未发送并记为 `NOT_SENT → SUPERSEDED`；W001～W004 的真实 `STOP` 历史和全部旧产物保留，但不证明 E 完成，也不再构成本次 E 的执行方案。新 `D006 / WI-E-R1 / M-E-R1` 已发布给逻辑 `executor:E2`，尚未物理发送；新 E 尚未开始专业执行。

## A. 身份、固定来源与当前采用

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `business_task_id / work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- manager：`chatgpt:OI-U2-F-OBS-20261118-01:manager`（FOBS-1118-M）
- 主控：`codex:OI-U2-F-OBS-20261118-01:controller`
- 新 E 逻辑执行身份：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- 预定新独立物理 Chat：`FOBS-1119-E2`；截至本快照尚未创建／绑定／发送。
- 原 E1 Chat：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`；不再承接本次重启后的 E。
- 新工作项：`OI-U2-F-OBS-20261118-01-WI-E-R1`
- 新阶段实例：`OI-U2-F-OBS-20261118-01-M-E-R1`
- 新委派：`D006`

当前采用来源：

- Owner E 重启原文：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_E_RESTART_20261119.md`
- 主控采用变更：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/E_RESTART_CONTROLLER_ADOPTION.json`
- 旧链收束：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/E_RESTART_OLD_CHAIN_CLOSURE.json`
- 当前主控来源：`daowei2026/cgpterm@d4ba9f8711f5d20633f789cacfe41c1aa8ba686a:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`
- 旧主控采用 `daowei2026/cgpterm@5461c6e51e73d011028afd8b41a0c5c340541df5` 保留为历史，不被静默覆盖。
- 固定业务 Workflow／Skill／输入来源：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288`
- 当前 Binding：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 当前 Resource Binding：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- C0022 完整任务：`daowei2026/observe-iterate@03a0a62d041c5c746ccd38d4a8dcc77b25271c4a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0022/FULL_ASSIGNMENT.md`
- C0022 Invocation：`daowei2026/observe-iterate@426e453c448dc871e6a879df94af912de37a1e51:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0022/INVOCATION.json`

业务对象和资源：

- 唯一输入：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- 对象：`CommonPriceTurnGroupCandidatesFrp`，只取正常 `make_features(...)` 返回的第一项 `f`。
- 实例：`TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i`。
- 实际工作区：`/dwdhome/fy/BASE_E6_2_copy`。
- FRP Haskell：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；工作区对应源码仓库应定位到 `edh-universe/frp/frp`。
- TIS Python：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`；构造入口 `frp/fqv_kline_example.py`，运行导入名 `mquant.tis.frp.fqv_kline_example`。
- 锁定 CAEGraph：`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad`。

当前新 E 委派：

- D006 正文：`daowei2026/observe-iterate@04a80f99ed0b276b2107943ea2e34f58fcbaf3dd:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D006/DELEGATION.md`
- D006 JSON：`daowei2026/observe-iterate@08988fc1f2e028caaf3bac40f2d557dddc2293f2:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D006/DELEGATION.json`

- `snapshot_status`：`current`
- 已知新事实但尚未纳入本快照：无。

## B. 整体目标、范围和完成边界

| 项目 | 当前有据状态 | 必需来源／后继 |
|---|---|---|
| 任务目标 | 为 F 完成观察材料准备 A～E，并以 E 的真实图、正式数据和一致性核对交付为终点 | Owner GO、Owner E 重启、`control/02` |
| 当前范围 | 只观察 F；Q 继续暂停，V 未启动；不做合理性分析，不预接受历史结果，不执行排除的全历史 producer 重跑 | Owner 原文、唯一 F 输入 |
| A～D | 本 Run 正式成果继续有效，不重跑 | C0003／C0005／C0008／C0010 Return |
| 旧 E 链 | 已停止后续调度并被替代；历史保留，不等于完成 | Owner 重启、旧链收束 JSON |
| 新 E 链 | D006 已发布未发送；新执行 Chat 尚未物理建立 | D006、当前 Binding／Resource |
| 整体状态 | `IN_PROGRESS / incomplete` | 主控创建并绑定 FOBS-1119-E2，实际发送 D006；新 E2 从内部 E1 建立运行基准 |
| 当前 Owner 请求 | 无。Owner 已给出重启指令和执行边界 | Owner E 重启原文 |

## C. Workflow 与依赖

```text
A → B
A → C1 → C2 → C3
外层输入 + A + B + C + 锁定 CAEGraph → D
D + C2 当前预期 HTML + 实例 + 环境／授权 → E
```

A、B、C、D 的当前有效结果已经满足新 E 的专业输入前置。Owner 选择的是“重新签发一次 E”，不是继续 D005，也不是重跑 A～D。

| Workflow | 阶段／实例 | 当前有效专业成果 | 当前未完成／在途 | 下一合法动作 |
|---|---|---|---|---|
| M 观察材料准备 | A～D 完整；旧 E=`M-E` 历史收束；新 E=`OI-U2-F-OBS-20261118-01-M-E-R1` | A occurrence；B 位置；C 当前展示预期／HTML／C3；D 完整定义 | D006 已发布未发送；新 E 未开始；无 Worker 工单在途 | 主控建立 E2 物理 Chat 并发送 D006 |
| R 合理性分析 | `NOT_APPLICABLE` | 无 | 本 Run 不启动 R | E 完成后也不自动进入 R |

## D. A～E 当前状态

| 阶段 | 当前状态 | 当前有效成果／版本 | 未满足条件 | 精确引用 |
|---|---|---|---|---|
| A occurrence 理解 | `COMPLETE / REPORTED_COMPLETE` | F occurrence、业务位置、revision 与读取边界 | 无 | C0003 Return `d573777...`；A 产物 `823b56a...` |
| B 观察位置 | `COMPLETE / REPORTED_COMPLETE` | `B-POS-001`：steel、rb/hc/i、5m、2021-01-01～2022-12-31、`groupKnownFrom` | 无 | C0005 Return `f4f82a7...`；B 产物 `6f1ee9e...` |
| C 展示方式 | `COMPLETE / REPORTED_COMPLETE` | `C2-CURRENT-V2`、当前唯一预期 HTML、C3 可注入代码 | 无 | C0008 Return `93478a7...`；C 产物 `bcb94cc...`；HTML `56eef30...` |
| D 定义集成 | `COMPLETE / REPORTED_COMPLETE` | `...D-CAEGRAPH-V1`、完整定义脚本、定义级检查；真实平台执行在 D 中为 `NOT_RUN_IN_D` | 无 | C0010 Return `6c88b6e...`；D 产物 `e35945a...`、`f4f0e4b...`、`37f8108...` |
| 旧 E 执行链 | `SUPERSEDED / NOT_COMPLETE` | W001～W004 `STOP` 历史和全部旧产物保留 | 不再调度 D005／C0021／W005 | 旧链收束 `ae7c4e6...:E_RESTART_OLD_CHAIN_CLOSURE.json` |
| 新 E 执行／运行 | `NOT_STARTED / DELEGATION_PUBLISHED_NOT_SENT` | 新 `D006 / WI-E-R1 / M-E-R1`；收件为逻辑 `executor:E2` | 物理 Chat 未创建／绑定，D006 未发送；E 内部 E1 基准、W1、候选图、E3、E4、W2、E5、E6 均未开始 | D006 正文 `04a80f9...`、JSON `08988fc...` |

### D.1 A～D 正式完成 Return

- A：`daowei2026/observe-iterate@d57377780714f737961fd6e8487f5eaf38ea0889:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0003/PRO_RETURN.json`
- B：`daowei2026/observe-iterate@f4f82a780b7549f56b78f4b76e8f784532baf655:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0005/PRO_RETURN.json`
- C：`daowei2026/observe-iterate@93478a76f6b751b8f712a8885322b45927a8a729:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0008/PRO_RETURN.json`
- D：`daowei2026/observe-iterate@6c88b6e905281e24ac9526f15277464af79ef31b:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0010/PRO_RETURN.json`

### D.2 旧 E 链的有据收束

- D005：`SUPERSEDED`，`business_complete=false`。
- C0021：`SUPERSEDED`；原件保留，不把手机端完成标记推断成业务完成。
- W005：真实 `physical_send_occurred=false`，状态历史为 `NOT_SENT → SUPERSEDED`；精确目标路径不存在。
- W001～W004：真实 `STOP` 历史保持不变；不据此认定 E 完成。
- 当前没有旧 Worker 工单在途，不允许自动续发 W005。

这些事实统一以：

`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/E_RESTART_OLD_CHAIN_CLOSURE.json`

为当前收束依据。旧 E1 的环境拼装方案不作为 D006 的执行方案。

### D.3 新 E 的身份与内部起点

```text
新 Skill Chat 逻辑身份：executor:E2
新工作项：WI-E-R1
新阶段实例：M-E-R1
新委派：D006
E Skill 内部第一步：E1 建立最小运行基准
```

`executor:E2` 与 Skill 内部步骤 `E1` 是不同维度。新执行 Chat 必须从完整原 E Skill 和 Owner 原文建立自己的 E1 基准；manager 未设计 Worker 工单。

### D.4 当前授权和未发生事实

D006 的机读操作授权与当前 Binding 对齐：

```text
run_record_write
caegraph_run_and_repair
caegraph_data_export
```

D 写面并集：

```text
longrun/runs/OI-U2-F-OBS-20261118-01/**
/dwdhome/fy/BASE_E6_2_copy/**
/dev/shm/sem.*
```

具体 Worker 工单仍须由新 E2 依据原 E Skill 形成，并由主控按当前 Binding 的 operation-specific grant、execution context、authority quote、物理 Worker、cwd、共享写面和单写者逐单核验。

截至本快照：

- D006 尚未实际发送；
- FOBS-1119-E2 尚未真实创建／绑定；
- 没有本次重启链的新 W；
- 没有第一个真实业务运行里程碑；
- 没有被新 E 接受的候选 HTML；
- 没有 E3 图接受；
- 没有 E4 正式取数准入；
- 没有 W2 正式导出；
- 没有 E5／E6；
- `DATA_READY=false`。

## E. 工作实例与执行 Chat

| `work_item_id / stage_instance_id` | 执行 Chat / D | 真实状态 | 当前有效成果 | 未完成与后继 |
|---|---|---|---|---|
| `...-WI-A / ...-M-A` | 原 E1 / D001 | `REPORTED_COMPLETE` | A 原生产物 | 保留；不重跑 |
| `...-WI-B / ...-M-B` | 原 E1 / D002 | `REPORTED_COMPLETE` | B-POS-001 | 保留；不重跑 |
| `...-WI-C / ...-M-C` | 原 E1 / D003 | `REPORTED_COMPLETE` | C1/C2/C3、当前 HTML | 保留；不重跑 |
| `...-WI-D / ...-M-D` | 原 E1 / D004 | `REPORTED_COMPLETE` | 稳定定义、脚本、检查 | 保留；不重跑 |
| `OI-U2-F-OBS-20261118-01-WI-E / OI-U2-F-OBS-20261118-01-M-E` | 原 E1 / D005 | `SUPERSEDED / NOT_COMPLETE` | W001～W004 STOP 历史及旧产物仅作历史 | 不再派发；W005 已替代 |
| `OI-U2-F-OBS-20261118-01-WI-E-R1 / OI-U2-F-OBS-20261118-01-M-E-R1` | 逻辑 E2 / D006 | `NOT_STARTED / DELEGATION_PUBLISHED_NOT_SENT` | 无新 E 专业产物 | 主控建立 FOBS-1119-E2、绑定逻辑 E2、发送 D006；之后由 E2 执行原 E Skill |

## F. 逐业务问题完成情况

| `question_id` | 所需回答深度 | 当前已满足 | 当前未满足 | 是否可结案 |
|---|---|---|---|---|
| `U2-FQV-F`（仅 F） | A～E 完成，并由 E 交付真实运行、核图、正式取数和一致性核对后的观察材料 | A～D 本 Run 正式成果有效；Owner 重启与旧链收束有据；新 E 合法入口已建立 | 新 E 尚未发送和执行；没有被接受的最终图、正式数据、E5/E6 | 否；Run `IN_PROGRESS` |

## G. 版本依赖、失效关系与恢复入口

| 对象 | 当前有效范围 | 历史／失效关系 | 恢复或下一动作 |
|---|---|---|---|
| A～D | 继续作为 D006 的唯一正式上游成果 | 旧 E 失败不自动使 A～D 失效；Owner 明确不重跑 | 新 E2 完整读取并消费 |
| C2 当前 HTML | 新 E 的核图基准 | 旧 E 未完成，不产生替代 HTML | E Skill 依原 Workflow核图 |
| D 完整定义 | 新 E 的正式运行输入 | D 中真实运行仍为 `NOT_RUN_IN_D`；旧 E 链不改写 D 正式成果 | 新 E 内部 E1 建立运行基准 |
| D005／旧 WI-E／M-E | 历史链；不再是当前执行入口 | Owner `SUPERSEDED`；W005 未发送 | 不恢复、不续发 |
| D006／WI-E-R1／M-E-R1 | 当前唯一合法 E 重启入口 | 尚未物理送达，不可宣称执行开始 | 主控创建／绑定 E2 Chat并发送 |
| Worker W1 物理线程 | 当前 Resource 允许复用，旧工单已结束 | 当前无业务工单在途 | 只有新 E2 原生签 W 后才可实际派发 |
| Controller 来源 | 新 `cgpterm@d4ba...` 为当前采用 | 旧 `5461...` 保留历史 | 主控按硬边界执行，不替 E 设计修法 |

## H. 本次更新与下一合法动作

- Owner 已明确：同 Run 保留 A～D，收束旧 E 链，从 E 重新开始。
- 旧链已完成必要对账：W005 未发送，D005／C0021／W005 被替代；无冲突 Worker 在途。
- manager 已新签 D006，并建立新 `WI-E-R1 / M-E-R1`；收件为已登记逻辑 `executor:E2`。
- D006 只传递任务身份、原 E Skill 全部原件、有效 A～D／Owner 输入、当前授权和回交对象；没有为新 E 设计具体 Worker 工单或新增 Gate。
- 当前下一合法动作：主控在同一 Project 新建独立物理 Chat `FOBS-1119-E2`，现场核验目标模型／推理强度，记录真实绑定后把 D006 原样发送给逻辑 E2。
- 发送后，新 E2 应先完成原 E Skill 内部 E1 最小运行基准；实际 W1 及后续工单由 E2 按完整 Skill形成，主控只做最小物理／权限核验。
- 第一个真实业务里程碑必须来自新 E 的实际执行（例如 E1 基准完成和首个真实 W1 运行事实），不能以 D006／TASK_PROGRESS 文件发布数量代替。
- 一次调用不足时继续原 `D006 / WI-E-R1 / M-E-R1`；不得回到 D005/W005。
- E 原生完成并交付后，本 Run 才可结案；不自动进入合理性分析。

**发布校验边界**：D006 已发布不等于物理发送；物理发送不等于 E 已开始形成专业产物；旧链收束不等于 E 完成；A～D 保留不等于允许旧 E 结果冒充本次重启交付。
