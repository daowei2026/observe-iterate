# BI-01 R0003｜I4 完整专业回交：共同 Trough 后的成员分化与层间增量

- work_id：`BI-01`
- invocation_id：`BI01-RESTART-01-R0003-9dda7755b8d94803ba5b03f53721d18c`
- assignment_token：`eab45254f4464b148d9ee7fd0833730a`
- 当前任务：`BI01-RESTART-01-I4-EXECUTION-01`
- professional_mode：`OBSERVATION_I4`
- 身份：执行 Pro；本报告不是管理接收、独立审查或正式产品发布。
- 核心问题 Q-01：一轮共同转折中的成员在 Progress、Friction、Retention 和生命周期上怎样分化；U2/U3 相对单品种、静态板块增加了什么。
- Case：`refonly-ad8824a52552d7bffa91`，HC/RB/I，actual `2021-04-30 15:00`，五个任务指定 As-Of 均为 10:00。
- 结果资格：Reference/Shadow；提出限定 G3/G4 消费范围，等待管理 Pro 决定。没有自行签 G4/G5，没有进入 I5/I6。

<a id="result"></a>
## 1. 业务回答

**共同发生转折，不等于成员随后以相同方式推进；当前结果更不能直接排列为“I 最好、RB 次之、HC 最差”。**

5 月 11 日 10:00 的原始切面中，HC 路径效率为 0.622677，RB 为 0.869619，I 为 1。三个数都能由当前上游价格复算，但它们分别描述 **38 个间隔的 Working 路径、33 个间隔的 Completed 路径和仅 1 个间隔的 Completed 路径**。数值正确不等于这个横向比较回答了“谁更顺畅”。

把 HC/RB 放回同一 33 间隔范围，效率变为 HC 0.882743、RB 0.869619；把两者都观察到第 38 间隔，效率为 HC 0.622677、RB 0.563564。原来的相对次序反转。这里的新增认识来自 I4 对观察范围的挑战，不应记成 U3 算法自动增加的质量判断。

I 的 Completed 效率 1、保留比例 1，只覆盖 1056→1107 这一个价格增量。它既不能证明 I 连续多日保持，也不能因为 Episode 很短就认定 I 后续走不动。相同 38 间隔事件窗口内，I 的相对推进较大，但折返负担也较大；这是一组竞争坐标，而不是一个总分。

当前 U2 有明确的**同轮对象组织和可追溯性增量**：不再仅因三个品种属于固定观察集合而一起看，而是明确它们共享哪次 actual turn、何时才可知、使用哪些 Episode、处于何种参考资格。可是本 Case 的成员一直恰好是 HC/RB/I，尚未检验出相对静态集合的成员筛选增量。当前 U3 的若干主要路径字段则可以逐项在 C0/N 中找到一致值；新增的保留、run、恢复表达尚未形成一个经挑战后超出既有路径认识的独立质量结论。

**有据的无增量结论限于本 Case、当前 Reference 方法和本报告列出的判断，不是“U2/U3 普遍无用”。**

另发现一个局部 Source/Method 不一致：HC 在 5 月 7 日 10:00 回到前高 5961；按 Movement 来源正文“重新触及 prior peak”计为第 4 次恢复，R02 却导出 3。3 与严格突破前高的诊断算法一致，但没有实际生成代码，不能声称已证明其实现采用了该算法。这个字段单独限制使用，不使已核实的关键路径、四层对照和本报告其他认识失效。

<a id="directed-g3"></a>
## 2. 定向 I3/G3 核查及可消费范围

### 2.1 输入冻结与核查方法

附件 A：
`steel_U2_U3_执行结果_20261010.zip`
SHA-256：`7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`。

附件 B：
`rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`
SHA-256：`4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`。
这就是本次候选 DataBinding 的实际原件；不称为历史 `ff3215...` 原件。

A 的 23 个 CSV 和 B 的完整归档均可读，ZIP CRC 核查无错误。B 的 15 个 CSV 的真实字节数与 SHA-256 均匹配 manifest。三品种每份 KLine 9080 行，各有 12 行原始空 OHLC，占位未插值、未删除。15 条承重 R02 路径、共同范围诊断和 knowledge-origin 诊断均没有命中空 OHLC。

来源实例按 B 的 `manifest.json` 与 `数据说明.md`：`TA_updto20240229`，`night_end_at_2300`，30m close/closeUti，`ZigZag["small"]` retracePct=0.5%，原始 `ScaleTurnCalendar("mid")` value1/value2，specTerm=M、stMembershipLine=0.3；没有运行 filtered ScaleTurn。本轮核了导出数据与具名方法的对应，没有取得这些生产类的源码提交和实际 Runner，不把 manifest 的本地路径当作源码核验。

时间保持原 CSV 显示值和 UTI 绑定，不转 UTC，不从自然时间差自行发明 Native Calendar duration。下文 h/bar 指**相邻价格点间隔数**：h=38 对应 39 个收盘价，h=33 对应 34 个收盘价；不能直接解释为连续 38×30 分钟。

`verify_case01.py` 是执行 Pro 的有界独立核查脚本，不是重建 Runner，不改正式方法、原 ZIP 或下游产品。它按冻结 Case/As-Of 读取、核对并输出诊断证据；没有 Worker 被派发或执行，没有生产工程修改。

### 2.2 实际核查结果与建议资格

| 对象/主张 | 已实际完成 | 执行 Pro 的范围建议 |
|---|---|---|
| 两包与 B 的成员身份 | 真实 SHA-256、CRC、15 个 manifest CSV 成员逐项匹配 | 可用作本次 Reference 输入；不追认历史包 |
| 三条 anchor 及三个 end turn | C0→原始 mid→exact Zig 行核对实际点、内嵌确认点、source occurrence、价格 | 可消费本 Case 的导出身份与时间对应；非生产 opaque identity 认证 |
| Episode 生命周期 | 五切面及 I 11:00、RB 09:30、HC 10:30 切换边界核查 | 可消费本 Case Working/Completed 分账，不回填 |
| 15 条 R02 关键路径 | start/end、点数、missing、进展、幅度、path length、efficiency、counter、peak、retained、origin、extreme count 逐条复算 | 限定范围建议可消费；最大数值绝对差 1.110223e-16 |
| R02 与现成 C0/N 的重复性 | 6 条 Working×4 字段与 N 相等；9 条 Completed×6 字段与 C0 相等，共 78 个配对值误差 0 | 支持所列字段的同源/重复事实判断 |
| N 已有单品种画像 | 15 切面的两个 exact 6-Episode 窗口；90 个有效 metric 行的 median、previous、change、MAD、LOO 重算，共 450 个数值；窗内 completion 不晚于 As-Of | 相对已导出 C0 的一致性成立；不是全部历史路径重审 |
| run/符号切换 | 15 行 advance/counter/flat run 与去 flat 后 sign changes 均匹配 | 可作本 Case 路径分解事实；不作独立多票 |
| `completed_recovery_events` | 14 行与触及算法相等；HC 05-07 10:00 导出3、触及4、严格突破3 | **NeedsRepair/限制该字段按“触及恢复”消费**；不能说已修复实际生成器 |
| C1/S/C2 参考状态 | 已读实际 120 条关系、5 切面 assessment/S/C2、12 行兼容矩阵 | 可陈述实际导出状态与方法限制；不代替正式算法运行证明 |
| 共同范围与参数挑战 | 已计算下文诊断；源数据无空值；参数只核必要条件 | 可作明确命名的 I4 诊断，非新正式 Episode/H1/Quality/Outcome |

没有把“需要修一个字段”扩大为全线 G3 失败，也没有把其余字段正确扩大为全包、全历史或生产 G3 通过。最终限定接收仍由管理 Pro 判断。

### 2.3 三成员身份、actual/confirm/knowledge 与 Completed 对照

共同 anchor actual：`2021-04-30 15:00` / UTI `75230999`。
三条 anchor 均来自 **value2**，内嵌 confirm point 为 **05-06 09:30**，source occurrence/knowledge proxy 为 **05-06 10:00**。后一个时间才是本次导出可知边界；不把 09:30 当成已经可用。

| 成员 | anchor turn id | Episode id | 起价 | canonical actual end | 终价 | 完成可见 |
| --- | --- | --- | --- | --- | --- | --- |
| RB | refonly-676f80eb6fcd938ea8 | refonly-9f55eb74da9a4089a7 | 5380.0 | 2021-05-10 21:30:00 | 6087.0 | 2021-05-11 09:30:00 |
| HC | refonly-52bd09357229361305 | refonly-18ddb757325fb8241e | 5684.0 | 2021-05-10 21:30:00 | 6482.0 | 2021-05-11 10:30:00 |
| I | refonly-040e0263e26abbb974 | refonly-22321a4b963e925b7c | 1056.0 | 2021-05-06 09:30:00 | 1107.0 | 2021-05-06 11:00:00 |

三条 anchor 在 B 的 mid CSV 的物理行：HC 43、RB 43、I 83；在 Zig-confirmed CSV 的物理行：HC 144、RB 142、I 210。C0 的 `source_csv_row` / `zig_confirmed_csv_row` 是不含表头的 1-based 数据行，故物理 CSV 行号加 1。这是行号口径，不是运行错误。

三个 end turn 的 mid/Zig 物理行分别为 HC 44/145、RB 44/143、I 84/211。RB 的 end 内嵌 confirm 是 05-10 23:00，source occurrence 是 05-11 09:30；HC 分别是 05-11 10:00/10:30；I 分别是 05-06 10:30/11:00。这些 exact 对应解释了“同一个 actual end，不同时间完成可见”。

<a id="timeline"></a>
## 3. 五个 As-Of 的真实过程

### 3.1 当时可知的成员客观事实

表中 P/L/counter 都是**各自品种原始价格点**，仅用于单品种路径核算，不能按点数跨品种排名。效率 E 与保留比例 R 是该行范围的无量纲量。`W` 是 WorkingSoFar，`C` 是 Completed；所有行的正式 Quality 均 Withheld。
| As-Of | 成员 | 阶段/h | 观察终价 | P | L | E | 最大counter | 已达峰值 | R |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05-06 10:00 | HC | W/2 | 5885.0 | 201.0 | 213.0 | 0.943662 | 6.0 | 207.0 | 0.971014 |
| 05-06 10:00 | I | W/2 | 1102.0 | 46.0 | 56.0 | 0.821429 | 5.0 | 51.0 | 0.901961 |
| 05-06 10:00 | RB | W/2 | 5600.0 | 220.0 | 236.0 | 0.932203 | 8.0 | 228.0 | 0.964912 |
| 05-07 10:00 | HC | W/14 | 5961.0 | 277.0 | 331.0 | 0.836858 | 8.0 | 277.0 | 1.000000 |
| 05-07 10:00 | I | C/1 | 1107.0 | 51.0 | 51.0 | 1.000000 | 0.0 | 51.0 | 1.000000 |
| 05-07 10:00 | RB | W/14 | 5648.0 | 268.0 | 328.0 | 0.817073 | 19.0 | 283.0 | 0.946996 |
| 05-11 10:00 | HC | W/38 | 6354.0 | 670.0 | 1076.0 | 0.622677 | 128.0 | 798.0 | 0.839599 |
| 05-11 10:00 | I | C/1 | 1107.0 | 51.0 | 51.0 | 1.000000 | 0.0 | 51.0 | 1.000000 |
| 05-11 10:00 | RB | C/33 | 6087.0 | 707.0 | 813.0 | 0.869619 | 19.0 | 707.0 | 1.000000 |
| 05-14 10:00 | HC | C/33 | 6482.0 | 798.0 | 904.0 | 0.882743 | 24.0 | 798.0 | 1.000000 |
| 05-14 10:00 | I | C/1 | 1107.0 | 51.0 | 51.0 | 1.000000 | 0.0 | 51.0 | 1.000000 |
| 05-14 10:00 | RB | C/33 | 6087.0 | 707.0 | 813.0 | 0.869619 | 19.0 | 707.0 | 1.000000 |
| 05-18 10:00 | HC | C/33 | 6482.0 | 798.0 | 904.0 | 0.882743 | 24.0 | 798.0 | 1.000000 |
| 05-18 10:00 | I | C/1 | 1107.0 | 51.0 | 51.0 | 1.000000 | 0.0 | 51.0 | 1.000000 |
| 05-18 10:00 | RB | C/33 | 6087.0 | 707.0 | 813.0 | 0.869619 | 19.0 | 707.0 | 1.000000 |

**05-06 10:00。** 三条共同 Trough 刚按 source occurrence 可知，三条 anchor Episode 当时都为 Working，已经包含从04-30到05-06早盘的较大价格跳变。I 后来会被定为 1 间隔 Completed，但 10:00 不能预先使用其 11:00 才可见的 end。Reference Formation 尚未关闭，Qualification/Persistence 均未满足，Shadow hold。

**05-07 10:00。** HC/RB 继续沿原 anchor 观察到 14 间隔；I 已在前一天11:00完成，旧 Episode 截在05-0609:30，不能随 As-Of 延长。参考 FormationAccepted、QualifiedWorking、ValidityAcceptedWorking；这个组级 Working 标签没有取消 I 的 Completed 身份。S 是空组外集合的参考持久性，不是证明比组外好。

**05-11 10:00。** RB 在09:30已知道旧 Episode 结束，I早已结束，HC还不知道本次 end（要到10:30）。HC含有21:30高点后的回落，RB却截在同一高点；这正是原效率次序不能直接作质量排序的原因。

**05-14 / 05-18 10:00。** 三条 anchor Episode 都已 Completed，旧 Episode 的数值相同。相同不是持续的新表现：原价仍然变化，N 的当前 Working Episode 已经切换。不得把两次复读已完成 Episode 的 R=1 算成新的“继续保持”支持。

后见 canonical 状态只放在上一节的回顾表中。R02 即使在早期行带有未来 `episode_completed_visibility_proxy`，它也是回顾性核查元数据，不是当时已知字段，更不能用于提前选择 end。

### 3.2 参考组织资格随切面怎样变化

| As-Of | Formation | Qualification / Validity | S：outside=0 | C2 / bridge |
|---|---|---|---|---|
| 05-06 | Working；epoch age2<12 | Pending | ValidEmptyAlternatives；K=1、elapsed0，PendingPersistence | 四门未满足，Shadow hold |
| 05-07 | Accepted；age14 | QualifiedWorking / AcceptedWorking | K=13、elapsed12，ValidEmptyPersistent | Shadow eligible；prior catalog/publication 未完成 |
| 05-11 | Accepted；age38 | QualifiedWorking / AcceptedWorking | K=37、elapsed36，ValidEmptyPersistent | 同上；成员成熟度仍混合 |
| 05-14 | Accepted；age74 | QualifiedCompleted / AcceptedCompleted | K=73、elapsed72，ValidEmptyPersistent | 同上；不是正式发布 |
| 05-18 | Accepted；age98 | 同上 | K=97、elapsed96，ValidEmptyPersistent | 同上；不是新增独立支持 |

五切面成员均为 HC/I/RB，formal assessment、official cluster、official H1 都未发布；bridge 为 `ShadowOpportunityClusterNotCanonical` / `PRE_CLUSTER_OBJECTIVE_FACT_PREVIEW`。R03 三轴为 CalibrationPending，quality 为 WITHHELD，capital 为 WITHHELD_LCC_NOT_PROVIDED。不存在“已正式排除 I”的事实，也不存在正式 Quality 给出的优劣排名。

<a id="comparison"></a>
## 4. 公平比较：三个必留域与一个时间敏感性诊断

### 4.1 比较域不能混用

| 域 | 它回答什么 | 本 Case 的范围 | 它不能回答什么 |
|---|---|---|---|
| As-Of lifecycle-true | 当时各自真正能读到哪个 Episode 状态 | 上节15行；完成前读prefix，完成后读actual end | 不自动公平比较不同长度的运动能力 |
| canonical completed | 事后确认这三条完整 Episode 各走成什么样 | HC/RB h33，I h1；completion时间分别保留 | 不能把事后end回填旧As-Of；不能延长已完成Episode |
| common-horizon / maturity-matched prefix | 同长度、同截止位置时的路径差异 | 三者不越canonical end的共同前缀最多h1；HC/RB可比h14、h33 | 三者h1的efficiency=1没有区分力；不能假装已有长范围三者完整Episode匹配 |
| anchor / knowledge-origin event window（诊断） | 从同一实际或可知事件起点，到同一日历观察终点发生了什么 | h2/14/33/38/74/98等；越过成员end者标为独立事件窗口 | 不是延长旧Episode，不是正式U3 Outcome，也不是交易回测 |

百分比推进为 `100*(末价-初价)/初价`，百分比 counter 为 `100*max_counter_move/初价`。这些只去掉原始价格水平的单位，不是已校准 normalizedAmplitude、波动风险、合约乘数或保证金收益率。效率为 `abs(P)/sum(abs(相邻价差))`；最大counter是方向累计峰值到之后位置的最大退让；retained是当前P/已达峰值，无峰值时不适用。

### 4.2 HC/RB 次序是否只因成熟度/截止点不同

| 比较 | HC | RB | 对原判断的影响 |
|---|---:|---:|---|
| 原05-11切面：HC W38，RB C33，效率 | 0.622677 | 0.869619 | 看似RB明显更顺畅，但范围混合 |
| 两者相同h33，效率 | 0.882743 | 0.869619 | 原相对次序不成立；差异也远小于混合比较 |
| 两者相同h38事件窗口，效率 | 0.622677 | 0.563564 | 同样观察高点后回落，仍不支持原次序 |
| h38推进/起价 | 11.787474% | 10.464684% | 两条路径都有正推进 |
| h38最大counter/起价 | 2.251935% | 2.955390% | 共同范围内HC的相对最大退让较小 |

HC 从h33到h38：价格6482→6354，净回退128，路径长度增加172，效率从0.882743变为0.622677。RB 同范围：6087→5943，净回退144，路径长度增加186；最大counter159。原切面只给 HC 包含这段尾部，并不是只有 HC 经历了回落。

HC 在10:30被确认后，旧 Episode 重新截为h33；当时真实收盘价6358，并没有回到6482。所以“Completed效率变高”是**确认到来导致的观察对象/范围回定**，不是价格突然恢复。5 月 11 日10:00时不能预知该回定。

### 4.3 三者共同事件窗口的全部核查结果

`跨end=是` 的行必须留在事件窗口域，不进入旧Episode的原R02。h1也不能提前在05-0609:30作为已确认anchor发信号。
| h | 终点 | 成员 | 推进% | counter% | E | R | 跨canonical end |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 05-06 09:30 | HC | 3.641802 | 0.000000 | 1.000000 | 1.000000 | 否 |
| 1 | 05-06 09:30 | RB | 4.237918 | 0.000000 | 1.000000 | 1.000000 | 否 |
| 1 | 05-06 09:30 | I | 4.829545 | 0.000000 | 1.000000 | 1.000000 | 否 |
| 2 | 05-06 10:00 | HC | 3.536242 | 0.105559 | 0.943662 | 0.971014 | 否 |
| 2 | 05-06 10:00 | RB | 4.089219 | 0.148699 | 0.932203 | 0.964912 | 否 |
| 2 | 05-06 10:00 | I | 4.356061 | 0.473485 | 0.821429 | 0.901961 | 是 |
| 14 | 05-07 10:00 | HC | 4.873329 | 0.140746 | 0.836858 | 1.000000 | 否 |
| 14 | 05-07 10:00 | RB | 4.981413 | 0.353160 | 0.817073 | 0.946996 | 否 |
| 14 | 05-07 10:00 | I | 9.895833 | 0.662879 | 0.794677 | 0.967593 | 是 |
| 33 | 05-10 21:30 | HC | 14.039409 | 0.422238 | 0.882743 | 1.000000 | 否 |
| 33 | 05-10 21:30 | RB | 13.141264 | 0.353160 | 0.869619 | 1.000000 | 否 |
| 33 | 05-10 21:30 | I | 21.354167 | 0.994318 | 0.757983 | 0.997788 | 是 |
| 38 | 05-11 10:00 | HC | 11.787474 | 2.251935 | 0.622677 | 0.839599 | 是 |
| 38 | 05-11 10:00 | RB | 10.464684 | 2.955390 | 0.563564 | 0.796322 | 是 |
| 38 | 05-11 10:00 | I | 16.571970 | 4.829545 | 0.484765 | 0.774336 | 是 |
| 74 | 05-14 10:00 | HC | 10.626319 | 7.072484 | 0.255499 | 0.600398 | 是 |
| 74 | 05-14 10:00 | RB | 7.453532 | 7.472119 | 0.178778 | 0.506953 | 是 |
| 74 | 05-14 10:00 | I | 10.558712 | 14.725379 | 0.151186 | 0.457906 | 是 |
| 98 | 05-18 10:00 | HC | 5.401126 | 14.813512 | 0.092890 | 0.305169 | 是 |
| 98 | 05-18 10:00 | RB | 4.423792 | 12.509294 | 0.078393 | 0.300885 | 是 |
| 98 | 05-18 10:00 | I | 11.837121 | 19.223485 | 0.123274 | 0.513347 | 是 |

由此得到两项实际区分：

在05-11共同h38范围，I的相对推进16.571970%，高于HC/RB，但其相对最大counter4.829545%、效率0.484765，显示较大的推进与较大的折返同时存在。不能用它的h1 Completed效率1抹掉这些后续事实，也不能以其摩擦更大就抹掉其推进。

到05-14共同h74，HC/I的相对推进已接近（10.626319%/10.558712%），counter和效率却差异明显；到05-18，I相对推进又较大。端点选择会改变某些相对位置，不能把05-11或05-18挑成永久品种属性。三个对象全h1的效率都等于1，是一个增量且无反向时的算式结果，不构成优质运动的重复验证。

### 4.4 去掉 anchor 可知之前的运动

进一步将起点固定在三条 source occurrence 已可知的05-06 10:00，五个终点不变。第一切面h0的净变化为真实0；路径效率/保留比例不适用，不填1，也不把“不适用”说成市场差。
| As-Of | 成员 | knowledge起点后h | 推进% | E | counter% | R |
| --- | --- | --- | --- | --- | --- | --- |
| 05-06 10:00 | HC | 0 | 0.000000 | 不适用 | 0.000000 | 不适用 |
| 05-06 10:00 | RB | 0 | 0.000000 | 不适用 | 0.000000 | 不适用 |
| 05-06 10:00 | I | 0 | 0.000000 | 不适用 | 0.000000 | 不适用 |
| 05-07 10:00 | HC | 12 | 1.291419 | 0.644068 | 0.135939 | 1.000000 |
| 05-07 10:00 | RB | 12 | 0.857143 | 0.521739 | 0.339286 | 0.761905 |
| 05-07 10:00 | I | 12 | 5.308530 | 0.774834 | 0.635209 | 0.943548 |
| 05-11 10:00 | HC | 36 | 7.969414 | 0.543453 | 2.175021 | 0.785595 |
| 05-11 10:00 | RB | 36 | 6.125000 | 0.449541 | 2.839286 | 0.704312 |
| 05-11 10:00 | I | 36 | 11.705989 | 0.422951 | 4.627949 | 0.716667 |
| 05-14 10:00 | HC | 72 | 6.847918 | 0.187355 | 6.830926 | 0.500621 |
| 05-14 10:00 | RB | 72 | 3.232143 | 0.090184 | 7.178571 | 0.316988 |
| 05-14 10:00 | I | 72 | 5.943739 | 0.096112 | 14.110708 | 0.331646 |
| 05-18 10:00 | HC | 96 | 1.801189 | 0.034282 | 14.307562 | 0.131677 |
| 05-18 10:00 | RB | 96 | 0.321429 | 0.006429 | 12.017857 | 0.031524 |
| 05-18 10:00 | I | 96 | 7.168784 | 0.082463 | 18.421053 | 0.400000 |

这项挑战改变了什么：05-07时，按actual起点HC效率0.836858高于I0.794677；按knowledge起点之后，I0.774834高于HC0.644068。早期较高的actual-origin效率受可知之前的大幅位移影响，不能当成信号之后才赚到的结果。到05-11，HC相对RB较高的同范围效率仍成立，但不推出“HC一贯更好”。没有模拟开仓、成交、成本或收益。

<a id="increment"></a>
## 5. 四层增量/无增量矩阵：逐项对照已有基线

| 层 | 本轮实际消费的原有信息 | 新增/未新增什么 | 被挑战后的判断 |
|---|---|---|---|
| 单品种：KLine、C0、N | 价格路径；actual/knowledge；Episode切换；N两组exact6已完成Episode及当前Working overlay | 单品种自身进展、效率、counter、近期变化本来已存在 | 单独看某个品种不能给跨成员同轮关系；但成员“怎么走”不是U3才产生 |
| 静态HC/RB/I集合 | 固定比较对象，可并排读三个单品种 | 增加固定观察范围；未增加本轮具体共同转折身份和可知时点 | 固定板块标签本身不证明本轮一起形成机会，不给优劣边界 |
| U2：本次C1/S/C2参考组织 | 共同actual=75230999；Up/Trough兼容；逐成员Episode；五切面Formation/Qualification/Validity/空组外持久性 | 有显式同轮组织、时间/资格/证据定位增量；本Case成员与静态集合相同，无已观察到的筛选增量 | 同轮成立并不要求摩擦/幅度相同。outside=0不能证明优于其他对象；没有正式cluster/H1 |
| U2+U3：当前R02/Withheld | 同轮成员客观movement bundles；h/Working/Completed；peak/retained、run/recovery等表达 | 多个核心字段是C0/N复述；补充表达有解释便利，但未形成独立Quality判断 | 本Case主要认识来自正确范围的事实与挑战；不归功于字段增多。恢复字段另有局部方法问题 |

### 5.1 不是只凭“同源”就否定信息价值

同一原始数据可以经过有价值的处理形成新认识，因此“同源”不自动等于“无增量”。本轮有据无增量依靠的是**同对象、同Episode、同As-Of、同字段**配对，以及相关业务判断在基线中已经可得到：

6 条 Working 行：R02 的 progress、efficiency、max_counter、extreme_count 与 N 的当前 overlay 四字段完全相等。9 条 Completed 行：R02 的 progress、amplitude、path_length、efficiency、max_counter、extreme_count 与 C0 complete metrics 六字段完全相等。15 行重复性有原始 ID/字段对照，不是名称推断。C1 的15条 PostTurnFrictionOrganization 也已经逐对列出同一效率坐标，R02并未第一次发现这个差异。

peak/retained、run/recovery不全部是N的同名列，不能把它们全部说成“逐字段复制”。但它们仍与同一价格路径共享证据；本Case的completed峰值保留1受端点选择影响，HC/RB canonical均有5次恢复计数也没有单独决定谁更好，Working恢复计数还存在一行方法不一致。当前没有证据显示这些新增表达改变了控制成熟度/时间之后仍成立的独立Quality结论。

### 5.2 N 实际已经知道、而旧anchor R02不会自动跟随的事

| 成员 | As-Of | N当前方向 | N当前Episode实际起点 | N当前方向化progress | N当前E |
| --- | --- | --- | --- | --- | --- |
| RB | 05-06 10:00 | Up | 04-30 15:00 | 220.0 | 0.932203 |
| RB | 05-07 10:00 | Up | 04-30 15:00 | 268.0 | 0.817073 |
| RB | 05-11 10:00 | Down | 05-10 21:30 | 144.0 | 0.774194 |
| RB | 05-14 10:00 | Down | 05-12 23:00 | 357.0 | 0.562205 |
| RB | 05-18 10:00 | Up | 05-17 14:00 | 120.0 | 0.550459 |
| HC | 05-06 10:00 | Up | 04-30 15:00 | 201.0 | 0.943662 |
| HC | 05-07 10:00 | Up | 04-30 15:00 | 277.0 | 0.836858 |
| HC | 05-11 10:00 | Up | 04-30 15:00 | 670.0 | 0.622677 |
| HC | 05-14 10:00 | Down | 05-12 22:00 | 388.0 | 0.565598 |
| HC | 05-18 10:00 | Up | 05-17 14:00 | 143.0 | 0.512545 |
| I | 05-06 10:00 | Up | 04-30 15:00 | 46.0 | 0.821429 |
| I | 05-07 10:00 | Down | 05-06 09:30 | -53.5 | 0.664596 |
| I | 05-11 10:00 | Down | 05-10 11:00 | 51.0 | 0.600000 |
| I | 05-14 10:00 | Up | 05-13 14:30 | 16.0 | 0.213333 |
| I | 05-18 10:00 | Up | 05-17 14:00 | 55.5 | 0.744966 |

例如05-11，RB的N已转向从05-1021:30起的Down Episode，方向化progress=144；R02仍在回答旧Up anchor Episode走到其已完成end是什么样。这不是两者互相算错，而是**当前状态问题与历史同轮Episode问题不同**。05-07 I的当前Down Episode progress=-53.5，也不能误读为该品种价格下跌53.5；它表示相对该Down方向，实际走到了反方向。

N的历史基线也不是空白：本轮对90行六类有效metric各五个统计量重算，最大绝对误差1.387779e-16。原N同时明确 withheld business_duration / normalized_amplitude；本报告未替它私自补正式归一化。

一个关键实际缺件必须保留：C1的 `NodeBehaviorComparison` 在15个 pair/cut 中都写的是 `RawNWindowAvailableButNotJoined`。N数据存在，但**这条参考关系尚未接入实际N比较**；不能称为“等数据”或“已用N共同支持成组”。本轮独立消费N完成基线对照，没有把这项阅读伪装成修改了C1的真实入口/消费者。

<a id="challenges"></a>
## 6. 方法、证据依赖与反例挑战

### 6.1 Δ/bar proxy 与兼容矩阵

当前方法标识为 `STEEL_U2_C1_SINGLE_SCALE_REFERENCE_METHOD_V0.1.0`。实际CSV给出 Δref=2bar、pair neighborhood4、epoch12、Working minimum4、S K3/elapsed8。来源焦点文档§3.4说明候选关系是2Δ/6Δ/2Δ/4Δ，而Δ不能自动等于30分钟。三成员actual lag都为0，故这个Case对pair邻域宽窄几乎没有辨识力。

按原候选倍数关系把Δref分别设为1、2、4，只核当前数据上的**必要条件**：
| Δref | pair邻域 | epoch/Working/S elapsed | 05-06必要条件 | 05-07必要条件 | 05-11及以后 |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | 6 / 2 / 4 | 未齐 | 齐 | 齐 |
| 2 | 4 | 12 / 4 / 8 | 未齐 | 齐 | 齐 |
| 4 | 8 | 24 / 8 / 16 | 未齐 | 未齐（epoch及S时间不足） | 齐 |

“齐”不等于重跑后新C1 Accepted，更不等于正式Gate：没有重建历史epoch catalog、overlap arbitration、native Calendar、正式兼容映射或真实每cut观察事件。本实验只能证明：虽然零lag成对事实不变，参考资格出现的时点会随这些等待长度移动。不能把参数等待造成的晚接受讲成市场那时才出现改善。

12行兼容矩阵全部标为 `NEW_REFERENCE_MATRIX_NOT_MISSION_C_APPROVED`，包含Up/Down、Peak/Trough和ZigConfirmedPeak/Trough。同名方向、转折类型、Geometry在此Case相容，不能证明真实生产字段映射和其他类型都已正确。把Geometry支持再当作一份独立确认尤其不成立，它沿同一Zig/turn来源派生。

### 6.2 Formation、质量、Separation 的循环

Formation使用同尺度、actual接近、方向/类型相容等条件。不能再把“成员共同Trough”拿来独立证明该组高质量；post-turn方向组织可支持资格，不要求所有摩擦坐标相等。C1/S/C2没有输出正式U3质量，低摩擦也不是Formation的独立真值来源。

S的外部集合固定为空，连续记录空集合只能支持“当前研究Universe内没有可比较组外成员”及其参考状态保持。它不比较谁更好，97次参考frontier计数也不是97条独立市场反证。第三成员I在此Case没有被剔除；其完成早、观察短，不是Pending、数据缺失或负面成员资格。

### 6.3 Evidence dependency

| 证据族 | 实际依赖 | 不得计为独立多票 |
|---|---|---|
| actual/Direction/TurnType/Geometry | 同一个mid/Zig源及其语义映射 | 四个字段不是四个独立市场来源 |
| C0 metric→N overlay/历史统计→C1 friction→R02 | 同Episode价格路径，部分同名字段逐值相等 | N与U3一致不等于第二套独立实验证据 |
| P、L、E、counter、peak、retained、run、recovery | 同一close路径的相关变换 | 不能给“效率好+回吐少+保持高”直接累加票数 |
| 五个As-Of | 大量重叠前缀；Completed后原范围不变 | repeated snapshot不是独立重复Case |
| S K及elapsed | 同一空组外集合、参考bar frontier | 不能据此证明相对优势持久 |

### 6.4 单Case选择偏差与仍缺什么

本Case原先因共同actual且已有结果而被选中，并非盲抽或代表性统计样本；它恰好是三成员覆盖整个研究Universe、pair lag全部为0，无法评价非传递拓扑、真实组外差距或成员筛选胜率。

已经在原五切面、共同范围、canonical/Working转换、knowledge-origin窗口中找到反例，足以推翻本Case的无条件质量排序，并形成限定无增量认识。因此本轮不为凑A/B/C配额额外扩样，也不声称B/C已经观察过。没有跨Case重复证据是结论范围限制，不是把所有已完成I4永久挂起的理由。

30m close路径没有刻画bar内全部来回次序；百分比没有风险、乘数、成交成本或容量归一化；source occurrence仍是本包的knowledge proxy，不是独立验证过的生产接收时钟。以上均阻止升级为可交易质量或资金判断。

<a id="findings"></a>
## 7. 具名 findings

### CF-01｜CaseFinding：混合生命周期会改变HC/RB的相对路径判断

**命题。** 在本Case05-1110:00，用HC W38和RB C33的效率作横向顺畅性排序不成立；相同范围对照反证原次序。

**Raw facts / refs / method。** A 的R02物理行8（HC）和10（RB）；C0 Episode IDs见§2.3；B各品种KLine物理行937起，h33终物理970、h38终物理975。方法为同close路径公式与 `BI01-I4-DIAGNOSTIC-R0003-v1`，原正式Normalization未变。

**Support。** h33：HC0.882743>RB0.869619；h38：HC0.622677>RB0.563564。HC多出的五间隔真实包含128回退和172路径增量。两品种共有高点，completion knowledge不同。

**Counter / missing。** 这不是“HC总更好”：h33效率差很小，HC相对counter0.422238%还高于RB0.353160%；无风险调整、成本和跨Case重复。已知价格回落是真的，不被范围修正抹掉。

**Dependency。** 配对值都来自各自同一Episode/后续窗口；不是四份独立支持。

**Alternative explanations。** 品种真实摩擦差异、单切面选择、价位单位、完成可见延迟。共同范围消除了本次原次序，但不能排除其他窗口的真实差异。

**Sensitivity / invalidation。** 更换起点、截止点或数据绑定会改变值；若原R02并非指定Episode/价格范围，本发现需重做。不得把后来end提前回填作为验证。

**Unknown / next probe。** 是否在其他有不同confirmation delay的真实共同转折重复出现。下一批应按预声明的时间/成熟度条件选样，不按相对表现挑选。

### CF-02｜CaseFinding：I的“一步满效率”与其后续较大推进、较大折返可以同时成立

**命题。** I旧Episode的E=1/R=1只描述一个增量，不足以说明后续比HC/RB更顺畅；短Episode也不证明后续没有推进。

**Raw facts / refs / method。** I anchor1056、canonical end1107、h1；A R02物理行6/9/12/15重复Completed值；B I共同h14/38/74/98及knowledge起点诊断，§4全表。

**Support。** h38 I相对推进16.571970%，counter4.829545%，E0.484765；h14同actual起点I推进9.895833%，并未因旧Episode完成而停止变化。

**Counter / missing。** h1所有品种都满效率；I在knowledge后到05-07的效率却高于HC。没有单一“始终最好/最差”的次序，没有FormalQuality。

**Dependency。** Progress/Friction/Retention竞争坐标共享价格路径，不能累票；不同cut前缀重叠。

**Alternative explanations。** 短样本、端点选择、实际起点可知前的大位移、真实波动强度不同。

**Sensitivity / invalidation。** canonical范围和event窗口严格分开；改变起点后05-07局部次序改变。不得把跨end窗口写回I的旧Episode。

**Unknown / next probe。** 在同成熟度下，更大的相对推进是否足以抵偿更大的折返，需要明确业务质量方法与更多Case；当前不代Owner作取舍。

### NI-01｜NoIncrementFinding：本Case尚未证明当前U3增加了独立质量判断

**命题。** 已核承重事实主要复用C0/N/C1；U2有同轮组织价值，但本Case未显示成员筛选或组外优势增量，U3未形成经挑战后新增的正式或独立质量判断。

**Raw facts / refs / method。** A 的C0 complete、N cuts/metrics、C1 relations与R02。78个R02↔C0/N配对值零差；90行N统计一致；C1已列同效率；R03全部WITHHELD。

**Support。** “HC原来更不顺畅”的解释在公平比较中被反证；“I满效率所以更好”受一步样本反证；多cutCompleted保持不是新反馈。成员五切面不变且等于静态集合。

**Counter。** 同源处理仍可能产生重要新关系认识。U2明确同轮身份、可知时点、方法资格和证据边界；U3补充peak/retained/run/recovery表达，不是所有字段简单复制。没有进行人类阅读效率实验，故“组织更省时”只作可检查表达特征，不能量化效率收益。

**Missing。** 真正改变成员集合的Case、有可比较组外成员的Case、跨Case重复、消费者使用收益，以及按合法方法形成的Quality。缺项限制增量主张，不自动变成当前必做扩Universe/校准任务。

**Dependency / alternatives。** 窄Universe、特意挑共同actual、当前参考链部分未接入，均可能解释为什么尚无进一步增量。不能把这里的无增量推广到完整U2/U3设计。

**Sensitivity / invalidation。** 若同等可用基线下新增关系/字段改变了明确业务判断且经成熟度、单位、选择偏差挑战仍成立，本结论在那个新Case可被替代；本Case原结论保留。

**Next probe。** 下一轮优先检验“同轮成员选择是否与静态集合不同且有业务意义”，而不是继续把这15行包装成更多评分。

### MF-01｜MethodFinding：恢复计数的“触及”与“突破”不一致

**命题。** HC05-0710:00的 `completed_recovery_events=3` 不能直接作为来源合同§10.3“重新触及prior peak”的次数使用。

**Raw facts。** HC close：05-0623:00=5961 → 05-0709:30=5954 → 05-0710:00=5961。触及诊断得到4次，严格新高诊断3次；A R02物理行5记3。四个触及完成点是05-0611:00、21:30、23:00和05-0710:00，见脚本完整事件表。

**Source / method。** 冻结Movement合同§10.3和§9.3，与本轮有界recovery诊断。不把与严格算法相等当作“已核实际代码采用strict”。

**Support。** equality touch是确切价格事实。前三次均越过前高，第四次恰好相等，能区分两种算法；其他14行数值相同不消除此差异。

**Counter / missing。** 原Reference producer和独立method实现文件未随A交付；不能确定是生成器条件、结算规则还是Reference方法说明缺失，也不能宣布生产U3计算错误已定位。

**Dependency / alternatives。** 与同一路径共享；“需严格突破才能结算恢复”的未声明Reference定义可能解释3，但不等于满足当前读取的“触及”语义。

**处置 / invalidation。** 原ZIP不改；该字段的“触及恢复次数”claim建议NeedsRepair/Withheld，其余路径正常消费。诊断4是具名替代核查值，不冒充已修R02。若有权提供明确不同的有效Reference方法，需说明其适用范围；否则由实际生成器责任者定向核对、修复实际调用和消费者。

**Next probe / unknown。** 只需取得产生这一字段的确切函数/方法和调用输入，核 equality case；不需要完整Runner重建或全仓审计。当前没有获执行的Worker回交，不自称修复完成。

### MF-02｜Design/MethodFinding：阅读界面必须区分“旧Episode结果”与“当前市场状态”

**命题。** 现有状态字段本身可表达边界，但跨成员读表时若不显式携带scope，就会把完成回定、重复快照和未接入的N关系误解为新市场认识。

**Raw facts / refs。** HC10:30旧Episode的h38→h33；RB/I已切换N当前Episode；三条Completed在05-14/18重复；C1 NodeBehaviorComparison实际未join；S始终outside0。

**Support。** §3–5的实际consumer路径对照足以解释错误读法，不是“文件列表齐全所以设计正确”。

**Counter / missing。** 本轮没有观察正式前端或真实Owner使用，不断言某生产界面已犯错；现有设计已有Working/Completed、Outcome分责，本发现不是要求推翻该设计。

**Dependency / alternatives。** 同一领域对象的不同视图、当前参考实现未完成、观察者忽略scope，均可能产生表象。技术未接入不叫市场Pending。

**处置 / sensitivity。** 本报告表已直接分域；不修改正式方法、公共入口或用户界面。任何后续展示应保留As-Of可知范围、canonical回顾、h、原/现Episode、与N重复事实；不能仅显示一个Quality颜色/排名。若消费者明确只问旧Episode全过程，Completed freeze是正确行为，不应改为继续延长。

**Next probe。** I5使用本报告的实际过程和限定结论；管理如授权技术修复，应只针对实际被消费的误读位置或未接入字段，不追加平台工程。

### H-01｜待证假设（不是发现）

同轮组织在成员集合、确认延迟和后续Episode发生变化时，可能主要通过避免跨对象/跨时间错配而增加业务价值，而非创造新的单品种路径事实。本Case只支持它值得检验，不支持其普遍有效、预测收益或成本收益率。

<a id="completed"></a>
## 8. G4 自查、完整未完与后继

### 8.1 当前阶段自查

| 当前合同义务 | 本轮实物/判断 | 自查结果 |
|---|---|---|
| A 定向G3 | hashes、六turn来源、15路径、6边界切换、N基线、恢复字段局部冲突 | 关键范围已核；恢复claim单独提出限制 |
| B 五切面真实时间线 | §2.3、§3，明确future metadata、组资格和成员事实 | 已交 |
| C 三种公平比较域 | §4，另加actual/knowledge起点挑战 | 已交；事件窗口不冒充Episode |
| D 四层增量/无增量 | §5、NI-01，实际C0/N/C1字段配对 | 已交；没有用字段数证明增量 |
| E 主动挑战 | §4、§6及五张finding卡 | 已交；无跨Case规律、无正式Quality |
| F 连续后继 | 下述预声明选样规则与管理接收请求 | 已形成G4候选；不以单Case数量结算 |
| I5可消费性 | 价格过程、15行时间线、三域比较、逐层结论及具体争议均可直接阅读 | 具备限定审阅输入，不等于I5/G5或Owner已批准 |
| 回交 | 配套ROLE_RETURN / QUESTION_WORK_RETURN | 指向同一结果、未完和continuation |

提出 **G4候选**，请管理判断是否限定接收：Q-01已得到真实回答、已有反证和有据无增量；关键比较结论不依赖恢复计数争议。若管理认为恢复次数必须进入此次G4承重判断，只对该claim定向补修，不重做已成立比较。

<a id="remaining"></a>
### 8.2 完整未完与准确停止原因

本次I4任务的A–F专业分析及规定交付已形成，未以“Case A做完”作为停点。**提交是因为全部当前I4义务已形成可核的G4候选，需要由管理接收；不是因为达到图数、Case数或调用数。**

仍未完成/未获资格的事项分别是：

1. 管理对限定G3范围、恢复字段局部限制和G4的最终接收尚未发生；执行者不能代签。
2. HC05-0710:00恢复计数所用实际Reference生成器/方法未取得，原R02字段未修；本轮隔离其“触及恢复次数”claim，没有隔离其正确的价格与其他路径字段。
3. 目前没有跨Case重复验证，也没有证明成员选择相对静态集合的增量；因此只交CaseFinding/限定NoIncrement/Hypothesis，不交普遍规律。
4. I5的正式Owner Pack、Owner重要业务取舍及I6下轮任务安排没有执行，本次并未获这些阶段的专业授权。

这些限制不重新引入已撤工作。恢复旧I4、正式C2/H1、Quality校准、全Universe、完整Runner、平台改造、A/B/C固定配额都不是本轮deferred required。

### 8.3 下一问的预声明选择规则与使用资格

建议下一个有业务区分力的问题是：

> 当共同转折的成员不再等于固定HC/RB/I集合时，U2为什么纳入/不纳入第三成员；这个区分是否在同一可知时点、同成熟度与N基线下仍提供认识？

候选选择规则在看候选路径表现之前固定：仍用本次A/B两包；从A的 `C1/01_equal_actual_uti_candidate_facts.csv` 中，按 actual_uti 再 common_visible_asof 升序，在本Case actual之后选择第一个恰有两个不同成员的条目。不按收益、efficiency、counter、图形是否好看筛选。先核第三成员source可用性及actual-neighborhood/类型兼容；若是Pending/DataUnavailable则记录该状态，不能以“反例不好看”为由跳过。只有发现身份/Scope不合法才能具名排除，并保留排除原因。

新Case使用当前Reference方法和知识时间，不代入正式H1/Quality；先取三成员共同可知范围、各自生命周期、N既有信息和第三成员状态，比较“静态三成员”与“实际候选两成员”具体改变哪项判断。若仍只是组织/无增量，也作为有效结果。没有扩Universe、没有把这个候选规则变成已派发工作，也没有声称已经执行B/C。

恢复字段的下一核查则只针对MF-01所列 equality touch，用真实生成器责任者的确切方法/调用确认并修复，或者保持claim受限。它与上述业务选样是不同问题，不让一个局部计数修复吞掉原业务后继。

<a id="continuation"></a>
### 8.4 唯一合法交接正文

向 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理` 提交本报告、实际证据与配套回交，申请按当前完整I4合同判断G4候选，并明确：
- 可接收的关键G3路径/时间/N对照范围；
- MF-01恢复计数的局部Source/Method冲突是否按受限claim保留，或交实际责任者定向补修；
- 限定发现进入I5的资格，以及重要未完和I6后继由谁按现有权限承担。

请勿将执行自查当作管理Pass，不要因此直接派发超出当前Binding的新阶段。若仅需补修，继续原I4完整任务，只处理管理指出的确切缺口，保留已成、原输入和方法；不恢复旧I4，不重建完整Runner，不把新Case当固定配额。本节是两份回交共同指向的continuation，不另写主控派发或全局计划。

<a id="trigger-g4"></a>
### 8.5 触发事实

`BI01-I4-G4-CANDIDATE`：SATISFIED。当前I4全部约定分析已形成，CF/NI/MF、证据范围、反例和下一问齐备，管理接收待发生。

<a id="trigger-g3-conflict"></a>
`BI01-I3-CONSUMPTION-CONFLICT`：SATISFIED，**只针对MF-01触及恢复计数claim的来源/参考方法不一致**。关键P/L/E/counter/retained路径没有冲突；不将局部问题升级为全包不可用。请求管理确认限定消费或定向补修。

<a id="trigger-change"></a>
`BI01-OWNER-METHOD-CHANGE`：NOT_YET。本轮没有Owner新授权/正式方向变更，没有更新既有正式方法；诊断算法具名独立，Source/Reference差异按上一触发报告，不能冒称正式方法已改。

<a id="trigger-effort"></a>
`BI01-I4-STAGNATION-REVIEW`：NOT_YET（业务条件）。本次R0003实际形成了上述实质结果，并非只有来源/工具/格式准备；没有自行统计运行端历史有效调用或清零其累计投入。运行端EFFORT计数仍应按真实ledger核，管理接收不由本行替代。

<a id="material-use"></a>
## 9. 来源实际读取与使用记录

本轮实际取得并完整读取规定的专业正文；长正文按连续行段读取并补齐截断处。未继承旧I4的“已读/已验/已通过”。附件完整取得并验证包与成员身份，数据按本Case、指定切面及直接依赖定向读取；不声称审计全部历史市场或全部Runner。

### 9.1 授权与方法锁

`daowei2026/observe-iterate`：
- Owner：`caccf69993b6f0c184fc89194476bcd542acb1e0:runs/BI-01-RESTART-01/OWNER_START.md::full`。
- P00–P05：`75d42776a78cd4cbdf3b61bbf86ec93701d06b84:professional/source/` 下
  `00_AGENT_CHARTER_AND_STAGE_CONTRACT.md`、
  `01_I1_I3_PROFESSIONAL_CONTRACT.md`、
  `02_I4_OBSERVATION_AND_CHALLENGE.md`、
  `03_STAGE_HANDOFF_AND_READINESS.md`、
  `04_PRO_WORKER_CODEX_HANDOFF.md`、
  `05_ROLE_GATE_AND_HANDOFF_CONTRACT.md`，均full。
  用于阶段职责、定向核查、事实/假设/无增量分账、挑战、Worker边界、管理Gate与I5交界。
- 当前生效任务及Binding：`465330476ae6091ba9ecacbbadbaf8a4de745dfc:runs/BI-01-RESTART-01/01_当前任务.md::full` 与
  `bindings/QUESTION_WORK_BINDING_I4.json::full`。
- 地图原业务范围：`46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/00_长程推进地图.md::full`。
- 管理采用：`465330476ae6091ba9ecacbbadbaf8a4de745dfc:runs/BI-01-RESTART-01/reviews/MANAGEMENT_DELIVERY_REPAIR_R0002.md::full`。
- 机械恢复证据：`7fc2661166edc91211b769990eda28d2a1e0caae:runs/BI-01-RESTART-01/reviews/WORKMAP_GATE_RESUME_R0002.json::full`。
  只采用已决定边界，不以它代专业事实。
- 回交协议：上述465330版本的`runtime/overlay/13_角色回交与主控接续协议.md`有关共同回交/一致性条款、
  `runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md`有关RETURN/trigger条款及两个schema的对应定义。
  没有替管理改地图、Binding、公共状态或主控操作记录。

### 9.2 用例与领域来源

- [01_首轮实例及子意图1至3上下文.md](https://github.com/daowei2026/complex-systems-vocabulary/blob/fe9656349c8f0aefeeef41c323bec81a688a2d70/docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md)（full）：Q-01、Case身份、参考计算链、候选Δ倍数与参数合法边界；不继承旧执行结论。
- [02_子意图4三类观察情形与挑战.md](https://github.com/daowei2026/complex-systems-vocabulary/blob/fe9656349c8f0aefeeef41c323bec81a688a2d70/docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/02_子意图4三类观察情形与挑战.md)（full）：四层比较、主动挑战、选择偏差、finding卡与阶段交界；已撤图数/固定配额按当前任务处理。
- [C0/N Source→Behavior Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md)（full，blob `7b00e335395c6aceb9fe648512c8f3a61ba2aeb2`）：actual/confirm/knowledge、Episode结束、path公式、N精确窗口和重复证据。
- [C1/S/C2 Relation→Cluster Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md)（full，blob `3b1f55c9a961ce288af09b79edee28a2ae9e042c`）：Formation/Qualification/Validity/Separation分责、混合成熟度、complete-link、Empty与Commit限制。
- [U3 Movement Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md)（full，blob `07a717f6886ddd6775c037d16148a2014bb157f5`）：R02 facts与R03 judgement分离、Working/Completed、§10.3触及恢复、Outcome/Current与no-backfill。

这些是指定冻结的来源正文，不代表把其历史candidate状态升级为当前生产接收。业务合同、参考方法、真实CSV和本轮诊断版本分别保持，没有一次性追latest。

### 9.3 实际数据成员与定位

A 的目录前缀缩写：
- `B0 = baseline_U2_C0_N_C1/`
- `S1 = single_scale_U2_C1_S_C2_U3/`

核心消费：
`B0/C0/02_turn_occurrences.csv`、`04_segment_episodes.csv`、`05_completed_episode_metrics.csv`、
`06_episode_and_working_cuts_30m.csv`；
`B0/N/01_node_behavior_cuts.csv`、`02_node_behavior_metrics.csv`；
`B0/C1/01_equal_actual_uti_candidate_facts.csv`、`03_eight_relation_raw_observations.csv`、`04_member_post_turn_at_common_cut.csv`；
`S1/C1/01_compatibility_method_matrix.csv`、`02_case_eight_relations.csv`、`03_case_formation_and_three_assessments.csv`；
`S1/S/01_case_external_separation_v0.csv`；
`S1/C2/01_case_opportunity_cluster_gates_v0.csv`；
`S1/U3/01_single_scale_shadow_bridge.csv`、`02_movement_r02_objective_facts.csv`、`03_r03_quality_withholding.csv`。

B 的归档根目录与ZIP同名（去.zip），实际核：
每品种`*_kline_30m.csv`、`*_mid_scaleturn_value1_value2.csv`、exact `*_mid_input_zig_small_confirmed.csv`，
以及manifest、数据说明、上游Zig成员身份。没有从最近Zig猜anchor。baseline零actual诊断candidate id
`refonly-d7ea0ed7945a722aaa` 与单尺度case id不同，按actual/member/source绑定对应，不伪装为同一个正式Life。

原结果方法标签：
- C0：`U2_BC41_7.6_RAW_EXACT_PATH`
- N cuts：`MedianTwoWindowV1_RawAndWorking_30m_CUT`
- N metric：保留原CSV的 `MedianTwoWindowV1_N6_MAD_LOO_EXACT` 标签
- C1/S/C2/R02：`STEEL_U2_C1_SINGLE_SCALE_REFERENCE_METHOD_V0.1.0`
- R02时间：`REFERENCE_OBSERVED_30M_BAR_INDEX_NOT_CALENDAR`
- 本轮诊断：`BI01-I4-DIAGNOSTIC-R0003-v1`；仅重算、范围对照、条件敏感性与恢复语义挑战。

没有未读的当前专业必读正文；没有把未取得的生成器代码声明为已读。不能取得/未验证的额外证明只有具名生产实现与正式身份/时钟/参数等边界，已在相关claim中限制，不以标题、hash或来源列表代替专业核查。

### 9.4 复跑与证据包

同目录 `verify_case01.py` 固定两包SHA和Case；运行：
```bash
python verify_case01.py --input-dir /path/to/original-zips --output-dir ./evidence
```

输出包括完整 `EVIDENCE.json`、原R02切片、15条路径核查、common_horizons、knowledge_origin_windows、delta_condition_sensitivity、N统计核查和C0/N重复性CSV、`CHECK_SUMMARY.json`。JSON保留原始ID、actual/knowledge/As-Of、方法、范围和null语义；数值表的显示舍入不是计算替换。

实际运行结果：
`path_rows_verified=15`，`n_metric_rows_checked=90`，`baseline_rows_checked=15`，
`recovery_touch_mismatches=1`。
完整EVIDENCE.json SHA-256：
`b17f77471b578317d3907eec4fcff3065612c04c9a08bab90e53abf2b457559d`。
此摘要不是Gate，只是可复核的脚本结果。整个分析没有生成正式机会簇、H1、Quality、Outcome、资金动作或管理接收。

本轮脚本已在同一冻结输入上独立运行两次，完整EVIDENCE.json字节哈希一致；同时完成Python语法编译检查。运行环境：Python 3.13.5、pandas 2.2.3、numpy 2.3.5。这些是执行自查，不是独立审查或管理Gate。

GitHub持续工作面保存完整本报告、同目录核查脚本及`evidence/CHECK_SUMMARY.json`；本轮随附实物包另含完整`EVIDENCE.json`及所有CSV。原始两ZIP未修改也未复制进Git；下游使用冻结原件可按上述命令重建全部诊断结果。
