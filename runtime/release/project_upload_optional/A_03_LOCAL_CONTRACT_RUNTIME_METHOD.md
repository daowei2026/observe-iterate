<!--
virtual_source_id: MA-RUNTIME-LOCAL-CONTRACT
runtime_bundle_id: mission-a-project-runtime-bundle-candidate-v0.2.0-integrated-20260904
canonical_successor_repo: daowei2026/feature-refinement-implementation-agent-evolution
canonical_successor_ref: SAME_GIT_TREE_AS_THIS_RUNTIME_RELEASE
canonical_paths:
  - references/local_contract/LOCAL_BUSINESS_CONTRACT_REFINEMENT_METHOD_FULL_REFERENCE.md
  - references/local_contract/CONTRACT_REFINEMENT_HARNESS_CANDIDATES.md
  - profiles/LOCAL_CONTRACT_PROFILE.md
v0_2_integration_ids:
  - MA-V02-LC-P0-001
  - MA-V02-HARNESS-P0-001
generated_release_candidate: true
manual_edit: forbidden
-->

# LOCAL_CONTRACT Runtime Method

## 1. 从 Feature 业务问题开始

每个承重 Feature 先写：

```text
要分辨哪些市场情形；
输入客观事实；
事实在何时可知；
形成动作；
当前方法；
Feature输出与正面含义；
下一层consumer；
相近但不同的解释。
```

## 2. Action／函数树

对可独立说清、做错或替换的业务动作展开：

```text
scope/observation；
evidence formation；
candidate generation；
filter/gate；
relation/group；
judgement；
tie/ambiguity；
transition proposal；
commit；
publication。
```

不要求每项都存在，也不允许把全链压回一个 `evaluate`。

## 3. 组合权力

```text
REQUIRED
VETO
SUPPORTING
DESCRIPTIVE
KNOWNNESS_ONLY
DEPENDENCY_CONSTRAINED
```

必须说明冲突和竞争解释，不用补偿式总分掩盖。

## 4. 运行语义

分别闭合：

```text
何时触发；
读什么旧状态；
哪些输入属于同一cut；
技术顺序是否有业务权力；
怎样形成proposal；
谁commit；
什么时候只更新current；
什么时候发occurrence；
duplicate/replay/late evidence/correction。
```

## 5. 方法

每个 method position 选一个当前状态：

```text
CURRENT_EXECUTABLE
PROVISIONAL_EXECUTABLE
CALIBRATION_PENDING
SOURCE_BLOCKED
OWNER_SEMANTIC_DECISION
```

核心method不能停在 `UNBOUND`。

## 6. 业务回看与state

```text
为什么需要过去；
业务起点；
业务终点；
进入材料；
working summary；
insufficient history；
成功／失败／父scope结束；
清退；
正式历史；
correction重建；
增长不变量。
```

## 7. 最低表达形态

```text
PURE_OR_PPS
SIMPLE_EVENT_TRANSFORM
SIMPLE_STATE_OWNER_UPDATE
CEPS_PROCESSOR
LOCAL_CEPS_SUBGRAPH
CROSS_OWNER_TRANSACTION
INDEPENDENT_BUSINESS_OWNER
PUBLIC_SEMANTIC_PUBLICATION
```

说明低一档为何不足、高一档为何过重。具体 combinator 和文件仍留给工程。

## 8. Book／Life

独立物化要有：

```text
独立业务含义；
独立发生／修订；
独立consumer；
独立history；
不可从相邻产品无损派生。
```

否则保留较小形态。

## 9. Case

走通：

```text
normal；
near-miss；
pending/conflict；
correction；
reopen trigger。
```

## 10. 实现者探针

实现者只读完整合同，真实模拟一条链。每条finding由Pro处置、改正文、横切重扫并re-probe。

## 11. 完成

下游剩余选择只能是：

```text
业务等价工程自由；
明确RepoFact；
窄Owner Gate；
精确Source blocker。
```

不能仍需它决定 Feature、method、state owner、lookback、Book 或正式product。
