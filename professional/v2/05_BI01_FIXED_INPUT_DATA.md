# BI-01 V2：本轮固定的事先验算数据、具体文件和取用位置

## 1. 本轮执行决定

**本轮只使用以下两份已经提前准备好的数据包作为业务观察的输入。** 它们是互补的一组：上游 rb/hc/i KLine/Zig/mid 贴近转折，以及下游单尺度 U2/U3 Reference/Shadow 预计算结果。数据不因某个正式算法或 Feature 已实现就被自动重算、替换或扩为新品种。必要时可以核验疑点并反馈，不能悄悄变动固定结果。

### A. 已验算的 U2/U3 下游结果

文件名：`steel_U2_U3_执行结果_20261010.zip`

- **本次实际收到的 ZIP SHA-256：** `7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`；与 2026-10-10 原 I1–I3 底稿记录一致。
- 本包 **23 个 CSV**，CRC 已校验通过；没有可直接运行的全链 U2/U3 Runner 或完整独立 Trace。
- `baseline_U2_C0_N_C1/C0/`：`01_source_confirmation_groups.csv`、`02_turn_occurrences.csv`、`04_segment_episodes.csv`、`05_completed_episode_metrics.csv`、`06_episode_and_working_cuts_30m.csv`。
- `baseline_U2_C0_N_C1/N/`：`01_node_behavior_cuts.csv`、`02_node_behavior_metrics.csv`、`03_window_membership_changes.csv`、`04_metric_details_at_window_changes.csv`。
- `baseline_U2_C0_N_C1/C1/`：`01_equal_actual_uti_candidate_facts.csv`、`02_pair_input_facts.csv`、`03_eight_relation_raw_observations.csv`、`04_member_post_turn_at_common_cut.csv`。
- `baseline_U2_C0_N_C1/S_C2_status/`：`C2_gate_only_NOT_CLUSTER.csv`、`S_outside_domain_only_NOT_ASSESSMENT.csv`。
- `single_scale_U2_C1_S_C2_U3/C1/`：`01_compatibility_method_matrix.csv`、`02_case_eight_relations.csv`、`03_case_formation_and_three_assessments.csv`。
- `single_scale_U2_C1_S_C2_U3/C2/`：`01_case_opportunity_cluster_gates_v0.csv`。
- `single_scale_U2_C1_S_C2_U3/S/`：`01_case_external_separation_v0.csv`。
- `single_scale_U2_C1_S_C2_U3/U3/`：`01_single_scale_shadow_bridge.csv`、`02_movement_r02_objective_facts.csv`、`03_r03_quality_withholding.csv`。

**消费界限：** Reference/Shadow 的 C1/S/C2 和 U3 R02 客观路径事实可供有限业务观察；C2 的正式 OpportunityCluster Commit/H1 不是已完成，R03 Quality 全部 Withheld。不能为了满足“四方面好不好做”自行补 0、伪造完整判断或重做一版数据。

### B. 上游 30m KLine/Zig/mid 贴近转折

文件名：`rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`

- **本次项目附件实际字节 SHA-256：** `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`；CRC 通过，内含 15 CSV + `manifest.json` + `数据说明.md`。
- **历史 2026-10-10 业务底稿记录的 ZIP SHA-256：** `ff3215126461a0cda564c82c4a6e42b99bf94cb7b6a8320df9c8ba93d269d70a`。两者 **整体 ZIP 哈希不一致**，原因未核定。**不得伪称历史 ZIP 与本次字节完全一致，不得擅自换包。** 本次 15 份内部 CSV 均已与本包 `manifest.json` 的各自 SHA-256/字节数比对一致，不能仅凭外部 zip 哈希差异就断言 CSV 内容有误或整批数据不可用。若此差异影响来源资格，记录并反馈 Owner，再据具体影响采取措施。
- Zip 内顶层文件夹同文件名主体，三个品种每个均有：
  - `{symbol}_kline_30m.csv`；
  - `{symbol}_mid_input_zig_small_all_bars.csv`；
  - `{symbol}_mid_input_zig_small_status.csv`；
  - `{symbol}_mid_input_zig_small_confirmed.csv`；
  - `{symbol}_mid_scaleturn_value1_value2.csv`。
- `manifest.json` 声明 `TA_updto20240229`、`night_end_at_2300`、`KLine(freq="30m")`、`ZigZag @ small`（30m close，`retracePct=0.5%`）→ `RctZigWithStatus` → 原始 `ScaleTurnCalendar("mid")`（`specTerm=M`，`stMembershipLine=0.3`），未运行 `FiltedScaleTurnCalendar("mid")`。
- 请求范围：2021-01-01 至 2024-02-29；实际 KLine 索引覆盖 2021-01-04 09:30 至 2024-02-29 15:00。各 9,080 根 30m KLine，**每品种 12 行空 OHLC 原始占位，不应插值**；mid 转折 rb 363、hc 342、i 752，共 1,457。
- 第一轮 `value1` / 第二轮 `value2`、actual/confirm/known、源 Zig 状态不可随便合并或替代。图上可显示上下文，但不能把未来实际点当作当时可知的信号。

## 2. 数据在哪：按使用者区分（不把一个环境冒充另一个）

| 入口 | 本次已知位置 | 可以说什么 / 还须确认什么 |
|---|---|---|
| ChatGPT 项目 `细节叙事生成_金标` Sources / 本项目附件 | 两个以上**完整原文件名**的 ZIP 均已提供；本次可核容器路径 `/mnt/data/<完整文件名>.zip` | 这是本次对话附件可读性证据；不能据此保证另一个专业聊天、手机客户端或 Worker 也已经读到 ZIP 内部 CSV。专业角色应真正读取需要的成员。 |
| 原 I1–I3 记录的 Linux Codex / Worker 路径 | `/m3varK/workspace/资金管理/` 下的同名 ZIP（2026-10-10 文档记录） | **历史位置，当前 Worker 是否仍存在尚未实测。** 真实运行前按文件名与 SHA/manifest 查验，不存在则从本轮固定原件建立受控可读入口，不能偷偷计算新数据替代。 |
| **执行 Codex 当前可用的 aidata 工作区** | `/dwdhome/fy/BASE_E6_2` | **运行环境/工作区位置，不是两份固定 ZIP 的数据所在位置。** 运行时仍需核实目录、所用 aidata 代码与必要依赖和 ZIP 实际读取路径，不能以此路径替代数据身份核验。 |
| GitHub `observe-iterate` V2 分支 | 本文件及业务上下文索引 | **只保存索引和接入合同，不保存两份 ZIP 二进制本体**；不能让 Pro/Worker 误以为阅读本文件就等于取得数据。 |

## 3. 首次消费的最低要求（不是重新验算任务）

1. 实际取得两份固定原件，记录读取路径、校验 SHA、成员数及必要字段；A/B 形成一个固定 `DataBinding`，不得从不同未知版本拼混。
2. 用既有 `aidata` 配置把需要的真实 KLine、U2 位置/成员以及可用 U3 结果画在一起；AI 读取图**对应的结构化数据**，Owner 查看图。数据包原件只读。
3. 若 aidata 只接受 Fao 的 `rerun().to_df()/to_dfs()`，不意味着可以自动重算预计算结果。先核现有导入/适配方法，确实缺通用接口时按 [aidata 工程边界](01_AIDATA_CHART_AND_DATA.md) 定向处理。
4. 如发现明确的验算疑问，报告 `zip/member/row/column/asOf`、与哪个原 Source/方法相冲突、影响哪些图/判断，以及建议的后续核验；**不要将“怀疑”变成默许重新验算全部参考数据**。

## 4. 源信息与复核范围

- 原始 I1–I3 事实底稿：`daowei2026/complex-systems-vocabulary@fix/work-order-boundary-part-a-20260909` 的 `U2U3首轮业务观察实例上下文_20261010/01_首轮实例及子意图1至3上下文.md` §0.1、§3、§4。
- 上面两个 ZIP 的本次外层 SHA 与 B 内部 15 份成员 manifest 一致性，是 **2026-10-17 对当前项目附件字节进行的核查事实**；不等于全链业务独立复算、正式 U2/U3 工程运行或对两个不同 B ZIP 的字节差异解释。
- 本文件用于固定本次观察输入，而不是给新 run 自动签出任何来源批准或业务结论。
