# WALL 基础 Feature Run 输入

> **状态：EAW 用例、品种、2021 全年范围、工作区、远端修复代码、正式 producer 入口和默认参数已锁定。** 正式启动仍须完成工作区与结果包预检。

## 1. 目标 Feature、用例与精确版本

```yaml
business_name: WALL
feature_type: WallAssembler
use_case_ref: task-inputs/eaw-p1-integrated
code_repository: daowei2026/tis
remote_branch: codex/wall-output-consistency-20261121
code_commit: 6618d4d147d6ebbe634e61facddf2c9a0b996982
source_file: hf/prel0/wall_assembler.py
python_class: mquant.tis.hf.prel0.wall_assembler.WallAssembler
formal_entry: WallAssembler().run() / the same formal full-instance production path already used by the archived WALL chat
parameter_policy: use WallAssembler defaults at the locked commit; no tuning or substitution without Owner confirmation
```

正式版本锁：

```text
daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982
```

已核实修复链：

```text
19e6b15ee4a5a58c71bf40902bbc6f6657a16ea2  D1：事件位置与最终 tick 状态同步
4d06ec211d0a20f2ded80417a3334c78cf4b1a0e  D2：同拍 End 优先于进入 Dormant
6618d4d147d6ebbe634e61facddf2c9a0b996982  D4：有效支撑恢复时清零连续 far 计数
```

上述三项是 Owner 已确认并已提交的当前输入，不在本 Run 中重复走修改确认。

## 2. 默认实例参数

以锁定提交中 `WallAssembler.params()` 为准，主要默认值包括：

```yaml
parameter_set_id: wall-default
qt_freq: 1d
qt_n: 30
qt_quantile: 0.997
w_depth_ref_ticks: 1200
large_quote_ratio_min: 1.0
allow_zero_qt_fallback: false
thick_vs_hi_ratio: 1.0
thin_vs_mid_ratio: 0.7
allow_thin_brick: false
p_wall_ticks: 1
t_wall_ticks: 6
allow_brick_join_dormant: true
thin_contact_min_hits: 3
thin_contact_frac_end: 0.6
```

其他派生参数保持 `None`，由 `make_wall_params(...)` 按当前正式实现推导。不得把前次 C1/C2 标定试验参数当成本轮正式实例。

运行前保存 `feature.ppdict`／等价序列化参数和 `inspect.getfile(WallAssembler)`，证明加载的是上述提交和默认实例。

## 3. Owner 锁定的正式运行范围

```yaml
sof_name: TA_updto20240229_DBA
symbols: [rb, m]
requested_start_time: 2021-01-01
requested_end_time: 2021-12-31
sides: [bid, ask]
sampling: current formal tick input used by WallAssembler
calendar: night_end_at_2300
workspace: /dwdhome/fy/BASE_E6_2
scope_change_policy: OWNER_CONFIRMATION_REQUIRED
```

这不是候选范围。AI 不得自行换品种、扩缩正式年份、换输入尺度或换工作区。可在该范围内用少量位置／短窗口做诊断，正式结果必须覆盖 2021 全年。

## 4. 当前已知输入处理

前次运行曾对 m 的 17 条全空占位行作具名处理。新 Run 先从正式入口核实：

- 当前修正版是否仍遇到同类占位；
- 处理是否只移除全空占位；
- 对 rb/m 有效行情是否逐值不变。

若需要改变正式数据处理方式，先形成 `ModificationProposal`，经 Owner 确认后采用；不能无痕继承或自行换一种处理。

## 5. 既有理解复用

正式起点：

```text
task-inputs/eaw-p1-integrated/feature-understanding-result/WALL_FEATURE_UNDERSTANDING_PACKAGE.md
```

执行 AI：

- 直接复用未受影响内容；
- 只核对 D1 对事件位置／载荷、D2 对同拍状态仲裁、D4 对 far 计数与支撑语义造成的差异；
- 补本轮统计确实需要而旧包缺少的最小事实；
- 记录 delta 或更新受影响部分。

Owner 不需要另行整理上一轮理解材料，也不要求先重写完整 Package。

## 6. 已有结果与重跑规则

前次默认实例结果目录线索来自归档 Chat：

```text
/dwdhome/fy/BASE_E6_2/.runtime/wall-rb-m-20210101-20211231-20261120/
```

但默认旧结果不能自动冒充最终修复版本结果。启动时：

1. 查找是否已有绑定 `6618d4d...`、默认参数、rb/m、2021 全年、同日历的最终结果；
2. 只有代码指纹、参数、数据范围、输入处理、结果目录、SHA 和独立读回全部一致时才可复用；
3. 不满足时用锁定提交重新运行 `WallAssembler`；
4. 无论复用还是新跑，都必须对最终修正版重新做本轮完整统计。

## 7. Owner 锁定的统计与分析问题

本轮首先回答：

1. 从输入到 WALL 输出有哪些真正业务对象／业务概念，各自围绕哪些属性判断；
2. 上下游业务对象怎样处理，包含什么时序逻辑，并对应哪些 Feature、Event、occurrence 和字段；
3. 每个业务对象发生多少次，与上游对象的次数、转化和发生位置相比是否异常；
4. bid / ask 分开统计；
5. 在最终版本上复验 D1、D2、D4，并重新量化 D3；
6. 继续寻找新的明显合理性问题；
7. 所有正式表格行说明计数单位、分母和业务含义。

最少覆盖：一档观测／上游资格／墙砖／Wall identity 转化、Start/BandUpdate/StateChange/End、event 与 trace 自洽、Dormant、结束原因、同位置反复新建、寿命与短命分布。

## 8. 新 finding 与修改确认

每个新 finding 先独立定位现象、业务冲突、相关逻辑、参数／常量和最早责任阶段。若建议改变正式代码、参数、配置、规则、数据处理或输出合同：

```text
形成 ModificationProposal 和验证方案
→ 回 Owner 确认
→ 确认后才实施并采用
→ 完整重跑和重统计
```

未确认的候选 patch 可用于隔离诊断，但不得提交、推送或登记为本 Run 正式版本。

## 9. 来源索引

```text
设计／用例入口：task-inputs/eaw-p1-integrated/README.md
已有理解包：task-inputs/eaw-p1-integrated/feature-understanding-result/WALL_FEATURE_UNDERSTANDING_PACKAGE.md
原统计过程：ai_chat/根据统计找不合理点/WALL 特征：统计线闭环.md
修复过程：ai_chat/根据统计找不合理点/wall特征，修frp代码.md
当前 producer：daowei2026/tis@6618d4d...:hf/prel0/wall_assembler.py
当前 core：daowei2026/tis@6618d4d...:hf/prel0/wall_assembler_core.py
```

## 10. 运行配置

```yaml
execution_profile: CODEX_NATIVE_DIRECT
run_id: ASSIGN_AT_REAL_GO
workspace: /dwdhome/fy/BASE_E6_2
manager: fresh Codex thread for this run
executor: fresh Codex thread for this run
workers: []
```
