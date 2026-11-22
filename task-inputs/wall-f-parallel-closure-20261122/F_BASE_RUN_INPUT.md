# F 基础 Feature Run 输入

> 状态：Owner 已锁定 U2/U3 用例、目标 F、钢铁板块、5m、2021—2023 范围和工作区；等待 Owner 提供并锁定新的参数实例及其准确代码／配置版本。

## 1. 目标 Feature 与用例

```yaml
feature_name: CommonPriceTurnGroupCandidatesFrp
business_name: F｜共同价格转折候选组
use_case_ref: task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md
base_instance_sources:
  - task-inputs/u2-fqv-observation/实例运行脚本.py
  - task-inputs/u2-fqv-observation/无二义性需求和实现文件.md
  - U2/U3 fqv-kline-rb-hc-i complete configuration
instance_selection: make_features(...) returned object f only
frp_repository: daowei2026/frp
frp_commit: PENDING_OWNER_NEW_PARAMETER_VERSION
TIS_constructor_ref: RESOLVE_FROM_OWNER_LOCKED_NEW_INSTANCE_AND_U2_U3_ENTRY
parameter_instance_ref: PENDING_OWNER_NEW_PARAMETER_INSTANCE
parameter_instance_sha256: PENDING_OWNER
parameter_change_policy: USE_ONLY_OWNER_PROVIDED_OVERRIDE; DO_NOT_TUNE_FURTHER_WITHOUT_OWNER_CONFIRMATION
```

旧 F 输入用于锁定用例、对象和构造关系。旧 commit／旧参数只作基线，不冒充 Owner 即将提供的新实例。

## 2. Owner 锁定的正式运行范围

```yaml
symbols: [rb, hc, i]
sampling: 5m
start_time: 2021-01-01
end_time: 2023-12-31
calendar: USE_THE_CALENDAR_FROM_THE_LOCKED_U2_U3_INSTANCE; NO_SUBSTITUTION
workspace: /dwdhome/fy/BASE_E6_2_copy
scope_change_policy: OWNER_CONFIRMATION_REQUIRED
```

该范围来自 Owner 原始 prompt，不是候选。实际首末交易日可以受锁定交易日历影响，但 AI 不得据此改写正式请求范围、缩短年份、换品种或换尺度。可在范围内用局部位置做诊断，正式结果仍须覆盖全范围。

## 3. 新参数实例的采用边界

Owner 提供的新实例至少应能核对：

- Δ 的准确字段和值；
- 迟到／首次准入期限的准确字段或派生方式；
- 观察关闭、修订终点等相关期限；
- 哪些原硬编码常量已参数化；
- 构造入口实际加载了该实例；
- 与旧实例的准确差异。

本 Run 把 Owner 锁定的新实例作为正式输入，不重复把“为什么最终选这个值”设为必做标定任务。AI 可以分析其效果和提出后续修改方案，但不得自行采用另一组参数、继续放大倍数或改相关规则；任何新改变先回 Owner 确认。

## 4. 既有理解复用

起点包括：

- `F特征：统计线闭环.md` 中已经形成的业务对象、属性层次、处理和时间逻辑；
- U2/U3 原实例、需求与实现索引；
- 旧实例运行结果；
- 当前新参数版本的源码和配置差异。

执行 AI 只核对／补齐本轮变化相关的最小事实，重点是参数消费、actual／confirm／selected／create／revision 时间、材料准入、观察关闭和修订责任。Owner 不需要先整理上一轮 FeatureUnderstanding，也不要求先新写一份完整 Package。

## 5. X｜正式运行

必须用 Owner 锁定的新参数实例，在上述正式范围完整运行 F。旧实例结果只作对照，不能冒充新实例结果。Q、V 不属于本基础 Run 的专业产物。

## 6. Owner 锁定的统计与分析问题

本轮首先回答：

1. 从输入贴近转折到候选组有哪些真正业务对象／业务概念，各自属性如何按业务处理组织；
2. 上下游对象的处理、时序逻辑和正式 Feature／Event／occurrence／字段映射；
3. 每个品种原有多少贴近转折，经过各层资格／关系／期限后形成多少候选组和候选组 occurrence；
4. 比较上游对象与下游对象的次数、转化、发生位置和首次阻断；
5. 区分 actual、confirm、selected、group create、revision 等时间，比较实际转折间隔与实际转折到确认的等待，并解释 Δ 及期限倍数在本实例中的作用；
6. 说明新参数让哪些原被期限挡住的对象重新进入，新增对象是否仍符合共同转折的业务条件；
7. 继续寻找新的明显合理性问题，而不是只确认“候选组数量变多”；
8. 所有正式表格行说明计数单位、分母和业务含义。

AI 可以增加为回答这些问题真正需要的分层或统计，不要求机械执行一张固定指标大全。局部案例用于理解和区分原因，不能替代整体转化比例和全量结果。

## 7. 当前判断边界

以下都不能单独证明 F 已合理：

- 候选组从约十次变多；
- 某一个迟到案例通过；
- 覆盖某个延迟分位数；
- 新参数没有运行报错。

需要回到整体候选比例、目标业务对象、上游转化、发生位置、对象身份、时间责任和新 finding 判断。当前不要求 AI自行重新设计最终参数理论。

## 8. 新 finding 与修改确认

若分析后建议继续修改参数、硬编码常量、期限关系、正式代码、数据处理或输出合同：

```text
形成 ModificationProposal、影响范围和验证方案
→ 回 Owner 确认
→ 确认后才实施和采用
→ 完整重跑和重统计
```

未确认的敏感性实验或候选配置只能作为诊断材料，不得登记为本 Run 正式实例。

## 9. 运行配置

```yaml
execution_profile: CODEX_NATIVE_DIRECT
run_id: ASSIGN_AT_REAL_GO
workspace: /dwdhome/fy/BASE_E6_2_copy
manager: new Codex thread
executor: new Codex thread
workers: []
```
