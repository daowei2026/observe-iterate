# E2｜W004 真实结果消费、问题分类与 W005 运行基准

## 1. 身份

| 字段 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-E` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-E` |
| `delegation_id` | `D005`（C0018 当前版本） |
| 当前调用 | `C0021` |
| 被消费工单 | `W004` |
| 后继工单 | `W005`，新的 W1 revision |
| executor | `chatgpt:OI-U2-F-OBS-20261118-01:executor:E1` |

本文件由原 executor:E1 消费 W004 正式 Return 后形成。W004 的 `STOP` 是真实工单结果，不等于 D005/E 或父 Run 已完成，也不等于 F、D 或 CAEGraph 已被证伪。

## 2. 正式消费原件

- W004 正式 Return：`daowei2026/observe-iterate@4fa846f81971100af6a7c16251ed011971100068:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/WORKER_RETURN.json`
- 完整事实报告：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/FACT_REPORT.md`
- 事实 JSON：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/facts.json`
- 首个阻断：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/first_blocker.json`
- 运行报告：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/output/u2_f_caegraph/definition_run_report.json`
- Overlay 报告：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/module_overlay_report.json`
- `t1` 有限核对：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/diagnostics/locked_tis_t1_path_check.json`

W004 Return 的 `work_order_id / order_ref / worker / return_to` 与 C0020 工单一致，因此本 Return 可由原 E1 正式消费。

## 3. W004 已确认的事实

### 3.1 两个 source staging 成功

```text
observe-iterate HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358
tis HEAD=2f460d663d821cf2ba25555eda13e78b697d0767
both detached=true
required files present=true
business-source diff=0
```

### 3.2 TIS 初步 package materialization 与 origin 检查成功

- 锁定 `seed_inits.py` 一次 `exit0`；
- 生成 18 个原先缺失的空 `__init__.py`；
- `pretty-exports.py` **未执行**；
- constructor、F/Q/V 类及 Wave/STCalendar/ScaleTurn 共 7 个 `find_spec` origin 均指向锁定 checkout；
- D、C3、TIS 已跟踪业务源码均未修改。

### 3.3 D 真实执行一次并停止

```text
D attempt count=1
D exit code=1
definition_run_report.completed=false
candidate HTML=null
```

阻断发生在 `CurrSof` 构造期间，晚于 constructor 模块成功导入、早于 `make_features(...)` 调用：

```text
m3sof.settings.lib3
→ mquant.worker
→ mquant.uplot.multiscale
→ mquant.tis.blk.gen
→ from ..t1 import *
→ ModuleNotFoundError: No module named 'mquant.tis.t1'
```

### 3.4 未进入 F 与图阶段

```text
make_features called=false
F constructed=false
fields.json checked=false
F producer called=false
Q/V product data read=false
prepared tables=null
plot data=null
HTML=null
E3=false
E4=false
DATA_READY=false
```

## 4. W004 overlay 为什么失败

W004 wrapper 只做了：

```text
mquant.__path__ = [W004/source/mquant, BASE/mquant]
```

随后 Python 从 W004 锁定 checkout 装载 `mquant.tis`。由于锁定 checkout 的新 `mquant.tis` package path 没有再包含平台既有的 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis`，`mquant.tis.blk.gen` 的相对导入 `..t1` 只能在锁定 checkout 内寻找。

W004 有限核对已确认：锁定 commit 中不存在 `t1/`、`t1.py` 或同名 Git tree 条目。因此该 overlay 不能闭合 `mquant.tis.t1`。

这与以下事实共同说明，锁定 TIS source 不是一个可以完全替代平台基础 TIS 的自闭合包：

1. 锁定 TIS README 把 `t0 / t1 / t2 / t3` 明确列为特征层 package 结构；
2. 锁定 `blk/gen.py` 直接依赖 `t0 / t1 / t2 / t3`；
3. 精确 commit 却不含这些目录；
4. D005 只把锁定 constructor 与 F 类等新 source 作为业务输入，同时固定实际运行环境为 `BASE_E6_2_copy`；
5. W004 的 constructor 和 7 个目标 module origin 已经证明新 source 本身可被定位。

所以当前问题不是选择另一个 constructor，也不是更改 F 业务逻辑；它是：

> 锁定的新 TIS source 应作为平台基础 `mquant.tis` 上的 source layer 使用，而 W004 把它错误地当成了整个 `mquant.tis` 的唯一 package root。

## 5. E2 专业分类

### 5.1 不是 B 问题

没有触达品种、时间、日历、多尺度位置或 `groupKnownFrom`。

### 5.2 不是 C 问题

没有生成 HTML、面板、图元或交互结果。

### 5.3 当前不返回 D 重做业务定义

D 的实例、字段、位置、C2 展示和精确 source refs 没有被证伪。W004 暴露的是运行时 package composition，而 E Workflow 明确把 import／路径问题列为可在基准不变时续发 W1 的机械问题。

### 5.4 分类

```text
LOCKED_TIS_LAYERED_PACKAGE_COMPOSITION_GAP
```

## 6. W005 的唯一机械修法

W005 不再把锁定 TIS checkout 当作独占 package，而建立一份只存在于 W005 Python 进程中的、可审计的 layered package：

```text
mquant.tis.__path__
=
[
  W005/source/mquant/tis,           # 锁定 source 优先
  /dwdhome/fy/BASE_E6_2_copy/mquant/tis  # 平台基础 package fallback
]
```

语义是：

- 锁定 checkout 中真实存在的模块，必须从锁定 commit 加载；
- 锁定 checkout 明确缺失、但其源码声明依赖的基础层（首先是 `t0/t1/t2/t3`），只可从固定 `BASE_E6_2_copy` 平台 package 补足；
- 不能从其他分支、提交、目录或未知本地文件补模块；
- 所有关键 module origin 都要逐项记录；
- D/C3/TIS 业务源码和平台文件均不修改。

这不是任意“混用版本”，而是把已锁定的新 source layer 与 D005 固定的基础运行环境按模块存在性显式组合。

## 7. W005 package materialization

W004 只执行了 `seed_inits.py`，但锁定 README 对 fresh clone 的完整步骤是：

```bash
python seed_inits.py
python pretty-exports.py
```

W005 在新的 TIS checkout 中执行两步，并保存：

- 两个脚本的 commit、hash、stdout/stderr、exit code；
- 所有生成／改写 `__init__.py` 的 path/hash manifest；
- 运行前后 tracked-source diff；
- 明确证明没有改写任何已跟踪业务 `.py`。

这些 `__init__.py` 是锁定仓库声明的构建产物，不视为业务源码修复。

## 8. W005 union-package wrapper

W005 wrapper 在 D 之前：

1. 只导入基础 `mquant`；
2. 断言没有任何 `mquant.tis` 模块预加载；
3. 用 `ModuleType + ModuleSpec(is_package=True)` 建立进程内 `mquant.tis` package；
4. 把 `submodule_search_locations` 精确设为 `[locked_tis_root, runtime_tis_root]`；
5. 把该 package 注册到 `sys.modules` 并绑定到 `mquant.tis`；
6. `invalidate_caches()`；
7. 验证锁定 source 模块的 origin；
8. 验证平台基础层模块的 origin；
9. 写出完整 `layered_tis_report.json`；
10. 只有全部 origin contract 通过后，才用 `runpy.run_path` 运行原 D 一次。

### 8.1 必须来自锁定 checkout

至少：

```text
mquant.tis.frp.fqv_kline_example
mquant.tis.frp.CommonPriceTurnGroupCandidates
mquant.tis.frp.PostTurnGroupDirectionalOrganization
mquant.tis.frp.CommonTurnGroupValidity
mquant.tis.frpExample.Wave
mquant.tis.frpExample.STCalendar
mquant.tis.frpExample.ScaleTurn
mquant.tis.blk.gen
```

### 8.2 必须来自固定平台基础 package

至少：

```text
mquant.tis.t0
mquant.tis.t1
mquant.tis.t2
mquant.tis.t3
```

实际 origin 必须位于：

```text
/dwdhome/fy/BASE_E6_2_copy/mquant/tis/**
```

如果任一模块不存在、origin 不匹配、package 发生提前加载，或需要第三个来源，W005 必须停止，不运行 D。

## 9. 运行与停止边界

W005 沿用正常平台入口和当前 Binding：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

不使用 Landlock、namespace、mount、sudo 或平台 patch。

除原 W1 停止条件外，新增：

- `seed_inits.py` 或 `pretty-exports.py` 不能按锁定原件完成；
- union-package origin contract 不成立；
- 需要除锁定 TIS 与固定平台 TIS 之外的第三来源；
- 需要修改 TIS/D/C3 业务源码或平台文件；
- 需要无痕替换已加载 module；
- 需要从未锁定分支／commit 取文件。

精确 F 没有既存 `fields.json` 时仍必须停止，不调用 producer。

## 10. 诊断副产物与正式数据边界

W005 随 D 产生的 `prepared_tables/`、`plot_data/` 和 run report 仍只是候选运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不属于正式数据导出；
- 不得标记 `DATA_READY`。

## 11. 当前状态与续接

```text
W004 Return: ACCEPTED_AS_FACT
W004 classification: LOCKED_TIS_LAYERED_PACKAGE_COMPOSITION_GAP
return B/C/D: NO
W005: TO_BE_ISSUED
candidate HTML: NONE
E3: NOT_STARTED
E4 formal data admission: NONE
DATA_READY: false
E professional_state: IN_PROGRESS
```

W005 Return 回原 executor:E1 后继续同一：

```text
D005 / WI-E / M-E
```

有 HTML 时进入 E2/E3；无 HTML 时消费新的首个真实阻断。