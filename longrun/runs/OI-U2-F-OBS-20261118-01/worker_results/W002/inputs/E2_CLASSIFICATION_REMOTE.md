# E2｜W001 真实结果消费与问题分类

## 1. 身份

| 字段 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-E` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-E` |
| `delegation_id` | `D005` |
| 当前调用 | `C0014` |
| 被消费工单 | `W001` |
| Worker | `codex:OI-U2-F-OBS-20261118-01:worker:W1` |
| E 状态 | `IN_PROGRESS` |

本文件是原 executor:E1 对 W001 正式 Return 的专业消费。它接受 Worker 已完成的事实回交，不把 `STOP/BLOCKED` 等同于 D005、E 或父 Run 整体阻断。

## 2. 消费的正式原件

- 正式 Return：`daowei2026/observe-iterate@7beda1b54e7777b5b4f86ef6174376570e4c8b1a:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/WORKER_RETURN.json`
- 原始事实报告：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/FACT_REPORT.md`
- 原证据清单：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/MANIFEST.local.json`
- 首个阻断：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/first_blocker.json`
- 运行报告：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/output/u2_f_caegraph/definition_run_report.json`
- source staging：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/source_stage_report.json`
- 运行包装器：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/run_w001.sh`
- 写边界实现：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/boundary_runner.py`

## 3. Return 路由与身份核对

W001 正式 Return 的关键字段成立：

```text
schema=longrun-worker-return/v2
run_id=OI-U2-F-OBS-20261118-01
work_order_id=W001
order_ref=...@74562f...:work_orders/W001/ORDER.json
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
outcome=STOP
```

因此该 Return 可以由原 executor:E1 正式消费。

## 4. 已确认的真实运行事实

### 4.1 source staging 成功

```text
requested_commit=f4f0e4b276b1118b779473c1fbe462bc7a64b358
actual_head=f4f0e4b276b1118b779473c1fbe462bc7a64b358
detached_head=true
D_exists=true
C3_exists=true
verification_passed=true
status=SUCCESS
```

### 4.2 D/C3 没有修改

- D 脚本与原精确引用逐字节一致；
- C3 脚本与原精确引用逐字节一致；
- `repair.diff` 为 0 字节；
- `final_git_status.txt` 为空；
- 没有推送 source checkout。

### 4.3 D 真实启动一次并停止

```text
business_attempt_count=1
exit_code=1
elapsed_seconds=12.225031648995355
definition_run_report.completed=false
error_type=PermissionError
candidate_html=null
```

### 4.4 尚未进入 F 专业数据阶段

- `make_features` 尚未导入；
- F 尚未构造；
- 精确 `fields.json` 尚未检查；
- 没有调用 `f.rerun()`；
- 没有调用全历史 producer；
- 没有读取 Q/V；
- 没有 prepared tables、plot data 或候选 HTML；
- 没有 `DATA_READY`。

因此，W001 不能支持“F 正式结果存在”或“F 正式结果缺失”任一结论。

## 5. 首个真实阻断

D 在以下语句停止：

```python
from mquant.frame import CurrCalendar, CurrSof, KLine
```

调用链进入：

```text
/dwdhome/fy/BASE_E6_2_copy/mquant/apt/tool/misc.py:144
ProcessPoolExecutor(max_workers=os.getpid() - 2)
→ multiprocessing.Lock
→ _multiprocessing.SemLock
→ PermissionError: [Errno 13] Permission denied
```

W001 为落实其 run-root 写入收敛，额外建立了 Landlock：

```text
writes only under W001; reads retain existing access
```

独立的标准库 `multiprocessing.Lock` 诊断在同一限制下观察到：

```text
openat(..., "/dev/shm/sem.<random>", O_RDWR|O_CREAT|..., 0600)
= -1 EACCES
```

该诊断没有加载 D/F/Q/V。

## 6. 问题分类

### 6.1 不是 B 问题

W001 没有进入品种、时间或多尺度位置解析；没有证据要求改变：

```text
rb/hc/i
2021-01-01—2022-12-31
night_end_at_2300
5m
groupKnownFrom
```

### 6.2 不是 C 问题

没有生成 HTML，也没有触达面板、图元、hover、转换或交互。当前没有展示预期冲突证据。

### 6.3 不是 D 业务集成问题

D/C3 原件未修改；异常发生于平台 import 副作用，早于 F 构造、表读取和 CAEGraph 构图。没有实例、字段或 C2→D 接线错误证据。

### 6.4 是 W1 运行包络的机械问题

阻断由 Worker 为收敛写入而新增的 Landlock 与平台 import 时所需 POSIX semaphore IPC 发生冲突。Worker 自己也明确限制了结论：

> 该事实只证明严格 Landlock 条件下失败，不能断言无保护原环境失败，也不能断言 D/C3 或 F 产品缺陷。

按 E Workflow，这属于：

```text
只是 import / 路径 / 运行入口等机械问题
+ D/C/B/A 基准不变
→ 新 W1 revision
```

## 7. 授权边界判断

当前 Owner 机读授权为：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

E 不把它解释为可以直接在宿主 `/dev/shm` 写随机 semaphore 文件。

后继 W1 revision 应当在不扩大持久写入面的前提下，为进程提供**私有的 runtime IPC 视图**：

```text
namespace-local /dev/shm
→ bind 到本次工单 run root 内的 runtime/shm
→ 实际持久写入仍只发生在 /dwdhome/fy/BASE_E6_2_copy/**
```

若当前 Worker 无法建立这种私有 mount namespace，或只能直接写宿主 `/dev/shm` 才能运行，则必须停止并回 E；不得自行扩权。

## 8. 后继决定

签发新的 W1 revision，使用新的去重动作身份：

```text
work_order_id=W002
operation=caegraph_run_and_repair
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
```

W002 不是正式取数 W2。E Skill 中的“W1/W2”表示操作类别；本 Run 的顺序工单编号不等同于类别编号。图被接受后的正式取数将使用后续新的 work order identity。

W002 只处理：

1. 重新建立／核对固定 D commit 的专用 source staging；
2. 建立 run-root-backed 私有 `/dev/shm`；
3. 在同一安全包络下先运行最小 SemLock probe；
4. probe 通过后运行 D；
5. 返回候选 HTML 或新的首个真实阻断；
6. 仅在原 W1 机械修复边界内修改，并保留 diff。

## 9. 当前 E 状态

```text
W001 worker result: ACCEPTED_AS_FACT
W001 professional classification: MECHANICAL_EXECUTION_ENVELOPE_BLOCKER
return B/C/D: NO
candidate HTML: NONE
E3 acceptance: NOT_STARTED
E4 formal data admission: NOT_ALLOWED
DATA_READY: false
E professional_state: IN_PROGRESS
```

## 10. 续接点

W002 正式 Return 回原 executor:E1 后，继续同一：

```text
D005 / WI-E / M-E
```

进入新的 E2 消费；若生成 HTML，再进入 E3。只有最终图被 E 接受后，才能形成正式取数准入。
