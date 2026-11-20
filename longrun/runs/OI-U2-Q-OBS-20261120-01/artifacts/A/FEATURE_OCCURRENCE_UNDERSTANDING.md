# A｜PostTurnGroupDirectionalOrganizationFrp 事件级 occurrence 与处理关系说明

## 0. 产物身份与结论

| 项目 | 值 |
|---|---|
| run_id | `OI-U2-Q-OBS-20261120-01` |
| work_item_id | `OI-U2-Q-OBS-20261120-01-WI-A` |
| stage_instance_id | `OI-U2-Q-OBS-20261120-01-M-A` |
| delegation_id | `D001` |
| 执行身份 | `chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1` |
| 特征 | `PostTurnGroupDirectionalOrganizationFrp`（Q｜转折后成员组的方向组织） |
| 阶段状态 | **完整** |
| 阻塞未确认项 | **无** |
| Worker | **不需要；未签发** |

机读同源产物已先发布：

`daowei2026/observe-iterate@61677f11bcdc41225d1df2615ca267f27e05a12f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.json`

本阶段只还原 Q 的真实事件边界、occurrence payload、发生位置、业务角色及形成／修订／结束关系。没有运行特征，没有选择观察时间，没有设计 CAEGraph，也没有把 F 的阶段成果计作 Q 的阶段成果。

### 0.1 一句话结论

Q 不是把 F 候选换个名字发布。它把 **F candidate occurrence** 作为一道待观察的方向问题，再结合 **同源 source frame** 和 **各成员原价／Calendar 样本**，维护问题订阅和成员运动；当完整组观点发生变化时，产生具有自身 `Life / Revision / Previous` 的 **Q 方向组织观点 occurrence**；当一个曾成功发行的 Q Life 不再承担观察责任时，另行产生 **Q 责任结束 occurrence**。

### 0.2 最关键的事件边界

1. `DirectionalOccurrence` 是 Q 的业务主输出：一个 occurrence 是对一个 F candidate Life 的一版完整组观点，不是某个成员的一行。
2. `DirectionalDutyEnd` 是 Q 的业务主输出中的生命周期收口：它引用最后成功 Q，不伪造新 Q revision。
3. `DirectionalMember`／公开 `members` 表是 Q occurrence 的嵌套成员快照，不是独立 Event occurrence。
4. `DirectionalDefinitionRecord` 是固定方法与对象绑定元数据，不是业务 occurrence。
5. `FrpEvent (Tick [DirectionalOrganizationRecord])` 是正式发布 envelope；一次 firing 可同时携带多个 Q occurrences 和多个 duty ends，表拆分不新增事件身份。
6. F bridge 仍是 F；即使与 Q 在同一函数返回，也不属于 Q 主输出。

---

## 1. 特征引用与当前实例

### 1.1 代码版本

| 职责 | 准确来源 |
|---|---|
| Q Haskell 主实现 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/PostTurnGroupDirectionalOrganization.hs` |
| Q 类型 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/DirectionalOrganizationTypes.hs` |
| Q 订阅 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/DirectionalOrganizationSubscription.hs` |
| Q 成员运动 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/DirectionalOrganizationMotion.hs` |
| Q 发行／修订／收口 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/DirectionalOrganizationPublication.hs` |
| Q 正式存储 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/DirectionalOrganizationStorage.hs` |
| Q Python 构造与读取 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/PostTurnGroupDirectionalOrganization.py` |
| Q 公开字段 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/_U2DirectionalOrganizationFields.py` |
| F Haskell 主实现 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs` |
| F candidate 类型 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateTypes.hs` |
| F source frame | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateMaterial.hs` |
| F→Q reader | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/U2/DirectionalFormationReader.hs` |
| F Python 包装 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py` |

### 1.2 实例

| 字段 | 值 |
|---|---|
| 数据集 | `TA_updto20240229_DBA` |
| 板块 | `steel` |
| Calendar | `night_end_at_2300` |
| 对象 | `rb / hc / i` |
| 尺度 | `5m` |
| 方向 | `up` |
| `common_directional_motion_delta` | `600` |
| `source_core_multiples` | `30` |
| 构造入口 | `make_features(...)` 的第二项 `q`；`PostTurnGroupDirectionalOrganizationFrp.from_formation(f, ...)` |
| 必要上游 | `CommonPriceTurnGroupCandidatesFrp`（F） |

准确实例来源：

- `daowei2026/observe-iterate@3efb2719a66a2fcc1bb86f33b7b0a2258f9bfbf7:task-inputs/u2-fqv-observation/Q_OBSERVATION_RUN_INPUT.md`
- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/实例运行脚本.py`
- `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`
- `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json`

### 1.3 实例参数不能混同的地方

Q 正式定义固定验证：

- 观察责任：`12Δ`；
- 修订责任：`6Δ`；
- 最少成员：`2`。

本实例的 `source_core_multiples=30` 是源材料／锚单位配置，不是把 Q 的 `12 / 6 / 2` 方法责任改成 `30`。这是后继读取定义表时必须保持的区别。

---

## 2. 事件与结果总表

| 编号 | 名称 | 载体 | 业务角色 | occurrence 自身发生位置 | 核心身份／修订 |
|---|---|---|---|---|---|
| `E-IN-01` | 方向形成 source frame 事件 | `Event (Tick FormationFrame)` | 直接输入 | 当前 source firing；frame 内含 `progress/known` | Turn／source patch 身份 |
| `E-IN-02` | F candidate occurrence 事件 | Event；同拍可多候选 | 直接上游输入 | F read/store firing；业务知识位置 `candidateKnown` | F `Life/Revision/Previous` |
| `E-IN-03` | 对象原价／Calendar 样本事件 | `Event (Tick [(Text, MotionSample)])` | 直接输入 | 当前报价 firing | `object + actual/position`；材料 `known` |
| `E-MID-01` | Q 同拍方向输入事件 | 内部 `Event (Tick DirectionalFrame)` | 中间处理 | 三类输入对齐后的当前 firing | 不新建业务 Life |
| `R-MID-02` | 方向问题订阅更新 | 同 firing 状态转移 | 中间处理结果 | 无独立发表位置 | `DirectionalKey = F candidate Life` |
| `R-MID-03` | 成员方向运动快照 | 同 firing 当前结果 | 中间处理结果 | 随 Q occurrence 发表，不独立 firing | `DirectionalKey + object` |
| `E-MID-04` | Q 方向发行批次事件 | 内部 `Event (Tick DirectionalBatch)` | 中间发布 | 当前 Q firing | 批次无独立业务 Life |
| `B-OUT-01` | Q 方向组织观点 occurrence | 批次／正式 envelope 内嵌套 | **业务主输出** | 当前 Q 发布 firing；另带 `directionalKnown` | Q 自身 `Life/Revision/Previous`；准确引用 F candidate |
| `B-OUT-02` | Q 责任结束 occurrence | 批次／正式 envelope 内嵌套 | **业务主输出：生命周期结束** | 当前 Q 发布 firing；另带 `dutyKnown/progress` | 引用最后成功 Q；不新建 Q revision |
| `E-OUT-01` | Q 正式存储发布事件 | `Event (Tick [DirectionalOrganizationRecord])` | 正式发布 envelope | 当前 batch firing | envelope 无业务 Life；内部记录保留身份 |

---

## 3. 输入事件 occurrence

## 3.1 `E-IN-01`｜方向形成 source frame

### 一次 occurrence 代表什么

一次已接受的 F 源材料 frame，给出当前 Calendar 进展、知识前沿、Turn、修订补丁、source 范围是否结束及覆盖事实。Q 需要它来：

- 知道当前源进展；
- 接收 Turn 的合法修订／撤回；
- 收紧问题观察界；
- 判断 source scope 是否结束；
- 在必要时结束 Q 的实际责任。

### payload

| 字段 | 含义 | 类型 | 缺失含义 | 位置字段 |
|---|---|---|---|---:|
| `progress` | Calendar 开放坐标进展 | `Double` | 不缺失 | 是 |
| `known` | frame 知识前沿 | `Int64` | 不缺失 | 是 |
| `turns` | 当前进入的 Turn 材料 | `[GroupTurn]` | 合法空：本拍无新 Turn | Turn 内含位置 |
| `patches` | 既有 Turn 的修订／撤回等 | `[FormationPatch]` | 合法空：本拍无补丁 | patch 内含位置 |
| `ended` | source 范围是否结束 | `Bool` | 不缺失 | 否 |
| `coverage` | 当前 source coverage | source-defined | 不缺失 | 可含范围 |

### 发生位置与携带位置

- **自己的发生位置**：外层 `Tick` 的当前 source firing。
- **携带位置**：`progress`、`known`，以及各 `GroupTurn.actual / confirmation / known` 等。
- 不能把某个 Turn 的 actual 当成整个 frame Event 的发生位置。

## 3.2 `E-IN-02`｜F candidate occurrence

### 一次 occurrence 代表什么

F 对一个候选组 Life 的新建或准确修订。它已经决定了当前组成员及形成依据；Q 不重新做 F 的候选识别，而是对这个准确候选提出方向组织问题。

### 核心 payload

| 字段 | 含义 | 类型 | 缺失含义 | 位置字段 |
|---|---|---|---|---:|
| `candidateReference` | F candidate 准确 `Life/Revision` | `ExactRef` | 不缺失 | 否 |
| `candidatePrevious` | 上一准确 F 修订 | `Maybe ExactRef` | 首个修订 | 否 |
| `candidateKnown` | 此候选修订的业务知识位置 | `Int64` | 不缺失 | 是 |
| `members` | 候选对象与准确 Turn | list | 至少 2 且对象唯一 | Turn 内含位置 |
| `basis/relations` | support／overlap／区间／模式等形成依据 | body fields | 依类型为合法空或有值 | 可含范围 |
| `participation` | 候选参与状态 | enum/status | 不缺失 | 否 |
| `observation` | 候选观察状态 | enum/status | 不缺失 | 否 |
| `domainIncomplete/currentClosed` | 当前领域完整性与闭合状态 | bool/status | 不缺失 | 否 |
| `anchor/deadline/revisionEnd` | F candidate 的 Calendar 界 | `Double` | 不缺失 | 是 |

### 发生位置与身份

- **自己的 Event firing**：F 存储/读取结果被 Q 接收的时点。
- **业务知识位置**：`candidateKnown`。
- **携带的更早位置**：各成员 Turn 的 `actual / confirmation / known`。
- **身份**：F `Life` 表示同一道候选，`Revision` 表示该候选的准确版本；`Previous` 保留修订链。

## 3.3 `E-IN-03`｜对象原价与 Calendar 样本

### 一次 occurrence 代表什么

在一个正常输入 firing 中，提供本实例各对象的原价和独立 Calendar 事实。Q 不前填缺值；缺价与缺 Clock 是两种不同缺件。

| 字段 | 含义 | 类型 | 缺失时含义 | 位置字段 |
|---|---|---|---|---:|
| `sampleActual` | 原材料实际位置 | `Int64` | 不缺失 | 是 |
| `sampleKnown` | 材料可知时点 | `Int64` | 不缺失 | 是 |
| `samplePrice` | 有限原价 | `Maybe Double` | 缺价，不是 0，不前填 | 否 |
| `sampleClock` | 独立 Calendar 事实 | `Maybe FormationClock` | 缺 Clock，与缺价独立 | 是 |
| `samplePosition` | 原采样格位置 | `Maybe Double` | 无可用连续格位置 | 是 |

对象键是 `Text`，本实例为 `rb / hc / i`。同一外层 occurrence 中各对象样本属于同一输入世界。

---

## 4. 中间事件与中间结果

## 4.1 `E-MID-01`｜DirectionalFrame

`buildDirectionalInputEvents` 把同一 firing 的三类输入组织为：

```text
DirectionalFrame
├─ directionalSourceFrame
├─ directionalSamples
└─ directionalCandidates
```

它是 Q 真正消费的一次完整输入 Event。它不建立新的业务 Life；各 candidate、Turn、object 和材料位置仍保留原身份。

## 4.2 `R-MID-02`｜方向问题订阅

订阅层为每个 F candidate Life 建立一道 Q 问题：

```text
F candidate Life
    ↓ 固定映射
DirectionalKey
```

它维护：

- 当前准确 `subscribedCandidate`；
- 原始 `anchor / deadline / revisionEnd`；
- 只可收紧、不可延期的当前三界；
- 各成员 Clock；
- 到期后不再重开的 `motionObservationClosed`；
- 当前接纳和退休回执。

重要身份规则：同一 F Life 的候选 revision 可以更新，但成员对象集合不能在该 Life 下偷偷换成另一组身份。

订阅更新没有自己的独立 Event 发表位置；它是由当前 `DirectionalFrame` firing 触发的中间状态转移。

## 4.3 `R-MID-03`｜成员方向运动快照

每个成员的当前结果包含：

| 字段 | 业务含义 | 位置／缺失语义 |
|---|---|---|
| `motionObject` | 成员对象 | 身份字段 |
| `motionAskedTurn` | F 候选明确问的 Turn | 含 actual/confirmation/known |
| `motionUsedTurn` | 合法源修订后真正量测使用的 Turn | 含 actual/confirmation/known |
| `motionSuccessor` | 真正紧邻后继 | `Nothing` 表示仍工作或没有真实后继；不是观察到期的伪后继 |
| `motionEndpoint` | 当前真实量测端点 | 可缺；含 actual/known/price/clock |
| `motionCompletion` | `MotionWorking` / `MotionCompleted` | Completed 与真实 successor 一致 |
| `motionQuantities` | 六类方向量 | 每类将“有数值／缺件／不适用”分开 |
| `motionVerdict` | 支持、反证、冲突、未决、工作中或撤回 | 组资格的直接成员事实 |
| `motionBasisCondition` | 原候选依据或成员依据已修订 | 不新建成员事件身份 |
| `motionPathComplete` | 路径材料是否完整 | `False` 不等于方向失败 |
| `motionThrough` | 已观察的 Calendar 开放边界 | 位置字段 |
| `motionMaterialKnown` | 实际参与量测的知识前沿 | 位置字段 |
| `motionMissingRange` | 缺件路径的实际包络 | `Nothing` 表示没有已识别缺件范围 |

六量按代码固定次序：

1. `ProgressP`；
2. `AmplitudeA`；
3. `DurationD`；
4. `PathLengthL`；
5. `EfficiencyE`；
6. `CounterC`。

每个 `DirectionalQuantity` 同时保留：

- `quantityKind`；
- `quantityNumber :: Maybe Double`；
- `quantityAvailability`。

其中真实数值 0 仍为 `Just 0`；`Nothing` 必须结合 availability 判断是 endpoint、Clock、路径缺失，还是 zero-path 不适用。

成员快照对观察很重要，但它没有独立 Event firing。只有形成一版新 Q 观点时，成员全量作为该 Q occurrence 的 payload 共同发表。

## 4.4 `E-MID-04`｜DirectionalBatch

一次内部发行 batch：

```text
DirectionalBatch
├─ batchInput
├─ batchOccurrences   -- 0..n 个新 Q 观点修订
└─ batchEnds          -- 0..n 个真实责任结束
```

它保留真实源顺序，不按 UUID 重排。无新 Q 时仍可有 `batchEnds`。batch 没有独立业务 Life。

---

## 5. 业务主输出

## 5.1 `B-OUT-01`｜Q 方向组织观点 occurrence

### 业务含义

一次 `DirectionalOccurrence` 是：

> 对一个 F candidate Life，在当前全部合法材料下形成的一版完整方向组织观点。

它同时表达：

- 当前使用哪一版 F candidate；
- 全体成员当前怎样运动；
- 各成员支持、反证、冲突或仍未决；
- 整个组处在工作、到达观察界还是 source scope ended；
- 当前问题是否仍适用；
- 当前组资格是 rejected、conflict、pending、qualified working 还是 qualified completed。

### 身份和修订

| 字段 | 含义 |
|---|---|
| `directionalReference` | Q 自身的准确 `Life/Revision` |
| `directionalPrevious` | 同一 Q Life 的上一准确 revision |
| `candidateReference` | 本 Q revision 使用的准确 F candidate；不冒充 Q 身份 |

同一 F candidate Life 映射到同一道 Q Life。只有当前 `DirectionalView` 相对最后已发行视图发生变化，才生成下一 Q revision；没有变化就没有新 Q occurrence。

### 位置

Q 组观点没有被压成一个单一价格 actual 点：

- **自己的发生／发表位置**：当前 Q 输入 firing；
- **知识位置**：`directionalKnown`，是形成完整观点所需事实的知识上界；
- **引用的实际位置**：成员 asked/used/successor Turn 的 actual；
- **引用的确认／已知位置**：Turn confirmation/known；
- **量测位置**：endpoint actual/known/clock、through、materialKnown、missing range；
- **观察界**：原始与当前 anchor/deadline/revisionEnd。

因此不能把最早 Turn actual、最后 endpoint actual 或 `directionalKnown` 任意一个单独称为“Q 的实际发生点”。

### 组级资格

发行层按成员与适用性形成资格：

- subject withdrawn → `QualificationRejected`；
- 存在方向反证／冲突 → `QualificationConflict`；
- 仍有未决成员 → `QualificationPending`；
- 全部支持且全部完成 → `QualifiedCompleted`；
- 全部支持但仍工作 → `QualifiedWorking`。

公开 wrapper 还可以展开方向状态、支持／反证／未决计数和 `all_support`。这些是本 Q occurrence 的派生组级字段，不是新的 Event occurrence。

## 5.2 `B-OUT-02`｜Q 责任结束 occurrence

### 业务含义

`DirectionalDutyEnd` 表示：一个曾成功发行 Q 观点的 Life 已不再由当前 Q 发行状态承担责任。

它与成员运动完成、观察到期并非同一个概念：

- 成员可以 `MotionCompleted`，Q Life 仍保有最后观点；
- Q 可以到达 `HorizonReached` 并发行观点，但实际责任是否结束仍由发行 retention 决定；
- 真正责任结束必须显式产生 `DirectionalDutyEnd`，不能从“本拍没有新 Q”推断。

### payload

| 字段 | 含义 |
|---|---|
| `dutyQuestion` | 原 DirectionalKey／原 F candidate Life |
| `dutyLastSuccessful` | 最后成功发行的准确 Q occurrence |
| `dutyEndReason` | `DirectionalRevisionDutyEnded` 或 `DirectionalScopeEnded` |
| `dutyKnown` | 真正结束知识位置 |
| `dutyProgress` | 结束时 Calendar 进展 |

### 修订规则

责任结束不生成一版虚假的“结束 Q revision”。它引用最后成功 Q，并作为另一类生命周期 occurrence 发布。

## 5.3 `E-OUT-01`｜正式发布 envelope

正式存储类型：

```text
DirectionalOrganizationRecord
├─ organizationDefinitions
├─ organizationOccurrences
└─ organizationDutyEnds
```

一次 envelope Event occurrence 可包含：

- 首次固定 definition；
- 0..n 个 `B-OUT-01`；
- 0..n 个 `B-OUT-02`。

`definition` 可在首次没有 Q viewpoint 时发布；此后若既没有新 Q 又没有 duty end，不应凭空解释成“失败 occurrence”或“结束 occurrence”。

Python 读取：

- `to_df()`：默认 Q occurrence 视图；
- `to_dfs()`：definition、occurrences、members、duty_ends 等；
- `read_exact(life, revision)`：准确修订；
- `read_at_knowledge(life, as_of)`：沿 previous 链选出该知识时点可见 tip。

DataFrame 拆成多张表不改变事件边界：一版 occurrence 与它的所有 member 行仍是同一个 Q 业务 occurrence。

---

## 6. 处理关系

```text
E-IN-01 source frame ─┐
E-IN-02 F candidate ──┼─> E-MID-01 DirectionalFrame
E-IN-03 price/clock ──┘
                              │
                              ├─> R-MID-02 subscription
                              │        │
                              │        └─ F Life → DirectionalKey
                              │
                              ├─> R-MID-03 member motion snapshots
                              │
                              └─> current DirectionalView
                                       │
                         view changed? ─┤
                               no       └─> 不产生新 Q occurrence
                               yes          │
                                            └─> B-OUT-01 Q Life/Revision

last successful Q no longer retained
              └─> B-OUT-02 duty end（引用最后准确 Q，不造新 revision）

B-OUT-01 + B-OUT-02
              └─> E-MID-04 batch
              └─> E-OUT-01 正式存储 envelope
              └─> Python exact / As-Of / tables
```

### 6.1 关系清单

| 关系 | 上游 → 下游 | 类型 | 身份映射 | 位置映射 |
|---|---|---|---|---|
| `R01` | 三类输入 → `DirectionalFrame` | 形成／对齐 | 保留 Candidate、Turn、Object 身份 | 当前外层 Tick 对齐，内层位置原样携带 |
| `R02` | F candidate + source frame → subscription | 形成／修订／收紧／退休 | F Life → `DirectionalKey` | candidate/Clock 决定观察界，只收紧不延期 |
| `R03` | subscription + price/clock + source → member snapshot | 量测／更新 | `DirectionalKey + object` | Turn 起点 + 样本路径 → endpoint/through/known |
| `R04` | subscription + members → Q occurrence | 形成／更新 | 同一 Q Life，变化产生新 Revision | 当前 firing 发表，`directionalKnown` 取证据知识上界 |
| `R05` | member verdicts → group qualification | 解释／资格 | 不改变 Q 身份 | 资格无独立 Event 位置 |
| `R06` | F exact candidate → Q candidate ref | 引用 | F 与 Q 各保留自身 Life/Revision | F known 与 Turn 位置进入 Q 证据 |
| `R07` | 旧 Q → 新 Q | 修订／替代 | Life 不变，Revision + Previous | 新 firing 发表；旧修订不无痕覆盖 |
| `R08` | 最后成功 Q + 退休事实 → duty end | 结束 | 引用最后准确 Q，不造新 Revision | 当前 firing + `dutyKnown/progress` |
| `R09` | Q occurrences + ends → store envelope | 正式发布 | 内部身份原样保存 | 继承 batch Tick |
| `R10` | store → Python 表／exact／As-Of | 读取／投影 | identity 与 previous chain 保留 | 所有位置语义不变 |
| `R11` | F bridge ↛ Q main output | 边界排除 | F/Q 各自身份 | 同函数返回不合并事件位置 |

---

## 7. 输入去向与主输出追溯

### 7.1 从 Q 主输出向上追溯

`B-OUT-01`：

```text
source frame + F candidate + price/Calendar
→ DirectionalFrame
→ subscription
→ member motion snapshot
→ DirectionalView
→ 变化检测
→ Q Life/Revision occurrence
→ storage/public reader
```

`B-OUT-02`：

```text
最后成功 B-OUT-01
+ source/candidate/subscription 的真实退休事实
→ duty end reason + known + progress
→ storage/public duty_ends
```

### 7.2 从输入向下追踪

- `E-IN-01`：输入对齐、Turn 修订、观察界收紧、source scope end、Q retention 和 duty end。
- `E-IN-02`：创建／修订 Q 订阅、固定问题成员、提供准确 candidate reference、决定同一 Q Life 的上游身份。
- `E-IN-03`：形成成员路径、endpoint、六量、verdict、材料知识和缺件状态，从而触发 Q revision。

---

## 8. 缺失、空与“无 occurrence”的语义

1. 某 firing 没有新 Q occurrence，只说明 view 未变化或没有可发行观点；不自动表示失败、无效或责任结束。
2. 责任结束必须有 `DirectionalDutyEnd`。
3. `samplePrice = Nothing` 与 `sampleClock = Nothing` 是不同缺件，不前填，也不把缺失改写成 0。
4. `quantityNumber = Nothing` 需要结合 `quantityAvailability` 区分 endpoint、Clock、路径缺失与 zero-path 不适用。
5. 真实数量 0 是 `Just 0`。
6. `motionPathComplete=False` 表示路径材料不完整，不等于成员方向反证。
7. `members` 是 Q occurrence 的嵌套 payload；DataFrame 没有成员行不能脱离 occurrence/read status 直接解释。
8. F bridge 为空或 Q 本拍无新观点，均不能被替换成另一个业务结论。

---

## 9. 业务角色判定

| 内容 | 判定 | 理由 |
|---|---|---|
| `DirectionalOccurrence` | 业务主输出 | Q 被定义出来要交付的当前方向组织观点，具有自身正式身份和修订链 |
| `DirectionalDutyEnd` | 业务主输出：生命周期收口 | 明确交付一个 Q Life 的真实责任结束 |
| `DirectionalMember` | 中间处理结果／主输出 payload | 用于形成和解释 Q 观点；公开保存不使其成为独立事件 |
| `DirectionalSubscription` | 中间状态 | 维护问题、界和成员身份，没有独立公开 occurrence |
| `DirectionalFrame` | 中间输入事件 | 对齐材料，不是最终业务观点 |
| `DirectionalBatch` | 中间发布事件 | 携带真正 Q occurrences/ends，本身不建业务 Life |
| `DirectionalDefinitionRecord` | 元数据 | 固定方法和对象绑定，只写一次 |
| `DirectionalOrganizationRecord` | 正式存储 envelope | 正式传输容器，不等于单个 Q 观点 |
| F candidate | 必要上游输入 | Q 准确引用，但不属于 Q 自身主输出 |
| F bridge | 上游回传 | 同函数返回不改变业务归属 |

---

## 10. A 阶段核对结果

### A1｜当前版本和实例

完成。Haskell 主实现、子模块、Python 构造／读取、实例参数和必要 F 上游均已定位到精确 commit。

### A2｜输入事件

完成。识别三类直接输入：source frame、F candidate occurrence、对象原价／Calendar 样本。

### A3｜输出事件

完成。识别 Q viewpoint occurrence、Q duty end，以及其正式发布 envelope；未把 definition、member 表或 F bridge 误判为 Q occurrence。

### A4｜业务主输出与中间结果

完成。`B-OUT-01 / B-OUT-02` 为业务主输出；订阅、成员快照、batch 等为中间结果。

### A5｜事件位置

完成。已分别说明 firing、actual、confirmation、known、Calendar progress/clock、endpoint 和 publication position。

### A6｜处理关系

完成。形成、更新、引用、修订／替代、结束和公开读取均可追溯到代码。

### A7｜交叉核对

完成：

- 从每类主输出均能追溯到必要输入；
- 从每类输入均能说明其下游去向；
- 事件发生位置与代码触发位置一致；
- 没有把无 occurrence 写成失败或结束；
- 没有未确认项被写成确定事实。

## 11. 未确认项与后继可用性

- 阻塞未确认项：**无**。
- 非阻塞说明：各六量的完整数值公式位于 `DirectionalOrganizationMotion.hs`，但 A 已确定其种类、载荷、缺失语义和在 Q occurrence 中的业务角色；公式的进一步数值分析不是 A 完成的前置。
- 后继可依赖的稳定结论：Q 的主观察对象应以 `DirectionalOccurrence` 与 `DirectionalDutyEnd` 为事件边界，并保留 Q/F 准确引用、全成员 payload 及多类位置，不能按 DataFrame 行机械拆事件。

## 12. 完成判定

**A 阶段状态：完整。**

当前版本中影响后继 B、C、D 的事件、位置、业务角色和真实处理关系均已说明；没有核心输入、主输出或发生位置缺口。A 不需要 Worker，也不需要通过运行 Q 才能完成上述代码事实判定。
