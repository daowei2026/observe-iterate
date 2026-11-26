# EAW P1 挂单—成交演化：本次 Run 最终成果索引

Run：OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01。本批授权研究已按任务书 §8.4–8.5 结束；S01～S09 实际完成，逐节点由原 Manager 消费，主控已回收最终 Return、原件和真实执行证据。主要发现目标**部分达成、未完全达成**：3 条研究线索，候选迭代点、有充分依据的迭代点、具有初步改进依据的迭代点均为 0；未确认正式缺口、必须修改点或生产 Bug。没有当前专业后继，不签 D011。

## 业务结果与后续问题

以下顺序来自原 Manager 的条件性取证建议，不是已确认研发优先级。

| 线索 | 本次最强可支持认识 | 仍需的关键证据 |
| --- | --- | --- |
| R2 数量角色、基线/参考价、可知时点 | 当前库存、累计代理活动、Build 基线及观测 ratio/level 须区分；已有信息能恢复所检多项区别。 | 相容实际 producer/FRP 版本、参数、receipt、完整正式历史及合法消费切点，先检验联合恢复，才能定位实际首损。 |
| R1 当前、阶段与复见量 | 相近端点/累计量能掩盖中途极薄及早晚形状；完整 L1 和已有联合材料可恢复部分区别。 | 同版本对象身份、切点可得性及正式历史，确认业务重要信息实际何处不可恢复，并评估最小信息成本。 |
| R3 共同来源可识别性 | 同源盘口下降代理不能独立认证真实消耗/补撤，停止本批真实分解。 | 来源量尺、单双边、精确区间、完整覆盖认证及独立方向/订单事件。 |

三入口、三组对照与三条潜力线索均已实际处理；S09 又补查全部第三入口独占 11 片段/17 原区间，没有形成第四条独立设计依据。关键缺证已落在实际正式链及来源认证边界，同批追加相似观察无明显新增认识。依据原任务可以结束本批；不宣称所有研究问题穷尽，也不将零发现写作主发现目标完全达成。

累计 69 次深入提取／66 个过程组／19 个日期块是实际工作量，不是 69 次独立攻击或严格留出验证。选择性窗口不代表全市场发生比例或预测效果。真实消耗/净撤减估计保持 null；没有实际 P2 实物，未证明实际消费错误。

## 可直接阅读的成果

| 原件 | 内容 |
| --- | --- |
| [最终业务报告](https://github.com/daowei2026/observe-iterate/blob/a64775f0e4a355bfa781c31fdd9c7c3a89411650/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0020/EXECUTOR_REPORT.md) | 三条线索的真实过程、图/数值、复现、反例、设计定位及限制。 |
| [统一证据索引](https://github.com/daowei2026/observe-iterate/blob/a64775f0e4a355bfa781c31fdd9c7c3a89411650/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0020/EVIDENCE_INDEX.md) | 全部 S01～S09 的报告、脚本、统计、案例和图的重放入口。 |
| [实际完成证据](https://github.com/daowei2026/observe-iterate/blob/a64775f0e4a355bfa781c31fdd9c7c3a89411650/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0020/report/COMPLETION_EVIDENCE.json) | 原步骤覆盖、逐条工作与主动补查的实物依据。 |
| [最终结果及限制](https://github.com/daowei2026/observe-iterate/blob/a64775f0e4a355bfa781c31fdd9c7c3a89411650/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0020/report/FINAL_RESULT.json) | 准确等级、目标达成程度、结束原因与条件性后续。 |
| [Manager 最终消费报告](https://github.com/daowei2026/observe-iterate/blob/e7d78c62cd2b7d561b363bbcfbaad08e2f44f378/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0021/MANAGER_REPORT.md) | 原 Manager 的实际消费、业务状态及无 D011 的判断。 |
| [原任务结束依据](https://github.com/daowei2026/observe-iterate/blob/e7d78c62cd2b7d561b363bbcfbaad08e2f44f378/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0021/RUN_END_BASIS.json) | 对照 §8.4–8.5 的逐项事实与恢复条件。 |
| [主控实际回收记录](https://github.com/daowei2026/observe-iterate/blob/2cc2771529a41a4d1818e700a280a13cc761431d/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/CONTROLLER_RECOVERY.json) | V2、身份/真实回执、原件/hash、终态行动及归档欠账。 |
| [资源释放记录](https://github.com/daowei2026/observe-iterate/blob/50a5681a6d654f8ceca5e9e23a14c47ba493a032/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/CURRENT_RESOURCE_STATUS.json) | 两角色队列空、Goal 空，无在途副作用，工作区占用已释放。 |
| [当前资源登记更新](https://github.com/daowei2026/observe-iterate/blob/2f250ff2ef70579da5c7d747dc04ee934c971e3a/longrun/controller/RUN_REGISTRY.json) | 仅移出已释放的本 Run；历史 Binding、成果和其他 Run 保留。 |

BUSINESS_PROGRESS.md 和 TASK_PROGRESS.md 的 Manager 业务版在 [e7d78c6](https://github.com/daowei2026/observe-iterate/blob/e7d78c62cd2b7d561b363bbcfbaad08e2f44f378/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/business_control/BUSINESS_PROGRESS.md)；后续主控补记仅同步真实回收/索引/资源状态，不改专业结论。获准分支上的 [业务进展](https://github.com/daowei2026/observe-iterate/blob/feat/statistics-driven-feature-closure-v0.3-20261122/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/business_control/BUSINESS_PROGRESS.md) 和 [恢复进度](https://github.com/daowei2026/observe-iterate/blob/feat/statistics-driven-feature-closure-v0.3-20261122/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/business_control/TASK_PROGRESS.md) 为最新视图。

## 本地材料与运行事实

- 研究根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/`，逐 C 保存详细真实数据派生材料、程序、图与冻结索引；本轮结束不清理这些成果。
- 主控证据根：`/dwdhome/fy/cgpterm/artifacts/eaw-discovery-controller/`，保存准确输入、trusted snapshots、实际发送回执、远端 exact 回读、hash 验证、行动账本和恢复记录。
- E1 最终 77 文件／2,140,343 bytes 已由主控按冻结索引核 hash；Manager 最终 6 份远端原件、23 个来源文件与 13 个支持原件已核，真实最终 turn completed、Sol/max 和 Git 交回已核。
- 原任务/通用 longrun 锁定 observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198；控制 Skill 锁定 cgpterm@da8dabfdaf9a46d563aab261bef77cb5d72d7782。原 Manager/E1 session 历史保留，workers=[]。
- C0019 未实际送达且已合法 SUPERSEDED，C0020 是 D010 首次实际执行；失败及修正原件保留，不重放。
- 主控聊天全文 GitHub 归档状态为 `ARCHIVE_NOT_COMPLETE`：未有已核实独立 observe-iterate Git 工作区。按锁定归档卡保存欠账，不猜路径、新建工作区或新增 Owner 审批；此项与研究结束解耦。准确线程、分支、原因及恢复条件见主控回收记录。

记录时间：2026-11-26T01:56:36.403255+00:00
