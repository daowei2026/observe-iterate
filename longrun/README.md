# 观察—迭代通用长程协作层 · V2 候选实现

> 位置：`daowei2026/observe-iterate`。此层是跨角色通信、交付和运行事实协议，不替代 L0/L1/L2 业务控制面。已提供离线机械校验与用例，不代表主控、手机／ChatGPT／Codex 物理通道或完整自动运行已经接通。

## 1. 用途与边界

Owner 给目标和允许边界；主控 Codex 实际派发、监控、回交并维护运行事实，不作专业结论；专业负责人 Pro 持有父业务任务的管理责任；专业执行人 Pro 承接具名专业 D，可以自己完成，也可以在权限内签 Worker W；Worker 结果先回签单 executor，再由 executor 完成专业核对并回 manager。

```text
Owner GO
  ↓
主控 Codex（机械收发／门禁／对账）
  └─ manager
       └─ D → executor
              ├─ 自己完成专业工作
              └─ W → Worker
                     └─ Worker Return → 原 executor
              └─ 专业回交 → 原 manager
```

D、W、C 是运行身份，不等于业务阶段、材料要求或问题身份。

材料准备采用当前 [A～E 外层 Workflow](../control/02_L1_观察材料准备流程.md)：

```text
A 特征事件级 occurrence 理解
    → B 观察位置准备
    → C 展示方式准备
A + B + C
    → D CAEGraph 定义集成
    → E CAEGraph 执行／运行
```

每个阶段的专业方法与字段见 [观察材料准备总入口](../skills/observation-material-preparation/SKILL.md)。历史旧“0～7 步”、S0～S5、Mxx 只用于既有成果追溯；R 按其现行 Skill 和管理视图组织。一次专业调用可以覆盖多个具备前置条件的内部步骤，但不能绕过尚未接受的上游产物。

## 2. 文件地图

| 文件 | 作用 |
|---|---|
| [contracts/LONGRUN_PROTOCOL_V2.md](contracts/LONGRUN_PROTOCOL_V2.md) | 运行身份、合法路径、委派／交付、授权、失败与接续 |
| [contracts/MULTI_RUN_CONTROLLER.md](contracts/MULTI_RUN_CONTROLLER.md) | 多 Run 身份隔离、独立 Linux 工作区和版本锁定 |
| [controller/CONTROLLER_OPERATIONS.md](controller/CONTROLLER_OPERATIONS.md) | 注册、调度、回收和恢复动作 |
| [controller/RUN_REGISTRY.json](controller/RUN_REGISTRY.json) | 空索引初稿，不是历史 Run 清单 |
| [controller/CGPTERM_ADOPTION_PENDING.md](controller/CGPTERM_ADOPTION_PENDING.md) | cgpterm 后续接入清单 |
| [contracts/longrun_schema_v2.json](contracts/longrun_schema_v2.json) | Binding、D/W、Return 和动作历史的机器合同 |
| [CONTROL_PLANE_ADAPTER.md](CONTROL_PLANE_ADAPTER.md) | 与当前 L0/L1/L2、A～E、Gate 和补证的接入合同 |
| [professional/README.md](professional/README.md) | manager／executor 专业角色入口 |
| [tools/longrun_gate.py](tools/longrun_gate.py) | 无副作用的离线身份、工单、回交和状态链校验 |
| [tools/multi_run_check.py](tools/multi_run_check.py) | 多 Run 注册表和工作区只读检查 |
| [templates/OWNER_GO.md](templates/OWNER_GO.md) | 新 Run 最小 GO 和授权 |
| [templates/TASK_PROGRESS.md](templates/TASK_PROGRESS.md) | A～E／R 到父任务的运行期完成全景模板 |
| [templates/MANAGEMENT_DECISION.md](templates/MANAGEMENT_DECISION.md) | manager 的 Gate、返修、补证和后继决定模板 |
| [templates/PRO_DELEGATION.md](templates/PRO_DELEGATION.md) | manager 签发的 D 正文模板 |
| [templates/WORKER_ORDER.md](templates/WORKER_ORDER.md) | executor 签发的 W 工单模板 |
| [MIGRATION_FROM_FPA.md](MIGRATION_FROM_FPA.md) | 旧 FPA longrun 的迁移边界 |

新版 `professional/` 是基于本仓当前观察—分析源重新组织的候选指南，不是旧指南副本。历史 Run 原封保留，不能标成新版实例。

## 3. 运行次序

1. Owner 发布真实 GO、专业材料入口和操作权限；主控检查身份、通道、账本与工作区，登记 `RUN_BINDING.json`。
2. 主控把同版本 manager 指南和业务源交给 manager；manager 只签具名 D，并写明已接受输入、适用阶段、专业产物和后继。
3. executor 根据同版本 executor 指南读取被委派的 A～E 或 R Skill，亲自承担专业工作；确需工具时签 W。
4. Worker 发布结果和证据；主控核实后交回原 executor。executor 按 Skill 接受、限域、返修或回流，再回 manager。
5. manager 消费结果，作 Gate、返修、补证、继续或结束决定，并更新 `MANAGEMENT_DECISION` 和 `TASK_PROGRESS`。主控只保存和回读，不替 manager 作专业决定。

状态未知或发送是否成功不明时先对账，不能重发。局部专业阻断不强制全 Run 停止。

## 4. A～E 在长程角色中的关键边界

- A～D 主要由 executor 依据 Skill 完成专业分析和定义；是否需要 Worker 取决于具体授权和工具需求。
- D 只形成完整 CAEGraph 定义，不派 Worker。
- E 内由 executor 签 W。Worker 只修权限内确定性问题，不能选择观察位置、改变展示语义或另算特征值。
- Worker 结果先回 executor；executor 用 D 核对最终脚本、用 C 预期 HTML 核对最终图。
- 最终图接受后才正式取得 CAEGraph 图数据，并检查图与数据一致性。
- 只有脚本或 HTML 不能形成 `DATA_READY`。

## 5. 管理 Pro 试运行模式

真实 GO 选定该模式时，manager 承担 L0/L1/L2 的业务 Gate、工作安排、返修、补证、收束和 [完成全景](../control/06_业务完成全景与更新协议.md) 管理判断。普通工作和 Gate 不逐项向 Owner 请示；实际 Worker 工具权限仍按 V2 `grants` 和环境核验。

运行期位置：

- `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`；
- `longrun/runs/<run_id>/business_control/decisions/<decision_id>.md`。

完成全景不是运行心跳，也不是新的独立权威数据库；它只投影真实阶段产物、Worker 记录、Gate 和业务决定。

## 6. 快速离线校验

```bash
python -m unittest discover -s longrun/tests -v
python longrun/tools/longrun_gate.py validate-binding snapshot.json
python longrun/tools/longrun_gate.py validate-delegation snapshot.json
python longrun/tools/longrun_gate.py validate-order snapshot.json
python longrun/tools/longrun_gate.py validate-worker-return snapshot.json
python longrun/tools/longrun_gate.py validate-executor-return snapshot.json
python longrun/tools/longrun_gate.py route-return snapshot.json
python longrun/tools/longrun_gate.py reconcile-actions snapshot.json
```

`snapshot.json` 必须是主控独立取得并核实的文件／回执／账本快照。离线 PASS 不能替代真实发送、锁、权限或专业 Gate。

## 7. 当前未完成／禁止冒充

- A～E 新 Workflow、三层 Gate 和角色映射仍需真实任务验证；
- cgpterm 物理收发、持久账本、并发独占锁、GitHub 远端证据读取和恢复对账尚未完成联调；
- 当前是运行合同和机械校验首版，不是可自主运行整条观察—分析任务的验收结论；
- 跳过专项测试 Run 不等于联调完成，首次真实调用仍须核实物理绑定、引用和回执。

## 8. 多 Run 首版

Owner 预先为不同 Run 准备独立 Linux 工作区，并在 GO 中逐 Run 给出绝对路径；主控不创建、不复用同一工作区。派 Worker 前在真实目标主机检查目录存在与 realpath 不重叠。每个 Run 的 A～E／R、manager、executor、Worker 和完成全景均独立。

```bash
python longrun/tools/multi_run_check.py validate-registry longrun/controller/RUN_REGISTRY.json
python longrun/tools/multi_run_check.py check-workspaces longrun/controller/RUN_REGISTRY.json --on-worker-host
```

现役 cgpterm 的固定 BASE 路径与单 Run 流程仍需后续接入；本文档和单元测试完成不等于物理多 Run 已打通。
