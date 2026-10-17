# 当前首图及同图数据版本

[打开 aidata 图](http://192.168.11.40:6244/graph/cae/5781/report)：节点 MAIN_ASOF_1，run BI01V2_R0004_fixed_20261018_033648。AsOf 为 2021-05-06 10:00，窗口为 2021-04-26 09:30 至 2021-05-18 15:00；需能访问部署工作站网络。

当前已发布数据是 [修正146 CSV原包](current_versions/MAIN_ASOF_1__8dd8824509375c57.zip)，SHA-256为 `8dd8824509375c57a1f47756d30403bc0fca92a0d6ab38c1ce839b174467f86c`。元数据、图指纹、代码树hash及验证时间见 [CURRENT_MAIN_ASOF_1_VERSION.json](CURRENT_MAIN_ASOF_1_VERSION.json)。Worker版本为 integer_lookup_and_full_coordinate_validation_v3，代码e59fd90de5237b8a6756de00e54bdf841832fad4，首图每一实际绘图坐标已对照原字段或声明连接核验。root只核原字节、hash、ZIP及文件数量，没有代签专业看图认识。

可直接读取同一包的 [VIEW](readable_views/MAIN_ASOF_1__8dd8824509375c57/VIEW.json)、[SOURCE_BINDING](readable_views/MAIN_ASOF_1__8dd8824509375c57/SOURCE_BINDING.json)、[CSV与导出manifest](readable_views/MAIN_ASOF_1__8dd8824509375c57/plot_view_data/)；原样解压的149成员hash与字节数见该目录EXTRACTION_RECEIPT.json。ZIP仍保留，无内容变换。

## 修复与历史快照

新增的 N_WORKING_ORIGIN 层在 known/retrospective 两scope保留原方向来源。随后发现small Zig原UTI文本75045599.0与KLine整数键75045599连接失败，旧检查遗漏了status/confirmed的实际时间坐标。当前版以Decimal精确连接整数键，保留原字段；非整数不取整，缺失不插值、不填零，固定输入/数值/窗口/AsOf不重算。

以下包原样保留为有上述连接缺口的历史技术快照，不能用于证明当前修正页面的完整显示：

- [首次144 CSV包](chart_data_packets/MAIN_ASOF_1.zip)，hash 26bc0ef801e4c7da673b9fdc4805f06c632c173007c583a030b0ed8a01f38e61，首次发布b7c8780；FIRST_DELIVERY.md为当时原始回交。
- [新增原方向层的146 CSV中间包](current_versions/MAIN_ASOF_1__ce68bae86a128a04.zip)，hash ce68bae86a128a046aa9e33b7b1cb87954792f0ade5fad3c8ea160c36ac660f5，发布91b0083。

## 未完与后继

本页是当前首图分批技术交付。Worker报告43项回归通过、原main仍9ff7ce4；全320视图和51请求真实会话正在以validation revision2重新核验，旧通过计数不沿用。图URL在施工期间可能继续接入修正，消费时须核当时当前版本索引与同图包。全工单最终技术回交、执行Pro的图数消费和S3业务认识仍待实际完成，完整U2/U3目标继续。
