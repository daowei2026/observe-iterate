# 首项V3快照与完整技术交付的版本对应

图 http://192.168.11.40:6244/graph/cae/5781/report，run=BI01V2_R0004_fixed_20261018_033648，node=MAIN_ASOF_1；窗口 2021-04-26 09:30:00 至 2021-05-18 15:00:00，As-Of 2021-05-06 10:00:00。

当前不可变包：`current_versions/MAIN_ASOF_1__8dd8824509375c57.zip`；**146 CSV，198655 bytes**；SHA-256：`8dd8824509375c57a1f47756d30403bc0fca92a0d6ab38c1ce839b174467f86c`。代码：`e59fd90de5237b8a6756de00e54bdf841832fad4`，独立分支codex/bi01v2-r0004-fixed-input，main未改。参数SHA：`9132841395767bffc5e03fcd55be990aaa632347360868a81eb8cc204843b39a`。

实际本地consumer及真实Bokeh会话的原行/原值/窗口/AsOf/报价轴/未来隔离均核查；并新增逐个实际绘图坐标与原字段/显式连接的独立比对。small Zig status/confirmed的浮点字面UTI已按显式整数键接入，主Case原来为空的绘图时间坐标已实核可用，不插值、不填0、不改原字段。

历史：b7c8780f的144CSV包SHA26bc0ef801e4c7da673b9fdc4805f06c632c173007c583a030b0ed8a01f38e61不含N Working新增层；中间146CSV包SHAce68bae86a128a046aa9e33b7b1cb87954792f0ade5fad3c8ea160c36ac660f5仍缺small Zig的显示连接。这些原件保留，不能与当前图混配冒称完整坐标覆盖。详见PUBLICATION_AND_VERSION_BOUNDARY.json、INTEGER_LOOKUP_DISPLAY_CORRECTION.json。

本文件记录首项V3快照及其版本边界；全工单当前技术终态、320图数/51真实请求会话及全部业务待决见WORKER_RETURN.md和当前索引。Worker未签专业S3、管理Gate或全BI01完成。
