# S02｜数据接入与实际版本核查（D002 / C0002）

状态：已完成本步骤；正式版本/历史及独立方向成交证据局部受限，可继续 S03。依据任务书 §3.1、§3.2、§8.0；没有执行 S03 候选检索或 B1/B2/B3 深入对照。

结果目录：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0002/`。机器汇总为 `audit/S02_AUDIT_SUMMARY.json`，逐项路径和 SHA-256 见 `ARTIFACT_INDEX.json`。

## 实际接入的材料

Owner 给定目录：

```text
/home/dw/.codex/visualizations/2026/11/16/01a1e335-cd15-7f72-a7d9-f53c52feb09e/caegraph-delivery-30/caegraph-review/data/
```

已实际读取全部 2,924 个文件，合计 27,947,649 bytes：2,920 个 CSV.gz，加 `manifest.json`、`included_tick_nodes.csv`、`timespans.csv`、`calendar.npz`。manifest 的文件存在性、CSV 字段和行数均匹配，0 项错误。完整文件哈希和实际行数在 `audit/FILE_INVENTORY.csv`；没有新增行情或运行生产特征。

| 范围 | 实查结果 |
| --- | --- |
| Tick 窗口 | 148 个，tick_000001～tick_000148；rb、hc、i，444 个窗口×品种单元全部含可用报价；两侧局部有效性见下文 |
| Tick 时间首尾 | 2021-08-06 14:05:00～2022-03-07 21:32:30（数据内自然时间） |
| 日期 | 29 个窗口起点自然日；按随包日历推定涉及 32 个交易日期，源表没有权威 trading_date 字段 |
| 报价行 | 346,764 行，包含窗口重复；每品种 115,588 行 |
| 去重后 | 328,920 个 symbol/UTI，17,844 行跨窗口重复；重复位置行情字段一致，0 冲突 |
| 其他随包资产 | evidence 33、kline 12、open_segments 1、window_evidence 2,430；只用于来源、字段和范围核查，未将概览多年 K 线或窗口外行情扩为新的研究样本 |

本批是选择性观察窗口，不能用本批窗口或候选比例推断全市场频率。`overview_start/end` 是概览范围，不能拿它扩大本轮 Tick 范围。

## 字段、时间及单位

字段全集和 manifest dtype 见 `audit/SCHEMA_CATALOG.json`；Tick 文件的 CSV 索引 `__index__`、列 `index` 只是存储/窗口行序，不能当全局时间。

| 字段 | 可支持的解释及已核边界 |
| --- | --- |
| timestamp、uti、linear_ts | 与随包压缩日历逐行核对，0 时间或轴不匹配；本批 linear_ts=(uti+1)×500，是交易轴数值，不是 Unix 自然时间。实际自然 Tick 间隔为 0.5 秒，休市处会跳时。 |
| buy_price1/buy_vol1、sell_price1/sell_vol1 | L1 可见买一/卖一价量。只对价格有限且正、数量有限且非负、未交叉的本侧使用；q0 必须大于 0 才计算相对量。买方墙的攻击方向为向下/主卖，卖方墙为向上/主买。 |
| price、trade_volume、open_interest | 随包基础行情值；参考 SubContinuousContract 合同把 trade_volume 定义为 Tick 间成交量。有效记录未发现负值或非整数成交量；有 1 行 i 的相关基础字段非有限。没有逐笔成交、真实买卖方或撤单 feed。 |
| buy_order_price/vol、sell_order_price/vol | 预测主买/主卖代理。当前包主买量非负、主卖量非正，使用方向字段与绝对量；不能把负号当负成交，或把代理相加当总成交。关键数值核查见下一节。 |
| 价格格点 | 本批观察到 rb=1、hc=1、i=0.5；这是包内经验格点，不是已核生产参数或官方合约规格。 |
| 数量/金额单位 | 沿用包内原始数值尺度；未提供量纲、单/双边口径及合约乘数 receipt，不补造人民币金额或跨品种绝对量比较。维度内相对量仍需保留这一来源限制。 |

包名日历为 `night_end_at_2300`。timestamp 没有显式时区字段，本次原样保留数据内自然时间，不补造 UTC 时区标签。只对所需 UTI 从压缩段解析时间，没有展开 calendar_size=103,316,400 的全长数组。夜盘交易日按随包下一日盘日期关联，仅作保守分组依据，并显式标为推定。

## 方向成交代理的关键限制

已在全部有效同侧、同价、连续自然 Tick 配对中作输入质量核查：

- ask：245,810 个同价配对；其中代理或可见损失非零的 116,763 个，全部满足 `abs(buy_order_vol[t]) = max(ask_vol[t-1] - ask_vol[t], 0)`，命中价也全部等于该同价卖一。
- bid：242,416 个同价配对；其中非零的 117,452 个，全部满足对应的主卖代理＝买一可见减少量，命中价匹配。
- 在保留窗口重复的口径下，296,682 行代理总量不等于 trade_volume；7,265 行 trade_volume=0 而方向代理有正绝对量。

这些是**输入同源性核查**，不是市场攻击或补单结论。任务给定参考版本的 `t0/gen/cc.py:120–138` 也将这些列描述为由盘口减少/消失等预测的主买/主卖量；本批生成代码版本尚未证明，但本批同价数值恒等关系已经实查成立。

因此，本批这些方向列不能作为独立于盘口变化的真实主动成交证据。在同价段若直接以其作为 C，`Δq+C` 只会把负向可见变化抵消，不能独立证明新增、撤单或冰山补充。F4/Absorb 展示表中的 proxy 字段也没有取得独立逐笔来源证明，不能用其与盘口代理相互印证来补足独立性。

后续可保留真实可见量、总 trade_volume、这些带来源标签的代理及展示材料，按任务书尝试可执行的检索；依赖真实方向归属的判断须保持局部受限。不要把这一输入限制升级为已经确认的 P1 设计缺陷，或据此跳过其他入口。

## 有效范围、缺失及交易边界

| 核查项 | 实际结果及处理 |
| --- | --- |
| 有效本侧报价 | 含窗口重复：bid 343,590、ask 346,763 行；去重后：bid 325,746、ask 328,919 行。所有 444 个窗口×品种单元仍有可用部分。 |
| 局部不可用 | i 有 3,173 行零买一量且买一价格不可用，另 1 行两侧及基础字段非有限；bid 合计 3,174 行、ask 1 行不进入连续价量配平。这里只标本侧不可见/不可用，不判断其市场原因。 |
| 受影响窗口 | 仅 i 的 tick_000005、tick_000091、tick_000092、tick_000093、tick_000123；rb/hc 无本侧报价无效行。具体位置见 `INVALID_ROWS.csv`，其余范围保留。 |
| 轴与重复 | UTI 无内部缺口、行数与窗口端点预期一致；UTI 连续并不等于自然时间连续。重复行按 symbol/UTI 去重，不能作为独立复现。 |
| 自然时间断点 | 63 个窗口×品种配对断点，均跨随包日历连续段；对应 21 个窗口内断点（各三品种）。9 个窗口跨推定交易日，包含日夜盘及长假边界。 |
| 连续有效索引 | `CONTINUITY_INDEX.csv` 保存本侧有效连续段；`GAP_INDEX.csv` 保存断点。换价仍由 S03 在段内继续分开；不得跨缺失、换价、休市配平，也不把缺少后续行情当无事件。 |
| 窗口首尾 | 首 Tick 没有该窗口以前的可见量基线；片段开端和末端截断必须保留。后续 10/30/60 秒观察等只能使用实际连续可见范围，不能跨夜盘/休市补齐。 |

## 已有特征、实际版本和完整历史

本包 P1 展示来源键为 `9be1111ea7a79a9e604f49e65f24a6c0fa019f8f`。这是 manifest 中的 source_key，**没有证据说明它是 producer Git commit 或 exact artifact ID**。

| 材料 | 本批可读内容 | 非空单元数/444 |
| --- | --- | ---: |
| Wall | 全局 wall_events、wall_segments；本地窗口段含 wall_id、侧、状态、价带、source_start/end 和裁剪后的 start/end | 247（窗口段） |
| F4 战术 / 结构 | 独立资格族展示流、grade、deal_amt、directional_hit_volume_proxy、qualification_code | 394 / 300 |
| Build | build_id、wall_local_no、ratio、level、cum_reload_proxy、baseline_vol、事件/availability/ordinal | 225 |
| Attack | segment_id、wall_local_no、start/business_end、entry/exit、grade/lane、推进/退离、结束原因和展示时间 | 207 |
| Absorb | track_id、wall_local_no、tracked_price、ratio、replenishment_proxy、hit_vol_proxy、事件/结果 | 245 |

统计只是材料存在性与覆盖，不是候选数、独立事件频率或“有/无 Wall”真值。197 个无 Wall 展示段的单元均保持 Wall 状态未知；没有把它们标为无墙。

逐窗口选择在 `FEATURE_AVAILABILITY.csv`：2,214 个特征单元使用 exact window snapshot，450 个用给定全局展示表按当前窗口筛选；有本地窗口快照时优先采用，即使它为空，也不从全局表补造本窗结果。墙区间的 source 边界与展示裁剪边界保留区分。

没有随包取得/验证：producer receipt、实际参数集和 source scope、exact Wall FeatureRunIdentity/上下游 artifact、Wall producer state trace、VolQuant/历史背景量、完整 F3、Attack FormationEvidence/Barrier、完整 FRP typed occurrence/current/history/publication。Attack 表有 uti/ts/plot_uti，但没有独立证明其为真实闭段/发布时点；不能从图上业务段末直接推定当时已可消费。

TIS@179016111ed0394f92025313e46bd13534932a74 与 FRP@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13 仍仅是任务参考。现场 TIS checkout HEAD 为 9161225b653b40a30fc45bd743a77a6525ca9022，存在预有的 `frpExample/STCalendar.py` 修改；本次未使用其工作树运行 producer，未更改该文件。随包绘图脚本只是 SnapshotFeature 读取与绘图绑定，未携 producer 依赖源码或 receipt，不能据其证明本批物化版本。

材料缺口不证明正式产品缺信息，也不证明 FRP 从未运行。后续可以研究可见过程差异并形成适当等级线索；若要确认现行正式表达的第一处损失，需要相容版本、参数、exact upstream 和完整历史补证，不能局部重跑后冒充原正式历史。

## 独立性及发现/复现索引

在读取具体过程数值之前，已依据窗口 metadata 和随包日历冻结 `SAMPLE_ALLOCATION_FROZEN.json`：先合并同一窗口跨越的交易日期，形成 23 个日期关联块；同一块所有品种、窗口同分配。再按各月块起点排序，将序号 1、4、7……（从 0 开始）预留，未用价格、形态、特征结果或后续走势决定分配。

发现侧 95 窗口/285 个窗口×品种单元，预留侧 53/159；预留涉及 7 个日期关联块、11 个推定交易日期。没有强制固定比例；这是同批未来复现机会，不是严格样本外证明。

在此基础上，按同交易日期的窗口重叠、至多 60 秒相邻，以及同一展示 namespace 中反复出现的 Wall/Build/Attack/Absorb local ID 建立 127 个保守过程组索引：发现侧 77、预留侧 50。`WINDOW_PROCESS_INDEX.csv`、`PROCESS_GROUPS.json`、`DEPENDENCE_LINKS.csv` 可追溯每次合并。

127 不是已经识别出的真实攻防过程数，也不保证统计独立。同日跨品种仍可能相关，故保留更保守的日期关联块；local ID 未有 exact source-run 证明，只用于防止重复计证，不能据其断言跨窗口对象身份已正式核实。S03 出现实际连续候选后还须继承并补充真实过程复用关系。

S02 程序仅遍历全批字段、质量、边界及 ID，没有深入查看预留过程的市场形态/后续走势或据此形成候选假设。`CASE_USE_LOG.csv` 当前为空；后续每条候选在第二轮启用预留材料前，应记录已冻结的检索口径/待验证问题和实际使用。若后来按预留结果反复调整，只能称同批探索性复现。

## 自检与后继

执行脚本：`research/audit_s02.py`（标准库）；输入只读；运行汇总、实际字段、无效行、断点、去重和样本索引均已保存。校验记录见 `SELF_CHECK.json`：包含源文件哈希回核、范围/分配互斥、有效段与有效本侧行数守恒等实质检查。

S01＋S02 已满足 D002 规定的本步产出。S03 可以使用此有效范围独立委派，继续任务书三入口全范围程序检索；不能把方向代理当独立成交真值、缺展示当无事件或参考代码当本批版本。S03～S09 本轮均未执行，没有候选迭代点、市场差异或正式缺陷结论。由原 Manager 消费本回交并组织下一项；无需新增 Owner 审批。
