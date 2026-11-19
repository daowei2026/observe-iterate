# C0021｜D005/E Skill 续接：消费 W004 并签发 W005

## 1. 调用与专业身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0021`
- `invocation_token`：`a113be25329642d3aeb2434046d5cb5b`
- `delegation_id`：`D005`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `delegation_ref`：`daowei2026/observe-iterate@7b2353915a15ecf29bc39eaaa0ea7f1f5be3dee8:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 本次 Invocation：`daowei2026/observe-iterate@c761e4467ffce37c775f6d5a3e489e5202c95b6f:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0021/INVOCATION.json`

本次继续原 `D005 / WI-E / M-E`；没有新建 D，没有重跑 A～D，没有启动 Q/V。

## 2. 已正式消费的 W004 Return

### 正式 Return

`daowei2026/observe-iterate@4fa846f81971100af6a7c16251ed011971100068:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/WORKER_RETURN.json`

### 主要事实原件

- `daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/FACT_REPORT.md`
- `daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/facts.json`
- `daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/MANIFEST.local.json`
- `daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/first_blocker.json`
- `daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/output/u2_f_caegraph/definition_run_report.json`
- `daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/module_overlay_report.json`
- `daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/diagnostics/locked_tis_t1_path_check.json`

W004 的 `work_order_id / order_ref / worker / return_to` 均与 C0020 活跃工单一致，因此本 executor 已正式接受该 Worker Return，并在本次 V2 Return 的 `accepted_worker_refs` 中登记。

## 3. W004 的真实结果

### 3.1 已确认

```text
observe-iterate detached HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358
tis detached HEAD=2f460d663d821cf2ba25555eda13e78b697d0767
D/C3/TIS tracked business source modified=false
seed_inits attempts=1, exit=0
generated empty init count=18
pretty-exports executed=false
locked target module origin checks=7/7 passed
D attempt count=1
D exit code=1
definition_run_report.completed=false
candidate HTML=null
```

W004 没有使用 Landlock、namespace、mount、sudo、平台 patch、producer 重跑或正式取数。

### 3.2 首个真实阻断

```text
ModuleNotFoundError: No module named 'mquant.tis.t1'
```

真实链路：

```text
D enters CurrSof
→ SOF context imports mquant.uplot.multiscale
→ multiscale imports mquant.tis.blk.gen
→ locked blk/gen.py executes from ..t1 import *
→ current locked-only mquant.tis package cannot resolve t1
```

constructor 模块已成功导入，但 `make_features(...)` 尚未调用；F 尚未构造，精确 `fields.json` 尚未检查。

### 3.3 未完成项

- 未读取 F 正式表；
- 未调用 `f.rerun()` 或全历史 producer；
- 未读取 Q/V 产品数据；
- 没有 prepared tables、plot data 或 HTML；
- E3 未开始；
- E4 正式取数未准入；
- `DATA_READY=false`。

## 4. 对 W004 overlay 的专业判断

W004 wrapper 把：

```text
W004/source/mquant
```

放到 `mquant.__path__` 首位，因此 Python 把锁定 checkout 中的 `mquant.tis` 当作完整 package。该 package 的搜索路径没有平台既有：

```text
/dwdhome/fy/BASE_E6_2_copy/mquant/tis
```

锁定 TIS commit 中又确实没有 `t1/`、`t1.py` 或同名 tree 条目，于是锁定 `blk/gen.py` 的相对依赖无法闭合。

这不表示 constructor 错误。锁定 TIS README 将 `t0/t1/t2/t3` 定义为特征层基础包；锁定 `blk/gen.py` 直接依赖这些包；精确 commit 却不携带这些目录。结合 D005 固定的 `BASE_E6_2_copy`，合理而且唯一的机械解释是：

> 锁定 commit 提供本次所需的新 source layer；基础 TIS 层由固定运行环境提供。二者必须显式分层组合，而不能把锁定 checkout 当作对平台 TIS 的完全替换。

## 5. E2 分类

完整原生产物：

`daowei2026/observe-iterate@43ff94cc90313b324cadbc4eba80fa5ec0eb2a3b:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W004_RESULT_CLASSIFICATION_AND_W005_BASELINE.md`

分类：

```text
LOCKED_TIS_LAYERED_PACKAGE_COMPOSITION_GAP
```

| 候选后继 | 判断 |
|---|---|
| 返回 B | 否；未触达位置 |
| 返回 C | 否；未生成图 |
| 返回 D | 当前否；D 的业务实例、字段、位置、展示与 source refs 未被证伪 |
| 接受图／进入 E4 | 否；没有 HTML |
| 新 W1 revision | **是**；属于 import／package path 的机械问题 |

## 6. 已签发 W005

### 6.1 工单正文

`daowei2026/observe-iterate@59205aa6c62349fdbf48ee841e9e7289d5f96ce6:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W005/ORDER.md`

### 6.2 机读工单

`daowei2026/observe-iterate@dae234377d403c08e8405efc64fbb390adac92bd:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W005/ORDER.json`

### 6.3 身份

```text
work_order_id=W005
operation category=new W1 revision
issuer=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
issuer_call_id=C0021
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
delegation_ref=D005 current C0018 version
```

## 7. W005 的具体修复边界

### 7.1 完整 materialize 锁定 TIS

W005 在新 checkout 中按锁定 README 依次运行：

```text
seed_inits.py
pretty-exports.py
```

保存生成的 `__init__.py` manifest、两个脚本日志与退出码、tracked diff，并保证不改任何已跟踪业务 `.py`。

### 7.2 建立两层 package，而不是独占 overlay

W005 在单个 Python 进程内建立：

```text
mquant.tis.__path__ =
[
  W005/source/mquant/tis,
  /dwdhome/fy/BASE_E6_2_copy/mquant/tis
]
```

根 package 由 wrapper 以 `ModuleType + ModuleSpec(is_package=True)` 明确建立，不执行未知 root init，不把路径变更写入平台文件。

### 7.3 模块来源硬合同

必须来自锁定 checkout：

```text
fqv_kline_example
F/Q/V classes
Wave / STCalendar / ScaleTurn
blk.gen
```

必须来自固定平台基础 TIS：

```text
t0 / t1 / t2 / t3
```

所有 origin／package locations 写入 `layered_tis_report.json`。任何不匹配、提前加载或第三来源都必须停止，不运行 D。

### 7.4 D 运行

origin contract 全部通过后，按原 CLI 用 `runpy.run_path` 执行原 D 一次，优先返回：

1. 可打开候选 HTML；或
2. 新的首个真实阻断。

W005 不修改 D/C3/TIS 业务源码或平台包，不使用 Landlock、namespace、mount、sudo 或平台 patch。

## 8. 当前权限和停止条件

W005 grant 与当前 Binding 一致：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

仍禁止：

- producer 重跑；
- Q/V 产品读取；
- SOF、品种、日历、5m、B 时间或 `groupKnownFrom` 改动；
- TIS 业务源码、D/C3 业务语义或平台文件修改；
- C2 页面／面板／图元／转换改变；
- 第三来源模块；
- 非 `sem.*` 的共享内存写入；
- sudo、mount、namespace 或未授权路径。

精确 F 没有既存 `fields.json` 时仍必须停止，不调用 producer。

## 9. 正式数据边界

W005 随候选运行产生的 prepared tables、plot data 和 run report 仍只是诊断副产物：

```text
E4 admission=NONE
formal export order=NONE
DATA_READY=false
```

只有 E3 接受最终图后，才能形成正式取数准入。

## 10. 当前真实状态

```text
W001: completed STOP; previously consumed
W002: completed STOP; previously consumed
W003: completed STOP; previously consumed
W004: completed STOP; consumed in C0021
W004 classification: LOCKED_TIS_LAYERED_PACKAGE_COMPOSITION_GAP
W005: PUBLISHED_NOT_SENT
candidate HTML: none
E3: not started
E4 formal data admission: none
formal export order: none
DATA_READY: false
E professional_state: IN_PROGRESS
Q/V: not started
```

## 11. 主控派发与续接点

主控收到本 Return 后，应独立核验：

1. W005 `ORDER.json@dae234...` 与 `ORDER.md@59205a...`；
2. grant 与当前 Binding 完全一致；
3. 物理 Worker 的模型、强度、cwd、空闲状态和单写者；
4. W004 已结束，W005 尚未发送且无未知在途；
5. layered package 只有锁定 TIS 与固定 runtime TIS 两个来源；
6. package build products 和 wrapper 均留在 W005 run root，不修改平台或业务源码。

物理发送后按真实回执登记 `IN_FLIGHT`。

W005 正式 Return 必须回原 executor:E1，并引用：

`daowei2026/observe-iterate@dae234377d403c08e8405efc64fbb390adac92bd:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W005/ORDER.json`

收到后继续同一：

```text
D005 / WI-E / M-E
```

- 有 HTML：E2 核 package report／脚本／diff 后进入 E3；
- 无 HTML：E2 消费新的首个阻断；
- 只有 E3 接受图后才允许 E4 和正式数据导出。

## 12. 完成判断

C0021 已完成 W004 的真实专业消费、问题分类和 W005 签发。原 D005/E Skill 尚未完成，因为 W005 尚未执行，没有候选 HTML，E3～E6 尚未发生。

```text
professional_state=IN_PROGRESS
accepted_worker_refs=[W004]
issued_order_refs=[W005]
remaining_scope=W005 + E2/E3 + accepted-graph-only E4/formal export + E5/E6
continuation=W005 Return to executor:E1
owner_request=null
```