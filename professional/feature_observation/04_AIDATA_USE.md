# aidata 在新四项专业工作中的位置（初版）

## 首次使用：从 README 进入

**先读取所采用 aidata 版本的 [README.md](https://github.com/daowei2026/aidata/blob/main/README.md)**，理解定位、观察范围、图和对应数据的关系。长期概览和大—中—小尺度是按问题使用的工具，不是工作 2 的设计模板。实际配置时再按需阅读 [开发参考](https://github.com/daowei2026/aidata/blob/main/docs/DEVELOPMENT_GUIDE.md)、[run_brief 输入合同](https://github.com/daowei2026/aidata/blob/main/docs/RUN_BRIEF_INPUT_CONTRACT.md)、[真实数据测试说明](https://github.com/daowei2026/aidata/blob/main/tests/README.md)，记录准确版本。

可优先查阅已经提供实际运行方式的 [microstructure_review.py 示例](https://github.com/daowei2026/aidata/blob/main/examples/microstructure_review.py)，了解多个具体特征怎样实例化、配置 `run_brief`、创建看图页面；**只借调用方法，不默认借其板块、参数、时间尺度或特征含义**。本次 `U2NormalNodeBehaviorFrp` 仍须从自己的真实结果读回与方法合同判断能否接入。

## 1. 工具职责与专业职责分开

- 工作 2 根据特征业务语义和 uplot/CAEGraph 实际能力，决定值得画的信息、K 线叠加或独立附图等具体表达，以及时间/状态/图层/更新含义，形成实际展示配置文件。应读取实际采用 uplot 版本的 `CAEGraph使用手册.md`，不能从 aidata 默认图反向决定专业画法。
- 工作 3 消费工作 2 的文件，将其放入 `aidata/feature_configs` 对应位置，验证实际调用；借助 aidata 多层定位值得观察的位置、组织图和范围并提供图对应数据。重要业务画法仍由工作 2 决定，适配和调用不能代做这项选择。
- 设计不固定为单 As-Of 的 6+6+Working 截面，要考虑沿时间观察和选定时点回看。最终多品种呈现中颜色优先留给品种，其他性质优先使用线型、形状、位置或分图；不新增单/多品种选择任务，不预设实时刷新或逐拍重算。
- 工作 4 优先分析正式 N、对应行情及必要上游；数据足够时直接给有边界认识，需要几何或展示判断时才定向看图，实际未看像素就如实标明。
- aidata 的实际绘图接口不是自动代替专业人员完成特征展示设计，更不是自动证明特征具有投资业务价值。

## 2. 已有能力的确认范围

以下是准备稿与首例提供的接口核对入口，不代表新设计已全部适配；实际能力以锁定版本的 README、docs/DEVELOPMENT_GUIDE.md、docs/RUN_BRIEF_INPUT_CONTRACT.md、feature_configs/、evidence_plot.py 和真实调用为准：

- 正常使用时，通过 run_brief_input 指明时间、对象、定位及观察特征、观察尺度等配置；定位特征和观察特征可以不同。
- 独立特征展示配置在 aidata/feature_configs，当前已有 ZigConfirm、ScaleTurnCalendar、ThickFrp、BlkThickFrp 的专属配置；通用绘图支持 point/line/segment 和有限的样式、文字、hover。
- 已声明的展示配置可被读取，调用方也能显式给完整 plot_binding 覆盖；不是每次都要 AI 任意决定已有特征的画法。
- 正常观察特征入口当前使用 Feature.rerun().to_df() 或 to_dfs()；这**不证明**外部正常保存的任意特征结果已经可以原样接入。
- 图页链接、实际 Bokeh 渲染、主证据切片和仅供展示的数据视图不是同一性质的产物；应按本次实际结果区分。

## 3. 实际使用时怎样考虑

先将工作 2 的配置与真实输出、uplot/CAEGraph 能力及 aidata 消费入口建立对应，再按实际问题定位时间位置、组织范围并取得真实图和同范围数据。配置格式或接口有较大问题时给出实际证据与最小接法，不自行改变配置归属，也不因工具默认能力压回专业设计。

**工作 2 实际配置文件 → 工作 3 接入 `aidata/feature_configs` 的交接已明确。**文件作为可修订专业成果保存，入库和验证仍走相关仓库实际分支及写权，不因有文件就宣称画法、接口或专业观察已通过。

优先实际验证正常 Feature 实例/已有正式结果能否直接供绘图。N 使用多表 `to_dfs`/`read_session`，已有结果可经 `CalType.OnlyRead` 读取；不能把普通入口调用 `rerun()` 理解为必须重算整段历史。按锁定 aidata、uplot、TIS 版本核多表关联、随时间变化及画法，只有实际不足才定位缺层和最小适配，不凭表数量或旧 CSV 路径推定必须改公共接口。

`BI-01-FO-01` Worker 首个 rb 单 As-Of 的八份 CSV 和 `fixed_input` 是有效的首例投影，不是未经比较即可固化的默认架构。需要缓存/导出时可保留 CSV 并说明理由，不为避开 CSV 复制正式计算或重跑 N。工作 4 的数据优先取正式特征、行情与必要上游；`plot_view_data` 核对显示内容，不能冒充正式结果或已经完成专业分析。

## 4. 工程边界

实际确需扩展 aidata 的通用能力时沿其自身仓库与独立分支处理，不在 observe-iterate 新造平行绘图实现。图形/数据服务具体能力及使用参数始终以当时锁定的 aidata 源码与实际接口为准，不能从历史操作说明推定最新运行已成功。

工具入口参考：
- https://github.com/daowei2026/aidata/tree/main/feature_configs
- https://github.com/daowei2026/aidata/blob/main/docs/RUN_BRIEF_INPUT_CONTRACT.md
- https://github.com/daowei2026/aidata/blob/main/docs/DEVELOPMENT_GUIDE.md
- https://github.com/daowei2026/aidata/blob/main/evidence_plot.py
