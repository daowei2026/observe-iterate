# W008｜核验唯一现有 FQV dedicated runtime，并仅在精确准入后运行原 D

## 1. 工单身份

- `run_id / work_order_id / parent_delegation_id`: `OI-U2-F-OBS-20261118-01 / W008 / D006`
- `issuer`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `issuer_call_id`: `C0025`
- `worker`: `codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`

本 W008 是 D006 下新的 W1 revision。它消费 W007 的真实 STOP；不续派 W007，不恢复 D005/W005，不采用旧 overlay、package materialization 或环境拼装方案。

## 2. 专业分类与原件

- E2 分类：`daowei2026/observe-iterate@f7ab7dcaf526e17f1ed796e9665014e35d0c74a2:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W007_CLASSIFICATION_AND_W008_RUNTIME_GATE_D006_C0025.md`
- W007 正式 Return：`daowei2026/observe-iterate@4566786786e8e754700c9cf2cafbbf66b44f030b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W007/WORKER_RETURN.json`
- W007 事实报告：`daowei2026/observe-iterate@130a62ef96ec32c0211a00a6ffb87208debf8e5b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W007/FACT_REPORT.md`
- W007 判据：`daowei2026/observe-iterate@130a62ef96ec32c0211a00a6ffb87208debf8e5b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W007/normal_fqv_entry_decision.json`
- 原 D：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- 原 C3：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- 锁定 TIS：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`
- 锁定 FRP：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`
- Owner 重启原文：`daowei2026/observe-iterate@ae7c4e6a389cc63d2d187d27c0d6b8f10a5e2eb7:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_E_RESTART_20261119.md`

W007 已证明当前默认 `m3rc` 活跃 TIS/FRP 与锁定组合不一致，但在当前工作区内只发现一个非旧 Run staging 的候选：

```text
CANDIDATE=/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
CANDIDATE_RUNTIME=$CANDIDATE/runtime
CANDIDATE_TIS=$CANDIDATE_RUNTIME/mquant/tis
```

本工单只核验这个精确候选，不继续搜索其他 runtime。

## 3. 工作区、授权与本工单写面

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

本 W008 的新输出进一步收敛到：

```text
RUN_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W008
```

候选 runtime、当前 TIS、固定 FRP、D/C3 和旧 Run 历史均只读。

## 4. 唯一目标与总分支

只回答：

```text
该 CANDIDATE 是否已经是一个无需安装、构建、切版本、复制、软链、overlay 或 package 混合即可使用的单一正常、锁定来源 FQV runtime？
```

处理分支：

```text
PASS
→ 使用候选已有正常入口运行原 D 一次；
→ 返回候选 HTML 或新的首个真实阻断。

FAIL / NOT_PROVEN
→ 不运行 D；
→ 返回精确失败条款；
→ 不建设环境。
```

## 5. 第一步：只读核验候选自身

### 5.1 候选存在性和有限目录清单

只检查 `CANDIDATE`，不得扩大搜索范围。记录：

- `realpath`；
- 候选根、`runtime/`、`runtime/mquant/`、`runtime/mquant/tis/` 是否存在；
- 候选根三层以内已经存在的 `README*`、`MANIFEST*`、`manifest*`、`PROVENANCE*`、`provenance*`、`SOURCE*`、`BUILD*`、`activate*`、`env*.sh`、`run*.sh`、`bin/python*`；
- 不跟随离开候选根的 symlink；遇到外部 symlink 只记录并判 FAIL。

不得制作全目录审计。

### 5.2 既有正常入口

候选必须已经提供可识别的正常入口之一：

- 候选自带 Python executable；或
- 候选自带 activation／launcher，且只选择这个候选 runtime，不修改 package `__path__`，不拼接第二套 TIS；或
- 候选 manifest 明确规定的等价现有入口。

只读检查入口内容和实际环境变量。不得新写 wrapper、activation、`sitecustomize`、`.pth` 或 launcher。

没有既有正常入口，分类：

```text
DEDICATED_RUNTIME_ENTRY_ABSENT
```

并停止。

### 5.3 TIS 锁定来源核对

当前活跃 TIS repo 已证明本地拥有锁定 commit 对象。只读比较候选文件与：

```text
2f460d663d821cf2ba25555eda13e78b697d0767:
  frp/fqv_kline_example.py
  frp/CommonPriceTurnGroupCandidates.py
  frp/PostTurnGroupDirectionalOrganization.py
  frp/CommonTurnGroupValidity.py
```

对每项记录候选路径、存在性、sha256、锁定 blob sha256 和字节相等结论。任何一项缺失或不等，分类：

```text
DEDICATED_RUNTIME_TIS_LOCK_MISMATCH
```

并停止。

候选还必须在同一个 `CANDIDATE_TIS` 中具备正常运行所需的 `blk.gen` 和 `t0/t1/t2/t3` 包／模块；这些不得来自当前活跃 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis`。缺失时分类：

```text
DEDICATED_RUNTIME_TIS_INCOMPLETE
```

并停止。

### 5.4 FRP 锁定 provenance

候选自身已有的 manifest／provenance／build receipt 必须明确、可追溯地记录：

```text
FRP source commit = 67711c492da909ed0f044f357beb278abf7fc71c
```

仅凭当前固定源码树存在、单个 Haskell 文件相似、目录日期或 runtime 名称，不算证明。没有候选自身明确来源记录，分类：

```text
DEDICATED_RUNTIME_FRP_PROVENANCE_NOT_PROVEN
```

若明确记录为其他 commit，分类：

```text
DEDICATED_RUNTIME_FRP_LOCK_MISMATCH
```

并停止。不得从当前非锁定 FRP tree 重新构建。

## 6. 第二步：在候选既有入口下做最小 origin probe

仅在第 5 节全部通过后，使用候选已有入口运行一个不调用 `make_features`、不调用 producer 的最小 probe，记录：

```text
python executable / version
sys.path
mquant.__file__ / __path__
mquant.frame.__file__ / __path__
mquant.tis.__file__ / __path__
mquant.tis.frp.__file__ / __path__
mquant.tis.frp.fqv_kline_example.__file__
F/Q/V wrapper __file__
mquant.tis.blk.gen.__file__
mquant.tis.t0/t1/t2/t3 __file__ or package paths
```

准入要求：

1. 构造模块和 F/Q/V wrappers 全部可导入；
2. 所有 `mquant.tis*` 来源均在同一个 `CANDIDATE_TIS` 下；
3. 没有任何 `mquant.tis*` 来源来自当前活跃 TIS、旧 `observe-iterate-runs/**`、其他工作区或 `/run`；
4. probe 未修改 `sys.path` 或任何 package `__path__`；
5. 没有调用 `make_features`、FAO、producer 或产品读取。

不满足时，从以下分类中选择并停止：

```text
DEDICATED_RUNTIME_IMPORT_FAILED
DEDICATED_RUNTIME_MIXED_TIS_ORIGINS
DEDICATED_RUNTIME_EXTERNAL_SOURCE_LEAK
```

输出：

```text
$RUN_ROOT/dedicated_runtime_provenance.json
$RUN_ROOT/logs/dedicated_runtime_probe.log
```

## 7. 第三步：准入通过后运行原 D 一次

只有第 5、6 节全部 PASS，才继续。

### 7.1 原 D/C3 只读核验

```text
SOURCE_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate
REL_D=longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py
REL_C3=longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py
D sha256=92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f
C3 sha256=798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7
```

hash 不一致则停止；不得复制或修复。

### 7.2 运行

使用候选已核准的现有入口，保持 D 的原参数，只改变 W008 输出目录：

```text
OUTPUT_ROOT=$RUN_ROOT/output/u2_f_caegraph
```

等价目标命令：

```text
<candidate-existing-python-or-launcher> \
  $SOURCE_ROOT/$REL_D \
  --output-dir $OUTPUT_ROOT
```

实际 argv、入口、环境摘要、开始／结束时间、退出码写入：

```text
$RUN_ROOT/execution_receipt.json
$RUN_ROOT/logs/w008_run.log
$RUN_ROOT/logs/w008_run.exit_code
```

本 W008 不修改 D/C3，也不在失败后修补 runtime。运行结果只能是：

1. 可打开候选 `$OUTPUT_ROOT/u2_f_caegraph.html`；或
2. 新的第一个真实阻断及 D 自己形成的 `definition_run_report.json`（若有）。

D 自带的 prepared tables／plot data 仍是候选运行副产物，不是 E4/W2 正式数据。

## 8. 明确禁止

```text
第二个 runtime 搜索
Landlock / namespace / mount / sudo
pip / conda install
stack / cabal build or install
git fetch / pull / checkout / switch / reset / restore
seed_inits.py / pretty-exports.py
复制、软链或生成 FQV / TIS 文件
修改 sys.path 或 package __path__ 拼接来源
候选 TIS + 当前活跃 TIS 分层组合
旧 Run TIS staging
其他工作区或 /run 的绝对代码入口
修改 TIS / FRP / m3 / uplot / 平台包
修改 D / C3
调用 F producer / rerun
读取 Q/V 产品
启动 W2 或正式数据导出
```

## 9. 最小回报

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
候选 runtime：<path>
候选既有入口：<path/type；无则写无>
TIS 四文件锁定核对：PASS / FAIL
TIS 单一完整来源：PASS / FAIL
FRP 锁定 provenance：PASS / FAIL / NOT_PROVEN
origin probe：PASS / FAIL / NOT_RUN
总准入：PASS / FAIL
失败分类：<精确分类；无写无>
D 实际启动次数：0 或 1
最终 D：<path/hash>
候选 HTML：<path；无写无>
definition_run_report：<path；无写无>
运行日志：<path；未运行写无>
实际修改：无
当前阻断：<首个真实阻断；无写无>
```

正式使用 `longrun-worker-return/v2` 回原 `executor:E2`。Worker 只交付来源事实、准入事实、运行事实和实物，不决定 E3 图接受、E4 准入或整个 E 完成。

## 10. 幂等、在途与确定停止点

- W008 首次物理派发前状态为 `NOT_SENT`；真实发送后才是 `IN_FLIGHT`。
- 若 `RUN_ROOT` 不存在，创建后执行。
- 若已存在 W008 的明确 provenance／execution receipt，先对账，不覆盖重跑。
- 状态未知、发现并发写者或无法判断既有动作时，返回 `EFFECT_UNKNOWN`。
- 任一准入条款失败后不再运行 D，也不继续环境探测。
- W008 若因 runtime 准入失败 STOP，E 的下一专业状态将是 `EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED`，不再签发同类 W1。
