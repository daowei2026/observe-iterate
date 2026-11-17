# C0002｜C0001 V2 机器回交修复报告

- `run_id`：`OI-EAW-P1-20261116-01`
- `call_id`：`C0002`
- `role`：`manager`
- `sender`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `invocation_token`：`d2b9f18ffea14c7e808fe3a45da201ad`
- 修复性质：只修复 C0001 的 `longrun-professional-return/v2` 机器合同，不重复 C0001 业务工作，不形成新 Gate，不重新签发 D001。

## 1. 唯一故障与实际修订

原 C0001 Return：

`daowei2026/observe-iterate@8912b459206af127e52235326d02f0f2e53749ea:longrun/runs/OI-EAW-P1-20261116-01/calls/C0001/PRO_RETURN.json`

原字段：

```json
"return_to": "codex:01a1e508-8411-7b10-bf9c-6d22c0427c6a"
```

按同版 V2 manager return 合同修订为：

```json
"return_to": null
```

实际修复原件：

`daowei2026/observe-iterate@0b5d6bfed28b1c65d14b900c81a09f382d54e0af:longrun/runs/OI-EAW-P1-20261116-01/calls/C0001/PRO_RETURN.json`

## 2. 保持不变的内容

本次没有修改以下业务原件或语义：

- C0001 `call_id`、`role`、`sender`、`result_ref`、`professional_state`；
- C0001 已签发 D001 的引用；
- `remaining_scope_ref` 与 `continuation_ref`；
- C0001 专业报告、MD-0001、D001 MD/JSON、TASK_PROGRESS；
- Owner GO、Binding、业务范围、H0 判断和后继关系。

本次没有创建新 D/W，没有把 D001 的 `issuer_call_id` 改成 C0002，也没有新增专业取材或重新读取数据。

## 3. 下一合法动作

主控重新执行 C0001 manager Return 与 D001 的同版 V2 校验。校验通过后，按原 C0001/D001 签发关系把 D001 派发给独立 executor E1；本 C0002 不替代该签发关系。