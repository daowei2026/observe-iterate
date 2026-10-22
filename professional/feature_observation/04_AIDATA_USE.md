# aidata 在新四项专业工作中的位置（初版）

## 首次使用：从 README 进入

**先读取所采用 aidata 版本的 [README.md](https://github.com/daowei2026/aidata/blob/main/README.md)**，理解整体用途、长期概览和大—中—小尺度、定位特征与观察特征，以及图和对应数据的基本关系。实际配置时再按需阅读 [开发参考](https://github.com/daowei2026/aidata/blob/main/docs/DEVELOPMENT_GUIDE.md)、[run_brief 输入合同](https://github.com/daowei2026/aidata/blob/main/docs/RUN_BRIEF_INPUT_CONTRACT.md)、[真实数据测试说明](https://github.com/daowei2026/aidata/blob/main/tests/README.md)。

可优先查阅已经提供实际运行方式的 [microstructure_review.py 示例](https://github.com/daowei2026/aidata/blob/main/examples/microstructure_review.py)，了解多个具体特征怎样实例化、配置 `run_brief`、创建看图页面；**只借调用方法，不默认借其板块、参数、时间尺度或特征含义**。本次 `U2NormalNodeBehaviorFrp` 仍须从自己的真实结果读回与方法合同判断能否接入。

## 1. 工具职责与专业职责分开

- 工作 2 决定特征信息怎样展示才方便理解，包括实际要画的内容、文字解释以及是否先单品种/多品种。
- 工作 3 检查 aidata 的长期概览和大—中—小尺度图是否适用，再按本次观察配置制图。
- aidata 的实际绘图接口不是自动代替专业人员完成特征展示设计，更不是自动证明特征具有投资业务价值。

## 2. 已有能力的确认范围

从 aidata 当前 README、docs/DEVELOPMENT_GUIDE.md、docs/RUN_BRIEF_INPUT_CONTRACT.md、feature_configs/ 和 evidence_plot.py 可核：

- 正常使用时，通过 run_brief_input 指明时间、对象、定位及观察特征、观察尺度等配置；定位特征和观察特征可以不同。
- 独立特征展示配置在 aidata/feature_configs，当前已有 ZigConfirm、ScaleTurnCalendar、ThickFrp、BlkThickFrp 的专属配置；通用绘图支持 point/line/segment 和有限的样式、文字、hover。
- 已声明的展示配置可被读取，调用方也能显式给完整 plot_binding 覆盖；不是每次都要 AI 任意决定已有特征的画法。
- 正常观察特征入口当前使用 Feature.rerun().to_df() 或 to_dfs()；这**不证明**外部正常保存的任意特征结果已经可以原样接入。
- 图页链接、实际 Bokeh 渲染、主证据切片和仅供展示的数据视图不是同一性质的产物；应按本次实际结果区分。

## 3. 实际使用时怎样考虑

先对特征需要展示的信息及实际已有结果建立对应；检查能否使用已有特征展示配置、是否只需新配置、还是有某种展示方式超出当前通用绘图能力。再在适合的时间尺度与范围中生成实际图及对应数据。必要时通过结果调整前面的展示设计或参数。

**展示配置未来放入 feature_configs 是当前倾向，不是已经决定的执行时点**；不能只为使目录“有文件”就提交未经专业观察的正式画法。

对特征保存结果的读取、可能的接口衔接、实际多尺度制图及浏览器可用性，应在后续新仓库材料落实后的运行前审查中按本轮真实代码和执行环境核对；本准备稿不把旧运行遗留问题直接推断成新的必然问题。

## 4. 工程边界

实际确需扩展 aidata 的通用能力时沿其自身仓库与独立分支处理，不在 observe-iterate 新造平行绘图实现。图形/数据服务具体能力及使用参数始终以当时锁定的 aidata 源码与实际接口为准，不能从历史操作说明推定最新运行已成功。

工具入口参考：
- https://github.com/daowei2026/aidata/tree/main/feature_configs
- https://github.com/daowei2026/aidata/blob/main/docs/RUN_BRIEF_INPUT_CONTRACT.md
- https://github.com/daowei2026/aidata/blob/main/docs/DEVELOPMENT_GUIDE.md
- https://github.com/daowei2026/aidata/blob/main/evidence_plot.py
