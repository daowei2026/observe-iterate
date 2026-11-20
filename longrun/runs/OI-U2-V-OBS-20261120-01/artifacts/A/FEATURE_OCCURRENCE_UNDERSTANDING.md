# A｜CommonTurnGroupValidityFrp 事件级 occurrence 与处理关系说明

## 0. 产物身份与阶段结论

| 项目 | 值 |
|---|---|
| `run_id` | `OI-U2-V-OBS-20261120-01` |
| `work_item_id` | `OI-U2-V-OBS-20261120-01-WI-A` |
| `stage_instance_id` | `OI-U2-V-OBS-20261120-01-M-A` |
| `delegation_id` | `D001` |
| 执行身份 | `chatgpt:OI-U2-V-OBS-20261120-01:executor:E1` |
| 特征 | `CommonTurnGroupValidityFrp`（V｜共同转折组的局部成立判断） |
| 方法 | `ClosedFormationLocalValidity` |
| 当前布局 | `common_turn_group_validity.core.v2` |
| 阶段状态 | **完整** |
| 阻塞未确认项 | **无** |
| Worker | **不需要；未签发** |

机读同源产物已先发布：

`daowei2026/observe-iterate@15ba2f067ec47b6e91132f583c2a859580e81947:longrun/runs/OI-U2-V-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

本阶段只还原 V 的真实输入 Event、业务主输出 occurrence、中间处理结果、发生位置、身份、修订、结束和处理关系。没有运行或重算 F/Q/V，没有选择观察时间，没有设计 CAEGraph，也没有把 F/Q 的历史阶段成果计作 V 的 A 阶段成果。

### 0.1 一句话结论

V 读取并组合**准确的 F 候选形成观点**、**准确的 Q 方向组织观点**及 **Q 的真实责任结束**；以 F candidate Life 为题维护当前足用状态；只有当正式 V 声明发生业务变化时，才产生具有自身 `Life / Revision / Previous` 的 `ValidityOccurrence`。Q 责任结束不是第二类 V 主输出，而是可能促成原 V Life 的一版收口修订。

### 0.2 最关键的事件边界

1. `ValidityOccurrence` 是 V 唯一的业务主输出 occurrence：一个 occurrence 是对一个 F candidate Life、一个显式方向问题的一版完整局部成立观点。
2. V 不重算 F 的两两相容、形成几何，也不重算 Q 的六类运动量；它只消费 F/Q 已正式裁定并保存的足用投影。
3. `ValidityStatement`、`ValidityMember`、`ValidityReason` 是 V occurrence 的嵌套正文或明细，不是独立 Event occurrence。
4. `ValidityInputError` 是独立工程诊断，不得伪装成 `Pending`、`Invalid` 或市场反证。
5. `GroupValidityRecord` 是正式存储 envelope；首次可以只保存 definition，没有业务 occurrence。
6. Q exact 发生变化但 V 正式声明承诺字段未变化时，不产生新 V revision；“静默”不等于失败、无效或结束。
7. V occurrence 的发表位置是触发本次声明变化的上游原 Tick；`validityKnown` 是参与事实的知识闭包，二者不能混同。

---

## 1. 特征引用与当前实例

### 1.1 当前实例

| 字段 | 值 |
|---|---|
| 数据集 | `TA_updto20240229_DBA` |
| 板块／对象域 | `steel` |
| Calendar | `night_end_at_2300` |
| 对象 | `rb / hc / i` |
| 尺度 | `5m` |
| 方向 | `DirectionUp` |
| V 方法 | `ClosedFormationLocalValidity` |
| 构造入口 | `make_features(...)` 的第三项 `v` |
| V 构造 | `CommonTurnGroupValidityFrp.from_organization(q)` |
| 必要上游 | 准确 Q；Q 又由准确 F 构造 |

F、Q 只是 V 的必要上游依赖。本产物不把 F/Q 当作本 Run 的目标特征，也不把 F/Q 的主输出或历史 A～E 产物冒充 V 当前阶段产物。

### 1.2 当前实现来源清单

| 编号 | 精确来源 | 入口／职责 | 核实状态 |
|---|---|---|---|
| `S01` | `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/SKILL.md` | A 阶段边界与完成条件 | 已核实 |
| `S02` | `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/WORKFLOW.md` | A1～A7 判断方法 | 已核实 |
| `S03` | `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/feature-occurrence-understanding/IO_SPEC.md` | 字段级输出合同 | 已核实 |
| `S04` | `daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/V_OBSERVATION_RUN_INPUT.md` | V 范围、实例选择与上游边界 | 已核实 |
| `S05` | `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py` | 实例参数、第三项 `v` 与公开读取入口 | 已核实 |
| `S06` | `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/无二义性需求和实现文件.md` | 现行 F→Q→V 索引与时间口径 | 已核实 |
| `S07` | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py` | `make_features` 与 F→Q→V 接线 | 已核实 |
| `S08` | `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json` | 完整展开实例参数 | 已核实 |
| `S09` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonTurnGroupValidity.hs` | V 主实现、已存输入读取、发行与存储 | 已核实 |
| `S10` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/GroupValidityTypes.hs` | V 输入、状态、occurrence、声明、成员、原因和错误类型 | 已核实 |
| `S11` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/GroupValidityInputs.hs` | 已存 F/Q 到 V 足用输入的投影 | 已核实 |
| `S12` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/GroupValidityProcess.hs` | 同拍安装、按题结算、修订、错误隔离和结束 | 已核实 |
| `S13` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/GroupValidityEvaluation.hs` | `ClosedFormationLocalValidity` 分类与变化比较 | 已核实 |
| `S14` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/GroupValidityStorage.hs` | V core.v2 正式存储表示 | 已核实 |
| `S15` | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonTurnGroupValidity.py` | V Python 构造、exact／As-Of 和公开读取 | 已核实 |
| `S16` | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/_U2GroupValidityFields.py` | V 主表及嵌套明细公开字段 | 已核实 |
| `S17` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs` | 必要 Q 正常存储事件与真实责任结束来源 | 已核实 |
| `S18` | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py` | Q 枚举、exact／As-Of 与成员读取 | 已核实 |
| `S19` | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs` | 必要 F 正常存储事件来源 | 已核实 |
| `S20` | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py` | F 枚举、exact／As-Of 与成员读取 | 已核实 |

---

## 2. 事件与结果总表

| 编号 | 名称 | 载体 | 业务角色 | occurrence 自身发生位置 | 核心身份／修订 |
|---|---|---|---|---|---|
| `E-IN-01` | F 正式候选更新 | `Event (Tick [GroupCandidatesRecord])` 经投影 | 直接输入 | 已存 F 外层 Tick 原时间 | F candidate `Life/Revision/Previous` |
| `E-IN-02` | Q 正式方向组织更新 | `Event (Tick [DirectionalOrganizationRecord])` 经投影 | 直接输入 | 已存 Q 外层 Tick 原时间 | Q `Life/Revision/Previous` + F exact |
| `E-IN-03` | Q 责任结束 | Q 正式记录内嵌套的 `ValidityDutyEnd` 输入 | 直接输入：生命周期收口 | 承载 duty-end 的 Q 外层 Tick 原时间 | `DirectionalKey + last Q exact` |
| `E-MID-01` | V 合并输入 | `Event (Tick ValidityInput)` | 中间处理事件 | 单路沿原 Tick；同拍合并取来源 Tick 的 `max` | 按 F candidate Life 归题 |
| `E-MID-02` | V 处理结果 | `Event (Tick ValidityProcessingResult)` | 中间处理事件 | 与触发 `ValidityInput` 相同 | 成功行各有 V exact；错误按题标识 |
| `B-OUT-01` | V 局部成立观点 occurrence | `ValidityOccurrence`，嵌套于处理结果与存储记录 | **业务主输出** | 触发正式声明变化的 F/Q/end 输入原 Tick | V 自身 `Life/Revision/Previous` |
| `E-OUT-01` | V 正式存储发布 | `Event (Tick [GroupValidityRecord])` | 正式发布 envelope | 沿处理结果的原 Tick | envelope 无业务 Life；内部 V exact 保留 |

V 没有第二种独立的“结束 occurrence”。真实 Q duty end 会写入 `ValidityStatement.statementEnd`，从而在原 V Life 上产生一版收口修订；结算后，该题的活动状态被移除。

---

## 3. 输入事件 occurrence

## 3.1 `E-IN-01`｜F 正式候选更新

### 一次 occurrence 代表什么

V 收到 F 对一个或多个 candidate Life 的准确形成观点。`readValidityFormations` 只读取 V 真正需要的已存字段，不恢复 selected 几何，不重新求两两关系，也不重新运行 F。

### 核心 payload

| 字段 | 业务含义 | 缺失／空值语义 | 是否位置字段 |
|---|---|---|---:|
| `validityFReference` | 实际采用的 F candidate exact | 不缺失 | 否 |
| `validityFPrevious` | 上一 F exact | `Nothing` 表示首版或存储未给前驱 | 否 |
| `validityFKnown` | F 观点知识位置 | 不缺失 | 是 |
| `validityFMembers` | 全部有序成员及转折小值 | 至少两个，对象唯一 | 成员内含位置 |
| `validityFPairs` | F 已裁定逐对 Required 坐标依据 | 合法空依具体候选状态解释 | 否 |
| `validityFBasis` | `Supported / Incomplete / Contradicted` | 不缺失 | 否 |
| `validityFClosed` | 形成观察是否真实关闭 | 不缺失 | 否 |
| `validityFObservation` | F 观察状态 | 不缺失 | 否 |
| `validityFOverlap` | unresolved overlap／overlap 事实 | 不缺失 | 否 |
| `validityFDomainIncomplete` | 形成域覆盖不足 | 不缺失 | 否 |
| `validityFSubsumedBy` | 包含该候选的其他 candidate Life | 空表示无已存包含关系 | 否 |

### 发生位置与携带位置

- **自己的发生位置**：已存 F Event 的外层 `Tick` 原时间。
- **携带位置**：F `known`；每个成员 Turn 的 `actual / confirmation / known`；可选 `FormationClock.coordinate / known`。
- V 不把成员 Turn 的 actual 当成整个 F Event 的 occurrence 位置。

## 3.2 `E-IN-02`｜Q 正式方向组织更新

### 一次 occurrence 代表什么

V 收到 Q 对准确 F candidate Life 的当前方向组织观点。V 消费 Q 已裁定的资格、观察、适用性、成员结论、必要缺件和责任边界，不重新聚合 Q，不重新计算六类运动量，也不读取“latest F”替换 Q 当时引用的 F exact。

### 核心 payload

| 字段 | 业务含义 | 缺失／空值语义 | 是否位置字段 |
|---|---|---|---:|
| `validityQReference` | 实际 Q exact | 不缺失 | 否 |
| `validityQPrevious` | 上一 Q exact | `Nothing` 表示首版或未给前驱 | 否 |
| `validityQKnown` | Q 观点知识位置 | 不缺失 | 是 |
| `validityQFormation` | Q 准确引用的 F exact | 不缺失 | 否 |
| `validityQMembers` | 全部原序成员小核心 | 至少两个，对象唯一 | 成员内含位置 |
| `validityQQualification` | 组资格 | 不缺失 | 否 |
| `validityQObservation` | Q 观察收口状态 | 不缺失 | 否 |
| `validityQApplicability` | Q 主语适用性 | 不缺失 | 否 |
| `validityQOriginalBounds` | 原 `anchor/deadline/revisionEnd` | 不缺失 | 是 |
| `validityQBounds` | 收紧后的责任边界 | 不缺失 | 是 |

成员中保留：对象、asked/used/successor Turn、成员判定、Working/Completed、必要量缺件、`observedThrough`、缺件 actual 包络，以及负向或零净推进的小解释数值。

### 发生位置与携带位置

- **自己的发生位置**：已存 Q Event 的外层 `Tick` 原时间。
- **携带位置**：`validityQKnown`；asked/used/successor Turn 的 `actual / confirmation / known / clock`；`observedThrough`；缺件 actual range；原始和当前责任边界。

## 3.3 `E-IN-03`｜Q 责任结束

### 一次 occurrence 代表什么

Q 对一道方向问题的真实责任结束。它准确引用最后成功 Q、结束原因和结束知识位置。V 不按自己的时钟推测 Q 何时结束。

| 字段 | 业务含义 | 是否位置字段 |
|---|---|---:|
| `validityEndQuestion` | 被结束的 Q 题／F candidate Life | 否 |
| `validityEndLastQ` | 真实最后 Q exact | 否 |
| `validityEndCause` | `DirectionalRevisionDutyEnded / DirectionalScopeEnded` | 否 |
| `validityEndKnown` | 责任结束知识位置 | 是 |

读取 Q duty-end 时，代码还把它携带的最后成功 Q 恢复为一次 Q update，使 V 能用同一份真实最后观点和结束事实共同收口。

---

## 4. 中间处理事件与状态

## 4.1 `E-MID-01`｜`ValidityInput`

F updates、Q updates 和 Q duty ends 合并为一次 V 输入：

```text
ValidityInput
├─ validityFormationUpdates
├─ validityOrganizationUpdates
└─ validityDutyEnds
```

- 单一来源 firing 沿其原 Tick。
- 同一 firing 同时有 F/Q 时，合并 Tick 使用来源 Tick 的 `max`。
- 各来源内部列表保持正式发生顺序。
- 该 envelope 不建立新的业务 Life。

## 4.2 `R-MID-01`｜每题当前 V 组合状态

```text
ActiveValidity
├─ 当前 F（可缺）
├─ 当前 Q（可缺）
├─ 当前 Q end（可缺）
└─ 最后已发行 V（可缺）
```

`CurrentValidityState` 以 `DirectionalKey = F candidate Life` 为 key。某一侧尚未到达时，V 合法持有已到材料，不猜测缺席观点，也不因此产生 `Pending` occurrence。

一个输入 firing 内：

1. 按题收集本拍所有 F/Q/end change；
2. 先安装本拍全部 change；
3. 再对该题共同结算一次；
4. 不发行“只安装了其中一半”的技术中间态。

## 4.3 `E-MID-02`｜`ValidityProcessingResult`

每个 `ValidityInput` firing 都产生一次处理结果：

```text
ValidityProcessingResult
├─ processedValidityRows :: [ValidityOccurrence]
└─ validityInputErrors   :: [ValidityInputError]
```

- `processedValidityRows=[]` 只表示本拍没有新正式 V 声明变化。
- 某题输入合同错误进入独立错误通道，失败题不安装半份状态。
- 同拍其他题仍可成功发行。
- 输入错误不是市场 `Pending`、`Invalid` 或 `ValidityConflict`。

---

## 5. 业务主输出：`B-OUT-01`｜`ValidityOccurrence`

### 5.1 occurrence 业务含义

一次 `ValidityOccurrence` 是：

> 对一个准确 F candidate Life、当前显式 `DirectionUp` 问题，在当时已到的合法 F/Q 观点及可选 Q 责任结束下，V 形成的一版正式局部成立声明。

它不是某个成员的一行，也不是 F/Q 表的简单拼接。

### 5.2 occurrence 主字段

| 字段 | 含义 | 是否位置字段 |
|---|---|---:|
| `validityReference` | V 自身准确 `Life/Revision` | 否 |
| `validityPrevious` | 上一已发行 V exact | 否 |
| `validityQuestion` | 所判断的 F candidate Life | 否 |
| `validityDirection` | 本实例显式方向 `DirectionUp` | 否 |
| `validityQ` | 本次实际采用的 Q exact | 否 |
| `validityKnown` | 参与事实的最大知识位置 | 是 |
| `validityStatement` | 已决定的正式业务正文 | 内含位置 |

### 5.3 `ValidityStatement` 承诺的业务轴

- 实际采用的 F exact；
- V 主结果；
- F `basis / closed / observation / overlap / domainIncomplete / subsumedBy`；
- Q `qualification / observation / applicability`；
- 全部原序成员小核心；
- 具体原因；
- Q 原始与当前责任边界；
- 可选的真实 Q duty-end 原因。

普通 Q endpoint 数值、完整六量向量和运行配置树不被复制成 V 的独立正文。

### 5.4 V 主结果分类与优先级

分类严格按源码优先级执行：

| 优先级 | 条件 | V 结果 | 主要原因 |
|---:|---|---|---|
| 1 | 真实锚撤回，或 F `Withdrawn` 且没有当前形成反证／独立运动判断 | `SubjectNotApplicable` | `CandidateWithdrawn` + 成员原因 |
| 2 | Q=`QualificationConflict` 且存在 `RequiredMotionConflict` | `ValidityConflict` | 成员冲突，必要时带形成缺件／形成原因 |
| 3 | Q=`QualificationRejected` | `Invalid` | 成员方向反证，必要时带撤回 |
| 4 | F basis=`Contradicted` | `Invalid` | `FormationVeto` 等形成反证 |
| 5 | F basis=`Incomplete` | `Pending` | `RequiredFormationMissing` + 形成／成员原因 |
| 6 | F 尚未关闭形成观察 | `Pending` | `FormationObservationOpen` + 成员原因 |
| 7 | Q=`QualifiedCompleted` | `AcceptedCompleted` | 正常无原因列表 |
| 8 | Q=`QualifiedWorking` | `AcceptedWorking` | 正常无原因列表 |
| 9 | 其他未决状态 | `Pending` | 成员原因 |

V 的原因类型包括：

- `FormationMissing`；
- `FormationVeto`；
- `MemberCondition`；
- `FormationObservationOpen`；
- `RequiredFormationMissing`；
- `CandidateWithdrawn`。

### 5.5 发生位置与携带位置

**V occurrence 自身发表位置**：触发本次正式声明变化的 F/Q/end 输入原 Tick。`publishGroupValidity` 原样使用处理结果的 `atTickTs`。

**V knowledge 位置**：

```text
validityKnown
= max(F known, Q known, 可选 end known, 前版 V known)
```

它用于表示本观点所依赖事实的知识闭包和单调性，不是成员 actual 的别名，也不由代码强制等于外层发表 Tick。

**occurrence 携带的其他位置**：

- asked/used/successor Turn 的 actual；
- 每个 Turn 的 confirmation；
- 每个 Turn 的 known；
- 可选 FormationClock coordinate/known；
- `validityObservedThrough`；
- 可选 missing actual range；
- Q original/current `anchor / deadline / revisionEnd`。

因此，V 组观点不能压成一个单一价格 actual 点。

---

## 6. 身份、修订、静默与结束

### 6.1 F/Q/V 身份不能混同

- F candidate 有自己的 `Life/Revision/Previous`；
- Q 有自己的 `Life/Revision/Previous`，并准确引用 F exact；
- V 又建立自己的 `Life/Revision/Previous`；
- `validityQuestion` 使用 F candidate Life 标识同一道业务题；
- `validityQ` 保存本版 V 实际采用的 Q exact。

### 6.2 首发与修订

- 一道题第一次需要发行时，V 生成新的 V Life 和 Revision；
- 后续正式声明变化时，保持同一 V Life，生成新 Revision；
- `validityPrevious` 精确指向上一已发行 V；
- `validityKnown` 不回退。

### 6.3 什么变化会发行

`validityStatementChanged` 比较正式承诺轴、成员小核心和原因。只有这些业务字段发生变化才发行新 V。

特别地：

- F exact 属于正式 statement，F 修订通常会形成新 V revision；
- Q exact 本身不在 statement 的业务变化比较中；若 Q exact 变化但其承诺字段不变，则不发行新 V；
- 已发行 V 保留当时实际 Q exact，不被当前 Q 静默改写。

### 6.4 责任结束

当真实 Q duty-end 到达：

1. 校验其 last Q exact 与当前实际最后 Q 一致；
2. 校验结束知识不早于 F/Q；
3. 把结束原因写入 `statementEnd`；
4. 若该轴造成声明变化，发行原 V Life 的一版收口修订；
5. 随后删除该题的活动状态。

结束不会伪造另一种 V occurrence 类型。

---

## 7. 中间结果、公开明细与业务角色

| 对象 | 真实角色 | 为什么不是独立业务主输出 |
|---|---|---|
| `ValidityStatement` | V occurrence 的嵌套核心 | 无独立 firing 和独立 Life；由所属 V exact 识别 |
| `ValidityMember`／公开 members 表 | V occurrence 的成员快照／明细 | 随所属 V 发表；每行不是一个 V Event |
| `ValidityReason`／公开 reasons 表 | V occurrence 的原因定位明细 | 随所属 V 发表；不是独立市场事件 |
| `ActiveValidity`／`CurrentValidityState` | 中间 working-state | 无独立发表位置；只在输入 firing 更新 |
| `ValidityInputError` | 工程诊断结果 | 不参与市场分类和正式 V 存储 |
| `ValidityDefinitionRecord` | 固定方法与上游绑定元数据 | 首次保存一次，不建立业务 Life |
| `GroupValidityRecord` | 正式存储 envelope | envelope 本身无业务 Life；内部 occurrence 保持 exact |
| `GroupValidityResult` | current v2／legacy v1 存读包装 | 只区分布局；不新增业务事件 |

公开保存、位于主表或被拆成子表，都不改变这些对象的业务角色。

---

## 8. occurrence 处理关系

```text
已存 F Event
  └─ readValidityFormations
       └─ ValidityFormation updates ─┐
                                     │
已存 Q Event                         ├─ mergeWith → Tick ValidityInput
  ├─ readValidityOrganizations       │
  │    ├─ ValidityOrganization updates
  │    └─ ValidityDutyEnd ──────────┘
  │
  └─ duty-end 同时恢复真实最后 Q update

ValidityInput firing
  └─ 按 F candidate Life 分题
       └─ 先安装本拍全部 F/Q/end change
            └─ 校验身份、成员锚、知识与边界
                 ├─ 某题失败 → ValidityInputError（不安装半份状态）
                 └─ F/Q 完整 → makeValidityStatement
                      └─ validityStatementChanged?
                           ├─ 否 → 静默保持既有 V
                           └─ 是 → issueValidityView
                                └─ ValidityOccurrence
                                     └─ storeValidityOccurrence
                                          └─ core.v2 正式发布／公开读取
```

### 8.1 主输出向上追溯

`ValidityOccurrence` 的必要来源链是：

1. 准确已存 F candidate occurrence；
2. 准确已存 Q direction-organization occurrence；
3. 可选真实 Q duty-end；
4. F/Q 足用投影；
5. 同题身份和完整成员锚校验；
6. `ClosedFormationLocalValidity` 分类；
7. 正式 statement 变化判定；
8. V Life/Revision/Previous 发行；
9. core.v2 编码与公开读取。

### 8.2 各输入可能去向

| 输入 | 可能结果 |
|---|---|
| F update | 缺 Q 时只持有；F/Q 完整且声明变化时形成／修订 V；合同错误进入 error channel |
| Q update | 缺 F 时只持有；声明变化时形成／修订 V；只变 Q exact 而正文不变时静默 |
| Q duty-end | 安装真实 end；材料完整时形成收口修订；随后结束该题活动责任 |
| 本拍无 `processedValidityRows` | 另一侧未到、声明未变化或无可发行变化；绝不自动解释成失败或结束 |

---

## 9. 缺失、有效空与无 occurrence

| 情形 | 正确含义 |
|---|---|
| `validityPrevious = Nothing` | 该 V Life 的首个已发行 occurrence |
| `validitySuccessor = Nothing` | 没有已存真实后继 Turn；不是按期限伪造 Completed |
| Turn direction/type=`Nothing` | Q 窄记录未保存且不能按 exact 从 F 补足；保持未知 |
| Turn clock=`Nothing` | 没有已存合法 Clock；不补造 |
| `validityUnavailable=[]` | 没有记录必要量缺件；仍须结合 verdict/completion |
| `validityMissingRange=Nothing` | 没有记录缺件 actual 包络；不等于 `QuantityKnown` |
| `validityProgress=Nothing` | 不在负向／零推进解释场景或无该小值；真实 0 应为 `Just 0` |
| `statementReasons=[]` | `AcceptedWorking/Completed` 的正常无原因列表；不是没有声明 |
| `processedValidityRows=[]` | 本拍没有新正式 V 变化 |
| `validityInputErrors=[]` | 本拍没有输入合同错误 |
| 首次存储记录 `validityOccurrences=[]` | 合法 definition-only 首发；不是市场 occurrence |
| 后续没有外层 V publication | 没有正式业务变化；已有 V 静默保持 |

没有新 occurrence 不能自行解释为 `Invalid`、`Pending`、`SubjectNotApplicable` 或责任结束。

---

## 10. 正式存储与公开读取边界

### 10.1 正式存储

当前生产布局是：

```text
common_turn_group_validity.core.v2
```

`GroupValidityRecordV2` 包含：

- 可选固定 definitions；
- 本拍 0..n 个正式 `ValidityOccurrenceRecordV2`。

旧 `core.v1` 只能显式只读，不能继续写作当前布局。

### 10.2 公开读取接口

- `CommonTurnGroupValidityFrp.to_df(product='occurrences')`；
- `CommonTurnGroupValidityFrp.to_dfs(products=None)`；
- `CommonTurnGroupValidityFrp.validity_overlay()`；
- `CommonTurnGroupValidityFrp.read_exact(reference, products=None)`；
- `CommonTurnGroupValidityFrp.read_at_knowledge(life, as_of, products=None)`。

主表是 `occurrences`。常用明细包括：

- `occurrences_validityMembers`；
- `occurrences_validityReasons`；
- previous、containments、dutyEnd、成员 Turn／Clock／Order／缺件等由字段声明展开的嵌套表。

这些明细是同一 V occurrence 的物理展开，不新增事件身份。

---

## 11. 交叉核对与完成判定

| A Skill 完成条件 | 本产物证据 | 判断 |
|---|---|---|
| 输入事件、输出事件和中间处理结果已按业务角色区分 | 第 2～7 节；机读 `event_catalog/non_event_records` | 通过 |
| 每类事件自己的发生位置及携带位置已说明 | 第 3～5、8～9 节；机读 `position_summary` | 通过 |
| 业务主输出形成／修订／结束关系可追溯到代码 | 第 5～8 节；机读 `processing_relations/business_main_output_trace` | 通过 |
| 未因公开保存而误判业务主输出 | 第 7、10 节 | 通过 |
| 可从主输出向上追溯必要输入 | 第 8.1 节 | 通过 |
| 可从输入向下说明可能结果与静默语义 | 第 8.2、9 节 | 通过 |
| 未确认项没有被写成确定事实 | 第 12 节 | 通过 |

因此，本项 A Skill 判定为：**完整**。

---

## 12. 未确认项、Worker 与阶段边界

### 12.1 阻塞未确认项

**无。** 当前锁定版本足以识别核心输入、业务主输出、位置、身份、修订、结束与处理关系。

### 12.2 非阻塞边界

1. 本阶段没有运行实例，因此不声称当前现场有多少行 V occurrence、各枚举的实际分布或具体发生日期。
2. 代码只承诺 V publication 沿触发输入原 Tick，并另存 `validityKnown`；本产物不把两者数值强制等同。
3. 后继若需观察真实样本、日期、分布或图形，应由 B～E 各自按原 Skill 形成，不由 A 预先选择。

### 12.3 Worker

- 未签发 Worker 工单；
- 未收到或虚称 Worker 结果；
- 原因：A Skill 只要求锁定源码和实例进行代码事实还原，精确主实现、类型、存储和公开读取接口足以完成；本阶段不运行特征。

### 12.4 本阶段不声称

- 不声称 V 已在本 Run 实际运行；
- 不声称已选定观察窗口或样例 occurrence；
- 不声称已有 B～E 产物；
- 不进入合理性分析、S/U2/U3、参数标定、收益判断或资金配置。
