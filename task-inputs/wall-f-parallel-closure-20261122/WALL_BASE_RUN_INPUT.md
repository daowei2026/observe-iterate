# WALL 基础 Feature Run 输入

> 状态：Owner 已锁定 EAW 用例、品种、2021 全年范围、工作区和远端修复代码；仍需在真实 GO 前从锁定用例与代码解析精确执行入口、参数实例及结果复用决定。

## 1. 目标 Feature 与用例

```yaml
business_name: WALL
feature_type: WallAssembler
use_case_ref: task-inputs/eaw-p1-integrated
code_repository: daowei2026/tis
remote_branch: codex/wall-output-consistency-20261121
code_commit: 6618d4d147d6ebbe634e61facddf2c9a0b996982
constructor_or_execution_entry: RESOLVE_FROM_LOCKED_EAW_P1_USE_CASE_AND_CODE
parameter_instance_policy: USE_THE_EAW_P1_WALL_INSTANCE; DO_NOT_TUNE_OR_SUBSTITUTE_WITHOUT_OWNER_CONFIRMATION
```

正式版本锁：

```text
daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982
```

已核实的修复链：

```text
19e6b15ee4a5a58c71bf40902bbc6f6657a16ea2  D1：事件位置与最终 tick 状态同步
4d06ec211d0a20f2ded80417a3334c78cf4b1a0e  D2：同拍 End 优先于进入 Dormant
6618d4d147d6ebbe634e61facddf2c9a0b996982  D4：有效支撑恢复时清零连续 far 计数
```

上述三项是 Owner 已确认并已提交的当前输入，不在本 Run 中重复走修改确认。

## 2. Owner 锁定的正式运行范围

```yaml
symbols: [rb, m]
start_time: 2021-01-01
end_time: 2021-12-31
sides: [bid, ask]
sampling: current formal tick input used by the EAW P1 WALL instance
calendar: RESOLVE_FROM_LOCKED_EAW_P1_INSTANCE; NO_SUBSTITUTION
workspace: /dwdhome/fy/BASE_E6_2
scope_change_policy: OWNER_CONFIRMATION_REQUIRED
```

这不是候选范围。AI 不得自行换品种、扩缩正式年份、换输入尺度或换工作区。可在该正式范围内用少量位置／短窗口做诊断，但正式结果必须覆盖上述范围。

## 3. 当前已知输入处理

前次运行曾对 m 的全空占位行作具名处理。新 Run 需要核实：

- 当前正式入口是否仍遇到该类占位；
- 处理是否只针对全空占位；
- 对 rb/m 有效行情是否保持不变。

若需要改变正式数据处理方式，应先形成 `ModificationProposal`，经 Owner 确认后采用；不得因为旧 Chat 曾这样处理就无痕继承，也不得自行换一种处理。

## 4. 既有理解复用

正式起点：

```text
task-inputs/eaw-p1-integrated/feature-understanding-result/WALL_FEATURE_UNDERSTANDING_PACKAGE.md
```

执行 AI 负责：

- 直接复用未受影响内容；
- 只核对 D1 对事件位置／载荷、D2 对同拍状态仲裁、D4 对 far 计数与支撑语义造成的差异；
- 补本轮统计实际需要而旧包缺少的最小事实；
- 记录 delta 或更新受影响部分。

Owner 不需要另行整理上一轮理解材料，也不要求本 Run 先重写完整 Package。

## 5. X｜运行或验证复用

优先级：

1. 若最终修正版完整结果包与本轮代码、参数、正式范围、日历及输入处理完全一致，验证身份、SHA 和读回后可复用；
2. 否则用锁定提交和 EAW P1 WALL 实例在正式工作区重新运行。

无论新跑还是复用，必须对最终修正版重新执行本轮完整统计。

## 6. Owner 锁定的统计与分析问题

本轮首先回答：

1. 从输入到 WALL 输出有哪些真正业务对象／业务概念，各自围绕哪些属性判断；
2. 上下游业务对象怎样处理，包含什么时序逻辑，并对应到哪些 Feature、Event、occurrence 和字段；
3. 每个业务对象发生多少次，与上游对象的次数、转化和发生位置相比是否异常；
4. 对存在方向的对象，bid / ask 分开统计；
5. 在最终版本上复验 D1、D2、D4，并重新量化 D3；
6. 在完成上述统计时继续寻找新的明显合理性问题；
7. 所有正式表格行说明计数单位、分母和业务含义。

AI 可以增加为回答这些问题真正需要的统计，不要求机械穷尽一张固定指标大全，也不能把补充统计自动升级为新的 Owner 验收条件。

## 7. 新 finding 与修改确认

每个新 finding 先独立定位现象、业务冲突、相关逻辑、参数／常量和最早责任阶段。若建议改变正式代码、参数、配置、规则、数据处理或输出合同：

```text
形成 ModificationProposal 和验证方案
→ 回 Owner 确认
→ 确认后才实施并采用
→ 完整重跑和重统计
```

未确认的候选 patch 可以用于隔离诊断，但不得提交、推送或登记为本 Run 正式版本。

## 8. 运行配置

```yaml
execution_profile: CODEX_NATIVE_DIRECT
run_id: ASSIGN_AT_REAL_GO
workspace: /dwdhome/fy/BASE_E6_2
manager: new Codex thread
executor: new Codex thread
workers: []
```
