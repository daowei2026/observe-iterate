# BUSINESS_PROGRESS｜AttackSegment 统计驱动闭环

## 当前业务位置

目标仍为 EAW P1 AttackFlowAssembler 默认实例，在 rb、m 的 2021 全年正式市场范围完成统计驱动闭环。[唯一业务输入](https://github.com/daowei2026/observe-iterate/blob/9877826236e0995e7255e6cbfedc2d1b89dea6da/task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md)、TIS `179016111ed0394f92025313e46bd13534932a74`、专业控制 `9877826236e0995e7255e6cbfedc2d1b89dea6da` 与正式参数、SOF、日历均未改变。

原 E1 已完成本项诊断：当前 m 上游输入轴与交易日分块合同不能共同满足正式 F4 运行。完整 X 仍缺 m 的两组 F4、Attack 三产品及严格读回，后续全量统计与 Feature 释放尚未成立。原 U 保持 PARTIAL，父 Run 保持 IN_PROGRESS。

## 本轮查明了什么

此前 m 交易集遗漏已在真实运行中补正，Wall 也已通过完整复用核验；两组 F4 随后实际遇到同一交易日覆盖错误。[原生诊断](https://github.com/daowei2026/observe-iterate/blob/28e8764aab3ce050b6167ad093bbe087574523d3/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D003/C0011/DiagnosisReport.md)进一步确认：半秒输入轴保留了 4 个不属于任何原生交易日区间的时段首条空报价行，覆盖检查因此在逐 chunk F4 业务计算前失败。首处为 2021-03-11 21:00:00.500，输入位置 1792800，而下一交易日区间从位置 1792801 开始。

E1 的真实数据正反对照支持这一直接因果；当前已暴露业务参数及已核数值常量不能改变该覆盖关系。责任定位限于上游输入适配与分块合同衔接，没有判定某个源数据写入者、F4 业务 core 或具体比较式有错，也未指认必须改哪一个文件。

仅在内存去 4 行后 planner 通过 243 日，仍属诊断对照。原输入 9,959,400 行、去 4 行诊断轴 9,959,396 行与现有 Wall 去 17 行轴 9,959,383 行不可混用；该对照不能证明 F4、Attack 或完整统计成功。m Attack 尚未启动。

## 仍有效的成果与保留材料

| 材料 | 当前用途与边界 | 原件 |
|---|---|---|
| 原 U | PARTIAL；处理链、对象、参数与具名未知继续保留，未自动升级为完成 | [U 包](https://github.com/daowei2026/observe-iterate/blob/758c77a566672a4514cbff6d3f26236769d17b59/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json) |
| rb 三产品及技术上游 | 既有三产品 35 表严格读回资格保留，未重新生产 | [现有 X 绑定](https://github.com/daowei2026/observe-iterate/blob/d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0009/FeatureRunResultBinding.json) |
| m Wall | 既有 5 表、receipt、PPID、当前源轴与 source_scope 的完整复用核验资格保留 | 同一 X 绑定 |
| m 两组 F4 与 Attack | F4 实际失败，无成功 receipt 或完整读回；Attack 未启动，完整 X/G 不具备条件 | [真实 X 回交](https://github.com/daowei2026/observe-iterate/blob/d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0009/EXECUTOR_REPORT.md) |
| 失败半成品与历史 | 12 个失败 DBA 共 677,239,968 字节保持失败资格，不可消费或覆盖；E1 记录 652 个既有文件、原 U 及历史原件保持 | [保全核对](https://github.com/daowei2026/observe-iterate/blob/28e8764aab3ce050b6167ad093bbe087574523d3/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D003/C0011/evidence/preservation_check.json)、[原失败清单](https://github.com/daowei2026/observe-iterate/blob/d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0009/evidence/failed_F4_effect_manifest.json) |
| 本项诊断 | 诊断范围已完成，上游问题及受影响工作仍未解决 | [DiagnosisReport](https://github.com/daowei2026/observe-iterate/blob/28e8764aab3ce050b6167ad093bbe087574523d3/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D003/C0011/DiagnosisReport.json)、[UpstreamFinding](https://github.com/daowei2026/observe-iterate/blob/28e8764aab3ce050b6167ad093bbe087574523d3/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D003/C0011/UpstreamFinding.json)、[ScopedBlocker](https://github.com/daowei2026/observe-iterate/blob/28e8764aab3ce050b6167ad093bbe087574523d3/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D003/C0011/ScopedBlocker.json) |

当前 X 绑定仍为 `INCOMPLETE_WITH_RECORDED_ENGINEERING_GAP`，`formal_complete=false / eligible_for_G=false`。诊断完成只改变问题的可解释性和恢复条件，没有产生修复后结果或关闭上游问题。

## 当前局部阻断与恢复

已形成具名上游问题 `UPSTREAM-M-INPUT-AXIS-01`，影响 m 有效 F4、m Attack 和完整 rb/m X/G。修复涉及本 Run 禁止修改的上游责任面，当前没有合法的新上游绑定；受影响动作停止，其他独立 Run 的工作不受此阻断影响。

恢复依 E1 [原生恢复条件](https://github.com/daowei2026/observe-iterate/blob/28e8764aab3ce050b6167ad093bbe087574523d3/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D003/C0011/ScopedBlocker.json)：由具相应合法责任面的上游处理方核定统一合同，取得准确代码、参数、SOF、日历、完整范围、源轴、成功 receipts 和完整读回；同时核 Wall/F4 availability 与 Attack 消费轴一致。上游变更时须说明旧绑定的受影响资格，不能以旧成果证明新版本。

条件满足后，按原 Workflow 回原 E1、原 D002 续接缺失的正式工程；先核 effects，采用新真实调用／attempt 和 fresh 写面，保留失败原件，任何共享生产重新实际取得同一原锁。完整 X 有效后才协调 G。

本次仅把完成诊断与具名局部阻断正式交回 controller，不签发新委派或任务消息，不改产品、不重跑，不创建 Owner 审批。尚无完整 G、FeatureReleaseGate 或 UpstreamReleasePackage，正式 rb/m 全年范围未缩减，Build 成果未混用。

- [真实运行状态、来源与恢复入口](TASK_PROGRESS.md)
- [本次 manager 报告](../calls/C0012/MANAGER_REPORT.md)
- [本次剩余范围](../calls/C0012/REMAINING_SCOPE.md)

快照：2026-11-24，C0012 已消费原 E1 已完成诊断；父 Run IN_PROGRESS。报告、剩余、双进度和原 V2 IN_PROGRESS manager Return 已发布并准确回读，实际发行引用见 TASK_PROGRESS；本次无新派工，具名上游恢复条件仍未满足。
