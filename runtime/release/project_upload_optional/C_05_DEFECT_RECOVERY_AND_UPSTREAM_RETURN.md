<!--
canonical_source: agent_evolution/agent_candidates/mission-c-host-implementation-system-candidate-v0.2/canonical_methods/defect/AUTONOMOUS_FIX_ZONE_AND_STOP_GATES.md
source_parent_commit: b85af4a6578cf455a3da8884a999d98bd5fb1050
execution_revision: 2026-09-30-continuous-implementation
manual_edit: forbidden
-->

# 运行调查、预授权编译小修与 Pro 修复边界

execution_revision: '2026-09-30-continuous-implementation'
role: `current_instruction_bound_repair_method`

源码主体仍尽量由 Pro 编写，Codex 承担现场执行。正常构建单预先授予有界编译小修，避免逐处远端往返；只读任务保持只读。权限来自实际工作单，本方法不恢复旧问题族的泛化修源码许可。

## 1. 取得实际故障并按原因归并

Codex 按授权取确切代码／配置／数据／命令，保存实际错误、预期依据和最近正确结果。读完本次已有错误，再围绕共同原因检查当前文件和本批直接相关模块中的相同写法；不只处理日志第一行，也不扩成全仓扫描、警告清理或场景穷举。

日志提取、输入比较、隔离复现和结果整理程序可以在授权诊断位置制作，不替代正式计算、不改变正式 Feature、共享配置、业务值或正式测试预期。无输出沿实际输入、预热、调用、方法、状态和读回定位，不另算旁路结果。

## 2. 编译小修、重要工程与业务修订分流

正常构建工作单预先给清小修源码范围，可以包含本次用例直接相关的既有模块。正确写法能从现有类型、函数体和调用确定，且无需新增业务或重要工程选择的括号、语法、局部类型标注和唯一明确引用，工程师可集中修复并继续复编，无须逐行重新许可。

需要决定 Event／Dynamic 关系、重要接口、状态／存读布局、资源增长的结构性修法等，即使没有 Owner 业务取舍，也交 Pro 判断和主要编写。改变来源、身份、生命周期、业务时间、参数含义、缺值处理或正式产品承诺的，按相应专业责任处理。改动行数、小或等价不能单独决定分流。

其他用例、共享平台、明确保护面和未知接口不因报错获得写权。需要重要判断时，工程师集中交已确认原因、相关位置、已作修订和待判部分；Pro 处理共同原因及直接调用／消费者，不只修被点名的一处。信息不足交定向调查，普通技术问题不逐项交 Owner。

已授权小修的差分随原回交由 Pro／审查者复核，不逐 hunk 设置再次编译的事前独立放行。重要业务和工程修订仍按原独立审查；局部复编资格不升级为完整业务通过。

## 3. 连续复编、复验及返回原问题

当前合法工作区内可确定的小修完成后，工程师检查直接相关同类位置并复编。TIS／FRP 严格在 `edh-universe` 目录执行 `stack install`，禁止添加其他参数。一次构建失败不自动结束工作单、归还现场或重新等待派发；持续无新信息时交 Pro 定向判断，不要求保证全部潜在错误已找完。

编译／运行中不修改同一源码；写面仍只有一个活动写者。后继保留工程师已经完成的有效差分，不用 Pro 旧版本覆盖。应用补丁、执行生成、自行小修、源码发布和实际运行分别记录；纯执行无需源码提交，execution_commit 如实填写。

构建通过且正式路径／运行安排已给清，继续运行和读回。遇重要修法时只停受影响路径，不冲突工作继续。修后对相同问题与受影响关系复验，再接回原业务目的，例如 reader 修好后仍需完成对象演化分析；回传不算修复完成。

读取异常先追既有平台调用，不默认造 DTO／codec／serializer／sidecar；容量异常测实际阶段、活跃对象与增长，重要修法交 Pro，不自主改变回看、历史、频率或业务范围。测试和 proof 按实际问题安排，不由一个缺陷扩成全场景工程。
# 4. 直接停止门

以下情形不先写几百行试错，不以先跑通绕过。

## STOP-01：Business scope

删除/延期/降级mandatory Action或product；减少品种/pair/方向/产品族；缩正式历史/窗口；用milestone或blocker宣布campaign完成。回accepted contract/Pro/Owner。

## STOP-02：业务对象、state owner、identity、cardinality

新增/合并/拆分owner，改实例域/业务主语/去重粒度，引入第二identity或技术key取得业务身份，改变public/private权力。回合同细化及repo-aware工程，必要时Owner。

## STOP-03：lifecycle、finality、correction、history

改变开始/结束/恢复/reentry，删改append-only occurrence，改变correction/revision，决定历史清退或current覆盖正式历史。回合同/Owner。旧P2 F11/F14缺件仅按§8历史身份处理，不成为所有任务的自动阻断。

## STOP-04：business time、same-firing、read-old/read-new

+1ns排序、等未来同UTI callback、延下一真实occurrence、新settle microstep、callback/container次序取得业务权或ambient latest恢复时间。Pro核当前taskpack并亲修或作有理由的具体委派，Codex不自行改。

## STOP-05：正式 public product、writer、consumer 权力

新增/删除产品、改唯一writer、消费者重算生产者事实、旁路notebook/cache替正式链、改产品可空/版本/correction含义。回工程/业务合同/Owner。

## STOP-06：method／RulePack／semantic parameters

调阈值造输出、改RulePack词表、新fallback、missing/pending当0、方法版本变化而claim不变。回方法诊断/合同/Owner。

在现有方法范围和实际运行授权内，Pro可安排保留基线的定向参数对照，工程师执行。这与改变参数语义／合同、静默改阈值造结果分开；不做最终调优不能排除当前必要对照。

## STOP-07：共享平台或第二系统

修改Frame/frp-core/cfis，新增通用serializer/identity/receipt/registry，第二DBA/FIS backend/event bus/scheduler，下游替上游造元数据。RepoFact后Pro核窄问题与任务写面，不默认平台开发或同事本人审批。

## STOP-08：容量修复需要改变业务

为内存删历史、为文件量合并不同产品、为性能降频/缩pair、不再发布某类产品、为有界current改实例生命。回Capacity专项及合同/Owner。

## STOP-09：source gap／supersession unresolved

缺required accepted parent，事故让位的后续合同不可读，alias/Branch/Owner delta未解析，未锁code ref就判现状。先取来源，仅限制受影响结论。

## STOP-10：Owner explicit stop／unsafe or unknown scene

Owner明确叫停、写者或改动归属不明、正式输出污染、危险运行或未授权重型／破坏性操作，限制受影响路径并按INTERRUPTED_WORK_RECOVERY_REFERENCE.md处理。当前已知写者的授权施工脏改、未完成生成和一般编译／类型错误不自动冻结；按§1—§3分流，本修订不解除已有Owner暂停。

# 5. 有限自校与实施偏差回压

不按固定分钟、文件数、代码行数或重试次数，按工作性质判断。

## 5.1 有限自校与指令边界

工程师在本单预授权范围内集中处理可确定的编译小修及直接相关同类错误，连续复编后统一回交差分；重要工程／业务修法回Pro。Pro尽量亲写修订，工程师现场复验后回原业务问题。只读单不扩权，局部绿不升完整业务接受，纯执行无须源码提交。

## 5.2 实施偏差信号

局部adapter演变身份/传输系统；业务函数引跨仓重构；主链长期不动；generic registry/dictionary/sidecar增长；测试/validator多但Action不可达；为绿改正式行为；局部修复需要新owner/product/method；多次实质不同尝试仍解释不了根因；成本收益风险或不可逆性发生变化。

发现测试/proof/抽象/文档挤占主体，停止非必要扩展并回原实际未完；不靠新报告或固定测试治理体系解决。标准构建、日志、内存保护和正式读回继续。

## 5.3 偏差回压单

```yaml
implementation_deviation_backpressure:
  expected_work_shape: 原预计局部结果、宿主及平台复用
  observed_work_shape: 实际发生的变化
  evidence: exact facts
  attempts_and_results: 实质不同尝试
  affected_business_result: 受影响Action/product
  authority_boundary: 超出哪项工程自由
  options:
    - option + business/engineering/cost/risk/reversibility
  recommendation: Pro推荐与最强反对
  blocked_work: 具体路径
  continuable_work: 不受影响工作
  forbidden_bypasses: fallback/scope shrink/platform clone等
  exact_decision_needed: Pro/Owner需裁什么
```

# 6. Owner Gate 之前的质量门槛

给所涉业务关系/产品链、来源事实、后续定案、代码/runtime能证明什么、现权力为何不能决定、真实候选（唯一则说明）、scope/state/identity/time/history/method/product/consumer/platform影响、推荐/信心/反例、可逆性/复验、阻断/可继续及禁止绕行。不能只说不清楚。

现合同已决定时不重问Owner，由Pro实际修正或有理由委派，Codex不自行取得修改权。

# 7. 只暂停受影响路径

```yaml
blocker_locality:
  blocked_authority_or_fact: exact
  directly_blocked:
    - Action / method / product / writer / test
  indirectly_blocked:
    - only real dependencies
  continuable:
    - unrelated reversible work
  shared_write_conflicts:
    - files/types/root/writer requiring single writer
  forbidden_outputs_before_resolution:
    - formal product / checkpoint / completion claim
```

门不能停掉全纵切，也不能给受影响路径填默认值。先真实反馈不删完整业务义务。

# 8. 旧构包时来源缺口：仅为定位线索

P1 requirement、Spine accepted engineering parent、P2长历史后续合同及FRP/TIS重锁在旧构包曾缺；这些只说明旧证据限制，不能套新用例全局阻断。实际任务核当前完整来源，旧事故不决定新产品应然；自己的设计、上游和交付未完继续由本任务补齐，不冒称外部条件。历史经Git保留，本文件不充当当前bug allowlist。
