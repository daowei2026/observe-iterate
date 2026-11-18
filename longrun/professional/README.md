# 长程专业角色指南（候选 V0.1）

本目录回答“专业负责人 Pro / 专业执行人 Pro 的专业工作做什么”；它不是第二套长程运行协议，也不是一套独立的观察／合理性分析 Skill。正式 C/D/W 派发和 Return 以 [长程 V2 协议](../contracts/LONGRUN_PROTOCOL_V2.md) 为准。

## 按角色读取

| 角色 | 文件 | 业务工作 |
|---|---|---|
| 专业负责人 Pro（manager） | [PRO_MANAGER_GUIDE.md](PRO_MANAGER_GUIDE.md) | 试运行 GO 授权后执行业务控制面：Gate、异常与补证、完成全景、M↔R 接续及逐问题收束；不自行发明专业标准 |
| 专业执行人 Pro（executor） | [PRO_EXECUTOR_GUIDE.md](PRO_EXECUTOR_GUIDE.md) | 根据当前 D 使用观察材料准备 A～E Skills 或合理性分析 Skills 完成实际专业工作；E 中分别签 W1 运行／修复和 W2 正式取数工单，并亲自作专业核对 |

一次专业调用不等于一个 A～E 阶段、一个内部步骤、一个 R 阶段或一种材料。manager 按 Control 的输入输出依赖组织 D；executor 可以在一份 D 内贯通具备前置条件的相邻工作，但不能把尚未形成或尚未接受的上游产物当成已具备。

## 必须以当前专业源为准

- [材料准备外层 Workflow](../../control/02_L1_观察材料准备流程.md)：A occurrence 理解 → B 观察位置／C 展示方式 → D 定义集成 → E 执行、核图后取数。
- [材料准备总入口与五个阶段 Skill](../../skills/observation-material-preparation/SKILL.md)：A／C／E 有内部 Workflow；B 只记录当前经验性用法；D 是单一集成动作，没有 `WORKFLOW.md`；E 另有 Worker 派单合同和 W1／W2 两份工单模板。
- [合理性分析 Skills README](../../skills/reasonableness-analysis/README.md)：最小预期与探索、冻结后正式对照、值得才诊断、可调才标定。
- [L0](../../control/01_L0_完整业务任务与双向衔接.md)、[L2 I/O](../../control/04_L2_节点输入输出登记表.md)、[Gate](../../control/05_三级Gate及后继路由.md)、[完成全景](../../control/06_业务完成全景与更新协议.md)：业务控制逻辑均为候选设计，不是生产级强制 Gate 服务。
- [审查与未决](../../review/06_接口对齐与缺环审查.md)、[运行路径走查](../../review/07_待确认的控制判断与运行路径.md)：尚需真实任务验证。

历史报告中出现旧“0～7 步”、Mxx 或其他旧结构，属于当时事实；新任务以当前 A～E 规范为准，不回写历史。

## 角色边界

### manager

- 传递 Owner 已给目标、外层输入和当前有效上游产物；
- 根据 A～E／R 的现有合同安排工作和检查消费资格；
- 不因自己没有新增专业信息而给 executor 增加新的业务验收目标；
- 依据实际结果决定返回 A/B/C/D/E、进入 R、补证或收束；
- 维护阶段→M/R→问题→父任务的完成全景。

### executor

- 亲自读取并执行被委派阶段的专业文件；
- 形成对应阶段原生产物，不能只写工单或概念说明；
- C 可只读使用实例，但必须给 D 保留实例注入接口；D 亲自理解仓库并完成真实实例绑定；
- E 的专业 Workflow 由 executor 自己执行，真实操作再按 W1／W2 分开派给 Worker；
- Worker 结果先回 executor，由 executor 完成与 D/C 的核对、正式取数准入和数据一致性检查；
- 不自行扩大 D、替 Owner 作业务取舍或让 Worker 决定专业目标。

## 最小使用方式

1. manager 的完整任务引用当前 commit 下的 Control 和本指南；executor 的完整任务含 D 正文、executor 指南、适用阶段 Skill 和已接受上游产物。
2. manager 只签具名专业 D；executor 判断并签发当前合法的 Worker 工单。W2 不能在最终图接受前提前签发。Worker 结果必须先回 executor。
3. 回交引用真实阶段产物、版本、限制和未决；角色指南不能替代数据、图、Gate 或业务结果。
4. 文档变更不能静默更新既有 Run；采用时固定 commit。

## 明确未完成

A～E 新 Workflow 和双 Pro 角色映射尚未经过完整的 manager→executor→worker→executor→manager 多轮真实验证；cgpterm 物理消息、工具可用性、受保护状态和正式 Gate 权限仍需在真实任务中核实。
