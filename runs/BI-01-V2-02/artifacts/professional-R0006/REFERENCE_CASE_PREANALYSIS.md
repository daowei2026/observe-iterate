# SCN-01 固定参考 Case 数据预分析（S3 前置，不替代 S2 图闭环）

invocation_id: `BI01-V2-02-R0006-20261018T154801Z-a5ec3f46`  
case_ref: `refonly-ad8824a52552d7bffa91`  
actual turn: `2021-04-30 15:00:00`，Up，hc/i/rb  
legal As-Ofs: `2021-05-06/07/11/14/18 10:00:00`

## 1. 资格声明

这份分析使用固定包的 C1/S/C2/U3 R02/R03、C0/N 和对应 KLine 数据。它是**结构化数据预分析**，不是完整 S3：

- 尚未有本 run 经浏览器核验的 Owner 图；
- R02 是 `ShadowOpportunityClusterMemberEpisode` objective facts；
- C2 没有 official cluster commit，H1 没有 emitted；
- R03 的 `quality_judgement` 与 `capital_use` 在 15 行中全部 `WITHHELD`；
- 简单归一化列（除以 start price）只用于同图解释，不是正式 U3 normalization/calibration；
- 后续 KLine 只作为明确标注的探索性显示范围，不回填历史 Current。

## 2. U2 位置和成员

### 市场事实

hc、i、rb 在 `2021-04-30 15:00` 有同一 `actual_uti=75230999`、同向 Up 的 mid turn；三者到 `2021-05-06 10:00` 共同可知。C1 reference 中三对关系的实际转折时间、方向和类型均支持；到 5 月 7 日，reference Formation/Qualification/Validity 由 Working/Pending 转为 Accepted/QualifiedWorking/AcceptedWorking。

### CaseFinding

把三者作为**同一轮共同启动候选**是合理的：它不是事后赢家筛选，而是共同 actual turn 和后续正向组织的身份对齐。

但以下结论不成立：

1. `outside_count=0`、`ValidEmptyAlternatives` 不是“外部对象都比它们差”，只是固定 Universe 恰好等于三成员；
2. `four_gate_reference_pass=True` 仍只是 shadow eligible；`official_cluster_committed=NO`、`official_h1_emitted=NO`；
3. 因此不能把这个 Case 写成正式 OpportunityCluster 或正式 H1。

### 设计问题

这个全 Universe 三成员 Case 可以检验同一机会身份和成员 Episode 对齐，却不能检验真正的 External Separation、漏组或组外第三对象。SCN-04/SCN-06 才承担第三对象边界挑战。

## 3. 五个 As-Of 的合法 Current

### 2021-05-06 10:00：同为 WorkingSoFar，观察 2 bar

以各自 start price 做探索性归一化：

| 成员 | 净推进 | 路径效率 | 最大反向/起点 | 峰值保持 |
|---|---:|---:|---:|---:|
| hc | 3.54% | 0.944 | 0.11% | 0.971 |
| rb | 4.09% | 0.932 | 0.15% | 0.965 |
| i | 4.36% | 0.821 | 0.47% | 0.902 |

**市场事实**：i 在两 bar 内净推进略高，但路径效率更低、最大反向相对更大、峰值保持更低。Progress 与 Friction/Retention 不给出同一个排序。

**CaseFinding**：四束分开是必要的；仅按 raw progress 选 i 会遗漏摩擦，仅按效率选 hc 又会遗漏推进幅度。当前只能说“i 推进快但路径较不稳”，不能说“i 最好/最差”。

### 2021-05-07 10:00：生命周期已经不可比

| 成员 | stage | observed bars | 净推进/起点 | 路径效率 | 最大反向 |
|---|---|---:|---:|---:|---:|
| hc | WorkingSoFar | 14 | 4.87% | 0.837 | 8 quote units |
| rb | WorkingSoFar | 14 | 4.98% | 0.817 | 19 quote units |
| i | Completed | 1 | 4.83% | 1.000 | 0 |

**市场事实**：i 的 anchored episode 已在 1 bar 后 Completed；hc/rb 仍在 14-bar Working。i 的 1.0 efficiency 来自一条极短完成路径，不能与 14-bar Working 路径当作同口径“最好效率”。

**CaseFinding**：`episode_stage_at_cut + observed_bar_elapsed` 本身就是 ObservabilityAndConstraint，必须先于数值比较。

### 2021-05-11 至 2021-05-14：成员延伸分化

- 5 月 11 日：rb anchored episode 已 Completed 33 bars，探索性净推进约 13.14%，efficiency 0.870；hc 仍 Working 38 bars，约 11.79%，efficiency 0.623；i 仍保留原 1-bar Completed episode，约 4.83%。
- 5 月 14 日：hc Completed 33 bars，约 14.04%，efficiency 0.883；rb 保持上述 Completed；i 仍是原 1-bar Completed。

**CaseFinding**：在 anchored episode 语义下，rb/hc 的持续和延伸显著高于 i；i 是“早期快速完成的小段”，不是同一 episode 中持续到后面的成员。

**反例**：从原始 KLine 将窗口延伸到 48 bar，i 的价格也继续上行，甚至累计幅度更大。那段后续运动包含新的转折/Episode，不能无条件算作原 anchored episode 的 Retention。若业务问题关心固定未来 horizon 而非 episode lineage，需要另立 Outcome 合同；否则会把“原机会持续”与“后来再次上涨”混在一起。

## 4. 与 C0/N 单品种画像的比较

最有价值的差别出现在 5 月 7 日：

- U3 R02 仍保留 i 的**原机会 anchored episode**：Completed，+51 quote units；
- N 在同一 As-Of 已滚动到 i 的**当前 working episode**：`working_prefix_progress=-53.5`、efficiency `0.6646`、counter `63.5`；
- rb/hc 的 N working path 当时仍与原机会 episode 对齐。

### 增量判断

**真实增量**：

1. U2+R02 给原共同机会保留稳定 member-episode identity；
2. 即使 N 已转到新 episode，仍可追踪“原机会中的 i 走了多远、何时结束”；
3. 因而组织、可追溯性和重复暴露分析有明确增量。

**尚未证明的独立投资增量**：

1. N 在 5 月 7 日已经显示 i 当前反向而 rb/hc 仍正向；
2. 仅就“此刻谁还在延伸”而言，N + KLine 已能给出主要差异；
3. R02 是否能更早、更稳定地改变成员选择，需要更多场景和合法 Outcome；本单 Case 不能证明。

## 5. 四束可判范围

### Progress

可观察：raw progress、amplitude、observed bars、run 结构、extreme count。  
限制：raw quote units 不可跨品种直接排名；不同 lifecycle/window 不可同票。

### Friction

可观察：path efficiency、max counter move、advance/counter runs、sign changes。  
限制：它们共享同一路径证据；没有正式 turn density、retracement burden 或 rapid reversal threshold。

### Retention

可观察：achieved peak、retained fraction、return-to-origin progress、recovery event count。  
缺失：outside-region dwell、recovery time、cross-scale continuation。  
结论：只能判部分代理，不能宣称完整 Retention bundle 已实现。

### ObservabilityAndConstraint

可观察：stage、observed bars、path status、missing count、actual/knowledge time、N sample adequacy。  
缺失：正式 business calendar duration、liquidity、capacity、cost coverage。  
结论：不能从“数据路径可读”推成“可交易/可承载资金”。

## 6. 后续事实与时间边界

`2021-05-18 09:30` 三品种实际出现共同 Down turn（SCN-02），但它们到 `2021-05-18 10:00` 尚未共同可知；共同可知时间为 `2021-05-19 14:00`。

因此：

- 在 5 月 18 日 10:00 的 Current 中使用该 Down turn，属于未来信息泄漏；
- 在后续 Outcome/反证中使用它，必须声明 horizon、actual/known time；
- 这正好说明 As-Of 和 Outcome 分离不是形式要求，而会改变结论资格。

## 7. 当前业务结论

### 支持

1. U2 的三成员共同机会身份在本 Case 中有基础行情支持；
2. member episode identity 与 lifecycle 是真实、可消费的组织增量；
3. U3 将 Progress、Friction、Retention 和 Observability 分开是合理设计；
4. 5 月 6 日 i“推进更快但摩擦/保持较差”的冲突证据，证明不能用单字段或总分替代叙事。

### 削弱/反证

1. closed Universe 无法证明 External Separation；
2. i 的 anchored episode 短，并不等于 i 后续整个市场路径弱；
3. N 已经较早暴露 i 当前 episode 的反向，U3 的独立投资信息增量仍未证明；
4. R03 全部 Withheld，不能形成正式成员质量排序、组预算或资金动作。

### 设计行动

**保留**：

- 原机会 member-episode identity；
- Current/Outcome、Working/Completed、actual/known 的分离；
- 四束分账与同源证据不多票。

**修订/补证**：

- 所有跨成员显示先提供可比归一化与 lifecycle/window；
- External Separation 必须使用有真实 outsider 的场景；
- Retention 补 outside dwell、recovery time 和 episode lineage；
- 明确 fixed-horizon Outcome 与 episode-based Outcome 的区别；
- 用 SCN-02—SCN-06 检验 U3 相对 N/KLine 的真正增量。

**有据停止的内容**：

- 不再尝试从本 Case 导出正式 Quality 或 Allocation；
- 不把 `ValidEmptyAlternatives` 改写成“分离良好”；
- 不按 raw progress、efficiency 或 retained fraction 单项选赢家。
