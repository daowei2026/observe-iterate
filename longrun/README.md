# 观察—迭代通用长程协作层 · V2 候选实现

> 位置：`daowei2026/observe-iterate` 的 `docs/observe-iterate-control-plane-3layer-v0.1-20261114` 分支。此层是跨角色通信/交付/运行事实协议，不是 L0/L1/L2 业务控制面的替代品。**已提供离线机械校验与用例，不代表已经接通主控、手机/ChatGPT/Codex 物理通道或完整自动运行。**

## 1. 用途与边界

Owner 给目标和允许边界；主控 Codex 实际派发、监控、回交、维护运行事实，不作专业结论；专业负责人 Pro 保有父业务任务的专业责任；专业执行人 Pro 承接明确的专业子任务，可以直接产出专业结果，也可以正式签 Worker 工单；Worker Codex 按其工单实施可核对的操作，结果先回签单的专业执行人。专业执行人再将已判断/未决交回原专业负责人。**负责人如何组织和接收工作、执行人怎样按既有专业 Skill 工作，见本目录 [professional/](professional/README.md) 两份候选角色指南。** 原 Skill 本身仍是专业方法权威，候选角色适配不构成正式 Gate 或权限授权。

```text
Owner GO
  │
  ▼
主控 Codex（收发/门禁/对账，非专业决策）
  ├─ 专业负责人 Pro
  │     └─ D：专业委派 → 专业执行人 Pro
  │                              ├─ 自己完成专业工作
  │                              └─ W：工单 → Worker Codex
  │                                         └─ Worker Return → 原专业执行人
  │                              └─ 专业回交 → 原专业负责人
  └─ 必要时调用已授权、规则确定的校验程序
```

这里 `D`（专业委派）、`W`（操作工单）、`C`（实际模型调用）与业务 `Mxx/Rxx` 节点、`S0～S5/R0～R5` 阶段、`MaterialRequirement` 不同。一个专业调用可完成多个业务节点，一个节点可需要多次调用。**不强制一阶段一次 Pro 调用，也不把每项材料都派成一个 Worker 工单。**

## 2. 文件地图

| 文件 | 作用 |
|---|---|
| [contracts/LONGRUN_PROTOCOL_V2.md](contracts/LONGRUN_PROTOCOL_V2.md) | 运行身份、合法路径、委派/交付、授权、失败与接续规范 |
| [contracts/longrun_schema_v2.json](contracts/longrun_schema_v2.json) | Binding、委派、工单、各类 Return 与动作历史的机器字段合同 |
| [CONTROL_PLANE_ADAPTER.md](CONTROL_PLANE_ADAPTER.md) | 与本分支候选 L0/L1/L2、Gate、补证和 Skill 的接合位置，不偷定专业规则 |
| [professional/README.md](professional/README.md) | 专业角色使用入口：负责人管完整任务和专业交付接收；执行人按原观察/合理性分析 Skill 承担实质工作 |
| [tools/longrun_gate.py](tools/longrun_gate.py) | **只读、无副作用**的离线身份、工单、回交、状态链校验；不发送、不写账本 |
| [tests/test_longrun_gate.py](tests/test_longrun_gate.py) | 可运行的正/反向离线夹具，无法证明真实通道接通 |
| [templates/OWNER_GO.md](templates/OWNER_GO.md) | 新 Run 的最小 GO 信息与明确授权 |
| [templates/TASK_PROGRESS.md](templates/TASK_PROGRESS.md) | 管理 Pro 在真实 Run 持续维护的五级业务完成全景模板；运行期实际文件按 Run 生成 |
| [templates/MANAGEMENT_DECISION.md](templates/MANAGEMENT_DECISION.md) | 管理 Pro 的 Gate、返修、补证和后继业务决定原件模板 |
| [templates/PRO_DELEGATION.md](templates/PRO_DELEGATION.md) | 专业负责人签发的 D 专业委派正文 |
| [templates/WORKER_ORDER.md](templates/WORKER_ORDER.md) | 专业执行人签发的 W 工单正文 |
| [MIGRATION_FROM_FPA.md](MIGRATION_FROM_FPA.md) | 旧特征生产 longrun 的保留/不迁入/改变清单 |

**不迁入旧 FPA 的 `PRO_MANAGER_GUIDE.md`、`WORKER_EXECUTION_GUIDE.md`、特征生产专属 GO 模板、Runner 字段和历史 `runs/`；新版 `professional/` 是基于本仓观察—分析源重新组织的候选指南，非旧指南副本。** 历史 Run 原封保存在 `feature-production-agent/longrun/runs/`，不能标成新版实例；新版 `runs/<run_id>/` 只在真实 GO 发生后建立。

## 3. 运行次序（不等于软件已打通）

1. Owner 发布真实 GO、专业材料入口和操作权限；主控检查身份、现役聊天/线程、可信账本与可用工作区，登记 `RUN_BINDING.json`。
2. 主控把正式任务及同版本 [专业负责人指南](professional/PRO_MANAGER_GUIDE.md) 作为来源交给绑定的 manager；其根据真实问题及材料、R 分析依赖签发具名专业委派 D，主控核身份/来源/授权后送执行人。
3. D 的执行人根据 [专业执行人指南](professional/PRO_EXECUTOR_GUIDE.md) 读取本次有权的材料准备或合理性分析 Skill，并**亲自承担专业分析**；能直接完成时零 W 回交；确需执行工具时签 W，主控检查 W 与 D、授权、去重、实际工作区独占后送 Worker。
4. Worker 发布结果和实物证据；主控用可信实际回执核实、交还签单专业执行人。专业执行人检查、形成专业结果，再回原专业负责人。
5. 专业负责人消费结果后执行本次业务 Gate、决定新委派/返修/补证/继续/有据结束；**同轮提交具体业务决定与受影响的五级完成全景更新**。若 Pro 不能直接写 GitHub，主控按其原文保存并回读；主控不替 Pro 作专业决定，也不从 Return `COMPLETE` 推断父任务完成。

状态未知/发送是否成功不明时，**先核实原物理通道和账本，不能重发**。专业阻断与确定性缺字段应分流，不强制全 Run 暂停。完整条件在协议中。

## 4. 本次优先采用管理 Pro 执行控制面的试运行模式

当 Owner 的真实 GO 选定此模式时，不等待业务控制程序，manager 承担 L0/L1/L2 的业务 Gate、工作安排、返修、补证、任务收束和 [control/06](../control/06_业务完成全景与更新协议.md) 的全部管理判断。**普通工作和 Gate 不逐项向 Owner 请示；** 实际 Worker 工具权限仍通过 V2 一次性 GO 的真实 `grants` 和运行环境核验。

Run 内当前业务完成全景约定位置为 `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`，管理决定为 `.../decisions/<decision_id>.md`。每次 manager 获得新的可核实节点/阶段/Gate 结果后，将全景增量变化与决定在同轮回交，主控只负责按原文持久化并核实际 commit。历史接受与当前需要重验的成果分别保存；没有新事实不需要反复重写进度。**业务完成全景不是 `long-task-status` 的运行心跳，也不是新的独立权威数据库**。详细接线见 [CONTROL_PLANE_ADAPTER](CONTROL_PLANE_ADAPTER.md) 和 [manager 指南](professional/PRO_MANAGER_GUIDE.md)。

具体特征输入尚未就绪时，不为此虚构业务 Run；Owner 随后用实际任务自然检验跨角色收发与 Worker 往返，不另强制设立专门测试 Run。首次真实调用仍必须满足主控的物理绑定、精确引用与回执核验，不能声称已经联调通过。

## 5. 快速离线校验

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

`snapshot.json` 是主控**独立获取且已核实**的文件/回执/账本只读快照，不是被派发者自述的事实，也不是自动从 GitHub 单方文件形成的权威状态。校验脚本不连接 GitHub、不验证签名/真实聊天、不取得锁；这些必须由主控及真实工具另行实施，不能拿离线 PASS 当派发许可证。

## 6. 当前未完成 / 禁止冒充

- 本分支 `control/`、`review/` 明说三层业务 Gate 和部分完成/限域政策尚待确认，`professional/` 的角色分工也为待验证适配，不预先固定这些判定结果。
- cgpterm 已提交专门的 V2 主控 Skill，但物理收发、持久动作账本、并发独占锁、GitHub 远端证据读取、专业角色指南的实际派发和恢复对账 **尚未与 V2 完成联调**。
- 当前仅是**运行合同 + 机器校验首版**，不是“立刻可自主运行整条观察—分析长程任务”的验收结论。
