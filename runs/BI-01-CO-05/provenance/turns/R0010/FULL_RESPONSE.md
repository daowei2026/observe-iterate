# BI-01-CO-05 R0010 实质管理、阶段接收与条件重入完整回交

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-05`
- `invocation_id`: `BI01-CO-05-R0010-b1ffdd7d4721`
- `assignment_token`: `cf21dd5b82654fe2ab91cd6aae97`
- `role`: `management`
- `recipient`: `chatgpt://global/BI05管理`
- `route`: `trigger:ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW`
- `work_status`: `SUBMITTED`
- `management_result`: `EFFORT_REVIEW_CONSUMED__ONE_SHOT_CONDITIONAL_REENTRY_AUTHORIZED__NO_MARKET_PACKAGE_ACCEPTED`

<a id="completed-scope"></a>
## 1. 本轮完成范围

本轮完成的是 R0006 重置后第二个两调用段的实质投入复看，以及对 R0008 全段准备、Worker 一次真实执行和 R0009 专业消费的阶段接收；不是重新启动、重复 M-START、技术故障转述或自动重派 Worker。实际完成：

1. 全文读取 R0010 完整派发，核实 invocation、assignment token、recipient、route、formal task、Question Work Binding 和两次有效 Professional 调用的触发事实；
2. 读取并核对 R0008 完整 Professional 回交、全段图数合同、脚本、静态校验和正式 Worker 工单；
3. 亲自核实 R0008 脚本中的对象、频率、尺度、Context、主/辅窗口、输出根、请求合同和 `build_chart_run → pages → board` 顺序；
4. 读取并核对 Worker `FULL_RESPONSE`、`EXECUTION_RECEIPT`、`BLOCKER_EVIDENCE`、页面/正式文件缺件表、身份记录及失败停止事实；
5. 读取并核对 R0009 完整 Professional 回交、报告、Worker 结果消费、阻断/重入裁定、关键 T 表、Owner 过程反馈、触发通知和两份 Return；
6. 重新核对 00/01/02/03/04/05/06、探索 README、运行指南、Owner GO、工具实践、当前正式任务、Workmap Binding、动态地图/入口/采用状态和 gate 实现；
7. 重建完整业务关系：Owner 问题与过程 → R0008 全段输入合同 → 环境条件与实际输入产生 → 正式证据资格 → 第一层连续背景 → 第二层具体用例 → Management/Owner；
8. 对 R0008/R0009 作有限接收：接收全段技术设计、固定脚本、一次真实失败执行和精确阻断分类；拒绝任何市场、特征不足、无候选或方法结论；
9. 裁定 R0008 原 order 已终态关闭，不得重派、自动重试、改名复用或保留 future/deferred 身份；
10. 作出真实投入安排改变：不盲跑完整脚本，也不无限等待外部恢复证明；由原 Professional 签一个一次性条件重入新 order，同一 Worker 执行内先做同身份精确文件读探针，通过即从头运行原 R0008 全段脚本一次，失败则在昂贵调用前停止；
11. 明确禁止复制日历、切换 resolver/source/checkout、修改 NFS/共享代码配置或使用平行数据入口；需要这些变化时按 `CORE_INPUT_OR_PROCESS_CHANGE` 回管理；
12. 限定同路径条件重入只有一次；再次失败后不签第三单，必须进入环境成本终止或向 Owner 明示申请输入变化的决定；
13. 消费 `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW` 并从下一有效 Professional 调用重置新两调用段；
14. 更新 Owner 入口、长程地图、采用状态和 Workmap Intake；正式任务、Binding、Owner 05、03 与全段纠正保持不变；
15. 重建 Workmap v2 指纹并绑定 R0010 管理决定、四次有效 Professional 历史、R0008 order 终态、阻断事实、触发消费和 routine same-work Professional 续作；
16. 形成完整管理决定、持续责任、唯一后继、主控接续及本轮双 Return 所需承重正文。

本轮没有由 Management 代签新 Worker order，没有直接调用 Worker，没有修改共享环境或输入源，没有生成图数，也没有形成或接受市场背景、候选、排序、无候选、自然挑战或 Owner 方法有效性结论。

<a id="decision-summary"></a>
## 2. 管理裁定摘要

正式决定：

`runs/BI-01-CO-05/reviews/management-R0010/DECISION.md`

核心裁定：

```text
R0008 full-range design and immutable script = ACCEPTED_AS_REUSABLE_TECHNICAL_BASIS
R0008 Worker execution = ACCEPTED_AS_ONE_REAL_FAILED_ATTEMPT
R0009 blocker classification = ACCEPTED
R0008 original order = TERMINAL_NO_REDISPATCH_NO_AUTORETRY_NO_DEFERRED
calendar read failure persistence = UNKNOWN_SINGLE_OBSERVED_ATTEMPT
qualified market T = 0
first process practice package = NOT_ACCEPTED
formal task / Binding / Owner 05 / tooling 03 = ACTIVE_UNCHANGED
ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW = SATISFIED_AND_CONSUMED_R0010
next route = SAME_WORK_TO_ORIGINAL_PROFESSIONAL
next execution = ONE_SHOT_SAME_IDENTITY_PROBE_THEN_CONDITIONAL_FULL_RUN
```

R0010 不采用“等待某个不具名外部主体先证明恢复”作为无时限后继，也不允许因为单次 errno 5 直接重复昂贵全段任务。管理把恢复判断和实际执行合成一个有责任人、低成本前置、单次额度和明确退出条件的 Worker 运行，同时保持所有业务输入与 Owner 过程不变。

<a id="business-system"></a>
## 3. 完整业务系统判断

### 3.1 当前真实问题

`CASE-OWNER-PROCESS-PRACTICE-01` 仍要求回答：

> 在本 Run 实际可核的 `rb/hc/i` 30m large/mid 特征输入中，沿当时可知信息向前推进时，多品种同向大尺度背景何时能够被辨认、怎样改变或失效；其中是否有足够中尺度对象和关系形成具体候选规律，对明确后续过程给出候选、排序或合法无候选并随新信息更新；最近自然挑战怎样支持、否定或限制规律；真实实践对 Owner 初版用例形成方式意味着什么？

它没有被改成“文件能否读取”“脚本能否跑通”或一次固定时点预测题。环境恢复只是让真实专业实践得以产生输入的依赖。

### 3.2 结果产生和消费关系

| 关系 | 真实对象 | 最低资格 | 当前状态 |
|---|---|---|---|
| Owner 过程 → 输入设计 | 正式任务、rb/hc/i、30m、large/mid、SOF/tlist、全段范围 | 不用旧局部 Case、图或工具问题替代 Owner 完整过程 | 有效且未改 |
| 输入设计 → 条件重入 | 新 Professional order；同身份精确日历读探针；通过即原脚本全量执行 | 同 workspace、Python 入口、权限身份、mount/source；无复制、替代、绕过 | 待签新 order |
| 条件重入 → actual 图数 | actual run/core、全段主图、七个辅助图、board/manifest/index、正式 KLine/large/mid | 实际生成、打开、程序读取；覆盖/缺失按实 | 尚无 |
| actual 图数 → 证据资格 | actual/confirm/event/revision、方向来源、无方向点、日历、缺失与当前发展部分 | 正式字段、可靠映射、视觉线索、未知分开；不倒填未来 | 尚未核 |
| 资格 → 第一层 | 关键 T 上背景提出、变化、错位、失效和中尺度充分性 | 只使用截至 T 可得信息；共同范围与完整线段分开 | 合格 T=0 |
| 第一层 → 第二层 | 中尺度对象、候选规律、目标后续、判断更新和自然挑战 | 支持、反证、等待、不可判定分开；过去表现不自动延续 | 未开始 |
| Professional → Management | 报告、关键 T 表、对象定位、挑战、限制和 Owner 过程反馈 | 技术 PASS、页面或单例不等于业务包 | 本轮仅接收技术事实 |
| Management → Owner/下一轮 | 采用、局部修改、待证、替换建议或下一问题 | 重要新增分析显式呈现；实质改输入/过程/方向前确认 | 当前无新业务分析 |

当前 I/O 阻断只限制输入产生及其下游，不证明研究问题、特征语义或 Owner 两层过程失败；但没有 actual 图数时也不存在不依赖这些输入即可合法完成的承重市场判断。

<a id="stage-acceptance"></a>
## 4. R0008、Worker 与 R0009 阶段接收

### 4.1 接收的实物与事实

- R0008 固定 `rb/hc/i`、30m、large+mid、small 关闭；
- `GTQH_L1_20210104_20240229 / gtqh_four`；
- Owner 主范围 `[2021-01-04 00:00:00, 2024-03-01 00:00:00)`；
- 一张全段主图和七张先验半年辅助图，辅助图不替代主图；
- 图与正式数据同 run/core，正式数据包含 KLine/large/mid 和 manifest/index；
- 原脚本 SHA-256 `5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`；
- Worker 实际执行一次，命令、cwd、解释器、时间、耗时、exit code 和原日志 hash 可定位；
- 实测脚本 hash 与 Professional 固定值一致，兼容 diff 为 0，未切换 checkout、修改共享源码/配置或重启服务；
- 精确失败文件 `/m3varI/var/L1_data/sof/unit/affiliated_calendar_no_night.csv`；
- 精确调用链 `script.main → build_chart_run → _build_chart_core_run → _default_calendar_resolver → blk_suitable_calendars → read_symbol_calendars_csv → open`；
- NFS mount source `192.168.9.79:/m3varI`；
- 失败发生在 actual core/run 建立前，pages 和 board 均未调用；
- R0009 正确把所有覆盖、行数、缺失和 warm-up 保留为 UNKNOWN，不填 0；
- R0009 正确触发本轮 EFFORT 并保留完整业务未完。

### 4.2 不接收

- 不接收预请求 run_id 为 actual run/core；
- 不接收 0 页面、0 切片为市场无数据、SOF 不存在、2024-02-29 无覆盖或特征没有对象；
- 不接收单次 `OSError(errno=5)` 为文件永久损坏、NFS 长期不可用或根因已明；
- 不接收静态脚本、机械工单、完整失败回交或探针计划为技术 PASS；
- 不接收任何共同大尺度背景、中尺度结构、候选、排序、合法无候选、自然挑战或方法有效性结论；
- 不接收 R0009 为 `FIRST_PROCESS_PRACTICE_PACKAGE`；
- 不接收无限期“等待恢复证明”为足够的业务推进安排。

R0008/R0009 的 round artifacts 对其技术设计、执行和阻断叙述是可复核的；这不等于当前长程业务任务或首个实践包完成。

<a id="bearing-issue"></a>
## 5. 承重问题的独立核实

管理亲自读取并核实：

- `runs/BI-01-CO-05/artifacts/professional-R0008/WORKER_ORDER.md`
- `runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py`
- `runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CHART-DATA-R0008-01/FULL_RESPONSE.md`
- 同目录 `EXECUTION_RECEIPT.json` 与 `BLOCKER_EVIDENCE.json`
- `runs/BI-01-CO-05/artifacts/professional-R0009/REPORT.md`
- 同目录 `BLOCKER_AND_REENTRY_DECISION.md`、`WORKER_RESULT_CONSUMPTION.json` 与触发通知
- R0009 两份 Return。

R0008 脚本在调用 `build_chart_run` 前只写请求合同。失败时 actual core/run 尚未建立，之后的页面与 board 调用均未发生。阻断文件位于当前默认 calendar resolver 的必需链上，因此不能删除日历机制或用另一路径伪装普通兼容。另一方面，只有一次 `open` 失败，不能把它当永久状态。

本轮新增的 Management 组织不是新业务分析，而是执行反馈回路：下一 Worker 在同一身份先做精确 `open/read`。该探针直接检验导致上次停止的必要条件；通过后在同一执行中立刻进入原业务脚本，不把探针变成新长期 Gate。这样既避免盲跑昂贵任务，也避免无责任、无时限等待。

<a id="reentry-decision"></a>
## 6. 一次性条件重入决定

原 Professional 下一次有效调用只签一个符合现行合同的新 order，建议：

```yaml
order_id: BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01
target_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
target_workspace: /dwdhome/fy/cgpterm
aidata_execution_workspace: /dwdhome/fy/BASE_E6_2
script: runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py
script_sha256: 5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16
business_inputs: UNCHANGED_FROM_R0008
```

同一次 Worker 执行先记录：

```text
same workspace + same Python entry + same permission identity
current /m3varI mount source
exact open/read of affiliated_calendar_no_night.csv
UTC timestamp + byte count + SHA-256 + exit code + stderr
no stale copy + no alternate source + no resolver bypass
```

执行分支：

1. **探针失败**：在全段脚本前停止，交精确失败证据；同路径重入额度耗尽，不自动重派、不签第三单。
2. **探针通过**：立即从头运行 R0008 原脚本一次，fresh dynamic run_id，不复用失败 attempt 的预请求 id；保留旧失败实物，按原工单实际开主/辅图、读 manifest/index/KLine/large/mid、核实际覆盖/缺失/hash 与同 run/core。
3. **普通兼容差异**：只在 R0008 原允许范围内修通并交 copy/diff，不改变业务语义。
4. **需替代 source/resolver、复制日历、修改 NFS/共享源码配置、切换 checkout/依赖或业务参数**：停止并提交 `CORE_INPUT_OR_PROCESS_CHANGE`，不临场处理。

Management 本轮不代签 order。控制器不得根据本报告直接自拟 Worker prompt；只有原 Professional 在真实 `COMMITTED` 调用中签发的新 order，经 exact commit 的 worker-order preflight 通过后才能投递。

<a id="effort-review"></a>
## 7. 投入收益与触发消费

R0006 重置后的有效调用：

| 调用 | 实际信息收益 | 仍未取得 |
|---|---|---|
| R0008（第 3 次累计、本段第 1 次） | 全段脚本、完整图数合同、新工单 | 目标 runtime 结果与 market T |
| R0009（第 4 次累计、本段第 2 次） | 消费实际 Worker 失败；把笼统不可用缩小到精确日历文件、call chain 和一次 errno 5 | core、图、正式数据与市场观察 |

这两次调用取得了可复用输入设计和一个低成本可证伪的环境条件，有真实信息收益；但投资业务推进仍为 0 条合格 T。继续价值来自一次条件重入，而不是再加厚来源讨论、重复图数设计或盲跑全量任务。

本轮正式消费：

```text
ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW = SATISFIED_AND_CONSUMED_R0010
```

新计数从 R0010 后第一次有效 Professional 调用开始。预期：

1. 第一次调用签发一次性条件重入 order；
2. Worker 返回后的第二次调用消费结果；成功则同轮核证据资格并开始第一层，失败则回管理作停止/输入变化决定。

运输补交、重复回执、SHA-only 修复和无回答不计。RESULT/CHANGE 可提前触发管理。同路径条件重入只有一次，不允许连续串联 Worker。

<a id="trigger-observations"></a>
## 8. 触发观察

| trigger_id | state | 本轮解释 |
|---|---|---|
| `FIRST_PROCESS_PRACTICE_PACKAGE` | `NOT_YET` | 无 actual 图数、合格 T、第一层、第二层、挑战或完整方法反馈 |
| `CORE_INPUT_OR_PROCESS_CHANGE` | `NOT_YET` | 条件重入保持同 source/path/script/业务参数；需要替代来源或绕过时才触发 |
| `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW` | `SATISFIED` | R0008/R0009 构成本段两次有效调用；R0010 已实质消费并重置下一段 |

同一个 R0009 触发不得再次引发完整管理调用。

<a id="workmap-intake"></a>
## 9. Workmap/Intake 更新

### 保持不变

- `runtime/config/WORKMAP_BINDING.json`，blob `baf957a4f029008a0f533fb4baedb82b07c65900`；
- `runs/BI-01-CO-05/01_当前任务.md`，blob `5d6589c9a6104f879711787157494247c0293932`；
- Owner 00/05/06、工具 03、全段时间纠正和 stable rule paths；
- Reader policy `OWNER_OPTIONAL`。

### 已更新

- README：反映 R0008 全段设计、Worker 实际失败、R0009 消费及 R0010 条件重入；
- 长程地图：反映完整业务关系、真实资格、order 终态、一次性退出条件和全部未完；
- Adoption status：从 R0006 等待新脚本更新到当前真实状态；
- Intake：记录四次有效 Professional 调用、第二次 EFFORT 消费、R0008 order 终态、精确阻断和 routine same-work 续作。

冻结的当前 Intake 数据：

- 受管状态 observed commit：`2d8568a081bab2da80f7a154238d2b8ea37166bb`
- Binding blob：`baf957a4f029008a0f533fb4baedb82b07c65900`
- README blob：`97c2ac84018d89cd1ead5c39927f1b2503529765`
- map blob：`7764b34717f6e2517938b9a3dc7d98dd38ff375d`
- task blob：`5d6589c9a6104f879711787157494247c0293932`
- Adoption status blob：`1c1fc9ce989c5f3daa0c29d08d006825817a403b`
- R0010 decision blob：`e79c87b621285ddfac9c3603e2faa576ac440190`
- current artifacts tree canonical projection：`adf35bf8b11cb092d0c35284f458a4ac2bf7499b15b1301499fbf0a7961ad351`
- Reader-input fingerprint：`75f8b09654fc8d3189d59d0306de980247400894e74f987414e905fb76e9af97`
- Workmap fingerprint：`4c67cdf27d96cee0ec2fe0d029f4062b892730b1cba78e201feaaed901e40014`
- Intake commit：`0576037aaf485bc7167ba8274703a3db22c33ffc`
- Intake blob：`1fc0bd5939d73eee5d4b9f5856dda28af7a798fb`

指纹按仓库 `overlay/tools/workmap_gate.py` 的 v2 projection/canonical JSON 算法重建：README 受保护锚点逐段 hash，map/task/Owner/rule 使用 immutable blob，artifacts watch root 使用 51 个真实 blob 的 `ls-tree` 形状，`reviews/independent` 当前为 `null`。本轮只在 reviews/provenance 继续写回交，不再改变受管 README/map/task 或 artifacts，因此 projection 保持稳定。

本会话通过 GitHub connector 读写，没有本地 checkout，故不声称本地 CLI `workmap_gate.py check/dispatch` 已运行。控制器必须在实际 Professional 发送前用最终 exact commit、当前 Intake 和真实 delivery observation 运行机械检查。新 Professional artifacts 写入 watch root 后会改变结果树；新 Worker 派发前须按当前机制重建或核验 Intake。

<a id="owner-items"></a>
## 10. Owner 与审查事项

### 当前无需新增 Owner 决定

本轮没有新的市场规律、投资判断、主过程替换或业务方向改变。一次性条件重入是现有输入链的可逆组织，不改变 Owner 05 或全段纠正。

### 后续必须显式处理

- 同身份探针再次失败：Management 不重复同路径，决定以环境成本终止当前 Case，或向 Owner 明示申请改变 calendar source/正式入口；
- 替代 source/resolver、不同 checkout、平行数据入口或共享配置变化：按 `CORE_INPUT_OR_PROCESS_CHANGE` 列新旧身份、成员/日历/夜盘/UTI/正式切片影响和既有主张失效范围；
- 重要候选规律、显著反例或 Owner 过程实质替换建议：呈现 Owner 校准。

当前不派业务 Reviewer，因为没有可复做的市场主张。Workmap Reader 仍为 Owner 授权的 `NOT_REQUIRED`，不是 PASS；机械检查全部保留。

<a id="materials-use"></a>
## 11. 材料使用记录

### 全文读取并实质使用

- R0010 `FULL_ASSIGNMENT.md`、`INVOCATION.json`、`DISPATCH.json`、`SEND_RECEIPT.json`；
- 当前正式任务及其 Question Work Binding；
- R0008 `FULL_RESPONSE.md`、Professional `REPORT.md`、`WORKER_ORDER.md`、完整 Python 脚本、请求/静态校验与签发链；
- Worker `FULL_RESPONSE.md`、`EXECUTION_RECEIPT.json`、`BLOCKER_EVIDENCE.json`、页面/正式文件缺件与身份记录；
- R0009 `FULL_RESPONSE.md`、Professional `REPORT.md`、`WORKER_RESULT_CONSUMPTION.json`、`BLOCKER_AND_REENTRY_DECISION.md`、关键 T 表、Owner 过程反馈、触发通知、`QUESTION_WORK_RETURN.json` 和 `ROLE_RETURN.json`；
- `OWNER_START.md` 与 Owner 全段时间纠正；
- `professional/README.md`、`professional/exploration/README.md`；
- exploration 00—06；
- 2026-11-01 30m 多品种工具实践；
- `runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md`；
- 当前 Workmap Binding、旧 Intake、README、长程地图和 Adoption status；
- `overlay/tools/workmap_gate.py` 的 snapshot、check、dispatch、worker-order/result 相关实现；
- DR14 与 Overlay 08 的现行运行边界。

### 定向使用

- R0002/R0005/R0006：用于核上一投入段、全段纠正和重置点，不继承其已撤工单；
- 当前 artifacts tree：用于核真实已成实物和 Workmap result projection；
- R0004 hold：用于确认未采用方案不复活；
- 03/05：用于确认条件重入没有改变图数身份、工具权限或 Owner 两层观察。

### 未读或不可用

- `unread_required: []`
- `unavailable_required: []`

actual 全段图、正式切片和同身份探针结果当前不存在，但它们是下一 Professional/Worker 的未成实物，不是本轮管理接收必须读取却缺失的既有来源。

<a id="limitations"></a>
## 12. 限制与不宣称事项

1. 没有运行下一次同身份读探针，也不知道文件当前是否可读；
2. 没有 actual run/core、图、正式数据或合格 market T；
3. 没有判断三品种共同背景、中尺度结构、候选/排序/无候选或自然挑战；
4. 没有由 Management 签新 Worker order，也没有实际派发；
5. 没有本地执行 Workmap CLI；指纹为按仓库实现和 immutable blobs 重建，仍需控制器 exact preflight；
6. R0010 控制面 `SEND_RECEIPT.json` 仍记录 `NOT_SENT`，Management 未擅改；当前用户实际委派使本轮工作得以执行，控制器仍须按真实发送事实对账；
7. Reader `NOT_REQUIRED` 不是 Reader PASS；当前没有业务 Reviewer；
8. 当前任务、Binding、05、03 均未改变，不能从本轮推断方法已稳定或完成。

<a id="remaining"></a>
## 13. 完整未完

1. 原 Professional 签发一次性条件重入新 order；
2. 控制器对新 order exact commit 做 worker-order preflight 并真实派发；
3. Worker 同身份执行精确读探针；通过则从头执行原全段脚本，失败则低成本停止；
4. Worker 完整回交探针、运行、页面、正式数据、覆盖、缺失、hash 与身份，或精确失败证据；
5. 原 Professional 消费结果，成功时核实际覆盖、字段/方向/时间语义和图数同身份；
6. 从第一条合格 T 开始第一层连续过程；
7. 判断背景内中尺度结构是否足够；
8. 形成具体用例、目标后续判断、更新或证据化无候选；
9. 检查确认滞后、阶段错位、短后续空间、反向负担、邻近失败和替代解释；
10. 给出 Owner 过程实践反馈和唯一下一专业问题；
11. Management 接收首个真实业务包，决定续作、Reviewer、Owner 校准或停止；
12. 同路径探针再次失败时停止重复投入，进入环境成本终止/输入变化决定；
13. 多轮真实实践后才判断是否固化方法、规范、Agent 或评分器。

<a id="continuation"></a>
## 14. 唯一实际接续

`same_work` → `chatgpt:BI-01-CO-05:professional`

下一次有效 Professional 调用只把 R0010 第 6 节管理决定转成一个符合现行 Worker 合同的新 order，保留 R0008 原脚本和全部业务参数；不得重做来源调查、再设计图数、等待无责任主体的外部证明，或把旧 order 改名继续。

新 order 合法签发后，控制器运行 worker-order preflight 并实际派发。Worker 结果回原 Professional：

- 技术成功：Professional 同一调用内完成结果消费、证据资格核对并开始第一层业务观察；
- 同路径探针失败：不签第三单，回 Management 决定停止当前 Case或提出有权输入变化；
- 其他失败：只限制实际受影响输出，说明仍可继续范围，不自动升级为市场或方法否定。

<a id="controller-handoff"></a>
## 15. 主控接续

1. fresh read：
   - `runtime/config/WORKMAP_BINDING.json`
   - `runs/BI-01-CO-05/README.md`
   - `runs/BI-01-CO-05/00_长程推进地图.md`
   - `runs/BI-01-CO-05/01_当前任务.md`
   - `runs/BI-01-CO-05/reviews/management-R0010/DECISION.md`
   - `runtime/config/ADOPTION_STATUS.md`
   - `runs/BI-01-CO-05/reviews/WORKMAP_INTAKE_CURRENT.json`
2. 在最终 exact commit 运行 mechanical Intake check；
3. 以 unchanged formal task 和真实 `NOT_SENT` delivery 运行 routine Professional dispatch preflight；
4. 通过后归档完整 Professional 派发原文，把当前正式任务、R0010 决定及必要 R0008/R0009 证据交 `chatgpt:BI-01-CO-05:professional`；
5. 保存真实 invocation/send receipt；不得直接派 R0008 原 order，也不得由主控自拟条件重入 Worker prompt；
6. 新 Professional order 形成后再运行 worker-order preflight，Worker 结果回原签发 Professional；
7. 不把有限技术接收、探针 PASS 或 Worker technical PASS改写成市场业务接收或 Owner 方法通过。

<a id="self-check"></a>
## 16. 自查

- [x] 使用最新 R0010 委派、身份、route 和触发，不复用 R0006 旧状态。
- [x] 全文核 R0008、Worker、R0009 主体与两份 Return，不只看摘要。
- [x] 亲自核脚本、工单、调用链、失败位置和业务消费者。
- [x] 从 Owner 完整目标与业务关系决定优先级，不把报错当完整任务。
- [x] 区分技术设计接收、失败事实、市场业务接收和阶段完成。
- [x] 原 R0008 order 终态关闭，不重派、不列 deferred。
- [x] 未删除必要日历机制，未授权替代 source、resolver 或平行取数。
- [x] 通过单次条件重入实际改变安排，避免盲跑与无限等待。
- [x] 限定一次额度和失败退出；Management 未代签 Worker。
- [x] 保留正式任务、Binding、Owner 05、全段范围和完整业务未完。
- [x] 实质消费 EFFORT 并重置下一段，未重复管理同一触发。
- [x] 更新动态工作面与 Intake，保持 Reader waiver 非 PASS。
- [x] 未声称 CLI、派发、图数、market T、候选、Reviewer 或 Owner 接收已完成。
