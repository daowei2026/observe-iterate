# Codex 原生直执行 Profile

> profile id：`CODEX_NATIVE_DIRECT`。本文件只规定物理执行方式，不重写专业 Workflow、Skill、Gate 或业务验收。

## 1. 适用场景

当一项长程工作需要频繁读取代码、运行 Feature、统计、修改和回归，并且在 Web Chat 与 Linux 间搬运会显著降低效率时，可由 Owner GO 显式采用本 profile。

## 2. 物理结构

```text
controller
├─ Codex manager thread
└─ one or more Codex executor threads
     └─ direct access to this run's Linux workspace

workers = []
```

- manager 与 executor 必须是本 Run 新建或本 Run 已绑定的线程；
- 不查找、借用其他 Run 的 thread id；
- 同一 Run 恢复时先核已有线程真实状态，再决定复用；
- executor 数量按实际独立写面和工作量增加，不默认每个 Skill 新建一个。

## 3. 调用路径

```text
manager 形成 D
→ controller 核 D、Owner grants 和工作区绑定
→ controller 向 Codex executor 发送 C
→ executor 阅读指定 Skill 和输入
→ executor 直接完成专业与必要操作
→ executor 形成原生结果和 PRO_RETURN
→ controller 核回交身份
→ manager 消费并安排后继
```

本 profile 不签发 `WORKER_ORDER`，也不产生 `WORKER_RETURN`。V2 schema 中 `workers=[]` 和空 `issued_order_refs` 是正常状态。

## 4. manager 边界

manager：

- 维护 TASK_PROGRESS；
- 根据已采用 Workflow 签发一项 Skill 工作；
- 消费真实 Return；
- 处理版本失效、等待、汇合和后继。

manager 不：

- 代 executor 跑命令或改代码；
- 在 D 中另写一套专业方法；
- 因为没有 Worker 就把执行步骤全部搬进 manager；
- 自行扩大 Owner 写权限。

## 5. executor 边界

executor：

- 亲自阅读指定 Skill 及适用补充；
- 在授权工作区直接查代码、运行、统计、修正和验证；
- 以 Skill 原生完成条件形成结果；
- 明确代码、参数、数据、结果和未完成范围；
- 直接回原 manager。

executor 不需要为了执行 Linux 操作再创建 Worker。若当前操作不在 Owner grant 中，只阻断该动作并报告准确缺口；其他合法专业工作继续。

## 6. 工作区和写面

每个 run_id 使用 Owner 已准备的独立绝对路径。主控首次派发前核：

- 目录存在；
- `realpath` 与其他活跃 Run 不重叠；
- executor 实际 cwd；
- 读写权限；
- 外部 Git 分支、缓存、数据库和结果目录是否仍有冲突。

路径绑定不等于写权限。代码提交、推分支、写数据库、覆盖缓存和发布结果必须被 GO 中的 `operation / execution_context / allowed_writes / authority_quote` 覆盖。

## 7. 多 Run

WALL、F 等独立业务线可各自采用本 profile 并行。每条线拥有独立 manager、executor、workspace 和 Gate。汇合条件写在具体任务输入中；主控只核真实 Gate，不建立跨 Run 专业上级。

## 8. 失败与恢复

- C 发送效果未知：先查原通道，不直接重发；
- executor 中断：保留原 D、工作项、当前产物和 thread binding，合法续接；
- 工作区冲突：只阻断受影响 Run 的实际操作；
- 代码或参数版本改变：按专业控制面传播失效，不由运行层猜测；
- 需要 Web 专用能力时，作为具名单项例外处理，不把整个 manager/executor 迁回 Web。
