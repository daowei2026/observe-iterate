# D003｜C0010 专业 EP Acceptance Matrix

> based on：W002 formal STOP Return + published evidence  
> status vocabulary：`SATISFIED / PARTIAL / UNSATISFIED / NOT_ATTEMPTED`  
> 本矩阵是 E1 专业判断，不替代 Worker 工程事实，也不表示 manager Gate 已通过。

| EP | E1 状态 | 已接受直接证据 | 当前缺口 | 对其他工作的影响 | 精确后继 |
|---|---|---|---|---|---|
| `EP-WALL-SHARED-01` read-only lifecycle state snapshot | **NOT_ATTEMPTED** | exact `WallLifecycle.hs` state fields/source hash已核 | 无 accessor、patch、typecheck、read-only test | 阻断真实 A observation 与 scenario transaction trace；不影响 static conflict ledger | Phase-0 三 blocker 全解后在 clean staged source构造并有限验证 |
| `EP-WALL-SHARED-02` structured firing evidence schema | **NOT_ATTEMPTED** | D002/D003 字段合同已冻结为输入 | 无 DTO/schema、canonical order、roundtrip、stable hash | 阻断 scenario structured evidence；不影响 closure recovery | Phase-0 通过后构造；synthetic serialization בלבד，不运行scenario |
| `EP-WALL-SHARED-03` isolated clean build closure | **UNSATISFIED** | exact/BASE resolver差异、15 package声明、工具hash、bwrap失败、procfs O_RDWR事实、命名共享before/after | compatible offline closure未固定；四预算unknown；全子进程零外写unknown | **Phase-0 hard blocker**；不得进入 staged construction/build/test | W003只用新的 confinement/full-write-trace 方法解除，不重复W002方法 |
| `EP-SCENARIO-01` dedicated scenario target | **NOT_ATTEMPTED** | `frp.cabal` exact baseline、目标名字与合同已知 | 无 component/main、patch、compile-only | 依赖 SHARED-01/02/03 | Phase-0 pass 后 staged construction；禁止执行fixture |
| `EP-SCENARIO-02` exact error assertions | **NOT_ATTEMPTED** | exact error constructors/source位置已核 | 无 adapter、structured constructor/payload、serialization test | 依赖 SHARED-02 与 target | Phase-0 pass后构造synthetic exact-error records；不以generic Left代替 |
| `EP-SCENARIO-03` transaction trace integrity | **NOT_ATTEMPTED** | `applyWallOccurrenceBatch/stepWall/partitionIngressBatch` 静态路径已核 | 无 transaction DTO、pre/post A、committed/uncommitted区分验证 | 依赖 SHARED-01/02 与 target | Phase-0 pass后构造并仅做直接synthetic serialization验证 |
| `EP-SCENARIO-04` existing test-contract conflict ledger | **PARTIAL** | exact commit/function/line：cross-firing Start replay、after-End generic Left、ingress/state边界；未改源码/旧断言 | dedicated target/manifest尚不存在，无法证明未来 harness 显式携带并不隐藏冲突；无actual result | 不阻断 closure recovery；不能单独解锁 action | 保留W002 ledger为不可覆盖输入；未来target manifest必须引用并逐项呈现 |
| `EP-SCENARIO-05` fixture schema and provenance | **NOT_ATTEMPTED** | D002 的9 scenario/18 firing/22 input合同与provenance要求已读 | 无完整schema/input/hash/static count/order validation | 不阻断 closure recovery；阻断未来target readiness | Phase-0 pass后物化并只做static parse/count/order/hash；fixture run必须为0 |

## 汇总

```text
SATISFIED      = 0
PARTIAL        = 1  (EP-SCENARIO-04 static subset only)
UNSATISFIED    = 1  (EP-WALL-SHARED-03)
NOT_ATTEMPTED  = 6
```

## 禁止误读

- `PARTIAL EP-SCENARIO-04` 不等于 current lifecycle behavior 已验证；
- exact source 可读不等于 snapshot/target存在；
- named shared paths unchanged 不等于 global outside writes=0；
- no detected persistent write in a subset不等于零外写；
- metadata command version不等于 compile-only；
- fixture design文本不等于完整fixture或static validation；
- 本矩阵不把 `ARUN-WALL-SCENARIO-001` 重分类，也不通过 `G-RUN`。

## 下一次矩阵更新条件

仅在 W003 或后继真实 Return 被原 E1 消费后更新。每项必须引用真实 patch/schema/test/audit evidence；若 W003 再 STOP，保留已独立满足的子集，不把局部失败扩散为虚假整包失败，也不把未发生项补成 PASS。
