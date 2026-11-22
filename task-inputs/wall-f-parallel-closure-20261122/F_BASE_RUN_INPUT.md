# F 基础 Feature Run 输入

> 状态：等待 Owner 补新代码／参数实例和工作区。

## 1. 目标 Feature

```yaml
feature_name: CommonPriceTurnGroupCandidatesFrp
business_name: F｜共同价格转折候选组
frp_repository: daowei2026/frp
frp_commit: PENDING_OWNER_FULL_40_CHAR_COMMIT
tis_constructor_ref: PENDING_OWNER_FULL_40_CHAR_COMMIT_AND_PATH
parameter_instance_ref: PENDING_OWNER_PATH
parameter_instance_sha256: PENDING_OWNER
```

旧 `task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md` 可用于定位原构造关系和资料，但其旧 commit／参数不自动成为本 Run 采用版本。

## 2. 候选数据范围

沿前次统计闭环的业务范围：

```yaml
symbols: [rb, hc, i]
sampling: 5m
start_time: PENDING_OWNER_THREE_YEAR_RANGE_START
end_time: PENDING_OWNER_THREE_YEAR_RANGE_END
calendar: PENDING_OWNER_EXACT_REF
```

Owner 应给出绝对日期，不在 GO 中只写“三年”。

## 3. 新参数实例要求

Owner 提供的新实例至少能够核对：

- Δ 的准确字段和值；
- 迟到／首次准入期限的准确字段或派生方式；
- 观察关闭、修订终点等相关期限；
- 哪些常量已参数化；
- 构造入口实际加载了该实例；
- 与旧实例的差异。

本 Run 接收 Owner 选择的新实例，不重复把“为什么最终选这个值”作为必做标定任务；但结果必须按业务效果重新统计。

## 4. U 复用边界

可以复用旧 F 理解，但需核对新版本是否改变：

- 输入转折和组身份；
- actual、confirm、selected、create、revision 时间；
- 材料准入和候选生成的期限；
- 观察关闭和修订责任；
- 输出字段和公开读取接口。

## 5. X

必须用新参数实例完整运行本轮范围。旧实例结果只作对照，不能冒充新实例结果。

## 6. G 最少覆盖

实际字段由共享理解决定，至少核：

- 输入 M 尺度转折数量、actual 与 confirm／selected 延迟；
- 两两相容关系及其发生位置；
- 上游对象在每一道期限或资格门的转化与首次阻断；
- 候选组身份数、创建、更新／修订和结束；
- 品种、年份、方向及延迟区间分层；
- 新参数恢复了哪些原来被期限挡住的对象；
- 新增对象是否仍满足实际位置共同性和其他业务条件；
- 是否出现过密、重复、长期开组、修订责任冲突或新的结构 finding；
- 从上游相容关系独立寻找未成组候选。

这些是本次 F 任务输入，不是通用 Skill 固定指标。

## 7. 验收边界

以下都不能单独证明 F 已合理：

- 候选组从 10 次变多；
- 某个 610 分钟迟到案例通过；
- 覆盖某个延迟分位数；
- 新参数没有运行报错。

必须回到目标业务对象、转化结构、对象身份、时间责任和全量 finding 判断。

## 8. 运行配置

```yaml
execution_profile: CODEX_NATIVE_DIRECT
run_id: PENDING_OWNER
workspace: PENDING_OWNER_ABSOLUTE_LINUX_PATH
manager: new Codex thread
executor: new Codex thread
workers: []
```
