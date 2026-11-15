# D003｜C0015 EP Acceptance Matrix

> basis：W002～W006 formal STOP Returns 与 E1 专业消费  
> status vocabulary：`SATISFIED / PARTIAL / UNSATISFIED / NOT_ATTEMPTED`  
> 本矩阵不通过 `G-RUN`，不形成 H3，不提供 current business evidence。

| EP | C0015 E1 状态 | 可接受事实 | 当前缺口 | 阻断关系 | 最小解除条件 |
|---|---|---|---|---|---|
| `EP-WALL-SHARED-01` read-only lifecycle state snapshot | **NOT_ATTEMPTED** | current source字段与D002合同可读 | 无snapshot/accessor、patch、typecheck、只读性质测试 | 阻断真实A observation/transaction trace；不阻断Phase0恢复 | 四PASS后在clean staged source构造并有限验证 |
| `EP-WALL-SHARED-02` structured one-record-per-firing evidence schema | **NOT_ATTEMPTED** | 字段、ordering、pre/post/error合同已定义 | 无DTO/schema、canonical bytes、roundtrip、stable hash | 阻断structured evidence；不阻断Phase0恢复 | 四PASS后构造；只做synthetic serialization |
| `EP-WALL-SHARED-03` isolated clean build closure | **UNSATISFIED** | 累积事实：W006 P0-P3全部PASS；current NNP/Landlock ABI6/rules/seccomp/second bootstrap/FIOCLEX成功；child inherited fd EBADF；parent holder pre/post及竞争有效 | restricted child跨进程fdinfo EACCES导致后续probe未达；同descriptor FIOCLEX effect、完整九项probe/global zero writes未证；offline closure、四预算/monitors未证 | **Phase0 hard blocker** | W007用child EBADF+parent pre/post组合锁证明，不要求child读holder fdinfo；完成R0-A后独立完成R0-B/C，四PASS同时成立 |
| `EP-SCENARIO-01` dedicated scenario target | **NOT_ATTEMPTED** | target名称、接口、禁令已冻结 | 无component/main/manifest/patch/compile-only | 依赖SHARED-01/02/03 | 四PASS后staged construction；fixture不得执行 |
| `EP-SCENARIO-02` exact error assertions | **NOT_ATTEMPTED** | exact constructors与ingress/state区分已定位 | 无adapter、constructor/payload schema、synthetic serialization | 依赖SHARED-02和target | 四PASS后构造direct synthetic records；不得用generic Left |
| `EP-SCENARIO-03` transaction trace integrity | **NOT_ATTEMPTED** | apply/partition/commit边界静态路径已知 | 无DTO、pre/post A、committed/uncommitted验证 | 依赖SHARED-01/02和target | 四PASS后构造；rejected post=pre、O/C空，仅synthetic验证 |
| `EP-SCENARIO-04` existing test-contract conflict ledger | **PARTIAL** | W002 exact commit/function/line static ledger；W003–W006未修改或反证 | dedicated target manifest未引用；无actual scenario result；implementation-vs-test选择未决 | 不阻断Phase0；不能单独解锁action | 未来target manifest逐项引用旧ledger并保留unresolved choice |
| `EP-SCENARIO-05` fixture schema and provenance | **NOT_ATTEMPTED** | 9 scenario/18 firing/22 input合同存在 | 无物化schema/input/hash/static parse-count-order验证 | 不阻断Phase0；阻断target readiness | 四PASS后物化，只做static validation，scenario run=0 |

## 汇总

```text
SATISFIED      = 0
PARTIAL        = 1
UNSATISFIED    = 1
NOT_ATTEMPTED  = 6
W006 new EP satisfied = 0
```

## W006 新增、但不构成 EP-PASS 的工程事实

1. W004 历史 FIOCLEX 已正确分为 policy前成功与policy后EPERM；
2. 本机FIOCLEX/FIONCLEX和seccomp_data layout双来源一致；
3. fresh W006 candidate filter为126 instructions，仅verified FIOCLEX例外；
4. pure evaluator 11 cases、24,240 comparisons、61 jump targets全部PASS；
5. current NNP/Landlock/seccomp实际安装成功；
6. current second Python bootstrap与FIOCLEX=0成功，其他ioctl仍EPERM；
7. restricted child证明inherited writable fd为EBADF；parent外部证明holder lock前后完整；
8. child跨进程读取holder fdinfo EACCES，导致其余probe未执行；
9. failed-chain 2290行trace内3次write/6594 bytes均W006 root，但不是global zero-write证明；
10. R0-B/C、Phase1/2未进入，scenario/normal/current材料为0。

## 专业边界

```text
P0-P3 PASS                       ≠ EP-WALL-SHARED-03 PASS
kernel policy install           ≠ full confinement PASS
current bootstrap FIOCLEX=0     ≠ same-inside-descriptor effect proof
child EBADF + parent lock checks = 可组合的独立事实，但需正式composite proof
failed-chain outside writes=0   ≠ global zero outside writes
static conflict ledger PARTIAL  ≠ current scenario behavior
W007 ORDER发布                  ≠ Phase0/EP/action已执行
```

## 下一次更新触发

仅在新的 W007 formal Return 被原 E1 消费后更新。W007 必须使用独立root、fresh binding/lock、明确的parent/child锁证明拆分与单次R0-A1；W006冻结不重开。若W007 STOP，保留独立成功子事实，不把未发生项补成PASS。
