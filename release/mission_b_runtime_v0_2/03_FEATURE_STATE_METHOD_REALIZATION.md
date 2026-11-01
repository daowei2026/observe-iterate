<!--
virtual_source_id: MB-RUNTIME-REALIZATION
candidate: Mission B v0.2
canonical_sources:
  - 10_methods/11_FEATURE_STATE_METHOD_REALIZATION_COMPILATION_V0_2.md
manual_edit: forbidden
-->

# Feature、状态、方法与产品的 repo-aware realization 编译方法

```yaml
stable_id: MB-V02-METHOD-FEATURE-REALIZATION
target_owner: 10_methods/03_ENGINEERING_COMPILATION_AND_REALIZATION_FULL_REFERENCE.md
method_status: source_backed_candidate_delta
scope: Mission B common core
```

# 1. 输入身份

Compiler 不再只接“业务任务包＋S0 RepoFact”。当上游使用 Mission A v0.2 时，至少需要收到：

```text
工作地图位置和完整 scope；
Feature Narrative 中本 slice 的正面含义、向上用途和 NonClaim；
Source／客观事实／Feature 的形成链；
承重 Action tree；
每个 method position 的成熟度和 current/provisional 程序；
business time、same-cut、read-old、current／occurrence／history；
业务回看起止、最小充分状态、结束、清退和重建；
Mission A 给出的最低充分运行表达候选；
正式产品、writer、readback 与 consumer；
normal／near-miss／pending-conflict／correction Case；
允许的工程自由；
Owner 未决项和 MapRevision 状态。
```

缺少上述内容时，Compiler 不应从代码猜补。它必须把缺口精确返回 Mission A，或仅编译不受影响的独立区域。

# 2. 两类事实必须先分开

## 2.1 业务应然

由 accepted business contract 决定：

```text
观察什么；
Feature 是什么；
Action 做什么；
状态属于谁；
何时发生；
回看什么；
方法回答什么问题；
正式产品和 consumer 承诺什么。
```

## 2.2 当前宿主事实

由 RepoFact S0 决定：

```text
当前 production entry 和真实 caller；
已有 symbol、module、state store、Event／Dynamic／Behavior；
已有 CEPS／Reflex／actor／batch 能力；
已有 RulePack／CFIS／method asset；
现有 writer／DBA／readback；
consumer 实际读取面；
平台职责、保护路径和未知项。
```

当前代码存在不能覆盖业务应然；业务合同完整也不能证明当前 repo 已有落点。

# 3. RepoFact 必须围绕 realization 问题定向读取

RepoFact 不做无目的全仓扫描。对每个承重 Feature／Action，最少调查：

```text
1. 真实输入从哪个 production caller 到达；
2. 当前有没有可复用的 typed business value；
3. 当前状态由谁拥有、生命周期如何结束；
4. 哪个 symbol 真正实现或最接近该 Action；
5. 方法资产怎样加载、参数怎样进入、结果怎样被消费；
6. 当前 product、writer、readback 和 consumer 链在哪里；
7. 哪些只是 PoC、legacy、failed code 或测试壳；
8. 平台是否已有表达能力；
9. 哪些事实无法从 repo 唯一得出。
```

输出仍是 direct fact／inference／candidate／gap 四分，且 S0 冻结后 Compiler 只读。

# 4. 业务到宿主 realization ledger

每个承重单元必须形成一条可读映射：

```yaml
business_unit:
  feature_or_fact:
  positive_meaning:
  action:
  business_owner:
  trigger_and_time:
  required_reads:
  state_writes:
  current_method:
  formal_output:
repo_realization:
  current_or_new_host:
  exact_repo_ref:
  production_entry:
  target_symbols:
  platform_assets:
  writer_and_readback:
  consumer:
realization_decision:
  category:
  why_lower_is_insufficient:
  why_higher_is_unnecessary:
  engineering_freedom:
  return_or_owner_gate:
proof:
  static:
  runtime:
  production:
```

Ledger 不是字段填表替代分析。它用于证明每个业务责任既没有丢失，也没有被多造一个 owner／Book／processor。

# 5. 最低充分运行表达的工程编译

Mission A 给出业务复杂度结论，Mission B 将它与当前平台事实对账。候选类别：

## `PURE_OR_PPS`

适用于同一冻结 cut 上的确定性变换或可替换纯程序。工程包必须说明真实 caller、typed 输入输出和方法版本；不得因为算法复杂就仪式化成 CEPS。

## `SIMPLE_EVENT_TRANSFORM`

适用于没有独立持续状态的 map／filter／merge。必须保留业务触发与错误语义，不能让 callback 顺序获得业务权力。

## `SIMPLE_STATE_OWNER_UPDATE`

适用于一个明确 owner、少量 Event 驱动的 transition。若一个简单 `foldDyn`／actor reducer 足以保持业务语义，不得为了“显得像 CEPS”拆出虚假 processor 网络。

## `CEPS_PROCESSOR`

适用于一个可以独立说清、独立做错、独立替换的事件业务 processor。必须有真实 typed ports、caller、实现和测试，不接受仅命名、no-op 或 wrapper。

## `LOCAL_CEPS_SUBGRAPH`

适用于 candidate、filter、gate、parallel evidence、sampling、feedback、proposal、commit 等多个独立 Action 组成的局部图。工程图必须展示拓扑，不得把它们重新压成 WholeState 大 reducer。

## `CROSS_OWNER_TRANSACTION`

适用于多个状态 owner 基于同一 cut／read-old 形成 proposal 并统一 apply。任务包必须锁 transaction identity、冲突处理和部分失败语义。

## `INDEPENDENT_BUSINESS_OWNER`

只在有独立 identity、lifecycle、writer、Current／History 和 consumer 时成立。实现方便、审计需要或 readback 需要不足以创造新的业务 owner。

## `PUBLIC_SEMANTIC_PUBLICATION`

只在多 consumer、公共语义、正式 history 或动态订阅确有需要时建立。局部 diagnostic、method intermediate 和 receipt 不得自动升级为公共产品。

Compiler 对每项选择同时说明：

```text
为什么低一档保持不了业务语义；
为什么高一档会增加无必要业务对象或运行复杂度；
哪些具体模块、类型、组合器仍属于实现者工程自由。
```

# 6. bounded-state 物理计划

业务回看不能等到性能事故后再由实现者发明。每个持续判断都必须编译出：

```yaml
bounded_state_plan:
  business_lookback_question:
  start_anchor:
  end_or_closure:
  eligible_material:
  active_identity:
  current_sufficient_state:
  working_summary:
  formal_append_only_history:
  eviction_condition:
  rebuild_source:
  replay_and_correction:
  allowed_growth_dimension:
  forbidden_unbounded_growth:
  persistence_boundary:
```

工程选择可以改变容器、索引、压缩和缓存，但不能改变：

```text
回看回答的业务问题；
材料资格；
结束和清退；
正式 history；
correction；
business identity。
```

固定最近 N 条与“从业务锚点到当前”若回答不同问题，不得当作等价性能优化。

# 7. current／provisional method 的实际绑定

对每个 method position，Compiler 必须读取 Mission A 的状态：

```text
CURRENT_EXECUTABLE
PROVISIONAL_EXECUTABLE
CALIBRATION_PENDING
SOURCE_BLOCKED
OWNER_SEMANTIC_DECISION
```

然后形成：

```yaml
method_binding:
  business_question:
  maturity:
  method_id:
  version:
  host_asset_or_symbol:
  deterministic_envelope:
  inputs_and_as_of_time:
  outputs_and_consumer:
  parameter_source:
  knownness_and_failure:
  activation_path:
  result_use_path:
  version_in_product:
  replay_consequence:
  proof_that_binding_is_effective:
```

特别检查：

```text
参数是否真正到达 method；
RulePack／CFIS是否复用已有平台；
membership／components是否被伪造为 crisp 后投影；
method运行成功是否被错误等同于 business commit；
fallback是否生成了未经授权的正式结果。
```

# 8. Book／记录／产品的物化节制

对每个拟新增 artifact，明确选择：

```text
同 owner 内字段；
active working state；
method intermediate；
immutable cut/run artifact；
audit receipt；
current projection；
append-only occurrence；
independent formal Book；
public product。
```

独立 Book 仍需证明：

```text
独立业务含义；
独立发生／修订；
独立 consumer；
独立 history；
不能从邻近正式产品无损派生。
```

consumer 当前只读取一小部分不能自动缩掉完整 business product；反过来，任务包里列出的全部内部量也不必全部公共物化。Compiler 必须同时给出：

```text
完整业务产品；
当前 consumer 读取面；
内部 working 面；
正式持久化面；
未来 consumer 扩展边界。
```

# 9. production 到 readback 的完整链

每个 VCC 所属业务结果必须能从工程图定位：

```text
真实输入
→ production entry
→ caller
→ Action／state／method
→ formal occurrence/current
→ writer
→ storage／transport
→ official readback
→ consumer。
```

源码存在、模块登记、fixture、测试 helper 和 schema 非空不能代替生产可达性。

# 10. VCC 切片

VCC 以一个可观察业务结果为中心，不按文件机械切。每个 VCC 至少包括：

```text
业务结果与 Feature 语义；
exact parent 和 repo tuple；
Action→symbol；
状态和 bounded-state 计划；
method binding；
产品、writer、readback、consumer；
允许写面和保护面；
不变量；
最小静态／运行／生产 proof；
与其他 VCC 的依赖；
失败时返回 RepoFact、Mission A、平台或 Owner 的路线。
```

D／S／I／P／X 按实际义务使用，不要求五类齐全。

# 11. Owner 五分钟工程图

Owner 先看：

```text
业务 Feature 在哪个宿主里怎样活；
哪些 Action 用 pure／simple state／CEPS；
重要状态保存什么、何时清退；
当前方法怎样生效；
新增／修改／退役哪些模块和 Book；
正式产品怎样到 consumer；
哪些改变会导致已有实现或下游 stale。
```

最后才看 VCC 编号、proof 清单和 repository metadata。

# 12. 完成和返回

Compiler handoff-ready 前必须满足：

```text
没有业务单元只剩文件名或模块名；
没有核心 method 只剩 asset ref；
bounded-state 不由 Codex 自行发明；
最低充分表达已说明；
Book／Life 资格已说明；
production/readback 链已定位；
Codex dry-run 后不再需要决定业务或中大型架构；
所有未决项都精确返回 RepoFact、Mission A、平台或 Owner。
```
