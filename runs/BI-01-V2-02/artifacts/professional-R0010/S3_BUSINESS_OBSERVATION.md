# BI-01-V2-02 R0010 S3 业务观察正文索引

invocation_id: `BI01-V2-02-R0010-20261018T175239Z-75847f6b`

完整 S3 正文因交付接口单文件载荷限制按原顺序拆分为四段；四段业务正文及其顺序在 R0011 有限补交中均未修改。

## R0011 交付元数据订正

历史提交 `b3284c7737b04ebb3ae5b58192d117fa459e33d3` 曾声称“原本地合并文件共 715 行、SHA256 为 `e00fa31976d68c8151b3594f2cd860ee6ed09c6dbf7684d6e2fd88d901758e59`”。当前可取得的 R0010 交付物中没有该原始本地合并字节流，因此本次不能复验该历史声称，也不以新拼接结果倒签为原合并原件。

对当前已交付四段按下列顺序做**原始字节直接拼接**，不插入分隔符、不规范化换行：

1. `S3_BUSINESS_OBSERVATION_PART_00.md`
2. `S3_BUSINESS_OBSERVATION_PART_01.md`
3. `S3_BUSINESS_OBSERVATION_PART_02.md`
4. `S3_BUSINESS_OBSERVATION_PART_03.md`

可复验结果为：

```text
bytes      = 28400
splitlines = 714
sha256     = fa67d5d09dc17098291e8ce545ebc0c19424c7f287a6ab3caec16f8f553c8498
```

该结果只标识“四个已交付分段的 raw concatenation”，不证明其与不可取得的历史本地合并原件相同。完整 part blob、字节数、拼接方法和复验命令见 [`S3_REASSEMBLY_CONTRACT.json`](./S3_REASSEMBLY_CONTRACT.json)。历史原声称仍可在旧提交追溯。

## 正文阅读顺序

1. [`S3_BUSINESS_OBSERVATION_PART_00.md`](./S3_BUSINESS_OBSERVATION_PART_00.md)：证据资格、S2 定位、SCN-01。
2. [`S3_BUSINESS_OBSERVATION_PART_01.md`](./S3_BUSINESS_OBSERVATION_PART_01.md)：SCN-01 结论、SCN-02、SCN-03、SCN-04 前半。
3. [`S3_BUSINESS_OBSERVATION_PART_02.md`](./S3_BUSINESS_OBSERVATION_PART_02.md)：SCN-04 结论、SCN-05、SCN-06、跨场景认识前半。
4. [`S3_BUSINESS_OBSERVATION_PART_03.md`](./S3_BUSINESS_OBSERVATION_PART_03.md)：U3 增量边界、四束范围、设计行动、事实分账、完成判定。

机器可核的事实表另见：

- [`COMMON_CUT_AND_BASELINE_FACTS.csv`](./COMMON_CUT_AND_BASELINE_FACTS.csv)
- [`SCN01_R02_N_ASOF_COMPARISON.csv`](./SCN01_R02_N_ASOF_COMPARISON.csv)
- [`SCENE_OUTCOME_PATH_FACTS.csv`](./SCENE_OUTCOME_PATH_FACTS.csv)
- [`S2_CHART_AND_DATA_INDEX.csv`](./S2_CHART_AND_DATA_INDEX.csv)

完整专业回交、原实质判断、触发、限制和接续见 [`FULL_RETURN.md`](./FULL_RETURN.md)。
