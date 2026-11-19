# W007｜核对 FY 当前正常 FQV 包来源，并在唯一正常入口成立时重跑原 D

## 1. 工单身份

- `run_id / work_order_id / parent_delegation_id`: `OI-U2-F-OBS-20261118-01 / W007 / D006`
- `issuer`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `issuer_call_id`: `C0024`
- `worker`: `codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`

本 W007 是 D006 下的第二张 W1 短执行卡。它消费 W006 的真实 STOP，基准不变；不继续 D005/W005，不复用旧 overlay／环境拼装方案。

## 2. 专业分类与原件

- E2 分类：`daowei2026/observe-iterate@54fb6c997210ffe7bebb67abf52f61473bc523d2:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W006_RESULT_CLASSIFICATION_AND_W007_BASELINE_D006_C0024.md`
- W006 正式 Return：`daowei2026/observe-iterate@b499d528dbca99d153b86a216833b7da8b5140d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W006/WORKER_RETURN.json`
- W006 事实报告：`daowei2026/observe-iterate@86bd00fbb7e61a969ac730b43b7bd19b34f69254:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W006/FACT_REPORT.md`
- W006 constructor 报告：`daowei2026/observe-iterate@86bd00fbb7e61a969ac730b43b7bd19b34f69254:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W006/constructor_import_report.json`
- 原 D：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- 原 C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- 锁定 TIS 正常构造：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- 锁定 FRP F 实现：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
- 2026-11-16 正常包装成功说明：`daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:discuss-materials/u2-u3长程任务安排以及经验总结讨论/FQV改用KLine和正常Python包装-本轮改动说明-20261116.md`

W006 已证明当前 `m3rc` Python 能进入 D `main()`，但活跃 `mquant.tis.frp` 无法导入 `fqv_kline_example`。W007 不再重复 `/usr/bin/python` 尝试。

## 3. 工作区、授权与本工单实际写面

```text
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
```

逐字授权：

```text
Owner 预先选择指令原文：碰到需要我处理的问题，先选第一项
适用请求：OR001；被选择的第一项：A. 确认首选 sem.* 机读补正；
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**,/dev/shm/sem.*
`/dev/shm` 只允许本 Run 的 CAEGraph 运行进程及其子进程为 Python multiprocessing 临时创建和删除 POSIX semaphore 对象 `sem.*`；不得写任意共享内存 payload、不得使用 sudo、不得建立 mount 绕过、不得 patch 平台源码、不得调用 F producer、不得读取 Q/V、不得据此启动正式数据导出。
```

本 W007 将实际新文件进一步收敛到：

```text
/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W007/**
```

除 CAEGraph 正常进程可能临时使用授权的 `sem.*` 外，不写 TIS、FRP、m3、uplot、平台包、D/C3 原件或其他 Run 历史。

## 4. 目标

只回答并执行以下有界分支：

```text
当前 FY 工作区是否已经有一个单一、完整、正常、与锁定版本一致的 FQV Python/Haskell 运行来源？

是
→ 不修改环境，按原 D 运行一次，返回 HTML 或新的首阻断。

否／不能证明
→ 不建设环境，返回精确来源差异和阻断。
```

不要求大环境快照，不做通用审计包。

## 5. 第一步：当前活跃运行包最小核对

只加载当前工作区既有 `m3rc`；不运行 `/usr/bin/python`，不创建新环境。

用 `/m3c3/Linux/apps/anaconda3/bin/python` 形成一个最小 JSON，至少记录：

```text
python executable / version
sys.path
mquant.__file__ / __path__
mquant.frame.__file__ / __path__
mquant.tis.__file__ / __path__
mquant.tis.frp.__file__ / __path__
find_spec(mquant.tis.frp.fqv_kline_example)
find_spec(F/Q/V 三个 wrapper)
```

输出：

```text
$RUN_ROOT/current_runtime_provenance.json
$RUN_ROOT/logs/current_runtime_provenance.log
```

不得修改 `sys.path`、`mquant.__path__`、`mquant.tis.__path__` 或 `mquant.tis.frp.__path__` 后再做这项核对。

## 6. 第二步：当前工作区源码来源的有界核对

### 6.1 活跃 TIS 路径

以 W006 已确认的活跃路径为起点：

```text
/dwdhome/fy/BASE_E6_2_copy/mquant/tis
```

只记录：

```text
realpath
git --show-toplevel（若不是 Git 工作树则明确记录）
git HEAD
origin URL
status --porcelain（限本次所需文件）
以下文件是否存在、是否 tracked、是否有工作树修改：
  frp/fqv_kline_example.py
  frp/CommonPriceTurnGroupCandidates.py
  frp/PostTurnGroupDirectionalOrganization.py
  frp/CommonTurnGroupValidity.py
```

若本地 Git 对象中存在锁定 commit，可只读检查：

```text
HEAD 是否等于 2f460d663d821cf2ba25555eda13e78b697d0767
git diff --quiet 2f460d... -- 上述四个文件
```

不得 fetch、pull、checkout、reset、restore 或复制锁定文件。

### 6.2 当前工作区内精确文件名的一次有界查找

只在：

```text
/dwdhome/fy/BASE_E6_2_copy
```

查找精确文件名 `fqv_kline_example.py`，并排除：

```text
observe-iterate-runs/**
.git/**
__pycache__/**
其他工作区或 /run 下的路径
```

每个命中只记录路径、Git root、HEAD 和是否属于一个完整单一 `mquant` 包。不得把旧 W checkout、其他工作区或不完整源码目录接入运行。

### 6.3 FRP Haskell 来源

只读核对固定路径：

```text
/dwdhome/fy/BASE_E6_2_copy/edh-universe/frp/frp
```

记录：

```text
realpath
Git HEAD
origin URL
锁定 commit 67711c... 是否等于 HEAD
若本地对象存在，锁定 commit 是否为 HEAD 祖先，以及目标 F 文件与锁定版本是否有 diff
```

不得切换版本、构建或安装。

输出一个最小汇总：

```text
$RUN_ROOT/normal_fqv_entry_decision.json
```

## 7. 唯一允许的“正常入口成立”判据

只有全部满足，才可以再次运行 D：

1. 当前 `m3rc` 激活后，`mquant`、`mquant.frame`、`mquant.tis` 与 `mquant.tis.frp` 的来源清楚；
2. `mquant.tis.frp.fqv_kline_example` 在**未修改 import path** 时可导入；
3. 构造模块和 F/Q/V wrapper 来自同一个完整 TIS Git 工作树，而不是两个来源拼接；
4. TIS 工作树 HEAD 为锁定 `2f460d...`，且四个相关文件无本地修改；
5. FRP 固定源码路径 HEAD 为锁定 `67711c...`；
6. 不需要安装、重建、生成 package 文件、切版本、复制／软链文件或修改平台；
7. 没有使用 `observe-iterate-runs/**` 中的旧 TIS staging 作为运行包。

只要任一项不满足，就不得以“可能兼容”“文件看起来相同”代替精确锁定版本运行。

## 8. 条件成立时：原 D 运行一次

沿用 W006 已核验的精确 D/C3 原件：

```text
SOURCE_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate
REL_D=longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py
D sha256=92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f
C3 sha256=798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7
```

重新核 hash；一致后执行：

```bash
RUN_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W007
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
cd "$SOURCE_ROOT"
/m3c3/Linux/apps/anaconda3/bin/python "$REL_D" \
  --output-dir "$OUTPUT_ROOT" \
  > "$LOG_ROOT/w007_run.log" 2>&1
printf '%s\n' "$?" > "$LOG_ROOT/w007_run.exit_code"
```

不得调用 `f.rerun()`、实例运行脚本的 rerun 模式或任何 producer。D 自己会只读检查精确 F 的 `fields.json`。

若产生 HTML，回传候选图和 run report；若失败，回传本次新的首阻断。若是 D/C3 允许的唯一机械问题，可在 W007 自己 `repair_source/` 中修复一次并保留 diff；不得修改 TIS/FRP/平台源码。

## 9. 条件不成立时：停止分类

从以下状态中选一项或多项，并用实际事实说明：

```text
LOCKED_TIS_NORMAL_PACKAGE_ABSENT
ACTIVE_TIS_VERSION_MISMATCH
ACTIVE_TIS_WORKTREE_DIRTY_OR_INCOMPLETE
MULTIPLE_OR_PARTIAL_PACKAGE_SOURCES
LOCKED_FRP_SOURCE_VERSION_MISMATCH
FRP_RUNTIME_PROVENANCE_UNRESOLVED
```

此时：

- 不再运行 D；
- 不提出或执行 overlay；
- 不从其他工作区借文件；
- 不安装／构建／补包；
- 不修改版本；
- 不把历史成功结果冒充本次结果。

## 10. 明确禁止

```text
Landlock / namespace / mount / sudo
pip / conda install
stack / cabal build or install
git fetch / pull / checkout / switch / reset / restore
seed_inits.py / pretty-exports.py
复制、软链或生成 fqv_kline_example.py
修改任何 package __path__
PYTHONPATH 拼接第二套 TIS
锁定 TIS 新层 + 平台旧层混包
执行其他工作区绝对路径中的代码
修改 TIS / FRP / m3 / uplot / 平台包
调用 F producer / rerun
读取 Q/V 产品
启动 W2 或正式数据导出
```

## 11. 最小回报

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
当前 Python：<executable/version>
活跃 TIS：<root/HEAD/origin/files>
活跃 FRP：<root/HEAD/origin>
正常入口判据：PASS / FAIL + failed clauses
D 实际启动次数：0 或 1（如唯一机械修复后复跑，另列）
最终 D：<path/hash>
候选 HTML：<path；无写无>
definition_run_report：<path；无写无>
运行日志：<path；未运行写无>
实际修改：<W007 repair.diff；无修改写无>
当前阻断：<精确分类；无写无>
```

正式使用 `longrun-worker-return/v2` 回原 `executor:E2`。Worker 只交付来源事实、运行事实和实物，不决定 E3 图接受、E4 准入或整个 E 完成。

## 12. 幂等与在途

- W007 首次物理派发前状态为 `NOT_SENT`；真实发送后才是 `IN_FLIGHT`。
- 若 `$RUN_ROOT` 不存在，创建后执行。
- 若已存在本 W007 的明确 provenance／decision／运行回执，先对账，不覆盖重跑。
- 若状态未知、发现并发写者或无法判定既有动作，返回 `EFFECT_UNKNOWN`。
