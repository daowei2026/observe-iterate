# C0017｜C0016 longrun-professional-return/v2 同源协议补正报告

## 1. 调用与专业身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0017`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 原 D005：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 本次 Invocation：`daowei2026/observe-iterate@runs/OI-U2-F-OBS-20261118-01:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0017/INVOCATION.json`
- 本次 token：`9759a7d8bcfd4e75aeccd6bd3ab1de0c`

本次只修复 C0016 Return 的 V2 机读枚举，不形成新专业结论，不新建 D，不签发 Worker 工单，不重新消费 Worker Return，不重跑 A～E，也不启动 Q/V。

## 2. 被修复的原件与拒绝原因

被拒绝的原 C0016 Return：

`daowei2026/observe-iterate@616497e3b3eb6f231c6b04f3218ea7ceea0e32b9:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PRO_RETURN.json`

原 C0016 Invocation：

`daowei2026/observe-iterate@28dbe8e9b2f8c0781bbdca24900c79d332ddf466:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/INVOCATION.json`

原 C0016 token：

```text
fe3fdadbdbd241aa998ce26b0a20cb19
```

固定合同：

`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json`

该合同对 `professional_return.professional_state` 只接受：

```text
IN_PROGRESS
WAITING_OWNER
REPORTED_COMPLETE
```

原 C0016 Return 使用：

```text
NEEDS_OWNER_INPUT
```

因此唯一拒绝原因是 `professional_state` 不属于 schema 枚举。

## 3. 同源补正原件

已由原签发者在同一路径重发：

`daowei2026/observe-iterate@4e0087f355313eb71914ad7d5d568737ae2f8fd6:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PRO_RETURN.json`

补正内容只有：

```diff
- "professional_state": "NEEDS_OWNER_INPUT"
+ "professional_state": "WAITING_OWNER"
```

`WAITING_OWNER` 是固定 V2 合同中对“专业工作等待 Owner 输入”的合法机读表达。

## 4. 保持不变的 C0016 专业事实

以下原件及其专业内容没有修改：

### C0016 完整专业报告

`daowei2026/observe-iterate@d7f834bf5d9c060af5602dea92c87521f4da5a04:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PROFESSIONAL_REPORT.md`

### W002 E2 分类

`daowei2026/observe-iterate@56ecda308a8ef02ec9848d44ff7bae78c0a56118:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W002_RESULT_CLASSIFICATION.md`

### Owner 请求 OR001

`daowei2026/observe-iterate@6f2fb38d8ff7e45c1ae6e234eaf2c95b215ee4a9:longrun/runs/OI-U2-F-OBS-20261118-01/owner_requests/OR001/REQUEST.md`

补正后的 C0016 Return 仍保持：

```text
call_id=C0016
role=executor
sender=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
delegation_ref=原 D005
return_to=原 manager
result_ref=原 C0016 完整专业报告
issued_delegation_refs=[]
issued_order_refs=[]
accepted_worker_refs=[W002 正式 Worker Return]
remaining_scope_ref=原 C0016 完整专业报告
continuation_ref=OR001
owner_request_ref=OR001
```

因此本补正没有改变：

- W002 的真实消费结论；
- `RUNTIME_IPC_CAPABILITY_AND_AUTHORITY_GAP` 分类；
- 没有候选 HTML、E3 未开始、E4 未准入、`DATA_READY=false` 的状态；
- 等待 Owner 对 OR001 作答的续接点；
- 原 D005、WI-E、M-E 和唯一 F 范围。

## 5. 历史保留与当前有效原件

Git 历史继续保留被拒绝的原 C0016 Return：

`daowei2026/observe-iterate@616497e3b3eb6f231c6b04f3218ea7ceea0e32b9:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PRO_RETURN.json`

协议消费时应采用同路径的当前补正原件：

`daowei2026/observe-iterate@4e0087f355313eb71914ad7d5d568737ae2f8fd6:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PRO_RETURN.json`

前者用于保留拒绝历史，后者用于 V2 合同消费。二者不能混用。

## 6. C0017 自身的真实状态

C0017 没有新增专业动作，只完成协议修复和精确引用更新：

```text
new delegation: none
new worker order: none
new worker result consumed: none
new Owner request: none
professional conclusion changed: no
current E state: WAITING_OWNER
```

C0017 的机器 Return 应：

- `professional_state=WAITING_OWNER`；
- `result_ref` 指向本报告；
- `remaining_scope_ref` 直接指向补正后的 C0016 Return，以引用当前有效同源状态；
- `continuation_ref` 与 `owner_request_ref` 继续指向 OR001；
- 不新增 `accepted_worker_refs` 或 `issued_order_refs`。

## 7. 当前续接点

Owner 对 OR001 作出明确答复，并由主控更新／回读对应 Binding 或物理运行环境后，继续原：

```text
D005 / WI-E / M-E
```

不新建 D，不重跑 A～D，不启动 Q/V。

## 8. 完成判断

C0017 的协议补正任务已经完成；D005/E Skill 的专业状态没有因此改变，仍为等待 Owner 输入。
