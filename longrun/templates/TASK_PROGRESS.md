# TASK_PROGRESS｜当前业务完成全景（运行期模板；不是实际进度）

> 仅在真实 GO 后，于 `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md` 使用。本模板没有任何已完成事实。五级汇总准则以 [control/06](../../control/06_业务完成全景与更新协议.md) 为准。
> 生成者：管理 Pro 依据原始业务实物和决定生成；若 Pro 无 GitHub 写入能力，由主控按其原文发布。此文件是当前查询视图，不是独立创造完成事实的第二本账。

## A. 身份和当前来源版本

- `run_id`：
- `business_task_id / work_id`：
- `BusinessTaskInput` 的准确引用：
- M 外层输入：`特征名称 / 特征代码版本 / 特征实例`（适用时）：
- `as_of_source_refs`：最近纳入本全景的受控阶段产物、Gate 决定和实际回执的精确 `repo@commit:path`：
- `last_accepted_management_decision_ref`：
- `snapshot_status`：`current / stale / not_yet_verified`：
- 已知新事实但尚未纳入本快照（如有）：

## B. 本轮整体业务任务

| 项目 | 当前有据状态 | 必需来源／后继 |
|---|---|---|
| 任务目标、对象及已明确边界 | 待填 | |
| 必须回答的业务问题 | 待填 | |
| 尚未确定的完成边界 | 待填 | |
| 整体完成状态 | `incomplete / complete / stopped_with_unmet_requirements` | |
| 下一个合法管理／专业工作 | 待填 | |
| 当前重要阻断或待决定事项 | 待填 | |

## C. M/R 两条 Workflow 与阶段实例

| Workflow | `stage (M: A～E) / stage_view (R) / stage_instance_id` | `question_id` / 轮次 / 范围 | 已核实完成及可消费成果 | 尚需完成／在途／受阻及恢复条件 | Gate／证据引用 |
|---|---|---|---|---|---|
| M 材料准备 | 待填 | 待填 | | | |
| R 合理性分析 | 待填 | 待填 | | | |

M 当前阶段为：

```text
A 特征事件级 occurrence 理解
B 观察位置准备
C 展示方式准备
D CAEGraph 定义集成（单一动作，无内部 Workflow）
E CAEGraph 执行／运行（专业 Workflow + W1 + W2）
```

B、C 可在 A 后并行；外层输入+A+B+C 进入 D；D 进入 E。历史旧“0～7 步”或 S/Mxx 只按原事实保留，不用于新 Run 的现行进度。

## D. M-A～E 当前状态

| 阶段 | 输入版本 | 当前状态 | 已接受产物 | 未满足条件／返修目标 | 精确引用 |
|---|---|---|---|---|---|
| A occurrence 理解 | | `NOT_STARTED / IN_PROGRESS / ACCEPTED / PARTIAL / RETURNED / BLOCKED / SUPERSEDED` | | | |
| B 观察位置 | | | | | |
| C 展示方式 | | | | | |
| D 定义集成 | | | | | |
| E 执行／运行 | | | | | |

D 需另外注明：

- 锁定的 CAEGraph／uplot 仓库版本；
- 仓库理解记录是否覆盖本次真实调用链；
- 外层特征实例是否已正式绑定；
- A 字段、B 位置、C 展示代码是否已完成一次性集成；
- C 的预览实例是否已经替换；
- 完整定义和定义级检查是否可供 E 消费。

E 需另外注明：

- 执行与核图基准；
- W1 工单、运行、patch、日志及 E 对回报的专业评价；
- 与 D 完整定义、与 C 展示预期／HTML 的核对结果；
- 最终图是否被接受；
- 正式取数准入是否已形成；
- W2 工单、正式数据包和 manifest；
- 图与数据一致性是否完成；
- 当前为 `PLAN_READY / DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED` 中哪一种。

## E. L2 工作实例及成果

| `work_item_id / node_id` | 当前输入版本及身份 | 结果（已验／待验／部分／返修／不适用／阻断） | 当前能被下游使用的范围 | 未满足条件及后继 | 实物／回执引用 |
|---|---|---|---|---|---|
| 待填 | | | | | |

不要把文件存在、图生成、运输端已发送或 Pro 自述完成误记为已验。尤其：

- C 用真实实例生成预期 HTML，不等于实例已正式绑定；
- D 只有完整脚本，不等于 E 已完成；
- W1 成功和候选 HTML，不等于最终图已接受；
- 最终图接受但尚未签发／完成 W2，不等于 `DATA_READY`；
- W2 文件存在但未完成 E 一致性核对，也不等于 `DATA_READY`。

## F. 逐业务问题的完成情况

| `question_id` | 本轮所要求的回答深度（或待明确） | 当前专业发现及版本 | 已满足的完成条件 | 未满足的必要条件 | 目前是否可结案与依据 |
|---|---|---|---|---|---|
| 待填 | | | | | |

可信的 `COUNTERS`、`PROVEN_NOT_ADJUSTABLE` 不等于工作失败；是否满足本轮交付条件以有据 H3 判断为准。

## G. Gate、补证、恢复与历史有效性

| 对象与身份 | 最近有据决定／回交 | 当前有效范围 | 历史已完成但需要重验的部分 | 尚需动作／退出条件 | 精确引用 |
|---|---|---|---|---|---|
| `Gate / AdditionalEvidenceRequest / stage revision / W1 / W2 / EFFECT_UNKNOWN` | | | | | |

依赖变化按 [control/06](../../control/06_业务完成全景与更新协议.md) 传播：

- A 的事件／字段变化可能影响 B/C/D/E；
- B 位置、C 展示／实例注入变化影响 D/E；
- 外层特征实例或 CAEGraph 仓库版本变化影响 D 和 E；
- D 变化使旧 W1 基准、图接受和 W2 准入失效；
- 最终脚本／HTML／运行变化使旧 W2 准入失效。

旧结果留历史，不无痕覆盖。

## H. 本次更新摘要与可执行后继

- 本次触发更新的新事实和原始证据引用：
- 本次管理 Pro 决定记录引用：
- 本次仅受影响的工作、阶段、Workflow、问题与父任务：
- 需要保留、复用或重验的历史成果：
- 下一具体专业 D／W1／W2／事实核查／等待事件／补证／完成 Gate 的条件：
- 无合法后继时的停止原因与恢复入口：

**发布校验**：主控依据管理 Pro 原文、业务原件和实际回执发布及回读 GitHub commit；只把真实提交登记为已保存。若 `as_of_source_refs` 落后于最新已核实事实，则标记视图陈旧，不按旧视图继续派发。
