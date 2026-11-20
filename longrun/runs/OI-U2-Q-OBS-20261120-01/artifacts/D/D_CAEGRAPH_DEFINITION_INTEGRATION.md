# D｜PostTurnGroupDirectionalOrganizationFrp CAEGraph 定义集成

## 0. 产物身份与结论

| 项目 | 值 |
|---|---|
| run_id | `OI-U2-Q-OBS-20261120-01` |
| work_item_id | `OI-U2-Q-OBS-20261120-01-WI-D` |
| stage_instance_id | `OI-U2-Q-OBS-20261120-01-M-D` |
| delegation_id | `D004` |
| 执行身份 | `chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1` |
| 特征 | `PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织） |
| 定义编号 | `Q-CAEGRAPH-D004-v1` |
| 阶段状态 | **完整** |
| Worker | **不需要；未签发** |

同源机读集成记录：

`daowei2026/observe-iterate@546e457983c7d3e00378eea26872e605d79f8e20:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_CAEGRAPH_DEFINITION_INTEGRATION.json`

本 D 已把外层真实 Q 实例、A 的事件／身份／位置／数值字段、B 的普通默认位置以及 C2/C3 展示定义一次性集成为可直接交 E 尝试运行的完整 Python CAEGraph 定义。

本阶段没有运行真实 Q、没有生成最终 HTML，也没有把定义级检查冒充 E 的真实运行结果。

---

## 1. 完整定义入口

E 的主入口：

`daowei2026/observe-iterate@9e03c89211ec4665763e1f609b37483c80c72930:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_definition.py`

该入口及同目录八个支持模块共同构成一份完整定义，不是彼此独立的候选方案：

| 职责 | 精确引用 |
|---|---|
| 共同合同、准确实例参数、canonical frames 与字段枚举 | `daowei2026/observe-iterate@3dc03ecfea52d38fa7ce965d17710f0ebb7b4021:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_common.py` |
| 锁定公共表读取、v2 duty-end 读取、真实父坐标索引 | `daowei2026/observe-iterate@cf6a5d496f6b3bfafdadcbd7f11f30a5a182b158:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_support.py` |
| 成员多位置及六量字段适配 | `daowei2026/observe-iterate@0fcb881f99c4035dc81de154f34d86e6994b1227:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_members.py` |
| F/Q exact occurrence、Previous、状态、显式 end 与 canonical frames | `daowei2026/observe-iterate@dcdf9949f1297f854dbd852f75a9f39ef268b72b:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter.py` |
| 生命周期与组级状态 plotter | `daowei2026/observe-iterate@eac1cb3342ff92961bf8055ac4c04042b94aeed4:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_base.py` |
| 成员几何与六量审计 plotter | `daowei2026/observe-iterate@23fcb47fff8494df138445fc5ee705fe43a36764:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_member.py` |
| 精确引用审计与 CAEGraph 总装配 | `daowei2026/observe-iterate@6ffa0e4b6ebb394f61fcb52277f7c27c69fd35b9:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_build.py` |
| plotter 汇总导出 | `daowei2026/observe-iterate@af96601fe525f2e6059ae3bd976b3b19de3060e7:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters.py` |

九模块按职责拆分只是为了可读性和长度控制；E 只运行 `q_caegraph_definition.py`。

---

## 2. 正式实例绑定

D 使用与业务输入一致的正常构造：

```python
formation, q_feature, _validity = make_features(**PARAMS)
```

并且只将第二项 `q_feature` 作为本定义目标。参数固定为：

```yaml
sof_name: TA_updto20240229_DBA
block: steel
calendar: night_end_at_2300
freq: 5m
symbols: [rb, hc, i]
delta: 600
direction: DirectionUp
retrace_pct: 0.5
check_retrace_pct: 0.5
membership_line: 0.5
spec_term: M
distance_times: 100
x_step_times: 0.1
overlap: 0.2
source_core_multiples: 30
```

`formation` 是同一正常构造中的正式 F，只用于 Q 的必要上游和准确 candidate 追溯；V 不属于本 D 定义，也不会被运行。

### 2.1 默认读取，不暗中重跑

默认命令：

```bash
python q_caegraph_definition.py --mode read
```

`read` 会先检查准确 F/Q 实例目录中的 `fields.json`。不存在时直接失败，不会为了填满图而暗中运行全历史 producer。

只有 Owner／后继明确授权全期重新生产时，才允许：

```bash
python q_caegraph_definition.py \
  --mode rerun \
  --allow-full-period-rerun
```

该模式先生产准确 F，再生产 Q；不会生产 V。

---

## 3. B 观察位置的真实绑定

B 当前有效合同：

```text
TA_updto20240229_DBA / steel / night_end_at_2300
5m / rb,hc,i / 2021-01-01～2022-12-31
```

D 绑定为：

```python
OptContext(
    sof_name="TA_updto20240229_DBA",
    stk_tlist="steel",
)

PlotSet(
    calendar_name="night_end_at_2300",
    blk=["rb", "hc", "i"],
    timespans=[
        ("2021-01-01 00:00:00", "2022-12-31 23:59:59")
    ],
)
```

结束日期被具体化为当日 `23:59:59`，使锁定 `PlotCtx` 的 `timesearch + end_uti += 1` 行为包含完整结束日；这没有修改 B 的位置选择，也没有修改 SOF 的 `startDay/endDay`。

本次不是高频多尺度位置路径，未调用 `MultiScaleLayout`。

---

## 4. A 字段怎样进入真实代码

## 4.1 正式 F candidate

从 Q 的正式必要上游读取：

```text
occurrences
occurrences_groupMembers
```

每个 Q revision 的 `candidateReference` 必须在正式 F exact 集合中存在；不存在时脚本失败，不会生成伪造上游事件。

## 4.2 Q identity 与 revision

从正式 Q 表读取并保持：

```text
organizationReference Life / Revision
organizationPrevious
organizationCandidate exact
organizationKnownFrom
```

同一 Q Life 的 `Previous` 只形成 revision segment；显式 duty end 不进入 revision chain。

## 4.3 Q 组级状态和观察界

绑定：

```text
qualification
observation
applicability
original/current anchor
deadline
revisionEnd
```

状态只在真实 `DirectionalOccurrence` 的正式 publication firing 上发表，不在两个 revision 之间合成 occurrence。

## 4.4 成员多位置

每个 member 保留：

```text
asked actual / price / confirmation / known / clock
used actual / price / confirmation / known / clock
successor actual / price / confirmation / known / clock
endpoint actual / price / known / clock
through
materialKnown
missingRange
completion
verdict
basis
pathComplete
```

各位置不合并成单一“发生时间”。成员表行仍然是 Q occurrence 的 payload，不被提升成独立业务 occurrence。

## 4.5 六量与缺失

每个 member 每版 Q 固定验证六类：

```text
ProgressP
AmplitudeA
DurationD
PathLengthL
EfficiencyE
CounterC
```

缺失时只保留真实 availability：

```text
EndpointUnavailable
ClockUnavailable
PathUnavailable
ZeroPathNotApplicable
```

禁止把缺失写成 `0`。六量单位不同，因此图中使用类别轨；原数值与 availability 放入 hover。

## 4.6 显式 lifecycle end

A 和 C2 要求显式 `DirectionalDutyEnd`。当前锁定 TIS v2 wrapper 的字段 registry 未公开 duty-end 表，但 FRP 锁定存储结构唯一规定：

```text
organizationEndLast
organizationEndReason
organizationEndKnown
organizationEndProgress
```

D 因而使用同一锁定 layout 的 `_event_df` 直接投影这些正式存储字段。该适配只适用于当前准确 `tis@2f460d / frp@67711c` 组合，并保留：

- 最后成功准确 Q；
- 准确 F candidate；
- end reason；
- end known；
- end progress；
- “不创建新 Q revision”的事实。

---

## 5. CAEGraph 仓库调用链

D 已按锁定版本：

`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad`

读取并采用：

```text
CAEGraph使用手册.md
__init__.py
utlv2.py
utkv2.py
pfw.py
pdt.py
core/__init__.py
core/utils.py
dynstd.js
fit_y_range.js
multiscale.py
```

本次实际调用链：

```text
CAEGraph.produce_widgets
→ PlotSet.plot
→ PlotCtx(SOF / Calendar / symbols / timespan)
→ AllSymsMainFig / AllSymsFig / PerSymFigSet
→ MainFig / SubFig
→ KPriceLine / custom BasePlotter
→ ColumnDataSource + Bokeh glyph
→ PlotDataFolder / PlotDataNode
```

### 5.1 数据进入图元

- `KPriceLine` 从 `KLine(freq='5m').rerun().to_df()` 读取 OHLC 和 UTI；
- overview 使用 ratio DynStd；
- member 价格图元注册为被同一 entity DynStd 驱动；
- per-symbol detail 保留 raw OHLC 和 raw member price；
- Q/F 公共表经 adapter 变为六张 canonical frames；
- custom plotter 的每一个 CDS 均通过 `ctx.add_cds(...)` 注册。

### 5.2 构图数据树

C3 原代码直接创建 custom CDS，未登记 `PlotDataNode`。D 已唯一纠正为：

```python
cds = ColumnDataSource(data)
ctx.add_cds(name, cds, 0.0, 0.0)
```

E 运行后，入口脚本会导出：

```text
canonical_frames_manifest.json
canonical_<frame>.csv
plot_data_manifest.json
每个 PlotDataNode 的 CSV
q_caegraph_run_report.json
```

这样后续不仅能看 HTML，也能正式取得构图数据。

---

## 6. C2 到 D 的逐层保持

| C2 | D 定义 | 保持的业务边界 |
|---|---|---|
| P1 多品种价格总览 | `AllSymsMainFig + KPriceLine(ratio) + QMemberGeometryPlot` | ratio 只是显示派生；raw 证据仍在各品种图 |
| P2 F→Q→end | `AllSymsFig + QLifecyclePlot` | exact F、Q Previous、显式 end 分开；end 不造 revision |
| P3 组级状态 | `AllSymsFig + QStatePlot` | qualification／observation／applicability 只随真实 Q revision 发表 |
| P4 成员事实 | `PerSymFigSet + raw KPriceLine + QMemberGeometryPlot + QMemberAuditPlot` | asked／used／successor／endpoint 分开；缺失原因保留 |
| P5 exact audit | `AllSymsFig + QAuditPlot` | Q/F exact、Previous、known、last successful 和 end 完整可追溯 |

D 没有改变 C2 的页面、面板、图元含义、转换方式或业务阅读方式。C2 中的 `T0..T11`、`Q-L7/F-L7` 和示意数值全部被正式实例数据替换，不会进入真实输出。

---

## 7. 上游确定性纠正记录

| 编号 | 来源 | 修正 | 是否改变业务选择 |
|---|---|---|---:|
| `D-CORR-001` | C3 | custom CDS 全部登记至 PlotDataTree | 否 |
| `D-CORR-002` | C3／锁定 TIS | 版本锁定读取正式 duty-end 存储字段 | 否 |
| `D-CORR-003` | B | 日期边界具体化为完整结束日 timespan | 否 |
| `D-CORR-004` | C3 | `price_feature` 绑定为同尺度 raw `KLine(freq='5m')` | 否 |

四项修正都满足：结果唯一、不改变 B 最终看哪里、不改变 C2 怎样展示、不引入新的业务判断，并已在机读产物中逐项记录修正前、修正后和证据。

没有需要退回 A、B 或 C 的不确定问题。

---

## 8. 定义级检查

检查记录：

`daowei2026/observe-iterate@78b306ae3dba130b4bd1015befdebe19090ac728:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_DEFINITION_CHECKS.json`

已真实重跑并通过：

1. 九个发布模块的 SHA-256 与检查记录一致；
2. 九模块全部通过 `py_compile`；
3. 九模块全部通过 AST 解析；
4. 在隔离 stub 环境中九模块可完整导入；
5. 合法空 canonical frames 通过 `QDisplayFrames.validate()`；
6. 没有未替换的注入占位、`TODO`、`FIXME` 或 `NotImplemented`；
7. exact instance、B position、A field、C2 panel 和 PlotDataTree 均进入真实代码；
8. 默认读取模式不会暗中 rerun。

### 8.1 没有做的检查

D 没有在 `/dwdhome/fy/BASE_E6_2_copy`：

- 导入真实 mquant/tis/uplot；
- 读取真实 F/Q `fields.json`；
- 执行真实表 adapter；
- 生成真实 Bokeh HTML；
- 验证动态标准化、hover、JS 或资源消耗。

这些正是 E 的真实运行、检视和交付范围。

---

## 9. 给 E 的直接执行合同

### 9.1 先只读验证正式数据

```bash
cd longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D
python q_caegraph_definition.py --mode read --validate-only
```

### 9.2 只读并生成正式 HTML／取图数据

```bash
cd longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D
python q_caegraph_definition.py --mode read
```

预期输出：

```text
longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH.html
longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH_DATA/
```

如准确实例没有既存正式输出，read 模式应失败，并由 E 按真实权限和 Workflow 决定后继；不能无痕改成 rerun。

---

## 10. Worker 与权限

D Skill 明确不派 Worker。本次：

- 没有签发 Worker；
- 没有接受或虚称 Worker Return；
- 没有写出本 Run 目录；
- 没有执行全历史 producer；
- 没有启动 V；
- 没有把 F 的历史观察成果计入 Q。

---

## 11. 完成判定

| D Skill 完成条件 | 实际结果 |
|---|---|
| 锁定 CAEGraph 仓库调用链已理解 | 是 |
| 外层真实 Q 实例已正式绑定 | 是 |
| B 位置进入真实代码 | 是 |
| A 身份、时间、成员和数值字段进入真实代码 | 是 |
| C2 展示语义未无痕改变 | 是 |
| 拿得准的 B/C 缺项已唯一纠正并留痕 | 是 |
| 不确定问题未被猜测 | 是；无待退回问题 |
| 完整可执行定义已发布 | 是 |
| 定义级检查已通过 | 是 |
| 与 E 真实运行清楚分开 | 是 |
| 剩余 D 范围 | 无 |

**D 阶段状态：完整。**
