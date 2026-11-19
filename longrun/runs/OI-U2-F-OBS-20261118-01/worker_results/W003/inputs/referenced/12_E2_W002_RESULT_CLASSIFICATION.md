# E2｜W002 真实结果消费、问题分类与后继边界

## 1. 身份

| 字段 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-E` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-E` |
| `delegation_id` | `D005` |
| 当前调用 | `C0016` |
| 被消费工单 | `W002` |
| Worker | `codex:OI-U2-F-OBS-20261118-01:worker:W1` |
| E 阶段状态 | `NEEDS_OWNER_INPUT` |

本文件是原 executor:E1 对 W002 正式 Return 的专业消费。它接受 Worker 的真实事实回交，不把 `STOP` 等同于 E、D005 或整个 Run 已完成，也不把一次 namespace 失败扩写成 D/F/CAEGraph 的缺陷。

## 2. 正式消费原件

- W002 正式 Return：`daowei2026/observe-iterate@08f9944755ac4ba8786249edb25ea4f5b5cab555:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/WORKER_RETURN.json`
- 完整事实报告：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/FACT_REPORT.md`
- 原证据清单：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/MANIFEST.local.json`
- source staging：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/source_stage_report.json`
- private-shm 报告：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/private_shm_report.json`
- 首个阻断：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/first_blocker.json`
- 物理执行回执：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/execution_receipt.json`
- 原始 namespace stderr：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/logs/private_shm_mount.log`

## 3. Return 路由与身份核对

W002 Return 的关键身份成立：

```text
schema=longrun-worker-return/v2
run_id=OI-U2-F-OBS-20261118-01
work_order_id=W002
order_ref=...@2bdc0b...:work_orders/W002/ORDER.json
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
outcome=STOP
```

因此该 Return 由原 executor:E1 正式消费，并在 C0016 Return 中列入 `accepted_worker_refs`。

## 4. W002 已确认的事实

### 4.1 source staging 再次成功

```text
requested_commit=f4f0e4b276b1118b779473c1fbe462bc7a64b358
actual_head=f4f0e4b276b1118b779473c1fbe462bc7a64b358
detached_head=true
D_exists=true
C3_exists=true
verification_passed=true
status=SUCCESS
```

D 与 C3 均与锁定源码逐字节一致：

- 没有修改；
- `repair.diff` 为 0 字节；
- `final_git_status.txt` 为空；
- 没有推送 source checkout。

### 4.2 私有 namespace 只尝试一次并在入口停止

实际命令：

```text
/usr/bin/unshare --user --map-root-user --mount --fork \
  /bin/bash <W002/private_shm_episode.sh> <W002 run root>
```

实际 stderr：

```text
unshare: write failed /proc/self/uid_map: Operation not permitted
```

事实边界：

```text
namespace_attempt_count=1
namespace_exit_code=1
namespace_inner_entered=false
mount_bind_attempted=false
private_shm_backing_proven=false
```

没有使用 PID namespace。

### 4.3 后续动作均未发生

```text
SemLock probe attempt count=0
D attempt count=0
D exit code=null
F constructed=false
fields.json=NOT_CHECKED
candidate HTML=null
definition_run_report=null
prepared tables=null
plot data=null
DATA_READY=false
```

本次也没有：

- 应用 Landlock；
- 直接写宿主 `/dev/shm`；
- 使用 sudo；
- 尝试替代 namespace；
- patch 平台库；
- 调用 `f.rerun()`；
- 调用全历史 producer；
- 读取 Q/V。

因此 namespace 的退出码 1 不是 D 的退出码，不能被记录为 D 运行失败。

## 5. 与 W001 合并后的最小因果链

W001 已确认：

```text
平台 import mquant.frame
→ ProcessPoolExecutor
→ multiprocessing.SemLock
→ 需要 /dev/shm/sem.<random>
```

在 W001 新增的严格 Landlock 下，宿主 `/dev/shm` 写入被拒绝。

W002 为避免扩大宿主持久写入范围，尝试把 namespace-local `/dev/shm` 映射到授权工作区内的 `W002/runtime/shm`；但宿主禁止当前 Worker 建立所需 user namespace，失败发生在写 `/proc/self/uid_map`，尚未进入 mount namespace 内部。

所以当前已经证实：

1. 正常平台 import 需要 POSIX semaphore IPC；
2. 只允许工作区写入的严格 Landlock 会阻断该 IPC；
3. 当前物理 Worker 不能通过 user+mount namespace 把 `/dev/shm` 重新映射到授权工作区；
4. 尚无证据说明 D、C3、F 产品或 CAEGraph 本身有问题。

## 6. E2 专业分类

### 6.1 不是 B 问题

没有触达品种、时间、日历、多尺度或 `groupKnownFrom`。没有理由改变 B-POS-001。

### 6.2 不是 C 问题

没有生成 HTML、图层、图元、hover 或显示变换。没有 C2 冲突证据。

### 6.3 不是 D 业务集成问题

D/C3 未修改，D 本轮甚至没有启动；没有实例、字段或集成错误证据。

### 6.4 也不再只是可在原授权内盲目续修的普通 import/path 问题

W001 的机械阻断已被 W002 进一步定位为：

```text
平台 IPC 需要宿主 /dev/shm
AND
当前 allowed_writes 只覆盖 /dwdhome/fy/BASE_E6_2_copy/**
AND
当前 Worker 无权建立 private user/mount namespace
```

在现有证据下，继续执行需要至少满足以下之一：

1. Owner 明确补充授权本 Run 的运行进程及其子进程创建／删除临时 POSIX semaphore 对象；或
2. 提供一个已经具有私有可写 `/dev/shm` 的物理运行环境，不要求当前 Worker 自行创建 user namespace。

这已经是运行能力与授权边界问题，不应再由 Worker 猜测其他旁路。

### 6.5 最终分类

```text
RUNTIME_IPC_CAPABILITY_AND_AUTHORITY_GAP
```

## 7. 为什么本次不签发 W003

在当前 Binding 下直接运行会写入授权路径之外的宿主 `/dev/shm`；W002 又证明当前 Worker 无法建立授权路径 backing 的私有 `/dev/shm`。在没有新授权或新运行环境事实前再签发 W1 revision，只会重复已知冲突，或迫使 Worker自行扩权／绕过平台。

因此：

- 不返回 B/C/D；
- 不接受图；
- 不启动正式取数；
- 不继续签发无新前提的 Worker 工单；
- 形成精确 Owner 请求。

## 8. 当前有效授权与缺口

当前 Binding 的 `caegraph_run_and_repair` 为：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

这不包含宿主 `/dev/shm`。本 executor 不自行把标准库／平台的 semaphore 写入解释为已授权。

## 9. 推荐的最小 Owner 补正

优先建议 Owner 确认一条 operation-specific 补正，允许本 Run 的 W1 运行进程及其子进程仅为 Python multiprocessing 创建和删除临时 POSIX semaphore：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

该补正不授权：

- 任意 `/dev/shm` payload；
- 其他共享内存文件；
- sudo；
- mount／namespace 绕过；
- 平台源码 patch；
- producer 重跑；
- Q/V；
- 正式数据导出。

若 Binding 实现只能登记目录前缀，则需要 Owner 明确确认：

```ini
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/**
```

同时在 `authority_quote` 中逐字限制 `/dev/shm` 仅用于本次进程树的临时 `sem.*` 对象，不得写其他共享内存内容。

替代方案是由 Owner／基础设施提供一个已经具备私有可写 `/dev/shm` 的运行环境；在该环境中不需要当前 Worker 写 `/proc/self/uid_map` 或建立 mount namespace。

## 10. 获得补正后的预定续接

Owner 补正被主控写入并回读新的 Run/Resource Binding 后，原 executor:E1 将签发新的 W1 revision，要求：

1. 保持同一 D commit、D/C3、实例、位置和 C2；
2. 不再使用 W001 Landlock 或 W002 namespace 方案；
3. 只运行标准平台入口；
4. 对 `/dev/shm` 仅保留临时 semaphore 事实和清理／残留报告；
5. 运行 D 一次，返回 HTML 或新的首个真实阻断；
6. 仍不得调用 producer 或读取 Q/V。

## 11. 当前 E 状态与续接点

```text
W001 Return: ACCEPTED_AS_FACT
W002 Return: ACCEPTED_AS_FACT
candidate HTML: NONE
E3: NOT_STARTED
E4 formal data admission: NOT_ALLOWED
DATA_READY: false
E professional_state: NEEDS_OWNER_INPUT
```

续接点：Owner 对 `OWNER_REQUEST_OR001` 作出明确答复，并由主控更新／回读 Binding 后，继续原：

```text
D005 / WI-E / M-E
```

不新建 D，不重跑 A～D。
