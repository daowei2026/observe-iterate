# W004｜CAEGraph W1 revision：materialize 锁定 TIS source 后运行 D

## 一、工单身份

- `run_id / work_order_id / parent_delegation_id`：`OI-U2-F-OBS-20261118-01 / W004 / D005`
- `issuer / issuer_call_id`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1 / C0020`
- `worker`：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- 操作类别：新的 **W1 运行／有限机械修复 revision**；不是正式取数 W2。

W001、W002、W003 均已有确定结果并已结束。本工单使用新的去重身份 `W004`，不得覆盖、清理或复用前三个工单的输出目录。

## 二、E2 分类与本次唯一修复目标

E2 分类：

`daowei2026/observe-iterate@b1625c62b599a2d693edb264ad815abf265853b7:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W003_RESULT_CLASSIFICATION_AND_W004_BASELINE.md`

W003 的首个阻断是：

```text
ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
```

D 与当前 D005 已精确锁定 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`；该提交真实包含构造模块和 F 类。问题不是选择哪个替代构造器，而是锁定 TIS source 尚未 materialize 到当前 `mquant.tis` namespace。

本次唯一机械目标：

```text
在 W004 run root 中 staging 锁定 TIS commit
→ 按仓库自带 seed_inits.py 生成 package boundary
→ 以 run-local namespace overlay 暴露到现有 mquant 包
→ 验证 module origin 全部来自锁定 checkout
→ 不修改 D/C3/TIS 业务模块，运行原 D 一次
```

## 三、当前权威输入

- 当前 D005 JSON：`daowei2026/observe-iterate@7b2353915a15ecf29bc39eaaa0ea7f1f5be3dee8:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 当前 D005 正文：`daowei2026/observe-iterate@51bb129c486c2654286fb9d990c18865c3d847ab:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.md`
- W003 Return：`daowei2026/observe-iterate@d334e1629cef997c5ba35564ce518f682a672652:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/WORKER_RETURN.json`
- W003 事实报告：`daowei2026/observe-iterate@9a9c5542f229078bedcfd1f65525d79c29cc33e4:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W003/FACT_REPORT.md`
- 当前 Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 当前 Resource Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 物理 Worker：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`

运行定义与展示输入：

- D：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- C2 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`

锁定 TIS：

- README：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:README.md`
- package seeder：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:seed_inits.py`
- constructor：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- F class：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py`
- Q class：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py`
- V class：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonTurnGroupValidity.py`

唯一观察对象仍是 `make_features(...)[0]` 返回的 F。不得读取或分析 Q/V；构造函数按锁定原文返回三项这一事实不作改写。

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
/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/**
```

除 D 进程树临时 `sem.*` 外，不写工作区外路径；不修改平台包、生产数据、其他仓库工作树或其他 Run。

## 五、run root 与幂等

```bash
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004"
OBS_ROOT="$RUN_ROOT/source/observe-iterate"
TIS_ROOT="$RUN_ROOT/source/mquant/tis"
OVERLAY_MQUANT="$RUN_ROOT/source/mquant"
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
OBS_COMMIT=f4f0e4b276b1118b779473c1fbe462bc7a64b358
TIS_COMMIT=2f460d663d821cf2ba25555eda13e78b697d0767
```

- `RUN_ROOT` 不存在：创建后继续。
- 已存在且有本 W004 完整 receipt：核对动作和结果，不重复执行。
- 已存在但来源不明、部分动作效果未知、提交不符或同 W004 在途：返回 `EFFECT_UNKNOWN`，不覆盖或清理。

## 六、两个精确 source checkout

### 6.1 observe-iterate

```bash
mkdir -p "$RUN_ROOT/source" "$OUTPUT_ROOT" "$LOG_ROOT" \
  "$RUN_ROOT/cache/tmp" "$RUN_ROOT/cache/xdg" \
  "$RUN_ROOT/cache/numba" "$RUN_ROOT/cache/matplotlib"

git init "$OBS_ROOT"
git -C "$OBS_ROOT" remote add origin https://github.com/daowei2026/observe-iterate.git
git -C "$OBS_ROOT" -c protocol.version=2 fetch --filter=blob:none --no-tags \
  origin refs/heads/runs/OI-U2-F-OBS-20261118-01:refs/remotes/origin/run
git -C "$OBS_ROOT" checkout --detach "$OBS_COMMIT"
```

### 6.2 TIS

```bash
mkdir -p "$OVERLAY_MQUANT"
git init "$TIS_ROOT"
git -C "$TIS_ROOT" remote add origin https://github.com/daowei2026/tis.git
git -C "$TIS_ROOT" -c protocol.version=2 fetch --filter=blob:none --no-tags \
  origin "$TIS_COMMIT"
git -C "$TIS_ROOT" checkout --detach "$TIS_COMMIT"
```

若 direct SHA fetch 不被远端接受，保存真实错误并停止；不得改取未锁定分支或其他提交。

### 6.3 核对

```bash
test "$(git -C "$OBS_ROOT" rev-parse HEAD)" = "$OBS_COMMIT"
test "$(git -C "$TIS_ROOT" rev-parse HEAD)" = "$TIS_COMMIT"
test -f "$OBS_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py"
test -f "$OBS_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py"
test -f "$TIS_ROOT/frp/fqv_kline_example.py"
test -f "$TIS_ROOT/frp/CommonPriceTurnGroupCandidates.py"
test -f "$TIS_ROOT/frp/PostTurnGroupDirectionalOrganization.py"
test -f "$TIS_ROOT/frp/CommonTurnGroupValidity.py"
```

分别写出 observe-iterate 与 TIS 的 source stage report。

## 七、materialize TIS package boundary

在 `TIS_ROOT` 运行仓库自带脚本：

```bash
cd "$TIS_ROOT"
python seed_inits.py \
  > "$LOG_ROOT/tis_seed_inits.stdout.log" \
  2> "$LOG_ROOT/tis_seed_inits.stderr.log"
```

要求：

- `seed_inits.py` 必须来自锁定 TIS commit；
- 只允许其创建原本缺失的空 `__init__.py`；
- 保存全部生成路径、字节数和 SHA-256 到 `tis_generated_inits.json`；
- 保存 `git -C "$TIS_ROOT" status --short`；
- 不运行 `pretty-exports.py`，不 eager-import 无关 TIS 模块；
- 不修改任何已跟踪 `.py` 业务源码。

生成的空 `__init__.py` 是该仓库 README 声明的构建产物，不计为 D/C3/TIS 业务修复。

## 八、run-local module overlay wrapper

在：

```text
$RUN_ROOT/run_d_with_locked_tis.py
```

创建只负责 namespace 接线的 wrapper。其行为必须等价于：

```python
from pathlib import Path
import importlib
import importlib.util
import json
import os
import runpy
import sys

run_root = Path(os.environ["OI_W004_RUN_ROOT"]).resolve()
overlay_mquant = (run_root / "source" / "mquant").resolve()
tis_root = (overlay_mquant / "tis").resolve()
obs_root = (run_root / "source" / "observe-iterate").resolve()
output_root = (run_root / "output" / "u2_f_caegraph").resolve()
d_script = obs_root / "longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py"
report_path = run_root / "module_overlay_report.json"

import mquant
preloaded = sorted(
    name for name in sys.modules
    if name == "mquant.tis" or name.startswith("mquant.tis.")
)
if preloaded:
    raise RuntimeError("mquant.tis loaded before locked overlay: " + ",".join(preloaded))

mquant.__path__ = [str(overlay_mquant)] + [
    str(p) for p in mquant.__path__
    if Path(p).resolve() != overlay_mquant
]
importlib.invalidate_caches()

expected = {
    "mquant.tis.frp.fqv_kline_example": tis_root / "frp/fqv_kline_example.py",
    "mquant.tis.frp.CommonPriceTurnGroupCandidates": tis_root / "frp/CommonPriceTurnGroupCandidates.py",
    "mquant.tis.frp.PostTurnGroupDirectionalOrganization": tis_root / "frp/PostTurnGroupDirectionalOrganization.py",
    "mquant.tis.frp.CommonTurnGroupValidity": tis_root / "frp/CommonTurnGroupValidity.py",
    "mquant.tis.frpExample.Wave": tis_root / "frpExample/Wave.py",
    "mquant.tis.frpExample.STCalendar": tis_root / "frpExample/STCalendar.py",
    "mquant.tis.frpExample.ScaleTurn": tis_root / "frpExample/ScaleTurn.py",
}
origins = {}
for name, wanted in expected.items():
    spec = importlib.util.find_spec(name)
    actual = None if spec is None or spec.origin is None else Path(spec.origin).resolve()
    origins[name] = {"expected": str(wanted.resolve()), "actual": None if actual is None else str(actual)}
    if actual != wanted.resolve():
        report_path.write_text(json.dumps({"ok": False, "preloaded": preloaded, "origins": origins}, indent=2) + "\n")
        raise RuntimeError(f"locked module origin mismatch: {name}: {actual} != {wanted}")

report_path.write_text(json.dumps({"ok": True, "preloaded": preloaded, "origins": origins}, indent=2) + "\n")
sys.argv = [str(d_script), "--output-dir", str(output_root)]
runpy.run_path(str(d_script), run_name="__main__")
```

允许为错误处理、JSON 编码和日志补充必要代码，但不得改变以上语义。

Wrapper：

- 不定义或替换 `make_features`；
- 不复制 F 构造参数；
- 不修改 D/C3；
- 不修改平台 `mquant`；
- 只把锁定 TIS checkout 放到 `mquant` 的子包搜索路径首位，并验证实际 origin。

保存 wrapper 的完整正文与 SHA-256。

## 九、正常平台入口运行

沿用 W003 已验证环境，不使用 Landlock、namespace、mount、sudo、平台 patch 或独立 SemLock probe：

```bash
export PYTHONDONTWRITEBYTECODE=1
source "$BASE/m3rc"

# M3HOST / NO_PROXY / PYTHONPATH / TLS 采用 W003 已验证接线
export TMPDIR="$RUN_ROOT/cache/tmp"
export XDG_CACHE_HOME="$RUN_ROOT/cache/xdg"
export NUMBA_CACHE_DIR="$RUN_ROOT/cache/numba"
export MPLCONFIGDIR="$RUN_ROOT/cache/matplotlib"
export OI_W004_RUN_ROOT="$RUN_ROOT"
ulimit -c 0

cd "$OBS_ROOT"
python "$RUN_ROOT/run_d_with_locked_tis.py" \
  > "$LOG_ROOT/w004_run.log" \
  2>&1
RUN_EXIT=$?
printf '%s\n' "$RUN_EXIT" > "$LOG_ROOT/w004_run.exit_code"
```

运行前后按 W003 相同方式只读记录 `/dev/shm/sem.*` 元数据；不手工创建测试 semaphore，不删除运行前对象或无法归属的对象。

## 十、可以直接修的范围

仅限：

- source staging、package boundary、namespace search path；
- Python 语法、import、文件路径；
- 锁定版本已确认的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、日志和静态 HTML 接线；
- 当前 Binding 允许的临时 `sem.*` 接线。

任何修改必须留在 W004 run root，保存独立 diff／正文／hash。不得推送或修改平台源码。

## 十一、必须停止并回 E

- 锁定 TIS commit 无法取得或 origin 不匹配；
- 需要混用旧 runtime TIS 与锁定 TIS；
- 需要修改 TIS 业务模块、D/C3 业务语义或平台库；
- 精确 F 实例没有既存 `fields.json`；
- 需要 `f.rerun()` 或全历史 producer；
- 需要改变 SOF、品种、日历、5m、2021—2022 或 `groupKnownFrom`；
- 需要读取 Q/V、替换业务字段或使用近似数据；
- 需要改变 C2 页面、面板、图元、时间、标准化、交互或阅读语义；
- 需要非 `sem.*` 的 `/dev/shm` 写入、sudo、mount、namespace 或未授权路径；
- 正确修法不唯一或语义影响不明；
- 同一 W004 有未知结果、非单写者或动作效果未知。

首次出现明确阻断后优先回报；不做无界搜索或无上限重试。

## 十二、诊断副产物与正式数据边界

D 若产生 `prepared_tables/`、`plot_data/` 或 `definition_run_report.json`，在 W004 中仍是候选运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不属于正式数据导出；
- 不得标记 `DATA_READY`；
- 不得修改 D 来扩大导出。

## 十三、最小交付

至少返回：

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
observe-iterate staging：<report>
TIS staging：<report>
TIS generated inits：<manifest>
module overlay：<module_overlay_report.json>
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
work_order_id=W004
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
order_ref=<本 W004 ORDER.json 精确 commit>
```

Worker 不判断图是否专业接受，也不启动正式数据导出。

## 十四、续接

W004 Return 回原 executor:E1 后继续同一：

```text
D005 / WI-E / M-E
```

- 有 HTML：E2 核脚本／overlay／diff 后进入 E3；
- 无 HTML：E2 消费新的首个阻断；
- 只有 E3 接受最终图后才允许 E4 和正式数据导出。