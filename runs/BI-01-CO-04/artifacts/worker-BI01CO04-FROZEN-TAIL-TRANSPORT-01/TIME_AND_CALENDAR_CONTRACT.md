# 本单行情时间与日历合同

- 业务字段沿用同一 PNV `closeTs`；源为 datetime64[ns] 无时区标签。按已冻结 replay 合同将其标签解释为 `Asia/Shanghai`，CSV 的 `business_timestamp` 显式加 `+08:00`。这是同一解释，不把原无时区标签先当 UTC 再平移。
- `closeTs` 原文本、`closeTs_raw_ns`、`closeUti`、`openTs`、`openTs_raw_ns`、`openUti` 均保留；源 staging `__ts__` 与 closeTs 全8964行相同。source_row 是原源零基序号，source_key 指向同一 PNV 序列和该序号。
- cutoff 为 `2021-09-30T15:00:00+08:00`。anchor 为原行2159；evaluation 为原行2160–2227，共68行，末条 exact `2021-10-15T15:00:00+08:00`。三CSV各69行；没有 T 之前行情行或 end 后行情行进入三份CSV和range payload。
- tail 第一条为 `2021-10-08T09:30:00+08:00`。这只是实际源集合的首条；没有按工作日假设填点或插值。三品种完整timestamp集合相等，68条evaluation共同timestamp与差异空集已逐值列入TAIL_MANIFEST。
- 冻结 source 配置的 session 边界为21:00至次日20:00。源 PNV目录只暴露close/closeTs/closeUti/high/low/open/openInt/openTs/openUti/volume十个字段，没有逐行 trading_day、session、night-session attribution、contract_id、continuous_series_id 或 adjustment_id。CSV相应六列保持空白；这不表示不存在连续化/复权，而表示该源未声明这些标签。
- `source_snapshot=GTQH_L1_20210104_20240208`、同一路径和完整8964行逻辑payload与已核staging逐字节相同，绑定了本单使用的序列口径。不猜合约切换，不增加“未复权”等标签，不从另一来源补列。
- prior/replay 的 calendar natural_tsa 与bar closeTs冲突限制仍保留在输入TIME_CONTRACT；本单不调用该替代日历，也不以其覆盖业务timestamp或UTI。当前纯close-path合同按同一closeTs集合计算，未要求建立旧native事件可知性或逐行交易日新映射。
- 源物理文件预分配49,461,184字节，头部声明8964条有效行情；物理容量剩余字节不是有效行情行。按头部逻辑长度解析；首末覆盖沿用并实际核对为2021-01-04 09:30至2024-02-08 15:00。

本单日历对齐只证明同源业务时钟、UTI、索引和冻结前缀口径一致；没有新增正式交易日或native实时发布语义。
