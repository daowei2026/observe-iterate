# D003｜C0012 EP Acceptance Matrix

> basis：W002 limited STOP acceptance + W003 formal STOP professional review  
> status vocabulary：`SATISFIED / PARTIAL / UNSATISFIED / NOT_ATTEMPTED`  
> action evidence：**none**；本表不通过 `G-RUN`，不形成 H3。

| EP | C0012 E1 状态 | 当前可接受证据 | 当前缺口 | 阻断关系 | 最小解除条件 |
|---|---|---|---|---|---|
| `EP-WALL-SHARED-01` read-only lifecycle state snapshot | **NOT_ATTEMPTED** | exact current source字段与D002合同可读 | 无snapshot/accessor、patch、typecheck、只读性质测试 | 阻断真实A observation和transaction trace；不阻断Phase0恢复 | 四PASS后在clean staged source构造并有限验证 |
| `EP-WALL-SHARED-02` structured one-record-per-firing evidence schema | **NOT_ATTEMPTED** | 字段、ordering、error、pre/post合同已书面定义 | 无DTO/schema、canonical bytes、roundtrip、stable hash | 阻断structured scenario evidence；不阻断Phase0恢复 | 四PASS后构造；仅synthetic serialization，不运行scenario |
| `EP-WALL-SHARED-03` isolated clean build closure | **UNSATISFIED** | W002确定closure/cap/zero-write未证；W003精确定位pre-policy fd0 wiring failure并提供failed-launch trace | kernel confinement未通过；single offline closure未证；四预算和continuous monitors未证 | **Phase0 hard blocker** | 新W4以read-only fd0+preconfirmed sentinel完成R0-A；随后独立完成R0-B/C，四PASS同时成立 |
| `EP-SCENARIO-01` dedicated scenario target | **NOT_ATTEMPTED** | target名称、接口、禁令已冻结 | 无component/main/manifest/patch/compile-only | 依赖SHARED-01/02/03 | 四PASS后staged construction；fixture不得执行 |
| `EP-SCENARIO-02` exact error assertions | **NOT_ATTEMPTED** | exact constructors和需要区分的ingress/state类别已定位 | 无adapter、constructor/payload schema、synthetic serialization | 依赖SHARED-02和target | 四PASS后构造direct synthetic records；不得用generic Left |
| `EP-SCENARIO-03` transaction trace integrity | **NOT_ATTEMPTED** | apply/partition/commit边界静态路径可读 | 无DTO、pre/post A、committed/uncommitted区分验证 | 依赖SHARED-01/02和target | 四PASS后构造；rejected formal post=pre，O/C空，仅synthetic验证 |
| `EP-SCENARIO-04` existing test-contract conflict ledger | **PARTIAL** | W002 exact commit/function/line ledger；C0010已接受为静态子集；W003未修改或反证 | dedicated target manifest未引用；无actual result；未决定implementation vs old test | 不阻断Phase0；不能单独解锁action | 未来target manifest逐项引用原ledger并保留unresolved choice |
| `EP-SCENARIO-05` fixture schema and provenance | **NOT_ATTEMPTED** | 9 scenario/18 firing/22 input合同存在 | 无物化schema/input/hash/static parse-count-order验证 | 不阻断Phase0；阻断target readiness | 四PASS后物化，只做static validation，scenario run=0 |

## 汇总

```text
SATISFIED      = 0
PARTIAL        = 1
UNSATISFIED    = 1
NOT_ATTEMPTED  = 6
W003 new EP satisfied = 0
```

## W003 新增但不属于 EP-PASS 的工程事实

1. 原 W1／fresh W003 binding、lock与actual HOME/CODEX_HOME已核；
2. W003 launcher在policy前fail-closed；
3. `subprocess.DEVNULL → O_RDWR /dev/null` 是直接integration cause；
4. 失败launcher完整trace中唯一successful write为W003 receipt；
5. 没有调用NNP/Landlock/seccomp，没有probe/child/scenario/compile/serialization；
6. 这些事实只支持精确后继设计，不升级任何EP。

## 禁止误读

- fail-closed inherited-FD guard **不等于** confinement；
- failed trace内outside writes 0 **不等于** global zero writes；
- Landlock未被调用 **不等于** kernel不支持；
- fixture合同文本 **不等于** fixture artifact；
- `EP-SCENARIO-04=PARTIAL` **不等于** current behavior实测；
- W004签发 **不等于** Phase0、EP或action已执行。

## 下一次更新触发

仅在新的W004正式Return被原E1消费后更新。W004必须使用独立root/lock/资格；W003不重开。若W004再STOP，按直接证据保留独立成功子项，但不得把未发生项补成PASS。
