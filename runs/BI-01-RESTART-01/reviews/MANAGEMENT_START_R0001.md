# BI-01-RESTART-01 R0001 M-START 管理决定

## 1. 决定摘要

1. 采用 Q-01：共同转折后的成员 Movement 分化及 U2/U3 业务增量。
2. G1 Pass。
3. G2 Pass，但限定 Reference/Shadow 路径。
4. G3 分区接收：下游导出/状态边界可消费；当前上游承重路径需定向核查。
5. 当前直接进入 I4，不因历史包 hash、完整 Runner 或正式 H1 全线等待。
6. 签发执行 Pro 的 I4 完整任务，包含定向 I3。
7. 不需要 Owner 当前决定；G4 尚未接收。
8. 没有独立审查方法，不宣称独立 PASS。

## 2. 管理亲自核实的承重事实

- 下游 ZIP：SHA-256 `7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`；23 CSV 可读。
- 上游 ZIP：实际 SHA-256 `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`，不同于历史记录 `ff3215...`；manifest 自洽。
- C2 未正式 commit，H1 未发，R03 Quality/Capital Use 均 Withheld。
- S 的 Universe 仅 `hc|i|rb`，outside_count=0。
- 2021-05-11 10:00 存在 38-bar Working 与 33/1-bar Completed 的成熟度差异，以及晚确认回定实际结束问题。
- 两包都没有完整独立 Runner/Trace；本轮决定不把恢复它们设为全线前置。

## 3. 管理已作的取舍

- 采用当前上游实际 hash 作为本次新的候选 DataBinding，不追认它是旧原件。
- 只要求 Case-01 的承重行和路径复算，不做全量审计。
- 不允许把参考/Shadow 输出升为正式 OpportunityCluster/H1/Quality。
- 不把 A/B/C 当配额；不把图/文件/代码长度当业务价值。
- 执行 Pro须连续推进 I4；局部修通后继续已明确后继。
- 管理在 G4 候选、承重资格冲突、Owner/方法变化或两次有效调用无业务推进时复看。

## 4. 当前交付

- `00_长程推进地图.md`
- `01_当前任务.md`
- `QUESTION_WORK_BINDING.json`
- `WORKMAP_BINDING_CANDIDATE.json`
- 本管理决定
- R0001 的 ROLE_RETURN / QUESTION_WORK_RETURN

## 5. 远端状态边界

本次回答环境没有 GitHub 写入动作。上述实物已形成，但尚未写入远端分支、remote readback 或完成 workmap intake。操作端应原样落盘并普通快进提交；在真实 commit 和 intake 之前，不得把 `WORKMAP_BINDING` 标为 ADOPTED，也不得发送执行 Pro 任务。
