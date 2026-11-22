# 观察—迭代长程运行协作层 · V2

> 本目录负责跨线程的身份、真实通信、回交、状态与恢复；不替代专业 Workflow、Skill 或其完成条件。源码和配置存在，不代表真实线程、工作区和权限已经核验。

## 1. 角色

| 角色 | 作用 |
|---|---|
| Owner | 提供业务任务、范围、版本、工作区和真实运行授权 |
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

观察材料准备仍依据 `control/02` 和 B～E Skills；共享 Feature 理解有效后，B/C 可按依赖并行，D 汇合，E 运行和取数。

统计驱动闭环可采用 `control-v0.3/`：

```text
U 共享理解
→ X 运行最新实例
→ G 全量统计
→ D/工程修正/参数处理
→ 重跑重统计
→ FeatureReleaseGate
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
| [templates/TASK_PROGRESS_STATISTICS_CLOSURE.md](templates/TASK_PROGRESS_STATISTICS_CLOSURE.md) | 统计闭环的轻量进度模板 |
| [CONTROL_PLANE_ADAPTER.md](CONTROL_PLANE_ADAPTER.md) | 专业控制面与运行协议边界 |
| [controller/CONTROLLER_OPERATIONS.md](controller/CONTROLLER_OPERATIONS.md) | 主控操作 |
| [tools/longrun_gate.py](tools/longrun_gate.py) | 单 Run 机械检查 |
| [tools/multi_run_check.py](tools/multi_run_check.py) | 多 Run 工作区和索引检查 |

## 5. 状态与真实事实

每个 Run 的当前视图保存在：

```text
longrun/runs/<run_id>/business_control/TASK_PROGRESS.md
```

它只投影 Owner GO、Skill 原生产物和已核回执，不是第二本专业事实。文件存在、命令成功、结果已上传或 executor 自述完成，均不能替代 Skill 自己的完成条件。

不同 Run 的工作区、物理线程、权限、代码版本和结果独立。一个 Run 等待时，其他非冲突 Run 可以继续；不得借用其他 Run 的 executor thread、工作区或授权。

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
