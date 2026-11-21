# 长程运行中的两类 Chat

本目录定义两类**运行职责**，不是两种专业 Agent。专业工作依据本 Run 采用的 Workflow 与具体 Skill；V2 的 `manager` / `executor` 字段继续作为**机读路由身份**。

| 运行职责 | 文件 | 主要作用 |
| --- | --- | --- |
| **多层 Workflow 运行协调 Chat**（`manager`） | [PRO_MANAGER_GUIDE.md](PRO_MANAGER_GUIDE.md) | 维护整体任务状态、按既定 Workflow 调用和接续 Skill、管理依赖/版本及按需增加执行 Chat；不自行增加专业判断或额外 Gate |
| **Skill 执行 Chat**（`executor`） | [PRO_EXECUTOR_GUIDE.md](PRO_EXECUTOR_GUIDE.md) | 每次按被调用 Skill 的完整专业文件实际执行、自检并产生原生结果；不预设固定专业角色 |

当前观察材料准备依据 [A～E 外层 Workflow](../../control/02_L1_观察材料准备流程.md) 和 [五个 Skill](../../skills/observation-material-preparation/SKILL.md)：A 后 B/C 可并行，D 汇合，E 运行、核图和取数。Skill 内部步骤由各自 Skill 管理，不作为默认单独调用单位。合理性分析仍按后续实际采用版本执行，不在本目录预设固定调用序列。

**职责边界**：协调 Chat 只传任务身份、准确 Skill 与输入产物来源、回交对象，不自拟执行约束、专业方法、Worker 结果处理或验收标准；执行 Chat 完成 Skill 自身定义的工作。主控负责 C/D/W 真实发送、回执、去重、工作区和授权校验；Run 状态继续使用既有 `TASK_PROGRESS` 视图与 GitHub 原件。

现有 C/D/W、V2 Return、Worker 回原签发 executor 的通信路由及版本锁不变；本次不新增 Schema、自动 Gate 或状态引擎。

**新版 E 执行环境**：E 默认为本 Run 独立 Codex executor；共享理解和 B～D 默认 ChatGPT executor。两者使用相同的 D/C/专业 Return 路由。E 零 W 时依真实操作与图/数据专业交付，不靠 W 回执判完成；旧 Run 按原采用版本。
