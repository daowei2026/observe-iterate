# BI-01 R0005｜Case-02 成员选择增量检验与 I5 就绪判断

- work_id：`BI-01`
- invocation_id：`BI01-RESTART-01-R0005-427e020c096844a98f9f46148fce405c`
- assignment_token：`8f4678dd01714eb8bc3a9d7f7cfcfe69`
- task_id：`BI01-RESTART-01-I4-EXECUTION-01`
- role / professional_mode：执行 Pro / `OBSERVATION_I4`
- Case：`refonly-671359b4c10f73db5c`
- 当前权威：R0004 管理决定和当前任务 `0c496004729d58ceb2033a14ba20e636b8979027`；Binding `ae2ac32857628e6a8f03e6bc361a14be2d175df1`。
- 本报告是专业结果、自查和限定接收申请，不是管理 G3/G4/G5、独立审查、正式 U2/U3 或 Owner 决定。

<a id="result"></a>
## 1. 核心回答：选出了不同集合，但未证明新的机会边界

**HC/RB 两成员与静态 HC/RB/I 集合的区别是真的；目前这个区别只能解释为“exact actual 相同”，不能升级为“I 没参与同一经济过程”或“剔除 I 后得到更好的机会”。**

在 2021-05-11 10:30，三者都有可读、方向为 Down、净方向推进为正的 Working 路径。I 未在 exact-same-actual 诊断行中，是因为其选定 Peak 的 actual 早五个共同 bar，不是数据缺失、未确认或正式质量否决。

这一组织相对**只贴静态成员标签**，确实增加了明确的转折时间分组与来源定位；相对**在同一可知时点联看三份 C0/N、时间戳和价格路径的基线**，本轮没有找到无法由基线得到的新业务判断。具体证据不是“算法是确定函数所以没价值”，而是：入选理由逐项可由 actual/source 字段重现；I 的排除并不对应不存在 Down 推进；相同观察范围与后继切面也不支持 HC/RB 构成稳定的质量优势组。

一个重要的读取纠正是：**Case-02 所在 baseline C1 已有与 N 对应的路径效率历史中位数差；不能把 Case-01 单尺度 C1 的 `RawNWindowAvailableButNotJoined` 扩大为“所有 C1 都没接 N”。** 这是不同结果载体的事实差异，不重开 Case-01 已接收结论。

当前 Case-02 没有正式 Formation、S assessment、C2、H1，也没有对应 U3 R02/R03 输出。因此可以得到本诊断的有据无增量结论，但不能据此判定完整正式 U2/U3 没有价值。以下完整保留事实、对照、挑战、具体消费者限制和管理后继。

<a id="identity"></a>
## 2. Exact 身份与可消费资格

### 2.1 冻结输入与继承范围

附件 A：`steel_U2_U3_执行结果_20261010.zip`，SHA-256 `7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`。

附件 B：`rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`，SHA-256 `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`。

直接采用 R0004 对包身份、CRC、成员及 Case-01 G3/G4 的接收，不重算 Case-01、不恢复历史 `ff3215...` 原件。脚本仅用固定 hash 防止复跑时误接输入，不据此重新签输入 Gate。

下文简写：`B0=baseline_U2_C0_N_C1/`，`S1=single_scale_U2_C1_S_C2_U3/`；B 内目录为 ZIP 同名去掉 `.zip`。所有 CSV 行号均为**含表头的物理行号**。C0 中的 `source_csv_row`、`zig_confirmed_csv_row` 是不含表头的数据行，定位物理行时加一。

时间沿用原 CSV/UTI；数据源为 `TA_updto20240229`、共同日历 `night_end_at_2300`、30m close、原始 `ScaleTurnCalendar(mid)` value1/value2 与 exact confirmed Zig。原始空 OHLC 保留；本轮使用的所有承重路径均未命中空值。没有插值、删行、引入新 Universe 或替换正式 Calendar。

### 2.2 三个选定转折

| 成员 | turn id | actual / 价格 | 内嵌 confirm point | source occurrence / knowledge proxy | A Turn 行 | B mid / Zig 物理行 |
|---|---|---|---|---|---:|---|
| HC | `refonly-d5b779f4ad88a8a276` | 05-10 21:30 / 6482 | 05-11 10:00 | 05-11 10:30 | 407 | 44 / 145 |
| RB | `refonly-910213b3cc62a71bdf` | 05-10 21:30 / 6087 | 05-10 23:00 | 05-11 09:30 | 44 | 44 / 143 |
| I | `refonly-4af5fd6260f29a3c68` | 05-10 11:00 / 1282 | 05-10 15:00 | 05-10 21:30 | 791 | 86 / 217 |

三条都是 value1 / first-round、Peak / Down。HC/RB actual UTI 为 `75344399`，I 为 `75326399`；在本共同 KLine 网格中相差五个间隔。UTI 差不是正式 business-duration，内嵌 confirm point 也不是本包 source 可见时点。

HC/RB 的共同可见时点取两者 source occurrence 的较晚值，即 **05-11 10:30**。05-10 21:30 时仅 I 的这条 Peak 已可知；HC/RB 的 actual 虽已发生，不能提前把诊断组当作当时已有信号。

### 2.3 诊断、正式 Formation、静态集合与当前 N 是四个对象

| 对象 | 真实结果 | 本轮合法含义 | 不能推出 |
|---|---|---|---|
| same-actual 诊断 | `B0/C1/01_equal_actual_uti_candidate_facts.csv` 行36；HC/RB、Peak/Down、zero lag | exact actual 相等的参考组织事实 | 正式 Formation / OpportunityCluster |
| pair 与两成员路径 | `B0/C1/02_pair_input_facts.csv` 行70；member 文件行87–88 | 同cut原始关系与 Working 事实 | 已经完成方向/类型/Geometry matrix、Δ、Epoch 评价 |
| 静态集合 | 当前研究域 HC/RB/I | 三个固定对象均可读 | 天然属于同一正式机会或各自独立机会 |
| 当前 N | 各自 exact cut 的 Working overlay 与历史窗 | 当前单品种状态、已完成历史 | 以旧 Episode 替代当前状态 |
| Case-02 S 域 | `B0/S_C2_status/S_outside_domain_only_NOT_ASSESSMENT.csv` 行36：outside=I，count=1，预期比较数2 | 已列出研究域内组外对象 | S 已完成或组内优于 I |
| Case-02 C2 | `B0/S_C2_status/C2_gate_only_NOT_CLUSTER.csv` 行36 | 四项 assessment、identity 均 NOT_EVALUATED，physicalization NOT_ISSUED | 正式发布、合法资本依据 |
| Case-02 U3 | S1 bridge/R02/R03 中对应 Case 行数为0，只载有 Case-01 | 本包没有该 Case 的 U3 结果 | 把 Case-01 的 Shadow/Withheld 逐行移植到 Case-02 |

Candidate 的正式状态为 `NOT_ISSUED_SCOPE_MATRIX_DELTA_AND_EPOCH_NOT_EVALUATED`，assessment 为 `NOT_EVALUATED_F29_BC30_BC31`。I 不是正式 `RejectedMember`，也不是 `Pending` 或 `DataUnavailable`；它只是未满足当前 exact-equality 诊断选组条件。S 域存在不等于 S 比较已执行；Case-01 的 outside=0 不适用于本 Case。

<a id="timeline"></a>
## 3. 三视图时间线：当时可知与后来回定分开

### 3.1 原 Down Episode 的回顾身份

| 成员 | 原 Episode id | canonical actual end / 价格 | 完成可见 | 完整长度 h |
|---|---|---|---|---:|
| HC | `refonly-a3fa6d9969b2e3679a` | 05-11 10:00 / 6354 | 05-12 09:30 | 5 |
| RB | `refonly-8ece0d42fdbfb0152a` | 05-10 23:00 / 5928 | 05-11 15:00 | 3 |
| I | `refonly-3e1f6ff2791e56bfc7` | 05-10 23:00 / 1235.5 | 05-11 21:30 | 8 |

这些 end 在各自 completion knowledge 到达前不能使用。三个完整范围不同，不能把其效率直接排列成最终 Quality。

本轮预先固定观察规则：读取 **05-11 10:30 至三个原 Episode 最晚完成可见时点 05-12 09:30 的全部共同 bar**，另保留前段已采用的 05-14、05-18 10:00 日历观察点。共13切面；没有根据表现挑切面，也没有选择第三 Case。

### 3.2 原 Episode 视图的关键切面

P 是按原 Down 方向计算的价格推进，负数表示走向相反方向；E 是绝对净位移/路径长度，不携带方向。h 为相邻价格间隔数，不是连续自然时长。原始价格点只在本品种内部使用。

| As-Of | HC 原段：状态/h，P，E | RB 原段：状态/h，P，E | I 原段：状态/h，P，E |
|---|---|---|---|
| 05-11 10:30 | W6；124；0.704545 | W6；140；0.736842 | W11；46；0.511111 |
| 05-11 15:00 | W11；-50；0.135870 | C3；159；0.987578 | W16；18.5；0.157447 |
| 05-11 21:30 | W12；-4；0.009662 | C3；159；0.987578 | C8；46.5；0.688889 |
| 05-12 09:30 | C5；128；0.744186 | C3；159；0.987578 | C8；46.5；0.688889 |
| 05-14 10:00 | 同一 C5，不延长 | 同一 C3，不延长 | 同一 C8，不延长 |
| 05-18 10:00 | 同一 C5，不延长 | 同一 C3，不延长 | 同一 C8，不延长 |

两成员视图取表中 HC/RB 两列；三成员视图包含 I。两者只是本报告对冻结选定段的观察视图，**不是声称 C1 已为这些后继切面产生组生命周期 revision**。

05-11 15:00，HC 价格6532已高于原起价6482，但其 Down Episode 尚未确认结束，P=-50是合法的反向运动事实。RB 此时知道原 Down 完成，旧段 E 回定为0.987578；当时实际价格6074，并非仍为旧段终价5928。不能用一个成员的新 Working 与另一个旧 Completed 的混合表作“现时谁更顺畅”判断。

05-12 09:30，HC 旧段回定为 C5，E 从长 Working 前缀改为0.744186；当时价格6579，并没有跌回6354。这仍是完成信息到达后的观察范围回定，不是行情突然改善。

### 3.3 当前单品种/N 视图

| As-Of | HC 当前方向 / P | RB 当前方向 / P | I 当前方向 / P |
|---|---|---|---|
| 05-11 10:30 | Down / 124 | Down / 140 | Down / 46 |
| 05-11 15:00 | Down / -50 | Up / 146 | Down / 18.5 |
| 05-11 21:30 | Down / -4 | Up / 67 | Up / 12 |
| 05-12 09:30 | Up / 225 | Up / 141 | Up / 28.5 |
| 05-14 10:00 | Down / 388 | Down / 357 | Up / 16 |
| 05-18 10:00 | Up / 143 | Up / 120 | Up / 55.5 |

每行的 P 依**当前 Episode 方向及起点**计算，因此这些点数不能跨成员或跨不同 Episode 直接比较。

RB 在05-11 15:00切入从05-10 23:00开始的 Up；HC 在05-12 09:30切入从05-11 10:00开始的 Up。I 在05-11 21:30同时收到 value1、value2 两条 Trough：前者 actual 为05-10 23:00，后者为05-11 10:00。当前 N 已读后者，不能假设只收到一个结束点。两条源分别可追到 A Turn 行792/793、B mid 行87/88、Zig 行220/222。

这里阅读后继单品种段仅为分清旧段与当前状态，没有将后来的共同日期另立第三个 Case。

<a id="comparison"></a>
## 4. 时间、成熟度与共同范围：哪些差异保留，哪些缩小或翻转

### 4.1 方法和比较域

本轮诊断方法 `BI01-I4-CASE02-DIAGNOSTIC-R0005-v1`：令 Down 的方向坐标 x=p起−p，P=x末，L=Σ|相邻价差|，E=|P|/L，counter=max(此前方向峰值−当前位置)，retained=P/已达方向峰值。L=0 时 E 不适用；没有有利峰值时 retained 不适用。负推进、负 retained 均保留，不夹为0。

推进百分比=P/p起×100，counter百分比=counter/p起×100，**仅是声明过的价格水平相对变化诊断，不是正式 normalizedAmplitude、波动风险、合约乘数或保证金收益率**。没有使用 MF-01 恢复计数。

| 比较域 | 回答什么 | 限制 |
|---|---|---|
| As-Of lifecycle-true | 当时可以知道的原段/当前段事实 | 同cut不代表同年龄；完成前不用未来end |
| canonical completed | 后来确认完整走成什么样 | HC/RB/I分别h5/h3/h8；不能回填旧cut |
| 各自起点的同h前缀 | 起动后同样经过几个价格间隔时怎样 | 截止的日历时间不同，不能替代共同过程 |
| 05-10 21:30共同起点事件窗口 | 三者在完全相同的价格时段怎样 | 对I不是新正式anchor；越end部分不并入旧Episode |
| 05-11 10:30共同可知后窗口 | 得知完整两成员诊断之后又发生什么 | 不是成交回测、正式Outcome或预测能力证明 |

### 4.2 首个 common cut：原始差异并非全部是成员本身差异

| 范围 | 成员 | h | P / L | E | counter / 起价 | 推进 / 起价 | retained |
|---|---|---:|---|---:|---:|---:|---:|
| 各自原起点→T0 | HC | 6 | 124 / 176 | 0.704545 | 0.339401% | 1.912990% | 0.968750 |
| 各自原起点→T0 | RB | 6 | 140 / 190 | 0.736842 | 0.328569% | 2.299984% | 0.880503 |
| 各自原起点→T0 | I | 11 | 46 / 90 | 0.511111 | 0.819033% | 3.588144% | 0.901961 |
| 共同21:30起点→T0 | I | 6 | 45.5 / 68.5 | 0.664234 | 0.507218% | 3.550527% | 0.900990 |

HC/RB的共同起点与原起点相同，所以无需另算两个“新支持”。共同范围后，I效率仍低于两者，但差距显著缩小；I的相对推进较大、相对counter也较大。它不是没有运动，只是在这些坐标上存在取舍。没有合法 Quality 方法，不能把这些取舍合成一个去留总分。

I 的早五间隔具体是：**1282→1271.5→1282→1282→1282→1281.5**。这段方向净推进仅0.5，路径长度21.5，counter10.5；早五个bar并不等于已经领先完成了一段持续下降。共同21:30到T0的45.5点占其原范围46点的约98.9%。这只解释位移主要发生在哪个范围，不证明经济因果或谁带动谁。

### 4.3 同成熟度前缀

| 各自起点后 h | HC E / 推进% | RB E / 推进% | I E / 推进% |
|---:|---|---|---|
| 1 | 1 / 0.941068% | 1 / 1.281419% | 1 / 0.819033% |
| 3 | 0.719745 / 1.743289% | 0.987578 / 2.612124% | 0 / 0% |
| 6 | 0.704545 / 1.912990% | 0.736842 / 2.299984% | 0.522727 / 1.794072% |

h3 时，I已经经历真实往返，P=0、L=21，故 E=0是**真实净零**，不是空输入；h1三者E=1则只是单个非零增量的算式性质。I 的h3终点为05-10 14:30，HC/RB的h3为当天23:00；同年龄差异提示 I 早段曾往返，但不能证明它不属于后来的共同运动。

h6 所有价格在 T0 都已可读，但按后来canonical范围，HC/RB已越过其最终end；只能作为 T0 当时的 Working 前缀或具名事件诊断，不作为完整段延长。若要求三者都不越后来end的共同成熟度前缀，最长只有h3。

### 4.4 后继端点挑战：组内并未持续优于 I

下表使用统一05-10 21:30起点的独立事件窗口，不随当前Episode切换而重置，也不延长旧Episode，展示每个成员相对同一起点的 **Down推进百分比 / E**：

| common end | HC | RB | I |
|---|---|---|---|
| 05-11 10:30 | 1.912990% / 0.704545 | 2.299984% / 0.736842 | 3.550527% / 0.664234 |
| 05-11 11:00 | 1.511879% / 0.485149 | 2.086414% / 0.625616 | 3.316426% / 0.594406 |
| 05-11 11:30 | 0.694230% / 0.176471 | 1.379990% / 0.341463 | 2.614124% / 0.416149 |
| 05-11 14:00 | -0.647948% / 0.122807 | 0.295712% / 0.057692 | 2.145923% / 0.317919 |
| 05-11 14:30 | -0.509102% / 0.094017 | 0.164285% / 0.031250 | 2.145923% / 0.317919 |
| 05-11 15:00 | -0.771367% / 0.135870 | 0.213570% / 0.040248 | 1.404604% / 0.187500 |
| 05-11 21:30 | -0.061709% / 0.009662 | 1.511418% / 0.228856 | 3.004292% / 0.330472 |
| 05-11 22:00 | -0.647948% / 0.092920 | 0.788566% / 0.107623 | 1.833789% / 0.178707 |
| 05-11 22:30 | -0.709658% / 0.100877 | 0.919993% / 0.123348 | 2.028872% / 0.194030 |
| 05-11 23:00 | -1.589016% / 0.200780 | 0.459997% / 0.058091 | 1.599688% / 0.146953 |
| 05-12 09:30 | -1.496452% / 0.186898 | 0.295712% / 0.036585 | 1.716738% / 0.156028 |
| 05-14 10:00 | 2.992903% / 0.132877 | 5.027107% / 0.213986 | 8.895825% / 0.259091 |
| 05-18 10:00 | 7.574823% / 0.204498 | 7.704945% / 0.210976 | 7.842372% / 0.140265 |

这里没有只保留有利于某个解释的端点。到11:30，I 的共同范围 E 高于 HC/RB；到05-18则再次低于两者。因此“在T0剔除I得到持续更顺畅两成员”的解释不成立；也不成立“I始终更好”。E 是绝对位移比：HC在14:00后多行P为负，不能因E非零而算为 Down 支持。

从共同可知的 **T0** 重新起算，到05-11 15:00，三者的Down推进分别为 **-2.736710%、-2.135531%、-2.224919%**。期间价格整体向上；I的这个反向窗口E恰为1，表示反向路径单调，不表示原Down机会质量好。T0自己的h0为真实净零，E/retained不适用；后续没有正向峰值时 retained 继续不适用，不填0或1。

这些后继都只构成观察挑战。没有交易执行、成本、仓位、因果或可交易收益的结论。

<a id="n-consumer"></a>
## 5. N 是否已有足够信息；未 join 究竟影响哪里

### 5.1 当前路径与历史画像是两种问题

T0三条N Working overlay的 progress、efficiency、counter、extreme updates 与直接KLine/C0一致；HC/RB也与C1 member行87–88一致。单品种基线已经知道三者的当前路径、起点、source可知时间及生命周期。要回答跨成员的关系，仍须**联看**这些单品种信息，不能声称孤立一份 N 就知道其他成员。

N的历史效率并不支持“排除I因为它历史路径更差”：

| 成员 | Recent exact6 中位数 | Previous exact6 中位数 | 变化 | MAD | 最大 LOO shift | N metric物理行 |
|---|---:|---:|---:|---:|---:|---:|
| HC | 0.377075 | 0.534999 | -0.157924 | 0.281495 | 0.222925 | 80437 |
| RB | 0.275691 | 0.397031 | -0.121340 | 0.132888 | 0.104475 | 7797 |
| I | 0.834862 | 0.286526 | +0.548337 | 0.165138 | 0.165138 | 153077 |

这个历史坐标上 I 的中位数较高；而T0自己的当前Working效率较低，二者不矛盾，回答的是不同范围。不能把历史中位数单独升级为I的正式Quality：六个Episode不是等长日历窗，且包含不同方向、不同长度和反方向的净推进。

HC/RB的recent6分别从04-13 21:30开始，I从04-28 22:00开始；I的六个效率中有三个1，其中包括 Case-01 的一步段。HC/RB的历史窗也包含 Case-01 的完整Up段。本轮核的是这三个新的T0窗口及效率统计与已导出C0的一致性，没有重新全历史价格审计。

### 5.2 两个 C1 载体必须分别陈述

| 实际载体 | 原始字段 | 已证明什么 | 仍未证明什么 |
|---|---|---|---|
| Case-01：`S1/C1/02_case_eight_relations.csv` | 15条 `NodeBehaviorComparison` 为 `RawNWindowAvailableButNotJoined` | 该单尺度参考分支尚未给出N比较 | 不能据其他目录有值就宣称这15条已修好 |
| Case-02：`B0/C1/03_eight_relation_raw_observations.csv` 行553 | `raw_observation=0.10138451373947993`；`AvailableEfficiencyMedianDifferenceReference` | 数值等于T0 HC/RB recent效率中位数之差的绝对值；有可读参考比较 | 不是完整多指标N比较或正式关系决策；未核实际producer代码 |

实际复算 `abs(0.377075098814229 − 0.275690585074749)` 与行553一致（浮点误差范围内）。同文件行552又已给当前路径效率差 `0.03229665071770327`。两者不应混成一个差值，前者比较近期已完成窗口，后者比较当前路径。

**具体消费者边界：** Case-01单尺度解释者不能说“此分支已经用N支持了Formation/Quality”；Case-02解释者可以用行553讨论HC/RB一个历史效率坐标的相似/差异，但不能说该数参与了选成员，不能说已经将I作正式组外N比较，也不能说已作多轴Qualification。当前Case-02的I对照是执行Pro在I4中独立读取N形成的业务分析，并未改接C1的公共入口、生成器或消费者。

这是**读取范围的澄清**，不是新发现包身份冲突。R0004已接收的Case-01十五条未join事实和NI-01不因此被推翻。

<a id="increment"></a>
## 6. 四层增量/无增量矩阵

| 层 | 本次实际提供 | 对业务命题的改变 | 限定结论 |
|---|---|---|---|
| 联看单品种 KLine/C0/N | 三者Down路径；不同actual/source；当前/历史；后继换段 | 已足以知道I早五bar但仍共同发生明显Down位移；知道路径与历史坐标不同 | 是本轮强基线；单看一个品种当然不足以作三者关系判断 |
| 静态 HC/RB/I 集合 | 固定研究对象及并列观察范围 | 只有标签时不知道转折来源的exact分组；带完整三品种事实时能复现本次关系判断 | 静态身份本身没有本轮组织证据 |
| exact-same-actual 组织 | HC/RB两成员诊断，pair与源行可追 | 相对标签多了“哪个actual相同”；相对强基线未增加新的成员经济边界或取舍判断 | 有组织/定位价值；不是简单复刻静态名单，但独立业务增量尚未证明 |
| 当前可用U3 | 该Case没有对应R02/R03/bridge；仅本轮有界诊断 | 本次认识无需新U3字段就能得到；不能给不存在的输出记功或判性能失败 | 没有证明U3必要；也没有完成第二次U3质量增量实测 |

分账回答成员选择：

**事实条件**：HC/RB actual相同；I不同且已可读。**方法条件**：当前诊断使用exact equality，而正式Formation需要有效Scope、兼容矩阵、Calendar/Δ、Epoch和assessments。**缺失条件**：后者在本Case未评价/未发布；不是缺I的价格或N。

“组织后多知道了什么”只在较弱基线下成立：知道确切事件同一性与来源，不再仅因板块身份把三者当同一次actual。它不能越级为“同一经济运动”或“重复暴露边界”已经判定。把现有三份事实按明确规则组织起来可以有实际解释价值；本轮未量化人类阅读效率、错误率降低或投资收益，不能把便利程度冒充已验证收益。

<a id="challenges"></a>
## 7. 必要反向挑战与证据依赖

### 7.1 Exact 筛选是否过强

在本共同bar坐标上，HC/RB距离0，I与两者均距离5。仅把时间条件写成“距离≤w”，则：

| 诊断 bound w | HC/RB 时间条件 | I与每个成员时间条件 |
|---:|---|---|
| 0 | 满足 | 不满足 |
| 4 | 满足 | 不满足 |
| 5 | 满足 | 满足 |
| 8 | 满足 | 满足 |

这不是重新运行Formation，不给Case-02绑定Case-01的Δ=2bar，不执行兼容、Epoch或完整complete-link裁定。它只说明：当前名单对时间条件的选择敏感；既有exact诊断不能被当作正式设计唯一允许的成组方式。

I早五bar却直到共同夜盘范围才产生大部分净下降，支持“严格actual分组可能切开一个更宽共同价格过程”的**假设**。没有事件驱动、外力或因果证据，不能确认同一经济原因；同板块的常见共同运动、不同转折定义、I原有高频往返均是替代解释。

### 7.2 其他挑战的结果

| 挑战 | 实际处理与影响 |
|---|---|
| 不同开始时间/成熟度 | T0为h6/h6/h11；同h与共同日历窗分开，I早段往返使原效率差放大 |
| source可知延迟 | 组最早T0可知；T0以后出现共同反向，不能把可知前的下降当成信号后获利 |
| Working/Completed | 三个完成可见不同时，旧段冻结且N当前换段；全表不回填 |
| 端点选择 | T0之后首段所有共同bar均列出，另保留既定日期；效率相对次序会变化 |
| 单位/方向 | 原价点不排名；百分比为诊断；E不带方向，必须连P一起读 |
| 组内优势循环 | exact actual是筛选依据，不能再作为质量证据；同向/类型/Zig不独立累票 |
| N/路径同源 | C0→N overlay→C1路径差共享价格；N历史比较也使用同一C0历史，不算独立多源 |
| formal status | 未正式发布不抹掉真实诊断；真实诊断也不批准正式Formation |
| 组外语义 | I在研究outside域，S比较未执行；不是正式劣势、不参与或数据缺失 |
| 选择偏差 | Case由R0004按预声明时间序挑选，没有按收益择优；只有一个关系区域，不能代表市场 |
| 独立重复性 | Case-02 HC/RB的start恰为Case-01的end，N窗也复用其Episode；不能计作独立随机样本 |
| MF-01 | 恢复计数未读取为业务支持/反证，未修复，也不作为完成前置 |

未发现新的承重 Source/Method/Case 身份或数值冲突。baseline/单尺度载体不同是具名范围澄清；已知formal缺件属于适用边界，不重新触发已经隔离的恢复计数问题。

<a id="findings"></a>
## 8. 具名 findings 与待证假设

### CF-02-01｜CaseFinding：actual边界不等于当前运动参与边界

**命题与范围：** Case-02、T0及所列共同窗口内，I未满足exact actual equality，但仍有真实Down推进；不能按未入exact组把它解释为没参加当前价格过程。

**Raw facts / refs / method：** §2 Turn/候选/member行；B I KLine物理965–976、共同起点物理970；`i_pre_common`和`common_event_windows`；诊断v1。

**支持：** I原起点到共同起点只有0.5净推进、21.5路径长度；随后共同范围45.5推进，T0三者均为可读Down Working。**反证/缺失：** I早段确实不同；无经济原因/因果资料，不能确认就是同一经济过程。**依赖：** 时间、价格与Zig来源相关，不多票计数。

**替代解释：** 较宽共同板块运动、不同转折节奏、相同价格平台后的先后识别。**敏感性/失效：** 变更actual定义或正式时间Scope可能改变名单；不得把诊断重锚I写回原Episode。**未知：** 正式同轮/重复暴露是否应纳入I。**下一行动候选：** 只在管理另授正式边界问题后取得该Case有效Formation方法，不能直接改阈值让I入组。

### CF-02-02｜CaseFinding：T0的两成员摩擦较低印象不是持久质量边界

**命题与范围：** T0共同窗口E为HC0.704545、RB0.736842、I0.664234，但11:30为0.176471、0.341463、0.416149；当前名单不能据此称为持续更顺畅两成员。

**Raw facts / refs / method：** §4完整13-cut表、B各KLine共同起点物理970，T0末物理976、11:30末物理978；`common_event_windows.csv`；诊断v1。

**支持：** 同范围后的I差距缩小；后继次序改变；T0到15:00三者都是对Down的反向位移。**反证/缺失：** T0初始效率差仍是真的；05-18 I效率又低于两者；未作风险/成本归一化。**依赖：** 重叠价格窗口，不能把13切面当13个独立Case。

**替代解释：** 端点选择、真实反向段、不同阶段的摩擦与推进取舍。**敏感性/失效：** 起点换为knowledge或各自actual会改变量；必须同时保留P符号。**未知：** 合法Quality如何评价这些竞争坐标。**下一行动候选：** 当前先保留分坐标认识，不创建统一分数、不展开Quality校准。

### NI-02-01｜NoIncrementFinding：当前exact组织未带来超出联看C0/N的新成员取舍判断

**命题与范围：** 在本诊断输入和本业务问题中，exact组提供事件身份/追溯组织，但未证明独立的机会筛选、质量或经济过程边界增量。

**Raw facts / refs / method：** §2–6；候选行36、pair70、members87–88、N新T0切片、S/C2行36；无新正式方法。

**支持：** 入组原因可从actual直接重现；I可读且有推进；三视图及公平比较没有产生强基线不可替代的取舍；Case-02无U3实际输出。**反证：** 名单确实不是静态三成员，有明确时间身份和定位价值；确定性处理也可能创造有价值的组织认识，不能仅因同源否定。**缺失：** 正式Formation/Separation和消费者使用收益未得到检验。

**依赖/替代解释：** 窄Universe、exact强筛选、当前参考程序覆盖有限，都可能解释未观察到更深增量。**敏感性/失效：** 将来合法关系或组边界在相同基线下改变了业务判断且经挑战仍成立，应在新范围修订结论。**未知：** 完整正式U2/U3价值。**下一行动候选：** 管理可限定接收并结束本次reference成员选择检验；不能把本结论变成停止完整U2/U3的决定。

### DF-02-01｜Design/ConsumerFinding：N比较的使用资格应按真实载体和字段限定

**命题与范围：** Case-01的single-scale分支未join，Case-02的baseline有一个可核历史效率差；两者不能共用一句“C1未接N”。

**Raw facts / refs：** `S1/C1/02_case_eight_relations.csv`的15条既有记录；`B0/C1/03_eight_relation_raw_observations.csv`行553及N metric行80437/7797；§5。

**支持：** 0.10138451373947993可由exact T0 N中位数复算；field knownness明确可用reference。**反证/缺失：** 只看到一个指标的数值对应，formal decision仍Withheld；没有producer代码或完整N多轴组外比较。**依赖：** 同一N/C0，不是新数据源。

**替代解释：** 不同参考批次、不同载体的功能覆盖不同，不能据此断言某公共实现已升级。**敏感性/失效：** 换cut、WindowRef或carrier必须重新精确匹配。**未知：** 正式consumer是否接入全部应有字段。**处置：** 本报告按carrier限定陈述；不改任何生产入口，不宣称原15条已修。**下一行动候选：** 后继消费时使用exact目录/Case/cut/metric，不把工程未接入称为市场Pending。

### H-02-01｜NarrativeHypothesis，而非已证结论

较严格的actual equality可能把较宽的共同价格运动拆成不同诊断轮次；组织的主要价值可能是帮助避免时间和对象错配，而非增加单品种路径事实。I早段接近净零且夜盘共同位移为其提供线索，但两段相邻、同源并且没有经济驱动资料，尚不能确认普遍性或因果。

<a id="case01-relation"></a>
## 9. 与 Case-01 已接收结果的合并边界

| Case-01 认识 | Case-02 的关系 | 合并后可以说什么 |
|---|---|---|
| 生命周期混合会误导 | 支持其风险；本Case又出现各自不同时完成和当前换段 | 保留每条事实的Episode、cut与长度；不是两次独立统计验证 |
| U2提供同轮身份与可追溯性 | 支持并细化：名单这次确实为二而非三 | 不是静态名单重贴标签；但exact事件分组不自动是经济机会边界 |
| NI-01：Case-01 U3未证明独立Quality增量 | 不反证；不伪装为第二次同类U3实测 | Case-01结论保留，Case-02仅说明当前诊断分析不需要新U3字段且缺对应输出 |
| C1 NodeBehaviorComparison未join | 缩窄到Case-01单尺度载体 | Case-02 baseline的历史效率差可用reference；没有修复旧分支 |
| 旧Episode与当前状态须分域 | 支持 | 后来Completed的好看数值不能覆盖当前反向或新Episode |
| H-01避免错配的组织价值 | 提供具体例子，仍非使用效果实验 | 可说明它防止哪类读错，不量化阅读效率或资本收益 |

重要的反向约束：U2本来不负责替U3做质量评分；不能仅以“未选出更高效率组”宣判U2失败。本轮否定的是**从当前exact名单直接推出更深业务边界**，不是否定同轮组织职责本身。

<a id="i5-readiness"></a>
## 10. I5 就绪表与 Owner 边界

| 类别 | 可消费内容 | 资格/限制 |
|---|---|---|
| 可进入I5的发现 | Case-01已接收发现；本报告时间身份、三视图、公平比较、限定NI-02-01和载体差分 | Case-02仍须管理接收；可以直接解释事实，不需Owner倒推CSV |
| 仍只是CaseFinding | I早五bar而夜盘仍明显推进；T0效率差与后继次序改变；完成回定 | 只限两个具名、相邻且有同源依赖的Case，不能外推品种规律 |
| 仍是Hypothesis | 宽经济过程可能跨exact组；组织可能降低错配 | 缺驱动证据、独立重复或实际使用比较 |
| 因具名Source/Method缺件不可判断 | 正式同轮成员、正式Separation、重复暴露、Case-02 U3 Quality | 该Case的有效Scope/矩阵/Δ/Epoch/assessments/H1/R02/R03未给出；不是缺I行情 |
| 当前是否有必须Owner回答的问题 | 没有阻断本轮的Owner问题，也没有已成立的投资/资金取舍 | 不让Owner替AI核一个中位数或批普通cut；不在本轮启动I5 |
| 何时才需Owner | 管理拟改变正式方法、扩大投入/Universe/Quality，或据这些证据调整完整U2/U3方向时 | 必须另行交具体范围与选项，不能本轮代Owner决定 |

**就绪判断：** 已具备向管理提交的完整I4结果和可读的I5输入；“可供I5使用”不等于“必须立即召开Owner审批”，更不等于本轮已完成Owner Pack/G5。建议管理先限定接收，并在“进入I5 / 指定具名补证 / 有据结束或修订本参考观察”之间作决定。不自动追加第三Case，也不把正式工程缺件变成此段的必做前置。

<a id="completed"></a>
## 11. 自查、交付与完整未完

### 11.1 当前任务自查

| 合同义务 | 本轮实物 |
|---|---|
| A exact身份、四对象分账 | §2、source_checks、原候选/pair/member/S/C2行 |
| B 三视图事实过程 | §3；39条原段cut、39条当前N cut；13条直接相关turn源核查 |
| C 成员选择增量与N/U3必要性 | §5–6、NI-02-01、DF-02-01 |
| D 时间/成熟度/方法/依赖/选择偏差挑战 | §4、§7、全部共同bar和明确bound敏感性 |
| E I5就绪 | §10，未代管理启动 |
| 对Case-01影响 | §9，保留已接收事实，只限定载体与外推范围 |
| 具名finding与全部重要未决 | §8及本节 |
| 双Return和唯一continuation | 同目录JSON，统一指向下节 |

执行Pro自查认为本轮已形成可供管理判断的完整专业结果；不自行签G3/G4/G5。

### 11.2 实际执行而非准备

`verify_case02.py` 已在冻结两包实际运行；它是本次有界读取/独立核查，不是旧Case-01 Up脚本直接套在Down，也不是生产Runner。没有Worker工单或Worker执行，没有生产方法、入口或消费者修改。

实际结果：13个As-Of；39条当前路径与C0/N对照最大绝对误差 `9.71445146547012e-17`；3条canonical路径与C0一致；2条C1 member路径一致；T0的3条N效率统计、15个数值最大误差 `1.249000902703301e-16`；13条直接相关source Turn对原mid/exact Zig匹配；承重OHLC空值0；Case-02 U3 R02行数0。

完成Python语法检查，两次独立进程运行的EVIDENCE.json字节一致；另核零路径、反向单调、Down单调的P/E/retained边界。Python3.13.5、pandas2.2.3、numpy2.3.5。最初临时展示代码误将`asof`当属性调用，修为显式列索引后重跑；该展示错误未改变输入或市场解释，交付脚本使用显式列索引。

完整 `EVIDENCE.json` SHA-256：`a4df147e6b7b6f448724cdaceaa0369b38360efaabae9a35037b9b1e69aa2b40`。核查摘要不是Gate，也不是独立审查。

<a id="remaining"></a>
### 11.3 全部重要未完与提交原因

本轮Case-02所约定的A–E和十项交付已形成；提交原因是完整限定问题已经有据回答，并触发管理接收，**不是只完成一个文件/字段或因Case数量收工**。

尚未发生的是管理对Case-02新事实、限定发现与I4后继的接收。完整正式Formation、S/C2/H1、Case-02 U3、跨市场规律、独立审查及I5/G5/I6均未完成/未启动；它们是当前结果的能力与权限边界，不列作本段deferred required。MF-01仍按R0004隔离，不重发修复。

本轮没有新的未解决承重数值或输入身份冲突。若管理要求回答“正式U2应不应纳入I”，必须先给该Case适用的正式Source/Method/执行权限；不能用这份诊断补造。未获管理新任务前，不继续第三Case或进入I5。

<a id="continuation"></a>
### 11.4 唯一合法continuation

提交给 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理`：本完整报告、实测证据、脚本、自查、I5就绪表与双Return。

请管理按R0004及当前完整I4合同判断：

- Case-02事实/诊断的限定可消费范围与CF-02-01、CF-02-02、NI-02-01、DF-02-01；
- Case-01与Case-02合并后的增量边界，尤其baseline/单尺度C1的区别和Case-02无U3输出；
- 下一步进入I5、具名补证，或有据结束/修订当前reference观察。

本回交不代写管理接收、公共工作量或主控派发。若需补修，只继续管理指出的确切缺口，保留已成事实、冻结输入和方法；不重做Case-01、不修MF-01、不自动加第三Case。两份Return共用本节与`#remaining`。

<a id="trigger-result"></a>
### 11.5 本轮触发事实

`BI01-I4-SELECTION-VALUE-RESULT`：SATISFIED，限定成员选择增量/无增量结果和I5就绪边界已形成。

<a id="trigger-effort"></a>
`BI01-I4-SELECTION-EFFORT-REVIEW`：SATISFIED，本次有效专业调用以实际结果回交结束，达到本段一次调用后管理复看条件。没有改写运行端记录；提示中的运行前有效回交数0是其当时事实，最终采纳/计数仍由既有运行端处理。

<a id="trigger-conflict"></a>
`BI01-I3-CASE02-CONSUMPTION-CONFLICT`：NOT_YET，未发现新的承重身份/方法/数值冲突；载体差分、原有formal缺件与隔离的MF-01不冒充新冲突。

<a id="trigger-change"></a>
`BI01-OWNER-METHOD-CHANGE-R0004`：NOT_YET，无新Owner授权、正式方法或DataBinding变更。时间bound实验和事件窗口均为具名诊断，不改正式方法。

<a id="material-use"></a>
## 12. 材料实际采用、来源与复跑

### 12.1 已读复用与本轮读取

本轮在同一专业会话中复用R0003已完整读取、冻结commit未变且关键语义可恢复的P00、Case-01完整报告及三个领域Local Contract。R0003完整报告正文和核查脚本也随本会话保留，Case-01结果使用资格以R0004而非执行自评为准。没有以旧试跑作为事实输入。

本轮新读取：完整R0004决定、当前Binding、当前推进地图、Owner START、P01–P05、两份用例焦点正文；当前任务和P00完整正文在本次消息中取得。三个长领域合同在复用既有完整阅读的基础上，重新读取与本Case承重判断直接有关的正文：C0/N的§7.6–8.9，Relation的§4.2–6.5，Movement的§5.5–7.4。不是声称本轮重新读遍全部长合同。

三个领域文件的实际blob仍分别为 `7b00e335395c6aceb9fe648512c8f3a61ba2aeb2`、`3b1f55c9a961ce288af09b79edee28a2ae9e042c`、`07a717f6886ddd6775c037d16148a2014bb157f5`。稳定语义分别用于方向化路径、eligible exact-N及Working overlay；时间临近/兼容/Formation与N的权力区分；Working/Completed、cut资格与不可回填。

复用证据：`daowei2026/observe-iterate@34d90874ddc9617a4dfecec1f39cbedf54c23845:runs/BI-01-RESTART-01/artifacts/I4_R0003/REPORT.md::#material-use`。没有把生成器源码或正式Case-02方法写成已读取/已实现。

### 12.2 精确来源

- [R0004接收与后继](https://github.com/daowei2026/observe-iterate/blob/0c496004729d58ceb2033a14ba20e636b8979027/runs/BI-01-RESTART-01/reviews/MANAGEMENT_GATE_DECISION_R0004.md)
- [当前完整任务](https://github.com/daowei2026/observe-iterate/blob/0c496004729d58ceb2033a14ba20e636b8979027/runs/BI-01-RESTART-01/01_当前任务.md)
- [当前Binding](https://github.com/daowei2026/observe-iterate/blob/ae2ac32857628e6a8f03e6bc361a14be2d175df1/runs/BI-01-RESTART-01/bindings/QUESTION_WORK_BINDING_I4.json)
- [P00–P05专业合同](https://github.com/daowei2026/observe-iterate/tree/75d42776a78cd4cbdf3b61bbf86ec93701d06b84/professional/source)
- [原用例I1–I3焦点](https://github.com/daowei2026/complex-systems-vocabulary/blob/fe9656349c8f0aefeeef41c323bec81a688a2d70/docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md)
- [原I4比较与挑战](https://github.com/daowei2026/complex-systems-vocabulary/blob/fe9656349c8f0aefeeef41c323bec81a688a2d70/docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/02_子意图4三类观察情形与挑战.md)
- [C0/N Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md)
- [Relation/Formation Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md)
- [Movement Local Contract](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/ed62cd716cd603f0bcc566368c62caec7cdba554/agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md)

旧焦点文档中的历史hash、固定图数/候选Case配额按当前管理处置，不重引为前置。正式方法版本、Reference载体版本和本轮诊断版本分别保留，不追latest。A/B原件的具体成员已写在脚本与证据中，正文关键事实给出可定位的物理CSV行。

### 12.3 复跑与实物

```bash
python verify_case02.py --input-dir /path/to/original-zips --output-dir ./evidence
```

同目录保存完整报告、真实核查脚本、`evidence/CHECK_SUMMARY.json`与关键机器证据；随本轮附件的完整证据包另含`EVIDENCE.json`、39条原段/当前段切片、共同事件/knowledge前缀、成熟度/完整段、source核查、N效率及`OBSERVATIONS.csv`。不复制/修改原始ZIP，不新增控制表，不更改任何管理材料。

本报告中的数值显示舍入不改变计算；机器证据保留原值、输入与成员定位、比较域和不适用状态。后继可以从冻结原件与脚本复建全部结果，而无需由Owner从全量CSV自行倒推本轮事实。
