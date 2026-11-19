# W009｜纠正 W008 的过宽 symlink 门禁，核验同一现有 runtime 并条件运行原 D

## 1. 工单身份

- `run_id / work_order_id / parent_delegation_id`: `OI-U2-F-OBS-20261118-01 / W009 / D006`
- `issuer`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `issuer_call_id`: `C0026`
- `worker`: `codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`

本 W009 是 D006 下新的 W1 revision。它消费 W008 的真实 STOP，纠正 W008 目录级门禁的假阳性；不重派 W008，不恢复 D005/W005，不建设新环境。

## 2. 专业分类与原件

- E2 分类：`daowei2026/observe-iterate@a3cd1b34702e7658d8ea5e69d157e187c9fcabd3:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W008_CLASSIFICATION_AND_W009_CORRECTED_RUNTIME_GATE_D006_C0026.md`
- W008 正式 Return：`daowei2026/observe-iterate@be3f2f9c2102fc182909140234921f7ad3d4457b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/WORKER_RETURN.json`
- W008 事实报告：`daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/FACT_REPORT.md`
- W008 inventory：`daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/candidate_inventory.json`
- 原 D：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- 原 C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- 锁定 TIS：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`
- 锁定 FRP：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`

固定候选仍只有：

```text
CANDIDATE=/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
CANDIDATE_RUNTIME=$CANDIDATE/runtime
CANDIDATE_TIS=$CANDIDATE_RUNTIME/mquant/tis
```

不得搜索第二个 runtime。

## 3. 授权与写面

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

本 W009 新输出只写：

```text
RUN_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009
```

候选 runtime、当前 TIS、固定 FRP、D/C3 和历史 W 均只读。

## 4. 对 W008 symlink 事实的正确处理

已知：

```text
$CANDIDATE_RUNTIME/.codex
  -> /dwdhome/fy/BASE_E6_2_copy/.codex
```

本 W：

- 记录该链接；
- 不跟随、不读取其目标；
- **不因链接存在本身判 FAIL**；
- 只有候选已有入口明确依赖它，或实际 origin probe 显示 Python executable、`sys.path`、`mquant*` 模块来自该外部目标时，才分类为 `DEDICATED_RUNTIME_EXTERNAL_SOURCE_LEAK`。

## 5. 第一步：读取候选已有元数据与入口

只在候选根内读取已经存在的：

```text
provenance.json
README* / MANIFEST* / manifest*
PROVENANCE* / provenance*
SOURCE* / BUILD*
activate* / env*.sh / run*.sh / bin/python*
```

不跟随离开候选根的 symlink。输出一个简短：

```text
$RUN_ROOT/candidate_entry_and_provenance.json
```

识别候选已经存在的正常入口，允许形式仅为：

1. 候选自带 Python executable；
2. 候选自带 activation／launcher；
3. 候选 `provenance.json`／manifest 明确记录的现有运行命令或环境设置。

可以按候选已有入口设置其已经声明的进程级环境变量；不得新写 wrapper、activation、`.pth`、`sitecustomize`，不得自行发明第二套 `PYTHONPATH`。

若没有既有入口，返回：

```text
DEDICATED_RUNTIME_ENTRY_ABSENT
```

并停止。

## 6. 第二步：锁定来源和单一包核对

### 6.1 TIS 四文件

用当前活跃 TIS Git 仓库中已经存在的本地 commit 对象，只读比较：

```text
2f460d663d821cf2ba25555eda13e78b697d0767:
  frp/fqv_kline_example.py
  frp/CommonPriceTurnGroupCandidates.py
  frp/PostTurnGroupDirectionalOrganization.py
  frp/CommonTurnGroupValidity.py
```

与候选：

```text
$CANDIDATE_TIS/frp/<same filename>
```

记录每项存在性、候选 sha256、锁定 blob sha256、字节相等结论。缺失或不等即：

```text
DEDICATED_RUNTIME_TIS_LOCK_MISMATCH
```

并停止。

### 6.2 TIS 完整性

候选自身必须提供正常构造需要的：

```text
mquant.tis.blk.gen
mquant.tis.t0
mquant.tis.t1
mquant.tis.t2
mquant.tis.t3
```

不得从当前活跃 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis` 或旧 W staging 补齐。缺失即：

```text
DEDICATED_RUNTIME_TIS_INCOMPLETE
```

并停止。

### 6.3 FRP provenance

候选自身已有 provenance／manifest／build receipt 必须明确、可追溯地记录：

```text
FRP source commit = 67711c492da909ed0f044f357beb278abf7fc71c
```

明确为其他 commit：

```text
DEDICATED_RUNTIME_FRP_LOCK_MISMATCH
```

没有可核记录：

```text
DEDICATED_RUNTIME_FRP_PROVENANCE_NOT_PROVEN
```

并停止。不得从当前非锁定源码树重建。

## 7. 第三步：使用候选已有入口做 origin probe

仅在第 5、6 节全部通过后执行。Probe 不调用 `make_features`、FAO、producer 或产品读取。

记录：

```text
python executable / version
sys.path
mquant.__file__ / __path__
mquant.frame.__file__ / __path__
mquant.tis.__file__ / __path__
mquant.tis.frp.__file__ / __path__
fqv_kline_example.__file__
F/Q/V wrapper __file__
blk.gen / t0 / t1 / t2 / t3 origins
probe 后 sys.modules 中全部 mquant.* 模块的 origin
```

准入要求：

- 构造模块和 F/Q/V wrappers 可导入；
- probe 加载的全部 `mquant*` 模块均来自同一个 `$CANDIDATE_RUNTIME/mquant` 根；
- 没有模块来自当前活跃 TIS、旧 `observe-iterate-runs/**`、`.codex` 目标、其他工作区或 `/run`；
- 没有运行时修改 package `__path__` 来拼接来源。

失败分类：

```text
DEDICATED_RUNTIME_IMPORT_FAILED
DEDICATED_RUNTIME_MIXED_MQUANT_ORIGINS
DEDICATED_RUNTIME_EXTERNAL_SOURCE_LEAK
```

输出：

```text
$RUN_ROOT/dedicated_runtime_provenance.json
$RUN_ROOT/logs/dedicated_runtime_probe.log
```

## 8. 第四步：全部准入后运行原 D 一次

### 8.1 原件核验

```text
SOURCE_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate
REL_D=longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py
REL_C3=longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py
D sha256=92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f
C3 sha256=798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7
```

重新核 hash；不一致则停止，不复制、不修复。

### 8.2 执行

使用候选已经核准的现有入口运行：

```text
$SOURCE_ROOT/$REL_D
--output-dir $RUN_ROOT/output/u2_f_caegraph
```

记录实际 argv、入口、环境摘要、时间、退出码和日志：

```text
$RUN_ROOT/execution_receipt.json
$RUN_ROOT/logs/w009_run.log
$RUN_ROOT/logs/w009_run.exit_code
```

本 W 不修改 D/C3，不修补 runtime。返回：

1. 可打开的候选 `u2_f_caegraph.html`；或
2. 新的首个真实阻断和 D 的 `definition_run_report.json`（若已形成）。

D 顺带形成的表仍不是 E4/W2 正式数据。

## 9. 禁止

```text
第二 runtime 搜索
Landlock / namespace / mount / sudo
pip / conda / stack / cabal 安装或构建
git fetch / pull / checkout / switch / reset / restore
seed_inits.py / pretty-exports.py
复制、软链或生成 FQV/TIS 文件
新建 wrapper / activation / launcher / .pth / sitecustomize
候选 TIS + 当前活跃 TIS 分层组合
旧 Run TIS staging 或其他工作区代码入口
修改 TIS / FRP / m3 / uplot / D / C3
调用 F producer / rerun
读取 Q/V 产品
启动 W2 或正式数据导出
```

## 10. 最小回报与确定停止点

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
候选入口：<path/type>
TIS 四文件锁定核对：PASS / FAIL / NOT_RUN
TIS 单一完整来源：PASS / FAIL / NOT_RUN
FRP provenance：PASS / FAIL / NOT_PROVEN / NOT_RUN
origin probe：PASS / FAIL / NOT_RUN
总准入：PASS / FAIL
D 启动次数：0 或 1
候选 HTML：<path；无写无>
definition_run_report：<path；无写无>
运行日志：<path；未运行写无>
实际修改：无
当前阻断：<精确分类；无写无>
```

正式使用 `longrun-worker-return/v2` 回原 `executor:E2`。

若入口、TIS 锁定、TIS 单一来源、FRP provenance 或 origin probe 任一失败，立即 STOP；不得继续环境探测。E2 将据此形成：

```text
EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

若全部通过，才运行 D。Worker 不判断 E3 图接受、E4 准入或 E 完成。

## 11. 幂等与在途

- W009 首次物理派发前为 `NOT_SENT`；真实发送后才是 `IN_FLIGHT`。
- 若 `RUN_ROOT` 已存在明确 W009 回执，先对账，不覆盖重跑。
- 状态未知、发现并发写者或无法判断既有动作时，返回 `EFFECT_UNKNOWN`。
