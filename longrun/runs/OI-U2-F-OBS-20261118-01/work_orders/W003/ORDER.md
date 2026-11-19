# W003｜CAEGraph W1 revision：按 OR001 新授权直接运行 D

## 一、通用 Worker 工单身份

- `run_id / work_order_id / parent_delegation_id`：`OI-U2-F-OBS-20261118-01 / W003 / D005`
- `issuer / issuer_call_id`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1 / C0019`
- `worker`：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- 操作类别：新的 **W1 运行／有限机械修复 revision**；不是正式取数 W2。

W001、W002 均已有确定 `STOP` 结果并已由原 E1 消费；当前没有未知在途。本工单使用新的可去重动作身份 `W003`，不覆盖或清理 W001/W002 产物。

## 二、为什么属于原 D005

原 E2 分类是：

```text
RUNTIME_IPC_CAPABILITY_AND_AUTHORITY_GAP
```

Owner 对 OR001 第一项 A 的既有选择指令已经被 manager 采用，并发布了新的 operation-specific Binding。它允许本 Run 的 CAEGraph 进程树为 Python multiprocessing 临时创建和删除 `/dev/shm/sem.*`。

因此，当前基准不变，合法后继是继续原 D005/E 的 W1 运行：用同一 D 定义、同一实例、同一位置和同一 C2 展示基准，按正常平台入口真实运行一次。

## 三、当前权威引用

- 当前 D005 JSON：`daowei2026/observe-iterate@7b2353915a15ecf29bc39eaaa0ea7f1f5be3dee8:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 当前 D005 正文：`daowei2026/observe-iterate@51bb129c486c2654286fb9d990c18865c3d847ab:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.md`
- C0019 基准：`daowei2026/observe-iterate@7881b0694af2166ea9d0d041938e36454085843b:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_OR001_RESOLUTION_AND_W003_BASELINE.md`
- Owner 第一项采用记录：`daowei2026/observe-iterate@1e6392ad185c9be31367f0001f82e83aa53ad14e:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_OR001_FIRST_OPTION_ADOPTION_20261119.md`
- 当前 Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 当前 Resource Binding：`daowei2026/observe-iterate@ec2c6c495327c885b02424714bd88d8d67dbceaa:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- 物理 Worker 绑定证据：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`
- W001 Return：`daowei2026/observe-iterate@7beda1b54e7777b5b4f86ef6174376570e4c8b1a:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W001/WORKER_RETURN.json`
- W002 Return：`daowei2026/observe-iterate@08f9944755ac4ba8786249edb25ea4f5b5cab555:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W002/WORKER_RETURN.json`

唯一运行定义与核图输入：

- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- C2 当前预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- 固定 source commit：`f4f0e4b276b1118b779473c1fbe462bc7a64b358`

唯一业务对象仍为 `make_features(...)[0]` 返回的 F。Q/V 不进入本工单。

## 四、精确操作权限

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

`authority_quote` 必须按当前 Binding 原样采用：

```text
Owner 预先选择指令原文：碰到需要我处理的问题，先选第一项
适用请求：OR001；被选择的第一项：A. 确认首选 sem.* 机读补正；
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
`/dev/shm` 只允许本 Run 的 CAEGraph 运行进程及其子进程为 Python multiprocessing 临时创建和删除 POSIX semaphore 对象 `sem.*`；不得写任意共享内存 payload、不得使用 sudo、不得建立 mount 绕过、不得 patch 平台源码、不得调用 F producer、不得读取 Q/V、不得据此启动正式数据导出。
```

持久写入进一步收敛到：

```text
/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/**
```

除 D 进程树临时创建／删除的 `/dev/shm/sem.*` 外，不写工作区外任何路径；不修改平台源码、生产数据、其他仓库或其他 Run。

## 五、run root、幂等与 source staging

```bash
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003"
SOURCE_ROOT="$RUN_ROOT/source/observe-iterate"
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
D_COMMIT=f4f0e4b276b1118b779473c1fbe462bc7a64b358
```

### 幂等检查

- `RUN_ROOT` 不存在：创建后继续。
- `RUN_ROOT` 已存在且有本 W003 完整 receipt：先核对动作、提交和结果，不重复运行。
- `RUN_ROOT` 已存在但来源未知、内容不匹配、部分动作效果不明或已有同一 W003 在途：返回 `EFFECT_UNKNOWN`，不得覆盖、清理或另建第二套结果。

### source staging

在 `SOURCE_ROOT` 建立本 Run 专用 detached checkout：

```bash
mkdir -p "$RUN_ROOT/source" "$OUTPUT_ROOT" "$LOG_ROOT" \
  "$RUN_ROOT/cache/tmp" "$RUN_ROOT/cache/xdg" \
  "$RUN_ROOT/cache/numba" "$RUN_ROOT/cache/matplotlib"

git init "$SOURCE_ROOT"
git -C "$SOURCE_ROOT" remote add origin https://github.com/daowei2026/observe-iterate.git
git -C "$SOURCE_ROOT" -c protocol.version=2 fetch --filter=blob:none --no-tags \
  origin refs/heads/runs/OI-U2-F-OBS-20261118-01:refs/remotes/origin/run
git -C "$SOURCE_ROOT" checkout --detach "$D_COMMIT"
```

若目录已由本 W003 正确建立，按幂等规则复用，不重复 `remote add` 或盲目覆盖。

运行前验证：

```bash
test "$(git -C "$SOURCE_ROOT" rev-parse HEAD)" = "$D_COMMIT"
test -f "$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py"
test -f "$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py"
```

写出 `source_stage_report.json`，至少记录 run、W003、remote、requested commit、actual HEAD、source root、D/C3 path 和 created/reused。

## 六、直接真实运行

### 6.1 运行包络

本次使用正常平台入口：

- 不使用 W001 的 Landlock／`boundary_runner.py`；
- 不使用 W002 的 `unshare`、user namespace 或 mount namespace；
- 不使用 sudo；
- 不 patch `/dwdhome/fy/BASE_E6_2_copy/mquant/**` 或其他平台库；
- 不先以独立 SemLock probe 替代 D；
- D 首次运行本身就是本次真实反馈入口。

### 6.2 环境与命令

复用 W001 已验证的工作区环境接线，但直接执行 D：

```bash
export PYTHONDONTWRITEBYTECODE=1
source "$BASE/m3rc"

if [[ -z "${M3HOST:-}" ]]; then
  M3HOST="$(python - <<'PYHOST'
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(("gogs.dw", 443))
    print(sock.getsockname()[0])
PYHOST
)"
  export M3HOST
fi

export NO_PROXY="${NO_PROXY:+${NO_PROXY},}${M3HOST},localhost,127.0.0.1,gogs.dw"
export no_proxy="$NO_PROXY"

if [[ -d "$BASE/.runtime/python-deps" ]]; then
  export PYTHONPATH="$BASE/.runtime/python-deps${PYTHONPATH:+:$PYTHONPATH}"
fi

export LD_PRELOAD="/lib/x86_64-linux-gnu/libssl.so.3:/lib/x86_64-linux-gnu/libcrypto.so.3${LD_PRELOAD:+:$LD_PRELOAD}"
export TMPDIR="$RUN_ROOT/cache/tmp"
export XDG_CACHE_HOME="$RUN_ROOT/cache/xdg"
export NUMBA_CACHE_DIR="$RUN_ROOT/cache/numba"
export MPLCONFIGDIR="$RUN_ROOT/cache/matplotlib"
ulimit -c 0

cd "$SOURCE_ROOT"
python \
  longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir "$OUTPUT_ROOT" \
  > "$LOG_ROOT/w003_run.log" \
  2>&1
RUN_EXIT=$?
printf '%s\n' "$RUN_EXIT" > "$LOG_ROOT/w003_run.exit_code"
```

若正式 Python 入口不是命令名 `python`，可使用工作区已配置的等价入口，但不得新建环境、升级依赖或切换平台版本；实际命令必须入日志。

D 第一次运行后优先回报候选 HTML或首个真实阻断。不得用无界诊断延迟首次事实回交。

## 七、临时 semaphore 的最小审计边界

运行前后可只读记录：

```bash
find /dev/shm -maxdepth 1 -name 'sem.*' \
  -printf '%f\t%u\t%g\t%m\t%s\t%T@\t%i\n' | sort
```

分别写入：

```text
$LOG_ROOT/dev_shm_sem.before.tsv
$LOG_ROOT/dev_shm_sem.after.tsv
```

规则：

- 不删除运行前已存在的 `sem.*`；
- 不由 wrapper 手工创建测试 semaphore；
- 不读写非 `sem.*` 对象；
- 正常 semaphore 创建／删除只由 D 进程树及其 Python multiprocessing 子进程完成；
- 不删除无法证明属于本次进程树的对象；
- 若本次可归属的 `sem.*` 在进程退出后残留，保存事实并回 E，不扩大清理动作。

## 八、可以直接修

只允许不改变业务含义的确定性机械问题：

- Python 语法、import、模块或文件路径；
- 锁定版本中已经核实的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、文件名、日志和静态 HTML 接线；
- 已由本工单明确授权的临时 semaphore 运行接线。

若修改 D/C3，只能改 W003 detached source tree，并保存：

```text
$RUN_ROOT/repair.diff
$RUN_ROOT/final_git_status.txt
```

不得推送或无痕改写 GitHub 原件。修复后每次运行必须保存独立日志和 attempt count；不做无上限重试。

## 九、必须停止并回 E

- 精确 F 实例没有既存 `fields.json`；
- 需要调用 `f.rerun()` 或输入排除的全历史 producer；
- 需要改变 `TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i`；
- 需要改变 B 的 `2021-01-01—2022-12-31` 或 `groupKnownFrom`；
- 需要读取 Q/V；
- 需要删除、增加、替换业务字段或另算近似值；
- 需要改变 C2 主图／附图、图元、时间表达、标准化、交互或阅读语义；
- 需要写 `/dev/shm` 中非 `sem.*` 内容；
- 需要 sudo、mount、namespace、平台库 patch 或其他未授权写面；
- 正确修法不唯一，或无法判断语义影响；
- 发现工作区冲突、非单写者、同一 W003 未知结果或动作效果未知。

## 十、W1 诊断副产物与正式取数边界

D 可能随候选运行写出：

```text
prepared_tables/
plot_data/
definition_run_report.json
```

在 W003 中这些仅属于运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不属于正式 W2 数据；
- 不得据此标记 `DATA_READY`；
- 不得修改 D 来扩大导出范围。

Worker 不判断最终图是否接受，也不启动正式数据导出。

## 十一、预期交付物与最小回报

至少返回：

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
source staging：<source_stage_report.json>
最终脚本：<SOURCE_ROOT path + HEAD>
候选 HTML：<path；未生成写无>
运行日志：<path>
D attempt count：<integer>
D 退出码：<integer/unknown>
实际修改：<repair.diff；无修改写无>
当前阻断：<首个真实阻断；无写无>
definition_run_report：<path；没有写无>
semaphore 事实：<before/after paths；残留或异常说明>
```

若生成 HTML，还应回报文件存在性、非零大小和可打开性检查；不得替 E 作专业接受判断。

正式 Return：

```text
schema=longrun-worker-return/v2
work_order_id=W003
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
order_ref=<本 W003 ORDER.json 精确 commit>
```

## 十二、失败、部分交付、重复和冲突

- 失败或部分结果：保留日志、report、HTML、diff 和 semaphore 记录，按真实状态返回；
- 无候选 occurrence／空表：按真实结果返回，不解释成失败或业务反证；
- 输出目录存在未知来源结果：`EFFECT_UNKNOWN`，先对账，不覆盖、不盲目重跑；
- 首次运行出现首个明确阻断：优先立即回报，不先写长说明；
- W003 已有确定结果时，不再次派发同一动作。

## 十三、续接

W003 正式 Worker Return 回原 executor:E1 后继续原：

```text
D005 / WI-E / M-E
```

有 HTML时进入 E2/E3；没有 HTML时消费新的首个真实阻断。只有 E3 接受最终图后，才允许正式取数准入和新的数据导出工单。
