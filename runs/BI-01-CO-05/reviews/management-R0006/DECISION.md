# BI-01-CO-05 R0006 管理阶段接收与投入复看决定

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-05`
- `invocation_id`: `BI01-CO-05-R0006-81bbad74993d`
- `assignment_token`: `0979ffeb0ae94fec8bda685d20fce36`
- `role`: `management`
- `route`: `trigger:ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW`
- `effective_professional_calls_reviewed`: `2`
- `decision_status`: `LIMITED_TECHNICAL_PREPARATION_ACCEPTED__OLD_45DAY_ORDER_STOPPED__FULL_RANGE_REVISION_CONTINUES`

<a id="decision-summary"></a>
## 1. 决定摘要

本轮是对 R0002 与 R0005 两次有效 Professional 调用的到期投入复看，也是对 Owner 最新时间覆盖纠正的同一次合法管理协调；不是 M-START，不重写正式任务、Binding、05 或 03，也不另建 Run。

管理决定如下：

1. **有限接收 R0005 的技术准备事实**：`rb/hc/i`、`30m`、`large+mid`、不默认启用 `small`、固定 SOF/tlist、同一 run/core 的图—正式数据调用链、脚本化执行方式及静态语法通过，可以作为下一次修订的可复用基础。
2. **不接收 R0005 的 45 天主范围**：`[2021-08-15, 2021-09-30)` 不具备承担 Owner 05 第一层“沿时间发现大尺度背景形成与演变”的资格。它只能在未来有实际需要时作为辅助局部放大，不能再作为本轮主图或正式数据主范围。
3. **旧工单永久停止新投递**：`BI01CO05-CHART-DATA-R0005-01` 虽已签发并通过机械 order check，但真实状态是 `NOT_DISPATCHED`；不得再派发、改名复用、手工补丁后发送或列为 deferred/future required。历史脚本、工单及签发记录保持不变。
4. **采用 Owner 明确指定的全段时间覆盖**：新主图与正式数据请求固定为 `[2021-01-04 00:00:00, 2024-03-01 00:00:00)`，即覆盖至 2024-02-29 当日；实际源数据首末时刻、交易日和特征有效覆盖按正式交付如实列出，不补造。
5. **由原 Professional 续作，不由 Management 或主控代写新工单**：原 Professional 下一次有效调用必须提交新的完整可执行脚本和新的正式 Worker 工单；保留已定品种、频率、特征及 Context，明确全段主图/正式数据和必要辅助分段。新工单经合法签发、机械校验和真实派发后，Worker 执行并回原 Professional。
6. **业务任务继续 ACTIVE**：当前合格市场 T 仍为 `0`，没有首层市场过程、第二层候选、排序、无候选、自然挑战或方法有效性结论。`FIRST_PROCESS_PRACTICE_PACKAGE` 仍未满足。
7. **消费本次 EFFORT 触发并重置下一投入段**：`ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW` 已由本轮实质消费。下一次有效 Professional 调用起进入新的两调用段；不能再次用同一个 R0005 触发重复完整管理。

<a id="business-system"></a>
## 2. 完整业务关系与当前系统应怎样工作

当前业务观察问题仍是：

> 在真实可核的 `rb/hc/i` 大、中尺度贴近转折输入中，沿当时可知信息向前推进时，共同大尺度背景何时能够被辨认、如何改变或失效；背景内中尺度结构何时足以形成具体候选规律，并对明确后续过程给出候选、排序或合法无候选，再随新信息更新？

正常系统按以下关系运行：

| 环节 | 当前真实输入/产物 | 可消费资格 | 直接消费者 | 当前状态 |
|---|---|---|---|---|
| 业务问题 | Owner 00/06/05 与当前正式任务 | 不把两层变成固定 Gate；不以工具题替代投资用途 | Professional | 保持有效 |
| 图数准备 | 新全段脚本、新正式 Worker 工单、合法派发 | 品种/频率/特征/Context 与全段范围被原 Professional 固定；历史旧单不复用 | Worker | 待原 Professional 修订 |
| 实际运行 | aidata run/core、全段主图、必要辅助图、board/manifest/FILE_INDEX、正式 KLine/large/mid 切片 | 实际运行成功；图与正式数据同一身份；实际覆盖和缺口可定位 | Professional | 尚未取得 |
| 证据资格 | 正式字段、上游可靠映射、视觉线索、未知；actual/confirm/event/revision 分开 | 不从最终图倒填；不把全部贴近点当有方向 zig；不把图投影冒充正式数据 | Professional、Management | 尚未核实 |
| 第一层观察 | 沿关键 T 的大尺度背景形成、改变、错位或失败，以及当时已有中尺度结构 | 使用截至 T 真正可取得的信息；共同观察范围与各品种完整线段分开 | Professional | 合格 T 为 0 |
| 第二层观察 | 具体中尺度对象、现象、候选规律、后续判断和更新 | 明确目标后续；支持、反证、等待、不可判定分开 | Professional | 未开始 |
| 管理接收 | 业务报告、关键 T 表、对象定位、挑战、限制、Owner 过程反馈 | 图/数据/脚本/机械 PASS 均不单独等于业务完成 | Management | 本轮只接收技术准备部分 |
| Owner/下一阶段 | 保留、局部调整、待证假说或实质改变建议 | 重要新增业务分析显式呈现；实质替换主问题/过程/方向前取得 Owner 确认 | Owner、下一 Professional | 当前仅采用 Owner 时间纠正，无新方向建议 |

本轮改变的是真实执行安排：不再把局部窗准备当成可继续直接派 Worker 的正常后继，而是先由原 Professional 把主图和正式数据覆盖纠正到 Owner 指定全段，再立即进入实际运行和业务观察。没有引入新的研究路线、评分器、Agent、事件账本或全面回放工程。

<a id="acceptance"></a>
## 3. R0005 阶段接收

### 3.1 接收的已成实物

| R0005 内容 | 接收结论 | 可用于什么 |
|---|---|---|
| 品种 `rb/hc/i` | 接收 | 保持钢铁链三品种共同观察对象 |
| K 线 `30m` | 接收 | 保持当前图数频率 |
| `ScaleTurnCalendar("large")` 与 `("mid")` | 接收 | 保持大/中尺度主输入；`small` 按需而非默认 |
| `GTQH_L1_20210104_20240229 / gtqh_four` | 接收 | 保持 Owner 最新固定 Context |
| `build_chart_run → build_big_world_chart_pages → build_board_run(reuse_core=True)` | 接收为执行结构 | 用同一 run/core 取得图与正式数据 |
| 相对比例、多品种同图、rb 背景轴、各品种源日历核验 | 接收为待现场执行的图面方案 | 新全段脚本继续明确，不交 Worker 临场决定 |
| 完整 Python 脚本与 `py_compile PASS` | 接收为可复用实现基础 | 只证明语法；不得称运行、图面或数据通过 |
| 原 Professional 具名签发工单 | 接收为历史签发事实 | 证明签发链曾合法；不授予旧单继续派发资格 |

### 3.2 不接收的内容

- 不接收 `[2021-08-15, 2021-09-30)` 作为主观察图或正式数据主范围；
- 不接收 R0005 脚本为当前可派发脚本；
- 不接收旧 Worker 工单为在途或可继续投递；
- 不接收静态语法 PASS 为目标环境运行、页面、manifest、正式切片或图数同身份通过；
- 不接收任何共同背景、中尺度结构、候选、排序、无候选、自然挑战或 Owner 过程有效性结论；
- 不接收 R0005 为 `FIRST_PROCESS_PRACTICE_PACKAGE`。

R0005 的 round artifact 对其本轮技术准备叙述是可复核的，但当前长程业务任务未完成。

<a id="bearing-issue"></a>
## 4. 承重问题的正文与代码核实

管理已亲自核实下列入口：

- `runs/BI-01-CO-05/artifacts/professional-R0005/WORKER_ORDER.md`
- `runs/BI-01-CO-05/artifacts/professional-R0005/build_bi01_co05_r0005_chart_data.py`
- `runs/BI-01-CO-05/OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md`

旧工单正文把 `图窗` 固定为 `[2021-08-15, 2021-09-30)`。旧脚本不仅在说明中写了局部窗，还在承重执行位置同时锁定：

- `WINDOW_START = "2021-08-15"`；
- `WINDOW_END_EXCLUSIVE = "2021-09-30"`；
- `CONTEXT_END = "2021-10-31"`；
- `brief["big_source"]["timespans"]` 使用该局部窗；
- 运行回执的 `actual_visible_window` 与 required verification 也使用该局部窗。

因此问题不是一句工单文字可修；若直接派发，实际 run/core、主图、正式切片和核验回执都会被裁成局部范围，无法支持 Owner 05 第一层从前向后发现大尺度背景形成与演变。正确处置是保留历史文件，另由原 Professional 创建全段新脚本和新工单，而不是覆盖、临时口头修改或让 Worker 自主改业务范围。

<a id="owner-correction"></a>
## 5. Owner 时间纠正的现行采用

本次只采用 Owner 已明确的时间覆盖纠正：

- 主请求范围：`[2021-01-04 00:00:00, 2024-03-01 00:00:00)`；
- 主图：人可看的全段 `rb/hc/i` 30m 同图，large+mid；
- 正式数据：同一输入身份下全段 30m KLine、large、mid 切片和 manifest/索引；
- 实际数据缺口：按源文件、日历、正式切片实际首末和空缺如实报告；请求范围不等于保证每一时刻均有数据；
- 辅助视图：允许按时间分段或对真实候选区间局部放大，但不得替代全段主图或裁短正式数据；
- 保留不变：`rb/hc/i`、`30m`、`large+mid`、不默认 small、SOF/tlist、当前正式任务和 Owner 两层业务过程。

本次不采用尚在讨论的《第一层业务观察实施设计》新要求，不修改 05/03，不把时间纠正扩展为完整方法重写。

<a id="withdrawn-scope"></a>
## 6. 已撤与保留

### 从当前执行退出

1. `BI01CO05-CHART-DATA-R0005-01` 的任何新投递、重复投递或未来必做地位；
2. 原 R0005 脚本作为当前执行脚本的资格；
3. 45 天局部窗作为主观察图或正式数据主范围；
4. R0002 的大型输入资格/事件账本/方向映射/全面审计工单范围；
5. R0004 未采用的迁移、任务/Binding/05/03 改写及其后继。

这些内容不改名保留为 deferred required，不让下一 Professional 重新研究其必要性。历史文件和事实记录仍保留，只是不再产生当前派发资格。

### 必须保留

- 当前正式任务、具名问题与完整业务范围；
- Owner 00/06/05 的目的和两层观察设想；
- 实际时间、身份、正式字段、状态和证据资格；
- `rb/hc/i`、30m、large/mid、SOF/tlist 与同 run/core 图数链；
- actual/confirm/event/revision、方向来源、无方向贴近点与当前发展部分的业务语义；
- Worker 结果回原签发 Professional、再由 Professional 形成业务结果；
- 全部未完成的第一层、第二层、挑战、方法反馈与 Owner 事项。

<a id="effort"></a>
## 7. 投入复看与实际安排改变

R0002 是第 1 次有效 Professional 调用，主要停在输入资格；R0005 是第 2 次有效调用，形成脚本和工单但仍没有实际图数或市场 T。继续按旧安排直接派 45 天 Worker 会把投入锁在不适配的局部输入上，因此本轮没有只写“scope 保留”，而是实际改变安排：

1. 停止旧单；
2. 固定 Owner 全段范围，消除 Professional 再次选择主时间窗的自由度；
3. 下一有效 Professional 调用只需完成全段脚本、新工单和准确执行细节，不再重做来源裁定或大范围资格调查；
4. 新单合法执行后，原 Professional 必须消费实际图数并进入真实第一层观察，不得再以格式、来源目录或静态准备作为主动停点。

本轮消费 `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW`，消费状态为 `CONSUMED_R0006`。重置规则：从本轮管理决定之后的第一次有效 Professional 调用开始计新段；下一段仍以两次有效调用为上限，但 RESULT 或 CHANGE 可提前触发管理。换 SHA、补运输或重复回执不计新调用、不清零。

<a id="continuation"></a>
## 8. 下一轮唯一可执行后继

接收者：`chatgpt:BI-01-CO-05:professional`（原 Professional 路线）。

Professional 继续同一正式任务，下一次有效调用必须：

1. 全文使用 Owner 时间纠正，不重写当前正式任务或主过程；
2. 在新的 Professional 轮次目录提交**新脚本**，主时间范围固定为 `[2021-01-04, 2024-03-01)`；
3. 保留 `rb/hc/i`、30m、large/mid、SOF/tlist、同 run/core 图—正式数据链和当前图面语义；
4. 明确全段主图的可读配置；如需分段/局部图，脚本中具体确定，不交 Worker 临场选择，并保证它们只是辅助；
5. 正式数据请求同样覆盖全段，回执要求核实际首末、缺失、manifest/索引与图数同身份；
6. 创建新的 order_id 和新的 `WORKER_ORDER.md`；不得覆盖 R0005 文件，不得引用旧 order 身份继续投递；
7. Worker 范围仅为执行、普通兼容修通、实际开图、读取正式数据和回交；不加入事件账本、全面方向审计、市场用例分析或第一层实施设计；
8. 在真实 `COMMITTED` 调用身份满足后正式签发，并明确 gate/实际派发仍由控制器执行；
9. 保留完整业务未完，不能把新脚本/工单当市场实践包。

控制器对新脚本/工单所在 exact commit 运行 worker-order preflight，实际派发后由 Worker 返回原 Professional。原 Professional 消费结果时，先核实际覆盖和证据语义，再从第一条合格 as-of T 开始大尺度背景—中尺度结构观察；有依据才进入候选/排序/无候选与挑战。

<a id="trigger-state"></a>
## 9. 触发与接收状态

| trigger_id | 本轮管理状态 | 后继 |
|---|---|---|
| `FIRST_PROCESS_PRACTICE_PACKAGE` | `NOT_YET` | 真实图数和完整业务实践包到达即回管理 |
| `CORE_INPUT_OR_PROCESS_CHANGE` | `NOT_YET` | Owner 本次纠正是已授权的执行输入纠正，不是替换正式任务/主过程；出现新的承重冲突再触发 |
| `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW` | `SATISFIED_AND_CONSUMED_R0006` | 从下一有效 Professional 调用重置计数；不得以 R0005 再重复管理 |

当前业务接收结论：

```text
technical_preparation_from_R0005 = ACCEPTED_WITH_SCOPE_LIMITS
old_45day_main_range = REJECTED_FOR_CURRENT_EXECUTION
old_worker_order_actual_dispatch = NOT_DISPATCHED
old_worker_order_new_dispatch = PROHIBITED
qualified_market_T_count = 0
first_process_practice_package = NOT_ACCEPTED
formal_task_status = ACTIVE_UNCHANGED
```

<a id="intake"></a>
## 10. Workmap 与 Intake 处置

- `runtime/config/WORKMAP_BINDING.json`：保持不变；
- `runs/BI-01-CO-05/01_当前任务.md`：保持不变；
- `professional/exploration/05_OWNER_PROCESS_EXPLANATION.md` 与 `03_TOOLING_AND_DATA_USAGE.md`：保持不变；
- README、长程地图与采用状态：按真实进展更新；
- `WORKMAP_INTAKE_CURRENT.json`：重建到当前受管输入和 artifacts 实际树，记录两次有效调用、本轮 EFFORT 消费、旧单停投与 routine same-work Professional 续作；
- Reader：仍为 Owner 授权的 `NOT_REQUIRED`，不是 PASS。当前没有替换问题、主要过程或 Binding，也没有独立 Reader 指定；机械检查全部保留；
- Reviewer：当前不派。没有市场主张、候选规律或方法有效性结论可供独立复做。

新 Professional artifacts 写入 watch root 后会使 Intake 结果树变化；因此新 Worker 派发前必须基于新 exact commit 重建/核对必要 Intake，不能复用本轮 snapshot 冒充 current。

<a id="owner-items"></a>
## 11. Owner 事项

### 已由 Owner 决定并已执行组织

- 全段主图/正式数据时间覆盖；
- 旧 45 天主范围不得继续派发；
- 保留品种、频率、特征及 Context；
- 原 Professional 修订新脚本和新工单；
- 不把新的第一层实施设计塞入当前 Worker 单。

### 当前无需新增 Owner 决定

本轮没有提出新的候选规律、投资判断、主过程替换或业务方向改变。普通图面可读性、辅助分段、API 兼容和实际缺口报告由 Professional/Worker 在既有边界内处理。

### 未来必须呈现 Owner

- 真实实践得出的重要候选规律或显著反例；
- 证据表明 Owner 两层过程需要实质替换；
- 需要改变当前研究问题、主要过程、品种/特征方向，或固化为规范/Agent/评分器。

<a id="remaining"></a>
## 12. 全部重要未完

1. 原 Professional 提交全段新脚本与新正式 Worker 工单；
2. 控制器对新工单 exact commit 做机械校验并真实派发；
3. Worker 在固定环境执行、普通修通、实际开图、读取全段正式数据，准确报告真实覆盖与缺口；
4. 原 Professional 消费图数，核字段、方向来源、actual/confirm/event/revision、日历和当前发展部分；
5. 从第一条合格 T 开始走第一层连续过程并检查中尺度结构；
6. 在有价值背景中形成具体用例、后续判断和更新，或给出有证据的无候选/框架限制；
7. 检查自然挑战、相邻失败片段和替代解释；
8. 回交 Owner 过程反馈和下一专业问题；
9. Management 接收首个真实业务实践包并决定续作、Reviewer、Owner 校准或停止；
10. 多轮实践后才判断方法是否值得固化，当前不提前建立评分器、Agent 或完整分类。

<a id="controller-handoff"></a>
## 13. 主控接续

1. fresh read 本决定、更新后的 README、地图、采用状态和 Intake；
2. 在同一 exact commit 运行 Workmap mechanical check；
3. 以真实 `NOT_SENT` delivery 对 unchanged formal task 运行 routine Professional dispatch preflight；
4. 通过后，把当前正式任务、Owner 时间纠正和本决定完整交给 `chatgpt:BI-01-CO-05:professional`；
5. 保存真实发送记录；不得把本轮 Management 决定改写成 Worker 工单，也不得直接派旧 R0005 工单；
6. Professional 新工单形成后再按现行 worker-order 机制处理；
7. R0006 当前仓库 `SEND_RECEIPT.json` 仍为控制面记录的 `NOT_SENT`，Management 不改写该控制记录；控制器按实际投递事实后续对账。
