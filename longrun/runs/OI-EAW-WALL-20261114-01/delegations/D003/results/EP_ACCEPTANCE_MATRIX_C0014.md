# D003｜C0014 EP Acceptance Matrix

> basis：W002/W003/W004/W005 formal STOP Returns 与 E1 专业消费  
> status vocabulary：`SATISFIED / PARTIAL / UNSATISFIED / NOT_ATTEMPTED`  
> 本矩阵不通过 `G-RUN`，不形成 H3，不提供 current business evidence。

| EP | C0014 E1 状态 | 可接受事实 | 当前缺口 | 阻断关系 | 最小解除条件 |
|---|---|---|---|---|---|
| `EP-WALL-SHARED-01` read-only lifecycle state snapshot | **NOT_ATTEMPTED** | current source字段与D002合同可读 | 无snapshot/accessor、patch、typecheck、只读性质测试 | 阻断真实A observation/transaction trace；不阻断Phase0恢复 | 四PASS后在clean staged source构造并有限验证 |
| `EP-WALL-SHARED-02` structured one-record-per-firing evidence schema | **NOT_ATTEMPTED** | 字段、ordering、pre/post/error合同已定义 | 无DTO/schema、canonical bytes、roundtrip、stable hash | 阻断structured evidence；不阻断Phase0恢复 | 四PASS后构造；只做synthetic serialization |
| `EP-WALL-SHARED-03` isolated clean build closure | **UNSATISFIED** | 累积事实：W004 O_RDONLY stdin/sentinel/ABI6/NNP/Landlock/seccomp安装成功；W005本机FIOCLEX=0x5451一致且精确定位准备器断言错误 | candidate BPF未生成/评价；当前R0-A1/九probe/global zero writes未证；single offline closure、四预算/monitors未证 | **Phase0 hard blocker** | W006先正确区分W004 pre/post-policy trace，pure static evaluator PASS；一次R0-A1通过后独立完成R0-B/C，四PASS同时成立 |
| `EP-SCENARIO-01` dedicated scenario target | **NOT_ATTEMPTED** | target名称、接口、禁令已冻结 | 无component/main/manifest/patch/compile-only | 依赖SHARED-01/02/03 | 四PASS后staged construction；fixture不得执行 |
| `EP-SCENARIO-02` exact error assertions | **NOT_ATTEMPTED** | exact constructors与ingress/state区分已定位 | 无adapter、constructor/payload schema、synthetic serialization | 依赖SHARED-02和target | 四PASS后构造direct synthetic records；不得用generic Left |
| `EP-SCENARIO-03` transaction trace integrity | **NOT_ATTEMPTED** | apply/partition/commit边界静态路径已知 | 无DTO、pre/post A、committed/uncommitted验证 | 依赖SHARED-01/02和target | 四PASS后构造；rejected post=pre、O/C空，仅synthetic验证 |
| `EP-SCENARIO-04` existing test-contract conflict ledger | **PARTIAL** | W002 exact commit/function/line static ledger；后续W未修改或反证 | dedicated target manifest未引用；无actual result；implementation-vs-test选择未决 | 不阻断Phase0；不能单独解锁action | 未来target manifest逐项引用旧ledger并保留unresolved choice |
| `EP-SCENARIO-05` fixture schema and provenance | **NOT_ATTEMPTED** | 9 scenario/18 firing/22 input合同存在 | 无物化schema/input/hash/static parse-count-order验证 | 不阻断Phase0；阻断target readiness | 四PASS后物化，只做static validation，scenario run=0 |

## 汇总

```text
SATISFIED      = 0
PARTIAL        = 1
UNSATISFIED    = 1
NOT_ATTEMPTED  = 6
W005 new EP satisfied = 0
```

## W005 新增、但不构成 EP-PASS 的工程事实

1. 原 W1/fresh W005 binding、lock、actual HOME/CODEX_HOME与具名sentinel已核；
2. 本机 `termios.FIOCLEX` 与 asm-generic header均为 `0x5451`；
3. W004 trace line312为policy前FIOCLEX成功，line1509为policy后EPERM；
4. W005准备器错误地要求所有FIOCLEX行含EPERM，exit1且按合同停止；
5. W005 runtime/launcher/BPF未物化，pure evaluator=0，R0-A1=0；
6. R0-B/C、Phase1/2未进入；
7. 场景、normal、build、compile、serialization、current材料均为0。

## 禁止误读

- local constant一致 **不等于** candidate BPF正确；
- intended request-level delta文本 **不等于** filter已生成或static PASS；
- W004历史安装后EPERM **不等于** W005 kernel实测；
- 准备器断言失败 **不等于** Linux/kernel/FIOCLEX不支持；
- 具名输入收尾一致 **不等于** global zero outside writes；
- `EP-SCENARIO-04=PARTIAL`不是current runtime evidence；
- W006签发不等于Phase0、EP或action已执行。

## 下一次更新触发

仅在新的W006正式Return被原E1消费后更新。W006必须使用独立root、fresh binding/lock、分层静态准备与单次R0-A1；W005冻结不重开。若W006 STOP，保留独立成功子事实，不把未发生项补成PASS。
