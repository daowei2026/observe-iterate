# E2｜OR001 采用消费与 W003 运行基准

## 1. 身份

| 字段 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-E` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-E` |
| `delegation_id` | `D005` |
| 当前调用 | `C0019` |
| executor | `chatgpt:OI-U2-F-OBS-20261118-01:executor:E1` |
| 后继工单 | `W003`，操作类别为新的 W1 revision |

本记录消费 manager C0018 已签认的同一 D005 当前版本、Owner 对 OR001 第一项的真实采用记录和新 Binding。它只恢复原 E Skill 的运行后继，不重做 A～D，不修改 D/C3、B 位置或 C2 展示预期，也不启动 Q/V。

## 2. 当前有效续接来源

- manager C0018 Return：`daowei2026/observe-iterate@7256830d9f7aae47668dcf7c16e0424db7866726:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0018/PRO_RETURN.json`
- 当前 D005 JSON：`daowei2026/observe-iterate@7b2353915a15ecf29bc39eaaa0ea7f1f5be3dee8:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 当前 D005 正文：`daowei2026/observe-iterate@51bb129c486c2654286fb9d990c18865c3d847ab:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.md`
- manager 报告：`daowei2026/observe-iterate@97864d02d19ee3ddfa0a9750589d9f75047aa5a9:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0018/MANAGER_REPORT.md`
- 统一全景：`daowei2026/observe-iterate@f40490dcf8c4aa0d2625cba615ce7ca805d1fa52:longrun/runs/OI-U2-F-OBS-20261118-01/business_control/TASK_PROGRESS.md`

## 3. OR001 采用与等待解除

原 executor:E1 在 C0016 的分类为：

```text
RUNTIME_IPC_CAPABILITY_AND_AUTHORITY_GAP
```

原请求：

`daowei2026/observe-iterate@6f2fb38d8ff7e45c1ae6e234eaf2c95b215ee4a9:longrun/runs/OI-U2-F-OBS-20261118-01/owner_requests/OR001/REQUEST.md`

Owner 第一项采用记录：

`daowei2026/observe-iterate@1e6392ad185c9be31367f0001f82e83aa53ad14e:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_OR001_FIRST_OPTION_ADOPTION_20261119.md`

该记录采用 Owner 既有原话“碰到需要我处理的问题，先选第一项”作为 OR001 第一项 A 的真实选择来源；没有伪称新收到逐字 INI。

当前 Binding：

- `daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- `daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`

当前 operation-specific grant 为：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

`authority_quote` 进一步限制：`/dev/shm` 只用于本 Run CAEGraph 进程树临时创建和删除 Python multiprocessing 的 `sem.*`；不授权任意 shared-memory payload、sudo、mount 绕过、平台源码 patch、F producer、Q/V 或正式数据导出。

因此 C0016 的 Owner 等待条件已经满足。E 从 `WAITING_OWNER` 恢复为 `IN_PROGRESS`，但这不表示 W 已执行、图已接受或 E 已完成。

## 4. W001／W002 的继承事实

- W001、W002 都已结束并由原 E1 接受为事实；当前无 Worker 工单在途。
- W001 证明正常平台导入需要 `/dev/shm/sem.<random>`，但其额外 Landlock 阻断了该写入。
- W002 试图建立工作区-backed private `/dev/shm`，但当前 Worker 无法写 `/proc/self/uid_map`；其 SemLock probe 和 D attempt 都为 0。
- 两次均未构造 F、未检查 `fields.json`、未调用 producer、未生成候选 HTML。
- D 与 C3 均未修改。

W003 不重发 W001/W002，也不复用它们的动作身份或输出目录。

## 5. W003 最小运行基准

### 5.1 唯一专业运行输入

- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- C2 当前预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- 固定源码提交：`f4f0e4b276b1118b779473c1fbe462bc7a64b358`

### 5.2 实际工作区与输出

```text
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT=$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003
SOURCE_ROOT=$RUN_ROOT/source/observe-iterate
OUTPUT_ROOT=$RUN_ROOT/output/u2_f_caegraph
LOG_ROOT=$RUN_ROOT/logs
```

W003 使用新的 run-local detached source staging；W001/W002 目录只作历史证据，不修改、不覆盖、不清理。

### 5.3 运行包络

W003 使用工作区既有正常平台入口运行 D：

- 复用 `/dwdhome/fy/BASE_E6_2_copy/m3rc`；
- 复用工作区已存在的 Python 依赖和 TLS 接线；
- 所有缓存、日志、输出和 source staging 写入 W003 run root；
- 不再添加 W001 的 Landlock；
- 不再尝试 W002 的 user/mount namespace；
- 不使用 sudo、mount、平台 patch 或 producer fallback；
- `/dev/shm` 只允许 D 进程树及其 Python multiprocessing 子进程临时创建／删除 `sem.*`。

### 5.4 第一次动作

按 E Skill 的执行优先原则，W003 应先真实运行 D 一次，优先返回：

1. 可打开候选 HTML；或
2. 新的首个真实阻断。

不以单独 SemLock probe 替代 D 首次运行；D 本身会真实经过平台 import。Worker 应记录实际 D attempt count 和退出码。

## 6. 可修范围与停止边界

W003 仍只可直接修：

- Python 语法、import、模块或文件路径；
- 锁定版本中已核实的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、文件名、日志和静态 HTML 接线；
- 本工单明确允许的临时 semaphore 运行接线。

必须停止并回 E，如果：

- 精确 F 实例没有既存 `fields.json`；
- 需要调用 `f.rerun()` 或全历史 producer；
- 需要改变 SOF、品种、日历、5m、2021—2022 或 `groupKnownFrom`；
- 需要读取 Q/V；
- 需要改变业务字段、面板、图元、标准化、交互或阅读语义；
- 需要写 `/dev/shm` 中非 `sem.*` 内容；
- 需要 sudo、mount、namespace、平台源码 patch 或其他未授权路径；
- 正确修法不唯一，或无法判断是否影响业务语义；
- 发现同一 W003 未知结果、动作在途或非单写者。

## 7. 临时 semaphore 的最小事实记录

W003 可以在 D 运行前后只读列出 `/dev/shm/sem.*` 的名称和元数据，以帮助区分既有对象与本次运行残留，但：

- 不删除任何运行前已经存在的 `sem.*`；
- 不手工创建测试 semaphore；
- 不删除无法证明属于本次 D 进程树的对象；
- 正常清理由 Python 进程树自己完成；
- 若本次可归属 `sem.*` 在进程结束后残留，返回 E 说明，不扩大清理动作。

## 8. W1 与正式数据的边界

D 脚本若随候选运行产生 `prepared_tables/`、`plot_data/` 或 `definition_run_report.json`，它们在 W003 中仍只是运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不属于正式数据导出；
- 不允许标记 `DATA_READY`；
- 不得为扩大导出而修改脚本。

只有候选 HTML 经原 E1 在 E3 接受后，才允许按未扩大的 `caegraph_data_export` grant 另签正式取数工单。

## 9. 当前状态与续接

```text
OR001: satisfied by recorded first-option adoption
E: IN_PROGRESS
W003: to be issued, not yet sent
candidate HTML: none
E3: not started
formal data admission: none
DATA_READY: false
Q/V: not started
```

W003 Return 回原 executor:E1 后，继续同一：

```text
D005 / WI-E / M-E
```

有 HTML 时进入 E2/E3；无 HTML 时消费新的首个阻断。发布或发送 W003 均不等于 E 完成。
