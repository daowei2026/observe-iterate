# 原51请求As-Of的当前同图原件：可读运输副本

按R5已签运输授权、R6实际取用需要，直接展开原47请求对应的51个As-Of原包。源固定为1917f868d61f8de7110b7165ee9125e5b156c4d2中worker-R0004/final的原chart_data_packets；不重导出、不改数据、不重画、不更换包版本。原ZIP、完整320节点与历史交付全部保留。

每个节点路径为本目录下`<node_id>/`，成员路径与ZIP完全相同：`VIEW.json`、`SOURCE_BINDING.json`、`plot_view_data/plot_view_data_manifest.json`及`plot_view_data/*.csv`。具体成员以原包和EXTRACTION_RECEIPT.json为准；有合法空CSV也原样保留。51个node_id、原页面、As-Of和请求关联继续使用final/CURRENT_VIEW_VERSION_INDEX.csv与REQUEST_WINDOW_NODE_MAP.csv，不建立另一套业务索引。

主Case为MAIN_ASOF_1至MAIN_ASOF_5；其余为原选C1_ROW_XXXX及UNCOVERED_01至UNCOVERED_11。可直接按GitHub文本接口读取各CSV；例如`C1_ROW_0033/plot_view_data/fixed__C1_ROW_0033__known__C1.csv`。原列、原行、可见性、source定位、_aidata字段、原VIEW/SOURCE_BINDING均不变；需批量时目录本身可按原成员路径取得，不必手工重组base64 ZIP。

所有成员逐字节SHA-256和长度、所属node、原包SHA、原成员路径在EXTRACTION_RECEIPT.json。该回执仅证运输同一性，不证明专业者已经读到、业务判断正确或管理采用。44MB原范围索引未作切片或改写；逐节点VIEW/SOURCE_BINDING及原CSV本身随原包完整到达。专业者继续已签完整S1—S3，不以这51个As-Of数量为完成配额，具体额外节点仍从原320包取用。
