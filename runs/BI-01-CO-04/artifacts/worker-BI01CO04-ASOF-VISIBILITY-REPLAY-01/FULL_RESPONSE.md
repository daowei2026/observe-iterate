order_id: BI01CO04-ASOF-VISIBILITY-REPLAY-01
work_id: BI-01
run_id: BI-01-CO-04
issuer_invocation_id: BI01-CO-04-R0007-WORKER-INTAKE-c149d108
return_to: chatgpt:BI-01-CO-04:management

# 新有限技术工单完整回交

**最终出口：B — BLOCKED_NO_LOOKAHEAD_PROOF。**

原临时目录错误已修复，原生 PNV 路由也已修复；六组同一原引擎的固定前缀计算全部完成并得到524条真实输出。最终阻断是没有取得主增量执行的逐事件状态及 input frontier 观察入口，不能构造可审计 first-seen/撤回/重现账本。固定前缀重算数值通过不等于无未来资格通过；本单不交第三种“基本可用”出口。

## 身份、授权和输入

- replay_run_id：`BI01CO04_ASOF_REPLAY_20261101T203232Z_f4a75f64`；没有沿用或重命名旧GTQH run。
- 完整原单SHA256：85512f2daafd0b5d9d145750216e266390c74ce03f30ff88d32a10445677f997；原单和12项必读全文读取及固定提交字节核验见WORKER_ORDER、REQUIRED_READS。
- 管理采用：956ae5891409e0092dd453d1379017486dca0d76；旧包输入基线：dfdf843b47c03c0121fd7151b72f24adb5d986c0；专业固定来源b6ccf766dac055a793e75f76b77a73f4cfc74064。
- 原生执行器版本e6.2.0.6，SHA256=dba166c7fc8d0acf2e56499699b36ac47dd30c923a739e52a7288860fae57450；同一selected big/mid参数，没有修改数学、排序、阈值或浮点路径。
- rb/hc/i、30m、warm-up从2021-01-04 09:30；decision窗口至2021-09-30 15:00。每品种2160根原生PNV输入，数值payload与此前实际消费FAO前缀逐字段字节相同。

## 已执行与修复边界

初期错误地把“一次有限执行”机械理解为进程次数，曾生成中间B结论；Owner工程范围澄清后已纠正。原Goal保留，不另建Goal、不恢复旧单；所有初始实际调用、失败和中间态仍保存于diagnostics/logs，不改记为未执行。

实际9次原生调用：首次/tmp EACCES；第二次设置owned TMPDIR成功后暴露PNV路径缺件；第三次提供同源原生PNV前缀后完成rb/big；第四次关闭strace及只读scope并完成同前缀计算；第五至九次完成其余五组。另有一次Python前置断言中止，发生在Popen之前，未额外启动原生引擎。精确command/cwd/环境、开始/结束、rc及stdout/stderr/strace均在各EXECUTION receipt和logs中。

进程rc=0但有`Edh program crashed`时仍判失败；打印参数/初始化不是计算完成。实际成功同时有完成标记、原生文件和回读对象。没有未知在途重放动作。

## 实物和准确测试结果

| 检查 | 结果及范围 |
|---|---|
| 源字节/新identity | 原单、旧包、同一二进制、所用配置、原生PNV前缀和实际加载代码/库有逐文件hash及实物；完整 qualified observer/source 合同未成立 |
| 六组原生固定前缀 | rb big14/mid112；hc big20/mid109；i big45/mid224；共524行 |
| 数值与正式基线 | 524/524恢复前缀行逐元组及重数匹配；原正式96行中95匹配，1条旧i/mid晚event单列；620行全部保留，无静默丢弃 |
| instrumentation on/off | rb/big同2160-bar前缀的14行，原生event/actual/confirm/价格/顺序完全相等；只证明此固定前缀 |
| 批次输入边界 | 实际strace确认rb/big打开owned PNV；无F盘行情回退打开；30个PNV前缀文件计算后hash不变；未得到逐事件读frontier |
| 原生观察能力 | 实测8个公开class方法，没有状态订阅/step回读；当前history入口只有结束后文件输出，不能据此填first_seen |
| 主逐事件monotone/known-time | 未证明；VISIBILITY六行为明确批次状态，lifecycle零观察；没有把event_ts/xConfirm倒填 |
| 全变化prefix invariance | 未证明；没有可作对照的合格主事件账本 |
| tail删除/扰动 | 未执行；没有声称通过，未消费tail |
| failure injection | 独立validator的六类结构坏包均被拒绝；不是生产无未来测试PASS；真实包伪称A也必须拒绝 |
| receipt/离线validator | 逐文件封口并由独立消费者重算；最终结果见INDEPENDENT_VALIDATION与封口日志 |

## copied / wrapper / recomputed 分账

- copied：copied/baseline为旧96文件原字节；frozen为原二进制、原入口、实际加载代码/库及支持性源码快照。
- wrapper-only：输入前缀文件封装与路由、TMPDIR、Landlock写面限制、strace、只读scope、回读、来源hash和validator；补丁随包。没有向原行情/共享源码写入。
- recomputed：execution/cache的原E结果和recomputed/、RECOMPUTED_OBJECT_ROWS，是真实原引擎重新计算的数值。它们标记为BATCH_OUTPUT，不伪称逐事件已知状态。
- diagnostics/superseded中的中间B记录已被修复后的事实取代，只供审计；当前结论由本报告和REPLAY_MANIFEST给出。

## 最终阻断与全部未完

BLOCKER_REPORT和NATIVE_OBSERVABILITY_ASSESSMENT给出实测方法清单、结束后输出证据、受影响范围和最小恢复条件。阻断覆盖全部三品种/两尺度的decision window和必要warm-up。

本单没有证明算法本质上不能因果重放，也没有把已修好的环境问题继续当blocker。缺的是同一冻结原生执行的逐事件观察与实际输入frontier绑定；独立batch查询不能未经合同替换主增量观察。需要同一引擎的只观察回调/状态读回合同，或Management具名采用不同查询式known-time合同，并重新完成原单第9节全部生产检验。

未完包括：完整逐事件/生命周期、monotone/read audit、全部状态变化的独立prefix/first-seen、tail删除/扰动、逐事件neutrality、完整observer冻结及session/夜盘交易日映射、Professional输入资格。原Management尚需接收本新包；原Professional尚未继续，业务T/排序/候选或无候选/自然挑战/方法反馈/业务Gate均未由Worker执行。

## GitHub 与回交

仓库daowei2026/observe-iterate，分支fy/feature-based-case-observation；唯一输出`runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/`。数据基线commit：`0cf1f1e9cd56f442d0b94657058f480eb761daa1`；最终完整封口为其后继提交，精确SHA由本聊天回交，避免自引用。只回原Management供技术接收，不发其他聊天、不操作手机、不改旧包、管理决定、任务、地图、Intake或主控Goal。
