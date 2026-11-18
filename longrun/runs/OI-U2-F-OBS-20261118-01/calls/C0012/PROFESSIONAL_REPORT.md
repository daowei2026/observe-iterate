# C0012｜D005 E Skill 专业回交：E1 基准与 W001 签发

## 1. 调用与回交身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0012`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 正式委派：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`

## 2. 本次实际完成的 E 工作

本次亲自读取并采用了 D005、E Skill、专业 Workflow、字段级 I/O、Worker 派单合同、W1/W2 短执行卡、通用 Worker Order、V2 协议与机读 schema，并核对了 Owner 路径更正、Run/Resource Binding、D 当前完整脚本和 C2 当前核图基准。

本调用实际完成：

1. E1 最小执行与核图基准；
2. W1 运行／机械修复范围和停止条件；
3. 正式 W001 通用工单正文；
4. 正式 `longrun-order/v2` 机读工单；
5. W1 诊断副产物与 W2 正式取数的边界。

本调用没有伪造：

- Worker 物理线程绑定；
- W001 实际发送／送达；
- Linux 命令执行；
- 候选 HTML；
- Worker Return；
- E2/E3 图接受；
- E4 正式取数准入；
- W2 或正式数据；
- `DATA_READY`。

## 3. 已发布专业产物与工单

### E1 执行与核图基准

`daowei2026/observe-iterate@942bb61c2453a44cc258da8c2832d89687c52aa0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E1_EXECUTION_AND_REVIEW_BASELINE.md`

该基准固定：

- D 唯一运行脚本；
- C2 当前唯一预期 HTML；
- `/dwdhome/fy/BASE_E6_2_copy` 工作区；
- 运行入口和候选输出目录；
- W1 可直接修范围；
- 必须停回 E 的语义问题；
- E2/E3 最小核对项。

### W001 正文

`daowei2026/observe-iterate@cfc1fabc0f910434743cea514ea28f674a35dcd0:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.md`

### W001 机读工单

`daowei2026/observe-iterate@17840c4dbc8493636ce75d07859ceecb31d885e7:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json`

工单身份：

```text
work_order_id=W001
issuer=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
```

W001 只授权真实运行 D 完整定义和权限内机械修复。它不授权改变实例、位置、字段或展示语义，也不授权正式取数。

## 4. W1 的实际运行目标

主控完成物理 Worker、模型／强度、cwd、单写者和修正后权限核验后，应将 W001 发送到逻辑 Worker：

```text
codex:OI-U2-F-OBS-20261118-01:worker:W1
```

Worker 从本 Run 的 `observe-iterate` 工作树根目录执行：

```bash
python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/u2_f_caegraph \
  > longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/w1_run.log \
  2>&1
```

优先返回可打开 HTML，或首个真实阻断错误。

若精确 F 实例没有既存 `fields.json`，Worker 必须停止；不得调用 `f.rerun()`，不得执行输入明确排除的全历史 producer。

## 5. 诊断副产物与正式数据边界

D 脚本当前会在候选运行目录中顺带写出 prepared tables、PlotDataTree CSV 和运行报告。E 已在基准与工单中明确：

- 这些在 W1 只属于诊断副产物；
- 不构成 E4 正式取数准入；
- 不得冒充 W2 正式数据；
- 不得据此标记 `DATA_READY`。

只有 E3 接受最终脚本和 HTML 后，E 才能形成明确的图层／对象和数据阶段清单，并另行签发 W2。

## 6. 当前真实状态

```text
E1 baseline: PUBLISHED
W001 order: PUBLISHED_NOT_SENT
physical worker binding: NOT_ESTABLISHED
W001 worker return: NONE
candidate HTML: NONE
E2/E3 review: NOT_STARTED
E4 data admission: NONE
W2: NONE
formal data: NONE
E stage: IN_PROGRESS
```

`RUN_RESOURCE_BINDING.actual_worker_thread_binding_ref=null`。因此，W001 文件存在不等于已经发送、执行或送达。

## 7. 剩余专业范围与同 D005 续接点

收到 W001 的正式 Worker Return 后，必须继续同一 `D005 / WI-E / M-E`：

1. E2 消费候选运行事实，检查 HTML、首个阻断、最终脚本、diff 和问题性质；
2. 机械问题且基准不变时，按 E Skill 决定是否续发具名 W1 revision；
3. 位置问题返回 B，展示问题返回 C，集成问题返回 D；
4. E3 核对最终脚本与 D、最终图与 C2，并作接受／限域接受／返回／阻塞判断；
5. 只有图被接受后，E4 才形成最小正式取数准入并签发 W2；
6. E5 消费正式数据，核对图层／对象、数据阶段、品种、时间、行数和绑定关系；
7. E6 在图与正式数据满足本轮用途后形成最终交付。

当前下一合法动作不是新 D，也不是 W2，而是主控对 W001 做物理派发和回执建账。

## 8. 完成判断

D005/E Skill 尚未完成。原因不是专业方法缺失，而是 E 原生 Workflow 要求的真实 W1 操作尚未发生。当前具备继续条件，未出现需要 Owner 新授权的问题。

- 本次签发 Worker 工单：`W001`
- 已接受 Worker Return：无
- `professional_state`：`IN_PROGRESS`
- `remaining_scope`：E2～E6
- `continuation`：W001 正式 Return 回原 executor:E1 后续接同一 D005
