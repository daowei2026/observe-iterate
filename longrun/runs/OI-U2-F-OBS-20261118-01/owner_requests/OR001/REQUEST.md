# OR001｜请求补充 CAEGraph 运行所需的临时 POSIX semaphore 权限

## 1. 请求身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `request_id`：`OR001`
- `issuer_call_id`：`C0016`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`

## 2. 为什么现在需要 Owner 输入

W001 与 W002 已分别真实确认：

1. 平台在导入 `mquant.frame` 时初始化 `ProcessPoolExecutor`；
2. Python multiprocessing 因此需要创建 `/dev/shm/sem.<random>` POSIX semaphore；
3. W001 的工作区-only Landlock 会拒绝该写入；
4. W002 尝试建立 backing 位于工作区内的私有 `/dev/shm`，但当前物理 Worker 在写 `/proc/self/uid_map` 时得到 `Operation not permitted`，无法进入 user/mount namespace；
5. 两次均未构造 F、未检查 `fields.json`、未调用 producer、未生成 HTML。

当前 Binding 只授权：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

原 executor:E1 不自行把宿主 `/dev/shm` 写入解释为已授权，也不再让 Worker 猜测旁路。

## 3. 请求 Owner 确认的首选文本

请确认是否将以下文本作为本 Run 的 `caegraph_run_and_repair` 机读授权补正，并据此更新 Run Binding 与 Resource Binding：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

该补正的业务／操作限制为：

> `/dev/shm` 只允许本 Run 的 CAEGraph 运行进程及其子进程为 Python multiprocessing 临时创建和删除 POSIX semaphore 对象 `sem.*`；不得写任意共享内存 payload、不得使用 sudo、不得建立 mount 绕过、不得 patch 平台源码、不得调用 F producer、不得读取 Q/V、不得据此启动正式数据导出。

## 4. 若 Binding 只能登记目录前缀

若机读 Binding 不支持 `/dev/shm/sem.*` 形式，请 Owner 改为确认：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/**
```

同时必须把下面限制逐字放入 `authority_quote`：

> `/dev/shm/**` 仅用于本 Run CAEGraph 进程树的临时 POSIX semaphore `sem.*` 创建和删除，不授权其他共享内存内容或其他进程使用。

## 5. 可接受的替代答复

若 Owner 不希望补充宿主 `/dev/shm` 权限，也可以提供或指定一个已具有私有可写 `/dev/shm` 的物理运行环境。该环境必须满足：

- 不要求当前 Worker 写 `/proc/self/uid_map`；
- 不要求 sudo；
- 不修改 D/C3、平台源码或业务实例；
- D 的持久产物仍只写 `/dwdhome/fy/BASE_E6_2_copy/**`；
- 物理 Worker、cwd、模型／强度和单写者由主控重新核验并进入 Binding。

## 6. Owner 需要回答什么

请明确选择其一：

```text
A. 确认首选 sem.* 机读补正；
B. 确认目录前缀补正及逐字限制；
C. 不补充宿主权限，提供已具备私有 /dev/shm 的运行环境；
D. 不继续该 E 运行。
```

## 7. 获得答复后的动作

- A/B：主控更新并回读 Binding；原 executor:E1 签发新的 W1 revision，按正常平台入口运行 D 一次。
- C：主控建立并核验新物理绑定；原 executor:E1 签发新的 W1 revision。
- D：原 executor:E1 按 E Skill 形成阻塞交付，不伪造 HTML 或正式数据。

无论哪种答复，都继续原：

```text
D005 / WI-E / M-E
```

不新建 D，不重跑 A～D，不启动 Q/V。

## 8. 支撑引用

- E2 分类：`daowei2026/observe-iterate@56ecda308a8ef02ec9848d44ff7bae78c0a56118:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W002_RESULT_CLASSIFICATION.md`
- W001 Return：`daowei2026/observe-iterate@7beda1b54e7777b5b4f86ef6174376570e4c8b1a:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/WORKER_RETURN.json`
- W002 Return：`daowei2026/observe-iterate@08f9944755ac4ba8786249edb25ea4f5b5cab555:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/WORKER_RETURN.json`
- W002 facts：`daowei2026/observe-iterate@613234399b4c5888524a8a6b9086124265f2040e:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/FACT_REPORT.md`
- 当前 Binding：`daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
