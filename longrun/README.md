# 通用长程运行协作层 · V2

本目录只定义跨线程的真实运行、身份、权限、状态与恢复。专业任务由每次 Run 采用的来源决定；不默认加载本仓 control/、skills/ 或任何业务阶段。任务书本身可以是完整专业依据。文件存在不代表实际线程、授权或自动运行已核验。

## 1. 角色与运行路径

| 角色 | 职责 |
|---|---|
| Owner | 初始任务、边界、执行配置及真实授权 |
| controller | 注册、绑定、传输、核验、对账、保存、调度和恢复 |
| manager | 依据本 Run 专业任务定义组织具名工作、维护依赖和两类进度，消费真实回交 |
| executor | 执行具名专业工作、读取实际专业依据、实际产出、自检和回交 |
| worker（可选） | 按授权 W 执行底层操作，回原 executor |

一项 D 是具名专业工作，不要求存在 Skill。一项 D 可跨多个 C 接续，内部小步骤不默认拆 D。专业判断由 executor，工作后继由 manager，主控不参与专业裁决。

- [Codex 原生直执行](CODEX_NATIVE_EXECUTION_PROFILE.md)：manager/executor 均为 Codex；workers=[]。
- 兼容物理配置：按本 Run 实际绑定的 Web/Codex 角色及可选 Worker 路由；旧 Run 按原采用来源继续。
- 新 Run 新建独立会话；同 Run 恢复核对并复用原绑定，不借其他 Run 的 thread。
- 同时占用资源的不同 Run 采用互不重叠的工作区；有据释放后可复用常用工作区，远端共享写面仍须核实单写者。

## 2. 专业任务接入

统一采用 [CONTROL_PLANE_ADAPTER.md](CONTROL_PLANE_ADAPTER.md)。Owner 的任务书/启动消息或已存在 Workflow + Skill 都可作为专业来源；允许混合，也允许结果驱动的后继。不强制独立计划、专业适配文件或任务类型注册。专业来源、运行协议及物理主控实现分别锁定精确版本，同一 Run 各角色一致。已有专业任务的 control/ 和 skills/ 保持其自身权威，不是运行层默认入口。

## 3. 运行协议及模板

| 文件 | 作用 |
|---|---|
| [LONGRUN_PROTOCOL_V2](contracts/LONGRUN_PROTOCOL_V2.md) | C/D/W、授权、真实回交与恢复 |
| [MULTI_RUN_CONTROLLER](contracts/MULTI_RUN_CONTROLLER.md) | 多 Run 资源、状态及采用版本 |
| [CODEX_NATIVE_EXECUTION_PROFILE](CODEX_NATIVE_EXECUTION_PROFILE.md) | 物理执行配置 |
| [PRO_MANAGER_GUIDE](professional/PRO_MANAGER_GUIDE.md) | 通用协调职责 |
| [PRO_EXECUTOR_GUIDE](professional/PRO_EXECUTOR_GUIDE.md) | 通用专业执行职责 |
| [OWNER_GO](templates/OWNER_GO.md) / [CODEX_NATIVE](templates/OWNER_GO_CODEX_NATIVE.md) | 通用启动输入与权限 |
| [PRO_DELEGATION](templates/PRO_DELEGATION.md) | 具名专业工作委派 |
| [TASK_PROGRESS](templates/TASK_PROGRESS.md) / [BUSINESS_PROGRESS](templates/BUSINESS_PROGRESS.md) | 通用恢复与业务阅读模板 |
| [CONTROLLER_OPERATIONS](controller/CONTROLLER_OPERATIONS.md) | 主控运行规程 |
| [longrun_gate.py](tools/longrun_gate.py) / [multi_run_check.py](tools/multi_run_check.py) | 只读机械核验 |

专业模板可由本 Run 的任务来源显式指定或已有专业 Workflow 明确引用。如统计闭环的 [TASK_PROGRESS_STATISTICS_CLOSURE](templates/TASK_PROGRESS_STATISTICS_CLOSURE.md) 和 [BUSINESS_PROGRESS_STATISTICS_CLOSURE](templates/BUSINESS_PROGRESS_STATISTICS_CLOSURE.md)，原样保留，不要求其他任务适配。原历史观察模板保存在 [TASK_PROGRESS_OBSERVATION_LEGACY](templates/TASK_PROGRESS_OBSERVATION_LEGACY.md) 及历史 commit 中；旧 Run 不静默升级。

## 4. 运行记录

```
longrun/runs/<run_id>/
  OWNER_START.md
  RUN_BINDING.json
  RUN_RESOURCE_BINDING.json
  business_control/TASK_PROGRESS.md
  business_control/BUSINESS_PROGRESS.md
  calls/
  delegations/
  ... 实际产生的记录
```

TASK_PROGRESS 服务技术恢复；BUSINESS_PROGRESS 服务 Owner 阅读。manager 根据真实专业产物更新两种视图，不重做分析。主控验证、保存及路由，不能凭文件存在或自报完成推断实际完成。专业内容依任务原件；仅保存有授权的材料，大体积或敏感数据用可核实引用。主控 Chat 归档仍按 [controller/chats](controller/chats/README.md) 和初始授权执行，仅主控自身可见对话。

## 5. 校验

```sh
python -m unittest discover -s longrun/tests -v
python longrun/tools/longrun_gate.py validate-binding snapshot.json
python longrun/tools/longrun_gate.py validate-delegation snapshot.json
python longrun/tools/longrun_gate.py validate-executor-execution snapshot.json
python longrun/tools/longrun_gate.py validate-executor-return snapshot.json
python longrun/tools/longrun_gate.py route-return snapshot.json
```

离线校验不证明真实通道、权限、工作区锁或自动唤醒。版本升级不改变历史 GO、专业事实及绑定；兼容性不足须记录明确迁移，不改回公共文件来切换任务。
