# 给 Codex 主控｜正式启动 EAW P1 Build 单 Feature 闭环（Owner GO）

本消息是**一个新 Run 的初始 Owner GO**：先只运行 Build，不启动 AttackSegment、Absorb、WALL 合理性或其他 Feature Run；不接续旧 Absorb 的 C/D、线程和完成状态。后续不再设置 Owner 业务审批节点，已授权范围内自主闭环。

## 1. 任务身份与精确来源

```text
run_id: OI-EAW-P1-BUILD-STAT-20261124-01
work_id: OI-EAW-P1-BUILD-STAT
business_case_id: EAW-P1-BUILD
execution_profile: CODEX_NATIVE_DIRECT
post_start_owner_policy: AUTONOMOUS
```

三类角色使用同一业务控制 commit：

```text
daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25
```

本次唯一正式业务输入：

```text
daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:task-inputs/eaw-p1-build-stat-20261124/BUILD_RUN_INPUT.md
```

读取该 commit 的 `control/01_L0_统计驱动的单特征闭环.md`、`skills/feature-understanding/`、`skills/reasonableness-analysis/` 及适用补充、`longrun/` 运行协议和 manager/executor 指南；按业务输入的精确引用阅读原需求及代码。主控 Skill：

```text
daowei2026/cgpterm@815c505c1cc3d965aaafa831d23c4c88368cb70a:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md
```

TIS 正式代码起点（包含已修复的 Wall）：

```text
daowei2026/tis@179016111ed0394f92025313e46bd13534932a74
branch: codex/wall-output-consistency-20261121
target: mquant.tis.hf.prel0.build_assembler.BuildAssembler
parameter_set_id: build-default
```

正式实例：`TA_updto20240229_DBA`、`rb/m`、`2021-01-01..2021-12-31`、`night_end_at_2300`，Build 默认参数。核实当前环境加载的真实代码／参数／数据及完整读回，不用人工构造输入替代正式市场实例。

## 2. 工作区与角色

本 Run 唯一指定工作区：

```text
/dwdhome/fy/BASE_E6_2
```

这是以前 EAW Run 用过的工作区，不代表本次已验证空闲。**注册前必须核实**目录、realpath、实际 TIS checkout、未完成写入与旧 Run 资源账本，尤其此前 `OI-ABSORB-STAT-20261123-01` 是否仍占用该目录。旧 Run 若已真实结束，先有据释放其写面占用记录；若仍在执行或状态不明，不覆盖、不强停、不重复创建写者，只报告具体阻断。不要新建或猜测备用工作区。

在可启动后，创建本 Run 全新的、不同的 Codex manager 和 executor:E1 线程，二者均绑定上述唯一工作区；`workers=[]`，不再签 Worker。目标模型 `gpt-6.1-sol`，推理强度 `max`；按当前 App Server 实际回读验证，不自动降级。

Build 相关 Git 写入使用以下具名分支（在确认无旧写者后按授权创建）：

```text
TIS: codex/oi-eaw-p1-build-fix-20261124-01
observe-iterate run records: codex/oi-eaw-p1-build-stat-20261124-01
```

只从上面锁定的 TIS commit 起步，不改原始 Wall 修复分支。不得覆盖历史 Run 的成果、任一其它在途分支或共享写面。

## 3. 本次一次性操作授权

作为 Owner，我授权本 Run 在指定工作区查看真实源码／数据，运行 Build 及准确绑定的 Wall 技术上游、进行全量统计、诊断、高置信 finding 闭环；在有据定位后**只修改 Build 自己的** `build_assembler.py`、`build_assembler_core.py`、其直接测试及本 Feature 的参数／业务常量；完成必要回归、正式重跑和结果读回，并向下列指定 Git 分支普通 commit/push。禁止 force push、破坏性清理、修改市场数据、Wall、F3/F4、Attack、Absorb、共享处理器或无关 FRP 源码／参数。

供 V2 从本次真实 GO 原文提取的具名授权（`allowed_writes` 中逗号分隔为独立写面）：

```text
operation=eaw-build-execute-and-profile execution_context=/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2
operation=eaw-build-repair-and-publish execution_context=/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2,daowei2026/tis:codex/oi-eaw-p1-build-fix-20261124-01,daowei2026/observe-iterate:codex/oi-eaw-p1-build-stat-20261124-01
operation=eaw-build-controller-run-records execution_context=github:daowei2026/observe-iterate:codex/oi-eaw-p1-build-stat-20261124-01 allowed_writes=longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/,longrun/controller/RUN_REGISTRY.json
operation=eaw-build-controller-chat-archive execution_context=github:daowei2026/observe-iterate:feat/statistics-driven-feature-closure-v0.3-20261122 allowed_writes=longrun/controller/chats/
```

主控严格核原文 `authority_quote`、D 委派权限与 Codex 物理操作权限，不能虚构审批已自动通过。若 Git 提交等常规动作被真实 App Server 审批设置阻断，只记准确的技术缺口／恢复条件，不反复触发人工审批或向 Owner 中途问询；其它合法工作继续。

## 4. 业务推进与交付

本 Run 只采用当前 L0 的首轮 U→X→G；有待处理 finding 时按 D Skill 诊断，由 executor 在授权范围内自主修正，必要时进入第二轮及以后。Q 是判断分支，不单独建 Skill。manager 只协调原 Workflow、Return、依赖和状态，不替 Skill 作专业决策，也不增设 Owner 确认节点。

Build 必须消费与当前版本／参数／范围严格一致的 exact Wall artifact 和 receipt。旧 WALL 合理性 Run 未通过 Release；本次明确允许 Wall 作为**技术上游**，不宣称 Wall 已全面合理。若缺该精确 Wall 结果，可在当前单写者工作区按既定代码／参数物化一次，但不能修改 Wall 代码或业务规则。若 D 定位上游缺陷，登记 `UpstreamFinding` 及对 Build 的影响，不越界修复。

当前专业结果按原 Skill 保存；manager 在每次重要回交后分别更新：
- `longrun/runs/<run_id>/business_control/BUSINESS_PROGRESS.md`：业务进展、finding 处理经过、当前有效业务产出与直接链接；
- `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`：实际版本、C/D、真实 Return、恢复状态与下一合法动作。

任务达到初始 ReviewTarget 的真实完成条件后形成 `FeatureReleaseGate` 和必要的 `UpstreamReleasePackage`。主控自己的聊天记录按 cgpterm 自动归档规则增量提交；不导出 manager/executor Chat。

**现在开始**：先核旧 Run 是否占用 `BASE_E6_2`、工作区现役 TIS 版本、Wall 结果与物理授权，再按 V2 注册并实际派达本 Run。第一次回报只需说明是否真正注册／派发、准确记录链接、Build 当前阶段、Wall 前置状态、主要阻断及下一合法动作，不把 GO 发布当成已成功运行。