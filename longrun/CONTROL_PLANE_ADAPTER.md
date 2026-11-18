# 与本分支三层业务控制面的接入合同（候选）

## 1. 不同层的权威边界

本分支根 [README](../README.md)、`control/` 和 `skills/` 规定：

- **L0**：完整业务任务、M↔R、补证回原问题和父任务收束；
- **L1-M**：采用 [control/02](../control/02_L1_观察材料准备流程.md) 的 A～E 外层 Workflow；各阶段专业方法见 [五个阶段 Skill](../skills/observation-material-preparation/SKILL.md)；
- **L1-R**：按合理性分析 Skills 及候选 R0～R5 管理视图组织；
- **L2**：记录 A～E／R 节点的实际 I/O 和消费资格，不按内部步骤机械派工；
- **运行层**：`run_id`、`delegation_id`、`work_order_id`、`call_id` 是通信身份，不替代 `question_id`、阶段实例、预期版本和材料身份。

真实 Owner GO 选择“manager 执行控制面”时，manager 在试运行范围内作业务 Gate、返修、补证、收束和完成全景维护；executor 承担实际专业工作；主控只负责机械身份、发送、回交、核验和保存。该模式不是生产级受保护 Gate 服务。

历史旧“0～7 步”、S0～S5、M05/S2 或 `G-PLAN/G-RUN/G-MATERIAL` 只用于追溯既有 Run，不指挥新工作。

## 2. D/W 可携带但不改写的业务封面

一张专业委派或 Worker 工单可通过 `business_context_ref` 指向业务原件或最小封面：

```yaml
parent_task_id: ...
question_id: ...
material_stage: A | B | C | D | E   # M 任务适用
stage_instance_id: ...
work_item_id: ...
feature_name: ...                    # M 外层输入适用
feature_code_version: ...
feature_instance_ref: ...
input_refs: [...]
input_versions: {code: ..., data: ..., display: ..., definition: ..., expectation: ...}
required_input_scope: ...
expected_outputs: [...]
completion_condition: ...
possible_outcomes: [...]
continuation_target: ...
```

封面不要求每个字段、图层或内部步骤另写一张表。一份 D 可以覆盖具备前置条件的相邻工作；一份 E Worker run 可以产出多个技术文件，但不能替代 executor 的专业核对。

## 3. Gate 与任务回交分开

V2 机械门禁只回答：身份、来源、版本、Owner 授权、回执、动作账本和派发顺序。它不回答：

- A～E 的专业产物是否合格；
- 最终图是否符合 D 定义和 C 预期 HTML；
- 是否已经允许正式取图数据；
- R 的冻结、对照、诊断、标定是否业务上通过；
- `SUPPORTS/COUNTERS/...` 哪种是“好”；
- `PLAN_READY/DATA_READY/PARTIAL_WITH_LIMITS/BLOCKED` 是否满足当前消费者。

这些由 manager／executor 按当前 Control 和 Skill 处理。主控不能自己推断业务结论，也不能把 `UNKNOWN` 当 `PASS`。

## 4. M-A～E 与 Worker 接入

```text
A occurrence 理解
    → B 观察位置
    → C 展示方式
A + B + C
    → D 完整 CAEGraph 定义
D + C + 特征实例
    → E 派 Worker、运行、核图、正式取数和一致性检查
```

- D 不派 Worker；
- E 的 Worker 工单必须引用 D 定义版本、特征实例、品种、时间和修改权限；
- Worker 的结果先回 executor；
- 位置问题返回 B，展示问题返回 C，集成绑定问题返回 D；
- 最终图通过 D/C 核对后，才正式取得 CAEGraph 图数据；
- 脚本、HTML、数据和核对必须绑定同一有效版本／运行。

## 5. 补证、重复比较与任务结束

- `AdditionalEvidenceRequest` 指向原 `question_id`、阶段／工作实例和原分析上下文；结果返回同一消费者。
- 实例复验 `INSTANCE_REVALIDATION` 保留唯一比较工作身份、原始业务窗口、新旧版本与用途，避免 R2/R4 重复发起。
- `PARTIAL / PROVEN_UNAVAILABLE / BLOCKED` 只关闭或限制对应范围；父任务是否可有界结束仍按当前完成合同判断。
- 任一 Worker STOP 不是 E、M 或父任务的 STOP；其他独立合法工作可以继续。

## 6. 专业指南怎样进入具体 D

manager 首轮任务引用同版 [manager 指南](professional/PRO_MANAGER_GUIDE.md)；executor 的 D 引用同版 [executor 指南](professional/PRO_EXECUTOR_GUIDE.md)，并精确引用本次所需 A～E 阶段 Skill 或 R Skill。

`DELEGATION.md` 保存业务语义；`DELEGATION.json` 保持 V2 现有身份和授权字段。不同 D 可以共用一个 executor，但不得把跨 D、跨问题结果混成一次完成。

## 7. 业务决定和完成全景如何回交

```text
executor 专业结果／Worker事实／业务证据
  → manager 作 Gate、返修、补证、后继或收束决定
  → manager 生成 MANAGEMENT_DECISION + TASK_PROGRESS 更新
  → manager 有写入工具则提交，否则主控原样保存
  → 主控回读真实提交与合法后继，再派下一 C/D/W
```

运行期位置：

- `longrun/runs/<run_id>/business_control/decisions/<decision_id>.md`；
- `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`。

全景反映工作实例、M-A～E／R 阶段、两条 Workflow、逐问题状态、父任务完成条件和下一合法动作。不能等最后才汇总，也不能从聊天散文自行生成专业决定。

## 8. 当前验证边界

Owner 可直接安排真实任务，不要求另建专项测试 Run。但首次 manager→executor→worker→executor→manager 中，仍须真实核实物理线程、工具权限、共享写面、身份、阶段产物、Worker 回流和全景保存；跳过专项测试不等于已经联调通过。
