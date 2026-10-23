# aidata 在新四项专业工作中的位置（初版）

## 首次使用：从 README 进入

**先读取所采用 aidata 版本的 [README.md](https://github.com/daowei2026/aidata/blob/main/README.md)**，理解定位、观察范围、图和对应数据的关系。长期概览和大—中—小尺度是按问题使用的工具，不是工作 2 的设计模板。实际配置时再按需阅读 [开发参考](https://github.com/daowei2026/aidata/blob/main/docs/DEVELOPMENT_GUIDE.md)、[run_brief 输入合同](https://github.com/daowei2026/aidata/blob/main/docs/RUN_BRIEF_INPUT_CONTRACT.md)、[真实数据测试说明](https://github.com/daowei2026/aidata/blob/main/tests/README.md)，记录准确版本。

可优先查阅已经提供实际运行方式的 [microstructure_review.py 示例](https://github.com/daowei2026/aidata/blob/main/examples/microstructure_review.py)，了解多个具体特征怎样实例化、配置 `run_brief`、创建看图页面；**只借调用方法，不默认借其板块、参数、时间尺度或特征含义**。本次 `U2NormalNodeBehaviorFrp` 仍须从自己的真实结果读回与方法合同判断能否接入。

## 1. 工具职责与专业职责分开

- 工作2由专业Pro主导，读所采用Uplot/CAEGraph手册后决定画法，并在真实特征数据及行情上实际重新画通、验证、修订，交配置及实际执行成功、可交互复现的Notebook；可委派现场Worker，不能把展示画通推给工作3。HTML仅辅助，不要求或以PNG作看图交付，不声称GitHub上传即可交互运行。使用Uplot不授源码写权。
- 工作3在工作2实际画通且对应成果得到管理Pro接收认可后，消费其适用画法/配置，按需放入`aidata/feature_configs`并验证正常平台调用；利用多层定位组织观察节点/范围，交实际打开的正常平台URL及同节点正式数据。它不从零承担特征画法调通，工具衔接若暴露画法问题返回工作2。
- 设计不固定为单 As-Of 的 6+6+Working 截面，要考虑沿时间观察和选定时点回看。最终多品种呈现中颜色优先留给品种，其他性质优先使用线型、形状、位置或分图；不新增单/多品种选择任务，不预设实时刷新或逐拍重算。
- 工作4在工作3的同节点平台和正式数据交付获管理Pro接收认可后，主要消费board正式切片/交付并关联同行情、必要上游；N多表/as-known不足时补正常OnlyRead原结果。已可靠原数据可用于上游准备和核验，但不能绕过工作3开始正式工作4；图用投影只核显示，未实际看图如实说明。
- aidata 的实际绘图接口不是自动代替专业人员完成特征展示设计，更不是自动证明特征具有投资业务价值。

## 2. 已有能力的确认范围

以下是准备稿与首例提供的接口核对入口，不代表新设计已全部适配；实际能力以锁定版本的 README、docs/DEVELOPMENT_GUIDE.md、docs/RUN_BRIEF_INPUT_CONTRACT.md、feature_configs/、evidence_plot.py 和真实调用为准：

- 正常使用时，通过 run_brief_input 指明时间、对象、定位及观察特征、观察尺度等配置；定位特征和观察特征可以不同。
- 独立特征展示配置在 aidata/feature_configs，当前已有 ZigConfirm、ScaleTurnCalendar、ThickFrp、BlkThickFrp 的专属配置；通用绘图支持 point/line/segment 和有限的样式、文字、hover。
- 已声明的展示配置可被读取，调用方也能显式给完整 plot_binding 覆盖；不是每次都要 AI 任意决定已有特征的画法。
- 正常观察特征入口当前使用 Feature.rerun().to_df() 或 to_dfs()；这**不证明**外部正常保存的任意特征结果已经可以原样接入。
- 图页链接、实际 Bokeh 渲染、主证据切片和仅供展示的数据视图不是同一性质的产物；应按本次实际结果区分。

## 3. 实际使用时怎样考虑

正常平台路径须实际核：`build_chart_run(run_brief_input)`建立定位节点/冻结run与范围；`build_big_world_chart_pages(run, run_brief_input=..., save=True)`注册现有Trier/CAE节点、取得`report_url`并实际打开核图层；`build_board_run({...原run_brief_input, "run_id": run.run_id}, reuse_core=True)`复用同定位取得`feature_slices/`、来源索引及`delivery/`。三者重在真实结果与同run衔接，不机械重跑三遍；board可创建/复用core，已有有效run可复用，按问题取层级/范围而非固定全导出。具体API和兼容情况须读所采用版本README/合同，不凭本文预言现场已成功。

N展示或多表不兼容时核实际差异、必要最小衔接及写权，不能绕过标准入口后把standalone HTML、PNG、临时localhost或写了适配器称工作3完成。平台链接要真实打开且同位置正式数据身份可追溯，缺任一部分如实记未完。

先将工作 2 的配置与真实输出、uplot/CAEGraph 能力及 aidata 消费入口建立对应，再按实际问题定位时间位置、组织范围并取得真实图和同范围数据。配置格式或接口有较大问题时给出实际证据与最小接法，不自行改变配置归属，也不因工具默认能力压回专业设计。

**工作2真实Uplot重画/Notebook验证及配置 → 管理Pro认可适用范围 → 工作3 aidata正常平台观察组织/同节点正式数据 → 管理Pro认可交付 → 工作4正式观察**。交接须有确切实物和管理决定，不能凭技术输出自动转下游。配置作为可修订成果保存，入库/最小接入走实际分支写权，不因文件存在称画法或专业观察通过。本轮Owner698b229不采用此前所有图作合格工作2成果，必须重新绘制/验证；旧图文件与历史保留，可信数据可核源复用、旧配置只作未验证参考，不用补链接/补验证恢复旧图资格。

优先实际验证正常 Feature 实例/已有正式结果能否直接供绘图。N 使用多表 `to_dfs`/`read_session`，已有结果可经 `CalType.OnlyRead` 读取；不能把普通入口调用 `rerun()` 理解为必须重算整段历史。按锁定 aidata、uplot、TIS 版本核多表关联、随时间变化及画法，只有实际不足才定位缺层和最小适配，不凭表数量或旧 CSV 路径推定必须改公共接口。

`BI-01-FO-01` Worker 首个 rb 单 As-Of 的八份 CSV 和 `fixed_input` 是有效的首例投影，不是未经比较即可固化的默认架构。需要缓存/导出时可保留 CSV 并说明理由，不为避开 CSV 复制正式计算或重跑 N。正式工作 4 的数据优先取获认可的同节点board正式切片、行情与必要上游；`plot_view_data` 核对显示内容，不能冒充正式结果或已经完成专业分析。

## 4. 工程边界

实际确需扩展 aidata 的通用能力时沿其自身仓库与独立分支处理，不在 observe-iterate 新造平行绘图实现。图形/数据服务具体能力及使用参数始终以当时锁定的 aidata 源码与实际接口为准，不能从历史操作说明推定最新运行已成功。

工具入口参考：
- https://github.com/daowei2026/aidata/tree/main/feature_configs
- https://github.com/daowei2026/aidata/blob/main/docs/RUN_BRIEF_INPUT_CONTRACT.md
- https://github.com/daowei2026/aidata/blob/main/docs/DEVELOPMENT_GUIDE.md
- https://github.com/daowei2026/aidata/blob/main/evidence_plot.py
