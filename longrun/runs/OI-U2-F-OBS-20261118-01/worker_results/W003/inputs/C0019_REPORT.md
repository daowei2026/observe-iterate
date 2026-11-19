# C0019｜D005/E Skill 续接：消费 OR001 采用并签发 W003

## 1. 调用与专业身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0019`
- `invocation_token`：`567acbc883844046a9489b47640d6868`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 本次 `delegation_ref`：`daowei2026/observe-iterate@7b2353915a15ecf29bc39eaaa0ea7f1f5be3dee8:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`

本次继续原 `D005 / WI-E / M-E`。没有新建 D，没有重跑 A～D，没有启动 Q/V。

## 2. 实际采用的当前续接原件

- manager C0018 Return：`daowei2026/observe-iterate@7256830d9f7aae47668dcf7c16e0424db7866726:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0018/PRO_RETURN.json`
- 当前 D005 正文：`daowei2026/observe-iterate@51bb129c486c2654286fb9d990c18865c3d847ab:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.md`
- manager 报告：`daowei2026/observe-iterate@97864d02d19ee3ddfa0a9750589d9f75047aa5a9:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0018/MANAGER_REPORT.md`
- 统一任务全景：`daowei2026/observe-iterate@f40490dcf8c4aa0d2625cba615ce7ca805d1fa52:longrun/runs/OI-U2-F-OBS-20261118-01/business_control/TASK_PROGRESS.md`
- C0016 当前有效 Return：`daowei2026/observe-iterate@4e0087f355313eb71914ad7d5d568737ae2f8fd6:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0016/PRO_RETURN.json`
- C0017 协议补正 Return：`daowei2026/observe-iterate@02331f1a4c84746a3e2a4d69dc9373a710ae47b7:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0017/PRO_RETURN.json`

本次重新亲读并采用固定 E Skill 的：`SKILL.md`、`WORKFLOW.md`、`IO_SPEC.md`、`WORKER_DELEGATION.md`、`RUN_REPAIR_ORDER_TEMPLATE.md`、`DATA_EXPORT_ORDER_TEMPLATE.md` 与通用 `WORKER_ORDER.md`。

## 3. Owner 输入与当前 Binding 的专业消费

### 3.1 Owner 第一项的真实采用

采用记录：

`daowei2026/observe-iterate@1e6392ad185c9be31367f0001f82e83aa53ad14e:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_OR001_FIRST_OPTION_ADOPTION_20261119.md`

它保留 Owner 原话：

> 碰到需要我处理的问题，先选第一项

并把它实际采用为 OR001 的第一项 A：确认首选 `sem.*` 机读补正。该记录没有伪称新收到逐字 INI。

### 3.2 当前 operation-specific grant

- Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- Resource Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`

当前运行 grant 为：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

`authority_quote` 继续限制 `/dev/shm` 只能被本 Run 的 CAEGraph 进程树用于 Python multiprocessing 临时 `sem.*` 的创建和删除，并明确排除任意共享内存 payload、sudo、mount 绕过、平台 patch、F producer、Q/V 和正式数据导出。

`caegraph_data_export` grant 没有扩大，仍只覆盖工作区；当前 E3 尚未接受图，E4 也未准入，因此本次不签发正式数据导出工单。

### 3.3 状态转换

C0016 的 `WAITING_OWNER` 是采用前的真实状态。OR001 第一项现已采用，当前 Binding 和同一 D005 机读包络也已更新，因此：

```text
E: WAITING_OWNER → IN_PROGRESS
```

这只表示运行前提已经具备，不表示 Worker 已发送、D 已运行、图已接受或 E 已完成。

## 4. W001／W002 历史的继承边界

- W001 Return：`daowei2026/observe-iterate@7beda1b54e7777b5b4f86ef6174376570e4c8b1a:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/WORKER_RETURN.json`
- W002 Return：`daowei2026/observe-iterate@08f9944755ac4ba8786249edb25ea4f5b5cab555:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/WORKER_RETURN.json`

两者均已在此前调用中由原 E1 正式消费，本调用不重复消费，所以 C0019 的 `accepted_worker_refs=[]`。

继承事实：

- W001 的额外 Landlock 阻断了平台所需 `/dev/shm/sem.*`；
- W002 无权建立 user/mount namespace，SemLock probe 和 D attempt 都为 0；
- 两次均没有构造 F、检查 `fields.json`、调用 producer 或生成 HTML；
- D/C3 均未修改；
- 当前没有 Worker 工单在途。

新授权正好补足原分类中的运行写面缺口。因此不返回 B/C/D，直接续发新的 W1 revision。

## 5. 已形成的原生产物

### E2／W003 最小基准

`daowei2026/observe-iterate@7881b0694af2166ea9d0d041938e36454085843b:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_OR001_RESOLUTION_AND_W003_BASELINE.md`

该基准固定：

- Owner 采用和当前 grant；
- W001/W002 的继承事实；
- D、C3、C2 和固定 source commit；
- W003 run root 和正常平台入口；
- 不再使用 Landlock 或 namespace；
- `/dev/shm/sem.*` 的最小审计边界；
- W1 诊断副产物与正式 W2 数据的边界。

## 6. 已签发 W003

### 6.1 工单正文

`daowei2026/observe-iterate@2ca58580f2d3334a7f9218deb4d254c8ec0a81c8:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W003/ORDER.md`

### 6.2 机读工单

`daowei2026/observe-iterate@dd919cca7df1203f7962888b4ecf8b7d24048c43:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W003/ORDER.json`

### 6.3 身份与路由

```text
work_order_id=W003
parent delegation=D005 current C0018 version
issuer=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
issuer_call_id=C0019
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
operation=caegraph_run_and_repair
```

W003 是新的 W1 运行／有限机械修复 revision，不是正式取数 W2。

## 7. W003 的实际动作

### 7.1 source 与输出

```text
RUN_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003
SOURCE_ROOT=$RUN_ROOT/source/observe-iterate
OUTPUT_ROOT=$RUN_ROOT/output/u2_f_caegraph
LOG_ROOT=$RUN_ROOT/logs
```

source staging 必须 detached checkout 到：

```text
f4f0e4b276b1118b779473c1fbe462bc7a64b358
```

W001/W002 目录完整保留，不复用、不修改、不清理。

### 7.2 正常平台入口

W003 复用 W001 已确认的 `m3rc`、工作区 Python 依赖、TLS 接线和 cache 重定向，但直接运行 D：

```text
u2_f_caegraph_definition.py
→ output/u2_f_caegraph
```

明确禁止：

- W001 的 Landlock／`boundary_runner.py`；
- W002 的 `unshare`／user or mount namespace；
- sudo、mount、平台源码 patch；
- 单独 probe 替代 D 首次真实运行。

### 7.3 semaphore 范围

- 只有 D 进程树及其 Python multiprocessing 子进程可以临时创建／删除 `/dev/shm/sem.*`；
- wrapper 不手工创建测试 semaphore；
- 不读取或写入非 `sem.*` 对象；
- 运行前后只读记录 `sem.*` 名称和元数据；
- 不删除运行前已有对象或无法证明属于本次进程树的对象；
- 若有可归属残留，保留事实回 E，不扩大清理动作。

### 7.4 第一次回报优先级

按 E Skill，W003 先真实运行 D 一次，优先返回：

1. 可打开候选 HTML；或
2. 新的首个真实阻断。

如精确 F 实例没有既存 `fields.json`，必须停止，不调用 `f.rerun()` 或全历史 producer。

## 8. W003 的专业边界

Worker 只可修复不会改变业务含义的确定性机械问题：语法、import、路径、已核 API、明确类型和输出接线。

Worker 不可：

- 改 SOF、品种、日历、5m、2021—2022 或 `groupKnownFrom`；
- 读 Q/V；
- 增删替换业务字段或使用近似值；
- 改 C2 页面、面板、图元、时间、标准化、交互或阅读语义；
- 写非 `sem.*` 的 `/dev/shm` 内容；
- 修改平台库或运行 producer；
- 判断最终图是否接受；
- 启动正式数据导出或宣称 `DATA_READY`。

D 候选运行若顺带产生 prepared tables、plot data 或 run report，它们仍只是诊断副产物。

## 9. 当前真实状态

```text
A/B/C/D: complete
OR001: satisfied by recorded first-option adoption
E: IN_PROGRESS
W001: completed STOP; previously consumed
W002: completed STOP; previously consumed
W003: PUBLISHED_NOT_SENT
worker currently in flight: none at executor return boundary
candidate HTML: none
E3: not started
E4 formal-data admission: none
formal export order: none
DATA_READY: false
Q/V: not started
```

发布 W003 不等于物理发送、Worker 执行或 E 完成。

## 10. 主控派发前与续接点

主控收到本 Return 后，应独立核验：

1. W003 `ORDER.json@dd919c...` 与 `ORDER.md@2ca585...`；
2. grant 与当前 Binding 的 operation、context、allowed writes 和 authority quote 精确一致；
3. 物理 Worker 仍为本 Run 专用 W1、目标 GPT-6.1 Sol Max，cwd 为 `/dwdhome/fy/BASE_E6_2_copy`；
4. W001/W002 已结束，W003 尚未发送且无未知在途；
5. 当前工作区与 `/dev/shm/sem.*` 使用满足真实进程归属和单写者约束。

实际发送后，主控按真实回执登记 `IN_FLIGHT`。

W003 正式 Return 必须回原 executor:E1，并引用：

`daowei2026/observe-iterate@dd919cca7df1203f7962888b4ecf8b7d24048c43:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W003/ORDER.json`

收到后继续同一：

```text
D005 / WI-E / M-E
```

- 有 HTML：E2 核脚本／diff 后进入 E3；
- 无 HTML：E2 消费新的首个阻断；
- 只有 E3 接受图后才允许 E4 和正式数据导出。

## 11. 完成判断

C0019 已完成：

- 当前 D005、Owner 采用与 Binding 的专业消费；
- E 从 Owner 等待恢复为运行中；
- W003 最小基准与真实 W1 revision 的签发；
- operation-specific 权限、运行入口、停止边界和续接点的固定。

原 D005/E Skill 仍未完成，因为 W003 尚未执行，没有候选 HTML，E3～E6 均未发生。

```text
professional_state=IN_PROGRESS
issued_order_refs=[W003]
accepted_worker_refs=[]
remaining_scope=W003 + E2/E3 + accepted-graph-only E4/formal export + E5/E6
continuation=W003 Return to executor:E1
owner_request=null
```
