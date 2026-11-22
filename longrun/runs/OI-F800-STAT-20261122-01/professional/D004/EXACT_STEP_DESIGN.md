# F800-MP-001 精确离散步长合同

依据 C0010/D004、原提案及 Owner「批准 F800-MP-001，实施修复并完整复验」。本 D 为 FI 实施回交；完整正式 X/G 属原 manager 的后继。

正常 KLine 的 closeUti 沿用现有 NativeSource 的 exactUTI：有限、无小数、在 Int64 内，不做舍入。连续边的期望原始步长以 `freq_ns / 60000000000 × units_per_open_minute / units_per_calendar_tick` 的精确有理数计算，仅接受正整数且不超 Int64。两项单位换算均须有限且为正。Double 单位值按其实际二进制值精确解释，未经声明的小数容差不构成合同。除以 Clock 缩放保证比较发生在源 UTI 上，例如 5m × 60 / 0.5 与 5m × 240 / 2 均为源 600UTI。

支持固定 SecondFreq、MinuteFreq，频率间隔与 ns 均须为正。Tick 不具有此固定 Calendar 开放分钟换算；日、周、月频率的名义 ns 不能直接代表 Calendar 开放时长，因此此适配器明确拒绝。分数单位仅在上述精确换算得整数时支持，例如 2m × 0.5 / 1 = 1 UTI；1m × 1.5 / 1 = 1.5 UTI 明确拒绝。当前批准输入 5m × 120 / 1 = 600 UTI，全部满足。

局部 previous 状态改存 `(Int64源UTI, Double覆盖Clock)`；用提升为 Integer 的源 UTI 差与已验证步长比较，避免 Int64 溢出。首次输入或非相邻输入只给当前点；正常相邻输入给上一 Clock 到当前 Clock 的窄边。严格 Material 累积规则保持。

`groupKLineEvents` 的四元组接口、Q 的归一化报价位置含义保持。F 与 Q 的共享 `buildKLineGroupSource` 都得到修正的覆盖边；Q 正式生产未授权给本 D，后续释放应按依赖规则处理。V 不直接导入该适配器。对象、Turn/Occurrence、候选状态/事件、结果字段、序列化配置合同均无结构变动，因此建议 FI 后直接 X，无需重做完整 U。

回归使用实际生产 helper 及原 Material/Evolution 入口：2^17 归一化边界旧比较失败而新边保持覆盖；真实 1200UTI 缺口、首次冷启动、SourceFailure 后恢复、未知 Clock 与更正均不得被假覆盖；保留原 800、revision、handoff、2Δ、期限等回归。局部结果不代表完整三年已复验或 finding 已关闭。
