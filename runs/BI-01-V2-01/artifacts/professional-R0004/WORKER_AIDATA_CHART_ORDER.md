# BI-01 V2 固定数据图与同源数据技术工单

worker_order_id: BI01V2-R0004-AIDATA-FIXED-01
work_id: BI-01
run_id: BI-01-V2-01
issued_by_role: professional
issued_by_invocation: BI01-V2-01-R0004-23dee3405bd9e50d20b28f00
issuer_assignment_token: 41acd7cfe4480f624bb09a27e9365f58
professional_mode: OBSERVATION_SCOPE
status_at_issue: ISSUED_BY_PRO_NOT_YET_DISPATCHED_OR_EXECUTED

## 1. 授权、接续与目标

本工单来自生效完整任务 `daowei2026/observe-iterate@81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/01_当前任务.md#worker`，专业方法为 `observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/03_EXECUTION_HANDOFF.md`。不是新的业务目标或主控派发表。原有操作 Codex 按已有机制收取、去重并交有权 Worker；Worker 的实际调用身份、发送及执行记录由原运行端产生，本工单不声称已经发生。

完整业务目标保持 U2 共同机会位置/成员/可知边界及 U3 Progress、Friction、Retention、ObservabilityAndConstraint 的增量检验。技术任务是把已经冻结的真实价格和预计算结果，通过 aidata 变成 Owner 能实际打开的图，以及执行 Pro 能读取的同图 CSV/图层数据。不能把第一图或某个局部 Case 的成功作为整个工单结束；首个合格图数可先回交供专业消费，已明确其余工作继续。

技术结果回 `chatgpt-project:细节叙事生成_金标/chat:BI01-V2-执行`，执行 Pro 再完成 S3。管理接收、全局预算、独立专业审查不由 Worker 代签。

## 2. 固定输入及工作位置

执行工作区：`/dwdhome/fy/BASE_E6_2`。两包目录：`/dwdhome/fy/资金管理`。

- A：`steel_U2_U3_执行结果_20261010.zip`；SHA-256 `7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`。
- B：`rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`；本次 ChatGPT 实际消费 SHA-256 `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`。

成员身份见同目录 `FIXED_INPUT_MEMBERS.csv`，首次发布 commit `c1599ffa6f64dfb406a6439cb9b9892c65b5cb4d`。B 历史外层 SHA 差异按 V2/05 与管理既有决定保留未知，不开展重验算。Worker 对实际读取文件记录包/成员身份；不同则具名反馈受影响输入，不能偷偷换源。

B 子目录与 ZIP 去掉 `.zip` 后同名。原始 KLine 是每品种 `*_kline_30m.csv`；small Zig 的 all_bars/status/confirmed 和 `*_mid_scaleturn_value1_value2.csv` 保持各自原义。mid 是本包原始 ScaleTurnCalendar，不换成 Filted 或另一正式 Feature。保留 value1/value2、actual/confirm/occurrence 时钟；不插值空 KLine，不填缺失为零。

窗口清单：同目录 `S1_WINDOW_SELECTION.csv`，首次发布 commit `46caec2dfbd762f8ef9004e1f46891eac87a41c9`。缩写展开：

- `A:C1/01` = `baseline_U2_C0_N_C1/C1/01_equal_actual_uti_candidate_facts.csv`。
- `A:C0/02` = `baseline_U2_C0_N_C1/C0/02_turn_occurrences.csv`。
- `A:U3/02` = `single_scale_U2_C1_S_C2_U3/U3/02_movement_r02_objective_facts.csv`。

清单 `physical_row` 一律包含首行表头：首个数据记录是第2行。原 C0 的 `source_csv_row` 是另一字段；本轮 main 锚点实际验证为不含表头的一基数据行，不能直接当物理行。rb/hc main 锚点在 B 的 mid 文件物理43行，i 在83行。原字段不得改写。

## 3. 观察范围与选择理由

### 3.1 广域必须保留的层

保留全部304个 C1 raw 候选的时间/成员/原状态定位和可选窗口入口。205个两成员候选显示固定 Universe 的第三品种；99个三成员候选明确组外为空。第三品种只是待比较对象，不自动获得正式可比资格，不自动属于负例。广域 S 文件的 NOT_EVALUATED 不改成 Separated。

初始深入选择是按 `(年份, member_symbols, source_turn_types, source_expected_directions)` 实际存在层取最早行，另保留 Initial/混合型边界、最大 actual→common-visible 墙钟间隔和最后行。实际得到32个不同候选。此间隔只用于显示选点，不是 Calendar 业务持续时间。用户先前已提供主 Case 数值，且本轮早期预览过最初若干 C1 行，故不宣称盲测；没有按成功结果筛选初始清单。

另有3个明确后验定向挑战：C1物理29行是最早有负向进展记录的三成员候选，33行是最早这类两成员候选，34行用于对照与主 Case 相同 common-visible 时间但不同 actual 锚点。这三项不得倒写成初始盲选。

C0 未覆盖观察按照每品种/每年最早有方向、且 actual_uti 不在任何 C1 候选中的原行选取，共11项。hc在2024没有满足该选择条件的行，不补造第12项。全域共有750条符合上述不覆盖谓词的有方向 C0 记录；不称750个漏掉的机会簇，也不重分组。

清单中的47项是47个请求窗口（含一项完整 Case），不是47张图配额、47个独立机会或完成条件。可以用已有 aidata 可复用页面/节点、选择器和关联视图承载，允许合并重叠价格窗口；必须保留每项可定位口径及逐项同源导出。全304入口和完整目标不被47项取代。

### 3.2 唯一完整参考 Case

`refonly-ad8824a52552d7bffa91`：价格窗口 `2021-04-26 09:30:00` 至 `2021-05-18 15:00:00`；As-Of为5月6/7/11/14/18日10:00，全部保留。广域 C1物理35行另有 `refonly-d7ea0ed7945a722aaa`；可按实际三个 turn refs 建立观察关联，不能宣称两个参考ID就是同一正式 Cluster Life。

图数需同时解释 actual 4月30日15:00、confirm point 5月6日09:30、occurrence/knowledge proxy 5月6日10:00。各 As-Of 的 R02、C1/S/C2、R03 withholding 应直接从固定原行显示，不重新评价。

主比较点：5月11日10:00，hc Working38 bar、rb Completed33 bar、i Completed1 bar。hc与rb实际终点同为5月10日21:30，但完成可知代理分别是5月11日10:30和09:30；i实际终点5月6日09:30、可知代理11:00。展示当时已知范围与事后完整段的区别，而不是预先得出哪个品种最好。

### 3.3 显示窗口与后验边界

除主 Case 外，清单窗口从 actual 位置前12条现有 KLine 行开始，到 common-visible/该 turn occurrence 位置后24条现有行结束，在输入左右边界截断。这只是显示上下文，不是新算法窗口、Outcome Horizon或观察完成判据。三品种使用同一时间范围、自己的价格轴。原 bar_ts/UTI 不重新解释为另一交易日历。

As-Of 之后价格可放在独立后续过程视图；不能当作当时已知。历史完整源行含未来完成可知时间时，保留原件，但在当时视图不绘成已知完成端点；必要标记明确为 retrospective，不伪装当时 current。每层导出其原时间字段、显示范围、As-Of及可见性说明。没有原可知证据的项目保持未知，不由图工具补出权威时间。

## 4. 必须显示和导出的业务对象

价格层：三品种 OHLC、close、原始 small Zig 与 mid 两轮实际/确认点。主图用本品种原价格单位，禁止新增归一化收益曲线替代原路径。

U2层：C0 turn/episode；C1 actual、成员、common-visible、8类原始关系、成员各自 endpoint/Working/Completed；现有 Formation/Qualification/Validity/Separation/Shadow gates逐项原状态。raw不画成正式簇；完整 Case 无组外优势；广域不足完整链不能补主 Case U3。

U3层：R02所有原字段、对应episode/start/end/maturity/As-Of。raw_progress/path_length/max_counter_move是原品种报价单位；path_efficiency/retained_fraction按原无量纲值；observed_bar_elapsed是本包bar间隔数量，不是原生Calendar duration。extreme_count、advance/counter/flat_runs、sign_change_count、completed_recovery_events是数量，不是节奏、密度、恢复时间或质量等级。return_to_origin_progress本批值与raw_progress相同，不能改名为已归一化回归程度。

N对照层：同品种、同As-Of的 N/01 与 N/02，保留recent_exact_6_ids、previous_exact_6_ids、原窗口refs、Working episode及方向。完成后的主Case R02仍留在旧Episode，而N可能已经进入另一个方向段，必须并列标清，不能把两者暗接成同一个Current。

缺项层：R03三个Axis CalibrationPending、quality WITHHELD、NO_FORMAL_H1和LCC未提供原文；未计算的turn density、dwell/recovery时间、跨尺度、U3 recentChange、流动性/容量/成本等明确标未输出，不补算。读取失败、未调用、合法空、未成熟分别保留。

具名单元问题：N/02在5月11日10:00的rb物理7792–7793、hc80432–80433、i153072–153073行中，business_duration/normalized_amplitude没有数值却带unit_semantics=per_symbol_raw_quote。不改固定源；显示端保留raw单位元数据及限制说明，不把未输出时长标成价格、不填值。此问题只影响有关标签/解释，不冻结其他图。

## 5. aidata实际调用与技术自由

先读实际 aidata README、OWNER_INTENT_AND_RATIONALE、TODO、Development Guide、Run Brief/API与本次接入相关现有代码，再直接使用现成能力。V2/01中的 build_chart_run、build_board_run、build_chart_review_requests、render_review_nodes、export_plot_view_data 等仅是导航，以实际公开入口合同为准，不能虚构API调用或CSV导入已支持。

允许在本工单内连续处理正常配置、依赖、固定CSV的合法输入表示、显示选择/连接/类型转换、实际调用和核验。不得用默认节点或空包重新选择Case。不得重跑U2/U3、恢复旧工程、创建新质量/归一化指标或在observe-iterate/cgpterm另建画图/特征切片工具。

确证通用能力缺口后，先核已有能力与TODO，在aidata新独立工作分支修通必要公共生产者/消费者并实际回归回用；原分支受保护。只加helper/类型不算业务图已改接。涉及固定结果、未定业务语义、源生产者写权的改变回原执行Pro/管理；一般技术错误不逐个回批、不自动停工。

AI不视觉看图，不接视觉模型。Worker用其实际具备的页面/浏览器能力验证真实打开和图层，返回文字/结构化检验记录；不能只交一个URL或脚本退出码。当前Pro本地没有上述远程工作区挂载和可调用aidata执行工具；这不是远端环境故障证明，也不要求重测Owner已经检查过的环境。

## 6. 实物、核验与专业消费

每个已交视图需有真实可打开页面/路径及访问前提，实际run/node/timespan/As-Of，aidata代码commit与工作区状态、输入包和成员身份、真实调用记录。对应CSV或图层导出须包含源原行引用、原数值/状态、显示变换和可见性；不同图范围不能共用一个未说明范围的CSV。

实际核查包括：页面打开；三品种各自价格轴和共同时间轴；actual/confirm/knowledge/As-Of标记；Working/Completed端点；未来信息隔离；raw与Shadow/Withheld标记；至少逐项检查所交层存在且来源行正确。批量视图可用现有结构化断言核对象/范围，记录真正执行的结果，不以清单存在冒充检查完成。

重点回传主Case R02物理2–16行和N exact-As-Of对应、C1负向挑战、205个潜在组外对象入口与99个空组外、未覆盖C0原行的同图定位。没有结果的维度写准确文件/字段/时间及原因。

Worker交真实技术回交、全部未完和最新合法接续；执行Pro消费后才能形成与Owner图对应的S3判断。本工单未执行、未专业接收，不自签Gate或完整BI-01完成。
