# C0013｜D005/E Skill 续接：W001 授权与运行入口修订

## 1. 调用与专业身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0013`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 原 D005：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 续接起点：`daowei2026/observe-iterate@5f639c77190a3dd220bc96c06a24726d970f8515:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0012/PRO_RETURN.json`

本次继续原 D005/E，不新建 D，不重跑 A～D，也不启动 Q/V。

## 2. 实际读取和采用的新增事实

### Owner 授权补正

`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_AUTHORITY_AMENDMENT_20261119.md`

Owner 已确认：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

并确认可直接建立本 Run 专用 Worker；Q 暂不继续。

### 当前 Binding

- `daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- `daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`

当前 Binding 已保存逐字 authority quote、修正后的实路径和物理 Worker binding 引用。

### 物理 Worker 证据

`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`

记录的事实为：

```text
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
model=gpt-6.1-sol
reasoning_effort=max
cwd=/dwdhome/fy/BASE_E6_2_copy
thread idle=true
business_order_dispatched=false
worker_goal_created=false
```

该记录证明物理绑定已建立，但不等于 W001 已发送或执行。

## 3. 对现场布局事实的 E 专业分类

有限预检查只覆盖工作区根及直接非 symlink 子目录，得到：

- 根目录没有 `.git`；
- 未找到 `observe-iterate` 命名候选；
- 未找到本 Run D 脚本相对路径。

该结果不能推出整个工作区缺少运行依赖或实例。它说明原 W001 的一个运行入口前提未被证实：

> “工作区内已存在包含 D 脚本的 observe-iterate 工作树”。

按 E Workflow，这属于**可在 E1/W1 内确定性修正的机械 source-entry 问题**，不要求返回 B、C 或 D，因为：

- B 的品种／时间位置没有变化；
- C2 的面板／图元／表达没有变化；
- D 的实例、字段和完整定义没有变化；
- 只需要把锁定 D commit 布置为可执行文件树。

## 4. 采用的机械入口

当前基准：

`daowei2026/observe-iterate@1a4d2e455a1175f1c20226fa9873c587c697021d:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E1_EXECUTION_AND_REVIEW_BASELINE_C0013.md`

采用在授权工作区内建立本 Run/W001 专用 detached source staging：

```text
/dwdhome/fy/BASE_E6_2_copy/
  observe-iterate-runs/
    OI-U2-F-OBS-20261118-01/
      W001/
        source/observe-iterate/      # HEAD 固定 D commit
        output/u2_f_caegraph/
        logs/
        source_stage_report.json
        repair.diff
```

source HEAD 必须为：

```text
f4f0e4b276b1118b779473c1fbe462bc7a64b358
```

该提交包含 D 脚本和相对 C3 文件。Git 获取失败或凭据不可用时，Worker 返回首个真实阻断；不得从未知本地文件拼接来源。

这一处理：

- 不改变工作区环境；
- 不修改其他仓库或生产数据；
- 不要求无界递归搜索；
- 不重跑 F producer；
- 不改变 D/C/B/A 的专业内容。

## 5. 同一 W001 的活跃修订

### 原 C0012 历史版本

- 正文：`daowei2026/observe-iterate@cfc1fabc0f910434743cea514ea28f674a35dcd0:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.md`
- JSON：`daowei2026/observe-iterate@17840c4dbc8493636ce75d07859ceecb31d885e7:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json`
- 状态：发布但未发送、未执行、无 Worker Return。

### C0013 当前活跃版本

- 正文：`daowei2026/observe-iterate@973c0da06c28b0ce7f343205858d9002f97667c9:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.md`
- JSON：`daowei2026/observe-iterate@74562f258d93fdea8db0ab334fb0ebb23f1cfb99:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json`
- 修订历史：`daowei2026/observe-iterate@dfeff952b71e22eebcede83cda6c19a2816f2b83:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/REVISION_HISTORY.md`

机读活跃版本已经：

- 保持 `work_order_id=W001`；
- 使用 `issuer_call_id=C0013`；
- 指向原 D005；
- 指向同一逻辑 Worker 和原 executor:E1；
- 对齐新 Binding 的 grant 与逐字 authority quote；
- 引用 Owner amendment、新 Binding、物理 Worker binding、C0012 Return 和旧 W001 历史；
- 增加 source staging report、实际退出码和首个真实阻断交付。

## 6. W001 当前运行边界

Worker 只能：

1. 在专用 run root 布置锁定 D commit；
2. 运行完整 D 定义；
3. 返回候选 HTML或首个真实阻断；
4. 修复不会改变业务含义的语法、import、路径、确认 API、类型和输出接线；
5. 保存日志、exit code、diff 和 run report。

Worker 必须停止并回 E，如果：

- 精确 F 实例无既存 `fields.json`；
- 需要 `f.rerun()` 或全历史 producer；
- 需要改变 SOF／品种／日历／5m／2021—2022／`groupKnownFrom`；
- 需要改变字段、图元、面板、标准化、交互或阅读语义；
- 正确修法不唯一或语义影响不明；
- 发现未知同一 W 结果或非单写者。

W1 顺带生成的 prepared tables、plot data 和 run report 仍只是诊断副产物，不构成 W2 正式数据，也不允许标记 `DATA_READY`。

## 7. 当前真实动作状态

```text
D005/E: IN_PROGRESS
E1 C0013 baseline: PUBLISHED
W001 identity: unchanged
W001 active order: PUBLISHED_NOT_SENT
physical worker binding: ESTABLISHED_BY_CONTROLLER_EVIDENCE
business order dispatched: false
worker goal created: false
W001 Worker Return: none
candidate HTML: none
E2/E3: not started
E4/W2: not permitted yet
DATA_READY: false
Q/V: not started
```

本 executor 没有把工单发布、物理绑定或未来发送等同于专业完成。

## 8. 下一合法动作与续接点

主控收到本 Return 后应独立：

1. 核对活跃 `ORDER.json@74562f...` 与 `ORDER.md@973c0d...`；
2. 核对 grant 与当前 Binding；
3. 重核 W1 实际线程仍 idle、模型／强度／cwd 正确；
4. 核对 W001 仍 `NOT_SENT`、无旧消息和未知现场结果；
5. 核对工作区单写者；
6. 实际发送同一 W001，并按真实回执登记 `IN_FLIGHT`。

Worker Return 必须：

```text
order_ref=daowei2026/observe-iterate@74562f258d93fdea8db0ab334fb0ebb23f1cfb99:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
```

收到 Return 后继续同一 `D005 / WI-E / M-E`，由本 executor 完成 E2 分类和 E3 核图。只有图被接受后，才能形成 E4 取数准入并签发 W2。

## 9. 完成判断

本次 C0013 已完成其续接任务：Owner 新授权、Binding、物理 Worker 和现场布局已经转成可去重、可派发的同一 W001 活跃工单与明确续接点。

原 D005/E Skill 仍未完成，因为 W001 尚未真实执行，E2～E6 尚未发生。

- `issued_order`：活跃 W001
- `accepted_worker_refs`：无
- `professional_state`：`IN_PROGRESS`
- `remaining_scope`：W001 实际运行，随后 E2～E6
- `continuation`：活跃 W001 的正式 Worker Return 回原 executor:E1
- `owner_request`：无
