# D001｜Additional Evidence Request Candidates

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> 来源：C0004 对 W001 的专业消费  
> 性质：**后继候选，不是 W002，不是当前 continuation，不授予执行权限**

## 1. 使用方式

D001 已完成事实／材料／WORKING 预期基线，并以 `PARTIAL_WITH_LIMITS` 回交。以下项目只供原 manager 决定后续 Gate、优先级和是否另立任务；不得把它们解释为本调用仍在等待的后台工作。

排序原则：

1. 能否解除 current source 与 historical material 的版本断点；
2. 能否直接区分高风险业务问题；
3. 是否能以小而隔离的动作获得；
4. 是否避免全年／全品种／多产品重算。

## 2. 候选 E1｜current canonical generation tuple

### 业务问题

当前 TIS／FRP working-tree 与历史 `P1Wall*Storage` 物化之间，真实生成关系是什么？现役 canonical writer 是否已有同版 materialization？

### 最小材料

```text
exact product leaf
+ generating task/command
+ binary hash / source commit
+ effective Wall params
+ target/calendar/source range/warmup
+ schema and generated wrapper version
+ native reader proof
+ product receipt/manifest
```

### 区分力

可以解除：

- current HEAD 是否实际生成产品；
- legacy/current schema 是否同一演化链；
- 当前 reader 能否解码；
- current tuple 是否具备正式比较资格。

### Gate

优先 provenance recovery；若必须生成新材料，需 manager G-RUN 和隔离 wall-only write/cache/log contract。

## 3. 候选 E2｜FRP full active-map / replay evidence

### 业务问题

`wall_current_view` update 与完整 active map 如何对应，尤其 End 后是否真实删除、同 firing 多变化时 current update 是否只保留最后状态？

### 最小材料

一条 current normal chain 的：

```text
input occurrence batch
pre-state active map
accepted occurrences
current-update batch
post-state active map
wall_occurrences
wall_current_view
wall_diagnostics
```

优先包含：

```text
Start
→ two legal updates in one firing
→ End
```

### 区分力

可直接验证：

- update stream 不是 snapshot；
- same-firing last update；
- Ended update + active deletion；
- O/C/A/D 的形式关系。

### Gate

需要 current schema、可审计 active-map trace 或确定性 replay；producer WallAssembler trace 不可替代。

## 4. 候选 E3｜terminal identity invariant 与 End 后场景

### 业务问题

current source 在 End 后删除 active entry、未见独立 terminal ledger；同 run 同 local no 的后续 Start／update／End 是否实际可能，若发生应怎样分类？

### 最小材料

两部分：

1. producer contract／property：local id 是否 run 内永不复用，End 后是否保证无事件；
2. current controlled fixture：
   - End→update；
   - End→End；
   - End→Start with same local no。

每个 fixture 保存 input、pre/post active map、O/C/D。

### 区分力

可区分：

- 当前静态风险是否不可达；
- before-start 与 after-end 诊断是否准确；
- 是否需要 terminal ledger 或新的 identity。

### Gate

这是高优先风险场景，但 fixture 不得冒充真实行情材料；需要独立受控场景 Gate。

## 5. 候选 E4｜duplicate、conflict 与 firing atomicity

### 业务问题

firing-local occurrence ledger 和两层整批拒绝是否符合真实输入 transaction 的业务原子边界？

### 最小场景

```text
same-firing exact duplicate
cross-firing exact duplicate
same-firing same-ref/different-payload
cross-firing same-ref/different-payload
one legal + one decode-invalid in a firing
one legal + one state-invalid in a firing
```

每个场景保存：

```text
firing formation rule
ordered input rows
pre/post active map
O/C/D
accepted/rejected refs
```

### 区分力

可判断：

- 去重是否只需 firing-local；
- replay contract 是否由上游保证；
- “一错全退”是否保护原子 transaction，还是扩大合法信息损失。

### Gate

先取得 firing formation contract，再设计 fixture；否则无法解释 rollback 是否合理。

## 6. 候选 E5｜Dormant／恢复与时间基础

### 业务问题

Present↔Dormant 是否是实际可达业务状态；BandUpdate 在 Dormant 下如何表达；writer trigger、producer UTI、actual／confirm／known 的关系是什么？

### 最小材料

- 一条 natural 或 controlled `Present→Dormant→BandUpdate→Present→End` 链；
- exact session/calendar/time-basis contract；
- producer ts/UTI、FRP firing、actual/confirm/known（如系统有）和三路输出。

### 区分力

可验证：

- Dormant／恢复的业务价值与状态保持；
- BandUpdate 是否保持 presence；
- 当前只有一个时间轴还是存在确认延迟／知识时间；
- late／out-of-order policy 是否需要显式化。

### Gate

若 producer 合同证明 Dormant 在当前对象／模式不可达，应记录 `NOT_APPLICABLE`，而不是强行构造。

## 7. manager 决策矩阵

| 候选 | 优先级 | 是否需要运行 | 是否能用相同一次动作覆盖 |
|---|---:|---|---|
| E1 current tuple | P0 | provenance 可不运行；否则需要 | 是，作为所有 current 证据的绑定层 |
| E2 active map | P0 | 通常需要 current trace/replay | 可与 E1 current normal chain 合并 |
| E3 terminal identity | P0 | controlled fixture 或强 producer contract | 可与 E4 共用 fixture harness |
| E4 duplicate/atomicity | P1 | controlled fixture | 可覆盖多项 scenario，但不可与自然样本混称 |
| E5 Dormant/time | P1 | natural reuse 或 fixture | 可与 E1/E2 current chain联合，但需状态实际可达 |

## 8. 明确非请求

本候选清单不请求：

- 全年／全品种重算；
- 原样运行现有 multi-product integration runner；
- 修改 TIS／FRP／schema／wrapper；
- 立即冻结 expectation；
- 把 current static finding 定性为生产 bug；
- 把 D001 或父任务重新打开为未完成。

manager 若采用任一候选，应先形成具名问题、精确动作、成本／写面／停止点和新运输合同，再签后续任务。
