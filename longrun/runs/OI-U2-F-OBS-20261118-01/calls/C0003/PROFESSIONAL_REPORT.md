# C0003｜D001 A Skill 专业回交

## 1. 调用与回交身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0003`
- `delegation_id`：`D001`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-A`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-A`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 正式委派：`daowei2026/observe-iterate@d1ef9eda82e6dd536959fde76e445d635430ded9:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D001/DELEGATION.json`

## 2. 实际采用的 Skill 与输入

亲自完整采用：

- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md`
- 同一提交同目录 `WORKFLOW.md`、`IO_SPEC.md`
- 唯一业务输入 `task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md`
- D001 列明的实例脚本、索引、TIS 构造、完整 JSON 配置、FRP 主实现及 Python 读取接口。

采用的唯一特征实例为：

```text
make_features(...) 返回的第一项 f
类型：CommonPriceTurnGroupCandidatesFrp
SOF：TA_updto20240229_DBA
对象域：steel
对象：rb / hc / i
Calendar：night_end_at_2300
尺度：5m
```

没有把 Q/V 扩入分析；没有运行特征；没有使用或签发 Worker。

## 3. 实际专业产物

完整 A 阶段产物：

`daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md`

产物按 A1～A7 形成了：

1. 当前实现来源记录；
2. 输入事件级 occurrence 记录；
3. 业务主输出与中间处理事件／结果记录；
4. 每类 occurrence 自身发生位置和携带位置总表；
5. 形成、更新、关闭、引用和修订关系；
6. 业务主输出向上追溯与输入事件去向；
7. 当前公开读取接口、明确缺口和后继使用边界。

## 4. 主要专业结论

### 4.1 业务主输出

F 的业务主输出是：

> 某个共同价格转折候选 Life 的一次新 revision。

对外载体是：

```haskell
FrpEvent (Tick [GroupCandidatesRecord])
```

一次 publication Event 可携带多个候选 revision。`occurrences_groupMembers`、Required Pair、previous、overlap 和 covered-by 都是候选 revision 的嵌套正文／形成证据，不是独立 F 业务事件；Python DataFrame 只是公开读取视图。

### 4.2 输入与中间形成链

当前正常 `from_kline` 实例实际消费：

- 各对象 5m KLine 的 `close + closeUti` occurrence；
- `ScaleTurnCalendar` 第一轮和第二轮 `CompleteScaleTurn` occurrence；
- `falter` 的 `ZigWithStatusOcc`，用于给 actual 位置补方向和 Peak/Trough 类型。

形成链为：

```text
KLine / ScaleTurn / Zig
→ FormationFrame
→ FormationMaterial
→ PairView
→ CandidateOccurrence revision
→ GroupCandidatesRecord publication
```

### 4.3 occurrence 位置

候选 revision 自己的正式业务可知／发表位置是：

```text
candidateKnown → groupKnownFrom
```

候选没有一个可替代所有成员的“实际转折位置”。其正文携带每个成员各自的：

```text
actual
confirmation
known
Clock
selected P/T/C
```

同时携带候选形成问题的 anchor/deadline/revisionEnd Calendar clock 窗口。成员 actual、成员 confirmation、候选 known 和外层 `Tick.ts` 不得混同。

### 4.4 身份和更新

- Candidate Life 由稳定 `CandidateKey=(FormationQuestion,[TurnKey])` 维持；`TurnKey=(object, turn Life)`。
- 候选正文或正式决定含义变化时，新建 Revision，并由 `previous` 指向前一 exact。
- 新 occurrence 可以表达形成、状态更新、关闭、withdrawn 或 subsumed；这些是同一候选 revision 正文的变化，不是各自独立 Event 家族。
- 非首次候选批次为空时，正式 F Event 不发生；无 Event 不表示失败、撤回或结束。

### 4.5 当前实例边界

本实例走 `GroupKLineConfiguration/from_kline`，不是旧 `NativeSourcePlan` 产品前置。当前正常路径：

- `framePatches=[]`；
- `frameEnded=False`；
- `memberRetracted=False`；
- 不发行 `GroupCoverageCorrection`。

源码中兼容的 stored-source、修订和 scope-end 能力没有被写成本实例已经发生的事实。

## 5. A Skill 完成条件核对

| 完成条件 | 结果 |
|---|---|
| 输入、输出和中间处理按业务角色区分 | 已满足 |
| 每类事件自身发生位置与 occurrence 内携带位置已说明 | 已满足 |
| 业务主输出与中间结果的形成／更新关系可追溯到代码 | 已满足 |
| 未因公开保存或 DataFrame 拆表把中间结果误判为主输出 | 已满足 |

A 阶段专业状态：**完整**。

## 6. 明确限制与未确认项

存在两项非阻塞边界：

1. F 合同未声明外层 `Tick.ts` 与 `groupKnownFrom` 在所有平台运行中完全同义；后继应使用显式业务字段 `groupKnownFrom`。
2. Haskell 已存 `groupFormationParticipation`，但当前 TIS `GROUP_TABLES` 未暴露该嵌套字段。若后继展示要求完整 admission/support-correction/alternative 细节，应记录为读取接口缺口，不能用其他字段猜测。

它们不妨碍 B/C/D 使用核心候选 occurrence、成员、Required Pair、状态和 revision 链。

## 7. Worker、剩余工作与接续

- 本 C 零 Worker；没有签发 W，也没有接受 Worker Return。
- D001／A Skill 内没有仍未满足的专业工作。
- 不需要接续原 D001。
- B、C、D、E 是父 Run 后继，未在本调用执行；应由原 manager 按既定 Workflow 和本 A 产物安排。
- Q/V、合理性分析和全历史 producer 重跑仍明确不在本 Run 当前范围。
