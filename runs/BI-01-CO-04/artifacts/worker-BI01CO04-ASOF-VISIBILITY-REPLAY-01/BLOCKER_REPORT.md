# BI01CO04-ASOF-VISIBILITY-REPLAY-01 准确阻断

出口：**B — BLOCKED_NO_LOOKAHEAD_PROOF**。

最终阻断是 `EVENT_OBSERVATION_AND_PER_EVENT_INPUT_FRONTIER_NOT_EXPOSED`。临时目录和原生 PNV 路由均已修复，不再把首次环境错误当成最终原因。本报告只证明本次所采用原生入口与 wrapper 的可知性证明没有成立；不证明算法本质上不可因果重放。

## 1. 已实际执行，不是准备或模拟

9 次原生进程调用完整保留；2 次初始化失败，7 次计算完成。另有一次 Python 前置断言失败，没有额外启动原生进程。

| 调用 | 实际结果 | 证据 |
|---|---|---|
| 1：原入口 + owned 写边界 | 已进入参数初始化和模型调用；`/tmp/hsfis…` 创建 EACCES，返回码却为0；未完成计算 | EXECUTION_RECEIPT、logs/native_engine.* |
| Python 临时目录预检查 | 错误地用 stdout 非空判断禁止继续，在 Popen 前断言停止；非一次额外引擎调用 | logs/bootstrap_temp_check.python.stderr、历史 wrapper 与修复 patch |
| 2：同入口仅加 owned TMPDIR | hsfis 创建/读取成功；随后原生 PNV open.dba 不存在，返回码0但程序崩溃 | BOOTSTRAP_TEMP_CHECK_RECEIPT、logs/temp_redirect_check.* |
| 3：提供原生 PNV 前缀 | 2,160 输入事件；rb/big 12+2=14 条输出；有真实完成标记 | NATIVE_PREFIX_ROUTE_EXECUTION、PNV_PREFIX_ROUTE_RECEIPT、logs/pnv_prefix_probe.* |
| 4：同前缀关闭 strace + 只读 scope | rb/big 14 行与调用3逐事件/坐标/价格完全一致；实际读出公开方法清单 | OBSERVER_CAPABILITY_EXECUTION、INSTRUMENTATION_NEUTRALITY |
| 5—9：其余5组同一原入口/数学/参数/前缀 | 全部计算完成，六组合计524条原生事件 | MATRIX_EXECUTION_RECEIPTS、recomputed/ |

actual command/cwd/环境白名单、开始/结束、rc、stdout/stderr、strace、binary 与 wrapper 字节均随包。`rc=0` 未冒充成功；必须同时核无 crash、完成标记和真实结果。

## 2. 最终承重失败点

1. 实测原生 class 的8个公开方法没有逐事件状态订阅或 step/state/frontier 回读；native 实例也未暴露可访问的状态 scope。
2. 当前正式 history 入口提供的是结束后结果文件；strace 与日志能证明整批2,160输入和最终对象字节，不能给每个内部事件配对实际读到的最大 source row 与输出/撤回/重现。
3. 因而没有合法的主逐事件账本，不能将静态 event_ts/xConfirm、批次结束时间或复制行号倒填为 first_seen。所有524条重算记录都保持这项未知。
4. 无主账本意味着逐变化 independent prefix invariance、first-seen 对照、tail 删除/扰动对完整 decision ledger 的不变性均未完成。固定前缀数值一致和坏包 validator 拒绝测试均不能补足它。
5. 细分 session、交易所标签/夜盘 trading_day 的冻结时间映射仍未形成；现有21:00/20:00配置和新时区声明不等于完整合同。

受影响范围：rb/hc/i × big/mid 全部；完整 decision window，及实际 warm-up 中需要给出首次可知状态的对象。不是只影响旧 i/mid 的某一条晚 event。

## 3. 为什么本单不继续换路线

相同 batch 调用已实际成功。重复这类调用只增加终态快照，不能从这些快照中观察已经结束的内部发射/撤回顺序。第9.2节独立前缀是对主顺序重放的校验，不能被静默改成另一种“查询完成即known”的主可知性定义。

目前公开 realtime 方法只有启动、停止和推送，尚没有被证明能观察逐事件完整状态。未经验证地换到另一种 realtime/查询语义，或重编未知版本的 native core 来增加内部 hook，会超出本次保持同一冻结数学及浮点路径的可证明范围。因此本单在具名观察合同缺口处停止，不再搜索旧聊天、参数寻优或循环重跑。

这是一项**本次边界内的证据不足/接口缺件证明**，不是声称任何后续工程方法都不可能成功。

## 4. 最小恢复条件

- 为同一冻结原生二进制提供有证据的逐事件输出/状态回读与实际 input frontier 观察入口；只观察，不改排序、阈值、浮点路径和数学。
- 观察行必须能关联到当前 canonical bar、真实前缀 hash 和 replay-local 对象连接规则；回调、撤回/重现、无状态与失败需可区分。
- 对该观察入口完成 on/off neutrality、全量变化 prefix invariance、尾部删除/扰动及坏包注入；同时补齐冻结的 session/夜盘归属合同。
- 如果 Management 改为具名采用查询式前缀可知性合同，应先明确新的 primary replay/known-time定义及其验收，Worker 不自行更换它。

## 5. 可保留与全部未完

可保留：新 identity；旧包96文件原字节；新冻结原生输入/配置/二进制/加载源码/动态库；所有失败与修复记录；6组524条真实重算；rb/big on/off 14行精确相等；620行基线逐条保留并比对（619匹配，旧正式 i/mid 第568行 event=2021-10-08 单列为冻结前缀之外，未删掉）；独立 validator 及六类结构注入。

未完：主逐事件可见性/生命周期、完整 per-event monotone/read audit、每次变化的 independent prefix/first-seen、尾部删除/扰动、全逐事件 instrumentation neutrality、完整 source-to-observer 合同与 session 映射、Professional 输入资格。Management 尚未接收本新技术包；原 Professional、业务T/排序/候选或无候选、自然挑战、方法判断与业务Gate均未由本Worker执行。
