# W006｜在当前真实环境运行 F 的原 D CAEGraph 定义

## 1. 工单身份

- `run_id / work_order_id / parent_delegation_id`: `OI-U2-F-OBS-20261118-01 / W006 / D006`
- `issuer`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `issuer_call_id`: `C0023`
- `worker`: `codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`

本 W006 是 D006 下的新 W1 工单。它不续派 W005，不复用 W001～W004 的执行方案，也不把旧运行结果算作本次结果。

## 2. 专业基准和原件

- E1 最小基准：`daowei2026/observe-iterate@3dff93bcbe19a8d6e7324f2a527a43d1adbeb807:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E1_EXECUTION_AND_GRAPH_CHECK_BASELINE_D006_C0023.md`
- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- D 集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- C3 代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- C2 核图基准：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`

唯一业务对象是正常 `make_features(...)` 返回的第一项 `f`。不得读取 Q/V，不得调用 F producer。

## 3. 工作区、授权与写面

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

本次实际新输出收敛到：

```text
/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/**
```

## 4. 先运行，不先建设环境

收到工单后先做一次原 D 真实运行。不得先加入 Landlock、namespace 或额外沙箱；不得先重建／补装平台、构造 TIS overlay、混合新旧 package、制作大环境报告或审计包。

### 4.1 有界选择原 D 源码根

只检查以下两个已有候选，不做无界搜索：

```bash
BASE=/dwdhome/fy/BASE_E6_2_copy
CANDIDATE_CURRENT="$BASE/observe-iterate"
CANDIDATE_EXACT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate"
REL_D=longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py
REL_C3=longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py
```

选择第一个同时满足下列条件的目录作为 `SOURCE_ROOT`：

```text
REL_D 存在且 sha256 = 92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f
REL_C3 存在且 sha256 = 798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7
```

`CANDIDATE_EXACT` 只提供已存在的精确 D/C3 原件；不得使用其旧输出、旧 overlay、旧运行日志或旧业务结论。本 W 的输出和 Return 必须独立产生。

若两个候选均不存在或内容不匹配，返回 `BLOCKED`，说明精确源码位置缺失；不得默认新建 checkout、拼装未知本地源码或继续旧 W 的 staging 方案。

### 4.2 FRP Haskell 与 TIS Python 必须分开

- Haskell 来源：`/dwdhome/fy/BASE_E6_2_copy/edh-universe/frp/frp` 对应 `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`；只记录实际路径／HEAD（可取得时），不把它放入 Python import。
- Python 构造入口：当前 FY Python 环境中的 `mquant.tis.frp.fqv_kline_example`，锁定源码为 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`。

不要修改 `PYTHONPATH` 去叠加另一套 TIS，不要把 Haskell `frp` 仓库解释为 Python `mquant.tis.frp`。

## 5. 第一次真实运行

```bash
RUN_ROOT=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
mkdir -p "$OUTPUT_ROOT" "$LOG_ROOT"
cd "$SOURCE_ROOT"
python "$REL_D" \
  --output-dir "$OUTPUT_ROOT" \
  > "$LOG_ROOT/w006_run.log" \
  2>&1
RUN_EXIT=$?
printf '%s\n' "$RUN_EXIT" > "$LOG_ROOT/w006_run.exit_code"
```

若 FY 当前正式 Python 入口不是命令名 `python`，可使用现场已配置的等价入口；记录实际命令，但不得新建环境或切换项目版本。

第一次运行的目标只有两个：

1. 生成可打开的 `$OUTPUT_ROOT/u2_f_caegraph.html`；或
2. 生成本次新的第一个真实阻断与 `$OUTPUT_ROOT/definition_run_report.json`。

D 脚本顺带产生的 `prepared_tables/`、`plot_data/` 在 W006 中只是候选运行副产物，不是 E4/W2 正式数据，不得标记 `DATA_READY`。

## 6. 第一次失败后的有界机械处理

不得一报错就停止；先依据日志和 `definition_run_report.json` 判断是否属于以下唯一机械问题：

- Python 语法；
- 当前已有模块／文件的确定性 import 或路径接线；
- 锁定版本中已核实的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、文件名、日志、静态 HTML 接线。

若修法唯一且只需修改 D/C3：

1. 在 `$RUN_ROOT/repair_source/` 下按原相对结构复制精确 D/C3；
2. 只修改该 run-local 副本；
3. 保存 `$RUN_ROOT/repair.diff`；
4. 从修复副本再运行一次并记录独立日志。

禁止修改或复制拼装 `mquant.tis`、Haskell FRP、uplot、m3、mquant 平台源码／安装；禁止新建 overlay、切换仓库版本或调用 producer。

若 import 失败，允许做一次最小定位：记录 `mquant.tis.frp.fqv_kline_example` 能否导入及其 `__file__`，以及异常链中的首个缺失模块。若问题显示当前 package 来源不完整、版本不匹配或需要混合 package，停止并回 E；不要构造替代环境。

## 7. 必须停止并回 E

- 需要改变 SOF、品种、日历、5m 尺度、2021～2022 时间或 `groupKnownFrom`；
- 需要增加、删除、替换业务字段，读取 Q/V，另算近似值或运行 F producer；
- 需要改变 C2 主附图、图元、时间表达、标准化、交互或业务阅读语义；
- 当前 TIS／FRP／运行环境与锁定版本的差异没有唯一机械修法；
- 正确修法不唯一或无法判断语义影响；
- 超出授权写面、存在破坏性风险、现场并发冲突或动作效果未知。

## 8. 最小交付

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
实际 SOURCE_ROOT：<path>
实际 Python 入口：<command>
TIS 构造模块：<import succeeded + __file__；失败则首个缺失模块>
FRP Haskell 来源：<path + HEAD；无法取得则说明>
最终脚本：<原 D path，或 W006 repair_source path>
候选 HTML：<path；未生成写无>
运行日志：<path>
退出码：<integer/unknown>
definition_run_report：<path；未生成写无>
实际修改：<repair.diff；无修改写无>
当前阻断：<首个真实阻断；无写无>
```

正式返回使用 `longrun-worker-return/v2`，回到 `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`。Worker 只交付事实和实物，不判断图是否通过，不启动 W2。

## 9. 幂等、在途与冲突

- 本 W006 首次派发前状态应为 `NOT_SENT`；主控真实发送后才变为 `IN_FLIGHT`。
- 若 `$RUN_ROOT` 不存在，创建后执行。
- 若 `$RUN_ROOT` 已存在且有本 W006 的明确运行日志／报告，先核对原动作状态；不得覆盖或重复执行。
- 若目录来源不明、旧动作效果未知或同一工作区已有冲突写者，返回 `EFFECT_UNKNOWN`。
- W006 Return 到达后由 E2 进入 E2 分类；工单发布或物理发送不等于 E 完成。