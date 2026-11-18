# CAEGraph：执行、核图后正式取数的技术参考

> 状态：技术接线参考（候选）。本文件服务 [E｜CAEGraph 执行／运行](../caegraph-execution/SKILL.md)，不替代 E 的内部 Workflow，也不替代 [CAEGraph 使用手册](https://github.com/daowei2026/uplot/blob/e6.2/CAEGraph使用手册.md)。所有结论均应以本次真实运行版本为准。

## 1. E 的固定顺序

```text
D 完整定义
→ Worker 运行与权限内修复
→ 与 D 核对最终脚本
→ 与 C 预期 HTML 核对最终图
→ 接受最终图
→ 正式取得图的数据
→ 核对图与数据一致
```

调试过程中可临时查看数据，但只有最终图接受后导出的数据，才进入正式观察材料。

## 2. 三类数据阶段不能混同

| 数据阶段 | 可以取得什么 | 不能据此宣称什么 |
|---|---|---|
| 业务特征源／ADT／公开输出 | 原始业务记录、主输出和已公开中间处理结果、真实时间字段 | 不代表已进入最终图，也未必包含内部 working-state |
| CAEGraph 构图数据树、图对象和 Bokeh CDS | 图元实际使用的字段数组及 Figure／Renderer／data source 关系 | 不自动还原后处理前原值，不自动等于前端窗口更新后的显示数据 |
| 指定可见窗口和前端回调生效后的显示数据 | 当前基准、动态处理、显隐和坐标范围下的最终显示数组 | 未验证同步和回调语义时，不能当稳定服务端输出 |

`__prestd_*` 只表示动态标准化之前，不保证是业务最原始字段；被 clip 的显示值不能反推未 clip 原值。

## 3. 已核对的构图入口

[utlv2.py · CAEGraph.layout](https://github.com/daowei2026/uplot/blob/e6.2/utlv2.py) 支持 `plot_roots`、`all_figs` 等参数；`produce_widgets()` 建立数据树，`PlotSet.plot()` 维护图对象。

```python
plot_roots = []
figure_groups = []
layout = graph.layout(
    ncols=1,
    plot_roots=plot_roots,
    all_figs=figure_groups,
)

for i, root in enumerate(plot_roots):
    root.print(f"plot_roots[{i}]")
```

[源码 pdt.py](https://github.com/daowei2026/uplot/blob/e6.2/pdt.py) 中 `PlotDataFolder.children` 与 `PlotDataNode.cds.data` 可用于检查构图数据。注意：不调用 `show()` 也可能触发取数、上游计算或显著内存占用。

### 该入口距正式数据包还缺什么

- 递归遍历并保存本次需要的完整行，不以少量预览冒充全量；
- 从 `figure_groups` 核对 Figure／Renderer 到 `data_source` 的绑定；
- 记录面板、标题、图例、图元类型及 CDS 之外的常量配置；
- 将图层重新关联到 A 的业务事件身份和 D 的字段绑定；
- 原图只保留显示值时，需要原值应回到源特征读取。

当前不声称存在“任意视窗一键完整导出”的通用 API。

## 4. 加载范围、可见范围与前端状态

必须分开：

- **加载范围**：构图时已经载入或计算的历史；
- **可见范围**：当前 `x_range.start/end`；
- **参数状态**：控件值是否已经通过更新或回调生效；
- **处理方式**：动态 JavaScript、静态 Python 或未标准化；
- **完成状态**：窗口回调是否完成、能否得到固定快照。

手册、[pfw.py](https://github.com/daowei2026/uplot/blob/e6.2/pfw.py) 与 [dynstd.js](https://github.com/daowei2026/uplot/blob/e6.2/dynstd.js) 可用于核对动态标准化路径。若只能导出构图阶段值，标记 `construction_snapshot`，不能写成 `viewport_final`。不要自行写近似算法后声称与前端逻辑精确等价。

## 5. 与 C 预期 HTML 的核对重点

必须核对：

- 面板数量、顺序和主附图关系；
- 图元类型及其业务语义；
- actual、confirm、known 等事件位置表达；
- 多品种布局、共享时间轴和独立价格轴；
- 图例、hover 和业务身份；
- 输入、业务主输出和必要中间处理结果是否处于预期位置。

允许因真实数据变化：曲线形状、点数量、坐标范围和局部缩放。无需追求无意义的像素级一致。

## 6. 一份正式 CAEGraph 图数据包至少包含什么

```text
observation_manifest.md / json
  ├─ 最终 D 定义版本、最终脚本版本、最终 HTML
  ├─ 特征实例、代码／数据版本、日历、对象、取数接口
  ├─ loaded_range / visible_range / applied_params / normalize_state
  ├─ 数据文件清单：source / postprocessed / construction_snapshot / viewport_final
  ├─ PlotSet、主／附图、Renderer、CDS／源表映射
  ├─ 事件身份、时间角色、单位、基准和转换损失
  ├─ 行数、对象数、时间范围与完整性状态
  ├─ 有效空、无 occurrence、缺数据、历史不足、Pending 等缺失语义
  ├─ 与最终图的一致性核对
  └─ 尚未解决的缺口和影响
```

不强制所有内容合并为一个超级 DataFrame。能够回溯同一业务对象和来源，比文件形式统一更重要。

## 7. 图与数据一致性最低检查

1. 最终脚本、HTML、定义和数据包绑定同一版本及有效运行；
2. 各主要面板／图层能追到 Renderer、data source 和源事件／字段；
3. 品种、时间、日历、参数和特征实例一致；
4. 原业务值、后处理值、构图 CDS 和视窗最终值阶段明确；
5. 同一 occurrence 出现在多个图元中只计一次业务事件；
6. 图例不是稳定身份，身份字段和 revision 仍可追溯；
7. 0、有效空、未读到、无历史和 Pending 不混同；
8. 只导出预览时明确标记 `preview`，不能形成 `DATA_READY`。

## 8. Worker 权限边界

Worker 可在派单授权内修复语法、导入、路径、确定 API 差异和不改变业务语义的机械错误。以下情况必须返回：

- 更换品种、时间或多层位置；
- 删除或新增业务字段；
- 改变主附图职责、事件位置表达或标准化方法；
- 新算一个值替代真实特征输出；
- 无法判断是位置、展示还是集成问题。

每次修复保留修改前后、原因、权限依据和语义影响。

## 9. 现有功能不够时

形成最小具体缺口：受影响的事件／字段／图层、现有定义和 API 实际输出、失败证据、最低替代方案、语义损失和成本。区分：

- 源特征已有但未公开：补读取或临时 trace；
- 后处理不足：使用确定性处理组件或纯函数；
- 图元／布局不足：提出最小绘图能力；
- 视窗最终值无法读取：提出状态／导出接口；
- 业务证据本身不存在：回 A 或源特征，不能靠绘图技术臆造。

不默认要求新增正式 FRP 特征，也不让 CAEGraph 承担合理性判断。
