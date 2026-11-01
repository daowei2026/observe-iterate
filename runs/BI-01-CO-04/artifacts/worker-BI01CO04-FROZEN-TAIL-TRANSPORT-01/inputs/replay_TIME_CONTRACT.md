# 新 replay 的时间合同与未通过项

replay_run_id：`BI01CO04_ASOF_REPLAY_20261101T203232Z_f4a75f64`。

本单采用 `KLine.closeTs` 作为拟议 consumer clock，显式按 `Asia/Shanghai` 解释源无时区文本；执行环境 `TZ=Asia/Shanghai`。这是新 identity 的明确解释，未改动原 `.dba` 的时间/UTI/价格字节，也不声称修复了旧 run 的历史时间合同。

- warm-up：2021-01-04 09:30:00 起；decision window：2021-08-15 00:00:00 至 2021-09-30 15:00:00，末 bar 包含在内。
- 六组实际固定前缀计算每组只提供 2,160 根原生 PNV bar，末条为 2021-09-30 15:00。当前没有提供或消费 evaluation tail；尾部删除/扰动检验未完成，不以“未提供尾部”冒充不变性测试通过。
- 每品种 source row 使用原行情零基序号，当前固定前缀最大为 2159。PNV 数值 payload 与旧包实际消费 FAO 前缀逐字段字节相等；原字段 open/high/low/close/volume/openInt/openUti/closeUti/openTs/closeTs 全保留。
- 原配置的 session 边界是 21:00 至次日 20:00。原始文件没有逐行 exchange/trading_day 标签；本单没有把无时区文本、calendar naiveDate 或夜盘的自然日期直接改成正式交易日。交易所、细分 session 和夜盘交易日的冻结映射仍属未完成合同，不制造新交易日列。
- 旧 B01 的两套值均保留在 `copied/baseline/regenerated/time/` 和 `copied/baseline/evidence/TIME_MAPPING_CONFLICTS.csv`。546 处冲突（观察窗 96 处）没有被取最早/最晚、平移或覆盖。actual/confirm UTI、bar closeTs、calendar alternate 和 native event_ts 分开解释。

## 观测与可知边界

原生批次确实完成，数值行数不能代替首次可知证据：本单重算的是 524 条事件记录，另保留 620 条待比对基线行（其中有重叠）。`RECOMPUTED_OBJECT_ROWS.csv` 中 `event_ts` 是原生输出索引；`x/xConfirm` 是原生坐标。它们不是本单已观察到的 first-seen。

实际公开原生 class 只有 `__repr__ / run / runRealTime / stopRealTime / pushTick / pushTicks / packEventName / uniqueId`。scope 探针没有发现状态订阅、每次 fire 的状态快照或同步输入 frontier 回读。所选 `FrpHistoryModel.run` 在 history 完成后提供文件结果。当前源码参考也将保存回调登记到 `getHistoryEndEvent`，但它不作为冻结二进制的编译来源证明；承重实测是原生 class 输出、批次日志、strace 和实际文件结果。

因此本单**没有生成合法的 primary replay_event_seq/ts、max_input_bar_ts、input_prefix_hash、first_seen_at、last_seen_at、state_change_at、withdrawn/reappeared**。六行 VISIBILITY_LEDGER 是明确标记的批次覆盖状态，不是六次增量事件；OBJECT_LIFECYCLE_LEDGER 为只有 schema 的零观察文件。零观察不等于市场无对象、无方向、无状态或真实 no-signal。

第9.2节的独立 prefix 重算可以检验数值；它不能单独充当第7节同一主增量执行中内部首次输出/撤回/重现的观测。若把一系列 batch 查询的完成边界定义成新的 known time，必须明确采用这种查询式合同，而不能由 Worker 静默替换本工单要求的主增量观察关系。

**最终时间资格：BLOCKED_NO_LOOKAHEAD_PROOF。** 这不是对算法是否因果的否定，也不是对临时目录是否可修复的否定。
