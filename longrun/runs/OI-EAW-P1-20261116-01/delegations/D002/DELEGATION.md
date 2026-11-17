# D002｜EAW P1 正式比较定向补证与 EvidencePreflight

## 0. 正式身份

- `run_id`：`OI-EAW-P1-20261116-01`
- `delegation_id`：`D002`
- `issuer_call_id`：`C0005`
- `issuer`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `recipient`：`chatgpt:OI-EAW-P1-20261116-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-P1-20261116-01:manager`
- `work_item_id`：`WI-D002-P1-R2-EVIDENCE`
- `stage_instance_id`：`M-P1-EVIDENCE-002`
- `origin_analysis_round_id`：`AR-P1-001`
- `frozen_expectation_set_id`：`FZ-EAW-P1-AR-P1-001`

本 D 只有在主控真实派发并核实 E1 物理接收后才开始。它是 D001 后的 H2 定向补证，不是 D001 返工，不是正式 R2，也不改变 D001 `issuer_call_id=C0001`。

## 1. 当前业务问题及下游消费者

### Q-EAW-P1-COVERAGE-001

补齐或有据关闭当前 Project Source 的 run provenance、产品 identity/time/availability 和 direct-product availability，使 manager 能判断哪些产品/场景真正具备正式 R2 输入资格。

### Q-EAW-P1-REASONABLENESS-001

在冻结预期不变的前提下，为后续正式对照准备 EvidencePreflight；本 D 不作 `SUPPORTS/COUNTERS`。

### 下游消费者

- H2 EVIDENCE-RETURN；
- manager 对正式 R2 D 的签发判断；
- Integrated Core Wave 与 Direct-Product Wave 的产品级输入资格；
- 后续 Q-EAW-P1-BOUNDARY-001 的可答/不可得边界。

## 2. 已接受上游结果

1. D001 WorkQuality 已被 manager 接收；不重做其 ProcessingSkeleton、覆盖矩阵、数据审计或 R0/R1。
2. H1 已按用途 `ACCEPTED_WITH_LIMITS`：当前材料可用于探索和补证，不能直接正式比较。
3. `G-EXPECTATION-FREEZE` 已通过本 Run v1：
   `daowei2026/observe-iterate@c88c4836269e8412e88e9ea6e7e871c0ad44f96e:longrun/runs/OI-EAW-P1-20261116-01/business_control/frozen_expectations/FZ-EAW-P1-AR-P1-001.yaml`
4. manager 决定：
   `daowei2026/observe-iterate@0e5387bbac5f09b3e0da63a407943b88f101a36a:longrun/runs/OI-EAW-P1-20261116-01/business_control/decisions/MD-0002.md`
5. `G-COMPARISON` 尚未满足；本 D 的结果用于决定是否解锁，而不是自行宣布解锁。

## 3. 必须亲自使用的专业输入

- D001 原报告：
  `daowei2026/observe-iterate@3d3b3b9c568f9b17037b747fc1ca44a76f847ddf:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/EXECUTOR_REPORT.md`
- D001 数据审计：
  `daowei2026/observe-iterate@624dd0dfb2deed97bf57c573ccbd63f9f636b6d7:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/D001_DATA_AUDIT.json`
- D001 WORKING 预期与场景源：
  `daowei2026/observe-iterate@0fff57bcc2cb85907586704a67389c038cf5ffa3:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/D001_EXPECTATION_REGISTER.yaml`
- 本次 manager 复审：
  `daowei2026/observe-iterate@21e2640a3574c2911592f8e9fcf24b3e97e42452:longrun/runs/OI-EAW-P1-20261116-01/calls/C0005/MANAGER_REPORT.md`
- 固定方法提交 `7e240b650b6ba6274b0263e34f5b0616a9a8ff1c`：
  - `control/02_L1_观察材料准备流程.md`
  - `control/03_L1_合理性分析流程.md`
  - `control/05_三级Gate及后继路由.md`
  - `skills/reasonableness-analysis/business-evidence-comparison/SKILL.md`
  - `longrun/professional/PRO_EXECUTOR_GUIDE.md`
- 原 Owner GO、RUN_BINDING、资源绑定、固定脚本/数据清单仍有效。

冻结集合中的命题文本和场景不可在本 D 中无痕改写。新事实若真正要求改变预期，只能提出新候选及理由，不能覆盖 v1。

## 4. 本次五项具名补证

## 4.1 AER-P1-001｜共同 provenance、DataBinding 和 availability

必须定向寻找并核验：

- 产生当前 Project Source 的 source run / run id；
- producer code commit、config、参数、输入数据版本；
- object universe、calendar、session、time basis；
- source_run_ref 或可构造其稳定范围的原始依据；
- typed product/occurrence identity 的真实实现或缺失事实；
- availability/missingness：valid activity、valid no activity、source missing、stale、session invalid、calculation unavailable、insufficient history、pending；
- 6 个 30m 窗和前 30 个 Tick 窗的选择规则或有据不可得结论。

### 最低合格返回

按每项给出：`OBTAINED / PARTIAL / PROVEN_UNAVAILABLE / BLOCKED`、实际查找范围、固定来源、版本/哈希及对哪些产品/场景的影响。

不得自行发明 `source_run_ref` 或用当前文件路径替代真正 provenance。

## 4.2 AER-P1-002｜AttackSegment complete occurrence 与时间合同

核实：

- 当前 Attack 表的真正 producer/export path；
- `start_uti`、`business_end_uti`、`closed_at`、`ts/business_end_ts/plot_uti` 的定义；
- 10,115/17,856 行时间绑定不一致的原因；
- `i` 五行 -21,600.5 秒 session-boundary offset 的原因；
- complete/incomplete、technical truncation、closure reason 是否存在；
- 是否已有 corrected complete export。

### 允许与禁止

- 允许取得现有 producer 正式导出或运行已有、低成本、非破坏性的固定 export；
- 允许建立“审计用纠错视图”帮助定位，但必须标作 review-only；
- 禁止把 executor 自行推断的时间映射冒充 producer corrected export；
- 需要修改业务源码或宽泛上游重算时停止并返回准确条件。

## 4.3 AER-P1-003｜canonical F4 union

核实：

- 是否存在 canonical DirectedBigDeal/F4 producer output；
- occurrence identity、source_run_ref、direction、UTI、lane_mask、tactical_grade、structural_grade；
- tactical/structural overlap 的官方 union/dedup policy；
- availability/capability 和 threshold/context audit；
- 当前两条 lane 表在生产链中的真实阶段。

可以生成 review-only union 以验证重合数量和字段一致性，但不得把一次性 union 宣布为 canonical producer output。若正式 union 不存在，必须有据返回 `PROVEN_UNAVAILABLE` 或明确需要的合法后继。

## 4.4 AER-P1-004｜FormationEvidence、Barrier、F3 direct products

对三类产品分别核：

- producer/module/export 的实际存在与版本；
- 当前 frozen source run 是否生成；
- direct product 文件/表/typed port；
- capability/availability；
- identity、actual/confirm/close time；
- 若不存在，调查到何处后可证明当前 run 不可得；
- latent 字段或图层为何不能替代 direct product。

不得：

- 把 Attack/F4 latent 字段重命名为 FormationEvidence；
- 从 Wall 迁移图形自行造 formal Barrier；
- 把旧 Thick/Dense/Fight 图证据重命名为 F3。

## 4.5 AER-P1-005｜Absorb milestone 与 identity

核实：

- Started→Milestone*→Resolved 的真实 producer identity；
- 同 UTI 多行是否对应不同 threshold/level；
- `occurrence_ordinal` 的语义；
- 5,534 个 resolve-only track 的形成原因；
- `wall_local_no=0` 的业务/技术语义；
- 是否有 typed interaction_ref、wall_ref、reason/time 和 capability 声明。

禁止在 identity 未明前把 25,821 行业务等价 payload 多票计数。

## 5. EvidencePreflight

将 AER 结果逐项映射到冻结集合和 14 个场景，但不作正式效果判断。

至少形成表：

```text
expectation_id / scenario_id
product
required evidence
actual evidence ref
validity
business meaning clarity
purpose suitability for formal R2
status: ELIGIBLE / PARTIAL / PROVEN_UNAVAILABLE / BLOCKED
remaining limitation
```

三层必须分开：

1. 数据/文件/字段是否有效；
2. 它在业务上代表什么；
3. 它是否适合本次正式比较目的。

同源证据和 derived view 不得重复计为多个独立 evidence source。

## 6. 操作、Worker 与写面

D002 可零 W；确需 Linux 现场时，E1 可在本 D 内签 W 给本 Run 专用 Worker。

### 允许下放

- 在 `/dwdhome/fy/BASE_E6_2` 定向查找现有代码、配置、日志、manifest、导出和数据；
- 哈希、列目录、读取小样、字段/身份/时间审计；
- 运行现有低成本、非破坏性、范围明确的只读/导出/检查命令；
- 在本 Run 独立目录保存日志、清单和 review-only 派生审计材料；
- 由 Worker 回 E1，再由 E1 专业消费。

### 禁止下放或执行

- 决定业务预期或修改冻结集合；
- 正式 `SUPPORTS/COUNTERS`；
- 修改业务源码；
- 宽泛上游重算或无预算长跑；
- 生成无 producer authority 的“正式产品”；
- 写到 `/dwdhome/fy/BASE_E6_2` 和本 Run GitHub 路径之外；
- 绕过 E1 直接向 manager 交专业结论。

### Worker 首次使用

主控须按 V2 核本 Run 专用物理 thread、cwd、授权、模型配置和真实文件可达性。E1 只能在合法绑定后签 W，manager 不直接签 W。

## 7. 成功、部分、不可得和阻断的专业回交

### 成功取得

提交固定来源、版本/哈希、审计结果和 preflight；不要仅说“找到文件”。

### 部分取得

保留已得结果，说明只阻断哪些 expectation/scenario/product；其他产品继续具备独立资格。

### PROVEN_UNAVAILABLE

说明调查范围、为何足以关闭当前请求、能形成的限域结论和不再循环查找的条件。不可得是合格 H2 结果，不是专业失败。

### BLOCKED

只有真实权限、物理访问、需要 Owner 改目标或必须进行未授权高影响动作时使用；写明解除条件。普通缺文件、缺字段或实现不存在优先用 `PROVEN_UNAVAILABLE/PARTIAL`。

### 新预期

若新事实产生不同业务预期，只登记候选、来源和影响；不得把其加入已冻结 v1 或用于本轮正式比较，等 manager 另行决定。

## 8. 明确非目标

本 D 不做：

- D001 返工；
- 正式 R2 `SUPPORTS/COUNTERS`；
- R3 根因诊断；
- R4 参数标定；
- 新 CAEGraph 设计；
- 全量上游重算；
- 业务源码修改；
- permanent Owner requirement 决定；
- P2/P3/P4；
- 最终策略或资金动作；
- AER-P1-006 `run.py --check`，除非它是某个已签 W 的附带低成本事实，且不得将其当产品证据。

## 9. 预期交付物

1. `D002_EVIDENCE_RETURN.md`：按 AER-P1-001～005 逐项报告；
2. `D002_EVIDENCE_AUDIT.json`：机器可读来源、版本、状态和产品映射；
3. `D002_R2_PREFLIGHT.yaml`：逐 expectation/scenario 的正式 R2 输入资格；
4. 如有 review-only 派生表，提供哈希、生成命令、输入 refs，并显式标 `NOT_CANONICAL_PRODUCT`；
5. 如有 W，提交正式 W、Worker Return 和 E1 接受意见；
6. 符合 V2 的 executor `PRO_RETURN.json`。

## 10. 正式回交要求

- 先发布专业报告、审计、preflight 和实际 W/结果，再发布 executor Return；
- `delegation_ref` 必须引用 D002 `DELEGATION.json` 的精确 commit/path；
- `return_to=chatgpt:OI-EAW-P1-20261116-01:manager`；
- D002 报告范围完成时可用 `REPORTED_COMPLETE`，即使部分证据为 `PROVEN_UNAVAILABLE`；这不表示 H2 已被 manager 接受或父任务完成；
- 完成态 Return 不登记 manager 后继为 E1 的 remaining/continuation；
- 不新增旧 ROLE_RETURN/FPA 字段；
- 回报准确 commit 和路径。