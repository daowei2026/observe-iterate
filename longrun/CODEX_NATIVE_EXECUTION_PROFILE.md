# Codex 原生直执行 Profile

> profile id：`CODEX_NATIVE_DIRECT`。本文件只规定物理执行方式，不重写专业任务定义或业务验收。

## 1. 适用场景

当一项长程工作需要频繁进行专业研究、读取代码和数据、统计或其他授权操作，并且在 Web Chat 与 Linux 间搬运会显著降低效率时，可由 Owner GO 显式采用本 profile。

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
- executor 数量按实际独立写面和工作量增加，不默认每个工作项新建一个。

## 3. 调用路径

```text
manager 形成 D
→ controller 核 D、Owner grants 和工作区绑定
→ controller 向 Codex executor 发送 C
→ executor 阅读 D 指定的专业依据和输入
→ executor 直接完成专业与必要操作
→ executor 形成原生结果和 PRO_RETURN
→ controller 核回交身份
→ manager 消费并安排后继
```

本 profile 不签发 `WORKER_ORDER`，也不产生 `WORKER_RETURN`。V2 schema 中 `workers=[]` 和空 `issued_order_refs` 是正常状态。

## 4. 三类角色会话的采用来源一致性

一次新启动或合法接续中，以下三类角色必须采用同一组精确的运行协议及专业任务来源（可跨仓/跨 commit，逐项锁定）：

```text
controller／主控会话
manager 会话
executor 会话
```

要求：

1. Owner 启动或接续信息提供明确采用来源，主控解析并锁定完整 commit，不以浮动分支继续执行；
2. controller 在派达时原样保留这组精确来源；
3. manager 将这组来源写入 `TASK_PROGRESS` 和下一项 D；
4. executor 在执行前读取本 D 实际采用的任务书、Workflow/Skill（如有）及输入；
5. Return 中说明实际采用的专业来源版本；
6. 若同一 Run 在途期间更新控制仓库，必须有新的明确接续调用，记录旧 commit、新 commit、适用起点和不需重做的既有产物。

更新专业任务来源不要求重建已有 manager／executor 线程。只要线程身份和 Run 绑定仍有效，可以在同一 Run 中接续；但不能只更新主控自己的理解，而让 manager 或 executor 继续按旧版专业来源工作。

cgpterm controller Skill 的 commit 与 `observe-iterate` 运行协议 commit 分开记录：前者决定物理调用方式，后者决定运行合同；专业任务依据独立记录，允许与运行合同同仓或不同仓。

## 4.1 启动后无 Owner 审批节点

新 Run 在初始 GO 中一次性明确业务目标、可自主执行或修改的范围、实际操作和提交权限。采用 `AUTONOMOUS` 后：

- 后续专业判断、研究及实际任务规定的授权内操作，由 executor 按已采用任务定义自主完成；
- manager 只消费回交、维护依赖和状态、签发已确定的下一项工作；不独立裁定业务方案，也不创建 Owner 确认节点；
- 主控不为已获授权的常规操作增加逐次审批；
- 技术资源缺失、证据不足或操作超出初始 GO 时，只记录具体阻断、缺口和恢复条件，继续其他独立工作；不能伪造扩权、自动修改业务目标或向 Owner 发送中途确认请求。

历史 Run 的 GO、Binding 与在途成果保持原样；采用新政策须有可追溯的正式新 Run 或有据的接续采用，不回写历史授权。

## 5. manager 边界

manager：

- 维护 TASK_PROGRESS 机器恢复视图；所有新 Run 同时维护 BUSINESS_PROGRESS 人类业务视图；
- 根据已采用任务定义签发具名专业工作；
- 消费真实 Return；
- 处理版本失效、等待、汇合和后继；不能决定新的业务目标或提出 Owner 审批节点。

manager 不：

- 代 executor 跑命令或改代码；
- 在 D 中另写一套专业方法；
- 因为没有 Worker 就把执行步骤全部搬进 manager；
- 自行扩大 Owner 写权限。

## 6. executor 边界

executor：

- 亲自阅读指定专业依据及适用补充；
- 在授权工作区直接执行本 D 要求的授权工作；
- 以任务原生完成条件形成结果；
- 明确代码、参数、数据、结果和未完成范围；
- 直接回原 manager。

executor 不需要为了执行 Linux 操作再创建 Worker。若当前操作不在启动 GO 的 grant 中，只阻断该动作并记录准确缺口及恢复条件，不升级为运行中 Owner 问询；其他合法专业工作继续。

## 7. 工作区和写面

每个 run_id 使用 Owner 已准备、且已核实没有其他 Run 占用的绝对路径；既有常用工作区有据释放后可复用，不要求重新创建目录。主控首次派发前核：

- 目录存在；
- `realpath` 与其他活跃 Run 不重叠；
- manager / executor 实际 cwd；
- 读写权限；
- 外部 Git 分支、缓存、数据库和结果目录是否仍有冲突。

路径绑定不等于写权限。代码提交、推分支、写数据库、覆盖缓存和发布结果必须被 GO 中的 `operation / execution_context / allowed_writes / authority_quote` 覆盖。

## 8. 多 Run

不同专业任务的独立业务线可各自采用本 profile 并行。每条线拥有独立 manager、executor、workspace 和专业状态。汇合条件写在具体任务输入中；主控只核真实回交及引用，不建立跨 Run 专业上级。

## 9. 失败与恢复

- C 发送效果未知：先查原通道，不直接重发；
- executor 中断：保留原 D、工作项、当前产物和 thread binding，合法续接；
- 工作区冲突：只阻断受影响 Run 的实际操作；
- 代码或参数版本改变：按实际任务依赖传播失效，不由运行层猜测；
- 专业任务来源或运行合同改变：明确记录采用起点，已有有效产物不机械重做；
- 需要 Web 专用能力时，作为具名单项例外处理，不把整个 manager/executor 迁回 Web。
