# C0020｜D005/E Skill 续接：消费 W003 并签发 W004

## 1. 调用与专业身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0020`
- `invocation_token`：`eaf1f3fe7f3b499682f4f53ac564bcb2`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 本次 `delegation_ref`：`daowei2026/observe-iterate@7b2353915a15ecf29bc39eaaa0ea7f1f5be3dee8:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`

本次继续原 `D005 / WI-E / M-E`；没有新建 D，没有重跑 A～D，没有启动 Q/V。

## 2. 已正式消费的 W003 Return

### 正式 Return

`daowei2026/observe-iterate@d334e1629cef997c5ba35564ce518f682a672652:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/WORKER_RETURN.json`

### 主要事实原件

- `daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/FACT_REPORT.md`
- `daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/facts.json`
- `daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/MANIFEST.local.json`
- `daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/output/u2_f_caegraph/definition_run_report.json`
- `daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/diagnostics/module_path_check.json`

W003 的 `work_order_id / order_ref / worker / return_to` 均与 C0019 活跃工单一致。因此本 executor 已正式接受该 Worker Return，并在本次 V2 Return 的 `accepted_worker_refs` 中登记。

## 3. W003 的真实结果

### 3.1 已确认

```text
observe-iterate detached HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358
D/C3 modified=false
repair.diff=0 bytes
D attempt count=1
D exit code=1
definition_run_report.completed=false
candidate HTML=null
```

W003 使用正常平台入口，不使用 Landlock、namespace、独立 SemLock probe、sudo、mount 或平台 patch。它已经越过 W001/W002 的运行包络问题，真实进入 D。

### 3.2 首个阻断

```text
ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
```

阻断发生在 D 导入锁定构造模块时，早于 F 构造、`fields.json` 检查、正式表读取和 CAEGraph 构图。

### 3.3 未完成项

- F 未构造；
- `fields.json` 未检查；
- 未调用 `f.rerun()` 或全历史 producer；
- 未读取 Q/V；
- 没有 prepared tables、plot data 或 HTML；
- E3 未开始；
- E4 正式取数未准入；
- `DATA_READY=false`。

### 3.4 semaphore 事实

`/dev/shm/sem.*` 前后端点快照均为空；没有手工创建或清理对象。该结果不证明进程存续期间没有临时 semaphore，只证明未观察到端点残留。

## 4. 对有限路径检查的专业解释

W003 只确认当前旧 runtime package：

```text
/dwdhome/fy/BASE_E6_2_copy/mquant/tis/frp
```

没有 `fqv_kline_example.py`、`CommonPriceTurnGroupCandidates.py` 等锁定新模块，旧 `frp/__init__.py` 也未导出它们。

这不是 F 产品不存在的证据，也不是可以选择任意替代 constructor 的依据。

当前 D005 和 D 的 `source_refs` 已经给出唯一语义来源：

```text
daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767
```

该提交真实包含：

- `frp/fqv_kline_example.py`；
- `frp/CommonPriceTurnGroupCandidates.py`；
- 同一构造模块直接依赖的 Q/V 类与 `frpExample` 模块。

## 5. 包装事实与唯一机械后继

锁定 TIS README 明确说明：

- `__init__.py` 是自动生成的构建产物，不纳入 Git；
- clone 或切换分支后需要运行仓库自带 `seed_inits.py` 形成 Python package boundary。

因此本轮无需改 D 的实例、参数、字段或 C2 展示，也无需返回 D 重做业务集成。唯一语义一致的后继是：

```text
在新的 W run root staging 精确 TIS commit
→ 用锁定 seed_inits.py 生成空 package init
→ 将该 checkout 作为 run-local mquant.tis overlay
→ 验证所有构造模块 origin 都来自锁定 checkout
→ 运行原 D 一次
```

不从旧 runtime TIS 中拼装模块，不复制 `make_features`，不改写 F 构造。

## 6. E2 分类

完整原生产物：

`daowei2026/observe-iterate@b1625c62b599a2d693edb264ad815abf265853b7:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W003_RESULT_CLASSIFICATION_AND_W004_BASELINE.md`

分类：

```text
LOCKED_TIS_SOURCE_MATERIALIZATION_GAP
```

| 候选后继 | 判断 |
|---|---|
| 返回 B | 否；未触达位置 |
| 返回 C | 否；未生成图 |
| 返回 D | 否；locked source、实例和展示集成本身未被证伪 |
| 接受图／进入 E4 | 否；没有 HTML |
| 新 W1 revision | **是**；属于 import／路径／锁定 source materialization 的机械问题 |

这一后继符合 E Workflow：基准不变时，语法、import、路径和已确认 API 等机械问题续发 W1；无法判断的语义问题不得交 Worker 猜测。

## 7. 已签发 W004

### 7.1 工单正文

`daowei2026/observe-iterate@a243c56c9450c3a6964ce9b56701c921244821ad:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W004/ORDER.md`

### 7.2 机读工单

`daowei2026/observe-iterate@1ce39d12f160c624916e7e370692915f3b4af6d3:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W004/ORDER.json`

### 7.3 身份

```text
work_order_id=W004
operation category=new W1 revision
issuer=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
issuer_call_id=C0020
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
delegation_ref=D005 current C0018 version
```

## 8. W004 的具体边界

W004 将分别 staging：

```text
observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358
tis@2f460d663d821cf2ba25555eda13e78b697d0767
```

TIS checkout 位于：

```text
W004/source/mquant/tis
```

只运行锁定 `seed_inits.py` 生成空 `__init__.py`；不运行聚合导出脚本，不修改 TIS 业务模块。

run-local wrapper 将：

1. 导入基础 `mquant`；
2. 确认 `mquant.tis` 未预加载；
3. 把 W004 `source/mquant` 放到 `mquant.__path__` 首位；
4. 验证 constructor、F/Q/V 类和 `frpExample` 三个依赖模块的 `spec.origin` 全部位于锁定 TIS checkout；
5. 按原 CLI 运行 D。

Wrapper 不定义或替换 `make_features`，不修改 D/C3/平台，只做锁定 source 的 namespace 接线。

## 9. 当前权限和停止条件

W004 grant 与当前 Binding 一致：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

仍禁止：

- producer 重跑；
- Q/V 读取；
- SOF、品种、日历、5m、B 时间或 `groupKnownFrom` 改动；
- TIS 业务源码、D/C3 业务语义或平台库修改；
- C2 页面／面板／图元／转换改变；
- 非 `sem.*` 的共享内存写入；
- sudo、mount、namespace 或未授权路径。

若精确 F 没有既存 `fields.json`，Worker 必须停止，不调用 producer。

## 10. 正式数据边界

W004 随候选运行产生的 prepared tables、plot data 和 run report 仍只是诊断副产物：

```text
E4 admission=NONE
formal export order=NONE
DATA_READY=false
```

只有 E3 接受最终图后，才能形成正式取数准入。

## 11. 当前真实状态

```text
W001: completed STOP; previously consumed
W002: completed STOP; previously consumed
W003: completed STOP; consumed in C0020
W003 classification: LOCKED_TIS_SOURCE_MATERIALIZATION_GAP
W004: PUBLISHED_NOT_SENT
candidate HTML: none
E3: not started
E4 formal data admission: none
formal export order: none
DATA_READY: false
E professional_state: IN_PROGRESS
Q/V: not started
```

## 12. 主控派发与续接点

主控收到本 Return 后，应独立核验：

1. W004 `ORDER.json@1ce39d...` 与 `ORDER.md@a243c5...`；
2. grant 与当前 Binding 完全一致；
3. 物理 Worker 的模型、强度、cwd、空闲状态与单写者；
4. W003 已结束，W004 尚未发送且没有未知在途；
5. 两个 locked commit、run-local overlay 和 module-origin check 不修改平台或业务源码。

物理发送后按真实回执登记 `IN_FLIGHT`。

W004 正式 Return 必须回原 executor:E1，并引用：

`daowei2026/observe-iterate@1ce39d12f160c624916e7e370692915f3b4af6d3:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W004/ORDER.json`

收到后继续同一：

```text
D005 / WI-E / M-E
```

- 有 HTML：E2 核 overlay／脚本／diff 后进入 E3；
- 无 HTML：E2 消费新的首个阻断；
- 只有 E3 接受图后才允许 E4 和正式数据导出。

## 13. 完成判断

C0020 已完成 W003 的真实专业消费、问题分类和 W004 签发。原 D005/E Skill 尚未完成，因为 W004 尚未执行，没有候选 HTML，E3～E6 尚未发生。

```text
professional_state=IN_PROGRESS
accepted_worker_refs=[W003]
issued_order_refs=[W004]
remaining_scope=W004 + E2/E3 + accepted-graph-only E4/formal export + E5/E6
continuation=W004 Return to executor:E1
owner_request=null
```