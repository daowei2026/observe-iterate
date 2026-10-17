# 现有能力与必要接入

基线 aidata main@9ff7ce4929b36945f63b1c9875e59f68141f997a，初始 tracked/untracked status clean。

已读工单全文、V2/01、V2/03、V2/05、aidata README、OWNER_INTENT_AND_RATIONALE、TODO 相关条目、Development Guide、Run Brief 合同及实际 API。

- feature_slicer.feature_df 仅调用 Feature.rerun().to_df/to_dfs；没有固定 ZIP/CSV 通用生产者。
- 现有 build_chart_run 人工窗口可冻结节点，但仍依赖 context／成员与默认价格 Feature。
- big_world_chart 的既有 KPriceLine 默认归一化轴不能直接满足本次原品种报价轴。
- export_plot_view_data 接受真实 ColumnDataSource；render_review_nodes 当前不会自动提取布局 CDS，不能把空导出当作同图数据。

在 aidata 独立分支 codex/bi01v2-r0004-fixed-input 修补必要公共生产者／消费者；固定包只读、业务层参数外置、不运行正式 Feature／U2／U3、不在 observe/cgpterm 增加绘图实现。
