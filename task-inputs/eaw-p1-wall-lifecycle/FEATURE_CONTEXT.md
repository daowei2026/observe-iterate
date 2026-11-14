# EawP1WallLifecycleFrp｜特征自身信息、已核来源与待核事实

> **性质**：为 EAW Wall 生命周期合理性分析挑选的特征资料，不是专业结论、实施设计或 Owner GO。主要根据用户 2026-11-14 上传的 `EAW_WallLifecycle_长程任务输入包_20261114.zip` 提取，并对关键概念回查 P1 v1.6.1 需求与指定历史 TIS/FRP 源码。
>
> **证据分级**：**需求基线**只说明设计要求；**源码基线**只说明指定 Git 提交的实现文本；**历史运行记录**不证明本次工作区已经具备相同数据/二进制；**待核问题**不能被下游当作已成立的事实。以上各类不可混用。

## 一、特征是什么（需求与源码均有依据）

| 项目 | 可作为本轮调查起点的内容 | 证据性质 |
|---|---|---|
| 主对象 | `EawP1WallLifecycleFrp`，EAW P1 的 Wall 生命周期产品 Feature，核心业务是维护在**本次运行范围内**由上游认出的同一 Wall 的状态及变化 | P1 v1.6.1 + TIS/FRP 源码 |
| 输入链 | `WallAssembler` 产生上游 Wall 变化；`WallOccurrenceFao` 为 typed ingress；`EawP1WallLifecycleFrp` 根据输入维护正式状态 | P1 架构与源码阅读起点 |
| 身份 | 设计语义是 `Wall FeatureRunIdentity + wall_local_no` 的 run-local Wall 身份，不默认跨运行识别同一堵墙，也不按价格相近重认墙 | P1 Wall DSU 需求；具体序列化及下游引用仍需查 |
| 生命周期 | `WallPresent`、`WallDormant`、`WallEnded`，以及起始、band 更新、出现/休眠状态转换和结束事件；非法或重复变化应有据区分 | P1 Wall DSU + `WallLifecycle.hs` |
| 正式输出 | `wall_occurrences`、`wall_current_view`、`wall_diagnostics` 三路业务/诊断材料 | P1 投影表 + `Publication.hs` |
| current 的含义 | `wall_current_view` writer 存的是**本次变化的 current update**，不等于每个时点复制一份完整 active map；完整 current map 在 DSU 的动态状态中维护 | `Publication.hs` 的代码注释与 `WallLifecycle.hs` |
| 下游关系 | Build/Attack/Absorb 可以消费 Wall 的准确上游身份/产物，但本轮首先研究 Wall 自身 | P1 架构/DSU 需求 |

**不应预置为事实的内容**：当前已经存在可直接给 CAEGraph 使用的 `to_df`、现役生产目录可复用、某段样本出现全部状态、P1 生命周期的实际业务结果合理、历史旧图已经画过这个特征。

## 二、最必要的需求与代码入口（精确基线，不等于现役运行 tuple）

**需求基线**：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f`

- `candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`：实际 v1.6.1 范围纠正；不强加 source correction、跨运行匹配、P1 总产品。
- 同目录 `02_FINAL_P1_ARCHITECTURE.md`：上游 Wall 和并列 P1 产品的职责/依赖。
- 同目录 `dsu/P1-DSU-01_Wall_生命周期_DSU.md`：Wall identity、状态转换和输出合同。
- 同目录 `tables/PYTHON_PROJECTION_TABLES.csv`：三张表的职责及只读投影预期。

**TIS 源码阅读基线**：`daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3`

- `frp/EawBattleP.py`：包含 `EawP1WallLifecycleFrp`、`WallOccurrenceFao`、`_CalculatedP1Product`；此版本 `hold_cal_type()` 返回 `CalType.Cache`，且基础类 `to_df()` 主动抛异常。**这不证明正式物化数据无法读取**：需核实实际 generated wrapper/DBA 读取入口。
- `hf/prel0/wall_assembler.py`：`WallAssembler` 上游生成与参数读取入口。

**FRP 源码阅读基线**：`daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`

- `src/Frp/Instance/ISL/Eaw/P1.hs`：`EawP1WallLifecycleFrp` Fao 注册和 `doWallLifecycleFrp`；**在该源码提交中** `propCalType = const Cal`，与上述 TIS `Cache` 说法存在需查明的运行组合差异。
- `src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs`：状态转移、current map、当前更新和错误类型。
- `src/Frp/Instance/ISL/Eaw/P1/Products.hs`：Wall 类型、run-local identity、occurrence、current view 和 diagnostics。
- `src/Frp/Instance/ISL/Eaw/P1/Publication.hs`：三路正式 writer 的名称/结构和 current-update 口径。

这些路径是**旧提交的调查起点**；管理 Pro 应让执行 Pro 在真实工作区核对实际 checkout、代码/参数、生成/物化数据及执行入口，不能把上面两个代码 SHA 直接拼成“现役可运行版本”。

## 三、历史线索（有记录，但本次不得直接当成立）

来源：`daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f` 的 `candidate_gold_cases/eaw/real_data_feedback/`：

- `EAW_FRP产品Fao真实运行接线与构建Gate经验_20260822.md` 的更新段落记载过 P1 四产品短窗口 `writer → 第二次 load` 成功，**只表示该历史运行报告有此记载**，不是本次运行可复用数据目录的证明。
- `EAW_P1_Wall产品DBA写出内存放大与物理布局Gate经验_20260822.md` 记录了历史一年跨度的 Wall writer 内存增长及主动停止，随后短窗复测又有修正和不同错误。**不能**把一次旧内存峰值误当当前必然故障，也不能据此跳过真实成本核查或直接做大范围重算。

此前 EAW T056/T059/看板 CAEGraph 的 `BP-07/BP-09` 等是**下游 EawBattleP 的观察图**，不是 Wall Lifecycle 的已完成观察材料。是否借用原有图的技术组织方式，由实际调查决定；不得用下游旧图作为 Wall 生命周期已核实的证据。

## 四、为合理性分析准备的“问题线索”，不是预先批准的结论

1. 同一 `wall_local_no` 在实际 run 范围中如何保持身份，出现/更新/结束的时间、event、字段是否一致？哪些同号或重复情形合法？
2. 不同当前状态下的输入变化如何处理：Start、BandUpdate、Present↔Dormant、End、非法或迟到事件；区分业务上“不应发生”与代码当前“确实这样处理”。
3. `occurrences`、`current updates`、`diagnostics` 和动态 active map 的对应关系是否能用真实样本及重要边界场景解释？`wall_current_view` 不得误读为全时点完整快照。
4. 与实际 `WallAssembler` sparse event、receipt 及必要价格/band/core 背景如何对账？如果某种业务判断缺证据，是补源材料、补观察投影还是设计本身需重新审视？
5. 若现有真实材料支持反证、缺失或有界未决，照实交付并给出最小后继；不因为目标叫“合理性分析”就预设必须修改代码、调参或证明合理。

**材料取舍留给专业执行**：上游 receipt/sparse event、三路 P1 结果与必要参照是可能的核心消费者输入，但原 ZIP 的 `MATERIAL_PLAN_SEED.md` / `PRECHECK_CHECKLIST.md` 不是已批准的逐项必做清单；是否需要 trace、Tick/L1、CAEGraph、短窗 Gen，取决于真实问题、已有数据和成本。不能从没有发生过的异常样本推断“diagnostics 正确”。

## 五、与业务任务的关系

本文件不管主控 C/D/W 发送、模型/Project、Owner grants、Run ID 或结果提交策略。业务目标和交付范围见 [BUSINESS_TASK_INPUT.md](BUSINESS_TASK_INPUT.md)，运行方式只从当前 GO 锁定的 `observe-iterate/longrun/`、`control/`、`skills/` 取得。必要时专业负责人可以要求执行 Pro 核实本文件中的疑点；**遇到证据与本文件矛盾时以新查明的原始需求、源码和真实运行结果为准，登记差异，不为保住输入包叙述而改写事实。**
