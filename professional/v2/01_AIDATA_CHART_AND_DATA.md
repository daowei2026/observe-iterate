# V2 S2：统一使用 aidata 画图与取得对应数据

## 1. 权威工具及其边界

图、图层数据、图所在的市场窗口和用于 AI 分析的特征数据，**统一由 `daowei2026/aidata` 形成**。不在 `observe-iterate` 创建第二套制图库、CSV 切片器、Bokeh 页面实现或独立视觉工作台。

每次准备使用前，实际读取当前锁定的 aidata `README.md`、`OWNER_INTENT_AND_RATIONALE.md` 和 `TODO.md`；接口按当前 `docs/DEVELOPMENT_GUIDE.md`、`docs/RUN_BRIEF_INPUT_CONTRACT.md` 及真实源码核对。TODO 的历史候选不自动等于当前必须实现，也不自动证明当前仍缺功能。

主要已知入口（以运行时事实为准）：
- `build_chart_run(run_brief_input)` 建冻结节点窗口和图 core；
- `build_big_world_chart_pages(run)` 提供图页面链接；
- `build_board_run({...}, reuse_core=True)` 在相同冻结 core 上补主证据与 delivery；
- `build_chart_review_requests` / `render_review_nodes` 用于 Pro 具名节点深查；
- `export_plot_view_data` 可导出与图上可见内容对应的展示视图。此数据**不是**主证据。

不要把 Bokeh URL、plot-view CSV、图片渲染、原始输入和可信业务特征结果互相等同。

## 2. 本次首先观察的业务内容

品种暂限 rb、i、hc。观察优先级来自 S1：
- 共同机会簇的位置、构成及形成时间；
- 组内/组外品种原始走势、实际转折及确认/可知时点；
- U3 四个方面在各共同机会位置上的结果与后续路径；
- 多种成员/时间/成熟度对照，用来发现错配、假好与额外价值。

专业 Pro 应先提出“为什么看这张图、希望比较什么、需要的合法窗口和哪些层”；再由有权 Worker 实际配置、渲染、核对，不让 Worker 自选业务结论。

## 3. 数据来源与当前特殊手段

1. 优先使用已有正式实现提供的真实 Feature，或有明确可消费范围的真实输出。
2. 如果只有冻结 CSV/ZIP，不得自动假设 `aidata` 支持任意 CSV 直入。先核对当前 Feature Provider / `rerun().to_df()` / `to_dfs()` 及 aidata 是否已有官方适配路径。
3. 如果这是一项 aidata 的**通用能力缺口**，由专业任务提出准确问题和最小验收，工程改动写在 aidata；不为本次在观察仓私建脚本链条。
4. 当前特征实现未齐、不得正式获取结果时，AI 可在明确算法、数据绑定和使用资格下进行有界参考验算，并明确 `diagnostic/reference`，不能把推算冒充正式 U2/U3。
5. 两个历史 ZIP 如被本次实际采用为数据原件，需重新验证文件身份、字段、交易日历和位置映射；**不采用**对应历史 Pro 的观察结论、Gate、任务回交。

## 4. 图与数据一致性

每份观察材料至少记录：
- aidata 仓库精确 commit、`run_id`、`node_id`、图链接和 render 状态；
- 业务数据身份、品种、日历、尺度和精确时间窗口；
- `chart_manifest` / `timespan_index` 对应窗口与来源；
- 主证据（`feature_slices`、`source_occurrences`、必要时 raw market sidecar）及 delivery 引用；
- 展示视图 `plot_view_data` 的身份，说明它只用于对齐可见内容；
- actual / confirm / known-as-of 与 working/completed 的图层语义；
- 图上额外上下文与真正可用于判断的数据范围。

手工 big 时间窗口 `big_source.mode=manual_timespans` 是现有候选入口；**仍需要合法的 mid/small anchor 和运行时 Feature**。禁止为了画图默认重选 BI-01 的已确定业务窗口。

## 5. AI 是否真的看过图

独立记录：
- `DATA_ONLY`：AI 实际读取主证据/图层数据，但未取得图像像素；
- `VISUAL_AND_DATA`：模型确实接收了具体已渲染图像并据此提出观察，随后对原始数据核验；
- `UNVERIFIED`：无法证明图像或数据真实到达模型。

不能用“导出了 plot_view_data”冒充视觉模型看过图。若运行环境暂时不能把图像提供给执行 Pro，记录限制、交付 Owner 图与 Pro 数据，不伪称视觉分析已完成。

## 6. 发现缺口怎样处理

运行时优先尝试现成入口、明确错误与缺项；先查 TODO 与 Owner 意图。可在有权授权下由 Worker 在 aidata 内做通用适配，并以真实数据、现有测试和可以打开的图验收。没有环境/数据时提交准确阻断和恢复条件，不以伪图凑完成。
