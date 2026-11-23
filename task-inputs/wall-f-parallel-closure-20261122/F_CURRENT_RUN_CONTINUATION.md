# F800 当前 Run 接续输入｜高置信发现补扫与 Life 36 候选

> 适用 Run：`OI-F800-STAT-20261122-01`。本文件用于接续已经在途的 F800 Run，不新建 F Run，不重做已经有效的 U/X/G，也不自动接受已有 Release 候选。

## 1. 当前已知状态

当前运行记录位于：

```text
daowei2026/observe-iterate
branch: codex/oi-f800-stat-20261122-01
```

截至本接续输入形成前，运行记录显示：

- 当前专业状态为 `WAITING_OWNER`；
- 当前正式 F 代码已演化到 FRP `39f02ec4548e68ba8dbd30061afc870546000994`，TIS 仍为 `2f460d663d821cf2ba25555eda13e78b697d0767`；
- D008 已完成当前正式三年 F800 的 X 与全量 G，31 表独立读回有效；
- GF001、GF002 已在最新结果上关闭；
- 当前报告给出 480 Life、1538 Revision occurrence、1217 publication，以及“峰值责任内 Life 36”；
- `F800-REL-001` 仍是未采用的 Release 候选，尚未形成真实 FeatureReleaseGate／UpstreamReleasePackage；
- Q、V 尚未运行、验证或释放。

本文件不替代当前 Run 自己的 `TASK_PROGRESS`。manager 接续前先读取最新 Run 分支，确认没有比上述状态更新的真实 Return 或 Owner 指令。

## 2. 本次 Owner 接续目的

当前不接受 `F800-REL-001` 的有限释放候选。

原因不是要求重新做完整 F，而是当前正式结果中已出现一个明确值得进入判断的现象：

```text
峰值责任内 Life = 36
```

当前对象只有 `rb / hc / i` 三个品种；如果这些 Life 表达当前仍有效或仍有维护意义的共同转折候选组，36 与该业务语义存在明显冲突风险。该现象此前被统计出来，但没有进入 finding 队列和责任逻辑定位。

同时，上一轮执行曾在发现一个大问题后提前进入深挖，后续问题要到下一轮才发现。本次接续要求在当前正式结果上补做一次“覆盖面与高置信度并重”的发现 pass：不是机械追求广度，也不是穷尽所有可能问题，而是把执行者判断为明确值得处理的高置信不合理现象先找齐、登记，再逐个进入 D。

## 3. 三类角色会话采用同一修正后仓库

本次接续中：

```text
controller／主控会话
manager 会话
executor:E1 会话
```

必须采用 Owner 接续消息中给出的同一个精确 `observe-iterate` commit。

要求：

1. controller 在接续调用中明确写出完整 commit；
2. manager 把该 commit 写入 `TASK_PROGRESS` 和新 D；
3. executor 在执行前读取该 commit 上的：
   - `control-v0.3/01_L0_统计驱动的单特征闭环.md`；
   - `control-v0.3/03_L2_节点输入输出与完成状态.md`；
   - `skills/reasonableness-analysis/feature-global-behavior-profiling/*`；
   - `skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md`；
   - 本文件；
   - `KNOWN_FINDINGS.md`；
4. executor Return 说明实际采用的专业控制 commit。

不需要重建原 manager 或 executor 线程；在原 Run、原 manager、原 E1 中合法接续即可。

## 4. 下一项专业工作

manager 应签发一项新的 G 补充工作，复用当前 D008 正式结果，不先重跑 U 或 X。

### 4.1 高置信发现 pass

executor 在当前正式 F800 结果上：

1. 复用已有 `FeatureUnderstandingPackage`、`FeatureRunResultBinding`、`GlobalBehaviorProfile` 和 31 表读回；
2. 从当前 F 的业务对象、身份、生命周期、上下游转化、时间语义、输出合同和全量／分层结果出发，完成一次高置信不合理现象发现；
3. 不在发现第一个候选后提前停止其余适用业务面的检查；
4. 不把参考类别当作穷尽清单、固定阈值或自动判错规则；
5. 由 executor 自主判断哪些现象已明确值得进入诊断；
6. 形成 `FindingDiscoverySummary`、当前结果绑定的 `CandidateFindingQueue` 和 `ObservationsNotPromoted`；
7. 原 GF001、GF002 保持关闭，不重复诊断，除非新证据直接推翻其闭环。

### 4.2 Owner 指定候选

登记：

```yaml
finding_id: F-LIFE-PEAK-CONCURRENCY
candidate_origin: OWNER_RAISED
status: CANDIDATE
must_assess_before_release: true
observation:
  peak_responsibility_in_scope_life_count: 36
business_concern:
  当前仅 rb/hc/i 三个品种；若这些 Life 表达当前仍有效或仍有维护意义的共同转折候选组，
  36 与该业务语义存在明显冲突风险。
```

不得预设：

- “责任内 Life”必然等于当前 active Life；
- 根因必然是历史累积；
- 根因必然来自 `observation_multiple=800`；
- 36 必然是已确认代码缺陷。

## 5. `F-LIFE-PEAK-CONCURRENCY` 的 D 要求

发现队列快照形成后，该候选进入 D，先完成 `LogicLocalization`。

至少核对：

1. responsibility-in-scope、active、unconfirmed、historical、publication 等口径；
2. 峰值时点、持续时间及峰值时全部 36 个 Life；
3. create／revision／end／current 的对账关系；
4. 每个 Life 的 identity、成员、方向、actual、known、age、最近 revision、expiry 和当前状态；
5. 历史残留、重复 Life、revision 被拆成新 Life、identity 漂移；
6. `observation_multiple=800` 与结束、revision、handoff 期限的关系；
7. 当前并发统计是否把 publication 持有区间、责任窗口或历史记录误解成业务 active；
8. 最早使该现象产生的责任逻辑及准确源码／配置／统计引用。

可能路由：

```text
只是统计或结果口径错误
→ B 修正绑定／统计
→ 更新 G，不重跑三年 Feature

Feature 行为确实需要改变
→ M 前先形成责任逻辑定位和修改影响
→ 按当前具体任务的修改要求处理
→ 正式行为改变后完整重跑 X/G

证据证明 36 个是互不等价且业务上合理的并发组
→ 说明业务依据和区分事实
→ REJECTED_AS_NON_ISSUE

证据不足
→ 保留未决边界，不得直接 Release
```

## 6. Release 与下游

以下条件满足前，不签 F FeatureReleaseGate，不形成 F UpstreamReleasePackage，不启动 Q/V：

- 当前结果上的高置信发现 pass 已完成；
- `F-LIFE-PEAK-CONCURRENCY` 已完成判断；
- 同轮其他高置信候选已有明确状态；
- 若行为或绑定改变，已经完成相应 X/G 回流。

F 最终通过后，Q 仍需绑定准确 F ReleasePackage，并核 F800→Q 的构造、身份与期限兼容；V 在 Q 通过后启动。不得原样调用旧 `make_features(...)` 而重新得到默认 F6，并把它冒充当前 F800 上游。

当前 Campaign 仍采用联合基础 Barrier；是否等待 WALL 由当前真实 Barrier 状态决定，主控不得自行改成独立释放政策。
