# 观察—迭代长程运行协作层 · V2

> 本目录负责跨线程的身份、真实通信、回交、状态与恢复；不替代专业 Workflow、Skill 或其完成条件。源码和配置存在，不代表真实线程、工作区和权限已经核验。

## 1. 角色

| 角色 | 作用 |
|---|---|
| Owner | 仅在 Run 启动时提供任务、范围、版本、工作区与一次性真实授权；运行中不承担审批或业务裁决 |
| 主控 | 注册 Run、绑定物理线程、发送／回收 C/D/W、核权限、去重与恢复 |
| Workflow manager（V2 `manager`） | 维护统一任务状态，按已采用 Workflow 调用 Skill、消费 Return、安排后继 |
| Skill executor（V2 `executor`） | 阅读并执行具名 Skill，形成原生产物和 Return |
| Worker（可选） | 仅在采用的执行 profile 和 Skill 明确需要时承担底层操作 |

`manager` 和 `executor` 是路由身份，不代表专业上下级。专业方法来自本 Run 锁定的 Workflow 和 Skill。

## 2. 两种执行 profile

### 2.1 兼容 profile

保留历史 ChatGPT executor + Codex Worker，以及新版 E 的 Codex executor 直执行路径。历史 Run 按当时锁定来源继续。

### 2.2 `CODEX_NATIVE_DIRECT`

入口：[`CODEX_NATIVE_EXECUTION_PROFILE.md`](CODEX_NATIVE_EXECUTION_PROFILE.md)

适用于 manager 和 executor 都在 Codex、executor 直接使用本 Run Linux 工作区的任务：

```text
Owner GO
→ 主控创建本 Run manager Codex thread
→ manager 签发一项 Skill 的 D
→ 主控创建／复用本 Run executor Codex thread并派发 C
→ executor 在授权工作区直接执行
→ executor Return
→ manager 消费并安排后继
```

此 profile 中：

```text
workers = []
不签发 W
不把 Linux 操作搬回 Web Chat
```

零 Worker 不降低专业完成条件，也不扩大 executor 写权限。

## 3. 当前专业流程

观察材料准备的 A～E 完整 Workflow 属于**历史 V0.2 控制面**，仅由准确采用该历史 commit 的 Run 使用，不应从当前 `control/02` 寻找已删除的旧文件。

当前统计驱动闭环采用 [control/01_L0_统计驱动的单特征闭环.md](../control/01_L0_统计驱动的单特征闭环.md)：

```text
首轮：U 理解 Feature → X 正式运行 → G 全量统计／发现
→ 如有待处理 finding：D 诊断，并在初始授权内处理
→ 发生正式行为或绑定变化时，进入后续轮次更新与验证
→ 当前目标达到后形成 FeatureReleaseGate／必要的 ReleasePackage
```

X 和工程修正是受授权的实际动作，不因直接在 Codex 中执行就成为新的专业 Skill。

## 4. 必要文件

| 文件 | 作用 |
|---|---|
| [contracts/LONGRUN_PROTOCOL_V2.md](contracts/LONGRUN_PROTOCOL_V2.md) | C/D/W 身份、合法回交、权限、失败及恢复 |
| [contracts/MULTI_RUN_CONTROLLER.md](contracts/MULTI_RUN_CONTROLLER.md) | 多 Run 独立状态、物理资源及版本 |
| [CODEX_NATIVE_EXECUTION_PROFILE.md](CODEX_NATIVE_EXECUTION_PROFILE.md) | Codex manager/executor 直执行、零 Worker profile |
| [professional/PRO_MANAGER_GUIDE.md](professional/PRO_MANAGER_GUIDE.md) | manager 职责 |
| [professional/PRO_EXECUTOR_GUIDE.md](professional/PRO_EXECUTOR_GUIDE.md) | executor 职责 |
| [templates/OWNER_GO.md](templates/OWNER_GO.md) | 通用历史模板 |
| [templates/OWNER_GO_CODEX_NATIVE.md](templates/OWNER_GO_CODEX_NATIVE.md) | Codex 原生直执行 GO 模板 |
| [templates/TASK_PROGRESS.md](templates/TASK_PROGRESS.md) | 通用历史进度模板 |
| [templates/TASK_PROGRESS_STATISTICS_CLOSURE.md](templates/TASK_PROGRESS_STATISTICS_CLOSURE.md) | 统计闭环机器状态与恢复模板 |
| [templates/BUSINESS_PROGRESS_STATISTICS_CLOSURE.md](templates/BUSINESS_PROGRESS_STATISTICS_CLOSURE.md) | 统计闭环的业务进展与产出阅读模板 |
| [CONTROL_PLANE_ADAPTER.md](CONTROL_PLANE_ADAPTER.md) | 专业控制面与运行协议边界 |
| [controller/CONTROLLER_OPERATIONS.md](controller/CONTROLLER_OPERATIONS.md) | 主控操作 |
| [tools/longrun_gate.py](tools/longrun_gate.py) | 单 Run 机械检查 |
| [tools/multi_run_check.py](tools/multi_run_check.py) | 多 Run 工作区和索引检查 |

## 5. 状态与真实事实

每个 Run 有两个用途明确的当前视图。**先看业务，再看运行细节**：

```text
longrun/runs/<run_id>/business_control/BUSINESS_PROGRESS.md  # 人类业务进展与成果入口
longrun/runs/<run_id>/business_control/TASK_PROGRESS.md      # 机器状态、精确版本、交接与恢复
```

历史 Run 可能只拥有 TASK_PROGRESS；不得伪造过去未生成的 BUSINESS_PROGRESS。

运行机器状态保存在：

```text
longrun/runs/<run_id>/business_control/TASK_PROGRESS.md
```

它只投影 Owner GO、Skill 原生产物和已核回执，不是第二本专业事实。文件存在、命令成功、结果已上传或 executor 自述完成，均不能替代 Skill 自己的完成条件。

不同 Run 的工作区、物理线程、权限、代码版本和结果独立。一个 Run 等待时，其他非冲突 Run 可以继续；不得借用其他 Run 的 executor thread、工作区或授权。

## 5.1 主控 Chat 归档（只导主控）

主控 Chat 的人类沟通记录放在 [controller/chats/](controller/chats/README.md)，按实际 Codex 主控线程身份保存。由 cgpterm Controller Skill 调用现有 App Server 只读能力提取用户／主控可见消息并向本仓受授权分支提交；不会收集 manager、executor 的原始聊天，避免与已有 D/Return/专业报告重复。

归档是帮助人追溯 Owner 输入与主控沟通，不是本 Run 的 `BUSINESS_PROGRESS`，也不能替代专业成果和业务 Gate。尚未看到真实 `<thread-id>.md` 时，应视为尚未确认归档成功。

## 6. 校验

```bash
python -m unittest discover -s longrun/tests -v
python longrun/tools/longrun_gate.py validate-binding snapshot.json
python longrun/tools/longrun_gate.py validate-delegation snapshot.json
python longrun/tools/longrun_gate.py validate-executor-execution snapshot.json
python longrun/tools/longrun_gate.py validate-executor-return snapshot.json
python longrun/tools/longrun_gate.py route-return snapshot.json
python longrun/tools/multi_run_check.py ...
```

离线校验成功不证明物理发送、Linux 目录、模型选择或权限已经真实生效。
