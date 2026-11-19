# W002｜CAEGraph W1 revision：私有 runtime IPC 后重试 D

## 一、身份与类型

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_order_id`：`W002`
- `parent_delegation_id`：`D005`
- `issuer_call_id`：`C0014`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `worker`：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- 操作类别：**新的 W1 revision**（运行／权限内机械修复），不是正式取数 W2。

W001 已有确定 `STOP` 结果且无未知在途，本工单使用新的可去重动作身份 `W002`。它不覆盖、不清理、不重用 W001 的输出目录。

## 二、E2 分类依据

- E2 分类：`daowei2026/observe-iterate@5f4678f14050e60ca4d5f75fee3054b07fafc96b:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W001_RESULT_CLASSIFICATION.md`
- W001 正式 Return：`daowei2026/observe-iterate@7beda1b54e7777b5b4f86ef6174376570e4c8b1a:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/WORKER_RETURN.json`
- W001 事实报告：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/FACT_REPORT.md`
- W001 首个阻断：`daowei2026/observe-iterate@2f090b678f765260e2b39c6d6da8780220738370:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/first_blocker.json`

E2 已判定：W001 失败来自 Worker 新增 Landlock 阻断 `/dev/shm` semaphore 创建，早于 F 构造；它不是 B、C 或 D 业务问题。D/C3、实例、位置和展示基准不变，因此按 E Skill 续发 W1 revision。

## 三、当前权威输入

- Owner 授权补正：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_AUTHORITY_AMENDMENT_20261119.md`
- Run Binding：`daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- Resource Binding：`daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 物理 Worker：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`
- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- C2 当前 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`

源码固定提交：

```text
f4f0e4b276b1118b779473c1fbe462bc7a64b358
```

唯一业务对象仍是 `make_features(...)[0]` 返回的 F；Q/V 不进入本工单。

## 四、精确授权

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

实际持久写入进一步收敛到：

```text
/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/**
```

不得修改：

- W001 目录；
- `/dwdhome/fy/BASE_E6_2_copy/mquant/**` 等平台源码；
- 其他仓库、其他 Run、生产数据；
- 外部 symlink 目标。

只读使用既有运行环境和既存特征产品是允许的。

## 五、本次唯一机械修复目标

W001 已证明同一写边界下 `multiprocessing.Lock()` 需要创建：

```text
/dev/shm/sem.<random>
```

本工单不得直接放开宿主 `/dev/shm` 写入。应建立一个**私有 mount namespace**，使 namespace 内的 `/dev/shm` 映射到 W002 run root 内的目录：

```text
namespace-local /dev/shm
→ /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/runtime/shm
```

这样 POSIX semaphore 的底层持久写仍落在 Owner 已授权的工作区路径。

### 强制边界

- 不使用 PID namespace；平台 import 中存在 `max_workers=os.getpid()-2`，本工单只隔离 mount/user namespace。
- 不以直接写宿主 `/dev/shm` 作为 fallback。
- 不 patch `mquant/apt/tool/misc.py` 或其他平台库来绕过 executor。
- 不改变 D/C3 业务代码来规避 import。
- 私有 mount 无法建立时，返回首个真实阻断。

## 六、run root 与幂等

```bash
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002"
SOURCE_ROOT="$RUN_ROOT/source/observe-iterate"
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
RUNTIME_SHM="$RUN_ROOT/runtime/shm"
D_COMMIT=f4f0e4b276b1118b779473c1fbe462bc7a64b358
```

- `RUN_ROOT` 不存在：创建并继续。
- `RUN_ROOT` 已存在且具有本 W002 的完整 receipt：先核对动作、提交和结果；不得盲目重跑。
- `RUN_ROOT` 已存在但来源未知、部分动作效果不明或与 W002 不符：返回 `EFFECT_UNKNOWN`。

## 七、源码 staging

按 W001 已验证的方法，在 `SOURCE_ROOT` 建立 detached checkout：

```bash
mkdir -p "$RUN_ROOT/source" "$OUTPUT_ROOT" "$LOG_ROOT" "$RUNTIME_SHM"
chmod 1777 "$RUNTIME_SHM"

git init "$SOURCE_ROOT"
git -C "$SOURCE_ROOT" remote add origin https://github.com/daowei2026/observe-iterate.git
git -C "$SOURCE_ROOT" -c protocol.version=2 fetch --filter=blob:none --no-tags \
  origin refs/heads/runs/OI-U2-F-OBS-20261118-01:refs/remotes/origin/run
git -C "$SOURCE_ROOT" checkout --detach "$D_COMMIT"
```

若目录已由本 W 正确建立，按幂等规则复用；不重复添加 remote 或覆盖结果。

运行前验证：

```bash
test "$(git -C "$SOURCE_ROOT" rev-parse HEAD)" = "$D_COMMIT"
test -f "$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py"
test -f "$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py"
```

写出 `source_stage_report.json`。

## 八、私有 `/dev/shm` 包络

Worker 应在不使用 PID namespace 的前提下，采用现有系统能力建立 user + mount namespace。可使用等价命令；实际命令、工具版本和结果必须入日志。

参考结构：

```bash
unshare --user --map-root-user --mount --fork bash -c '
  set -euo pipefail
  mount --make-rprivate /
  mount --bind "$RUNTIME_SHM" /dev/shm
  test -d /dev/shm
  test -w /dev/shm
  # 保存 mountinfo / findmnt；验证 alias 的实际 backing 为 W002 runtime/shm
  ...
'
```

必须用可审计方式证明 namespace 内 `/dev/shm` 指向 W002 的 `RUNTIME_SHM`。推荐同时保存：

- `findmnt -T /dev/shm`；
- `/proc/self/mountinfo` 相关行；
- 一个 alias probe：在 namespace 内 `/dev/shm` 创建临时文件，并在 run root 的 `runtime/shm` 观察到同一文件，然后删除。

若无法证明 backing 位于 W002 run root，停止，不运行 D。

## 九、Landlock 与 SemLock probe

在私有 mount 建立后，可以继续使用 run-root 写边界。若 Landlock 需要为 namespace-local `/dev/shm` alias 增加第二条规则，只能在已经证明该 alias backing 为 W002 `runtime/shm` 后增加；不得授权其他 `/dev/shm`。

先在与 D 完全相同的 namespace、环境和写边界中运行最小标准库 probe：

```python
import multiprocessing as mp
lock = mp.Lock()
lock.acquire()
lock.release()
```

保存：

```text
logs/private_shm_mount.*
logs/semlock_probe.log
logs/semlock_probe.exit_code
logs/semlock_probe.strace   # 若已有工具且不扩大范围
```

- probe 失败：停止，返回首个真实阻断；不运行 D。
- probe 成功：才进入 D 运行。

## 十、D 运行

复用 W001 已验证的现有环境入口：

- `/dwdhome/fy/BASE_E6_2_copy/m3rc`；
- 工作区 `.runtime/python-deps`；
- 现有 `run-python.sh` 所需 TLS 库；
- 工作区正式 Python，实际入口入日志。

从 `SOURCE_ROOT` 运行：

```bash
python \
  longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir "$OUTPUT_ROOT"
```

将完整 stdout/stderr、退出码、开始／结束时间保存到 W002 日志。

首次 D 运行后：

- 若生成 HTML，立即保留并回报；
- 若出现新的首个阻断，按原 W1 边界判断；
- 只有语法、import、路径、已确认 API、明确类型或输出接线等唯一机械修复才可在 `SOURCE_ROOT` 修改；
- 修改必须保存 `repair.diff`、最终 HEAD、status 和每次运行日志；
- 不进行无界诊断或无上限重试。

## 十一、必须停止并回 E

- 精确 F 实例没有既存 `fields.json`；
- 需要调用 `f.rerun()` 或全历史 producer；
- 需要改变 SOF、品种、日历、5m、2021—2022、`groupKnownFrom`；
- 需要读取 Q/V；
- 需要改变业务字段、面板、图元、标准化、交互或阅读语义；
- 需要修改平台库或使用近似数据；
- 正确修法不唯一或语义影响不明；
- 私有 IPC 只能通过扩大宿主写权限实现；
- 发现同一 W002 未知在途、非单写者或不明产物。

## 十二、W002 交付

至少返回：

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
source staging：<report>
private shm：<mount / alias / probe evidence>
最终脚本：<path + HEAD>
候选 HTML：<path；无则明确>
运行日志：<path>
退出码：<integer/unknown>
实际修改：<diff；无则明确>
首个阻断：<无或精确事实>
definition_run_report：<path；无则明确>
```

正式 Return：

```text
schema=longrun-worker-return/v2
work_order_id=W002
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
order_ref=<本 W002 ORDER.json 精确 commit>
```

Worker 不判断 HTML 是否专业接受，也不启动正式取数。

## 十三、E 续接

W002 Return 回原 executor:E1 后继续：

```text
D005 / WI-E / M-E
```

- 仍无 HTML：E2 消费新的首个阻断；
- 有 HTML：E2 核脚本／diff 后进入 E3，与 D 和 C2 核对；
- 只有 E3 接受图后才允许正式取数工单。
