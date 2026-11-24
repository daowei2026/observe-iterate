# C0002｜D001 首轮 U 执行回交

原生 `FeatureUnderstandingPackage.completion_status=PARTIAL`。当前实现的核心对象、身份、状态、occurrence、处理关系、参数及公开结果布局已还原；当前版本正式 receipts／完整结果未确认，字段实际可读性有具名缺口。X 可以据此继续，G 尚无有效正式运行绑定。本次回交不代表父 Run 或 Feature 已完成。

- run_id：`OI-EAW-P1-ATTACK-STAT-20261124-01`；call_id：`C0002`；delegation_id：`D001`。
- sender：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:executor:E1`；return_to：原 manager；`workers=[]`。
- Invocation：`daowei2026/observe-iterate@496166abf737b6b7bb58c04c08fc421d8ca7b723:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0002/INVOCATION.json`。
- D：`daowei2026/observe-iterate@e20128bff682c58bc2a66a6c5ed176f78634c476:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D001/DELEGATION.json`。
- 采用专业控制：`9877826236e0995e7255e6cbfedc2d1b89dea6da`；亲读原 Skill、业务对象判别补充、WORKFLOW、IO、L0、executor 指南、V2/Profile、唯一正式业务输入、Owner/Binding 和四份业务来源。快照九项 blob 均与精确远端一致。
- 实际 cwd：`/dwdhome/fy/BASE_E6_2_copy`；TIS 根为 `mquant/tis`；HEAD `179016111ed0394f92025313e46bd13534932a74`；本 Run 修复分支 `codex/oi-eaw-p1-attack-fix-20261124-01`。核对的九个 TIS 源文件与锁定 commit 一致，tracked 工作树没有修改。

原生产物：

- [FeatureUnderstandingPackage.json](../../professional_results/D001/FeatureUnderstandingPackage.json)：原生完整记录。
- [中文阅读版](../../professional_results/D001/FeatureUnderstandingPackage.md)：产品、身份和时间语义。
- [仍未确认范围](../../professional_results/D001/REMAINING_SCOPE.md)：本 D 的缺口及后续使用资格。
- [来源核验](../../professional_results/D001/evidence/source_read_manifest.json)、[工作区源码核验](../../professional_results/D001/evidence/workspace_source_verification.json)、[构造实例证据](../../professional_results/D001/evidence/instance_introspection.json)、[候选 receipt 拒用核验](../../professional_results/D001/evidence/candidate_receipt_check_summary.json)、[产物自检](../../professional_results/D001/evidence/package_self_check.json)。

已确认的关键事实：完整 AttackSegment 在真实闭段时发布，business_end 保留末材料位置，closed_at 保留关闭触发位置；FormationEvidence 是形成材料／区间，正式 Barrier 当前只复制 exact Wall.End。半秒材料、F4资格行、段、Formation 和 Barrier 不能混计。双lane共享材料只累计一次段总量，overlap view可重叠。段及资格信息跨物理chunk carry，技术边界不无条件关闭段；内部 atom/carry/checkpoint/summary 没有进入当前正式 `.F`。

真实操作只包括读取、源码/字段交叉核对、构造参数探针及准确路径的已有 receipt 查询。两个探针均禁止 Feature 运行入口；实际加载模块全部位于 copy 工作区，完整 P/ppdict/ppid 已保存。没有执行 Feature，没有全量行为统计、诊断、参数调整、实验、回归或产品代码修改，没有消费 Build 结果。

已有 receipt 的有界查询结果：rb 三 Attack 产品、Wall、tactical/structural F4均为其它代码版本；m 的 Wall 也为其它代码版本，m 的三 Attack 与两组 F4 在本次实例解析目录下没有 receipt。所有候选均未接纳，没有读取或统计其市场结果。此查询未遍历共享缓存，不能声称其它位置绝无结果。准确 Wall/F4 receipts 和当前正式完整结果仍需在 X 核定或按已有授权物化。

原文／合同与实现的差异已并列记录：原始 A3 的 FRP 组段及 chunk 内建议与当前 producer/carry 不同；指定 FRP 参考要求 Attack v1.6.2、attempt/available_at 字段，而当前 TIS 声明 v1.6.1 且无这些字段；该 FRP 段簿 current view 实现按本次 firing 重建。它们属于 U 的来源事实，未升级成 finding 或 Diagnosis，也未替 manager 签发后继。

机械 Return 使用 `REPORTED_COMPLETE` 表示本次专业报告已提交；原生包状态保持 `PARTIAL`，未将其改写成 COMPLETE。原 manager 仍须真实消费本 Return，沿既定 L0 安排后继。没有 Owner 请求。发布前一次带编码斜杠的 branch URL 查询被工具以 INVALID_ARGUMENT 拒绝；已改用准确 Git ref 只读端点成功回读，没有发生变更，也无持续审批或权限阻断。既有运行证据缺口如实保留。跨 Chat 运输由 controller 承担，本 executor 未向其他 Chat 发送消息。

