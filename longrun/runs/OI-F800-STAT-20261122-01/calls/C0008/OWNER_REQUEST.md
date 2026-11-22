# Owner 修改确认项｜F800-MP-001（待确认）

## 请确认的具体事项

请确认是否批准原提案 `daowei2026/observe-iterate@a99ab37cdcf43759b7f203a1233fe69a7fa733db:longrun/runs/OI-F800-STAT-20261122-01/professional/D003/ModificationProposal.json`（proposal_id=`F800-MP-001`），对已确认的 `F800-GF-001` 正式实施修复、回归、提交/推送并采用新的准确 FRP 版本，再按原 Workflow 进行完整正式 X 与 G 复验。当前没有批准回执，本包不是修改授权；本 C 未签发正式实施委派。

本确认项直接整理原 executor 提案，不改写提案、不补作诊断或自行选定另一修法。Owner 可批准、提出具体范围调整、明确暂缓或拒绝；所需确认仅针对本次新正式行为改变，原800实例和生产范围无需重新请示。

## 已确认问题及现状

原生诊断：`daowei2026/observe-iterate@a99ab37cdcf43759b7f203a1233fe69a7fa733db:longrun/runs/OI-F800-STAT-20261122-01/professional/D003/DiagnosisReport.json`；问题：`daowei2026/observe-iterate@a99ab37cdcf43759b7f203a1233fe69a7fa733db:longrun/runs/OI-F800-STAT-20261122-01/professional/D003/RequirementOrImplementationIssue.json`；最新回交：`daowei2026/observe-iterate@9e014214d9c62b6e69a0610068c49187497cb903:longrun/runs/OI-F800-STAT-20261122-01/calls/C0007/PRO_RETURN.json`。

原 executor 已确认 ImplementationMismatch：正常 KLine 适配器对两个归一化 Double 商作严格差值相等，真实600UTI连续边在数值边界被误判为断点，随后重启覆盖累计。已定位 `GroupCandidateKLineInput.hs:109—112`。影响为22/1546观点（1.423%）、12/480 Life（2.5%）、18个发行时刻。原生判断为MEDIUM、未修复；不是当前数据缺口、冷启动、错绑或reader反读。

D003诊断职责已完成，正式Feature、参数及输入处理未修改。原D002完整X/G和31表独立读回保持当前ac版本的有效未修复结果；GlobalProfileGate仍为DIAGNOSIS_REQUIRED，尚无UpstreamReleasePackage。当前不存在新的正式修复产物或已验证修后版本。

## 原提案范围

当前正式基线为 `daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574` 与 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`；变更仓库/责任文件沿原提案FRP范围，后续实施回交再绑定真实新commit。

- 责任点：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs` 正常KLine覆盖相邻边判定及必要局部状态载荷，配套适用现有FRP测试入口由后续实施工作确定。
- 具体改法：以源UTI及该频率/Calendar的准确预期步长表达相邻，避免两个已除法归一化Double位置的严格差值比较；保留真实缺口、失知/失败与冷启动边界。对支持频率/单位和非整数步长先明确合同，不能盲目round。
- 保持原批准实例：observation_multiple=800、delta=600、CalendarUTITick、2Δ贴近条件、method.revision=1；rb/hc/i、5m、2021—2023、night_end_at_2300、TA_updto20240229_DBA、steel。本确认项不扩为Q/V正式运行或更换用例/范围。

## 影响与尚不能承诺的事项

原提案的隔离诊断方程使22个错误flag转为完整，8个冷启动flag保留。这是DIAGNOSTIC_ONLY证据，不代表已经完成正式修复或全候选演化。

覆盖值和变化时刻会影响candidate affected/body比较、稀疏Revision发行及组间exact引用；新生产的组数、观点数、UUID链和下游效应须实测，不能承诺只减少22个观点或保持原ID。正常F/Q共享适配器的下游影响按原提案由实施/释放角色评估，本Run当前仍只运行F。

替代方案按原提案保留：保持现状并由Owner明确暂缓；缩短K/改delta不能修复责任点且会改变业务范围；浮点容差会新增边界，原提案未作为推荐。manager不替Owner接受缺陷或改变正式参数。

## 原验证计划与批准后的既定回交

按原提案 validation_plan：先确认准确离散步长合同，保留数值边界前/中/后及真实1200UTI缺口对照；正式实施后完成数值边界、真实缺口、冷启动、未知Clock及观察窗/2Δ等原合同回归。结构合同变化时只更新受影响U，否则锁新准确版本进入完整X、31表独立读回和G。

以原22个位置和全三年覆盖状态复验，并检查状态、引用、密度和原4项场景问题的影响。正式输出及UUID沿革需按新结果绑定；局部算术或测试成功不等于Feature释放。后续实际commit、改动文件、测试、行为变化和新版本应按既有ImplementationFixReturn/原生报告回交，由manager再沿既定Workflow消费。

## 确认依据与当前状态

真实 Owner GO：`daowei2026/observe-iterate@43a13e14129984d6f3a142c6eb64397a43c3ca79:longrun/runs/OI-F800-STAT-20261122-01/OWNER_START.md`，原文为“确认后才实施、提交和采用”。本 C 派工：`daowei2026/observe-iterate@213c5d6e33b3c1651ebcf347f407d32094a282c6:longrun/runs/OI-F800-STAT-20261122-01/calls/C0008/FULL_ASSIGNMENT.md` 明确要求Owner未批准前，不得将候选改法作为已批准的正式修改/提交/推送/采用。原 L0 §7.2：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md`。

`OWNER_DECISION_APPLICABILITY.json` 指明无需业务价值取舍型OwnerDecisionPacket，但正式修改确认仍必需；两者不混用。原ModificationProposal的executor历史approval_status保持原文，本包为manager整理并发布的具体确认项。等待实际Owner答复，不把发布、模型措辞或controller回收视为批准。
