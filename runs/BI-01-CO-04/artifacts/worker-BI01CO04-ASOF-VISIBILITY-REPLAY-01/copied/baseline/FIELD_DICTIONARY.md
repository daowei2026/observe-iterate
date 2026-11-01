# 字段与时间语义：已核事实及未决合同

本词典说明原字节和只读整理字段，**不证明 as-of 资格成立**。主要实物入口为 `copied/formal_slices/`、`regenerated/market/`、`regenerated/objects/` 和 `regenerated/time/`。原运行身份见 `DATA_MANIFEST.json`。

| 字段 | 已核来源及含义 | 消费边界 |
|---|---|---|
| symbol | 原 run 的 member_symbols、逐品种文件和原 CSV symbol，固定 rb/hc/i | 不凭板块别名猜成员 |
| scale | 原 E 参数与原 CSV 绑定：big=ScaleTurnCalendar/large、specTerm=L；mid=mid、specTerm=M | 与 aidata 节点 big_000001 及 K 线频率 30m 分开 |
| open/high/low/close | 原 run 实际消费的 staging KLine 30m 数值；正式窗口导出与缓存逐值相符 | 未标准化；PNG 纵轴 ratio 不能当原始价格 |
| volume/openInt | 原 KLine 提供的成交量／持仓量，按原值保留 | 不补零，不插值 |
| openUti/closeUti | 原 KLine 的 int64 业务时间轴坐标 | 不是 Unix 秒或毫秒，不得自行换算 UTC |
| openTs/closeTs | 原 KLine 既有自然时间字段；openTs 含 .500 秒偏移 | 保留原值；closeTs 与 natural_tsa 的同 UTI 映射并非全同 |
| source_index_ts | 原 run staging KLine `__ts__.dba` 中的原生索引 | 单独保留，不把它自动解释成发布或可知时间 |
| event_ts | 原 E `value1.__ts__.dba`／`value2.__ts__.dba` 经原 Int/Double ADT reader 取得的事件输出索引 | 由 CSV 适配器用作 index；未取得与 publish/known 的权威等价合同，不能直接宣称可知时间 |
| x/y | 原 E CompleteScaleTurn2D.actual2D，实际转折位置／价格 | 每个交付整理对象的 UTI 和价格均可精确追到实际消费 KLine；不能当确认时点 |
| xConfirm/yConfirm | 原 E CompleteScaleTurn2D.confirm2D，确认位置／价格 | 确认位置存在，但位置映射时间、event_ts 与实际信息可知边界之间仍有缺口 |
| x_ts/xConfirm_ts/_csv_x_ts | 原 aidata 在正式切片中从 natural_tsa 映射得到的自然时间 | 原字节不改写；不能忽略与 bar closeTs 的实值冲突 |
| x_bar_close_time/xConfirm_bar_close_time | 本包通过 x 或 xConfirm 精确连接已消费 KLine.closeUti 得到的 closeTs | 只是原数据连接结果，不宣布它取代正式确认时间 |
| x_calendar_time/xConfirm_calendar_time | 本包只读 natural_tsa[x]／[xConfirm] 的映射 | 与上列并列，未把冲突消掉 |
| turn_round | value1 或 value2；源 STCalendar.py 的两轮筛选结果 | 不是 revision=1/2；不可按轮次去重，重复事件保留 |
| source_feature_ppid | 原 ScaleTurnCalendar 参数身份；与 selected JSON、prepared job、validated receipt 三方相符 | ReadOnlyCsvFeature 还有自己的 ppid，不把两者混为一物 |
| source_engine_sha256 | 原 E 执行器的原有 receipt 哈希 | 证明所记录执行器字节身份，不代表所有 Python／共享库／E 源码都被冻结 |
| source_native_parameter_path | 原 E 参数身份对应的存储路径 | 不当作对象 id |
| _csv_source_row | 原 ReadOnlyCsvFeature 的 CSV 物理行号：首条数据为第 2 行 | 与零基 dataframe index 的换算为 row-2；已按源码核实 |
| source_row（整理对象） | 沿用原合并 CSV 的物理行号，首条数据为 2 | source_key=原合并 CSV SHA256 + csv_line；不声称是生产 object id |
| source_row（行情／时间映射） | staging KLine 的零基原生行序号 | 对应源 __ts__，与对象 CSV 物理行号体系不同 |
| source_key | 行情为原缓存目录+__ts__+行序号；对象为冻结 CSV hash+物理行号 | 可追溯 occurrence，不推导生命周期 |
| object_id / revision / segment_id | 原数据没有这些字段，本包空值并附 status 原因 | 不制造对象连续身份、线段关系、revision 或撤回事件 |
| current_status | PRESENT_IN_FROZEN_EXPORT_ASOF_NOT_VALIDATED | 只表示本次冻结产物中存在，不表示任何历史 T 时有效 |
| direction | 原 ScaleTurnCalendar 只有 actual2D/confirm2D，无方向；本包留空 | 不能用前后价格、yConfirm-y 或图形颜色补造 |
| direction_status | NOT_PROVIDED_UNVERIFIED_UPSTREAM_LINK | Wave.py 表明 RctZigWithStatus.pivot1 为带方向的最近 zig 价格，但尚无本配置上游缓存及逐对象映射的完整证明 |

## 日历、时区、session 与交易日

- 原 brief 使用 `calendar_override=@`，背景轴 rb；源 metadata 的 @ 明确链接到 F 盘 calendar/rb。三品种自身 open/close UTI 与时间列在本包范围内逐行相同，见 `evidence/VALIDATION.json`。
- 原 E source config 的会话边界为 `opt_start_hour=21:00:00`、`opt_end_hour=20:00:00`；这是实际配置证据，不能仅据此补造逐行夜盘交易日。当前保存的源时间为无时区 datetime，没有逐行 exchange、timezone、trading_day 字段。所在市场常识不能代替本 run 的正式时间合同；本包不擅自标 UTC 或 Asia/Shanghai。
- `regenerated/time/*_bar_calendar_mapping.csv` 同时保留 openTs、closeTs、source_index_ts、UTI 与 calendar 映射；具体冲突见 `evidence/TIME_MAPPING_CONFLICTS.csv`。例如 rb closeUti=6161399：closeTs=2021-08-16 10:30:00，而 natural_tsa=2021-08-16 10:15:00。这两项均来自真实源，不能只保留其中一个后宣布修复。
- 原正式窗口是 2021-08-15 00:00 至 2021-09-30 00:00；三份正式行情各 368 行，实际 closeTs 至 2021-09-29 23:00。整理行情按 closeTs < 2021-10-01 导出，补齐 9 月 30 日，同时从原运行实际源起点保留必要 warm-up；不声称它自动修复已知时间。
- `regenerated/objects/` 只截取 event_ts < 2021-10-01 的既有大／中事件，不含未来事件。原全历史运行之后的事件／修订是否会影响先前有效状态，没有完整合同证明；此过滤不是 as-of 重建算法。
- 原正式 i/mid 切片有一条 event_ts=2021-10-08 09:30:00 的事件，虽然实际位置进入原观察窗。它在 copied/ 原样保留，在 regenerated/ 事件前缀中排除；消费者不能将其当作 9 月底已知证据。此项是技术时间边界检查，没有选择任何业务 T。

## 缺失、故障、未运行与无信号

| 状态 | 本包判据 | 不能推出 |
|---|---|---|
| 文件存在且有行 | copy hash、行数和原 stats 一致 | 不表示数据满足业务资格 |
| 计算成功 | 六组 E state returncode=0，validated CSV hash 正确；原 board stats 成功 | 不表示无未来信息或方法有效 |
| 缺字段 | 源 schema 没有 direction/revision/object id 等 | 不表示市场无方向或真实无信号 |
| 缺数据／缺覆盖 | manifest、stats、源文件及实际首末行核验后列明 | 不把窗口外静默当空信号 |
| 计算失败 | 非零返回、错误日志、slice_success=false 或 hash 不符才记失败 | 本包成功复制不掩盖历史失败；当前选定六组未出现此证据 |
| 未运行 | 没有相应执行/结果证据 | 不写作 no-signal；本单未补小尺度，也未重算任一尺度 |
| 真实无信号 | 需完整成功执行、合法窗口与正式空结果合同 | 不能由方向空值、无某字段或过滤后无行推定 |
| as-of 状态未知 | 方向关联、发布时间或修订合同不足 | 不等于市场 NO_CANDIDATE |

撤回、更新、revision、line/segment 关系在已取得的 CompleteScaleTurn2D schema 中均未正式提供。没有将 value2 解释成对 value1 的撤回或替代，也没有用最终结果倒填 T。
