# D001｜Asset and Binding Assessment

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> 评估时点：C0003 首轮专业执行  
> 当前材料状态：**PLAN_READY**  
> 当前 D 状态：**IN_PROGRESS；等待 W001 真实 Linux 回报**

## 1. 结论先行

目前只能确认：

1. Owner 的 Linux/GitHub grant、Run 逻辑绑定、D001 与 C0003 运输身份有效；
2. 指定需求、TIS 旧源码、FRP 旧源码可读，并足以形成处理骨架和 WORKING 预期；
3. W001 已按“只读核验、无重算”发布正式 ORDER 原件；
4. 真实 `/dwdhome/fy/BASE_E6_2` checkout、当前 HEAD/dirty、现役参数、generated wrapper、DBA/receipt/fields、三路输出、active-map/state trace、真实读取入口和成本**尚未由 Worker Return 证明**。

因此：

```text
旧源码可读        ≠ 当前现役 tuple 已核实
历史报告存在      ≠ 当前物化数据可复用
ORDER 已发布      ≠ Worker 已收到/执行
文件可能存在      ≠ 可解码
可解码            ≠ 足以回答本轮业务问题
```

不得填写 `DATA_READY`。

## 2. 授权与逻辑绑定

| 项目 | 已核事实 | 证据 | 状态 |
|---|---|---|---|
| Owner GO | 本 Run 目标为对 `EawP1WallLifecycleFrp` 开展观察材料准备和业务合理性分析 | `daowei2026/observe-iterate@9188847b057f1e39dd210a80862f6af358b617a9:longrun/runs/OI-EAW-WALL-20261114-01/OWNER_START.md` | VERIFIED |
| Linux grant | `operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01` | 同上、`RUN_BINDING.json` | VERIFIED AS TEXT; PHYSICAL ACCESS PENDING |
| GitHub grant | Run 分支/目录写面 | 同上 | VERIFIED；本 C 已实际发布 Run 文件 |
| executor | `chatgpt:OI-EAW-WALL-20261114-01:executor:E1` | `RUN_BINDING.json`、C0003 invocation | VERIFIED |
| Worker logical identity | `codex:OI-EAW-WALL-20261114-01:worker:W1` | `RUN_BINDING.json` | VERIFIED LOGICAL ONLY |
| Worker physical thread/cwd/model | 请求 `GPT-6.1 Sol Max`、cwd `/dwdhome/fy/BASE_E6_2` | W001 要求主控核真 | NOT YET VERIFIED |
| 单写者 | 必须由主控派 W 前独立核实 | V2 协议/W001 | NOT YET VERIFIED |

## 3. 已核 Source Baseline

### 3.1 需求/业务范围

已读：

- `feature-refinement-implementation-agent-evolution@8d58.../01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`
- 同提交 `02_FINAL_P1_ARCHITECTURE.md`
- 同提交 `dsu/P1-DSU-01_Wall_生命周期_DSU.md`
- 同提交 `tables/PYTHON_PROJECTION_TABLES.csv`

可以稳定保留的范围：

- Wall 是六个独立 P1 Feature 之一；
- WallLifecycleDSU 只维护 producer 已认出的 run-local Wall；
- identity 由 exact run scope + local no 解释；
- 输出角色为 occurrences/current view/diagnostics；
- 不做 source correction、跨运行 matching 或 P1 总聚合。

### 3.2 TIS 旧阅读基线

`daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3`

已确认文本：

- `EawBattleP.py` 中 ingress 是 `OnlyRead`；`_CalculatedP1Product` 报 `Cache`；直接 `to_df()` 被禁止并提示读 materialized public products；
- `WallAssembler` 旧实现能产出 receipt、packed sparse events、tick-aligned state trace、chunk meta/carry/summary/checkpoint；
- sparse event code 4/5/6/7 分别对应 Start/BandUpdate/StateChange/End；
- receipt 包含参数、source scope、code fingerprint 和 state-trace capability。

未证明：BASE 当前就是这个 commit、这些文件已实际运行、数据仍在、正式 reader 可用。

### 3.3 FRP 旧阅读基线

`daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`

已确认文本：

- `EawP1WallLifecycleFrp` FaoMeta 在该 SHA 报 `Cal`，与旧 TIS product wrapper 的 `Cache` 构成需要实际组合核实的差异；
- `WallOccurrenceFao` 只读 receipt+DBA，packed row 转 typed occurrence；
- lifecycle transition、transaction、active map、current update 与 diagnostics 的具体控制流；
- writer 键名和 current update 口径；
- compact-local-v2 occurrence ref 物理断点。

未证明：当前生成类/注册/DBA 与该 SHA 同版，或旧 cache 可由现行 decoder 读取。

## 4. 资产资格分层

| 层级 | 定义 | 当前情况 |
|---|---|---|
| `SOURCE_BASELINE_VERIFIED` | 精确 Git ref 的需求/源码文本已读 | 达到 |
| `CURRENT_CHECKOUT_VERIFIED` | Linux repo/worktree/HEAD/dirty 与相关文件 hash 已核 | 未达到，W001 |
| `CURRENT_CONFIG_VERIFIED` | 实际参数、target/calendar/time/source scope/CalType 已核 | 未达到，W001 |
| `ASSET_EXISTS` | receipt/fields/DBA/三路表/trace 在实际路径存在 | 未达到，W001 |
| `ASSET_DECODABLE` | 当前 reader 对 schema/version/path 读取成功 | 未达到 |
| `ASSET_IDENTITY_COMPLETE` | 可恢复 exact run identity、local no、时间和参数 | 未达到 |
| `MATERIAL_PURPOSE_SUITABLE` | 足以对账 sparse input、O/C/A/D 和反例 | 未达到，由 E1 在 Worker 回报后判断 |
| `DATA_READY` | 本轮必需材料真实取得并通过质量核验 | 未达到 |

## 5. 候选资产与复用资格

### 5.1 旧 GitHub 源码

资格：`SOURCE_BASELINE_VERIFIED`。  
用途：形成处理骨架、字段/reader 查找路径、反例和 W001 定向问题。  
不可承担：现役版本证明、数据存在证明、真实行为结论。

### 5.2 历史 real-data feedback 报告

已知历史目录曾记录：

- P1 四产品短窗口 writer→第二次 load 的历史结果；
- Wall 长跨度 writer 内存/物理布局问题及后续修正；
- occurrence identity/长 Text/物理合同等后续接缝问题。

资格：`HISTORICAL_CANDIDATE_ONLY`。  
原因：历史报告不等于当前 BASE 的目录、tuple 或数据；其中一些物理合同后来有断点。只有 W001 找到精确 artifact、receipt、schema/code、reader 并对齐后，才可能局部复用。

### 5.3 既有 EAW 看板/CAEGraph

Feature context 已指出 T056/T059 等 BP 图是下游 `EawBattleP` 观察，不是 WallLifecycle 的三路输出材料。  
资格：`NOT_ELIGIBLE_AS_WALL_EVIDENCE`；最多借技术组织方式，不能冒充本轮数据。

### 5.4 当前 Run 资产

- W001 ORDER MD：`daowei2026/observe-iterate@db0487b03bd81c6393639ac02ffe6534874dc80d:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W001/ORDER.md`
- W001 ORDER JSON：`daowei2026/observe-iterate@ad20770c69bc431d2e9188dcecd89883bce20cfa:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W001/ORDER.json`

资格：`ORDER_PUBLISHED`。  
目前没有主控物理发送回执、Worker receipt 或 `WORKER_RETURN`；不得写成 `EXECUTED`。

## 6. 当前需要由 W001 查明的绑定

### 6.1 工作区/仓库

- 实际 `pwd`、repo root、worktree、branch/detached、HEAD 40位 SHA、dirty；
- 当前 TIS/FRP/相关需求仓是否在 BASE，是否有多个 checkout；
- 相关文件 hash 与旧 baseline 的限定差异；
- 共享工作区单写者。

### 6.2 运行/配置

- `EawP1WallLifecycleFrp`、`WallOccurrenceFao`、`WallAssembler` 当前注册；
- `Cal/Cache/OnlyRead` 的真实组合；
- parameter set、target、calendar、time range、source scope；
- generated wrapper、FrpDbaDao/DBA/public product reader；
- `to_df` 限制在现役组合中的实际含义。

### 6.3 物化/数据

- `p1_receipts/wall_lifecycle.json`、`fields.json`、DBA result keys；
- WallAssembler sparse events/state trace/manifest；
- `wall_occurrences`、`wall_current_view`、`wall_diagnostics`；
- 文件/分区数量、大小、mtime、范围、schema/code/params；
- 当前 reader 是否低成本可解码；
- 是否存在一条真实正常链。

## 7. 关键风险与核验动作

| 风险 | 为什么重要 | 当前动作 |
|---|---|---|
| 旧 SHA 与当前 checkout 不同 | 静态反例可能已修或另有变化 | W001 记录 HEAD/blob/diff；E1 只按相符范围消费 |
| TIS `Cache` 与 FRP `Cal` 表面不一致 | 可能只是跨语言职责差异，也可能影响读取入口 | 定位 generated wrapper/FaoMeta/实际 reader；不靠名字下结论 |
| compact-local-v2 物理断点 | 老 cache 可能不能被新 decoder 静默复用 | receipt/schema/code 必须先过；不强行双轨读取 |
| current update 被当全量快照 | 会误判无行、End 和 active membership | 必须取得 active map/state trace或可验证重放 |
| local no 脱离 receipt | 会跨 run 错连 Wall | 样本包强制附 exact run identity |
| reader 隐式触发重算/写入 | 可能越权、耗时、污染现役目录 | W001 静态/metadata 优先；未知副作用立即停 |
| 大范围 writer/DBA 内存成本 | 历史已有风险线索 | 禁止全年重算；无资产只做 ActionPreflight |
| diagnostics 空被当正确 | 异常可能根本未发生 | 空 D 只说明已核范围未观察到 diagnostic |
| End terminality/跨 firing dedup 静态疑点 | 可能影响同一 Wall 身份完整性 | current code + producer invariant + 定向 fixture/样本分层核验 |
| 同 firing 整批拒绝 | 可能是业务原子性，也可能是物理同拍放大损失 | 先查 firing formation，再决定业务判断 |

## 8. Action Eligibility

| 动作 | 当前资格 | 说明 |
|---|---|---|
| GitHub 需求/源码只读分析 | ELIGIBLE / 已执行 | D001 授权范围内 |
| 发布 Run 结果/工单 | ELIGIBLE / 已执行 | 仅 Run branch/path |
| Linux 只读资产核验 | ELIGIBLE，待主控派 W | W001 已收窄操作和写面 |
| 读取现有低成本 metadata/局部分区 | 条件 ELIGIBLE | 由 W001 在无副作用、无大加载前提执行 |
| 实际短窗重跑 | **NOT ELIGIBLE YET** | 需无材料后的 ActionPreflight + manager/G-RUN 决定 |
| 全年/全品种重算 | NOT ELIGIBLE | D001 明确禁止 |
| 修改 TIS/FRP/reader/schema | NOT AUTHORIZED | 本 D 只调查与分析 |
| expectation freeze/正式对照 | NOT ELIGIBLE YET | 真实材料和 manager Gate 未满足 |

## 9. 接收 W001 后的专业消费规则

E1 不会把 Worker 的 `EXECUTED` 自动转成 `DATA_READY`。逐项检查：

1. 真实 checkout 与旧 baseline 对齐到哪些文件/语义；
2. asset 是“存在”还是“可解码”；
3. identity/time/version 是否完整；
4. reader 是否重算/二次处理；
5. sample 是否真实、局部、可复现；
6. O/C/A/D 是否能按 firing+identity 对账；
7. 缺失项限制哪个问题；
8. 是否需要 ActionPreflight，而不是直接运行。

然后把 D001 状态更新为真实的 `DATA_READY`、`PARTIAL_WITH_LIMITS`、`BLOCKED` 或继续 `PLAN_READY`。

## 10. 当前准确状态

```text
Source baseline:        VERIFIED at specified old refs
Linux current checkout: UNKNOWN
Current config/binding: UNKNOWN
Materialized assets:    UNKNOWN
Reader/decodability:    UNKNOWN
Real sample:            NOT OBTAINED
W001 order:             PUBLISHED, NOT YET ACCEPTED/EXECUTED
Material status:        PLAN_READY
Professional D state:   IN_PROGRESS
```
