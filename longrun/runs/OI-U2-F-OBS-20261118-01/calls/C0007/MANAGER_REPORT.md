# C0007 MANAGER_REPORT｜D003 机器引用格式定向补正

## 1. 调用身份与性质

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `call_id`：`C0007`
- `invocation_token`：`d0b8c412b53903d01faf0c69a35bf44b`
- `role / sender`：`manager / chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 本次性质：仅补正 V2 机器引用格式及其引用链，不是新的专业任务。

## 2. 补正依据

- C0007 正式任务：`daowei2026/observe-iterate@a8cba4cd026995479742458af55c5b1e61f426b8:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0007/FULL_ASSIGNMENT.md`
- C0007 Invocation：`daowei2026/observe-iterate@05a604af32fccf14833400d1e61e902ac7fc44c1:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0007/INVOCATION.json`
- 原 C0006 Return：`daowei2026/observe-iterate@e16c882f078b1f60266a3fb466ab7840d3ad428a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0006/PRO_RETURN.json`
- 原 D003 JSON：`daowei2026/observe-iterate@4118bf902fbb12bfa7751691f8aa80e7148a9868:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D003/DELEGATION.json`
- 原 D003 正文：`daowei2026/observe-iterate@0a9b669e4be78d4325c99269b72061bd9d8ab52f:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D003/DELEGATION.md`
- 机械校验原件：
  - `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json`
  - `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/tools/longrun_gate.py`

原 D003 JSON 的最后一个 `input_refs` 使用标签形式：

```text
daowei2026/uplot@e6.2:CAEGraph使用手册.md
```

该字段要求 `owner/repo@40位提交:path`。主控已核实同一 `e6.2` 标签解析为：

```text
daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md
```

标签与精确提交下的手册均对应 Git blob `f426390409bd141accf389ff5427850160d7d173`，因此这是同一采用版本的精确引用展开，不是专业版本变化。

## 3. 已执行补正

### 3.1 原 D003 JSON

补正后准确引用：

`daowei2026/observe-iterate@fadf29d9c0e57bf3eb77d9b198392b902b94a0f9:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D003/DELEGATION.json`

唯一内容变化是将最后一个 `input_refs` 从标签引用替换为上述 40 位提交引用。下列内容均保持不变：

- `delegation_id=D003`
- `issuer_call_id=C0006`
- `recipient=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to=chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `work_item_id=OI-U2-F-OBS-20261118-01-WI-C`
- `stage_instance_id=OI-U2-F-OBS-20261118-01-M-C`
- C Skill 专业任务、其他输入、预期输出、权限和写入范围

原 D003 正文未修改。正文中的标签表述仍指向同一采用版本，机器 JSON 已承担所需的精确提交引用。

### 3.2 原 C0006 Return

补正后准确引用：

`daowei2026/observe-iterate@1284ef04010533122d4883d41b990520deaa076a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0006/PRO_RETURN.json`

唯一内容变化是将 `issued_delegation_refs` 改为指向补正后的同一 D003 JSON：

```text
daowei2026/observe-iterate@fadf29d9c0e57bf3eb77d9b198392b902b94a0f9:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D003/DELEGATION.json
```

C0006 的 manager 身份、`result_ref`、专业状态、剩余范围、原 D003 正文续接引用和 Owner 请求状态均保持原样。

### 3.3 统一 TASK_PROGRESS

当前准确引用：

`daowei2026/observe-iterate@1bd2b98774b44e94f7dd1a771bbcec83aaefc305:longrun/runs/OI-U2-F-OBS-20261118-01/business_control/TASK_PROGRESS.md`

全景只更新了：

- D003 JSON 的当前精确提交引用；
- 补正后的 C0006 Return 引用；
- `uplot@e6.2` 到精确提交的同版本解析关系；
- C0007 格式补正事实。

A/B 的专业结果、C 的 `DELEGATION_PUBLISHED_NOT_SENT` 状态、D/E 未开始状态、W1/W2 未签发状态及工作区更正均未改变。

## 4. 明确未执行事项

- 没有重做 A 或 B；
- 没有签发新的 D；
- D003 仍由 C0006 签发；
- 没有改写 C 的专业内容或新增专业要求；
- 没有实际发送 D003；
- 没有开始 C；
- 没有签发或接受任何 Worker 工单；
- 没有 Owner 请求。

## 5. 当前状态与下一合法动作

本 Run 仍为 `IN_PROGRESS`。A/B 保持当前有效，C 尚未实际派发。下一合法动作是主控核验补正后的 D003/C0006 引用链，然后将原 D003 实际发送给已建立的 `executor:E1`，继续原 `D003 / WI-C / M-C`。

本次 C0007 不重新签认 D003，因此其 `issued_delegation_refs`、`issued_order_refs` 和 `accepted_worker_refs` 均应为空；接续点应为补正后的原 C0006 Return。
