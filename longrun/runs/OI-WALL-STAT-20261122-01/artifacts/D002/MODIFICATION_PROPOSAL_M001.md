# M001｜待 Owner 确认 m 的正式输入处理

需要确认的具体动作是：是否批准下述严格空日历占位过滤，随后更新正式代码锁，并按原 rb/m、2021 全年范围完整重跑与重统计。生产本身已经获授权；本请求针对实际触及的输入处理改变。

## 当前阻断与实证

本 Run 真实调用锁定的 `WallAssembler()` 默认实例后，m 失败：

```text
ValueError: 交易日区间在 2021-03-12 00:00:00 前不连续: 1792800 != 1792801
```

失败来自 TIS `6618d4d147d6ebbe634e61facddf2c9a0b996982` 的原生分块保护；完整记录见 [M_FORMAL_FAILURE.json](M_FORMAL_FAILURE.json)。本次没有采用原工作树已有的输入过滤，也没有生成合格 m 结果。

对 2021-03-10 至 2021-03-12 三个自然日作 `DIAGNOSTIC_ONLY` 读取，实际覆盖 `2021-03-10 09:00:00.500000` 至 `2021-03-12 23:00:00`：

| 项目 | 当前证据 |
|---|---|
| 原始诊断窗 | 124,200 行 |
| 全空且未被交易日区间覆盖的行 | 1 行；`2021-03-11 21:00:00.500` |
| 全空字段 | `price / buy_price1 / buy_vol1 / sell_price1 / sell_vol1`；`linear_ts` 仍有值 |
| 原锁定分块检查 | 同位置失败，窗内行位置 `68400 != 68401` |
| 候选处理的隔离反事实 | 排除 1 行后剩余 124,199 行，分块检查通过（4 个交易日 chunk） |
| 数据保持 | 所有保留字段逐值一致；原 frame 的值哈希前后相同，原始 Sof 未改写 |

数据与完整诊断范围见 [M_INPUT_DIAGNOSTIC.json](M_INPUT_DIAGNOSTIC.json) 和 [缺口行](m-uncovered-rows.csv)。这不是本轮全年 17 行已重验的结论；“17 行”仍只是历史线索。

## 可审阅候选及影响

候选只涉及 `hf/prel0/wall_assembler.py`：在输入包装层排除分时段首个半秒、五个报价字段全空、下一半秒报价完整的日历占位；继续拒绝有效行情或其他未覆盖缺口。它拟排除所有符合严格谓词的空占位，不仅是触发第一个异常的行。core、默认参数、期限、D1/D2/D4 及四类事件合同保持原定义。

该差异原本已在旧工作树中，本 Run 保留原状。以下副本仅供审阅，尚未应用到本 Run 的锁定正式检出、提交或登记为正式版本：

`/dwdhome/fy/BASE_E6_2/.runtime/OI-WALL-STAT-20261122-01/proposals/M001/candidate-wall-input-filter.diff`

SHA-256：`6d5fa9068a75922406233e884721a76130255a0594136460d0e5242726b98b1b`。

输入处理会改变 wrapper 指纹及 trace 的采样行集合。应记录排除时间和 source scope；跨特征按 timestamp/UTI 对齐。Owner 确认并采用后，需要更新正式版本锁，使用本 Run 新 attempt 目录完整运行 rb/m 并重新 G；当前 rb 的 `6618d4d…` 结果保留为对照。

验证方案包括全年两品种的空占位清单、有效报价和 `linear_ts` 逐值保持、异常缺口仍被拒绝、完整参数回读、既有回归、正式结果哈希及独立 Dao 逐表逐行读回。完整字段见 [MODIFICATION_PROPOSAL_M001.json](MODIFICATION_PROPOSAL_M001.json)。

另一选择是保留锁定实现及 m 阻断，由 Owner 指定已认可的规范输入处理／版本。本次没有缩短正式范围或静默换用其他处理。

## 为什么需要确认

[D002 原执行授权](https://github.com/daowei2026/observe-iterate/blob/8fafd07ff658f519ca000c81fede1ac343f36603/longrun/runs/OI-WALL-STAT-20261122-01/delegations/D002/EXECUTION_AUTHORIZATION.md) 明确：**“既有 wrapper 输入处理差异不因本 D 签发而获准采用”**。原 Owner GO 也要求正式数据处理改变先形成 ModificationProposal、取得 Owner 确认后才实施、提交和采用。因此本提案保持待确认；隔离诊断通过不等于正式采用授权。
