# C｜PostTurnGroupDirectionalOrganizationFrp CAEGraph 展示方式准备

## 0. 产物身份与结论

| 项目 | 值 |
|---|---|
| run_id | `OI-U2-Q-OBS-20261120-01` |
| work_item_id | `OI-U2-Q-OBS-20261120-01-WI-C` |
| stage_instance_id | `OI-U2-Q-OBS-20261120-01-M-C` |
| delegation_id | `D003` |
| 执行身份 | `chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1` |
| 特征 | `PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织） |
| 阶段状态 | **完整** |
| Worker | **不需要；未签发** |

本 C Skill 已按内部 C1、C2、C3 完成：

1. 从 A 当前有效产物整理待展示信息；
2. 读取锁定版 CAEGraph 手册与必要源码；
3. 发布第一版可打开 HTML；
4. 对复杂点完成一轮展示能力核对和方案修订；
5. 发布当前唯一预期 HTML；
6. 从当前方案整理出可由 D 注入实例、字段与 B 位置的真实 CAEGraph Python 代码。

本阶段没有运行 Q，没有用示意图冒充真实行情结果，也没有把 B 的当前位置固化进 C3。

---

## 1. 当前原生产物

| 产物 | 精确引用 |
|---|---|
| C1 待展示信息机读清单 | `daowei2026/observe-iterate@781865309218623fecb355a2c6bb826de08cf735:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C1_DISPLAY_INFORMATION.json` |
| C2 确定性预览生成器 | `daowei2026/observe-iterate@5a1ecd7efaa4c176b262a0104fd2d87f79f6e4f3:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_preview.py` |
| C2 第一版 HTML | `daowei2026/observe-iterate@36f88213832fe1ea90b29cecd47c0825e50ddf34:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED_V0_1.html` |
| C2 当前唯一预期 HTML | `daowei2026/observe-iterate@85b41da60713f7ed2824b104bff614478c0f9371:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED.html` |
| C3 可注入 CAEGraph Python | `daowei2026/observe-iterate@435c2ed129ba7596b9d5a102bc0d8bf6104729ba:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_injectable.py` |
| C3 注入合同 | `daowei2026/observe-iterate@747ce755d95e9354dd13209c41ba053d219febe1:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C3_INJECTION_CONTRACT.md` |
| C 阶段机读汇总 | `daowei2026/observe-iterate@42a603fc8d209ea1bed7870c7b298f99a2785782:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.json` |

---

## 2. C1｜待展示信息

C1 直接消费 A 的当前有效产物：

- `daowei2026/observe-iterate@bf50bbe5c9447cb992af547e3f5f95f7465cae88:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- `daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

### 2.1 必须常显或可直接展开的信息

| 信息 | 为什么要展示 | 必须保持的语义 |
|---|---|---|
| 多对象原价和 Calendar 背景 | 成员方向运动必须回到 `rb/hc/i` 的实际价格路径核对 | actual、known、clock 不能混同 |
| F candidate exact | Q 的问题身份、成员和上游修订来自 F | F Life/Revision 与 Q Life/Revision 分开 |
| Q `DirectionalOccurrence` | Q 的业务主输出 | 一点代表一个完整组观点，不是一个成员行 |
| Q Previous 修订链 | 说明同一道 Q 怎样被修订 | Life 不变、Revision 变化、Previous 指向上一准确 Q |
| qualification / observation / applicability | 说明每版观点当前怎样解释整个组 | 状态属于该 Q occurrence，不是另一个 Event |
| 成员 asked / used / successor / endpoint | 说明量测基础、修订依据、完成与真实端点 | 各位置和各自 actual/confirmation/known 均可审计 |
| verdict / completion / basis / path | 直接解释成员为何支持、反证、未决或缺件 | `path_complete=False` 不等于方向失败 |
| 六类 quantity 与 availability | 解释成员量测结果 | 缺失不是 0；不同量不共用一个数值轴 |
| `DirectionalDutyEnd` | 真正表达一个已发行 Q Life 的责任结束 | 显式 occurrence；引用最后成功 Q；不造新 revision |

### 2.2 条件显示或元数据显示

- source frame 的 `progress / known / ended / patch / coverage` 摘要；
- subscription 的原始与当前 `anchor / deadline / revisionEnd` 及 closed 状态；
- definition 的方向、Δ、观察倍数、修订倍数、最少成员和 binding。

这些信息用于解释 Q 的修订、收紧和结束，但不值得机械地各自占一张主图。

### 2.3 不单独画成业务事件的信息

- `DirectionalFrame`：只负责对齐三类输入；
- `DirectionalBatch`：只是同一 firing 的发行批次；
- `DirectionalOrganizationRecord`：正式存储 envelope；
- definition：固定元数据；
- members 表的每一行：Q occurrence 的嵌套 payload。

这避免了“正式保存了，所以就是业务主输出”的错误。

---

## 3. C2A｜CAEGraph 能力核对

### 3.1 锁定依据

- `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`
- 同 commit 的 `utlv2.py`、`utkv2.py`、`pfw.py`、`__init__.py`

### 3.2 直接采用的现有能力

```text
CAEGraph
→ PlotSet
→ AllSymsMainFig / AllSymsFig / PerSymFigSet
→ MainFig / SubFig
→ KPriceLine / custom BasePlotter
```

已确认：

- 多图共享 x-range；
- 图例可点击隐藏；
- `KPriceLine` 可画 raw 或 ratio 显示派生；
- `AllSymsMainFig` 可把多个品种放在一个总览；
- `PerSymFigSet` 可为每个品种生成 raw 主图和审计附图；
- `BasePlotter` 是合法扩展点，可直接使用 Bokeh point、segment、text 和 hover。

### 3.3 不能直接照搬的地方

内置 `MulFieldsGlyphs` 的默认 hover 主要提供时间和 y 值，无法完整承载：

- Q/F exact；
- Previous；
- qualification / observation / applicability；
- verdict / basis / availability；
- duty end 的 last successful Q。

因此没有强行把所有字段塞进通用 plotter，而是使用薄的自定义 `BasePlotter`：

```text
QLifecyclePlot
QStatePlot
QMemberGeometryPlot
QMemberAuditPlot
QAuditPlot
```

这属于锁定版 uplot 已支持的扩展方式，不是要求新增 uplot 核心功能。

`SeqOfFieldsPlot` 在手册中缺少本 Q 嵌套公共表可直接验证的完整例子，本阶段不押注该类。嵌套表由 D 的 adapter 根据真实父子坐标和 identity 展开为 canonical frames。

---

## 4. C2B｜第一版展示预期

第一版 HTML：

`daowei2026/observe-iterate@36f88213832fe1ea90b29cecd47c0825e50ddf34:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED_V0_1.html`

第一版完成了：

- 多品种 5m 价格总览；
- F candidate、Q revisions、duty end 三条生命周期语义；
- Q 组级状态表；
- 三个成员的运动与六量卡片；
- 页面层次和共享时间轴的可打开验证。

第一版明确使用确定性示意数据。它不是 Q 的运行结果，也没有选用 B 的真实位置。

---

## 5. C2C / C2D｜复杂点、修订与当前展示预期

### 5.1 第一轮发现的复杂点

1. **一个 Q occurrence 有多个成员和多类位置。** 不能只在一个时间点放一个标签就认为表达完整。
2. **publication、known、actual、confirmation、endpoint、Calendar 不同。** 不能统一压成“发生时间”。
3. **Q revision 和 duty end 不同。** end 不能画成下一 Q revision。
4. **没有新 Q 不等于失败或结束。** 图的空白区不能自动上色成负面。
5. **多品种价格尺度不同。** 总览需要 ratio 显示派生，但 raw 价格仍需逐品种保留。
6. **六量单位不同且有缺件。** 不能在同一 y 轴上比较数值；必须保留 availability。
7. **精确身份字段太多。** 常显图元会过载，需要 hover 和审计明细分层。

### 5.2 当前修订

当前 HTML：

`daowei2026/observe-iterate@85b41da60713f7ed2824b104bff614478c0f9371:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED.html`

相对第一版增加：

- 可见的 Q Previous segment；
- F candidate、Q revision、duty end、成员位置的开关；
- asked / used / endpoint 与价格路径的对齐；
- `PathUnavailable` 等缺失原因；
- Q/F identity、Previous、publication/known 和 end 语义的独立审计面板；
- 明确声明 ratio 只是显示派生；
- 明确声明视觉延续不是合成 occurrence。

### 5.3 当前五层展示结构

| 层 | 内容 | 主要阅读问题 |
|---|---|---|
| P1 | 多品种 ratio 价格总览 + 成员位置 | 这组成员的价格路径怎样分化？ |
| P2 | F candidate → Q revision → explicit duty end | 同一道问题何时形成、如何修订、何时真正结束？ |
| P3 | qualification / observation / applicability | 每一版 Q 对整个组的判断是什么？ |
| P4 | 各品种 raw K + asked/used/successor/endpoint + verdict/六量 | 每个成员为什么支持、反证、未决或缺件？ |
| P5 | exact refs / Previous / known / end audit | 图上的判断能否追到准确身份、版本与位置？ |

当前 C2 没有阻塞展示缺口。

---

## 6. C3｜可注入 CAEGraph 代码

代码：

`daowei2026/observe-iterate@435c2ed129ba7596b9d5a102bc0d8bf6104729ba:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_injectable.py`

注入合同：

`daowei2026/observe-iterate@747ce755d95e9354dd13209c41ba053d219febe1:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C3_INJECTION_CONTRACT.md`

### 6.1 D 注入边界

```text
QDisplayBinding
├─ q_feature
├─ price_feature
├─ frame_adapter
├─ field_binding
└─ QPositionBinding
   ├─ sof_name
   ├─ block
   ├─ calendar_name
   ├─ objects
   └─ timespans
```

因此 C3 没有固化：

- B 的默认日期；
- `steel` 或 `rb/hc/i`；
- `TA_updto20240229_DBA`；
- `night_end_at_2300`；
- 本 Run 的具体 `q`；
- 结果目录。

### 6.2 canonical frames

D 的 adapter 输出：

```text
timeline
revision_links
states
members
quantities
audit
```

这些 frame 明确保留：

- Q/F identity；
- Previous；
- publication 和 known；
- asked / used / successor / endpoint；
- verdict / completion / basis / path；
- quantity raw value 与 availability；
- explicit duty end 与 last successful Q。

### 6.3 C2—C3 对应

| C2 | C3 |
|---|---|
| P1 | `AllSymsMainFig + KPriceLine(ratio) + QMemberGeometryPlot` |
| P2 | `AllSymsFig + QLifecyclePlot` |
| P3 | `AllSymsFig + QStatePlot` |
| P4 raw | `PerSymFigSet + MainFig + KPriceLine(raw) + QMemberGeometryPlot` |
| P4 audit | `PerSymFigSet + SubFig + QMemberAuditPlot` |
| P5 | `AllSymsFig + QAuditPlot` |

已通过 `py_compile`，并完成无硬编码 SOF、对象、日期、Q 实例的静态检查。

---

## 7. B 位置处理边界

B 当前有效合同仍为：

```text
TA_updto20240229_DBA
steel
night_end_at_2300
5m
rb / hc / i
2021-01-01 ～ 2022-12-31
```

C 只证明代码能够接收这类位置，不在 C2/C3 中把它变成最终 timespan。后续 D 必须正式消费 B，并根据 Calendar 与 PlotSet 决定日期边界和实际 `timespans`。

---

## 8. Worker、运行与事实边界

本次没有签发 Worker，也没有接受 Worker Return。

理由：C 的原生工作是展示信息整理、展示方式迭代和可注入代码形成；这些可以由锁定代码与手册完成，不需要在 Linux 上运行特征。

已经完成：

- 两份 HTML 结构解析；
- Python 语法检查；
- 注入点静态检查；
- C2 与 C3 逐层对应检查；
- capability gap 判断。

没有声称：

- 在 `/dwdhome/fy/BASE_E6_2_copy` 真实运行；
- 读取真实 Q 数据；
- 生成最终 D/E HTML；
- 验证目标环境全部依赖。

这些属于 D 的实例/字段/位置正式绑定和 E 的真实运行、检视与交付。

---

## 9. 完成判定

| C Skill 完成条件 | 结果 |
|---|---|
| 已整理输入、主输出和必要中间结果的待展示信息 | 是 |
| 已先形成第一版显示预期和 HTML | 是 |
| 已识别复杂点并做展示能力核对 | 是 |
| 已完成至少一轮修订并发布当前唯一 HTML | 是 |
| 已形成可注入的真实 CAEGraph Python | 是 |
| C3 与当前 HTML 的图层、字段和语义一致 | 是 |
| B 最终位置仍留给 D 注入 | 是 |
| 存在阻塞 capability gap | 否 |
| 存在剩余 C 范围 | 否 |

**C 阶段状态：完整。**
