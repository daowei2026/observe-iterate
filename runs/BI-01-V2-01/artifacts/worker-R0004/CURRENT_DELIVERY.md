# 当前首图及同图数据版本

当前节点 MAIN_ASOF_1：[打开 aidata 图](http://192.168.11.40:6244/graph/cae/5781/report)。AsOf 为 2021-05-06 10:00，窗口为 2021-04-26 09:30 至 2021-05-18 15:00，需能访问部署工作站网络。

当前同图数据为 [146 CSV 原包](current_versions/MAIN_ASOF_1__ce68bae86a128a04.zip)，完整 hash、view spec 和 Worker 验证时间见 [CURRENT_MAIN_ASOF_1_VERSION.json](CURRENT_MAIN_ASOF_1_VERSION.json)。新增层为 N_WORKING_ORIGIN 在 known/retrospective 两个 scope 的原方向来源；固定原值、窗口及 AsOf 未改或重算。

首次 b7c8780 发布的 [144 CSV 包](chart_data_packets/MAIN_ASOF_1.zip) 与 FIRST_DELIVERY.md 保留为历史快照，不覆盖新增层。当前技术验证和后续专业看图认识仍分别验收；整个 S1—S3 工作继续。

## 在途发现：时间坐标连接缺口

2026-10-17 20:00Z 从同一实际 Worker turn 得到新事实：small Zig 的 UTI 在原 CSV 写作 `75045599.0`、KLine 键写作 `75045599`，此前 status/confirmed 图层时间坐标没有接上；原行已经导出。Worker 正在同一工单内补显式整数键转换、坐标值核验并重新验证。固定源数据不改。

此前技术检查未覆盖该连接缺口，不能将旧包视为完整显示验证通过。以上 144 和 146 CSV 包、hash、验证时间均作为已发布快照保留；此 URL 的在途图形会随修复变化，后续正式回交须给出修复后的当前图数版本及受影响核验，不能仅凭旧包证明当前页面一致。
