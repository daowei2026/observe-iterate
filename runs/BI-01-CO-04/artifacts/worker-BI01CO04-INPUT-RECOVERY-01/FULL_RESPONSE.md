order_id: BI01CO04-INPUT-RECOVERY-01
work_id: BI-01
run_id: BI-01-CO-04
issuer_invocation_id: BI01-CO-04-R0006-PROFESSIONAL-INTAKE-6fd91174
return_to: chatgpt:BI-01-CO-04:management

# 有限 Worker 工单技术回交

**结果：真实恢复包已形成；P0 为 PARTIAL_BLOCKED_FOR_ASOF，随包交准确 BLOCKER_REPORT。**

本工单恢复了原运行的真实字节、参数消费链和静态图，完成字节与结构复核。时间可知语义、方向关联及生命周期合同仍不足，不能宣告输入完全合格或让 Professional 据此开始 as-of 比较。Worker 没有选择 T、排序品种、判断候选／无候选或作市场判断。

本单为 Owner 备用授权新聊天的唯一实际派发，替代不可接单的原 Worker；只管理本聊天 Goal。原单全文及六必读均已完整读取并核固定版本，原单 SHA256 与派发值相等。没有修改管理面、启动其他聊天或操作手机。

## 1. P0／P1 状态

| 工单项 | 状态 | 已交付及准确限制 |
|---|---|---|
| 5.1 正式实例身份 | PARTIAL | 同一 run brief/summary/manifest/timespan/stats、源根/输出根、三品种30m、warm-up/覆盖、aidata commit、E版本/二进制hash均可核；完整历史build与冻结日历版本未取得 |
| 5.2 实际参数及消费 | SATISFIED | selected JSON 原字节；六组task hash=prepared_jobs；任务全参数=原engine log全JSON；ppid=selected/validated；validated及合并CSV hash正确，正式slice源物理行与合并CSV相符 |
| 5.3 正式行情 | PARTIAL | 三份原正式slice各368行；实际消费缓存只读导出各2160行，含1784行前置warm-up及376行完整观察窗，至9月30日15:00；日历与bar/index时间冲突未解 |
| 5.4 大／中对象 | PARTIAL | 六份正式slice合计96行；前缀整理524条原有事件，actual/confirm UTI与价格均连到真实行情；原字段无方向、object id、revision及生命周期合同，不造值 |
| 5.5 语义词典 | PARTIAL | 已交字段来源、actual/confirm/event、UTI、轮次、空值及失败区分；publish/known、时区、夜盘交易日、revision/撤回/更新仍列明未知 |
| 5.6 Receipt | SATISFIED | 逐文件source/path/hash/bytes/rows/首末时间/tool/version/复制或整理/source_run/状态；外层SHA256SUMS封口并可离线独立复核 |
| P1 图面 | SATISFIED_EXISTING_STATIC_EXPORT | 取得并目视查看原platform_plot.png；附node6153/run/config/原图与slice匹配证明。未刷新线上页面或新建节点，不把历史截图当当前可知状态 |

整体不是 P0 全通过。适合交原签发 Management 做技术接收和具名补件；**不足以作为合格输入直接恢复 Professional 的 as-of 研究**。

## 2. 恢复数量与时间边界

| 品种 | 原正式行情 | 含warm-up整理行情 | 原正式big／mid | 事件前缀big／mid |
|---|---:|---:|---:|---:|
| rb | 368 | 2160 | 2／18 | 14／112 |
| hc | 368 | 2160 | 1／16 | 20／109 |
| i | 368 | 2160 | 12／47 | 45／224 |

- 原 run：GTQH_C001_three_turns_20261101_162005；board node=big_000001，平台node=6153。big窗口层级与large特征尺度分开。
- 原 Context 从源起点读取，每品种原输入8964根，源实际首末为2021-01-04 09:30至2024-02-08 15:00。本包只交实际warm-up和观察范围，不复制2024全历史。
- 原显示／正式slice窗口至2021-09-30 00:00，原行情实际至9月29日23:00。本包只读整理按closeTs<2021-10-01，末条为9月30日15:00，不填夜盘或节假日。
- 在保留范围内每品种182处calendar_close_time与bar closeTs不等，合计546处，其中观察窗96处。三品种时间轴相同不能消除同一坐标的解释冲突。完整逐行证据见TIME_MAPPING_CONFLICTS。
- 原正式i/mid有1条event_ts=2021-10-08 09:30的事件，实际x落于9月29日23:00，xConfirm_ts为9月30日15:00。原字节保留；截至9月末的事件整理排除。不能任选三个时间中的最早者当可知时间。

## 3. copied 与 regenerated

- copied/：原单、实际参数、六组任务/执行日志/收据、运行manifest、三行情和六大中slice、日历配置/读取语义源码、原PNG及对应证明，均逐文件原字节复制。
- regenerated/：从原运行实际消费staging KLine及既有大中CSV只读截取，添加来源键、字段状态及两套时间映射；未运行数值引擎、未改变价格/坐标、未重新计算特征。
- evidence/、scripts/和报告：本工单工程整理、核验与可独立复核工具。原selected JSON含small配置、原PNG含small图例；没有补小尺度数据或据此增加业务门槛。
- exact数值重生条件未全部成立，算法重生次数=0；没有参数寻优、修改业务算法或全市场重算。

## 4. 实际版本、命令与核验

原 E 日志版本e6.2.0.6；原执行器SHA256=dba166c7fc8d0acf2e56499699b36ac47dd30c923a739e52a7288860fae57450。aidata历史/当前commit=b5a752c2701dd8997b47583808f30bc5da5d9769。其余现场checkout和tracked差异见ENVIRONMENT；不声称全工作区等同该SHA。

实际运行与离线复核命令见SOURCE_AND_REPRODUCTION。恢复用现有Python3.10环境、numpy/pandas/pydim只读DBA；receipt复核仅stdlib，无源盘依赖。完成的检查包括：

1. 三品种、30m、实际warm-up与完整9月30日覆盖逐一核对。
2. task→engine参数、validated→合并CSV hash、正式slice→原物理行逐项核对。
3. 原正式行情与原实际消费缓存重叠OHLC/量/仓/UTI逐值相等；整理对象actual/confirm UTI及价格精确对应。
4. 对缺方向、缺版本、两轮结果、时间冲突、窗口后event分别保留真实状态，不补造无信号结论。
5. 独立消费者脚本重算文件集合、逐文件hash/bytes/CSV行数/首末时间及外层seal；INDEPENDENT_VALIDATION给出字节通过与语义阻断分开的结果。

## 5. 全部未完与最小恢复条件

BLOCKER_REPORT逐项列B01—B04。需要原输入生产者补：UTI/bar/index/publish的权威时间合同及冻结版本、时区/session/夜盘交易日；本0.5%上游zig参数/缓存与逐对象方向映射；对象id/revision/撤回/更新/current/segment合同或证明不可变的事件合同；如确需数值重生，再补完整exact build与依赖绑定。

Management尚未接收本技术包，Professional尚未恢复输入资格或执行首个合法T、比较、候选／无候选、自然挑战及方法反馈。所有业务Gate、主控Goal及长程任务保持原责任与状态。本Worker不代管理更新Intake，不续发Professional。

## 6. GitHub 交付

- 仓库：daowei2026/observe-iterate；分支：fy/feature-based-case-observation。
- 唯一输出：runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/。
- 数据提交及最终完整提交采用两阶段封口：数据commit在本报告最终封口时写入；最终完整commit的精确SHA由本聊天最终回交给原Management/主控，避免把本文件自身commit SHA写入自身造成循环。
- 本单完成的是技术包与准确blocker回交；不是市场输入合格或业务任务完成。后续只由原签发Management消费并决定下一步。
