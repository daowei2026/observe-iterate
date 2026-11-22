# WALL 基础 Feature Run 输入

> 状态：等待 Owner 补远端版本和工作区。

## 1. 目标 Feature

```yaml
business_name: WALL
feature_type_or_entry: PENDING_OWNER
code_repository: daowei2026/tis
code_commit: PENDING_OWNER_FULL_40_CHAR_COMMIT
constructor_or_execution_entry: PENDING_OWNER
parameter_instance_ref: PENDING_OWNER
```

修复 Chat 中出现的本地短提交和分支仅作为追溯线索，不作为新 Run 版本锁。正式运行只接受 Owner 提供的远端完整 commit。

## 2. 候选数据范围

沿前次统计用例，建议作为新 Run 默认候选：

```yaml
symbols: [rb, m]
start_time: 2021-01-01
end_time: 2021-12-31
sides: [bid, ask]
sampling: 0.5s market ticks / current formal input
calendar: PENDING_OWNER_EXACT_REF
```

Owner GO 可调整；调整后必须同步更新统计可比性和已知 finding 的复验范围。

## 3. 当前已知输入处理

前次运行曾对 m 的全空占位行作具名处理。新 Run 必须从当前正式入口核实：

- 是否仍存在；
- 处理发生在哪一层；
- 是否只移除全空占位；
- 对 rb/m 有效行情是否逐值不变。

不能无依据继承旧 Chat 的数据处理结论。

## 4. U 复用边界

可以复用旧 WALL 业务对象理解作为起点，但必须核对最终修正版是否改变：

- Wall 身份；
- 状态转换；
- 位置事件发布；
- far 计数；
- 支撑语义；
- 运行结果字段。

只更新受影响部分，不重做无变化内容。

## 5. X

优先级：

1. 若 Owner 提供的最终修正版完整结果包与本轮范围完全一致，验证版本、参数、数据、SHA 和读回后可正式复用；
2. 否则用最终远端 commit 重新运行。

无论 X 是新跑还是复用，G 都必须对最终修正版重新完整执行。

## 6. G 最少覆盖

由 `FeatureUnderstandingPackage` 决定实际字段，至少核：

- 一档观测／上游资格／墙砖／Wall 身份的转化；
- bid/ask 方向；
- Start、BandUpdate、StateChange、End 和同拍 occurrence；
- event 与 trace 正式输出自洽；
- Dormant 持续、恢复和结束；
- far、thin、timeout 等结束原因；
- 同位置反复新建；
- 寿命、单砖、短命和重建分布；
- D1、D2、D4 在最终版本上是否归零或符合新合同；
- D3 的最新影响范围。

这些是本次 WALL 任务输入，不是通用 Skill 的固定指标。

## 7. 运行配置

```yaml
execution_profile: CODEX_NATIVE_DIRECT
run_id: PENDING_OWNER
workspace: PENDING_OWNER_ABSOLUTE_LINUX_PATH
manager: new Codex thread
executor: new Codex thread
workers: []
```
