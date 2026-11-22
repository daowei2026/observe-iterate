# 版本、正式范围、工作区与授权锁

> 本文件与两个真实 GO 一起使用。Owner 已给出的用例、品种、时间、尺度和工作区已锁定，不再标成 `PENDING_OWNER`。真正尚未提供的版本、参数和授权继续保留待办。

## 1. observe-iterate

```yaml
branch: feat/statistics-driven-feature-closure-v0.3-20261122
adopted_commit: PENDING_FINAL_COMMIT_IN_REAL_GO
control: control-v0.3
execution_profile: CODEX_NATIVE_DIRECT
owner_prompt_ref: task-inputs/wall-f-parallel-closure-20261122/OWNER_PROMPT_EXTRACT.md
```

`adopted_commit` 由真实 GO 锁定当时采用的最终 40 位提交；不要求本准备文件自引用自身提交。

## 2. WALL

```yaml
run_id: ASSIGN_AT_REAL_GO
use_case: EAW P1 integrated / WALL
repository: daowei2026/tis
remote_branch: codex/wall-output-consistency-20261121
full_commit: 6618d4d147d6ebbe634e61facddf2c9a0b996982
commit_url: https://github.com/daowei2026/tis/commit/6618d4d147d6ebbe634e61facddf2c9a0b996982
constructor_or_entry: RESOLVE_FROM_LOCKED_EAW_P1_USE_CASE_AND_CODE_BEFORE_GO
parameter_instance_ref: RESOLVE_EAW_P1_WALL_INSTANCE_BEFORE_GO
symbols: [rb, m]
start_date: 2021-01-01
end_date: 2021-12-31
sides: [bid, ask]
calendar_ref: RESOLVE_FROM_LOCKED_EAW_P1_INSTANCE_BEFORE_GO
linux_workspace: /dwdhome/fy/BASE_E6_2
result_reuse_ref: OWNER_DECISION_OR_NONE
result_sha256: REQUIRED_IF_REUSED
scope_change_policy: OWNER_CONFIRMATION_REQUIRED
external_write_targets: []
```

已核实的修复提交链：

```yaml
D1_output_position_consistency: 19e6b15ee4a5a58c71bf40902bbc6f6657a16ea2
D2_end_precedes_same_tick_dormancy: 4d06ec211d0a20f2ded80417a3334c78cf4b1a0e
D4_effective_support_resets_far_streak: 6618d4d147d6ebbe634e61facddf2c9a0b996982
```

正式 Run 以 `full_commit` 为版本锁；分支名只用于定位。

## 3. F

```yaml
run_id: ASSIGN_AT_REAL_GO
use_case: U2/U3 F-Q-V use case / F only
feature: CommonPriceTurnGroupCandidatesFrp
frp_repository: daowei2026/frp
frp_branch: PENDING_OWNER_NEW_PARAMETER_BRANCH
frp_full_commit: PENDING_OWNER_NEW_PARAMETER_COMMIT
TIS_constructor_ref: PENDING_OWNER_OR_RESOLVE_FROM_LOCKED_NEW_INSTANCE
parameter_instance_ref: PENDING_OWNER_NEW_PARAMETER_INSTANCE
parameter_instance_sha256: PENDING_OWNER
symbols: [rb, hc, i]
sampling: 5m
start_date: 2021-01-01
end_date: 2023-12-31
calendar_ref: USE_LOCKED_U2_U3_INSTANCE_CALENDAR; RECORD_EXACT_REF_BEFORE_GO
linux_workspace: /dwdhome/fy/BASE_E6_2_copy
scope_change_policy: OWNER_CONFIRMATION_REQUIRED
external_write_targets: []
```

## 4. 正式范围与临时诊断

- 上述用例、品种、时间、尺度和工作区不得由 AI 自行调整；
- 正式范围无法运行时，停止相应正式动作，报告阻断和方案，等待 Owner 决定；
- 允许在锁定范围内做临时短窗口／少量位置诊断；
- 临时诊断不改变正式范围，也不替代正式结果。

## 5. 工作区检查

启动前主控核：

- 两个路径存在；
- `realpath` 不相同且不存在父子包含；
- 实际 cwd 和权限；
- 工作区中的代码 checkout 是否能锁到本 Run 精确版本；
- Git 分支、缓存、数据库和输出目录是否仍然共用；
- 共用外部目标是否有单写者。

工作区由 Owner 已指定，不再要求 Owner 另找路径；若现场不满足条件，只报告实际问题，不自行换目录。

## 6. 修改确认与授权

每个 Run 的 GO 分别登记需要的：

```text
operation
execution_context
allowed_writes
authority_quote
```

分析、统计、报告和不采用的隔离诊断不等于正式修改授权。任何新的正式代码、参数、配置、业务规则、数据处理或范围改变，还必须有 Owner 对相应 `ModificationProposal` 的确认。WALL 和 F 不互相继承授权。

## 7. 尚待补齐

WALL：

- 从锁定 EAW P1 用例和当前代码解析并记录精确构造／执行入口、参数实例和日历引用；
- Owner 决定是否复用最终结果包；复用则登记 SHA；
- 真实 GO 与 grants。

F：

- Owner 提供的新参数代码版本、参数实例路径、字段和值及 SHA；
- 新实例所使用的精确构造入口和日历引用；
- 真实 GO 与 grants。

Campaign：

- WALL 下游 Feature 的精确依赖图。
