# 既有业务参考与历史实物入口

本文件是定向导航，不是每轮必读清单；参考材料中的示例不等于本轮真实市场结论。当前工具和 aidata 操作知识已直接整理在 [03_TOOLING_AND_DATA_USAGE.md](03_TOOLING_AND_DATA_USAGE.md)，本分支不依赖旧版专业目录作为执行说明。具体调用前仍须核对现场 aidata README/API 与本次正式交付。

## 业务表达参考

- [U3人读叙事V0.3.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b4b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md)：业务语言、叙事层次、推进/摩擦/保持及关系语义。
- [U3用例卡V0.4.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md)：按需参考细化情境与边界。
- [U2人读叙事V0.3.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md)及[U2用例卡V0.4.0](https://github.com/daowei2026/complex-systems-vocabulary/blob/48f55f53e25d04e5b59fae1e652dd4b679c9d3/docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md)：按需理解多品种转折、过程和关系。

## 历史业务研究的定向参考

旧的 CO-01 业务用例、研究依据和观察材料保留在原分支。只有当前具体业务问题确实需要复核某个历史判断、事实或Owner反馈时，才定向查阅对应Case和证据；不把旧四例当作本轮必须修订、必须复用的用例，也不继承其原有选例方法、批次要求、图页要求或运行状态。

历史业务结果可帮助理解此前讨论过哪些市场现象，但不能代替本轮实际特征交付、不能自动证明当前候选场景成立，也不能把历史Case中的参数和图形配置变成本轮默认值。

本轮工具操作、aidata接口关系、数据交付消费及首次画图注意事项，以本分支 [03_TOOLING_AND_DATA_USAGE.md](03_TOOLING_AND_DATA_USAGE.md) 为直接工作说明。旧运行中的测试结果只作为其当时事实，不要求执行者为了取得这些操作知识而回到旧分支重新阅读整套专业目录。

## 使用边界

参考材料用于理解业务表达或复核具体历史事实，不是本轮已验证规律、市场答案或正式特征链前置。需要新特征或新属性时，先说明当前既有特征是否已经提供、缺少什么业务信息及其用途；不因阅读参考材料就自动启动特征开发或实现任务。

## 已完成的绘图工具实践

- [2026-11-01 当前30m多品种三尺度转折图](tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md)：一次实际走通的 uplot、CAEGraph/PlotSet 与 aidata 组合实践，含图页、参数和工作区入口。仅作为特定实践参考，不代表后续任务必须使用相同的品种、窗口、30m频率或small/mid/big参数。
