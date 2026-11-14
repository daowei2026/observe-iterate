# W003 本地 EP 事实矩阵

本 W 在 R0-A 的继承 fd 检查失败，未进入 R0-B/C 或 Phase1/2。以下“继承 E1 状态”仅引用只读 C0010 专业矩阵，不代表 Worker 对专业接受的决定，也不是 W003 当前生命周期实测。

| EP | 继承 E1 状态 | W003 新工程事实 | 当前缺口 |
|---|---|---|---|
| EP-WALL-SHARED-01 | NOT_ATTEMPTED | 未构造 accessor/snapshot | 无 patch、typecheck/read-only test |
| EP-WALL-SHARED-02 | NOT_ATTEMPTED | 未构造 DTO/schema | 无 canonical order、roundtrip/stable hash |
| EP-WALL-SHARED-03 | UNSATISFIED | 新 R0-A launcher 在安装 policy 前拒绝 writable fd0，exit73；保留完整 trace | confinement 未通过；closure、预算和持续监测仍无本 W 证明 |
| EP-SCENARIO-01 | NOT_ATTEMPTED | 无 dedicated target/manifest | Phase0 hard gate 未通过 |
| EP-SCENARIO-02 | NOT_ATTEMPTED | 未构造 exact-error serialization | 无 structured constructor/payload 验证 |
| EP-SCENARIO-03 | NOT_ATTEMPTED | 未构造 transaction DTO | 无 pre/post A 和 committed/uncommitted 验证 |
| EP-SCENARIO-04 | PARTIAL（旧静态子集） | 旧 ledger 只作为不可覆盖输入；无新 target | 未进入 target manifest；无 actual result |
| EP-SCENARIO-05 | NOT_ATTEMPTED | 未物化 9/18/22 fixture | 无完整 schema/input/static count/order/hash |

继承 E1 状态合计：SATISFIED=0，PARTIAL=1，UNSATISFIED=1，NOT_ATTEMPTED=6。W003 新满足的 EP=0。`scenario evidence runs=0`，compile-only=0，serialization=0。

来源：`input/mirrors/` 中逐字 C0010 `EP_ACCEPTANCE_MATRIX_C0010.md` 及 W002 frozen 输入；W003 的 `PHASE0_RECOVERY_VERDICT.json` 和 `FULL_WRITE_TRACE_REVIEW.json`。W002 原件不改，不据旧源码/旧证据替代当前实测，不判断 G-RUN 或父任务完成。
