# W005｜CAEGraph W1 revision：建立锁定 TIS／平台基础 TIS 分层 package 后运行 D

## 一、工单身份

- `run_id / work_order_id / parent_delegation_id`：`OI-U2-F-OBS-20261118-01 / W005 / D005`
- `issuer / issuer_call_id`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1 / C0021`
- `worker`：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- 操作类别：新的 **W1 运行／有限机械修复 revision**；不是正式取数 W2。

W001～W004 均已有确定结果并已结束。本工单使用新的去重身份 `W005`，不得覆盖、清理或复用前四个工单的输出目录。

## 二、E2 分类与唯一修复目标

E2 分类：

`daowei2026/observe-iterate@43ff94cc90313b324cadbc4eba80fa5ec0eb2a3b:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W004_RESULT_CLASSIFICATION_AND_W005_BASELINE.md`

W004 的首个阻断：

```text
ModuleNotFoundError: No module named 'mquant.tis.t1'
```

W004 已证明：

- 锁定 constructor 与 7 个目标模块可定位；
- 锁定 TIS commit 不含 `t1`；
- 锁定 `blk/gen.py` 却直接依赖 `t0/t1/t2/t3`；
- W004 将锁定 checkout 当成唯一 `mquant.tis` package root，因而无法使用固定平台中的基础 TIS 层。

本次唯一机械目标：

```text
完整 materialize 锁定 TIS checkout
→ 建立进程内 layered mquant.tis package
→ 锁定 source 优先，固定 BASE_E6_2_copy 基础 TIS fallback
→ 对 locked/base module origins 分别作硬核对
→ 不修改任何业务源码或平台文件
→ 运行原 D 一次
```

## 三、当前权威输入

- 当前 D005 JSON：`daowei2026/observe-iterate@7b2353915a15ecf29bc39eaaa0ea7f1f5be3dee8:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 当前 D005 正文：`daowei2026/observe-iterate@51bb129c486c2654286fb9d990c18865c3d847ab:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.md`
- W004 Return：`daowei2026/observe-iterate@4fa846f81971100af6a7c16251ed011971100068:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/WORKER_RETURN.json`
- W004 事实报告：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/FACT_REPORT.md`
- W004 首个阻断：`daowei2026/observe-iterate@feb62ad895d3f60a6075b65384a2605bc49d50d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W004/first_blocker.json`
- 当前 Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 当前 Resource Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 物理 Worker：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`

运行定义与展示输入：

- D：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- C2 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`

锁定 TIS：

- commit：`2f460d663d821cf2ba25555eda13e78b697d0767`
- README：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:README.md`
- `seed_inits.py`：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:seed_inits.py`
- `pretty-exports.py`：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:pretty-exports.py`
- constructor：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- F class：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`
- `blk/gen.py`：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:blk/gen.py`

唯一观察对象仍是 `make_features(...)[0]` 返回的 F。不得读取或分析 Q/V 产品数据；构造模块正常导入 Q/V 类不等于读取 Q/V 结果。

## 四、精确授权

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

`authority_quote` 必须逐字采用当前 Binding：

```text
Owner 预先选择指令原文：碰到需要我处理的问题，先选第一项
适用请求：OR001；被选择的第一项：A. 确认首选 sem.* 机读补正；
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
`/dev/shm` 只允许本 Run 的 CAEGraph 运行进程及其子进程为 Python multiprocessing 临时创建和删除 POSIX semaphore 对象 `sem.*`；不得写任意共享内存 payload、不得使用 sudo、不得建立 mount 绕过、不得 patch 平台源码、不得调用 F producer、不得读取 Q/V、不得据此启动正式数据导出。
```

实际持久写入进一步收敛到：

```text
/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W005/**
```

除 D 进程树临时 `sem.*` 外，不写工作区外路径；不修改平台 package、生产数据、其他仓库工作树或其他 Run。

## 五、run root 与幂等

```bash
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W005"
OBS_ROOT="$RUN_ROOT/source/observe-iterate"
TIS_ROOT="$RUN_ROOT/source/mquant/tis"
RUNTIME_TIS="$BASE/mquant/tis"
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
OBS_COMMIT=f4f0e4b276b1118b779473c1fbe462bc7a64b358
TIS_COMMIT=2f460d663d821cf2ba25555eda13e78b697d0767
```

- `RUN_ROOT` 不存在：创建后继续。
- 已存在且有本 W005 完整 receipt：核对动作和结果，不重复执行。
- 已存在但来源不明、部分动作效果未知、提交不符或同 W005 在途：返回 `EFFECT_UNKNOWN`，不覆盖或清理。

## 六、两个精确 source checkout

按 W004 已验证的方法 staging：

```bash
mkdir -p "$RUN_ROOT/source/mquant" "$OUTPUT_ROOT" "$LOG_ROOT" \
  "$RUN_ROOT/cache/tmp" "$RUN_ROOT/cache/xdg" \
  "$RUN_ROOT/cache/numba" "$RUN_ROOT/cache/matplotlib"

# observe-iterate
git init "$OBS_ROOT"
git -C "$OBS_ROOT" remote add origin https://github.com/daowei2026/observe-iterate.git
git -C "$OBS_ROOT" -c protocol.version=2 fetch --filter=blob:none --no-tags \
  origin refs/heads/runs/OI-U2-F-OBS-20261118-01:refs/remotes/origin/run
git -C "$OBS_ROOT" checkout --detach "$OBS_COMMIT"

# TIS
git init "$TIS_ROOT"
git -C "$TIS_ROOT" remote add origin https://github.com/daowei2026/tis.git
git -C "$TIS_ROOT" -c protocol.version=2 fetch --filter=blob:none --no-tags \
  origin "$TIS_COMMIT"
git -C "$TIS_ROOT" checkout --detach "$TIS_COMMIT"
```

若 direct SHA fetch 不被接受，保存真实错误并停止；不得改取其他分支或提交。

核对：

```bash
test "$(git -C "$OBS_ROOT" rev-parse HEAD)" = "$OBS_COMMIT"
test "$(git -C "$TIS_ROOT" rev-parse HEAD)" = "$TIS_COMMIT"
test -f "$OBS_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py"
test -f "$OBS_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py"
test -f "$TIS_ROOT/frp/fqv_kline_example.py"
test -f "$TIS_ROOT/frp/CommonPriceTurnGroupCandidates.py"
test -f "$TIS_ROOT/blk/gen.py"
test -d "$RUNTIME_TIS"
```

写出 observe-iterate、TIS 和组合 source stage reports。

## 七、完整 materialize 锁定 TIS package

W004 只运行了第一步；W005 必须按锁定 README 顺序运行两步：

```bash
cd "$TIS_ROOT"
python seed_inits.py \
  > "$LOG_ROOT/tis_seed_inits.stdout.log" \
  2> "$LOG_ROOT/tis_seed_inits.stderr.log"
printf '%s\n' "$?" > "$LOG_ROOT/tis_seed_inits.exit_code"

python pretty-exports.py \
  > "$LOG_ROOT/tis_pretty_exports.stdout.log" \
  2> "$LOG_ROOT/tis_pretty_exports.stderr.log"
printf '%s\n' "$?" > "$LOG_ROOT/tis_pretty_exports.exit_code"
```

要求：

1. 两个脚本都必须来自锁定 TIS commit；
2. 两步均须 `exit0`，否则停止；
3. 保存运行前后全部 `__init__.py` 的 path、bytes、SHA-256；
4. 保存 `git status --short` 和 tracked diff；
5. 只允许生成／改写被 `.gitignore` 排除的 `__init__.py` build products；
6. 不允许修改任何已跟踪业务 `.py`；
7. 写出 `tis_package_materialization_report.json`。

## 八、进程内 layered `mquant.tis`

在：

```text
$RUN_ROOT/run_d_with_layered_tis.py
```

建立只负责 package path 接线的 wrapper。核心语义必须等价于：

```python
from pathlib import Path
import importlib
import importlib.machinery
import importlib.util
import json
import os
import runpy
import sys
import types

run_root = Path(os.environ['OI_W005_RUN_ROOT']).resolve()
locked_tis = (run_root / 'source/mquant/tis').resolve()
runtime_tis = Path('/dwdhome/fy/BASE_E6_2_copy/mquant/tis').resolve()
obs_root = (run_root / 'source/observe-iterate').resolve()
output_root = (run_root / 'output/u2_f_caegraph').resolve()
d_script = obs_root / 'longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py'
report_path = run_root / 'layered_tis_report.json'

import mquant
preloaded = sorted(
    name for name in sys.modules
    if name == 'mquant.tis' or name.startswith('mquant.tis.')
)
if preloaded:
    raise RuntimeError('mquant.tis loaded before layered package: ' + ','.join(preloaded))

pkg = types.ModuleType('mquant.tis')
pkg.__file__ = None
pkg.__package__ = 'mquant.tis'
pkg.__path__ = [str(locked_tis), str(runtime_tis)]
spec = importlib.machinery.ModuleSpec('mquant.tis', loader=None, is_package=True)
spec.submodule_search_locations = list(pkg.__path__)
pkg.__spec__ = spec
sys.modules['mquant.tis'] = pkg
setattr(mquant, 'tis', pkg)
importlib.invalidate_caches()
```

允许补充严格错误处理、JSON 报告和日志，但不得改变以上 layered path 顺序和来源。

### 8.1 locked-source origin contract

以下模块必须解析到 `$TIS_ROOT/**`：

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

### 8.2 runtime-base origin contract

以下模块必须解析到 `$RUNTIME_TIS/**`：

```text
mquant.tis.t0
mquant.tis.t1
mquant.tis.t2
mquant.tis.t3
```

如某项是 package，记录其 `submodule_search_locations`；如为 module，记录 `spec.origin`。所有真实路径必须位于固定 runtime TIS root。

### 8.3 package report

在运行 D 前写出：

```text
$RUN_ROOT/layered_tis_report.json
```

至少包含：

- preloaded module list；
- locked/runtime roots；
- package path 顺序；
- 每一 required module 的 expected class、actual origin／locations；
- origin contract 总结果；
- 没有第三来源；
- root `__init__.py` 未被执行、subpackages 使用 materialized init 的事实。

任一 origin 不满足，停止，不运行 D。

## 九、正常平台入口运行

沿用 W003/W004 已验证环境，不使用 Landlock、namespace、mount、sudo、平台 patch 或独立 SemLock probe：

```bash
export PYTHONDONTWRITEBYTECODE=1
source "$BASE/m3rc"

# M3HOST / NO_PROXY / PYTHONPATH / TLS 沿用已验证接线
export TMPDIR="$RUN_ROOT/cache/tmp"
export XDG_CACHE_HOME="$RUN_ROOT/cache/xdg"
export NUMBA_CACHE_DIR="$RUN_ROOT/cache/numba"
export MPLCONFIGDIR="$RUN_ROOT/cache/matplotlib"
export OI_W005_RUN_ROOT="$RUN_ROOT"
ulimit -c 0

cd "$OBS_ROOT"
python "$RUN_ROOT/run_d_with_layered_tis.py" \
  > "$LOG_ROOT/w005_run.log" \
  2>&1
RUN_EXIT=$?
printf '%s\n' "$RUN_EXIT" > "$LOG_ROOT/w005_run.exit_code"
```

Wrapper 在 origin contract 通过后：

```python
sys.argv = [str(d_script), '--output-dir', str(output_root)]
runpy.run_path(str(d_script), run_name='__main__')
```

记录 wrapper attempt、D dispatch、D attempt、实际退出码和时间。D 第一次运行后优先回报候选 HTML或首个真实阻断，不作无界诊断或无上限重试。

## 十、临时 semaphore 的最小审计边界

与 W003/W004 相同，运行前后只读记录 `/dev/shm/sem.*` 名称和元数据：

- wrapper 不手工创建测试 semaphore；
- 不读写非 `sem.*` 对象；
- 不删除运行前对象或无法证明属于本次进程树的对象；
- 若本次可归属残留存在，保存事实回 E，不扩大清理。

## 十一、可以直接修的范围

仅限：

- source staging、package build products、layered search path；
- Python 语法、import、文件路径；
- 锁定版本已确认的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、日志和静态 HTML 接线；
- 当前 Binding 允许的临时 `sem.*` 接线。

任何修改必须留在 W005 run root，保存独立 diff／正文／hash。不得推送或修改平台源码。

## 十二、必须停止并回 E

- 锁定 commit 无法取得；
- `seed_inits.py`／`pretty-exports.py` 不能按锁定原件完成；
- required locked/base module origin 不符合合同；
- 需要锁定 TIS 与固定 runtime TIS 之外的第三来源；
- 需要无痕替换已经加载的 TIS module；
- 需要修改 TIS 业务模块、D/C3 业务语义或平台库；
- 精确 F 实例没有既存 `fields.json`；
- 需要 `f.rerun()` 或全历史 producer；
- 需要改变 SOF、品种、日历、5m、2021—2022 或 `groupKnownFrom`；
- 需要读取 Q/V 产品数据、替换业务字段或使用近似数据；
- 需要改变 C2 页面、面板、图元、时间、标准化、交互或阅读语义；
- 需要非 `sem.*` 的 `/dev/shm` 写入、sudo、mount、namespace 或未授权路径；
- 正确修法不唯一或语义影响不明；
- 同一 W005 有未知结果、非单写者或动作效果未知。

首次出现明确阻断后优先回报；不做无界搜索或无上限重试。

## 十三、诊断副产物与正式数据边界

D 若产生 `prepared_tables/`、`plot_data/` 或 `definition_run_report.json`，在 W005 中仍是候选运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不属于正式数据导出；
- 不得标记 `DATA_READY`；
- 不得修改 D 来扩大导出。

## 十四、最小交付

至少返回：

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
observe-iterate staging：<report>
TIS staging：<report>
TIS package materialization：<report + init manifest>
layered TIS：<layered_tis_report.json>
wrapper：<path + sha256>
最终 D/C3/TIS 业务源码：<paths + commits + modified=false/true>
候选 HTML：<path；无则明确>
运行日志：<path>
D attempt count：<integer>
D 退出码：<integer/unknown>
实际修改：<diff；无则明确>
当前阻断：<首个真实阻断；无写无>
definition_run_report：<path；无则明确>
semaphore 事实：<before/after；残留说明>
```

正式 Return：

```text
schema=longrun-worker-return/v2
work_order_id=W005
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
order_ref=<本 W005 ORDER.json 精确 commit>
```

Worker 不判断图是否专业接受，也不启动正式数据导出。

## 十五、续接

W005 Return 回原 executor:E1 后继续同一：

```text
D005 / WI-E / M-E
```

- 有 HTML：E2 核 layered package／脚本／diff 后进入 E3；
- 无 HTML：E2 消费新的首个阻断；
- 只有 E3 接受最终图后才允许 E4 和正式数据导出。