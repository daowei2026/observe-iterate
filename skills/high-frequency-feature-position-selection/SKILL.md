---
name: high-frequency-feature-position-selection
description: 在观察材料准备流程第 3A 步，对需要分层查看的高频特征，按 aidata 已有 big/mid/small/tick 定位、图页组合及真实取数方式确定位置和落地方案。初版只复用已核实做法，不要求执行 Agent 重新设计选位规则。
---

# 高频特征的分层观察与位置选择（初版 Skill）

**调用位置**：\`control/02_L1_观察材料准备流程.md\` 的条件步骤 3A，使用该流程第 1～3 步已经明确的观察对象、要观察的特征及材料要求。第 4～6 步仍负责实际落地、取得数据和核验；本 Skill 不替代它们。

**初版方法来源**：\`daowei2026/aidata@9ff7ce4929b36945f63b1c9875e59f68141f997a\`，重点为 \`profiles.py\` 的 \`standard_multiscale\` v4、\`timespan_builder.py\`、\`big_world_chart.py\`。完整、可逐项查验的默认参数与绘图实现，见 [aidata 四层选位与 CAEGraph 落地对照](references/aidata四层选位与CAEGraph落地对照.md)。引用的是**已核实的实现**，不是要求执行 Pro 每次重新研究整个 aidata 仓库。

## 1. 何时使用，做完什么

本轮高频特征的输入或输出需要观察到很细的时间尺度，且在本次时间范围内发生次数多，直接把整个范围全部画成细粒度图不适合阅读或取数时，使用本 Skill。其余情况不强制执行；已指定具体时间位置时，可直接用该范围，无须先重做多年概览。

本 Skill 的任务仅是：**用 aidata 已有定位特征与参数，得到 big→mid→small→tick 的时间窗，并按已有的多页面 CAEGraph／Bokeh 组织方式提供观察图的落地方案**。不另创造“值得关注”“典型”“代表性”之类自动评分或选样规则，也不负责根据图判断目标特征是否合理。

只沿用下列已有称呼：

- **定位特征（anchor）**：提供实际转折位置，供程序生成观察时间窗；不等于本轮需要判断合理性的目标特征。
- **观察特征（evidence_features）**：步骤 1～3 已经确定要看的特征，在相应图上显示，并在需要时按窗口取得其实际输出；与定位特征各司其职。
- **big／mid／small／tick**：aidata 时间窗树中的四级节点，**不是四张 CAEGraph 图**；每个节点有来源、父节点及起止时间。
- **timespan**：一个节点对应的时间范围；图和数据切片都必须引用同一个已形成的时间窗，不在绘图时重新定位。

## 2. 执行前直接取得的输入

从前述步骤和真实运行环境取得：观察品种或板块、使用的日历、真实数据源及可用范围、观察特征的源接口与真实字段、已有图或运行结果、Owner 给出的时间范围或位置。**这些输入已确定的就直接使用，不重新让 Owner 填另一份表。**

先检查是否已经有在同一代码／数据／日历／参数约束下可复用的 aidata 时间窗或 CAEGraph；有则按其真实身份直接使用。没有时使用下一节默认选位配置。

特别注意：aidata 的**平台标准 Profile**是以登记过的板块 \`blk@...\` 为入口，绑定特定历史数据范围，不能直接宣称适用于任意 EAW Wall 单品种实例。若本轮真实对象或数据源不同，应在该实例真实 \`context\`、\`blk\`／品种集合和日历下，用公开 \`run_brief_input\` 配置**同一套定位特征、字段与参数**，而不是照抄 Profile 的历史 Sof 或日期。若真实源接口不支持这套定位，不自行更换业务特征或编造字段；记录实际缺口并交原流程处理。

## 3. 固定的四层定位规则

按下表依次使用 aidata 的现有定位特征，不另外构造一种“Wall 专用定位器”：

| 节点 | 真实定位特征 | 读取的实际位置字段 | 节点对应的细看尺度 |
|---|---|---|---|
| \`big\` | \`ZigConfirm(ZigZag(KLine('30m') close, retracePct=10))\` | \`zigUTI\` | 30m |
| \`mid\` | \`ScaleTurnCalendar('large')\`（30m 的 L 贴近转折） | \`x\` | 1m |
| \`small\` | \`ScaleTurnCalendar('mid_1m')\`（1m 的 M 贴近转折） | \`x\` | 5s |
| \`tick\` | \`ZigConfirm(ZigZag(KLine('1m') close, retracePct=0.4))\` | \`zigUTI\` | 半秒 tick 盘口 |

上述是现有 \`standard_multiscale\` v4 的初版默认，不是重新为目标特征推导的最优参数。对 ScaleTurn，DataFrame 索引可能是**确认时间**，\`x\` 才是**实际位置**；不得拿确认时间代替定位字段。Zig 同理使用 \`zigUTI\`。

按 \`timespan_builder.extract_timespans_by_actual_position_fields\` 及 \`identify_uti_segments\` 处理实际位置：按 \`n_inter\` 分段，增加 \`n_margin\` 前后余量，用 \`n_max\` 限制长度；在 big 内产生 mid，在 mid 内产生 small，在 small 内产生 tick；tick 窗口按现有代码裁到父 small 范围并合并重叠段。**不要另实现一套分段、排序或“重要程度”筛选算法**。四层现有参数数值及上限原样列在 [对照文件](references/aidata四层选位与CAEGraph落地对照.md)。

节点数量达到 \`limits\` 上限时，必须保留实际截断记录；上限只是执行限制，不表示留下的节点最有代表性。

## 4. 两种进入方式，不额外发明选择规则

**A. 本轮已有明确时间范围**：该范围直接作为 \`big_source.search_timespans\`（或使用已存在合格节点的时间窗），按上述四层定位依次展开。不必先运行多年全局概览。

**B. 本轮只有宽泛历史范围、没有要展开的局部**：先按现有 \`overview\` 逻辑生成 **1d 全局图和 big 节点**，不同时计算整个历史的 mid/small/tick；在图上查看 big 范围。后续 \`focused\` 需明确 \`selection_start/selection_end\`，在这段范围内重新产生四层节点。

**需特别保留的真实限制**：aidata 当前的标准流程由使用者从概览选择进入 focused 的日期范围；仓库没有已经成立的“自动判断哪段历史最值得深入”的规则。如果本轮既没有明确位置，也没有人／上游实际提供 focused 日期，执行者只能交付真实 overview、big 节点及来源，**不得擅称已完成 focused 选位，更不能替业务合理性分析自造评分标准**。

focused 在选择范围内重新搜索 big，会产生新 run；仅凭 \`big_000001\` 一类名称不能把 overview 与 focused 的节点认作相同。需要核对 \`run_id\`、来源及实际时间窗。

## 5. 具体怎样落地 CAEGraph／图页面

严格区分**四层时间窗**和**多张图**，照搬 aidata 的已有图组织结构（类和构图函数详见对照文件）：

1. **1d 全局概览**：\`AidataRunOverviewCAE\`；内含一个 1d \`CAEGraph\`，叠加搜索范围、big 的时间框和定位实际点。不是四层节点中的额外一级。
2. **30m—1m—5s 页面**：每个 big 使用 \`AidataBigWorldReviewCAE\`；内部分别注册 30m big、1m mid、5s small **三个 CAEGraph 定义**，按一个 big、其多个 mid、各 mid 下多个 small 组合为一页；图中标出子时间范围与定位点。
3. **1m—5s—tick 页面**：每个 mid 使用 \`AidataMidTickWorldReviewCAE\`；1m、5s 使用**两个 CAEGraph 定义**，每个 tick 时间窗的半秒盘口用 \`_build_tick_l1_figure\` 等独立 **Bokeh** 绘制函数按需读取真实一档数据，不是又一个 CAEGraph 定义。页面含当前 mid 的 small 和各 small 下的 tick 盘口图。

CAEGraph 中按当前 \`timespan_index.csv\` 指定 \`plotsets.*.timespans\`，不得在 \`layout\` 阶段重新执行选位。相应 CAEGraph 使用 \`KPriceLine\` 的 1d/30m/1m/5s 行情作为价格参照；按目标特征已核实的数据字段与绘图合同，把观察特征叠加到相应尺度。不可把没有实现的 Wall 画法或字段编造出来。

这属于**复用现有组合方式定义观察图**，不是要求为每层、每个节点独立发明一套页面。优先直接复用已有 aidata 实现和 CAEGraph 能力；如果目标工作区不能直接复用，按 [对照文件](references/aidata四层选位与CAEGraph落地对照.md) 中的函数逐项对应实现并验收，不能把多图页面错误地压成一张 CAEGraph。

## 6. 与原第 4～7 步的交付关系

本步骤先提供：已采用的定位配置及代码版本、实际时间范围、四层节点及父子关联（若已真实生成）、需要的多图定义／复用入口、哪些图和数据尚未得到；**没有实际运行时，只能说明设计，不得宣布真实数据就绪**。

第 4～6 步按原 Skill 负责调用已有代码、真正取得和检查材料：

- 看图入口：\`build_chart_run\` 产生 \`manifest/timespan_index.csv\`、\`source_occurrences/\`、\`chart_manifest.csv\`；\`build_run_overview_chart_page\` 或 \`build_big_world_chart_pages\` 取得对应图 URL。
- 数据切片：需要正式证据时，在同一批时间窗调用 \`build_board_run(..., reuse_core=True)\` 获取真实 \`feature_slices/\`、\`delivery/\`；图层共享视图 \`plot_view_data/\` 不能替代源特征切片。
- tick：创建链接不等于已经读到 tick 盘口；tick 图在实际打开页面时按需读取，半秒盘口 CSV 另按需导出。缺读数、链接打不开或核验失败如实报告。
- 记录 \`run_id\`、\`node_id\`、\`parent_node_id\`、实际时间窗、实际用到的定位特征/观察特征/日历/数据源与版本、图 URL、成功或失败及截断范围；再由原第 6、7 步检查和交接。

**禁止**以人造行情或合成窗口代替本轮真实业务数据；禁止用图的显示扩展范围代替实际数据切片范围；禁止在 3A 提前作高频特征合理性判断。

## 7. 何时仅交缺口，不自行改变方法

如果当前实例缺必要定位特征的真实结果、无法访问所需历史数据或缺目标特征的已实现画法，先在原第 4～5 步范围内按真实接口定向查证。仍不满足时，报告缺的是哪一层的哪项输入和对本轮的影响；**未经新的上游事实与授权，不替换定位算法、静默缩短时间范围或宣称新方案已验证**。

本 Skill 是当前 aidata 方法的**初版复用**，不是对 Wall 特征作出的正式位置筛选标准，也没有证明图上的所有节点都足以回答全部业务问题。具体合理性判断仍归后续合理性分析。
