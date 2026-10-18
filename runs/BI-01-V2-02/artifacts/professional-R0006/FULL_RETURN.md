# BI-01-V2-02 R0006 专业回交：场景先行 S1 实质结果、SCN-01 固定数据预分析与 S2 连续施工入口

invocation_id: `BI01-V2-02-R0006-20261018T154801Z-a5ec3f46`  
assignment_token: `BI01-V2-02-PRO-S123-d03493944588440c883e80e9de243050`  
role: `professional`  
professional_mode: `OBSERVATION_SCOPE`  
work_status: **IN_PROGRESS**  
route: `same_work / CONTINUE`

<a id="delivery"></a>
## 1. 本轮交付状态

本轮完成了新的 `BI-01-V2-02` 第一次实质专业推进：

1. 真正取得全部 Binding 指定业务正文和两份固定 ZIP；
2. 不先查看 C1/U3 候选结果，从 rb/i/hc 全范围基础 KLine、small Zig、mid 贴近转折自主搜索位置；
3. 形成六个具名场景、搜索覆盖、后验边界、主要反例、第三对象及可执行问题；
4. 对唯一完整参考 Case 的五个合法 As-Of 做了 U2/U3/C0/N 结构化预分析；
5. 完成四束设计字段到固定数据字段的资格映射；
6. 签发六场景 aidata 图与同源数据 Worker 工单。

本轮没有完成 S2 实际出图、真实浏览器渲染和 aidata 同源数据导出，因当前执行上下文没有 `/dwdhome/fy/BASE_E6_2` 运行工作区，也没有可控制的连接浏览器上下文。故不得宣称首个 S1—S3 闭环、RESULT 触发或完整任务完成。

<a id="result"></a>
## 2. 本轮专业结果

### 2.1 当前最重要的业务认识

基础行情已经给出三类彼此不能混同的问题：

- **同一 actual turn、整组强或整组弱**：U2 可以组织共同机会身份，但不能替代 U3 质量；
- **同一/近邻共同启动、成员后续分化**：需要在合法 As-Of 下区分 Progress、Friction、Retention 与 Observability，而不能事后选赢家；
- **第三对象应入还是应出**：exact-UTI baseline 既可能漏掉错时共同启动，也可能正确排除反向对象，不能一概放宽或一概收紧。

唯一完整参考 Case 支持 U2 保留“原共同机会中的 member-episode identity”这一组织价值；但在“当时谁还在延伸”这个较窄问题上，C0/N 与原 KLine 已经暴露主要差异，U3 的独立投资知识增量尚未证明。

### 2.2 当前资格边界

- 六个位置全部是回顾性发现，只能作为研究 Case，不能声称提前识别；
- 304 个 exact-UTI C1 行仍是 raw/reference candidate，不是 304 个正式 OpportunityCluster；
- SCN-01 的 R02 仍是 objective facts/reference；R03 的正式 Quality/Capital Use 全部 `WITHHELD`；
- 本轮没有正式 U3、H1、Allocation Evidence 或资金动作；
- broad scenes 没有完整 U3，缺失只能记为 Unknown/Missing，不能写成 Negative。

<a id="completed"></a>
## 3. 已完成的实质范围

- 固定上游包 SHA256：`4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`；
- 固定下游包 SHA256：`7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`；
- 三品种各 9,080 根 30m KLine，统一覆盖 `2021-01-04 09:30:00`—`2024-02-29 15:00:00`；
- mid ScaleTurn 1,457 条：rb 363、hc 342、i 752；
- 全范围独立重建 exact-UTI 同方向组 304 个，其中两成员 205、三成员 99；
- 三品种同方向、1—4 bar 近邻但非 exact 的组合 125 个；
- 六个场景的 4/12/24/48 bar 基础路径事实；
- SCN-01 五 As-Of 的 R02/N 可比视图和专业预分析；
- 四束与固定字段对应；
- 六场景 S2 Worker 工单。

固定上游存在 12 根共同空 OHLC，范围为 `2023-03-10 21:30`—`2023-03-13 15:00`；六个入选场景均不穿过该缺失段，故当前结论未受其直接影响。

<a id="s1"></a>
## 4. S1：基础行情搜索、选择与问题形成

### 4.1 搜索顺序

本轮没有用 U2/U3 输出选答案，实际顺序为：

1. 只读 KLine、small Zig、mid ScaleTurn；
2. 全范围扫描 12/24 bar 的共同方向与成员差异；
3. 用 actual turn 的 exact/near-time 结构作可复核指针；
4. 导出 4/12/24/48 bar 的简单路径事实；
5. 场景冻结后才对照 C1、C0/N 和单一完整参考 Case。

方法核对中确认：方向必须由 confirmed Zig 的 `swingStatus` 映射，不能用 `confirm_value - actual_value` 猜方向；最终全部场景与路径事实均采用正确方向口径。

### 4.2 六个场景

| 场景 | 基础位置 | 方向与成员 | 共同可知 | 回顾性路径事实 | 主要问题 |
|---|---|---|---|---|---|
| `SCN-01` | 2021-04-30 15:00 | Up；hc/i/rb exact | 2021-05-06 10:00 | 24-bar 成员中位 +6.95%，范围 7.46pct | 同一机会身份与不同成员 Episode 生命周期 |
| `SCN-02` | 2021-05-18 09:30 | Down；hc/i/rb exact | 2021-05-19 14:00 | 三者约 +10.27%—+10.73% | 整组强且接近时，U3 是否有增量 |
| `SCN-03` | 2021-11-08 10:30 | Up；hc/i/rb exact | 2021-11-08 21:30 | 24 bar 后三者约 -4.66%—-5.14% | 共同启动但整组失败 |
| `SCN-04` | 2021-11-19 14:00 | Up；hc/rb exact；i 第三对象 | 2021-11-19 15:00 | hc/rb +4.04%/+5.11%，i +12.55% | 组外对象后来更强，成员边界是否合理 |
| `SCN-05` | 2021-10-27 22:00—23:00 | Up；i/rb/hc 近邻 2 bar，非 exact | 2021-10-28 15:00 | rb/hc +1.63%/+2.30%，i -7.91% | exact-UTI 是否漏掉错时共同启动；当时能否分辨弱成员 |
| `SCN-06` | 2021-07-30 15:00 | Down；hc/rb exact；i 第三对象 | 2021-08-02 11:00 | hc/rb +9.22%/+8.84%，i -2.60% | 支持排除第三对象，反驳静态三品种绑定 |

这些百分比只是统一以各自起点归一化的回顾性搜索事实，不是正式 U3 字段、策略收益或资金结论。

### 4.3 场景覆盖的正反面

- `SCN-01`：完整参考链，检验 U2 identity 与 U3 lifecycle；但 closed Universe 不能检验 outsider separation。
- `SCN-02`：成员都强且接近，防止为了“必须有赢家”硬造差异。
- `SCN-03`：共同启动后整组失败，防止 U2 身份被误写成质量。
- `SCN-04`：第三对象没有 exact 同刻身份却后来更强，防止事后把赢家塞回 U2。
- `SCN-05`：近邻非 exact，检验 Formation 时间边界，而非先接受它属于同一组。
- `SCN-06`：第三对象初始反向，检验 U2 排除是否保真；后来同向不自动推翻“不是同一轮”。

<a id="remaining-s1"></a>
### 4.4 S1 后继边界

初始全范围搜索已经完成，但完整 S1 责任仍随 S2/S3 保留：只有真实图或同源数据揭示新的边界、反例、时间冲突时，再定向补场景或调整窗口；不因已有六个场景永久冻结全部观察范围，也不重新从字段列表或 raw candidate 倒推选样。

<a id="s2-prepared"></a>
## 5. S2 已准备：六场景真实图与同源数据工单

已签发 [`WORKER_AIDATA_CHART_ORDER.md`](./WORKER_AIDATA_CHART_ORDER.md)，明确：

- 原件目录 `/dwdhome/fy/资金管理`；
- aidata 工作区 `/dwdhome/fy/BASE_E6_2`；
- 统一 `run_id=BI-01-V2-02`；
- 每个场景的 `BASE` / `EVIDENCE` 节点、时间窗、As-Of、基础图层和证据图层；
- SCN-01 五个 As-Of 的 R02/N/C1/S/C2/R03 对照；
- SCN-02/03/04/06 的 C1 raw + C0/N；SCN-05 明确不伪造 C1/U3；
- `plot_view_data` 或等价正式同源导出；
- 真实浏览器 KLine/图层/缩放/DOM/Canvas 核验；
- HTTP 200 不构成渲染通过；
- 优先现有 aidata API，通用修改只允许 aidata 新独立分支；
- 六个场景全部在工单范围，首图不是停点。

<a id="s2-gap"></a>
## 6. S2 未执行及真实限制

本轮当前聊天运行环境具备固定 ZIP、本地 Python 和 GitHub 写权，但不具备：

- `/dwdhome/fy/BASE_E6_2`；
- `/dwdhome/fy/资金管理` 服务器路径；
- aidata 服务运行环境；
- 可控制的连接浏览器上下文。

Browser 连接实际返回“需要 originating browser context”，因此本轮不能验证旧图或新图的 KLine/图层真实可见。没有用本地 matplotlib/Bokeh 造第二套工具，也没有拿旧 V2-01 URL、HTTP 200 或文件存在冒充 S2 完成。

所以当前准确状态是：**工单已签、S2 未执行、同源图数据尚未取得。**

<a id="s3-preanalysis"></a>
## 7. S3 前置：SCN-01 固定参考 Case 预分析

### 7.1 U2 位置与成员

hc/i/rb 在 `2021-04-30 15:00` 具有同一 actual UTI 和 Up turn，到 `2021-05-06 10:00` 三者共同可知。将三者作为同一轮共同启动候选有基础行情支持。

但：

- `outside_count=0` / `ValidEmptyAlternatives` 只是 fixed Universe 没有 outsider，不是 External Separation 证据；
- four-gate reference 仍只是 shadow/reference；
- `official_cluster_committed=NO`、`official_h1_emitted=NO`；
- 本 Case 不能升级为正式 OpportunityCluster/H1。

### 7.2 2021-05-06：四束给出冲突而不是单一排名

三者都只观察 2 bar：

| 成员 | 净推进/起点 | 路径效率 | 最大反向/起点 | 峰值保持 |
|---|---:|---:|---:|---:|
| hc | 3.54% | 0.944 | 0.11% | 0.971 |
| rb | 4.09% | 0.932 | 0.15% | 0.965 |
| i | 4.36% | 0.821 | 0.47% | 0.902 |

i 的短期 Progress 略高，但 Friction 与 Retention 较差。事实支持四束分账，反对 raw progress 或 efficiency 单项选赢家。

### 7.3 2021-05-07：生命周期先于数值比较

- i：`Completed`，只观察 1 bar，净推进约 4.83%，efficiency 1.0；
- hc/rb：`WorkingSoFar`，各观察 14 bar，净推进约 4.87%/4.98%，efficiency 0.837/0.817。

i 的 1.0 是极短完成路径，不能和 14-bar Working 路径按同一口径排名。`episode_stage_at_cut + observed_bar_elapsed` 本身就是 ObservabilityAndConstraint。

### 7.4 2021-05-11—05-14：anchored episode 分化

- rb 在 5 月 11 日完成 33-bar episode，探索性净推进约 13.14%；
- hc 在 5 月 14 日完成 33-bar episode，约 14.04%；
- i 始终保留 1-bar Completed episode，约 4.83%。

在“原共同机会的 anchored episode”语义下，rb/hc 的持续与延伸明显高于 i。

但原始 KLine 扩展到更长固定 horizon 时，i 后来仍上涨。后续包含新的转折/Episode，不能无条件回填原 episode Retention。设计必须分开：

```text
episode-lineage Outcome
vs
fixed-future-horizon Outcome
```

### 7.5 相对 C0/N 的增量

5 月 7 日：

- R02 仍保留 i 的原机会 anchored episode：Completed，+51 quote units；
- N 已滚到 i 的当前 working episode：progress `-53.5`、efficiency `0.6646`、counter `63.5`。

由此得到：

- **已证明的增量**：稳定 member-episode identity、原机会追溯和重复暴露组织；
- **未证明的增量**：就“此刻谁仍在延伸”而言，N + KLine 已揭示主要差异，U3 是否更早、更稳定地改变选择仍需其他场景和合法 Outcome。

### 7.6 时间泄漏反例

`2021-05-18 09:30` 三品种实际出现共同 Down turn，但到 `2021-05-18 10:00` 尚未共同可知，共同可知为 `2021-05-19 14:00`。所以它不能进入 5 月 18 日 10:00 Current，只能在带明确 horizon/known time 的后续 Outcome 中使用。

<a id="bundles"></a>
## 8. 四束与固定数据的可判范围

| Bundle | 固定包可用 | 主要限制 |
|---|---|---|
| Progress | raw progress/amplitude、observed bars、runs、extreme count | raw quote unit 不可跨品种直接排名；不同 stage/window 不可同票 |
| Friction | path efficiency、max counter、runs、sign changes | 同源路径证据；缺正式 turn density/retracement burden/reversal threshold |
| Retention | achieved peak、retained fraction、return-to-origin、recovery event count | 缺 outside-region dwell、recovery time、cross-scale continuation |
| ObservabilityAndConstraint | stage、observed bars、path status、missing、actual/known、N sample status | 缺正式业务日历 duration、liquidity、capacity、cost coverage |

四类 Allocation Evidence 不在这些 Bundle 中：R03 的 Group Budget、Member Relative、Repeated Exposure、Uncertainty Holdback 正式投影均未形成；只能保留 withholding reason 与参考边界。

<a id="findings"></a>
## 9. 事实、CaseFinding、假设和问题分账

### 9.1 市场/数据事实

- 全范围存在 exact 同方向、近邻错时、整组强、整组弱和第三对象分化等多种结构；
- SCN-01 的三成员共同实际转折成立；
- SCN-01 五个 As-Of 中成员 episode stage 和观察长度显著不同；
- R03 全部 Withheld；
- broad scenes 没有正式 U3。

### 9.2 CaseFinding

- 同一机会身份不等于成员同质，也不等于高质量；
- 四束会产生合理冲突，不能合成字段票数；
- member-episode identity 有组织增量；
- exact-UTI 只是 baseline：既可能漏组，也可能正确排除第三对象；
- closed Universe 的空 outsider 不能证明 External Separation。

### 9.3 待证假设

- SCN-05 的三次近邻转折是否属于同一机会，需要图和原 Formation/Qualification 口径检验；
- SCN-04 的 i 是相邻但独立机会，还是应当进入同一更宽 Cluster，当前未知；
- U3 是否能比 N/KLine 更早、稳定地区分成员，当前只有 SCN-01 一例，尚不能确认；
- SCN-02 成员接近时，U3 可能应输出“不足以区分”，而不是制造排名。

### 9.4 设计/方法问题

- 方向判定必须采用 TurnType/swingStatus；
- 跨成员比较要显式统一单位、lifecycle 和观察长度；
- fixed horizon 与 episode lineage 必须分别定义 Outcome；
- External Separation 需真实第三对象；
- 同源指标必须按 Bundle 联合解释。

### 9.5 数据缺失，不是市场 Negative

- broad formal U3；
- outside-region dwell、recovery time、cross-scale continuation；
- liquidity、capacity、cost；
- official Cluster/H1；
- 四类正式 Allocation Evidence。

<a id="design-actions"></a>
## 10. 设计行动

### 保留

1. U2 的原机会 member-episode identity；
2. actual/confirm/asOf、Current/Outcome、Working/Completed 分离；
3. Progress/Friction/Retention/Observability 四束分账；
4. 同源证据不逐字段多票；
5. U2 身份与 U3 质量责任分离。

### 修订或补证

1. 所有跨成员展示先给可比归一化、stage 与 observed bars；
2. External Separation 改由 SCN-04/06 等真实 outsider 场景检验；
3. Retention 补 outside dwell、recovery time 和 episode lineage；
4. 明确 fixed-horizon 与 episode-based Outcome；
5. 用 SCN-02—06 检验 U3 相对 KLine/C0/N 的真实增量；
6. exact-UTI 和 near-time Formation 分开检验，不能简单放宽阈值。

### 当前有据停止

- 不从 SCN-01 导出正式 Quality/Allocation；
- 不把 `ValidEmptyAlternatives` 写成分离良好；
- 不按 raw progress、efficiency 或 retained fraction 单项选赢家；
- 不为 broad scenes 自行补算正式 U2/U3。

<a id="materials"></a>
## 11. 实际材料使用

### observe-iterate `@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080`

完整读取：

- `professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md`
- `professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md`
- `professional/v2/04_BI01_BUSINESS_BASELINE.md`
- `professional/v2/05_BI01_FIXED_INPUT_DATA.md`
- `professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md`
- `professional/v2/01_AIDATA_CHART_AND_DATA.md`
- `professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md`
- `professional/v2/03_EXECUTION_HANDOFF.md`
- `runtime/dual_route_execution/DR12_PROFESSIONAL_QUESTION_CATALOG.md`

### complex-systems-vocabulary `@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3`

完整读取：

- `OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md`
- `U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md`
- `U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md`
- `U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md`
- `U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md`

### 固定数据

两份 ZIP 均按 Binding SHA 实际读取；未重算、未修改、未替换。

### 未采用为事实

- 旧 V2-01 的专业选样、结论、Gate 和接收状态；
- 旧图 URL 的可见性；
- 未浏览器复核的 HTTP/file 存在；
- 未正式实现的 U2/U3 TypedDesign；
- R03 Withheld 内容。

## 12. 交付物索引与校验

| 产物 | 用途 | 本地内容 SHA256 |
|---|---|---|
| [`S1_SCENE_SEARCH_AND_SELECTION.md`](./S1_SCENE_SEARCH_AND_SELECTION.md) | 搜索方法、覆盖、六场景与问题 | `8e4c9d747430b240be0478769fab830abfa12aedd68dd85c0aa4467f350df88b` |
| [`S1_SELECTED_SCENES.csv`](./S1_SELECTED_SCENES.csv) | 场景/窗口/成员/known/问题索引 | `af0b8b23be1494e378a76d8185389e98ea172b9d107497ca0bc4f6e06ab94160` |
| [`S1_SCENE_SYMBOL_PATH_FACTS.csv`](./S1_SCENE_SYMBOL_PATH_FACTS.csv) | 六场景各成员 4/12/24/48 bar 路径事实 | `e00375365e1524a8f73d0107de381f6041053301736f894a05acde02be0d1157` |
| [`U3_BUNDLE_FIXED_DATA_MAP.csv`](./U3_BUNDLE_FIXED_DATA_MAP.csv) | 设计字段—固定字段—资格/缺失映射 | `8987ba4cce38911bc193c6e6777e02f45df2c63d3c3f447e01a90a2bb02755a3` |
| [`REFERENCE_CASE_PREANALYSIS.md`](./REFERENCE_CASE_PREANALYSIS.md) | SCN-01 五 As-Of 专业预分析 | `501de1b96b362a164d15755cf96cc7d8cc16bd4bb3b8c8e2f5b2a0c85935ade6` |
| [`REFERENCE_CASE_R02_NORMALIZED_VIEW.csv`](./REFERENCE_CASE_R02_NORMALIZED_VIEW.csv) | R02 与 N 的可比辅助视图 | `a62364ffb640a4d69b976f7da072dc76067508143d2ed6da09235c940a0190d7` |
| [`WORKER_AIDATA_CHART_ORDER.md`](./WORKER_AIDATA_CHART_ORDER.md) | 六场景 S2 真施工工单 | `9ba1371de1401535e3ab3d624d43f601aa5c6796f6174660a805ec0d535680b8` |
| `S1_SCENE_BASE_FACTS.csv` | 本地完整选窗基础切片；只作 S1 支持，不冒充 S2 同源导出 | `0bb4ec33b54e8c82e0ca42dd872434704a7c6d8ce527044129d7c9db6d90cacc` |

<a id="remaining"></a>
## 13. 完整未完

<a id="remaining-s3"></a>
### 13.1 S3 未完

- 六场景尚未与本 run 的真实 Owner 图和 aidata 同源导出逐项绑定；
- SCN-02—06 目前只有基础路径事实和问题，不能形成正式 U3 判断；
- SCN-01 仍需图定位和浏览器核验；
- U2 位置/成员、第三对象、actual/known 在图上的可见性尚未验收；
- U3 相对 KLine/C0/N 的广域增量仍未完成；
- 设计行动尚未经过六场景支持/反证汇总。

### 13.2 完整任务未完

尚未满足：

- Owner 可打开并定位每项重要判断；
- 六场景基础图与证据图层；
- 同一 run/node/timespan 的 AI 数据；
- U2 位置和成员/第三对象的完整检验；
- 四束在可用范围内逐场景支持/反证；
- 全部基线增量与最终设计行动；
- 首个真实闭环后的非阻塞管理复看。

<a id="triggers"></a>
## 14. Trigger 状态

- `BI01V202-FIRST-GROUNDED-CYCLE`: **NOT_YET**。已有真实基础位置和固定数据预分析，但缺本 run 的可打开图、同源 aidata 数据和图定位，尚不满足 RESULT 条件。
- `BI01V202-SUBSTANTIVE-CHANGE`: **NOT_YET**。未发现需要改变固定范围、数据前提、工具边界或完成条件的冲突。exact/near-time 的问题属于待检设计问题，不是数据身份冲突。
- `BI01V202-EFFORT-4`: **NOT_YET**。这是首次有效 professional 实质回交，尚未达到四次周期。

<a id="continuation"></a>
## 15. 已明确的连续后继

同一工作、同一 Binding、同一完整范围继续：

1. 将 [`WORKER_AIDATA_CHART_ORDER.md`](./WORKER_AIDATA_CHART_ORDER.md) 实际路由给有权 Worker；
2. Worker 在 `/dwdhome/fy/BASE_E6_2` 先完成 SCN-01 首个闭环，再连续完成六场景，不以首图停止；
3. Worker 回交真实 report URL、同源导出、aidata commit、固定源 SHA、浏览器验收和失败事实；
4. 执行 Pro 消费 Worker 结果，先复核 SCN-01 图定位，再完成 SCN-04/06 第三对象、SCN-03/02 整组弱/强、SCN-05 错时边界；
5. 对每个场景按“市场事实—设计承诺—当时判断—后续检验—基线—结论—行动”完成 S3；
6. 首次形成“真实图/同源数据 + U2 判断 + U3 差异/精确限制 + 后续/基线增量”的闭环时，发 `BI01V202-FIRST-GROUNDED-CYCLE` 非阻塞 M-REASSESS；完整责任继续，不因该触发停止。

当前停止是因本聊天缺 aidata/浏览器执行能力，而不是自设小目标完成；真实下一步已具备场景、窗口、固定源和可执行工单。

<a id="question-work-return"></a>
## 16. QUESTION_WORK_RETURN

完整机器回交见 [`QUESTION_WORK_RETURN.json`](./QUESTION_WORK_RETURN.json)。状态为：

```text
S1: 本轮初始全范围搜索已完成；随 S2/S3 暴露的新问题继续
S2: 工单和输入已准备；真实图/同源数据/浏览器核验未执行
S3: SCN-01 固定数据预分析已完成；六场景图联分析未完成
batch: IN_PROGRESS / CONTINUE same_work
```

<a id="role-return"></a>
## 17. ROLE_RETURN

完整机器回交见 [`ROLE_RETURN.json`](./ROLE_RETURN.json)。执行 Pro 不宣布管理或 Owner 接收，也不把此回交写成 U2/U3 业务 PASS。
