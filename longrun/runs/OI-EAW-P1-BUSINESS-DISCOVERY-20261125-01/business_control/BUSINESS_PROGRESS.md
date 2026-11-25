# BUSINESS_PROGRESS｜EAW P1 挂单—成交演化的业务迭代点发现

## 一、当前任务与整体情况

研究目标不变：在 Owner 指定同批真实 Tick 窗口内，找出有实际证据、可指向具体业务设计的 EAW P1 迭代点。

业务/特征理解及数据接入核查（S01＋S02）已经实际完成，本次 manager 已消费原 E1 报告及有效回交。下一项为独立 S03 全范围候选检索，已签发 D003，待 controller 派达同一 E1。目前没有候选迭代点、市场差异或已确认正式设计缺陷；整体研究尚未完成。

## 二、实际工作与结果

| 工作 | 已取得的真实结果 | 当前状态与入口 |
| --- | --- | --- |
| S01 业务及特征理解 | 理清 Wall 与 Build/AttackSegment/Absorb 的共同 exact Wall 依赖、互不消费关系、业务语义、入口/稀疏化取舍与可观测边界；历史建议和参考代码不作为本批市场结论 | 已完成并消费；[理解记录](https://github.com/daowei2026/observe-iterate/blob/2919b043df8ac5f2aafeebf425b93a25d118ab53/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/S01_UNDERSTANDING.md) |
| S02 数据及版本核查 | 148 窗口、rb/hc/i、444 窗口×品种单元；全部 2,924 文件的 manifest/字段/行数核对；报价去重 328,920 行、重复 17,844、0 重叠冲突；有效范围、断点、版本证据和独立性索引已保存 | 本步已完成，局部证据限制保留；[数据核查](https://github.com/daowei2026/observe-iterate/blob/2919b043df8ac5f2aafeebf425b93a25d118ab53/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/S02_DATA_AUDIT.md) |
| S03 全范围候选检索 | 以已核有效范围尝试三入口，形成统一候选研究表及可重放扫描材料 | 已独立委派，尚未确认开始；[D003](../delegations/D003/DELEGATION.md) |
| S04/S05/S06 第一轮 B1/B2/B3 | 待候选表形成后，在各实际业务节点分别消费和安排 | 尚未委派/执行 |
| 每条候选 S07＋S08 | 待实际候选形成，逐条开展第二轮取证与设计定位 | 尚未委派/执行 |
| S09 总体归并 | 待真实成果及原任务结束依据 | 尚未委派/执行 |

本次消费使用补正后有效 Return；补正仅涉及机器回交和发布，S01/S02 原报告、数据及研究成果没有重跑。业务成果形成于原执行，不重复计为新研究。

## 三、已经明确的材料限制及业务影响

| 已核事实（来源为 E1 原报告） | 对后继结论的实际影响 |
| --- | --- |
| 同价配对的主买/主卖代理逐项等于相应盘口可见减少量，且有总成交为零而代理为正的记录 | 不能把代理当成独立方向成交真值，也不能用同源的净新增计算独立证明补单；可执行检索继续，依赖此独立性的判断保留限制 |
| 已读到 Wall/F4/Build/Attack/Absorb 展示材料，但 producer commit、参数 receipt、exact upstream 与完整正式历史/发布未证实 | 缺展示不表示无墙或正式产品缺信息；参考代码不等于本批版本，确认正式表达缺口仍待相容证据 |
| 有局部买侧无效、自然时间/休市断点、窗口重叠与截断 | 复用已保存有效范围和连续性索引，不跨断点配平；不把缺后续数据当作无事件 |
| 已冻结 95 个发现窗口与 53 个预留窗口，并保存保守过程组及日期关联块 | 保留同批复现机会与实际使用追溯；这些是保守关联索引，不是已证实独立攻防样本数 |

这些属于输入证据与解释边界，目前没有据此确认 P1 设计缺陷，也没有发现数量或市场频率结论。三入口及 B1/B2/B3 的实际检索、对照仍待开展。

## 四、可直接查看的当前成果

| 产出 | 用途 | 原件入口 |
| --- | --- | --- |
| E1 原专业报告 | S01/S02 完成事实、限制与后继可行性 | [EXECUTOR_REPORT](https://github.com/daowei2026/observe-iterate/blob/2919b043df8ac5f2aafeebf425b93a25d118ab53/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/EXECUTOR_REPORT.md) |
| 冻结产物索引 | 本地 24 项详细报告、清单、索引和脚本的准确路径/大小/哈希 | [ARTIFACT_INDEX](https://github.com/daowei2026/observe-iterate/blob/2919b043df8ac5f2aafeebf425b93a25d118ab53/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/ARTIFACT_INDEX.json) |
| 来源索引 | 原始讨论、合同、参考代码及实际版本未知项 | [SOURCE_INDEX](https://github.com/daowei2026/observe-iterate/blob/2919b043df8ac5f2aafeebf425b93a25d118ab53/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/SOURCE_INDEX.json) |
| 独立 S03 委派 | 承接 S02 有效范围及限制，直接按原任务开展候选检索 | [D003](../delegations/D003/DELEGATION.md) |

详细成果保存在 `/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0002/`，由上述冻结索引核查；无需重复远端发布全部大表。

## 五、下一步

由 controller 派达 D003 至当前已实际执行的同一 E1，完成独立 S03 后交 manager 消费，再分别安排 S04/S05/S06；第二轮按每条候选合并 S07＋S08，最后独立 S09。保留 Owner 最新粒度，不新增专业复审或审批，也不因局部证据不足暂停可继续工作。

技术恢复见 [TASK_PROGRESS.md](TASK_PROGRESS.md)，本次消费及后继事实见 [C0004 报告](../calls/C0004/MANAGER_REPORT.md)。旧整体委派 D001 保留被替代历史；已消费 D002 的有效成果继续复用。

更新时间：2026-11-25T16:34:32.038Z
