# C0003｜D002 回交补正与发布恢复

本次仅补正原 D002 的机器回交并恢复发布。S01＋S02 的专业成果、数据范围和采用版本不变；未重跑研究、未执行 S03、未新建会话或 Worker。

C0002 的零 W 候选 Return 为 REPORTED_COMPLETE，却将父 Run 的 S03～S09 引用写入 remaining_scope_ref。锁定 V2 的 pro_state 要求已完成本 D 时该字段为 null，因此旧候选不能作为合规完成回交。本次由原 E1 在真实 C0003 签认：call_id=C0003、delegation_ref 仍为 D002、return_to 仍为原 Manager、REPORTED_COMPLETE、remaining_scope_ref=null；其余正文保持零 W，result_ref 继续引用已发布的 C0002 专业报告。

C0002 原候选、发布失败及恢复记录保持原样。父 Run 未完成，S03～S09 未执行，正式版本/历史及方向成交的局部限制，继续保留在原报告和 REMAINING_SCOPE.md；清空本 D 的机器字段不清除这些事实。

专业报告：daowei2026/observe-iterate@2919b043df8ac5f2aafeebf425b93a25d118ab53:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/EXECUTOR_REPORT.md

旧候选（保留作历史）：daowei2026/observe-iterate@98a0308d04671a54b7d2e6b4116cf94ff25d037f:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/PRO_RETURN.json

本 C INVOCATION：daowei2026/observe-iterate@29f1e68ee1a2648833047bffae68c3948e327964:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0003/INVOCATION.json

已直接调用锁定 longrun_gate.py 的 validated/pro_state：新 Return 通过，旧 Return 准确复现原错误；并核对本 C token、E1、D002、原 Manager 和零 W。没有构造独立物理 receipt；完整 validate-executor-return 由 controller 回收真实 C0003 后运行。

按本次明确的运输授权，使用同一 Personal 连接 link_6ab37f74c7288191a52eb23d2ca1e2c8，经 Contents API 的路径不存在/已有 blob SHA 条件写入本 Run 指定分支，先核实际 head，未知副作用先对账，随后 exact commit 回读。本次不推广旧候选分支、不覆盖本 INVOCATION 或其他 Run。

完成发布后回原 controller 回收，再由原 Manager 消费 D002 并安排独立 S03；不把本 D 回交或本 turn 结束视为整个 Run 完成。
