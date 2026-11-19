# E2｜W003 真实结果消费、问题分类与 W004 运行基准

## 1. 身份

| 字段 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-E` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-E` |
| `delegation_id` | `D005`（C0018 当前版本） |
| 当前调用 | `C0020` |
| 被消费工单 | `W003` |
| 后继工单 | `W004`，新的 W1 revision |
| executor | `chatgpt:OI-U2-F-OBS-20261118-01:executor:E1` |

本文件由原 executor:E1 消费 W003 正式 Return 后形成。W003 的 `STOP` 是该工单的真实结果，不等于 D005/E 或父 Run 已完成，也不等于 F、D 或 CAEGraph 已被证伪。

## 2. 正式消费原件

- W003 正式 Return：`daowei2026/observe-iterate@d334e1629cef997c5ba35564ce518f682a672652:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/WORKER_RETURN.json`
- 完整事实报告：`daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/FACT_REPORT.md`
- 事实 JSON：`daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/facts.json`
- 运行报告：`daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/output/u2_f_caegraph/definition_run_report.json`
- 有限路径核对：`daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/diagnostics/module_path_check.json`
- 运行时旧 `frp/__init__.py` 快照：`daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/diagnostics/runtime_frp_init_snapshot.py`

W003 Return 的 `work_order_id / order_ref / worker / return_to` 与 C0019 工单一致，因此本 Return 可被原 E1 正式消费。

## 3. W003 已确认的事实

### 3.1 source 与脚本

```text
observe-iterate detached HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358
D/C3 exists=true
D/C3 modified=false
repair.diff=0 bytes
source tree clean=true
```

### 3.2 正常平台入口真实运行

```text
D attempt count=1
D exit code=1
definition_run_report.completed=false
candidate HTML=null
```

W003 没有使用 Landlock、namespace、独立 SemLock probe、sudo、mount 或平台 patch。`/dev/shm/sem.*` 前后快照均为空；这只说明端点没有观察到残留，不声称进程存续期间从未创建并正常删除 semaphore。

### 3.3 首个真实阻断

```text
ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
```

阻断发生在 D 的：

```python
from mquant.tis.frp.fqv_kline_example import make_features
```

它早于：

- `make_features` 可用；
- F 构造；
- 精确 `fields.json` 检查；
- F 正式表读取；
- CAEGraph layout；
- HTML、prepared tables 和 plot data。

W003 没有调用 `f.rerun()`、全历史 producer 或 Q/V 读取。

## 4. W003 有限路径检查的正确边界

W003 只检查了当前运行时：

```text
/dwdhome/fy/BASE_E6_2_copy/mquant/tis/frp
```

及声明模块／类的几个直接路径。该旧运行包的 `frp` 直接条目没有 F/Q/V 新模块，旧 `__init__.py` 也没有导出它们。

这证明：

> 当前已安装的旧 `mquant.tis.frp` 不能直接提供 D 声明的构造模块。

它不证明：

- 锁定 TIS 提交不存在该模块；
- 整个工作区或远端没有该源码；
- 可以任选其他构造器替换；
- F 正式产品不存在。

## 5. 锁定来源已经给出唯一语义来源

当前 D005 和 D 定义均精确锁定：

```text
daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767
```

其中：

- `frp/fqv_kline_example.py` 正式定义 `make_features(...)`；
- 它直接构造并返回 `f, q, v`，D 只观察返回的第一项 `f`；
- `frp/CommonPriceTurnGroupCandidates.py` 正式定义 `CommonPriceTurnGroupCandidatesFrp`；
- 构造模块使用同一提交内的相对模块 `frp/*` 和 `frpExample/*`；
- D 的 `source_refs` 也记录同一构造模块和 F 类文件。

因此后继不需要从运行时旧包中猜替代模块。唯一可接受的来源是：

```text
将锁定的 tis@2f460d... 作为 run-local source package materialize，
再让 D 的原 import 指向该精确源码。
```

## 6. TIS 包装事实与机械修法

锁定 TIS README 明确：

- 仓库中的 `__init__.py` 是构建产物，不纳入 Git；
- clone／切换分支后需运行 `seed_inits.py` 补全包初始化文件；
- `pretty-exports.py` 用于生成聚合导出。

锁定 `seed_inits.py` 只在不存在时创建空 `__init__.py`，不覆盖业务源码。

W004 的目标是直接导入明确模块：

```text
mquant.tis.frp.fqv_kline_example
```

因此第一轮只运行 `seed_inits.py` 形成可导入包边界，不运行会聚合并 eager-import 大量无关模块的 `pretty-exports.py`。这是 run-local direct-module overlay，不是安装或替换平台 TIS。若任一确切依赖需要 package export，真实 import 会给出新的首个阻断，Worker 不猜测补齐。

## 7. E2 专业分类

### 7.1 不是 B 问题

没有触达品种、时间、日历、多尺度或 `groupKnownFrom`，没有理由改变 B-POS-001。

### 7.2 不是 C 问题

没有生成 HTML 或任何图层／图元，当前没有 C2 冲突证据。

### 7.3 不返回 D 重新做业务集成

D 的实例、字段、位置、展示代码和 locked source refs 没有被证明有误。当前缺口是：锁定 TIS source 没有 materialize 到运行时 Python namespace。

这个缺口满足 E Workflow 的机械问题条件：

```text
import / 路径 / 已确认 source package materialization
+ 业务基准不变
→ 新 W1 revision
```

### 7.4 分类

```text
LOCKED_TIS_SOURCE_MATERIALIZATION_GAP
```

## 8. W004 运行基准

### 8.1 新 run root

```text
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT=$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004
OBS_ROOT=$RUN_ROOT/source/observe-iterate
TIS_ROOT=$RUN_ROOT/source/mquant/tis
OUTPUT_ROOT=$RUN_ROOT/output/u2_f_caegraph
LOG_ROOT=$RUN_ROOT/logs
```

### 8.2 固定提交

```text
observe-iterate=f4f0e4b276b1118b779473c1fbe462bc7a64b358
tis=2f460d663d821cf2ba25555eda13e78b697d0767
```

两个 source checkout 都必须 detached、可核对。W001/W002/W003 目录保持只读历史，不修改、不覆盖、不清理。

### 8.3 TIS package materialization

在 `TIS_ROOT`：

```bash
python seed_inits.py
```

保存：

- TIS source stage report；
- generated `__init__.py` path/hash manifest；
- `git status --short`；
- constructor／F class／Q class／V class及 `frpExample` 依赖文件的 origin 检查。

生成的空 `__init__.py` 是该仓库声明的 build product，不视为业务源修复；不得修改任何 `.py` 业务模块。

### 8.4 run-local namespace overlay

W004 使用一个 run-local wrapper，不修改 D/C3 或平台：

1. 导入现有基础 `mquant` 包；
2. 确认 `mquant.tis` 尚未预加载；
3. 将 `$RUN_ROOT/source/mquant` 放到 `mquant.__path__` 首位；
4. `invalidate_caches()`；
5. 用 `find_spec` 验证下列 module origin 均位于 `TIS_ROOT`：
   - `mquant.tis.frp.fqv_kline_example`；
   - `mquant.tis.frp.CommonPriceTurnGroupCandidates`；
   - `mquant.tis.frp.PostTurnGroupDirectionalOrganization`；
   - `mquant.tis.frp.CommonTurnGroupValidity`；
   - `mquant.tis.frpExample.Wave`；
   - `mquant.tis.frpExample.STCalendar`；
   - `mquant.tis.frpExample.ScaleTurn`；
6. 写出 `module_overlay_report.json`；
7. 用 `runpy.run_path` 按原 CLI 参数执行 D 一次。

任何 origin 不匹配、parent package 提前加载或源码提交不一致，都应停止并返回，不得从旧 runtime package 拼装混合模块。

### 8.5 运行与权限

沿用当前 Binding：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

W004 继续使用正常平台入口和当前 `sem.*` 限制；不使用 Landlock、namespace、sudo、mount 或平台 patch。

### 8.6 停止条件

除原 W1 停止条件外，新增：

- TIS 精确提交无法 fetch／checkout；
- `seed_inits.py` 不能形成包；
- module origin 不能全部落在锁定 TIS checkout；
- 发现混用旧 TIS 与锁定 TIS；
- 需要改写 TIS 业务模块或 D/C3 业务语义。

若精确 F 实例没有既存 `fields.json`，仍按 D 合同停止，不调用 producer。

## 9. W1 与正式数据边界

W004 随 D 产生的 `prepared_tables/`、`plot_data/` 和 run report 仍只是候选运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不属于正式数据导出；
- 不得标记 `DATA_READY`。

## 10. 当前状态与续接

```text
W003 Return: ACCEPTED_AS_FACT
W003 classification: LOCKED_TIS_SOURCE_MATERIALIZATION_GAP
return B/C/D: NO
W004: TO_BE_ISSUED
candidate HTML: NONE
E3: NOT_STARTED
E4 formal data admission: NONE
DATA_READY: false
E professional_state: IN_PROGRESS
```

W004 Return 回原 executor:E1 后继续同一：

```text
D005 / WI-E / M-E
```

有 HTML 时进入 E2/E3；无 HTML 时消费新的首个真实阻断。