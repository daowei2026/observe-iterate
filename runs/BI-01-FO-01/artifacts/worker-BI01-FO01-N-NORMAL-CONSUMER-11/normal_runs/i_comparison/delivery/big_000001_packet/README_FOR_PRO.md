# Aidata BigNodeCase 包 / big_000001

本目录是一个可单独投喂给 Pro 的普通文件包。它只覆盖当前 big node 及其 mid/small 子树，不代表全 run 连续叙事。

默认读取顺序：
1. `00_CONTRACT.yaml`
2. `01_NODE_SCOPE.csv`
3. `02_EVIDENCE_REFS.csv`
4. `06_FEATURE_CONFIGS_AND_FIELDS.yaml`
5. 需要主证据时读 `03_FEATURE_SLICES.csv` 和 `04_SOURCE_OCCURRENCES.csv`
6. 人同步看图读 `07_PLOT_REFS.csv`

边界：`03_FEATURE_SLICES.csv` 是内容主证据本体的包内合并表；`04_SOURCE_OCCURRENCES.csv` 是定位主证据本体的包内合并表。这些表只做 scope filter 与 concat，不做评分、分桶、排序结论或叙事提示。
K 线等 raw market data 会进入 `05_MARKET_SIDECAR.csv`，它是 sidecar：默认不要全读；只有当路径摘要不足、需要复查走势或核对 OHLCV 时，才按 node_id 定向读取。`slice_id` 对应的 run 内来源文件见 `06_FEATURE_CONFIGS_AND_FIELDS.yaml` 的 `slice_index`。

如果需要 join / stats / new window / full scan，请先输出 DataSideRequest，而不是自己写代码扫完整包。
