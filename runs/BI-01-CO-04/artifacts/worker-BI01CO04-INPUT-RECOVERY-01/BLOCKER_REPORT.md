# BI01CO04-INPUT-RECOVERY-01 准确阻断报告

结论：**已恢复真实字节，P0 部分完成，仍阻断 as-of 消费**。输入未被否定为不存在；不输出市场判断，不选择 T。

## 1. 已查位置与已有实物

已定向读取原工单和六必读、原 `build_three_turn_plot.py`、selected 参数、原 run 的 brief/manifest/stats/timespan、六组大中 E task/state/engine log/validated receipt、原 Int/Double reader 及 schema、实际消费的 staging KLine、日历 natural_tsa 相关坐标、ScaleTurnCalendar/Wave/CSV 适配源码。源路径均逐文件列于 PACKAGE_RECEIPT；未递归查旧业务 runs、聊天历史或全市场。

已恢复：同一 run 的三份正式 30m 行情、六份大中正式对象切片；参数消费链、静态 PNG 及 run/node 对应证据；必要 warm-up 到完整 9 月 30 日的只读行情导出；大中已有事件的前缀导出；逐行时间映射与冲突实物。准确数量见 DATA_MANIFEST、OBJECT_COVERAGE 和 VALIDATION。

## 2. 阻断项与最小恢复条件

| ID | 已证实事实／具体缺件 | 受阻 P0 | 最小恢复条件 |
|---|---|---|---|
| B01 | natural_tsa[closeUti] 与同一正式 KLine.closeTs 存在实值冲突；event index 也单独存在。三品种轴一致不能消除此冲突。 | 5.3、5.4、5.5 | 由本输入生产者提供冻结版本的 UTI、bar closeTs、事件索引与 publish/known 的精确合同及修复/兼容映射；明确时区、交易所 session、夜盘交易日和端点。保留原字节，不改成猜测时间。 |
| B02 | CompleteScaleTurn2D 只有 actual2D/confirm2D；正式切片与源 validated CSV 没有方向。发现 RctZigWithStatus 上游缓存和 Wave.py 的 pivot 字段，但未取得其与本次 0.5% 配置的可靠绑定和逐对象 direction 对应证明。 | 5.4、5.5 | 交本 run exact falter/fcheck 上游参数身份与缓存索引，按 symbol+实际UTI+价格+上游事件时间给可靠方向映射；额外贴近点不能可靠映射时保留 UNKNOWN，并给该类对象的正式语义。无需重算全市场。 |
| B03 | 没有生产 object id、revision、撤回/更新/current/segment 字段及完整生命周期合同；value1/value2 是两轮筛选，不是已证实的版本号。 | 5.4、5.5 | 生产者提供原对象生命周期/不可变事件合同，或准确的 id/version/撤回事件；证明 event_ts 之前不可知、之后何时有效以及如何防最终修订倒填。不能由 Worker 自行定义业务状态。 |
| B04 | 有原 aidata commit、E 版本和二进制 SHA、当时部分源码 hash/checkout 审计，但没有该二进制完整编译源码/依赖构建绑定与冻结日历版本。 | 5.1；阻止缺件重算 | 只有需要数值重生时，补足 exact build/config/source/calendar/command 和消费关系；否则使用已有字节并补 B01—B03 权威合同。单独重跑同一二进制不能解决时间合同。 |

原正式 run 窗口不含 9 月 30 日全天。本包已从原实际消费缓存只读导出到 9 月 30 日最后已存 bar；这解决字节覆盖不足，但不解除 B01。原 E 按完整源历史计算；本单没有重算，也没有复制 2024 全历史。所需 warm-up 从 2021-01-04 起点保留。

另有直接的未来信息边界证据：原正式 i/mid 按实际 x 切出的对象中，1 条 event_ts 为 2021-10-08 09:30:00。copied 切片原样保留；截至 9 月 30 日的整理事件排除此条。它证明“正式切片存在”不能代替按已知时间消费，但 Worker 不自行裁定应如何改业务 T。

## 3. exact gate 与本单停止边界

exact 条件未全部成立，未执行数值重生、参数寻优、算法修改、全市场/全历史复制。`regenerated/` 是既有真实缓存和 CSV 的只读导出，并非新数值结果。

上述缺件不能靠增加计算量或读取更多旧聊天恢复。本单交付准确 blocker 及已取得实物，符合工单第七节；P0 状态不得写成全满足，不能直接通知 Professional 开始 as-of 判断。原签发 Management 接收技术包后决定专业消费及后续最小补件。

## 4. 全部重要未完

1. B01—B04 所列合同／身份缺件及独立消费者复核。
2. Management 尚未技术接收；原 Professional 尚未确认输入资格或继续业务研究。
3. 首个合法 T、品种比较、候选／排序／无候选、自然挑战、方法反馈和管理 Gate 均未由本 Worker 执行。
4. 未刷新线上 node 6153 或新建平台节点；P1 为原已有静态 PNG 的真实复制与目视核对，随包交历史对应证明。

本有限工单可在技术报告、receipt、数据与准确 blocker 提交推送并回交后结项；这不表示上述业务未完或主控 Goal 已完成。
