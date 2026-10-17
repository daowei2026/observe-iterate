# 03A output contract and encoding checks

## 0. 用途

这份文档收录 pre-L0 review checks 中，与正式输出合同、编码字段、事件表时间语义最相关的规则。


## 1. 规则目录

### PCHK-001 正式 wrapper 输出不得含 `object` dtype

- 风险：
  - repo-facing wrapper 一旦返回含 `object` dtype` 的 DataFrame，DAO 落库路径很容易直接失败
- 程序性检查建议：
  - 对 `_impl()` 返回的 DataFrame 禁止任何 `dtype == object`
  - 对 `*_chunk_end_state / *_sparse_events / *_chunk_summary / *_chunk_checkpoints` 做专项检查

### PCHK-002 标签字段必须编码，不得只编码一半

- 风险：
  - 看起来“已经做了编码”，但只编码了一部分标签字段，会让人误以为 DAO 风险已清掉
- 程序性检查建议：
  - 扫描正式输出列名
  - 若出现 `side/status/reason/end_reason/event_type/checkpoint_type/lane/boundary_type` 原始字符串列，则报警

### PCHK-002A `*_code` 不能是假编码；编码表必须覆盖真实业务枚举

- 风险：
  - 存在 `*_code` 列并不自动表示编码正确
- 程序性检查建议：
  - 对当前 packet 实际可能出现的标签值做覆盖性检查
  - 已知标签值不得被编码成 `0 / unknown`

### PCHK-005A `sparse_events` 的 index 不得误用 `chunk_end_ts`

- 风险：
  - 事件表若把 index 设成 chunk 结束时间，会保留 chunk 归属，但丢掉事件流最关键的时间语义
- 程序性检查建议：
  - `*_sparse_events` 默认使用事件发生时间 `ts`
  - `chunk_id / chunk_end_ts` 应保留为普通列，不应用来替代事件时间 index


## 2. 审查结论格式建议

- `PCHK-001 FAIL: wall_assembler_chunk_summary.active_wall_status is object`
- `PCHK-002 FAIL: build_assembler_sparse_events.event_type remains string`
- `PCHK-002A FAIL: event_type_code maps known Build events to 0`
- `PCHK-005A FAIL: sparse_events uses chunk_end_ts as index instead of event ts`
