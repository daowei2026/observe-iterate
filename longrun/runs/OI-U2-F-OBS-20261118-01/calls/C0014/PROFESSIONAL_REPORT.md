# C0014｜D005/E Skill 续接：消费 W001 并签发 W002

## 1. 调用与专业身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0014`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 原 D005：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 续接起点：`daowei2026/observe-iterate@f9e435fe79818d22f84661f7186ec07ecd410b44:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0013/PRO_RETURN.json`

本次继续原 D005/E，不新建 D，不重跑 A～D，不启动 Q/V。

## 2. 已正式消费的 W001 Return

### 正式 Return

`daowei2026/observe-iterate@7beda1b54e7777b5b4f86ef6174376570e4c8b1a:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/WORKER_RETURN.json`

### 事实与证据

- `daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/FACT_REPORT.md`
- `daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/MANIFEST.local.json`
- `daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/facts.json`
- `daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/first_blocker.json`
- `daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/output/u2_f_caegraph/definition_run_report.json`
- `daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/source_stage_report.json`

W001 Return 的 `order_ref / worker / return_to` 与活跃 W001 完全匹配，因此本 executor 将该 Return 正式记入已消费 Worker 结果。

## 3. W001 真实结论

### 3.1 已成立

- source staging 成功；
- detached HEAD 精确为 `f4f0e4b276b1118b779473c1fbe462bc7a64b358`；
- D 与 C3 均存在且逐字节未改；
- `repair.diff=0 bytes`，source 工作树干净；
- D 真实启动一次，退出码 1；
- 没有调用 `f.rerun()`、全历史 producer 或 Q/V；
- 没有修改平台源码、生产数据、其他 Run；
- 没有候选 HTML、prepared tables 或 plot data。

### 3.2 未成立

W001 在导入 `mquant.frame` 时停止，因此尚未：

- 导入 `make_features`；
- 构造 F；
- 检查精确 `fields.json`；
- 读取任何正式 F occurrence；
- 进入 CAEGraph 构图；
- 形成可供 E3 核对的 HTML。

所以 W001 不能支持 F 产品存在／缺失、D 图定义正确／错误或 C2 图形一致／不一致等结论。

## 4. 首个阻断与因果边界

D 停在：

```python
from mquant.frame import CurrCalendar, CurrSof, KLine
```

平台 import 在 `/dwdhome/fy/BASE_E6_2_copy/mquant/apt/tool/misc.py:144` 创建：

```python
ProcessPoolExecutor(max_workers=os.getpid() - 2)
```

由此触发 `_multiprocessing.SemLock`。W001 为收敛写入范围新增的 Landlock 只允许 W001 目录写入，因而拒绝 `/dev/shm/sem.<random>`。独立标准库 probe 在同一限制下确认了该 syscall；它未加载 D/F/Q/V。

因此，W001 证明的是：

> 在 Worker 新增的严格 Landlock 条件下，平台 import 所需的 POSIX semaphore IPC 被拒绝。

它不证明：

- 无保护的原环境也失败；
- D/C3 有代码缺陷；
- F 正式产品缺失；
- 当前实例或位置错误。

## 5. E2 专业分类

完整分类产物：

`daowei2026/observe-iterate@5f4678f14050e60ca4d5f75fee3054b07fafc96b:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W001_RESULT_CLASSIFICATION.md`

结论为：

```text
MECHANICAL_EXECUTION_ENVELOPE_BLOCKER
```

### 后继判断

| 可能后继 | 判断 |
|---|---|
| 返回 B | 否；没有位置问题证据 |
| 返回 C | 否；未进入展示阶段 |
| 返回 D | 否；D/C3 未改且异常早于业务集成 |
| 接受图并进入 E4 | 否；没有 HTML |
| 新 W1 revision | **是**；基准不变，只需修复运行包络 |

## 6. 为什么不直接放开宿主 `/dev/shm`

当前 Owner 授权为：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

本 executor 不把该授权扩展为直接写宿主 `/dev/shm`。后继采用 run-root-backed 私有 IPC：

```text
namespace-local /dev/shm
→ W002/runtime/shm
```

只要 mount alias 的实际 backing 被证明在 W002 run root 内，POSIX semaphore 的持久写仍处在 Owner 授权路径下。

若 Worker 无法建立这种私有 mount，或只能写宿主 `/dev/shm` 才能继续，应停止并回 E，而不是自行扩权。

## 7. 已签发 W002

### 工单正文

`daowei2026/observe-iterate@3596c4fbe550fc01b667b743d0ed952d1a25717e:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W002/ORDER.md`

### 机读工单

`daowei2026/observe-iterate@2bdc0b96259b9c2a895113328b9ccc1172f09e6e:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W002/ORDER.json`

### W002 身份

```text
work_order_id=W002
operation category=new W1 revision
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
```

W002 不是正式取数 W2。E Skill 中 W1/W2 表示操作类别，本 Run 的 `W001/W002/...` 是顺序工单身份。正式取数仍需图被接受后另签后续工单。

## 8. W002 的最小动作

1. 在新 W002 run root 中固定同一 D commit；
2. 建立只含 user + mount、**不含 PID namespace** 的私有运行包络；
3. 将 namespace-local `/dev/shm` bind 到 W002 `runtime/shm`；
4. 保存 mount／alias 证据；
5. 在相同写边界内先运行 `multiprocessing.Lock` probe；
6. probe 通过后运行 D；
7. 返回 HTML 或新的首个真实阻断；
8. 不 patch 平台 `mquant`，不改变 D/C3 业务语义。

W002 若发现精确 F 没有既存 `fields.json`，仍应按 D 合同停止；不得调用 producer。

## 9. Worker、E3、W2 与数据状态

当前：

```text
W001 Worker Return: ACCEPTED_AS_FACT
W001 outcome: STOP
W002: PUBLISHED_NOT_SENT
candidate HTML: none
E3: not started
formal data admission: none
formal export order: none
DATA_READY: false
```

主控收到本 Return 后，应独立核验 W002 权限、物理 Worker 状态、cwd、模型／强度、动作账本和单写者，再实际发送 W002。

## 10. 同一 D005 的续接点

W002 正式 Worker Return 必须回：

```text
chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
```

收到后继续原：

```text
D005 / WI-E / M-E
```

- 若仍无 HTML：E2 消费新的首个阻断；
- 若有 HTML：E2 核脚本与 diff，随后进入 E3；
- 只有 E3 接受图，才允许 E4 正式取数准入。

## 11. 完成判断

C0014 已完成：

- W001 正式 Return 的专业消费；
- 首个阻断的因果边界判断；
- B/C/D 与机械问题分类；
- W002 的真实签发和续接点确定。

原 D005/E Skill 仍未完成，因为尚无候选图，E3～E6 未发生。

```text
professional_state=IN_PROGRESS
accepted_worker_refs=[W001]
issued_order_refs=[W002]
remaining_scope=W002 + E2/E3 + accepted-graph-only E4/W2 + E5/E6
owner_request=null
```
