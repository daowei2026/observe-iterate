# C3｜Q CAEGraph 可注入代码与 D 阶段绑定合同

## 1. 当前代码

`daowei2026/observe-iterate@435c2ed129ba7596b9d5a102bc0d8bf6104729ba:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_injectable.py`

该文件是可执行 Python 定义，不是伪代码。它使用锁定版 `uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad` 已存在的：

- `CAEGraph`、`PlotSet`；
- `AllSymsMainFig`、`AllSymsFig`、`PerSymFigSet`；
- `MainFig`、`SubFig`；
- `KPriceLine`；
- `BasePlotter` 扩展点；
- Bokeh `ColumnDataSource`、`HoverTool` 与 glyph。

## 2. D 必须注入的内容

D 通过 `QDisplayBinding` 注入：

| 参数 | 含义 | 不得替代成什么 |
|---|---|---|
| `q_feature` | 本次真实外层 Q 实例 | 不能在 C 代码中硬编码 `make_features(...)` |
| `price_feature` | 在各 `CurrSymbol` 上读取原价的特征 | 不能从 ratio 总览反推原始价格 |
| `frame_adapter` | 将真实 Q 公共表整理为六张 canonical display frames | 不能把 DataFrame 行机械认作业务 occurrence |
| `field_binding` | 当前版本真实字段路径及必要转换 | 不能将字段名猜测写死为永久合同 |
| `position` | SOF、block、calendar、对象集、timespans | 不能在 C3 固化 B 的当前默认位置 |

`QPositionBinding` 明确接收：

```text
sof_name
block
calendar_name
objects
timespans
context_start / context_end（可选）
```

因此 C3 没有写死：

- `TA_updto20240229_DBA`；
- `steel`；
- `night_end_at_2300`；
- `rb/hc/i`；
- `2021-01-01～2022-12-31`；
- 任一具体 Q 实例或结果目录。

这些值由 D 消费 B 当前有效产物后正式注入。

## 3. canonical display frames

### `timeline`

一行对应一个真实 F candidate、Q `DirectionalOccurrence` 或 Q `DirectionalDutyEnd`。必需字段：

```text
event_uti, event_kind, event_id,
q_life, q_revision, previous_ref,
candidate_ref, members, known_uti,
qualification, observation, applicability,
end_reason, last_successful_ref, detail
```

约束：

- Q revision 的 `event_uti` 是正式 publication firing；
- `known_uti` 是 `directionalKnown`；
- duty end 使用自身真实 firing/known/progress，不能伪造成 Q revision；
- F/Q Life 和 Revision 保持各自身份。

### `revision_links`

```text
from_uti, to_uti, q_life, from_revision, to_revision
```

只表达同一 Q Life 的 `directionalPrevious` 链。Duty end 不进入该链。

### `states`

```text
publication_uti, q_life, q_revision,
state_kind, state_value, detail
```

`state_kind` 只允许表达该 Q revision 的：

```text
qualification
observation
applicability
```

### `members`

```text
publication_uti, q_life, q_revision, member,
asked_uti/price,
used_uti/price,
successor_uti/price,
endpoint_uti/price,
completion, verdict, basis,
path_complete, through, material_known,
missing_range, candidate_ref
```

约束：成员行是 Q occurrence 的嵌套 payload，不是独立业务 occurrence。实际、确认、已知、endpoint 和 Calendar 位置不得合并成一个时间字段。

### `quantities`

```text
publication_uti, q_life, q_revision, member,
quantity_kind, quantity_value, availability
```

`quantity_kind` 保持六类：

```text
ProgressP, AmplitudeA, DurationD,
PathLengthL, EfficiencyE, CounterC
```

`quantity_value` 缺失时必须保留 `availability`，例如：

```text
EndpointUnavailable
ClockUnavailable
PathUnavailable
ZeroPathNotApplicable
```

禁止把缺失替换成 `0`。不同量单位不同，代码只在分类轨上显示种类，原值和 availability 放入 hover。

### `audit`

```text
event_uti, event_id, event_kind,
previous_ref, candidate_ref,
publication_or_end_known, detail
```

用于保留完整审计信息，避免常显图元过载。

## 4. 真实公开表到 canonical frames 的映射边界

D 的 adapter 应优先读取 Q wrapper 的 `to_dfs()`／`read_exact()`／`read_at_knowledge()`，至少处理：

- `definitions` 与 bindings：方法、方向、Δ、12Δ/6Δ/2 等固定元数据；
- `occurrences`：Q identity、candidate exact、known、观察界和组级状态；
- `occurrences_organizationPrevious`：Previous；
- `occurrences_organizationMembers`：成员对象、asked/used、completion、verdict、basis、path、through、material known；
- successor、endpoint、clock、missing range 子表；
- quantities 与 quantity number 子表；
- `duty_ends` 及其最后成功 Q 展开：真实 end reason/known/progress 和最后成功观点。

adapter 必须以公共表的坐标／父子层次完成 join，不能仅凭时间或成员名做模糊拼接。

## 5. 当前图层与 C2 的对应

| C2 面板 | C3 实现 |
|---|---|
| P1 多品种 ratio 总览 | `AllSymsMainFig + KPriceLine(std_method="ratio") + QMemberGeometryPlot` |
| P2 生命周期轨 | `AllSymsFig + QLifecyclePlot` |
| P3 组级状态 | `AllSymsFig + QStatePlot` |
| P4 各品种原价与成员位置 | `PerSymFigSet + MainFig + KPriceLine(raw) + QMemberGeometryPlot` |
| P4 成员 verdict/六量审计 | `PerSymFigSet + SubFig + QMemberAuditPlot` |
| P5 精确引用审计 | `AllSymsFig + QAuditPlot` |

所有图共享 CAEGraph 的统一 x-range。图例支持隐藏；hover 保留精确身份、状态、位置和缺失语义。

## 6. 已核对的能力边界

1. 锁定版内置 `MulFieldsGlyphs` 的默认 hover 主要是时间和值，不能完整承载本 Q 的 identity/reference/missingness；因此 C3 使用官方 `BasePlotter` 扩展点，不要求修改 uplot 核心。
2. `SeqOfFieldsPlot` 在手册中缺少本场景可直接验证的完整例子；本方案不依赖它，而由 adapter 把嵌套公共表展开成 canonical frames。
3. CAEGraph 没有专用“revision chain”业务类；`QLifecyclePlot` 使用普通 segment 和 point glyph 实现，仍保留真实 Q Previous 语义。
4. ratio 只用于 P1 显示；各品种 detail 保留 raw K 与 raw member price。

因此本 C 阶段没有必须新增 uplot 核心能力的阻塞缺口。

## 7. 验证状态

已完成：

- Python `py_compile`；
- 无固定 SOF、日期、对象、实例的静态检查；
- 位置、实例、字段 adapter 的显式注入检查；
- C2 面板与 C3 plotter 的逐项映射；
- 显式 duty end、Previous、candidate reference、missingness 的代码检查。

尚未声称：

- 已在 `/dwdhome/fy/BASE_E6_2_copy` 运行；
- 已读取真实 Q 产物；
- 已生成真实 D/E HTML；
- 已证明目标环境中所有依赖版本可运行。

这些属于后续 D 的实例/字段/位置正式绑定与 E 的真实运行检查，不是 C 将模拟结果冒充真实结果的理由。
