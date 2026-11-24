# 给 Codex 主控｜正式启动 EAW P1 AttackSegment 单 Feature 闭环（Owner GO）

本消息是**第二个 EAW P1 Feature 的全新 Run 初始 GO**。第一项 Build 继续按原 Run／工作区独立执行；**这次只新启动 AttackSegment**，不额外启动 Absorb、WALL 合理性或其他 Feature，不迁移旧 F/Q/V 的 Run 身份和成果。启动后由 AI 在本次真实授权内自主闭环，不设置中途 Owner 审批。

## 1. 身份、准确业务来源

```text
run_id: OI-EAW-P1-ATTACK-STAT-20261124-01
work_id: OI-EAW-P1-ATTACK-STAT
business_case_id: EAW-P1-ATTACKSEGMENT
execution_profile: CODEX_NATIVE_DIRECT
post_start_owner_policy: AUTONOMOUS
```

统一专业控制及唯一正式业务输入：

```text
daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da
daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md
```

主控 Skill 采用：

```text
daowei2026/cgpterm@815c505c1cc3d965aaafa831d23c4c88368cb70a:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md
```

所有 controller／本 Run manager／executor 依据同一 `observe-iterate` 精确 commit 的 `control/01_L0_统计驱动的单特征闭环.md`、具名 Skills、实践补充、longrun 合同与专业指南执行；业务输入只用于确定本 Run 目标、正式实例、上游、设计来源和修改边界，不复制 Skill 的专业方法。

## 2. 本次唯一目标及准确正式实例

目标是 EAW P1 的 `mquant.tis.hf.prel0.attack_flow_assembler.AttackFlowAssembler`，不是 Build 或整个 EAW 用例。TIS 从修复后的 Wall 版本开始：

```text
repository: daowei2026/tis
branch_at_start: codex/wall-output-consistency-20261121
commit: 179016111ed0394f92025313e46bd13534932a74
parameter_set_id: attack-default
formal_products: attack_segment, attack_formation_evidence, wall_relation_barrier
```

当前默认实例有 `WallAssembler()`、tactical 和 structural 两组 `DirectedBigDealTick`（F4）。它们是 Attack 的技术上游，不是三个需要再独立闭环的专业任务；必须核实其实际参数和 receipts，不能以代码默认假定实际已成功加载。

正式市场范围：

```text
sof_name = TA_updto20240229_DBA
symbols = rb, m
requested_start_time = 2021-01-01
requested_end_time = 2021-12-31
calendar = night_end_at_2300
Attack parameters = 当前代码正式默认实例
```

X/G 必须依据真实市场数据、当前源码／参数、完整正式结果和准确读回；局部实验标 `DIAGNOSTIC_ONLY`，不能拿人工构造输入或旧 cache 代替。先核已有合格实例／Wall／F4 是否可读取，只有完全同一性通过才允许复用，否则按授权物化本次技术上游和 Attack 正式实例。

## 3. 工作区、线程、Git 分支

Owner 说明**之前使用的 copy 工作区已经释放**。本 Run 只使用：

```text
/dwdhome/fy/BASE_E6_2_copy
```

请在启动前核目录、realpath、真实模块加载、旧 F/Q/V 等 Run 是否仍有在途写者、旧资源绑定能否有据对账，以及共享数据库／缓存写面是否与其它活跃任务冲突。已释放的 Owner 信息是本轮启动依据，但不是现场命令已验证；如旧 Registry 尚有记录，按真实状态对账，不能因旧记录存在就擅判持续占用。不得强停旧线程、覆盖未提交代码或自行换目录。

本 Run 与前一 Build Run（`/dwdhome/fy/BASE_E6_2`）的 manager/executor、真实 cwd、Git checkout、运行状态与专业产物**必须保持独立**，只允许共享经核实可并发读取的上游成果或环境。不要误把 Build 的返回当作 Attack 的前置；Build 未完成不会阻断本 Run。

注册后为本 Run 新建独立 Codex manager 与 executor:E1 线程，`workers=[]`，两者使用 copy 工作区。模型 `gpt-6.1-sol`，effort `max`，以 App Server 实际回读为准，不自动降级。

Git 输出分支（若现场核实尚无同名现役写者，按权限创建）：

```text
TIS: codex/oi-eaw-p1-attack-fix-20261124-01
observe-iterate run records: codex/oi-eaw-p1-attack-stat-20261124-01
```

TIS 修复分支以 `179016111...` 起步；不得修改 Wall 修复原分支、Build 的修复分支或现有运行记录。保留 copy 工作区原有未归属文件，不能以覆盖／清理的方式假装新 Run 已隔离。

## 4. 一次性工程授权与限制

作为 Owner，我一次性授权本 Run 在 copy 工作区读取必要代码、市场数据、exact Wall 和 F4，运行／读回准确上游技术产物和 `AttackFlowAssembler`，进行完整统计、找高置信不合理 finding、诊断、必要实验、回归、正式重跑和结果归档。**仅可正式修改 AttackSegment 自己的** `hf/prel0/attack_flow_assembler.py`、`hf/prel0/attack_flow_assembler_core.py`、对应测试及其专属参数和业务常量。不得改 Wall、`DirectedBigDealTick`／F4、Build、Absorb、上游数据、共享处理器或无关 FRP 代码与业务合同；确属上游问题只记录 `UpstreamFinding`、影响与恢复条件。

只授权向下面具名分支普通 commit/push，不授权 force push、删除生产数据或覆盖别的 Run。为 V2 正式 grant 校验，以下操作与执行场景／允许写面是本次 Owner GO 的原始授权文字（逗号分隔的 allowed_writes 逐项登记）：

```text
operation=eaw-attack-execute-and-profile execution_context=/dwdhome/fy/BASE_E6_2_copy allowed_writes=/dwdhome/fy/BASE_E6_2_copy
operation=eaw-attack-repair-and-publish execution_context=/dwdhome/fy/BASE_E6_2_copy allowed_writes=/dwdhome/fy/BASE_E6_2_copy,daowei2026/tis:codex/oi-eaw-p1-attack-fix-20261124-01,daowei2026/observe-iterate:codex/oi-eaw-p1-attack-stat-20261124-01
operation=eaw-attack-controller-run-records execution_context=github:daowei2026/observe-iterate:codex/oi-eaw-p1-attack-stat-20261124-01 allowed_writes=longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/,longrun/controller/RUN_REGISTRY.json
operation=eaw-attack-controller-chat-archive execution_context=github:daowei2026/observe-iterate:feat/statistics-driven-feature-closure-v0.3-20261122 allowed_writes=longrun/controller/chats/
```

主控须核机械 grants 与真实物理权限、执行线程绑定和审批策略。Owner 的业务授权不等于 Codex App Server 已自动批准外部操作；若发生真实审批／写权限不足，只局部阻断并记录恢复条件，不向 Owner 发起中途审批，不重复发送不明效果的提交动作。归档 controller Chat 只由主控在上述单独授权写面执行，不混入 executor 的 D grant。

## 5. 专业执行、进度和首次回报

按现行 L0 完成首轮 U→X→G；有高置信 finding 进入 D，执行者在本次允许范围内诊断、修正、回归、更新后续轮次，直到形成有据完成状态。finding 判断不是独立 Q 节点，Manager 只协调 Workflow 和真实 Return，不制定专业方法或增加 Owner Gate。

技术前置须包含当前代码下准确的 `wall_lifecycle` receipt／Wall trace，以及所选 F4 tactical、structural 的有效 receipts／范围。旧 WALL 合理性 Run 未完成 Release，这不阻止本次明确授权的技术消费，也不能说 WALL 已全面合理；不把 F4 或 Wall 的技术物化等同于其业务合理性完成。

Manager 在正式回交与结果变更时更新本 Run 的两个文件：

- `business_control/BUSINESS_PROGRESS.md`：已查明的业务进展、finding 处理过程和有效结果链接。
- `business_control/TASK_PROGRESS.md`：真实 Run、C/D/Return、版本、阻断和恢复。

本 Feature 达到当前 ReviewTarget 后形成 `FeatureReleaseGate` 及必要 `UpstreamReleasePackage`。主控只增量归档自身 Chat，不导出 manager/executor Chat。

请**现在启动这个新 Run**，不等待 Build 完成。优先核 copy 工作区释放事实、与 Build 的实际写面是否相冲突、代码和上游产物、真实模型及审批环境；条件满足立即注册／派达，否则准确记录受阻动作，不阻断 Build 已经在做的事情。

首次回报只需：是否真实注册／派达、采用的 commit 和线程／工作区绑定、当前 U/X/G/D 的业务位置、Wall/F4 状态、`BUSINESS_PROGRESS` 链接、阻断与下一合法动作。不能把发布 GO 或读取代码等同于实际 Feature 已运行／完成。