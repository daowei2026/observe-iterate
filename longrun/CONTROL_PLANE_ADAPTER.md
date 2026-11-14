# 与本分支三层业务控制面的接入合同（候选）

## 1. 不同层的权威边界

本分支 `00_README_范围来源与阅读顺序.md` 明确：L0/ L1/ L2 控制逻辑为候选、专业 Skill 方法不在控制面重写、管理 Pro／程序／专业角色的具体分工还未确定。本文件只定义**可以跨角色安全传输的上下文形状**，不制定业务 Gate 的专业充分性政策。

- L0：`TaskBrief` / `TaskBoundary` / `ParentTaskOutcome`，M ↔ R 与 AdditionalEvidenceRequest 的原点恢复。
- L1：材料准备 `S0～S5`；合理性分析 `R0～R5`，仅管理视图，不是固定调用次数。
- L2：`M01…`/`R01…` 的 I/O；`MaterialRequirement`、`WorkItem`、`ExecutionAction` 三种实体不应混同。
- 运行层：`run_id`、`delegation_id`、`work_order_id`、`call_id` 是通信/任务执行身份，不替代 `question_id`、`analysis_round_id`、`expectation_version`、`material_id`。

## 2. D/W 可携带但不改写的业务封面

一张专业委派或 Worker 工单在实际使用时，可通过 `business_context_ref` 指向业务原生材料或最小封面（精确提交引用），建议封面保存：

```yaml
parent_task_id: ...
question_id: ...
stage_view: S3                 # 管理视图
control_nodes: [M06, M07]     # 可多节点，非固定一一派单
work_item_id: ...
input_refs: [...]
input_versions: {code: ..., data: ..., parameter: ..., expectation: ...}
required_input_scope: ...     # 对象、时间、用途、就绪等级
expected_outputs: [...]
completion_condition: ...
possible_outcomes: [...]
continuation_target: ...
```

这个封面不要求每份材料再写一张表。单一真实数据加工可以满足多项 `MaterialRequirement`；复验必须保留被消费的对应身份和资格。

## 3. Gate 与任务回交分开

V2 机械门禁只回答：谁派给谁、来源是否已存在、精确版本是否一致、Owner 操作授权是否覆盖、回执与动作账本是否相符、是否已经派发或正在等待。不回答：

- `H0/H1/H2/H3` 是否业务上通过；
- `G-PLAN / G-RUN / G-MATERIAL` 和 `G-EXPECTATION-FREEZE / G-COMPARISON / G-DIAGNOSIS / G-CALIBRATION` 的专业充分性；
- `SUPPORTS/COUNTERS/MISSING/AMBIGUOUS/NOT_APPLICABLE/PENDING` 哪种是专业好坏；
- `PLAN_READY/DATA_READY/PARTIAL_WITH_LIMITS/BLOCKED` 是否符合特定下游 `use_kind`。

有规则且输入充分的机械判断，可由有权限的确定性程序执行；缺未确认业务政策时产出**具名待判断问题**，不由主控自行猜选项或把 `UNKNOWN` 当 `PASS`。控制面候选设计中的 D01、D04/D05、D10、D12、D13/D15 等保持待确认。

## 4. 补证、重复比较与任务结束

- `AdditionalEvidenceRequest` 须指向原 `question_id`、`work_item_id`、原分析上下文/预期版本；冻结前允许记录 `not_frozen`；结果返回**同一原始消费者**，不可自动用在新预期版本。
- 实例复验 `INSTANCE_REVALIDATION` 要有唯一 `comparison_work_item_id`、原始业务窗口、新旧版本与用途，以避免 R2/R4 重复发起。
- `PARTIAL / PROVEN_UNAVAILABLE / BLOCKED` 只关闭/限制对应工作；是否可交付有界未决必须符合原 `TaskBoundary`，不能因执行层完成就宣布 `ParentTaskOutcome` 合格。
- 任一子工单 STOP 不是父专业任务的 STOP；某局部无后继也不代表其他独立问题不能继续。

## 5. 接入后续实现的条件

只有在业务控制面确定实际 Gate 规则后，才能将其转成受版本管理的具体规则/程序或专门专业判断任务。调用确定性程序的**选择依据**须来自明确路由规则/已接受的专业决定，不能让主控依据工具名称自行判断。程序结果须有 action_id、真实输出引用、版本、失败/未知状态；主控维护可信执行账本。专业执行人的方法可单独在 Skill 中定义，不进入本文件。
