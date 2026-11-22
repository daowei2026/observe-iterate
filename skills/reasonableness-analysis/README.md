# 合理性分析 Skills

本目录保留 V0.2 的五项专业 Skill。V0.3 没有再增加 Feature 执行、实现修正或 Campaign Skill，而是在现有 Skill 之上增加一份轻量实践补充：

- [`STATISTICS_DRIVEN_PRACTICE.md`](STATISTICS_DRIVEN_PRACTICE.md)

采用 `control-v0.3/` 的 Run，应把该补充与实际调用的 Skill 一起锁定；它只增加统计选择、抽样、诊断和标定的通用边界，不重写各 Skill 的原生输出合同。

## 1. 共享前置

所有合理性 Skill 与观察材料准备共同消费：

- [`skills/feature-understanding/`](../feature-understanding/SKILL.md)
- 业务对象判别补充：[`BUSINESS_OBJECT_QUALIFICATION_GUIDE.md`](../feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md)
- 核心产物：`FeatureUnderstandingPackage`

共享理解负责当前实现实际维护的对象、身份、状态、事件级 occurrence、中间判断、处理关系、参数和结果字段。它不判断设计是否合理。

## 2. 现有 Skill

| 顺序 | Skill | 职责 |
|---|---|---|
| 0 | `feature-global-behavior-profiling` | 对最新运行结果做全量／分层行为统计，发现结构 finding 和需要场景解释的问题 |
| 1 | `business-expectation-derivation` | 在宽范围观察材料完成后，选择真实正／负例、误报／漏报候选、参数边界和覆盖外场景，并冻结场景预期 |
| 2 | `business-evidence-comparison` | 逐场景对照原始市场过程、预期 Feature 过程和实际 Feature 过程，定位第一次业务分歧 |
| 3 | `business-discrepancy-diagnosis` | 沿处理链查根因，做参数可修复性初筛并路由 |
| 4 | `feature-instance-calibration` | 对确有标定目标的问题求参数可行范围、试验少量候选并验证完整实例 |

## 3. 两种采用方式

### V0.2 完整场景线

```text
共享理解
→ Feature 运行
→ Skill 0 全量统计和问题闭环
→ 观察材料 B～E
→ Skill 1 选场景并冻结预期
→ Skill 2 场景对照
→ Skill 3／4 或外部接口
```

### V0.3 轻量统计闭环

```text
共享理解
→ 运行最新实例
→ Skill 0 全量统计
→ Skill 3 逐 finding 诊断
→ 实现修正／新参数实例／数据修正
→ 重跑 Feature 和 Skill 0
→ FeatureReleaseGate
```

统计不能判断真实市场过程时，再转入 V0.2 的观察材料和场景线；不为了形式完整机械画图。

## 4. 共同规则

1. Feature 行为改变后，旧运行结果、旧统计和旧图不能继续作为当前证据。
2. Skill 0 不在 `DiagnosisInputAdapter` 中提前写根因。
3. Skill 3 的局部反事实实验只用于区分原因，不等于正式标定。
4. Skill 4 不以输出数量增加或单个案例通过作为参数成功标准。
5. 已确认实现问题通过普通工程接口修正；修复后仍回到完整实例运行和全量统计。
6. 场景正式对照前，Skill 1 必须冻结案例和预期；新证据不能无痕改写旧版本。
7. `PASS_TO_SCENARIO_REVIEW` 只表示 Skill 0 当前职责结束，不等于 Feature 可以无条件释放给下游。

## 5. 具体任务与通用 Skill 的边界

通用 Skill 不固定以下内容：

- 品种、方向和年份；
- 某个 Feature 必须统计的专用字段；
- 固定抽样数量；
- 某个用例的门槛或结论；
- 某条下游依赖。

这些信息由 `FeatureUnderstandingPackage`、`CurrentReviewTarget` 和具体 `task-inputs/` 提供。实践补充只规定怎样从这些输入推导统计和证据。

## 6. 版本与历史

历史 Run 按当时锁定版本解释，不因本 README 更新而自动切换。V0.2 的原控制文件继续有效；V0.3 是面向当前统计驱动闭环的轻量采用方式。
