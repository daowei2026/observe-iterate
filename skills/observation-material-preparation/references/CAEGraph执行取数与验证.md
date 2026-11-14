# CAEGraph：从已有定义到真实观察数据的执行说明

> 状态：**技术接线操作约定（候选）**，不是声称已有“任意视窗一键完整导出”的稳定接口。所有用例应先锁定真实运行版本。此文专门解决上位 Skill 的**执行取数**步骤，不替代 [使用手册](https://github.com/daowei2026/uplot/blob/e6.2/CAEGraph使用手册.md)。

## 1. 先选对完整入口

- 若已有图，找到**原 Notebook / 真实注册函数**、对象、参数、交易日历、PlotSet.timespans、实际特征来源和原运行路径。不能只凭图截图恢复含义。
- 新图按手册查：图集 CAEGraph/PlotSet → 主附图布局类 → VBarPlot/MulFieldsGlyphs/MulSegPlot/KPriceLine 等 → 参数/字段绑定与必要后处理 → 控件及视窗。
- EAW 有多个版本：T056 是含 1m/5s K 线及两张支持度附图的 CAEGraph；T059 剩余 CAEGraph 主要为 K 线，其它内容可由直接 Bokeh 实现；正式看板 30m/1m/5s 为多个 CAEGraph。**独立 Bokeh 内容必须另取，不能由 CAEGraph 图树推断它存在**。详见 [EAW 原稿](../../../reference-cases/EAW_CAEGraph观察准备Skill候选_原图落地与复用边界_20261112.md)。
- 有条件读取原特征表（`to_df` / `to_dfs`）时，通常比从最后显示值反推更可靠；CAEGraph 则提供其实际显示/组织口径。两者应在需要时关联而非二选一。

## 2. 三个不可混成一份的数据阶段

| 数据阶段 | 可以取得什么 | 不能据此宣称什么 |
|---|---|---|
| 业务特征源/ADT/正式输出 | 原始业务记录、已实现的中间业务结果、真实实际/确认时间（如字段存在） | 不代表已经呈现于原图；也未必有所有内部 working-state |
| CAEGraph **构图后的**数据树、图对象和 Bokeh CDS | 图元实际使用的字段数组，及通过 Figure/Renderer 能回溯的标题/图例/画法 | 不自动还原 FeatDFProcessor 前的原值；不自动等于用户拖动后画面 |
| **指定可见窗口与前端回调生效后的**显示数据 | 当前基准/动态处理完成的图层数组、显隐、坐标范围 | 在未验证同步/回调语义时不能当作稳定 Python 服务端输出 |

尤其注意：`__prestd_*` 保存的是“动态标准化之前”的值，**不保证是最原始的业务字段**；显示前已经 clip 的数值不能反推出未 clip 的真值。

## 3. 已在源码核对的 Python 构图数据入口

[utlv2.py · CAEGraph.layout](https://github.com/daowei2026/uplot/blob/e6.2/utlv2.py) 定义了 `plot_roots`、`all_figs` 等参数；`produce_widgets()` 会建立 `PlotDataFolder`，`PlotSet.plot()` 维护图对象。结构可这样检查：

```python
# 在真实 Notebook 中 graph 已定义，运行前已核实上下文/缓存/成本。
plot_roots = []
figure_groups = []
layout = graph.layout(ncols=1, plot_roots=plot_roots, all_figs=figure_groups)
# 注意：不调用 show() 也可能取数、触发上游计算或内存占用。

for i, root in enumerate(plot_roots):
    root.print(f"plot_roots[{i}]")  # 输出可访问的树和数据源表达式

# source 叶节点包含 cds.data；具体字段和图元关联还要看 figure_groups
```

[源码 pdt.py](https://github.com/daowei2026/uplot/blob/e6.2/pdt.py)：`PlotDataFolder.children` 与 `PlotDataNode.cds.data`。它的 `print` 给出 `pd.DataFrame(<node>.cds.data)` 的使用指引。注意 `cds.data` 是**绘图数据源**，不是所有正式业务输出的合集。

### 此入口距“完整导出”还差什么

- 递归遍历数据树并保存**全量需要的行**，标注实际行数、来源路径；不能只保存前 5 条预览然后声称材料齐全。
- 检查 `figure_groups` 内 Figure/Renderer 到 `data_source` 的绑定：面板顺序、标题、图例、图元类型及常量画法（例如 `bottom`、固定颜色或大小可能不是 CDS 列）。
- 与原图配置中的真实业务身份联系：同一图例 2 可能对应不同参数全局 ID；不以图例文字作为稳定 ID；同一 CDS 供多个图元时按**业务事件**而非图元数量计数。
- 如果图中只有筛选/合并后的字段，需要原值/中间状态还应回到源特征或增加 trace；不让“展示值”冒充“业务输出”。

目前文档给的是**可使用的已存在构图入口 + 待完成的通用导出职责**，不声称已经存在独立的全量导出 API 或真实用例全字段验收。

## 4. 观察窗口和交互状态：什么已实现、什么待接通

手册说明 PlotSet.timespans、KPriceLine.std_method、动态控件；[utlv2.py · CAEGraph](https://github.com/daowei2026/uplot/blob/e6.2/utlv2.py) 的 `manual_upd` 默认 True；[pfw.py](https://github.com/daowei2026/uplot/blob/e6.2/pfw.py) 与 [dynstd.js](https://github.com/daowei2026/uplot/blob/e6.2/dynstd.js) 用于价格动态标准化。必须区分：

- **加载范围**：构图时已经载入/计算的历史；
- **可见范围**：当前 `x_range.start/end`，放大/平移可能改变价格基准；
- **参数状态**：控件的新值是否已经通过手动更新或回调生效；
- **处理方式**：动态 JS、静态 Python、未标准化，实际是哪一种；
- **数据完成状态**：是否已经完成窗口回调/数据更新，是否可以得到固定快照。

**当前最低目标**：给定一个确定的已加载观察实例与指定窗口，取得该窗口的对应显示数据，并与浏览器中实际处理后的数据比对。首先验证一个原窗口和一个局部窗口，再验证超出加载边界的情况；不必先做鼠标拖动自动化。

若只能导出构图阶段值，应标记 `construction_snapshot`，不是 `viewport_final`。若窗口状态无法稳定读取，记录阻碍/可分析范围；不要自行写近似算法后称与 `dynstd.js` 精确等价。

## 5. 一份实际观察数据包最少包含什么

```text
observation_manifest.md / json
  ├─ 来源：特征实例、参数、版本、日历、对象、取数接口
  ├─ 观察问题与本轮所需处理阶段
  ├─ loaded_range / visible_range / applied_params / normalize_state
  ├─ 数据列表：原业务数据、中间或后处理表、图元 CDS（按需）
  ├─ 图表组织：PlotSet、主/附图、面板标题、图例 → Renderer → CDS → 来源
  ├─ data_stage：source / postprocessed / construction_snapshot / viewport_final
  ├─ 时间角色、单位、确认/已知规则和身份范围
  ├─ 数据量及取得状态：完整、必要范围完整、部分、失败、有效空
  ├─ 质量核对：样例对账与影响结论的缺失
  └─ 尚需补充的业务中间证据、阻塞/建议
```

实际文件格式按既有项目工具选择，不强制所有数据合成一个大表；多对象、多频率、不同量纲及动态图层可分别存储。**保持能回溯来源和同一业务对象**比统一成一个超级 DataFrame 更重要。

## 6. 真实环境的最小验收

1. 固定原实际实例、数据盘和各仓库版本，记录执行入口及是否重算；同一运行应可重复得到相同关键行数/字段。
2. 比对原业务 `to_df/to_dfs` 的关键样例与后处理值；区分 0、有效空、未读到、无历史、Pending。
3. 列出各主要面板/图层及来源，核对正确的参数/事件身份和图例映射；不能漏非 CDS 常量参数。
4. 定义两段窗口，核对价格原值、基准及显示值；静态/动态路径分别核对，必要时从浏览器端取得真实结果。
5. 检查一条同一对象多时间图元只计一次事件；检查某条业务重要但原图未提供的中间信息是否能从源特征取得。
6. 记录 `PLAN_READY / DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED`，只在实际运行数据及关键核查完成后写 `DATA_READY`。

验收数据不在本文件中伪造。参考案例：[高频完整原图](https://github.com/daowei2026/viewer/blob/e6.2/frp/同步(多对象)/密集与板块密集的简单标准化.ipynb)、[EAW T056/正式看板源码导航](../../../reference-cases/EAW_CAEGraph观察准备Skill候选_原图落地与复用边界_20261112.md)。

## 7. 当现有功能不够

先形成**最小具体缺口**：当前观察问题、期望字段/时间/图层、现有图定义和 API 的实际输出、失败证据、最低可行补丁、验证方式与成本。区分：
- 现有源特征已计算但没有公开：补读取/临时 trace；
- 数据后处理能力不足：考虑 FeatDFProcessor/纯函数组合或新增处理组件；
- 构图和图元表达不足：新绘图器/参数/布局；
- 指定窗口的完整取数不足：CAEGraph/uplot 通用导出/状态接口；
- 只有业务因果证据缺失：不能靠绘图技术臆造；回原业务处理链找证据。

不默认要求新增正式 FRP 特征，也不让 CAEGraph 承担整个业务合理性判断。
