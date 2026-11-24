# BUSINESS_PROGRESS｜AttackSegment 统计驱动闭环

## 当前任务与真实业务位置

目标仍为 EAW P1 AttackFlowAssembler 当前默认实例，在 rb、m 的 2021 全年正式市场范围完成统计驱动闭环。[唯一业务输入](https://github.com/daowei2026/observe-iterate/blob/9877826236e0995e7255e6cbfedc2d1b89dea6da/task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md)、TIS `179016111ed0394f92025313e46bd13534932a74` 和专业控制 `9877826236e0995e7255e6cbfedc2d1b89dea6da` 均不变。

本轮已有 rb 三产品 35 表严格读回资格；m Wall 已在当前原生 m 上下文、源时间轴和 source_scope 下完成 5 表、receipt、PPID 和源码指纹的只读复用核验。m 两组 F4 在真实执行中均失败，m Attack 尚未启动。

当前绑定为 `INCOMPLETE_WITH_RECORDED_ENGINEERING_GAP`，`formal_complete=false`、`eligible_for_G=false`。原 U 保持 PARTIAL，完整 rb/m X、G 和 Feature 释放均未完成。当前专业责任尚未诊断，下一项由原 E1 执行已存在的偏差诊断 Skill。

## 当前有效成果与失败边界

| 对象／材料 | 当前事实与用途 | 入口 |
|---|---|---|
| 原 U | PARTIAL，核心业务对象、处理链、参数及字段布局可追溯，具名未知与 NOT_EXPOSED 保留 | [原 U 包](https://github.com/daowei2026/observe-iterate/blob/758c77a566672a4514cbff6d3f26236769d17b59/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json) |
| rb 三产品与技术上游 | 沿 C0007 已核当前结果保留；三产品 35 表经 R01 完整只读重算和按列名全量读回有效，既有元数据未变 | [当前完整绑定](https://github.com/daowei2026/observe-iterate/blob/d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0009/FeatureRunResultBinding.json) |
| m Wall | 本次完整只读复用核验通过，未重产 Wall／rb；当前源轴和 source_scope 已核 | 同一绑定及 [C0009 报告](https://github.com/daowei2026/observe-iterate/blob/d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0009/EXECUTOR_REPORT.md) |
| m tactical／structural F4 | 两者均实际执行，在原生交易日 chunk 校验报错；没有完整结果、成功 receipt 或严格读回资格 | 同一绑定及原异常链 |
| m Attack | 缺少有效 F4，未启动，目标目录不存在 | 同一绑定 |
| 失败半成品 | 两组目录共 12 个 DBA，677,239,968 字节；仅为被冻结的失败 effects，不是有效 F4 或 G 输入 | [逐文件失败清单](https://github.com/daowei2026/observe-iterate/blob/d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34/longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0009/evidence/failed_F4_effect_manifest.json) |

## 工程错误与纠正过程

此前默认 `black` 交易集遗漏 m 的运行上下文问题，已在 A05 真实补正：原生 m 交易集实测 `symbols=['m']`、`index=0`、`trading_unit=10`。因此本次记录的是补正上下文后的真实新失败，不是尚未执行的前检状态。

A05 实际取得同一生产锁并释放。m 两组 F4 均在执行后收到原生错误：

`交易日区间在 2021-03-12 00:00:00 前不连续: 1792800 != 1792801`

调用栈经过 `pressure_big_deal.py` 至 `tick_quote_context.py`。这些是执行证据，尚未证明最早责任逻辑或修法；manager 未据堆栈位置作归因。原 rb 结果、m Wall、640 个既存文件及 A01/A02/A03/R01/A04 历史原件核对未变。产品源码、默认业务参数、市场数据和正式范围均未改。

12 个失败 DBA 保留其路径、大小、mtime 和 SHA256；不能覆盖重复 Gen、当成功 receipt 或当作完整结果使用。失败内容也不等于业务行为数量为零。

## 当前问题与后继

本次已成立的是工程执行失败及其业务影响：m 缺有效 F4，目标 Attack 无法建立完整正式结果。原因、责任层和合法处理路线仍需专业诊断；当前没有已确认的上游责任结论、DiagnosisReport 或 UpstreamFinding，也没有 G 的正式 finding 队列。

manager 已为原 E1 签发 [D003](../delegations/D003/DELEGATION.md)，调用锁定版本中已有的 `business-discrepancy-diagnosis` Skill，输入为原正式目标、U 处理链、C0009 真实比较／绑定和失败原件。原 D002 仍未完成，签发调用仍为 C0004；D003 是本次已有 Skill 的独立工作，不表示 G 已完成，也不另建实现修改 Skill 或验收 Gate。

诊断若有证据指向禁止修改的上游，原 E1 按原输入／Skill 形成有据 UpstreamFinding、影响与恢复条件；不得越权修改 F4、Wall、公共模块、市场数据或借用其它 Run 的修复结论。当前不为了运输再 Gen 同一失败目标，不缩窗、换品种、绕过检查或覆盖半成品。

## 保留范围、恢复与阅读入口

原 U 的对象／时间语义、NOT_EXPOSED、分支可达性和参考合同差异继续按原件追踪；局部有效 X 不将 U 自动改为 COMPLETE。尚无 G、业务验收、FeatureReleaseGate 或 UpstreamReleasePackage。

下一动作由 controller 核本 C Return／D003 和原权限后，复用原 E1 派达现有诊断 Skill；专业回交原 manager 后，再依原 Workflow 和合法条件协调原 D002 的剩余工程。任何共享写入仍实际取得原锁，探测不代表预约。独立工作继续，Build 的控制版本、业务成果和诊断结论不混用。

- [当前运行状态、历史及恢复](TASK_PROGRESS.md)
- [本次 manager 报告](../calls/C0010/MANAGER_REPORT.md)

快照：2026-11-24，C0010 已消费真实未完 X 并安排诊断，父 Run IN_PROGRESS。
