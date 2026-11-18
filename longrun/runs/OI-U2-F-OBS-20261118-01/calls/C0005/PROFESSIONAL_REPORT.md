# C0005｜D002 B Skill 专业回交

## 1. 调用与回交身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0005`
- `delegation_id`：`D002`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-B`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-B`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 正式委派：`daowei2026/observe-iterate@b543f4b91482716577ebc0b59f786b5ab45aba61:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D002/DELEGATION.json`

## 2. 实际采用的 Skill 与输入

本次亲自读取并采用：

- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/observation-position-preparation/SKILL.md`
- 同一提交同目录 `WORKFLOW.md`、`IO_SPEC.md`、`MULTISCALE_POSITION_REFERENCE.md`
- 唯一业务输入 `task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- D002 所列实例脚本、正常 `make_features(...)` 构造、完整展开配置与 A 当前有效原生产物。

被观察对象保持为：

```text
make_features(...) 返回的第一项 f
类型：CommonPriceTurnGroupCandidatesFrp
SOF：TA_updto20240229_DBA
板块／domain：steel / blk@steel
对象：rb / hc / i
日历：night_end_at_2300
源尺度：5m
```

未处理 Q/V，未进入 C/D/E，未运行或重跑特征。

## 3. 实际专业产物

B 阶段原生产物：

`daowei2026/observe-iterate@6f1ee9eb4595254845d3b228a146ad68cabc64e0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md`

该产物形成了 D 可直接消费的单一位置记录 `OI-U2-F-OBS-20261118-01-B-POS-001`，并记录适用分支、位置字段、来源、边界和排除项。

## 4. 专业判断与位置结果

### 4.1 位置用法

采用：

```text
普通默认
```

不采用高频 `1d → 30m → 1m → 5s → tick` 路径。

理由是当前输入没有指定高频多尺度位置，也没有提供 `overview → big → mid → small → tick` 的节点身份、父子关系和时间窗；当前 F 只是以固定 5m KLine/ScaleTurn/Zig 形成候选组，分钟级源频率不自动构成 B Skill 的高频多尺度位置用法。B 不得据此虚构 1m、5s 或 tick 子位置。

### 4.2 D 可绑定位置

| 字段 | 值 |
|---|---|
| SOF | `TA_updto20240229_DBA` |
| 板块／domain | `steel / blk@steel` |
| 实际品种集 | `rb / hc / i` |
| 日历 | `night_end_at_2300` |
| 特征源尺度 | `5m` |
| 开始日期 | `2021-01-01` |
| 结束日期 | `2022-12-31` |
| F 主 occurrence 位置 | `groupKnownFrom` |
| 高频多尺度路径 | 不适用 |

“钢铁板块”作为当前默认品种语境由实例的 `steel` 绑定满足；实际 F 只构造了 `rb/hc/i`，所以不能把其他钢铁品种扩入本次观察对象。

完整配置记载三品种原始 5m 行情约覆盖 `2013-01-04 09:05:00` 至 `2024-02-29 15:00:00`，当前默认日期范围处于其覆盖范围内。B 不处理原始缺价，也不核实 F 正式输出是否已落盘。

### 4.3 与 A 的位置对齐

A 已确定候选 revision 自己的业务可知／发表位置是：

```text
candidateKnown → groupKnownFrom
```

因此观察范围内的 F 主 occurrence 应按 `groupKnownFrom` 对齐。成员 `actual / confirmation / known` 与候选窗口属于正文携带位置，不替代候选自身位置；外层 `Tick.ts` 也不能无条件替代 `groupKnownFrom`。

开始／结束端点在 `night_end_at_2300` 日历和 PlotSet 中的边界解释留给 D 的绑定，不由 B 另设。

## 5. B Skill 完成条件核对

| 原生完成条件 | 结果 |
|---|---|
| 普通场景采用任务明确位置或当前默认位置 | 已采用当前默认位置 |
| SOF、品种和时间可追溯 | 已满足 |
| 位置可供 D 绑定 | 已形成结构化位置记录和绑定表 |
| 未把高频脚本的图内容当作位置方法 | 已满足；高频路径判定为不适用 |
| 未决定图形布局和图元 | 已满足 |

B 阶段专业状态：**完整**。

## 6. Worker、缺口与接续

- 本 C 零 Worker；没有签发 W，也没有接受 Worker Return。
- D002／B Skill 内不存在仍未满足的专业工作。
- 不需要接续原 D002。
- 当前经验性默认位置不声称最优，也不是 occurrence 搜索得到的“典型位置”；这是 Skill 明确规定的当前用法边界。
- C、D、E 均未在本调用执行，应由原 manager 消费本次真实回交后沿既定 Workflow 推进。
- Q/V、合理性分析、历史成果预接受和输入排除的全历史 producer 重跑仍不在范围。
