# 观察—迭代长程运行协作层 · V2

> 本目录负责跨 Chat／Worker 的身份、真实通信、回交、状态与恢复；不替代任何专业 Workflow、Skill 或其完成条件。源码和配置存在，不代表真实聊天/Worker 已联调成功。

## 1. 当前职责与调用结构

| 角色 | 作用 |
|---|---|
| Owner | 提供业务任务、已确定的外层输入和真实运行授权；未定义的业务取舍需明确决定 |
| 主控 Codex | Run 与物理聊天绑定、C/D/W 发送和回执、权限/工作区校验、去重与恢复 |
| **多层 Workflow 运行协调 Chat**（V2 `manager`） | 维护统一任务状态和版本依赖；依已定义 Workflow 调用、等待、接续和回流 Skill；按需增设执行 Chat |
| **Skill executor**（V2 `executor`） | 依 D 指定 Skill 执行、自检及回交；A～D 默认 ChatGPT、E 默认独立 Codex 线程 |
| Worker Codex | 在已授权 W 范围内执行实际操作，按 V2 回原签发 executor；专业后续依对应 Skill |

V2 仍使用 `manager/executor/worker` 机读身份；`D→Codex executor C→PRO_RETURN→manager` 是 E 的零 W 路径；历史 `D→ChatGPT executor→W` 路径仍兼容。它们均不是专业 Workflow 的阶段。

```text
Owner GO → 主控（真实发送和账本）
               → 多层 Workflow 运行协调 Chat（状态与既定流程）
                     → D：指定一项 Skill 工作
                           → Skill 执行 Chat（按 Skill 实施）
                                ↔ Worker（仅在该 Skill 需要且获准时）
                     ← Skill 原生结果与准确引用
               → 既定后继 / 同一 Skill 续作 / 返回 / 等待
```

**委派不再是重新写一份专业任务方法**：协调 Chat只传任务身份、准确 Skill 与上游输入产物引用、结果回交对象；不自拟“执行约束”、Worker 处理步骤、业务预期或额外专业验收。真正的 Owner 授权由主控按 V2 机械校验，不能省略。

## 2. 当前观察材料准备 Workflow

依据 [control/02](../control/02_L1_观察材料准备流程.md) 的 A～E 和 [五个 Skill](../skills/observation-material-preparation/SKILL.md)：

```text
A occurrence 理解
  ├→ B 观察位置 ─┐
  └→ C 展示准备 ─┼→ D 完整 CAEGraph 定义 → E 真实运行/核图/取数
                 ┘
```

A 先行，B/C 在有效输入下可按需并行，D 汇合，E 按 Skill 在独立 Codex executor 中连续执行，不强制 W1/W2。一个 Skill 允许多次 C 继续同一 D；可由一个执行 Chat 顺序工作，或按真实需要增加执行 Chat。Skill 内步骤默认不另立专业 D。

合理性分析具体 Workflow 仍在迭代，只按实际 Run 固定采用的专业来源执行，不在长程运行层硬编码 R0～R5。

## 3. 必要文件

| 文件 | 作用 |
|---|---|
| [contracts/LONGRUN_PROTOCOL_V2.md](contracts/LONGRUN_PROTOCOL_V2.md) | C/D/W 身份、合法回交、权限、失败及恢复 |
| [contracts/MULTI_RUN_CONTROLLER.md](contracts/MULTI_RUN_CONTROLLER.md) | 多 Run 独立状态、物理资源及版本 |
| [contracts/longrun_schema_v2.json](contracts/longrun_schema_v2.json) | 既有机器合同（此次角色更名不修改） |
| [professional/README.md](professional/README.md) | 两类 Chat 的职责入口 |
| [templates/OWNER_GO.md](templates/OWNER_GO.md) | 新 Run 启动输入与真实授权 |
| [templates/PRO_DELEGATION.md](templates/PRO_DELEGATION.md) | 以 Skill 来源与输入事实为主的 D 正文 |
| [templates/TASK_PROGRESS.md](templates/TASK_PROGRESS.md) | 工作项—Skill—阶段—任务完成全景、依赖/版本/执行 Chat |
| [templates/WORKER_ORDER.md](templates/WORKER_ORDER.md) | V2 操作端 W 身份模板；专业细节由具体 Skill 决定 |
| [CONTROL_PLANE_ADAPTER.md](CONTROL_PLANE_ADAPTER.md) | Workflow/Skill 与 C/D/W 的边界 |
| [controller/CONTROLLER_OPERATIONS.md](controller/CONTROLLER_OPERATIONS.md) | 主控注册、真实调度、回收和恢复 |
| [tools/longrun_gate.py](tools/longrun_gate.py) | 现有只读机械核验和路由建议 |
| [tools/multi_run_check.py](tools/multi_run_check.py) | 多 Run 索引及工作区只读核验 |

## 4. 整体状态及接续

运行协调 Chat根据真实上游产物、Codex executor/历史 Worker 的专业 Return 和已采用 Workflow，持续维护 `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`。状态包含整体任务、各 Skill 的工作项、执行 Chat、输入和成果版本、实际完成范围、在途/阻断、历史失效及下一合法动作。**状态视图只投影已有真实事实，不是第二本权威账本。**

专业完成、实际操作结果怎么消费、什么时候返回上游，依具体 Skill 的原生结果与现行 Workflow；协调 Chat不额外设置独立专业 Gate。主控仅核真实消息送达、身份、引用、权限、去重与可用的后继，不替任何 Chat 决定专业问题。

## 5. 校验及当前边界

```bash
python -m unittest discover -s longrun/tests -v
python longrun/tools/longrun_gate.py validate-binding snapshot.json
python longrun/tools/longrun_gate.py validate-delegation snapshot.json
python longrun/tools/longrun_gate.py validate-order snapshot.json
python longrun/tools/longrun_gate.py validate-worker-return snapshot.json
python longrun/tools/longrun_gate.py validate-executor-execution snapshot.json  # Codex E 直接执行前
python longrun/tools/longrun_gate.py validate-executor-return snapshot.json
python longrun/tools/longrun_gate.py route-return snapshot.json
python longrun/tools/longrun_gate.py reconcile-actions snapshot.json
```

`snapshot.json` 必须由主控依据真实来源取得；离线校验成功不是物理发送成功。每个 Run 的 Owner GO、业务代码/Skill 采用版本、物理聊天、Worker 工作区和行动账本独立；不同 Run 不借用权限或完成事实。新提交不自动升级已锁定来源的 Run。新增专业 Skill 与新 Chat 组合仍须用真实任务验证。
