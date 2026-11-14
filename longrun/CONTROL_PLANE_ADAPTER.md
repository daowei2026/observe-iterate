# 与本分支三层业务控制面的接入合同（候选）

## 1. 不同层的权威边界

本分支根 [README](../README.md) 与 `control/`、`review/` 明确：L0/L1/L2 仍为候选控制设计，专业 Skill 的方法不在控制面重写。**当真实 Owner GO 选用本轮“管理 Pro 执行控制面”模式时**，由 manager 在试运行范围内亲自完成所有业务管理判断、Gate、定向返修、补证、收束和业务完成全景维护；executor 继续承担实际专业工作，主控继续只负责机械身份/发送/回交/核验及保存。试运行的管理决定不是已有生产级受保护 Gate/权限服务。

- L0：单份 `BusinessTaskInput`（业务目的、对象、已知约束和未定边界）/ `ParentTaskOutcome`，M ↔ R 与 AdditionalEvidenceRequest 的原点恢复；完成深度及允许未决可随任务合法查明，不强制起步另填第二份 `TaskBoundary`。
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
- M 交接的 `PLAN_READY/DATA_READY/PARTIAL_WITH_LIMITS/BLOCKED` 和真实限制，不自动证明 R 当前消费者所需输入已满足；R03/R05 依实际工作分别检查探索样本或正式对照的输入。**H1 不再分成材料准备的两条正式出口。**

试运行期间，对尚未程序化或尚需专业判断的控制点，**交 manager 按真实证据作出具名业务决定**，包含通过/返修/限域/补证/等待/收束及合理后继；主控不能自己推断业务结论，也不能把 `UNKNOWN` 当 `PASS`。D01、D04/D05、D10、D12、D13/D15 等在试运行中由 manager 逐案处理并记录哪些判据仍待迭代，而不是要求 Owner 每次补批。

## 4. 补证、重复比较与任务结束

- `AdditionalEvidenceRequest` 须指向原 `question_id`、`work_item_id`、原分析上下文/预期版本；冻结前允许记录 `not_frozen`；结果返回**同一原始消费者**，不可自动用在新预期版本。
- 实例复验 `INSTANCE_REVALIDATION` 要有唯一 `comparison_work_item_id`、原始业务窗口、新旧版本与用途，以避免 R2/R4 重复发起。
- `PARTIAL / PROVEN_UNAVAILABLE / BLOCKED` 只关闭/限制对应工作；是否允许有界未决，须符合本轮**已经合法明确的完成范围**，不能因执行层完成就宣布 `ParentTaskOutcome` 合格。
- 任一子工单 STOP 不是父专业任务的 STOP；某局部无后继也不代表其他独立问题不能继续。

## 5. 专业指南怎样进入具体 D（不新增 Schema）

manager 首轮实际完整任务应包含已锁定 [manager 指南](professional/PRO_MANAGER_GUIDE.md) 和业务问题/控制来源；executor 的 D 应引用同版 [executor 指南](professional/PRO_EXECUTOR_GUIDE.md)，并按本次 D 明确引用 [材料准备 Skill](../skills/observation-material-preparation/SKILL.md) 或 [合理性分析 Skills](../skills/reasonableness-analysis/README.md) 的真正适用部分。

D 的 `DELEGATION.md` 使用 `question_id`、节点范围、输入版本/材料与结果消费者定义**业务工作**；`DELEGATION.json` 仍遵从已有 V2 的 D 身份与授权字段，专业指南不能给机读 Schema 增加私有必填项。不同 D 可以共用一个专业执行人，但不得把跨 D、跨问题的结果混为一次完成。

## 6. 接入后续实现的条件

只有在业务控制面确定实际 Gate 规则后，才能将其转成受版本管理的具体规则/程序或专门专业判断任务。调用确定性程序的**选择依据**须来自明确路由规则/已接受的专业决定，不能让主控依据工具名称自行判断。程序结果须有 action_id、真实输出引用、版本、失败/未知状态；主控维护可信执行账本。专业执行人的方法可单独在 Skill 中定义，不进入本文件。

## 7. 本次试运行的业务决定和完成全景如何回交

**正式启动时采用本协议，仍须有真实 Owner GO 和准确 GitHub 写入位置**。没有业务控制程序也能运行：manager 负责业务决定，主控负责把决定及引用的原始证据作为可查实物保存并据此组织下一次派发。

```text
专业执行结果、Worker事实、原业务证据
  → executor 依 D 回 manager
  → manager 执行本次业务 Gate、选择准确的下一节点/补证/返修/结束
  → manager 同轮生成 MANAGEMENT_DECISION + 受影响的 TASK_PROGRESS 更新
  → 若 manager 有真实 GitHub 写入工具：自行提交并报精确 SHA/path
    否则主控将 manager 完整原文逐字保存，不增加专业判断
  → 主控回读已发布原件、真实回执和合法后继，再派发下一 C/D/W
```

实际运行中采用的相对路径（最终 Run 的 repository/branch 以 GO 为准）：

- `longrun/runs/<run_id>/business_control/decisions/<decision_id>.md`：管理 Pro Gate、范围及后继的不可无痕改写记录；模板 [MANAGEMENT_DECISION](templates/MANAGEMENT_DECISION.md)。
- `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`：当前五级业务完成全景的查询视图；模板 [TASK_PROGRESS](templates/TASK_PROGRESS.md)；历史快照由 Git 历史保留。

全景至少反映工作实例、S/R 阶段实例、M/R 两条线、逐问题状态、父任务完成条件及下一合法动作；**首次 GO 后就建立真实的初始化全景**，并在合法新事实、Gate、交接、补证、版本失效、恢复时更新受影响部分。不能等最后才汇总，也不为每条普通聊天另设一次 Pro 轮次。

`PRO_RETURN.json` 与 D/W 继续使用 V2 原 Schema，不在机器 Return 中塞未经批准的新必需字段。可由现有 `result_ref`、`continuation_ref` 和已发布的报告/决定/全景来源记录业务信息；遵守“先发布被引用原件、再发布引用它的 Return”的 Git 版本顺序，不能自我引用尚不存在的 commit。

真实操作许可区别于业务管理委托：**业务 Gate、补证、正常返修不再向 Owner 逐项申请**；仅当实际工具的环境/写入权限不支持、与 Owner 已明确禁令冲突或确需改变已确认目的时，形成具体阻断与选择。V2 `grants` 仍按 GO 原文和实际执行权限做机械核验；不得伪造 Owner 的 `authority_quote`，不改动全局手机与 Worker 传输 Skill。

## 8. 无专门测试 Run 时的真实业务验证边界

Owner 将直接安排一项真实任务启动。主控在该任务实际发生的首次 manager→executor→manager（以及首次真实 Worker W）中自然核验 C/D/W、回执、全景保存和恢复；**不再把另开一个测试 Run 设为前置要求**。实际物理线程、共享写面和身份校验仍须在首次使用时真实核实，不能因跳过专门测试就虚称已经联调通过。
