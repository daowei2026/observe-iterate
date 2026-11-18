# B｜CommonPriceTurnGroupCandidatesFrp 观察位置准备

## 0. 产物身份与阶段结论

| 项目 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-B` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-B` |
| `delegation_id` | `D002` |
| 执行调用 | `C0005` |
| 特征 | `CommonPriceTurnGroupCandidatesFrp`（F｜共同价格转折候选组） |
| 被观察实例 | `make_features(...)` 返回的第一项 `f` |
| B 位置用法 | **普通默认** |
| B 阶段状态 | **完整** |

本阶段只给出后续 D 可绑定的观察品种与时间位置，不选择 SOF、不挑选“典型 occurrence”、不设计主图／附图／图元，也不运行特征。

## 1. 适用分支判断

本次采用 B Skill 的“普通特征经验性默认位置”，不采用高频 `1d → 30m → 1m → 5s → tick` 多尺度位置路径。

判断依据：

1. 唯一业务输入没有额外指定 B 的品种、时间或样例位置；因此不存在“任务明确指定”位置可优先采用。
2. 当前 F 实例是固定 `5m` KLine、ScaleTurn 与 Zig 输入形成的共同价格转折候选组；当前任务没有把它指定为需要既有高频多尺度路径的特征。
3. 高频参考路径要求已有 `overview → big → mid → small → tick` 的节点身份、父子关系和各层时间窗。本次实例与输入没有提供这套位置节点，也没有要求从 1d 概览逐层下钻。
4. 输入频率为 `5m` 并不自动等于 B Skill 所定义的高频多尺度位置用法；不得因为出现分钟级 KLine 就虚构 `1m/5s/tick` 子位置。

因此，本次按普通默认值形成一个可直接绑定的观察位置。

## 2. 实际观察位置

### 2.1 结构化位置记录

```yaml
position_id: OI-U2-F-OBS-20261118-01-B-POS-001
position_usage: ordinary_default
feature:
  name: CommonPriceTurnGroupCandidatesFrp
  selected_return: f
  source_frequency: 5m
sof:
  name: TA_updto20240229_DBA
  policy: inherit_from_feature_instance
universe:
  block_context: steel
  symbols:
    - rb
    - hc
    - i
calendar:
  name: night_end_at_2300
observation_range:
  start_date: 2021-01-01
  end_date: 2022-12-31
  boundary_interpretation: deferred_to_D_calendar_or_PlotSet_binding
primary_occurrence_position:
  field: groupKnownFrom
  meaning: candidate_revision_business_known_or_publication_position
position_source: B_Skill_current_ordinary_default
high_frequency_multiscale_path: not_applicable
```

### 2.2 SOF

沿用外层特征实例已经绑定的：

```text
TA_updto20240229_DBA
```

B 不修改、不替换，也不重新选择 SOF。

### 2.3 品种集

当前经验性默认是钢铁板块；本实例已经把钢铁语境具体绑定为：

```text
block / domain：steel / blk@steel
实际 F 对象：rb、hc、i
```

因此本次 D 可绑定的实际品种集为：

```text
{rb, hc, i}
```

“钢铁板块”在这里是实例的板块／domain 语境，不能据此把未进入本次 `f` 构造的其他钢铁品种扩入观察对象。

### 2.4 时间范围

采用普通位置的当前默认值：

```text
开始：2021-01-01
结束：2022-12-31
```

完整配置说明当前三品种 5m 行情索引约覆盖 `2013-01-04 09:05:00` 至 `2024-02-29 15:00:00`，因此上述默认范围处于实例原始行情覆盖范围内。原始缺价仍保持缺价；B 不对缺价进行填补、筛除或重跑。

开始／结束边界在交易日历及 PlotSet 中究竟按闭区间、开区间或端点时间怎样解释，由 D 按 `night_end_at_2300` 日历和锁定 CAEGraph 绑定处理；B 不另造边界规则。

## 3. 与 A occurrence 位置的对齐

A 已确认 F 的业务主 occurrence 是候选 Life 的一次新 revision。对当前观察范围进行候选 occurrence 绑定时，使用显式业务位置：

```text
candidateKnown → groupKnownFrom
```

因此：

- `groupKnownFrom` 是候选 revision 自己的业务可知／发表位置；
- 成员各自的 `actual`、`confirmation`、`known` 是 occurrence 正文携带的位置，不替代候选自己的 B 观察位置；
- `groupOriginalAnchor / Deadline / RevisionEnd` 及收紧后的 Calendar clock 窗口属于候选形成问题正文，不是本 B 另选的观察时间窗；
- 外层 `Tick.ts` 未被当前特征合同声明为在所有平台中与 `groupKnownFrom` 完全同义，后继不能用它无条件替代显式字段。

B 只固定整体观察范围，不在这个范围内进一步预选某一条候选 Life、revision 或发生日期。

## 4. 方法和来源追溯

### 4.1 B Skill 来源

- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/SKILL.md`
- 同提交同目录 `WORKFLOW.md`、`IO_SPEC.md`、`MULTISCALE_POSITION_REFERENCE.md`

### 4.2 实例来源

- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`

### 4.3 A 阶段来源

- `daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`

## 5. D 可直接消费的绑定结论

D 应以以下单一 B 位置产物作为位置输入：

| 字段 | 绑定值 |
|---|---|
| SOF | `TA_updto20240229_DBA` |
| 板块／domain | `steel / blk@steel` |
| 品种 | `rb / hc / i` |
| 日历 | `night_end_at_2300` |
| 特征源尺度 | `5m` |
| 开始日期 | `2021-01-01` |
| 结束日期 | `2022-12-31` |
| F 主 occurrence 的位置字段 | `groupKnownFrom` |
| 位置用法 | `普通默认` |
| 高频多尺度父子路径 | 不适用 |

D 不应从本 B 产物推导：

- 新 SOF；
- 其他钢铁品种；
- `1m / 5s / tick` 子节点；
- 预选 occurrence 或“典型案例”；
- 图层、绘图器、颜色、布局或主附图关系。

## 6. 缺口与限制

1. 当前位置是 B Skill 明确规定的经验性默认，不声称最优，也不是从 F occurrence 中搜索出的典型案例。
2. B 不验证 2021～2022 期间最终 F 输出是否已经落盘，也不运行或重跑 producer；这属于后续 D/E 的实际绑定与执行范围。
3. B 不改变原始行情缺价，不新增数据筛选。
4. 当前不存在高频多尺度位置节点缺失问题，因为该位置用法对本实例不适用。
5. A 提到的 `groupFormationParticipation` Python 读取接口缺口不影响品种和时间位置的确定。

## 7. 完成条件核对

| B Skill 完成条件 | 结果 |
|---|---|
| 采用任务明确位置或当前普通默认位置 | 已采用普通默认位置 |
| SOF、品种和时间可追溯 | 已分别追溯到实例与 B Skill 默认约定 |
| 形成可供 D 绑定的位置产物 | 已形成 `B-POS-001` 结构化记录与绑定表 |
| 未把高频脚本图内容误作位置方法 | 已排除；高频路径对本实例不适用 |
| 未决定图布局和图元 | 已遵守 |

本阶段状态为 **完整**。不存在需要 Worker 执行的 B 工作，也不存在原 D002 内尚未满足的专业工作。
