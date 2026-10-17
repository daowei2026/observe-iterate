# BI-01 V2 R0004：观察对象、四束字段与原数据发现

work_id: BI-01
run_id: BI-01-V2-01
task_id: BI01-V2-S123-OBSERVATION-01
invocation_id: BI01-V2-01-R0004-23dee3405bd9e50d20b28f00
assignment_token: 41acd7cfe4480f624bb09a27e9365f58
role: professional
professional_mode: OBSERVATION_SCOPE

<a id="result"></a>
## 1. 本次专业结果与资格

**已经完成 S1 的可执行观察问题、选择依据、实际窗口、四个 Movement Bundle 的设计—字段—缺项映射，并签出真实 aidata 技术工单。已经直接读取两份固定 ZIP，形成下文有原行定位的原数据事实和案例层解释。尚未取得实际 aidata 图、同图导出或 Worker 执行回交，不能宣称 S2 完成、AI 看过图、已完成图数对应的 S3，或完整 BI-01 通过。**

最值得随后放到 Owner 图上检验的认识不是“hc/rb/i 谁最好”，而是：同一 As-Of 下的三个 R02 数值可能描述不同终点、不同成熟度的段；部分数值已经包含在 N 中；而同名、同值的数值甚至可以属于相反方向的不同 Episode。先把这些对象和范围放对，才有资格讨论 U2/U3 是否增加业务认识。

完整责任继续覆盖广域 C0/N/C1 raw、唯一完整参考 Case 的全部五个 As-Of、U2位置/成员/边界、U3四束、单品种/静态分组增量、支持与反证及后继。没有以一个 Case 或首图替代终点。本次没有改固定结果、重新计算 U2/U3、修改 aidata、修改管理地图/任务或代签独立审查。

<a id="completed"></a>
## 2. 实际已成与输入身份

实物在本目录：`FIXED_INPUT_MEMBERS.csv`、`S1_WINDOW_SELECTION.csv`、`WORKER_AIDATA_CHART_ORDER.md`及本完整回交。前两份是来源身份和观察选择，不是新的调度控制表。工单 `BI01V2-R0004-AIDATA-FIXED-01` 是本专业者依据生效任务签发的技术任务，尚无实际派发或执行证据。

本次通过项目挂载文件直接读取：

| 包 | 实际字节数 | 本次SHA-256 |
|---|---:|---|
| A：steel_U2_U3_执行结果_20261010.zip | 4112144 | 7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c |
| B：rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip | 1408219 | 4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987 |

两包 ZIP CRC 检查无错误；A的23个CSV、B的15个CSV及manifest/数据说明的本次成员SHA与行数写入身份CSV。没有把哈希检查当成算法正确性或生产资格证明。B的历史外层SHA差异继续沿管理裁定保留未知，不重启全量验算。B实际manifest和说明已读；每品种KLine均9080行，本次三品种bar_ts序列一致，原空OHLC不插值。

本文所有“物理行”包含表头，首个数据记录为第2行；已检查本批CSV的实际文本行数等于数据记录数加表头，没有多行字段造成的行号歧义。C0原字段 `source_csv_row` 与本文物理行不同；main锚点已实际核到 B 中 rb/hc物理43行、i物理83行，不能直接把C0的42/82当物理行。

后文路径缩写：

- `A0` = A包 `baseline_U2_C0_N_C1/`。
- `A1` = A包 `single_scale_U2_C1_S_C2_U3/`。
- `B0` = B包 `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229/`。
- `R02` = `A1/U3/02_movement_r02_objective_facts.csv`。
- `R03` = `A1/U3/03_r03_quality_withholding.csv`。

<a id="s1"></a>
## 3. S1：要检验的业务问题与选择

### 3.1 具体问题、设计期望和主要反例

| 问题 | 原设计期望 | 本次如何观察、什么构成挑战 |
|---|---|---|
| 共同转折的位置是否有意义？ | 同轮组织来自实际转折和相容方向/类型，不是确认时间凑在一起 | 同时显示actual、confirm point、occurrence/knowledge proxy、value1/value2；对照同确认容器中不同actual的点，不能合成一轮 |
| 成员是否在后续仍可共同解释？ | Formation与post-turn Qualification、Validity分开，方向反证不由大幅度补偿 | 比较同一common-visible时刻下每个成员的原Episode、端点、成熟度及原raw进展；明确反向记录是挑战，不等于正式算法已经错组 |
| 第三品种是否被合理留在组外？ | 组外来自完整比较域，内部紧密不能代替外部分离 | 两成员候选把第三品种的真实路径/turn/N并列；同方向接近、相反、尚未确认、缺失分别解释；三成员候选明确固定Universe内无组外 |
| 组织被知道时是否仍有观察价值？ | 实际发生与可知时间分离，后续资料不回填历史 | 检查长确认延迟、Working转Completed、已有段已经结束的情形；不把墙钟跨度当交易持续时间，不把早已结束的段冒充当前运动 |
| U3四束是否改善“好不好做”的认识？ | 推进、摩擦、保持和观察/约束分别贡献信息，不能合成未经验证总分 | 同As-Of对照N和单品种路径，检查重复字段、相反方向的新段、缺失LCC和四束部分输出；高效率的一根间隔是主要反例 |

成功不能定义为事后找出一段涨得漂亮的行情。需要记录支持、反证、没有增量、仅改善组织/追溯以及不能判断的部分。后续图数可以推翻本文初步解释。

### 3.2 广域范围与选点

直接读取原C1全304行，保持全部候选定位。成员构成为 hc|rb 108、i|rb 60、hc|i 37、三成员99；年份分布2021/2022/2023/2024为137/104/57/6。205个两成员候选有固定Universe内的第三品种可观察，99个三成员候选不能制造组外。

初始选择在本轮深入价格路径之前记录：对 `(年份,member_symbols,source_turn_types,source_expected_directions)` 每个实际存在层取最早行，保留Initial/混合边界，追加最大actual到common-visible墙钟间隔和末行，共32个不同候选。最大间隔只用于挑确认延迟挑战，不是U2新指标。已见过用户给的主Case数值和最初若干C1行，不声称盲测；初始选择没有按这些数值挑赢家。

随后明确追加3个后验反证窗口：C1物理29、33、34行；分别针对最早负向三成员、最早负向两成员、与main同common-visible但不同actual位置。没有把这3项倒签为初始选点。

对C0选每品种/每年最早有方向且actual_uti未被任何C1候选覆盖的原行，得到11项；hc的2024年没有符合此谓词的行，不补第12项。该谓词全域命中750条C0记录，只表示不在“同actualUTI候选索引”中，不是750个漏掉的机会簇或召回率。

`S1_WINDOW_SELECTION.csv` 给出全部47个请求窗口：唯一完整Case一项、32个初始广域候选、3个后验挑战、11个未覆盖原turn。它们不是47个独立机会或图数配额。全部304位置/成员仍需保留可观察入口；已有视图可复用/合并窗口，不能以清单画完自签业务完成。

### 3.3 窗口及时间口径

main价格窗口为2021-04-26 09:30至2021-05-18 15:00，五个As-Of为5月6/7/11/14/18日10:00。其他窗口从actual前12条现有KLine行到common-visible/occurrence后24条现有行，在包边界截断；这是显示上下文，不是新Feature窗口或Outcome Horizon。所有窗口同时显示rb/hc/i，各用自己的价格轴，不新算跨品种归一化指标。

主参考Case为 `refonly-ad8824a52552d7bffa91`。A0/C1/01物理35行另有 `refonly-d7ea0ed7945a722aaa`，A0/C1/04物理84–86行可按三个原turn refs连接主Case观察；这只是精确来源关联，不宣布两个ID属于同一正式Cluster Life。

## 4. 四个Movement Bundle：设计—固定字段—缺项—可判范围

依据U3 Narrative V0.3.0、Use Case Card V0.4.0、Source/Metric/Step Witness及Movement Local Contract 0.2候选正文，四束不是四个Allocation接口。下表中的数值只拥有固定Reference资格；没有将候选设计目录名effective视为生产采用。

| 束及设计项 | 固定输入实际字段/来源 | 可以判断与不能判断 |
|---|---|---|
| Progress：净方向推进 | R02 raw_progress；anchor/expected_direction/observed_end | 可描述该段到其自身端点的方向位移；原品种报价单位，不直接跨品种比较幅度大小 |
| Progress：运动持续时间 | R02 observed_bar_elapsed；C0 completed的business_duration_knownness | 有bar间隔数量，没有本批原生Calendar业务时长；不能把38 bar写成19小时交易持续 |
| Progress：极值更新节奏 | R02 extreme_count，N working_prefix_extreme_updates | 有次数，未提供完整更新时点与间隔；次数不等于节奏/速度 |
| Progress：同向连续性 | R02 advance_runs/counter_runs/flat_runs/sign_change_count | 有分段次数，缺各run边界/持续长度；不能据此判长时间连续推进 |
| Progress：近期变化 | R02未输出；N/02有recent_change及exact 6+6窗口 | 可用N作既有单品种基线，不把N近期变化伪装为已输出U3近期变化 |
| Friction：路径效率 | R02 path_efficiency及path_length/applicability | 描述各自测量区间；一间隔效率1不证明长程低摩擦或可交易 |
| Friction：最大反向运动 | R02 max_counter_move | 原报价单位和原区间的逆向负担，不是止损/风险额度 |
| Friction：低一级转折密度 | R02无对应density；B有small Zig原件 | 当前未输出；不能临时用Zig计数/除法补成新特征 |
| Friction：回吐负担 | R02 achieved_peak/retained_fraction及端点 | 有相关事实但无完整独立burden输出；不可把同源字段当独立多票 |
| Friction：快速反转负担 | R02 sign_change_count、run counts | 没有rapid的时间/幅度profile及逐次边界，不输出“快速反转严重”等级 |
| Retention：区域外驻留 | 固定R02无RegionProfile和dwell | 未输出，不能以段长代驻留 |
| Retention：峰值保持 | R02 achieved_peak/retained_fraction | 只在各自Working或Completed范围内成立；Completed=1不是后来As-Of仍保持1 |
| Retention：回到原起点的进度 | R02 return_to_origin_progress | 本15行数值均等于raw_progress；只能作为当前导出的原始位移式字段，不能宣称已有归一化回归程度或新增独立信息 |
| Retention：恢复时间 | R02 completed_recovery_events | 是恢复事件数量，不是恢复时间；缺扰动身份、起止和持续时长，不补算 |
| Retention：跨尺度延续 | 本包单尺度，无该输出 | 未输出，不以缺失判失败；不扩尺度补齐 |
| Observability：样本充分性 | R02范围/阶段；N Available12及exact窗 | 可说明段有多长、N基线历史是否齐；不等于R03质量分类充分性已验证 |
| Observability：确认延迟 | actual/confirm point/occurrence、anchor_knowledge_proxy、completed visibility | 可说明哪个时间才进入本参考可见域；EVENT_TS代理不是历史provider到达证明，也不是原生Calendar延迟值 |
| Observability：数据质量 | R02 path_status/missing_count；C0 coverage；B原空KLine | 能区分本范围已观察与缺失；不能据此宣称所有源生产链完备 |
| Constraint：流动性 | 没有正式LCC事实；R03资本资格Withheld | 未提供。KLine volume/openInt不能自动替代流动性可承载结论 |
| Constraint：容量 | 未提供 | 不默认为无限容量，不给资金分配建议 |
| Constraint：成本覆盖 | 未提供 | 不因路径漂亮判成本已覆盖；交易成本事实同样缺失 |

Witness另外要求parameterSensitivity/missingness等：missing/withheld原状态存在，但本批没有参数敏感性实验结果。缺方法实现、缺输入、阈值未定和未产生正式产品分别保留，不能统称市场Pending。R03全15行的三个Axis为CalibrationPending，quality_judgement为WITHHELD；原因原文为 `NO_FORMAL_H1;AXIS_THRESHOLD_PROFILE_CALIBRATION_PENDING`，资本为 `WITHHELD_LCC_NOT_PROVIDED`。这不是低质量，也不说明只要校准阈值就已具备全部工程条件。

<a id="source-facts"></a>
## 5. 原数据事实及案例层解释（尚未取得S2图数对应资格）

### 5.1 三个时钟不能合并

主Case三个actual锚点均2021-04-30 15:00、UTI75230999，Trough/Up、second-round/value2。confirm point均2021-05-06 09:30、UTI75234599；source occurrence与knowledge proxy是同日10:00。A0/C0/02物理43(rb)、406(hc)、788(i)及B0相应mid物理43/43/83可定位。

rb/hc的B0 mid物理42行与43行在同一occurrence时刻，却分别是4月28日09:30的value1点和4月30日15:00的value2点。i同一occurrence的value1物理82行actual_uti75200399，也不等于value2的75230999。**因此“同一确认到达”不能直接定义同一轮实际转折。**这支持保留原设计actual/known及可分解原点的必要性，不是本次新建成组规则。

### 5.2 38/33/1首先是测量区间不同，不是排名

主Case原Episode：

| 品种 | Episode ref | actual终点 | 完成可知代理 |
|---|---|---|---|
| rb | refonly-9f55eb74da9a4089a7 | 2021-05-10 21:30 | 2021-05-11 09:30 |
| hc | refonly-18ddb757325fb8241e | 2021-05-10 21:30 | 2021-05-11 10:30 |
| i | refonly-22321a4b963e925b7c | 2021-05-06 09:30 | 2021-05-06 11:00 |

来源A0/C0/04物理43、406、788。全历史表中的Completed标签不能回填到更早As-Of。

5月11日10:00，R02物理8–10行：

| 品种 | 当时记录 | 测量结束点 | bar间隔 | raw_progress | efficiency | max_counter | retained |
|---|---|---|---:|---:|---:|---:|---:|
| hc | WorkingSoFar | 5月11日10:00 | 38 | 670 | 0.62267658 | 128 | 0.83959900 |
| i | Completed | 5月6日09:30 | 1 | 51 | 1 | 0 | 1 |
| rb | Completed | 5月10日21:30 | 33 | 707 | 0.86961870 | 19 | 1 |

各数量均原值展示，仅表内小数作阅读舍入；分析不以舍入重算特征。hc相对于rb多包含了完成尚未被知道时的后续可见前缀；i只测量一个早已结束的短段。该表不能支持“i最顺所以最好做”“hc最差所以应该排除”或“38比33更能保持”。主要替代解释是范围、成熟度和确认延迟，而不是算法错误。

### 5.3 hc效率提高包含端点回切，不等于当时市场改善

R02物理11行（5月14日10:00）hc变成Completed33 bar，端点回到5月10日21:30，progress798、path_length904、efficiency0.88274336、max_counter24、retained1。与物理8行的Working38比较，改变的不只是一个评价数字，而是结束点与包含的路径。

B0/hc_kline_30m.csv物理970行（5月10日21:30）close6482，物理975行（5月11日10:00）close6354，物理1011行（5月14日10:00）close6288。不能把R02的798或retained1解释为5月14日当前市场仍在6482、或把0.623到0.883说成新增价格恢复。**合理的解释是完成可知之后对该历史段按实际终点归档；不合理的是把归档后的历史量当当前行情质量。**这是一项使用边界发现，不是已证实的计算错误。

### 5.4 i一bar完成不能说明后续没有运动

R02物理6/9/12/15行的i始终停在5月6日09:30的Completed1 bar、1056到1107。B0/i_kline_30m.csv物理951行5月7日10:00 close1160.5、物理970行5月10日21:30 close1281.5；真实价格在该Episode之后仍继续变化。

这反证“该段短，所以后面没有机会”的读法，也不证明后面的运动都属于同一机会。该差异必须在S2同时展示原锚定段和随后已有N/turn路径；不能扩大原R02窗口重新计算一份质量。

### 5.5 与N的实际增量对照：相同数值、不同对象都要分开

已在15个品种/As-Of组合中连接原N。6条Working R02与同cut N的Episode完全相同，而且raw_progress、path_efficiency、max_counter_move、extreme_count四项数值全部相等：

| R02物理行 | N/01物理行 | 品种/As-Of |
|---:|---:|---|
| 2 | 10019 | hc 5月6日10:00 |
| 3 | 19099 | i 5月6日10:00 |
| 4 | 939 | rb 5月6日10:00 |
| 5 | 10031 | hc 5月7日10:00 |
| 7 | 951 | rb 5月7日10:00 |
| 8 | 10055 | hc 5月11日10:00 |

这些已有数值本身不构成超越N的新独立测量。Completed部分也能回到A0/C0/05的主Episode原指标：rb物理43、hc405、i786。R02新增的一些峰值/保持/run/恢复数量仍来自同一价格路径，不能当作独立多票。是否通过共同锚点和可追溯组织改善业务理解，仍须S2/S3对照；“不是新数值”不等于“绝无组织价值”。

尤其在5月11日10:00：R02物理9行i的+51属于上述早先Up Completed段；N/01物理19135行也写+51，却属于 `refonly-3e1f6ff2791e56bfc7`，是5月10日11:00起、5月10日21:30可知的Down Working段。其方向来自C0原绑定，不是从价格正负猜出。**同名同值不等于同一个业务事实。**若只按数值合并，会同时丢失方向和段身份。

N近期画像也不是主CaseR02的复制。5月11日三品种N/02的path_efficiency近期中位数/相对前窗变化为：rb0.27569059/-0.12134044（物理7789），hc0.37707510/+0.05242256（80429），i0.83486239/+0.54833683（153069）。这些使用各自recent6/prior6已完成段；不能与主锚定段、或彼此不同市场时长的窗口混称同一比较范围。原exact 6+6 IDs必须保留。

### 5.6 广域的真实反证材料，不是算法错误率

A0/C1/01全部304行中，60行的原 `raw_negative_progress_count>0`。这是读取并计数已存字段，不是重算U2、创造新标签或检验正式准确率。raw组的正式状态仍是 `NOT_ISSUED_SCOPE_MATRIX_DELTA_AND_EPOCH_NOT_EVALUATED` 和 `NOT_EVALUATED_F29_BC30_BC31`。

具名挑战：

| C1物理行/候选 | common-visible | A0/C1/04原成员事实 | 必须检验的解释 |
|---|---|---|---|
| 29 / refonly-2a081ad7c13ad30866 | 2021-03-31 11:00 | 物理69–71：hc Working -7；i Completed +51；rb Working +71，Peak/Down | 同actual不保证随后同向，且仍有测量端点差异；不能据raw组宣称正式错组 |
| 33 / refonly-b7c41bdb17f9fd0404 | 2021-04-28 10:00 | 物理79–80：i Completed -5；rb Working +77，Peak/Down；hc为潜在组外 | 原成员有反向事实时，第三品种实际怎样；不能只比较两个成员后下组外优势结论 |
| 34 / refonly-27cb8096d5a3f4bae0 | 2021-05-06 10:00 | 物理81–83：hc +34、i -10.5、rb +69，均Completed；actual是4月28日09:30 | 与main同common-visible但不同actual/轮次及终点；要防止确认时刻将不同组织混在一起 |

因此支持保留原设计的post-turn Qualification与方向反证职责；尚不能说现有正式U2成功排除了这些候选，因为该范围没有相应正式结果。205个潜在组外对照及11个未覆盖原turn仍需真实图数检查，不能由这3例替代广域责任。

### 5.7 完整参考链提供什么、没有提供什么

A1/C1/03五行先为FormationWorking/QualificationPending/ValidityPending，5月7/11为FormationAccepted/QualifiedWorking/ValidityAcceptedWorking，5月14/18为QualifiedCompleted/ValidityAcceptedCompleted，均保持reference、formal_assessment_published=NO。固定值是delta_ref_bars2、pair邻域4、epoch12，不能将其名称解释成已应用原生交易Calendar。

A1/S/01的outside全为0；current-cut为ValidEmptyAlternatives，首cut PendingPersistence、后续ValidEmptyPersistent。它没有证明组外更差。A1/C2/01首cut为SHADOW_HOLD_FOUR_GATES_NOT_SATISFIED，后续为SHADOW_ELIGIBLE_NEEDS_PRIOR_CATALOG_AND_PUBLICATION；prior catalog未完整评估、正式Cluster/H1未发布。A1/U3/01 bridge是PRE_CLUSTER_OBJECTIVE_FACT_PREVIEW及NOT_AUTHORIZED_NO_U2_SNAPSHOT_H1。R03的Withheld不能被上述Shadow通行结果抹去。

本轮依据这些字段说明参考链的可用和不可用，不重判管理已经采用的非正式资格，也不重新生产缺失的输出。

<a id="data-question"></a>
## 6. 具名元数据问题、未提供证据与计算错误分账

**MD-01：单位元数据错误，限展示/解释。**A0/N/02在2021-05-11 10:00，rb物理7792–7793、hc80432–80433、i153072–153073行，metric分别为business_duration和normalized_amplitude，数值为空、knownness分别WITHHELD_CALENDAR_NOT_APPLIED/WITHHELD_NORMALIZATION_PROFILE，却都带unit_semantics=per_symbol_raw_quote。不能用该元数据把未输出的时长或归一化量标成原报价量。

影响是N图层标签、字段字典和S3单位解释，不是已证明错误数值或真实市场现象。固定原件不改；已在Worker工单要求保留原字段，并另标“未输出/单位元数据不适用”，不补值。将这六行位置及影响反馈管理及原参考结果责任者；不要求为此重跑整包或停止其他观察。本次没有审计并宣称全N其他行都已修复。

**证据未提供：**图与同源导出、实际aidata版本/调用/打开验证尚无；广域不存在完整U3链；完整Case没有非空组外；区域驻留、恢复时长、跨尺度、LCC及正式H1/Quality/Outcome等如上分项未输出。缺正式Outcome不能将Completed几何直接改名为已经反馈验证的Quality结果。

**方法范围限制：**原First Edition Profile的Δ是显式业务时长输入，2Δ/6Δ/2Δ/K3-D4Δ与本固定Shadow的2bar基准是不同方法表达。保留两者，不擅自用一个去覆盖另一个，不把参考替代直接判为算错。两包不包含完整U2/U3 Runner与正式生产Trace；本轮未据摘要杜撰实现、未重新验算公式，也未声称得到独立算法正确性证明。

**计算错误：本轮尚未确证新的U2/U3数值计算错误。**38/33/1、效率变化、旧段与新N差异都先按明确范围和生命周期解释；MD-01单列为元数据问题。真正出现具名数值冲突时才回相应文件/行/As-Of有界核对。

<a id="s2"></a>
## 7. S2：已签工单，实际图数尚未取得

已发布 `WORKER_AIDATA_CHART_ORDER.md`，首次commit `5620595ef81ca93f7c708cbfcca0e4dae40410bc`，工单完整列出固定源、全部选择窗口、图层、价格轴/As-Of、同源导出、实际打开和图层检查、N对照、未来信息隔离、缺项及权限边界。

应在`/dwdhome/fy/BASE_E6_2`使用aidata处理`/dwdhome/fy/资金管理`两包。先用现有公开入口；固定CSV合法接入能力由首次实际使用核实，不因缺正式Feature重跑U2/U3。一般配置/依赖/输入表示/调用/核验可连续处理。确需通用修补先核已有能力/TODO并在aidata新独立分支，不能改其原分支或在观察仓做第二套图工具。

当前ChatGPT工具上下文中，这两个远程目录以及共享目录都没有本地挂载；已尝试发现cgpterm/aidata/远程文件或执行能力，未取得可调用的相应工具。GitHub工具可读写业务实物，但不是远程aidata执行器。这里不能伪造Worker发送、页面打开、run/node ID或同图CSV。此事实不否定Owner已经检查过的远端环境，也不是要求重新测试环境。

已成的是可执行技术授权与业务图设计；未成的是实际执行及图数产物。GitHub发布通道可用，未启用H盘ZIP备用运输，未向`H:\fy\observe-iterate-share`写入任何ZIP。

<a id="s3"></a>
## 8. S3：已有原数据支持的方向，以及仍需图数证实的判断

当前可保留的案例层认识是：actual/known分离、Episode身份/方向/成熟度和字段单位确实影响解释；本批U3部分原数值没有超出N，而范围和同源依赖若被隐藏会产生误读。这是专业者读取固定原数据后的解释，不冒称既有R03已发布了这些结论。

需要检验的增量分三层：第一，是否增加原来没有的事实；第二，是否把单品种已有事实按共同起点、成员关系和可知时间组织得更好；第三，是否改变了值得保留/修订/继续观察的判断。第一层目前对6条Working的四个指标明确未见新增独立测量；第二层有可检验的组织价值；第三层尚不能以几张表就宣布完成。

后续S3须逐项处理：U2位置与成员/第三品种的合理性；确认滞后和不同实际转折是否降低当前使用价值；Progress是否只是位移重复、Friction是否受区间/短段主导、Retention是否被Completed端点假象代替、Observability是否充分提示资格与缺失；并列N、单品种行情和静态三品种分组，记录支持、反例、替代解释及真正变化的判断。

可以直接在图展示层保留并实施的方向：把旧锚定Completed段与最新N/价格分开、把同名同值但不同方向的Episode分开、保留As-Of可见性、按count/ratio/raw quote/未输出正确标注。不需要新增U2/U3总分或重算结果。

仍待证的设计方向：共同起点是否提供持续有效的机会观察边界；何时历史锚定段不再适合回答当前“好不好做”；等actualUTI候选之外是否有值得观察的近邻转折。反证条件包括第三品种已有同样组织、所谓分化可完全由成熟度解释、图数范围统一后原判断不再成立、或新增组织没有改变任何有用判断。没有正式输出的设计环节不能据缺失直接宣布失败。

<a id="materials"></a>
## 9. 本轮实际材料使用与版本边界

以下记录的是本轮实际正文读取及用途，不是管理已读状态的继承。分段响应被截断处已补取相关正文；读取不等于Owner接受或生产采用。

**运行/业务方法：**`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615` 的 `professional/v2/README.md`、00_PURPOSE_AND_THREE_STEP_FLOW、04_BI01_BUSINESS_BASELINE、05_BI01_FIXED_INPUT_DATA、06_U2_U3_DESIGN_SOURCE_MAP、01_AIDATA_CHART_AND_DATA、02_OBSERVATION_IDEAS_AND_VALIDATION、03_EXECUTION_HANDOFF完整正文均用于本轮。00/04保持OP-01/Q-01与全S1–S3；05固定包和成员而非替换Feature；06定位下述承重原文；01用于图数同源和不视觉识图；02用于事实/发现/假设及增量/反例分账；03用于当前已签Worker工单和实际结果消费边界。

**实际授权/采用：**OWNER_START全文在`e07034fbab080df85af57da4362d5a24119a8bbe`；management-R0001/DECISION全文在`444179c49ae2f926c287d3bf75b43e1eea44fcfc`；management-R0002/DECISION的采用正文在`f87a9a64f4f0fa3ead13b9ee7c108f87847a581a`；WORKMAP_INTAKE_CURRENT及00_长程推进地图在`81533abbced55b3af14a428dec9cbf8353fc8286`已读。采用其四束映射、空组外、Reference/Withheld和优先级，不自行重判全历史。生效完整任务与Binding来自本次正式发送的81533完整载荷，不用当前分支HEAD替换任务冻结版本。

**原I1–I3：**`complex-systems-vocabulary@fe9656349c8f0aefeeef41c323bec81a688a2d70:docs/network-dynamic-ceps-factory/capital-management-purpose/discuss-materials/U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md`全文已读，blob `5bd81ef05dce01ac36704085d71221c958907b93`。实际采用OP-01/Q-01及N/静态/U2/U2+U3比较依据；旧I4–I6/Gate/状态不继承，旧机器目录也不覆盖V2已改路径。

**原业务设计：**`complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3` 下 `docs/network-dynamic-ceps-factory/` 中以下全文已读：

| 正文 | 在本轮真正承重的用途 |
|---|---|
| OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md | U2边界不等于质量；四Allocation接口与Movement四束分开；不产生资金动作 |
| U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md | 共同实际转折→线段组织→机会边界的人读过程；本文5.1/5.6的挑战依据 |
| U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md | Formation/Qualification/Validity/Separation、候选/正式和反例职责，不把raw行当全链 |
| U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md | Current/Outcome、推进/摩擦/保持与Constraints、同源证据依赖 |
| U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md | 第4节逐字段映射、四资金接口非本轮四方面、未输出项及完整目的 |
| U2_SCALE_TURN_SOURCE_METRIC_STEP_WITNESS_V0.1.0.md | actual/confirm、可分解点、Episode/N到Cluster的真实来源层次 |
| U3_SOURCE_METRIC_STEP_WITNESS_V0.1.0.md | rhythm/density/dwell/recovery与简单count的差别、LCC、Evidence Dependency及Current/Outcome资格 |

**细节方法：**`feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554`，根`agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/`，以下全文已读：

1. `u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md`，blob `7b00e335395c6aceb9fe648512c8f3a61ba2aeb2`。§6–8用于actual/knowledge、Working/Completed、原始/归一化/业务时长、N历史窗及同源指标解释；未借此启动生产实现。
2. `u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md`，blob `3b1f55c9a961ce288af09b79edee28a2ae9e042c`。§4–13用于方向不可补偿、non-transitive、完整outside和commit边界。其BC32修订候选未激活，不能用该旧分支正文冒充本固定结果实际运行算法。
3. `u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md`，blob `07a717f6886ddd6775c037d16148a2014bb157f5`，0.2.0-candidate.1。§6–12用于逐束字段、R02事实/R03唯一判断、Working/Completed；§15/18用于Outcome资格和方法状态；ownerAccepted=false且未应用current CB09，不因effective目录升格。

**触发读取的Profile：**`feature-refinement-implementation-agent-evolution@ea126840aa68701135491572a453bf88e96ca58d:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/mission_a_r28_role_domain_20260917/UPSTREAM_FIRST_EDITION_PROFILE.md`全文，blob `6b433558fa4db41ca5c7c12843a2acb419b6e396`。实际用来区别N=6、Δ业务时长及2/6/2/4倍关系与固定Shadow bar参数。保留NOT_APPLIED/非生产资格，没有把Profile更新传播为全源latest或补算要求。

**返回边界：**`observe-iterate@11626...` 的 `runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md`、`runtime/overlay/13_角色回交与主控接续协议.md`全文已读，用于完整剩余、continuation、非阻塞触发及两份Return。longrun_handoff.schema全文与question_work.schema的本轮Return定义已读取；不声称运行端自动状态迁移已部署或本次运行了其回归测试。

**真实数据消费：**两包成员身份全面记录，解释时直接读取C0/N/C1原行、完整Case C1/S/C2/U3全部五cut、N对照15cut及120条metric、B manifest/说明与有关KLine/mid/Zig字段；广域计数来自全304候选原行。没有用这些源级摘录替代尚不存在的aidata同图数据。未取得的S2技术实物只限制其依赖判断，不冻结已完成S1。

<a id="remaining"></a>
## 10. 完整未完

<a id="s2-missing-input"></a>
S2仍需实际Worker消费已签工单并返回：可打开aidata图、全部相应结构化视图、真实run/node/timespan/版本/As-Of、调用与打开/图层核验。包括主Case全部五cut、广域304入口及已选窗口、第三品种、未覆盖turn、四束实际字段/缺项及N对照。尚未派发/未执行不是市场正常Pending。

S3仍需专业者读取上述真实同图导出，逐项检验U2位置、成员/组外边界、可知及时性和U3四束；形成支持/反证/替代解释、相对N/单品种/静态分组的增量或无增量、每项图和原行定位，以及保留/修订/继续/停止方向。本文原数据发现可以作为起点，不自动作为该阶段已完成结论。

固定资料使非空组外的完整U3、多尺度、LCC、正式H1/Quality/Outcome等暂不能判断；须在最终覆盖中逐项说明影响，不能补值或扩数据。对MD-01的具名反馈保留；原包不修改。完整任务/独立审查/管理及Owner接收均未关闭。

<a id="continuation"></a>
## 11. 最新合法续作与本次停止原因

继续本次81533有效Binding及完整S1–S3工作，沿原same_work路线回 `chatgpt-project:细节叙事生成_金标/chat:BI01-V2-执行`。当前直接动作是由既有运行端收取本目录已签 `WORKER_AIDATA_CHART_ORDER.md`，核真实在途/权限后按已有Worker机制执行；专业任务范围和方法已经明确，不需要再开一轮只重读来源的Pro准备。

Worker依工单在已有工作区直接形成图数；一般配置、输入表示和调用问题连续处理，不重跑U2/U3。首个真实图数回交即可由同一专业Pro消费并继续其余范围。收到技术产物后，首先核主Case测量区间与N对照，再推进广域成员/第三品种/未覆盖turn与四束增量，保留全部未完；第一图不收工。新的影响业务前提或受保护源的矛盾准确回管理，未受影响工作继续。

**本次不能继续到S2实际执行的真实原因是本ChatGPT上下文没有可调用的远端aidata/Worker执行与结果回取能力，且尚无Worker产物可消费；不是S1局部完成即认定整个任务完成，也不是要求Owner重新选择业务方向。**已签完整技术工单与原数据发现已经交出，后继明确；不虚报消息已发或图已生成。

<a id="triggers"></a>
## 12. 触发观察

- BI01V2-FIRST-GROUNDED-OBSERVATION：NOT_YET。没有实际可打开图及同源数据，本文原数据发现不冒充该RESULT触发。
- BI01V2-SUBSTANTIVE-CHANGE：SATISFIED，限MD-01的六行单位元数据矛盾及其N显示/S3解释消费者。依原非阻塞M-REASSESS向既有管理聊天具名反馈；不要求全局重算或暂停其他观察。已知38/33/1、空组外和旧B哈希差异不另伪造为新冲突。
- BI01V2-EFFORT-4：UNKNOWN。派发输入的实际记录是3个有效回交；本回答尚未由运行端收取记账。收到并认定本轮有效后，应按原R0001起点判断是否第4个，不能由本文代写计数、接收结论或清零预算。

<a id="question-work-return"></a>
## QUESTION_WORK_RETURN

```json
{
  "schema": "question-work/v2",
  "kind": "RETURN",
  "work_id": "BI-01",
  "invocation_id": "BI01-V2-01-R0004-23dee3405bd9e50d20b28f00",
  "binding_ref": {"repo":"daowei2026/observe-iterate","commit":"81533abbced55b3af14a428dec9cbf8353fc8286","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#question-work-binding"},
  "focus_results": [
    {"question_id":"S1","completed_ref":{"answer_ref":"#s1"},"remaining_ref":null,"affected_refs":[{"answer_ref":"#source-facts"},{"answer_ref":"#data-question"}]},
    {"question_id":"S2","completed_ref":{"answer_ref":"#s2"},"remaining_ref":{"answer_ref":"#s2-missing-input"},"affected_refs":[{"repo":"daowei2026/observe-iterate","commit":"5620595ef81ca93f7c708cbfcca0e4dae40410bc","path":"runs/BI-01-V2-01/artifacts/professional-R0004/WORKER_AIDATA_CHART_ORDER.md","selector":"full"}]},
    {"question_id":"S3","completed_ref":{"answer_ref":"#s3"},"remaining_ref":{"answer_ref":"#remaining"},"affected_refs":[{"answer_ref":"#source-facts"}]}
  ],
  "material_use_ref":{"answer_ref":"#materials"},
  "trigger_observations":[
    {"trigger_id":"BI01V2-FIRST-GROUNDED-OBSERVATION","state":"NOT_YET","evidence_ref":{"answer_ref":"#triggers"}},
    {"trigger_id":"BI01V2-SUBSTANTIVE-CHANGE","state":"SATISFIED","evidence_ref":{"answer_ref":"#data-question"}},
    {"trigger_id":"BI01V2-EFFORT-4","state":"UNKNOWN","evidence_ref":{"answer_ref":"#triggers"}}
  ],
  "continuation_ref":{"answer_ref":"#continuation"},
  "batch_remaining_ref":{"answer_ref":"#remaining"}
}
```

## ROLE_RETURN

```json
{
  "schema":"longrun-return/v1",
  "work_id":"BI-01",
  "invocation_id":"BI01-V2-01-R0004-23dee3405bd9e50d20b28f00",
  "assignment_token":"41acd7cfe4480f624bb09a27e9365f58",
  "question_work_ref":"#question-work-return",
  "work_status":"IN_PROGRESS",
  "completed_scope_ref":"#completed",
  "remaining_scope_ref":"#remaining",
  "artifact_refs":[
    {"repo":"daowei2026/observe-iterate","commit":"c1599ffa6f64dfb406a6439cb9b9892c65b5cb4d","path":"runs/BI-01-V2-01/artifacts/professional-R0004/FIXED_INPUT_MEMBERS.csv"},
    {"repo":"daowei2026/observe-iterate","commit":"46caec2dfbd762f8ef9004e1f46891eac87a41c9","path":"runs/BI-01-V2-01/artifacts/professional-R0004/S1_WINDOW_SELECTION.csv"},
    {"repo":"daowei2026/observe-iterate","commit":"5620595ef81ca93f7c708cbfcca0e4dae40410bc","path":"runs/BI-01-V2-01/artifacts/professional-R0004/WORKER_AIDATA_CHART_ORDER.md"},
    {"answer_ref":"#result"}
  ],
  "delivery":{"status":"INCOMPLETE","missing_refs":["#s2-missing-input","#remaining"]},
  "materials":{"use_record_ref":"#materials","unread_required":[],"unavailable_required":["#s2-missing-input"]},
  "handoff":{"kind":"CONTINUE","route_key":"same_work","instructions_ref":"#continuation"},
  "role_outputs":{"professional":{"mode":"OBSERVATION_SCOPE","result_ref":"#result","continuation_ref":"#continuation"}}
}
```
