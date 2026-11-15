<!--
virtual_source_id: MB-RUNTIME-VCC-PROBE
candidate: Mission B v0.2
canonical_sources:
  - 10_methods/04_VCC_EXECUTION_COMPILATION_AND_OWNER_REVIEW.md
  - 30_artifact_contracts/ENGINEERING_IMPLEMENTER_COMPREHENSION_PROBE_V0_2.md
manual_edit: forbidden
-->

# 工程实现者理解探针与重新编译闭环

```yaml
stable_id: MB-V02-OPS-ENGINEERING-PROBE
target_owner:
  - 20_runtime_profiles/compiler/03_OUTPUT_OWNER_AND_AUDIT_HANDOFF.md
  - 30_artifact_contracts/COMPILER_SUBMISSION_BUNDLE.md
role: read_only_downstream_comprehension_probe
```

# 1. 目的

未来实现者只读工程包，模拟一条真实业务结果的实现。它不修改工程包、不裁业务、不选中大型结构，只报告仍被迫自行决定的内容。

# 2. 必须走通的链

```text
accepted Feature／Action
→ exact repo entry
→ target symbol
→ state owner and bounded state
→ current method binding
→ formal product
→ writer/readback
→ consumer
→ required proof。
```

# 3. 探针问题

```text
我从哪个 exact entry 开始；
哪些 parent 内容必须保留；
哪个 Action 对应哪个真实 symbol；
哪些状态属于哪个 owner；
回看、结束和清退是否唯一；
当前 method／RulePack／参数是否已经指定并可达到调用；
pure／simple state／CEPS／transaction的边界是否已决定；
新增 Book 或公共产品是否有业务理由；
production、writer、readback和consumer是否清楚；
我还需要决定哪些业务问题；
我还需要决定哪些跨模块／跨仓主要架构；
哪些选择明确属于业务等价工程自由；
发生阻断时回哪个 Agent／Owner。
```

# 4. Finding 分类

```text
A_CONTRACT_GAP
REPOFACT_GAP_OR_DRIFT
REALIZATION_MAPPING_GAP
STATE_LOOKBACK_GAP
METHOD_BINDING_GAP
PRODUCT_CONSUMER_GAP
PLATFORM_CAPABILITY_GAP
VCC_DEPENDENCY_GAP
ENGINEERING_FREEDOM
IMPLEMENTER_OVERREACH
```

# 5. Compiler disposition

每条 finding 必须由 Compiler Pro 逐项给出：

```yaml
finding_id:
classification:
accepted: yes | partial | no
reason:
authority_and_evidence:
change_location:
affected_vccs:
cross_cut_rescan:
return_route:
  REPOFACT_DELTA | MISSION_A_LOCAL_CONTRACT | MISSION_A_MAP_REVISION |
  PLATFORM_BACKPRESSURE | OWNER_DECISION | COMPILER_LOCAL_FIX | NONE
recompile_required:
re_probe_required:
```

# 6. 闭环

```text
修 active engineering artifact
→ 重扫受影响 Feature／Action／state／method／product
→ 重新编译受影响 VCC
→ 用完整新版重新 probe
→ 再交独立 cold Auditor。
```

只登记 finding、写 debt 或要求 Codex“实现时注意”都不算关闭。
