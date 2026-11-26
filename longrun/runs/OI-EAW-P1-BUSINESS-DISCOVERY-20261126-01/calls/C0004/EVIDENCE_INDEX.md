# D002 / C0004 证据与重放入口

本次独立根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261126-01/calls/C0004/`，以下相对路径均相对于此根。大表、图、代码和原始定点读审计保留获准本地目录；正式报告不发布原 Chat 全文。文件大小与 SHA-256 见 `ARTIFACT_INDEX.json`，真实发布/回读见 `publication/`。

## 正式输入与采用依据

- D002 JSON：`daowei2026/observe-iterate@144be4e9b4131ae7b021a6c36af76284a003a461:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/delegations/D002/DELEGATION.json`。
- D002 正文：`daowei2026/observe-iterate@4644ee14551563ec72ebc2808c1f2445305a55ec:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/delegations/D002/DELEGATION.md`。
- 本 C 调用：`daowei2026/observe-iterate@28fb31b515f259b2e59256e7c9ec9edb60fdefb2:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0004/INVOCATION.json`。
- Manager 真实回交：`daowei2026/observe-iterate@f16762119e055ef994712a9cf276778a53dd2a9c:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0003/PRO_RETURN.json`。
- 上述准确本地副本与 Manager 原报告/完整委派在 `sources/`；原路径和 copy SHA-256 在 `SOURCE_INDEX.json`。
- 原 Owner：controller 本地 `OWNER_START.original.md`；原任务全文 `TASK_V0.4.md`；新版 executor guide / TASK_WORK_PRACTICE 位于同 controller 根的 `adopted-observe-iterate/longrun/professional/`。正式 task/guide/protocol 均采用 D002 固定 OI `ff45aab0c8e66e4feb552b2c8a632210d9b58b56`，controller 固定 `0f029333a7fc4b568b5e49a77a5c8ab185baa336`。这些作为既有有效输入复用，不另设审批。

## 已验证源、实际版本和参数

源根 `../C0002/` 保持冻结。正式 C0002 证据索引：
`daowei2026/observe-iterate@77f11f6e5ea4de5ad9e0be1caa3d1312bf4e84c3:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261126-01/calls/C0002/EVIDENCE_INDEX.md`。

来源解析 `../C0002/sources/RESOLVED_SOURCE_PATHS.json`；24 张 receipt、完整参数/上游引用 `../C0002/sources/RECEIPT_INDEX.json`；共同 exact Wall 检查 `../C0002/report/EXACT_UPSTREAM_CHECK.json`；实际源码匹配 `../C0002/report/RECEIPT_CODE_VERIFICATION.json`。本次不改参数、不重新验证 9,537 行，未将展示字段或当前外部 HEAD 当作来源替代。

所有实际 code_version 的 Git 部分为 `git:c747d88a93528fa65cce8f2a6238e1c925bb3b9f`，仍须连同对应 source-sha256 使用：

|组|实际匹配 source-sha256|
|---|---|
|Wall|e5144afcf10de8bda39625157a01b09297410c83dca65321340ad2460497be0d|
|Build|bcc762ed31b3df22c436d3654a1dfbaeb5e96cdb60fcbdefadd6dbad79d73563|
|Absorb|a699d8c95adf6df7fd0dac0dde43ec0964ce4e6c682ec25b30cc2ae114460ded|
|Attack|0be69c60a802982b630ea94523d4ff27a1e0dd51b98c7b53eea4d11c802fd6f5|
|F4|7f718553bf3ab8c420feeb0e198e40c17b0759f50e6287ba79901306f4562444|

匹配源码冻结副本 `../C0002/sources/producer-source-matched/`：

- `build_assembler_core.py:520` 起按 Wall 侧取 best_vol，约 539 行将其固定为 baseline，约 595 行累计量/基准；没有“当前核心价库存”的赋值语义。
- `absorb_assembler_core.py:290` 起定义同价可见量，离档置方法零；329 行起 C/I 与 visible_remaining；约 1293 行 `max(R+C−I,0)`；Started/Milestone/Resolved 的公开属性在其后分支。
- `wall_assembler.py:568` 附近明确 dense state trace 是供下游 producer 使用的私有 trace，不是第五个公开产品。

原始同批行情根保持原入口：
`/home/dw/.codex/visualizations/2026/11/16/01a1e335-cd15-7f72-a7d9-f53c52feb09e/caegraph-delivery-30/caegraph-review/data/`。只用 manifest 指定的 148 窗口×3 品种 quote，抽取六个已有列并去重；本次缓存为 `report/{rb,hc,i}-ORIGINAL_QUOTES.csv`。没有新增行情。参数和代理量的含义不因本次关联而改变。

## 主张到证据的映射

|主张|可核实文件|
|---|---|
|旧 R1 28 例关键切点无当前 Wall，1 例 same core|`report/OLD_R1_ACTUAL_CLASSIFICATION.csv`、`OLD_R1_CUT_POINTS.csv`；旧源根 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0013/`；本根 `cases/R1-*`|
|稀疏历史重建不是漏了另一侧窗口前状态|`report/{symbol}-WALL_CONTEXT.csv`、`sources/WALL_CONTEXT_READ_AUDIT.json`；旧 89 点交叉核对 `OLD_WALL_TRACE_CROSSCHECK.csv` / `PRIVATE_TRACE_POINT_READ_AUDIT.json`|
|867 次同 Wall/核心价复见及条件分母|`report/SAME_WALL_RECONTACTS.csv`、`RECONTACT_SUMMARY.json`；`RECONTACT_ONE_PER_PG.csv`、`RECONTACT_SENSITIVITY.csv`|
|六过程、反例、基准时价角色|`report/N2_CASE_INDEX.json`；`cases/N2-01` 至 `N2-06` 各有 QUOTE_TRACE、WALL/BUILD/ABSORB/FORMATION/BARRIER/SEGMENT_HISTORY、CASE_METRICS、ABSORB_RECOVERY_AT_RETURN；相关 history 是已采集 C0002 同对象资料，不冒称窗口外未读资料完整|
|精选复见对象连续性另有研究交叉核验|`report/N2_WALL_TRACE_CROSSCHECK.csv` 共 18 点；`sources/N2_PRIVATE_TRACE_READ_AUDIT.json`；不作为公开 quantity 输入|
|Absorb 等式/上界/未知及 off-best 边界|`report/ABSORB_QUANTITY_RECOVERY.csv`、`ABSORB_RECOVERY_SUMMARY.json`、`ABSORB_BOUNDARY_CHECK.json`；`cases/CLIP-RB`、`CLIP-HC`、`CLIP-I` 的原 quote/同 track 正式历史/度量原数；`report/CLIP_CASE_INDEX.json`|
|两字段试查与基准选择|`research/RECONTACT_BASIS.json`、`report/N2_TWO_FIELD_PROBE.csv`、`N2_PROBE_SUMMARY.json`；18 PG、54 切点，合成旧量 baseline，不是实际 P2|
|后续走势不支持统一方向结论|`report/RECONTACT_FIXED_HORIZONS.csv`、`RECONTACT_OUTCOME_SUMMARY.csv`、`N2_FIXED_HORIZONS.csv`；各 N2 案例 FIXED_HORIZON_CHECK；截断保留，不扩窗口|
|图可对回原数|`figures/N2_RECONTACT_CASES.png` / `.pdf`；离档断线，Build 基准附自身价格和距复见的年龄，未来部分仅作复盘示意，不用于切点恢复|

PG 和日期关联块复用旧同批 `calls/C0002/audit/WINDOW_PROCESS_INDEX.csv`。PG 去重不等于所有 PG 统计独立；日期块也不能当全市场抽样。

## 重放和核验

使用既有 `/m3c3/Linux/apps/anaconda3/bin/python`，按依赖顺序在本根运行：

1. `research/joint_inventory.py`：原窗口六列缓存、Absorb 原数/恢复依据与代数核对。
2. `research/wall_context.py`：只读精确 Wall DBA 的稀疏时间/侧码索引，窗口内记录及每侧窗口前一条；追加审计，不重跑 producer。
3. `research/classify_old_r1.py`、`research/check_old_wall_trace.py`：旧案例关键切点身份；后者仅 89 个 private 点，无 dense 全值扫描。
4. `research/recontact_wall.py`：同对象/价/连续块复见条件全集与具名恢复方法。
5. `research/recontact_cases.py`：确定性六例与 18 PG 试查、PNG/PDF；需本机已有 Noto CJK 字体。
6. `research/joint_diagnostics.py`：截零实例、阈值敏感性、每 PG 一条、精选 18 个 private 点。
7. `research/recontact_outcomes.py`：原 owner 窗口内固定 10/30/60 秒后续描述。
8. `research/verify_delivery.py`：只读核验表间对应、source 切点/价位/可见状态、公式边界、冻结包和报告数值，输出 `report/LOCAL_VERIFICATION.json`。

重放写独立研究输出，不修改生产。详细正式源已在 C0002 冻结，不必重新取得 receipt 或启动原数据 Chat。所有批量工作限定原 scope/已引用正式源，private trace 仅做二分索引和选中点读取。`ARTIFACT_INDEX.json` 是本次研究快照，排除自身、发布回读、终态进度等可变管理文件；排除项明确记录，不以文件存在替代验证。

本次仍未知：FRP 实际对外 publication、真实 P2 消费行为、独立真实消耗/撤减、稀疏化生产成本及分组预测价值。它们不是本次 source 内恢复的通用前置条件，也不能从已有结果推断已解决。
