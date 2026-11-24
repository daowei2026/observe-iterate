# C0004／D002｜原L0 X实际回交

本次完整rb/m正式X未完成。rb的当前默认实例全年产物已核验成功；m的当前Wall已物化，但Build原生调用在交易日分块前失败，没有Build fields或receipt。不能进入完整正式范围G，也不构成Build验收。本D只做X工程动作，未执行G、偏差诊断、参数调整或实现修复。

## 准确身份与采用

- Run `OI-EAW-P1-BUILD-STAT-20261124-01`；原executor:E1；C0004；D002；work_item `EAW-P1-BUILD-X-R01`；stage `X-R01`；`CODEX_NATIVE_DIRECT / AUTONOMOUS / workers=[]`。
- Invocation：`daowei2026/observe-iterate@93cdba6ebd154e74f64bbf1a419045c1cd3ec9a6:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/calls/C0004/INVOCATION.json`；唯一token沿原件核对，本报告不另造token或物理回执。
- D002 JSON：`daowei2026/observe-iterate@df705ec129a532130198cbbfe966e3b4f27acc1f:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/delegations/D002/DELEGATION.json`；同commit MD：`daowei2026/observe-iterate@df705ec129a532130198cbbfe966e3b4f27acc1f:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/delegations/D002/DELEGATION.md`。
- 原manager触发：`daowei2026/observe-iterate@cc80d1af22ac2845f34f934aec0b9cdc131dada5:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/calls/C0003/PRO_RETURN.json`。来源共21份准确Git对象已读，见结果目录`SOURCE_READ_MANIFEST.json`。
- 专业控制 `391adcd18bd2da82c13c01710980f41e01c7de25`；TIS `179016111ed0394f92025313e46bd13534932a74`；唯一业务输入：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:task-inputs/eaw-p1-build-stat-20261124/BUILD_RUN_INPUT.md`。继续消费原U包，无业务/代码/参数变化，不重复U。
- 运行使用`./run-python.sh -B`，解释器`/m3c3/Linux/apps/anaconda3/bin/python`，实际TIS路径`/dwdhome/fy/BASE_E6_2/mquant/tis`。

## 正式范围与实例

SOF `TA_updto20240229_DBA`；仅rb/m；请求2021-01-01至2021-12-31；Calendar `night_end_at_2300`。两品种实际原始输入均9,959,400行，首2021-01-04 09:00:00.500000，末2021-12-31 15:00:00；索引唯一且递增。未缩短范围，也未以小窗口替代全年。原始DBA前后元数据相同，证据不扩称为全部源数据内容hash。

Build ppid `BuildAssembler_954318e844386b1a4967d626990a21e0be640bfd`；Wall ppid `WallAssembler_f32460448c4bde6d0a683cfc262808694c9f0a75`。完整嵌套ppdict、param_path、Qt参数、trading_unit及实际source_scope均在`FeatureRunResultBinding.json`逐品种给出。构造默认窗口None在有效core参数中为3/3，未人为重设参数。

旧共享rb Build/rb Wall/m Wall receipt与当前锁定实现不符，因此均未复用。使用平台已有`TmpStoreEnv(True, store_dir=...)`，所有新Feature缓存/结果位于本调用`formal_store`，`backup_full_dirs=[]`；这是存储路径选择，未改业务实现、参数或输入。未消费Attack副本的产物或控制。

## 实际结果与读取校验

| 品种 | 当前Wall | 当前Build | 完整请求范围后继 |
|---|---|---|---|
| rb | 全年243块完成；trace 9,959,400行，与Build原始轴相同 | 全年243块完成并落盘；6个公开流全部精确读回 | rb结果保留为当前正式结果 |
| m | 全年243块完成；trace 9,959,383行，比Build原始轴少17行 | 原生交易日分块ValueError；无fields/receipt | 完整rb/m X仍缺m Build |

rb全部物理lane如下，不能只读主lane：

| lane | 行数 |
|---|---:|
| `build__stream` | 197837 |
| `build__stream__occ0001` | 42949 |
| `build__stream__occ0002` | 6564 |
| `build__stream__occ0003` | 413 |
| `build__stream__occ0004` | 70 |
| `build__stream__occ0005` | 4 |

rb最初`DataFrame.equals`读回guard因列顺序不等而失败，原始记录保留。后续在同一正式锁下，当前Wall/VolQuant设置OnlyRead，Build设置Cal，完整原生重放在内存中完成。按全部列名对齐后逐值、索引、ts精确比较；唯一dtype差异为当前导出器既有的`availability_code int8 → int64`。6个lane全部通过，正式DBA、fields及receipt的SHA/size/mtime均未变；随后禁止Feature执行，独立DAO再次读取全部6个lane并核行数。`RB_READBACK_RECONCILIATION.json`与`POSTCHECK.json`解释原始状态和最终有效状态的区别，未覆盖原始失败记录。

rb Build receipt为`build_activity-v1.6.1`、`build-default`、`status=success`，code_version为`git:179016111ed0394f92025313e46bd13534932a74+source-sha256:924da4d9388a44039df47207d10b0b3b7f740a463c064d20eeae908da817cee1`。它对本次当前Wall artifact/code/instance/参数/schema的exact引用已核，receipt来源范围与rb实际输入一致。Wall仅为技术上游可用证据，不代表Wall合理性Release。

m真实内层异常：`ValueError: 交易日区间在 2021-03-12 00:00:00 前不连续: 1792800 != 1792801`。调用栈：`BuildAssembler._impl → run_build_assembler_trading_day_chunks → support._trading_day_chunk_plan`；原件见`M_BUILD_ERROR.json`，没有构造成功receipt。m轴差17行及17个全空quote时间点另在绑定/输入中逐项记录；本D只报告观察与运行停止位置，不把它们升级为finding或认定最早责任逻辑。

## 共享写面与保留证据

所有Feature生产及rb内存重放沿用户指定的同一`flock`：`/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock`，inode `15061041`。实际取得与释放证据见`LOCK_EVIDENCE.json`；未改锁文件内容，结束为0字节。控制器此前的探测未冒充本次占锁。原正式调用从`2026-11-24T07:57:23.352125+00:00`至`2026-11-24T08:42:45.580053+00:00`，后继核验也分别实际占用同一锁。

TIS HEAD仍`179016111ed0394f92025313e46bd13534932a74`，仍为原Wall分支`codex/wall-output-consistency-20261121`。本D无TIS修改、commit或push。唯一已有tracked改动`frpExample/STCalendar.py`原样保留，SHA256 `3001e49a3b812b5281ddca12795e5aa279d5ca09fd510ba0a4cfc330b42c6980`；来源未定，未单独追踪全执行链影响，不声明零影响。framework HEAD `4d0ff8f2640e07a8b9ff066c48114f451fca6cfe`、tracked clean。共享历史产物fields/receipt前后核对不变，未覆盖旧结果。

前检曾遇只读FD独占NFS锁EBADF和错误读取SubCC accessor；首次构造guard曾直接比较tuple与JSON list误报。均仅修正调用脚本，未执行Feature或改业务代码。后续真实生产及rb读回校验按原件保留，见`ENGINEERING_ATTEMPTS.json`。没有实际工具审批拒绝；普通运行异常不冒充系统审批结果。

## 交付与未完成边界

原生产DBA保留于`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-build-stat-20261124-01/calls/C0004/formal_store`。GitHub交付完整绑定、receipt、所有公开表inventory、结果文件SHA256、代码/参数/输入/上游、锁和读回证据及运行脚本；不上传多GB市场DBA。既有U中的dense/Stop原因/typed/来源未知STCalendar限制继续有效；FRP未执行。

结果入口为`longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/delegations/D002/results/X-R01/FeatureRunResultBinding.json`。未完成范围见同次提交`calls/C0004/REMAINING_SCOPE.md`，恢复衔接见`CONTINUATION.md`。V2 Return使用`IN_PROGRESS`，回原manager；由controller负责真实跨Chat回交，E1不向其他Chat发送消息，不设Owner节点、不签W或新D。manager按原L0消费真实X缺口，不把工程返回当Build验收。
