# B｜PostTurnGroupDirectionalOrganizationFrp 观察位置准备

## 0. 产物身份与结论

| 项目 | 值 |
|---|---|
| run_id | `OI-U2-Q-OBS-20261120-01` |
| work_item_id | `OI-U2-Q-OBS-20261120-01-WI-B` |
| stage_instance_id | `OI-U2-Q-OBS-20261120-01-M-B` |
| delegation_id | `D002` |
| 执行身份 | `chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1` |
| 特征 | `PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织） |
| 位置用法 | **普通默认** |
| 阶段状态 | **完整** |
| Worker | **不需要；未签发** |

同源机读产物已先发布：

`daowei2026/observe-iterate@1214b9580f9a8b455d5df7524335e614058f2a69:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.json`

本阶段只决定最终 CAEGraph 可绑定的品种与日期位置；不重新选择 SOF，不从 A 的 occurrence 中挑选“典型样例”，不设计图层、图元、布局或样式，也不运行 Q。

---

## 1. 采用的 B Skill 合同

- Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/SKILL.md`
- 当前用法：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/WORKFLOW.md`
- 字段级 I/O：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/IO_SPEC.md`
- 高频参考：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/MULTISCALE_POSITION_REFERENCE.md`

B 当前只有两种经验性用法：普通特征的默认位置，以及已有 `1d→30m→1m→5s→tick` 节点层级的高频多尺度位置。不得为普通场景另造复杂典型案例选择算法。

---

## 2. 输入核对

### 2.1 外层实例

| 字段 | 当前实例 |
|---|---|
| SOF | `TA_updto20240229_DBA` |
| 逻辑板块 | `steel` |
| Calendar | `night_end_at_2300` |
| 频率 | `5m` |
| 实际对象 | `rb / hc / i` |
| 方向 | `up` |
| 目标对象 | `make_features(...)` 返回值中的第二项 `q` |
| 必要上游 | 准确的 F，仅用于构造和运行 Q |

准确实例来源：

- `daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md`
- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`

### 2.2 A 当前有效产物

- 人读：`daowei2026/observe-iterate@bf50bbe5c9447cb992af547e3f5f95f7465cae88:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`
- 机读：`daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

A 已明确：Q 的业务主输出是 `DirectionalOccurrence` 与显式生命周期收口 `DirectionalDutyEnd`；Q publication firing、`directionalKnown`、成员 Turn 的 actual／confirmation／known、endpoint 与 Calendar 位置不能混同。

B 沿用这些位置区分，但不从中预选某一个 occurrence 或业务发生点。

### 2.3 任务是否明确指定位置

唯一 Q 业务输入明确写明：

```text
B 额外位置输入：无
```

因此不存在需要优先覆盖默认值的任务指定品种、时间范围或样例位置。

---

## 3. 为什么采用“普通默认”

1. 当前 Q 是固定 `5m` K 线实例。
2. 本次输入没有 `timespans.csv`、`node_id / parent_node_id` 或 `overview→big→mid→small→tick` 路径。
3. 高频参考只适用于已具备 `1d→30m→1m→5s→tick` 父子位置层级的高频特征；不能因为 Q 使用 `5m` 数据，就虚构一条不存在的高频多尺度路径。
4. 对普通场景，B Skill 要求在任务未另行指定位置时直接使用当前默认值。

因此：

```text
位置用法 = 普通默认
```

`MULTISCALE_POSITION_REFERENCE.md` 已完整核对，但本实例不应用其中的高频父子路径。

---

## 4. B 阶段最终位置

| 字段 | 最终值 | 来源／解释 |
|---|---|---|
| SOF 引用 | `TA_updto20240229_DBA`，由当前 Q 实例原件绑定 | B 沿用，不修改 |
| 逻辑品种集 | `steel` | B Skill 普通默认；与实例板块一致 |
| 实际可绑定对象 | `rb / hc / i` | 当前 Q 实例已经固定；B 不扩展对象集合 |
| Calendar | `night_end_at_2300` | 当前实例绑定 |
| 频率 | `5m` | 当前实例绑定 |
| 开始日期 | `2021-01-01` | B Skill 普通默认 |
| 结束日期 | `2022-12-31` | B Skill 普通默认 |
| 位置来源 | 当前经验性默认 | 不是最优样例选择算法 |

### 4.1 `steel` 与 `rb/hc/i` 的边界

`steel` 是 SOF／板块层面的逻辑品种集；当前 Q 实例的实际对象集合已经固定为 `rb、hc、i`。D 应在 `steel` 上下文中绑定这三个对象，不得把 B 默认理解为授权扩展到其他钢铁品种。

### 4.2 日期边界

B 只给出日期范围：

```text
2021-01-01 ～ 2022-12-31
```

日期的日历切片、包含／排除边界以及 PlotSet 绑定由 D 在 `night_end_at_2300` 下确定。B 不为此修改 SOF 的 `startDay/endDay`；当前实例原件仍保持二者为 `null`。

---

## 5. 可用性核对

完整配置声明当前三品种 5m 行情范围为：

```text
2013-01-04 09:05:00 ～ 2024-02-29 15:00:00
```

因此 B 默认的 `2021-01-01～2022-12-31` 位于来源声明范围内。

本项仅是来源配置核对，不是运行时读取证明。B Skill 不要求访问 Linux 或读取行情；实际数据存在性和最终绘图可用性由 D/E 在同一实例上继续核对。

---

## 6. 给 D 的直接绑定合同

D 可以直接消费以下位置：

```yaml
position_usage: 普通默认
sof_name: TA_updto20240229_DBA
block: steel
calendar: night_end_at_2300
frequency: 5m
objects:
  - rb
  - hc
  - i
start_date: 2021-01-01
end_date: 2022-12-31
```

同时必须保持：

- 日期窗口只是 CAEGraph 外层观察范围，不是某个 Q occurrence 的业务发生位置；
- Q occurrence 的 publication、known、成员 Turn、endpoint 和 duty end 位置继续依 A 产物解释；
- 不在 B 阶段预选 occurrence；
- 不继承 F 的观察位置产物或现有 uplot 例外。

---

## 7. 明确没有做的事

- 没有重新选择或修改 SOF；
- 没有运行 F、Q 或 V；
- 没有从历史输出挑选“典型日期”；
- 没有创建高频多尺度位置节点；
- 没有决定 CAEGraph 主图、附图、图元、布局或样式；
- 没有把高频参考脚本的绘图器、图层或展示合并逻辑搬入 B；
- 没有把 F 的阶段成果计入 Q。

---

## 8. Worker 判断

**不需要 Worker，未签发工单。**

理由：本阶段只需读取明确实例和 B Skill 的经验性默认值，形成可供 D 绑定的位置合同；不需要 Linux 文件操作、行情读取、特征运行或代码修改。

---

## 9. 完成判断

| 完成条件 | 判断 |
|---|---|
| 采用任务明确位置或当前普通默认位置 | 已采用普通默认 |
| SOF 可追溯且未被修改 | 是 |
| 品种集可追溯 | `steel`，实际对象 `rb/hc/i` |
| 开始、结束日期明确 | `2021-01-01～2022-12-31` |
| 可供 D 直接绑定 | 是 |
| 未把图内容误当成位置方法 | 是 |
| 阻塞缺口 | 无 |

**B 阶段状态：完整。**
