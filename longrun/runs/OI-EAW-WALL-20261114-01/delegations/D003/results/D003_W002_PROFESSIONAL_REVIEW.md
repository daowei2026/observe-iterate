# D003｜W002 STOP 专业消费与接受范围

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D003`  
> `call_id`：`C0010`  
> executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`  
> reviewed Worker Return：`daowei2026/observe-iterate@9bce93fcd7bbd0c91a08c0ace86b332e55b9f629:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W002/WORKER_RETURN.json`  
> professional decision：**ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS**  
> D003 state after review：**IN_PROGRESS**

## 1. 运输与原件核验

主控已对 W002 正式 Return、299 份冻结原件、309 项 manifest 映射、hash、V2 schema 和 return-to 路由完成独立机械核验。本轮 E1 接受以下运输事实：

- `work_order_id=W002`；
- Worker 为绑定批准的 W1；
- Return 只回原 E1；
- `outcome=STOP`；
- `decision=PREFLIGHT_STOP`；
- 正式结果 commit 为 `2af8a364b4157958b59d68ab4fc24eb6a95f5593`；
- W002 的本地锁和写者已经终止、资源锁释放；
- Return 原文里“待发布正式 Return”的记录属于冻结时点历史，现已由 commit `9bce93f...` 解决；这只消除运输待办，不消除工程缺口。

E1 没有把主控的机械 Gate 通过解释成 EP 专业接受。

## 2. W002 STOP 是否有效

结论：**有效，且必须保留。**

W002 严格执行了原 ORDER 的 Phase-0 Gate。三类硬停止都具有直接证据：

1. `STOP-CLOSURE-001`：exact FRP stack 与 BASE overlay 使用不同 resolver/local-package 声明，兼容离线 compiler/resolver/package DB 与最小 rebuild closure 未冻结；
2. `STOP-CAP-001`：未来工程的 disk、peak RSS、post-preflight wall、new-files 四项预测均为 unknown；原合同规定任一 unknown 即 STOP；
3. `STOP-WRITE-001`：两次 bwrap probe 失败；Haskell 元数据进程有 9 次成功 `O_RDWR` 打开 `/proc/self/task/*/comm`，但原 trace 没覆盖后续 write-family；因此不能证明实际写入，也不能证明零外写，`writes_outside_WORK_ROOT=unknown`。

Phase 1 staging 与 Phase 2 compile/serialization 均未进入。没有 patch、fixture、local commit、compile、serialization、单个或九场景运行。停止没有破坏 D003 禁令，也没有以假空文件补合同。

## 3. 可以专业接受的事实子集

### 3.1 Binding 与 source baseline

接受：

- 实际 W002 thread/model/effort/cwd 与 single-writer 事实；
- Owner literal grant 与 D003/W002 实际子根的分层；
- exact FRP base `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`、tree `66c53649915731c4665536ad810823f50e4749d9`；
- 八个指定 source/test/build blob 的 exact hash；
- 15 个具名 local-package root 的 repo/HEAD/cabal 声明清单；
- exact stack 为 lts-18.28，BASE overlay 为 lts-22.24，现场 GHC 为 9.4.8；
- 这些事实只说明存在两套候选环境，不能拼成一个兼容闭包。

### 3.2 具名共享路径未改

接受到明确覆盖边界：

- FRP/TIS/worker 的 HEAD、branch、status；
- W002 指定的 source/build declaration、既有 dirty、wrapper、index/HEAD 文件 hash/mtime；
- before/after 在这些具名项目上相等；
- `shared_checkout_changed_by_W002=false` 在上述命名覆盖范围内成立。

不外推为全盘零写或所有生产目录零变化。

### 3.3 Static contract conflict ledger

接受为 `EP-SCENARIO-04` 的可审查静态子集：

- 旧 test 的 cross-firing Start replay 期待幂等；
- current firing-local ledger 静态预测 `WallStartedTwice`；
- after-End test 只确认任意 `Left`，不能区分 before-start/after-end；
- ingress/state transaction 边界和 exact error 必须分开；
- exact commit、函数和行号均有来源。

它不是 current runtime evidence，也没有决定修改 implementation 还是旧 test。

### 3.4 禁止项遵守

接受：

```text
scenario evidence fixture runs = 0
normal runs                    = 0
DBA/wrapper/native reader      = 0
network downloads              = 0
dependency installs            = 0
source repo pushes             = 0
```

## 4. 不能接受或不能上调的事项

### 4.1 零外写

`writes_outside_WORK_ROOT=unknown` 必须原样保留。

- 9 次 `O_RDWR` open 不能证明实际 write；
- 未捕获 write-family 也不能证明零 write；
- `/m3varK`、production product 的全流程零写仍为 unknown；
- 命名共享路径 before/after相等不能替代全局 confinement。

因此 `EP-WALL-SHARED-03=UNSATISFIED`。

### 4.2 离线 closure 与成本

不能接受：

- exact stack 与 BASE overlay 兼容；
- transitive Hackage/local-package closure 已闭合；
- 最小 target 可离线编译；
- disk/RSS/wall/files 任一预算已知或在 cap 内。

版本查询、浅层 cache index 和 22 条逻辑输入规模都不能作为 build 预算。

### 4.3 八项 EP

除 `EP-SCENARIO-04` 的静态台账子集外，W002 没有构造或验证任何 EP。E1 不接受：

- snapshot accessor；
- evidence DTO/schema；
- isolated build closure；
- dedicated target；
- exact-error adapter；
- transaction DTO；
- complete 9/18/22 fixture；
- patch/local commit/compile/serialization。

### 4.4 current business evidence

静态 source、schema 文档、版本命令和 conflict ledger 均不构成 current O/C/A/D、terminal/replay/atomicity/late 业务 evidence。`G-RUN`、H3 和三个父 Q 均不因 W002 改变。

## 5. 对 W002 的处理决定

```text
Accept formal W002 Return:                  YES
Accept STOP/PREFLIGHT_STOP decision:         YES
Accept exact source/binding/static facts:    YES, scoped
Accept EP-SCENARIO-04 static subset:         YES, PARTIAL
Accept EP-WALL-SHARED-03:                    NO, UNSATISFIED
Accept any other EP as constructed:          NO
Rework/reopen W002:                          NO
Republish/fill fake missing artifacts:       NO
```

W002 已封存，不重发、不覆盖、不要求补造空 patch/fixture。

## 6. 后继专业判断

局部 STOP 不等于 D003 或父任务结束，但原 Phase-0 blocker 不能靠放宽 cap 或改写 unknown 绕过。合法后继必须同时满足：

1. 使用新的唯一 W 和新的实际子根；
2. 不重复 W002 的 bwrap 探针和未覆盖 write-family 的审计方式；
3. 先构造并验证真正的 write confinement／全子进程写审计；
4. 冻结一套兼容、完全离线的 compiler/resolver/package DB closure；
5. 为 disk/RSS/wall/files 给非空、有依据、可持续监测的预测；
6. 三类 blocker 全部解除后才可 staged construction；
7. caps 与九场景／normal／DBA／wrapper／native-reader禁令保持不变。

C0010 因此签发独立的 `W003`，先解除 Phase-0 三类 blocker，并在全部通过时才条件性继续 D003 八 EP。W003 不是 W002 重跑，也不继承 W002 的锁、thread 或执行资格。

## 7. 当前准确状态

```text
D003 professional state:          IN_PROGRESS
accepted_worker_refs:             W002 formal Return
W002 professional disposition:    ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
W002 EP result:                   1 PARTIAL static subset / 1 UNSATISFIED / 6 NOT_ATTEMPTED
G-RUN:                            NOT PASSED
H3:                               NOT AVAILABLE
parent questions:                 OPEN
parent task completion:           NOT CLAIMED
```
