# D003｜C0013 EP Acceptance Matrix

> basis：W002/W003/W004 formal STOP Returns 与 E1 专业消费  
> status vocabulary：`SATISFIED / PARTIAL / UNSATISFIED / NOT_ATTEMPTED`  
> 本矩阵不通过 `G-RUN`，不形成 H3，不提供 current business evidence。

| EP | C0013 E1 状态 | 可接受事实 | 当前缺口 | 阻断关系 | 最小解除条件 |
|---|---|---|---|---|---|
| `EP-WALL-SHARED-01` read-only lifecycle state snapshot | **NOT_ATTEMPTED** | current source字段与D002合同可读 | 无snapshot/accessor、patch、typecheck、只读性质测试 | 阻断真实A observation/transaction trace；不阻断Phase0恢复 | 四PASS后在clean staged source构造并有限验证 |
| `EP-WALL-SHARED-02` structured one-record-per-firing evidence schema | **NOT_ATTEMPTED** | 字段、ordering、pre/post/error合同已定义 | 无DTO/schema、canonical bytes、roundtrip、stable hash | 阻断structured evidence；不阻断Phase0恢复 | 四PASS后构造；只做synthetic serialization |
| `EP-WALL-SHARED-03` isolated clean build closure | **UNSATISFIED** | W004新增：O_RDONLY stdin、sentinel、ABI6/NNP/Landlock ruleset/restrict/seccomp安装成功；failed trace路径完整 | FIOCLEX兼容性、九项probe、global zero writes、single offline closure、四预算/monitors均未证 | **Phase0 hard blocker** | W005仅放行verified FIOCLEX、其余ioctl拒绝；R0-A通过后独立完成R0-B/C，四PASS同时成立 |
| `EP-SCENARIO-01` dedicated scenario target | **NOT_ATTEMPTED** | target名称、接口、禁令已冻结 | 无component/main/manifest/patch/compile-only | 依赖SHARED-01/02/03 | 四PASS后staged construction；fixture不得执行 |
| `EP-SCENARIO-02` exact error assertions | **NOT_ATTEMPTED** | exact constructors和ingress/state区分已定位 | 无adapter、constructor/payload schema、synthetic serialization | 依赖SHARED-02和target | 四PASS后构造direct synthetic records；不得用generic Left |
| `EP-SCENARIO-03` transaction trace integrity | **NOT_ATTEMPTED** | apply/partition/commit边界静态路径已知 | 无DTO、pre/post A、committed/uncommitted验证 | 依赖SHARED-01/02和target | 四PASS后构造；rejected post=pre、O/C空，仅synthetic验证 |
| `EP-SCENARIO-04` existing test-contract conflict ledger | **PARTIAL** | W002 exact commit/function/line static ledger；后续W未修改或反证 | dedicated target manifest未引用；无actual result；implementation-vs-test选择未决 | 不阻断Phase0；不能单独解锁action | 未来target manifest逐项引用旧ledger并保留unresolved choice |
| `EP-SCENARIO-05` fixture schema and provenance | **NOT_ATTEMPTED** | 9 scenario/18 firing/22 input合同存在 | 无物化schema/input/hash/static parse-count-order验证 | 不阻断Phase0；阻断target readiness | 四PASS后物化，只做static validation，scenario run=0 |

## 汇总

```text
SATISFIED      = 0
PARTIAL        = 1
UNSATISFIED    = 1
NOT_ATTEMPTED  = 6
W004 new EP satisfied = 0
```

## W004 新增、但不构成 EP-PASS 的事实

1. read-only stdin 父子接线真实通过；
2. controller sentinel preconfirmation真实完成；
3. Landlock ABI=6、NNP、ruleset create/add/restrict与seccomp install真实成功；
4. 第二Python exec成功，probe脚本O_RDONLY open/read成功；
5. seccomp整体拒绝`ioctl`，导致`FIOCLEX` EPERM，probe主体未运行；
6. 失败链1518行trace的两个成功write均在W004，不能外推全局零外写；
7. R0-B/C、Phase1/2未进入。

## 禁止误读

- kernel setup成功 **不等于** confinement pass；
- `FIOCLEX`被拒 **不等于** Landlock不支持；
- failed-chain outside writes 0 **不等于** global zero writes；
- W004 O_RDONLY接线与sentinel成功不应在后继中重复列为未做；
- `EP-SCENARIO-04=PARTIAL`不是current runtime evidence；
- W005签发不等于Phase0或EP已执行。

## 下一次更新触发

仅在新的W005正式Return被原E1消费后更新。W005必须使用独立root、fresh binding/lock与单次实际尝试；W004冻结不重开。若W005 STOP，保留独立成功子事实，不把未发生项补成PASS。
