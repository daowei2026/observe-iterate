# BI-01-CO-05 Professional R0005：图数脚本与正式工单签发

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-05`
- `invocation_id`: `BI01-CO-05-R0005-39b928f3b0b1`
- `assignment_token`: `06b1e5482b6b4651a68af7fb774bc42`
- `role`: `professional`
- `question_id`: `CASE-OWNER-PROCESS-PRACTICE-01`
- `effective_professional_call_index`: `2`
- `round_state`: `SCRIPT_READY__FORMAL_ORDER_SIGNED__PENDING_CONTROLLER_VALIDATION`

<a id="decision-summary"></a>
## 1. 裁定摘要

本轮按 Owner 最新纠正，把 R0002 过宽的“输入资格/事件账本调查”收缩为具体图数准备，并完成 Professional 应先承担的选择与代码固化：

> 准备 `rb/hc/i` 的 30m 同图，窗口 `[2021-08-15 00:00, 2021-09-30 00:00)`；只叠加 `ScaleTurnCalendar("large")` 与 `ScaleTurnCalendar("mid")`，并交付同一 run/core 的正式 30m KLine、large、mid 数据。Context 使用 Owner 最新指定的 `GTQH_L1_20210104_20240229 / gtqh_four`。完整 Python 脚本已提交并通过语法编译检查。

本轮执行期间，控制面以提交 `748de226b79aa66044d60c1dfa5a4b6ac48b138a` 记录了原 Professional 调用的真实发送证据，并将同身份 `SEND_RECEIPT.json` 更新为 `state=COMMITTED`。本 Professional 回读该提交后，现行 `overlay/12#worker-order-contract` 的签发身份前提已满足，故正式签发 `WORKER_ORDER.md`；但不声称控制器已运行 `worker-order`、已派发、已执行或已有 Worker 结果。

| 项目 | 状态 |
|---|---|
| 图数选择 | 已完成 |
| Python 脚本 | 已完成；静态语法 PASS，目标环境未执行 |
| R0002 旧工单 | 继续隔离，不按原范围新投 |
| 新工单内容 | 已冻结并正式签发 |
| 控制器校验/派发 | 尚未发生；不得由签发代替 |
| 新图页/正式数据 | 尚未回交 |
| 合格市场 T | `0` |
| 首个实践包 | 未满足 |
| 投入复看 | 第 2 次有效 Professional 调用，触发复看 |

<a id="completed-scope"></a>
## 2. 本轮已完成范围

1. 全文读取完整派发、现行任务、Owner 起始材料、最新图数纠正、最新 `07` 约定、R0004 HOLD、Owner Intake 例外和当前控制身份文件。
2. 核实旧工单 `BI01CO05-AIDATA-EVIDENCE-01` 不得按原范围新投，也不能改名复用。
3. 固定 `rb/hc/i + 30m + 单窗口 + large/mid`，明确排除 small。
4. 使用最新固定 Context，写出 `build_chart_run → build_big_world_chart_pages → build_board_run(reuse_core=True)` 完整脚本。
5. 脚本直接表达品种、窗口、特征、图面、正式数据与输出；运行 `python -m py_compile` 得到 `PASS`。
6. 固化 Worker 可做的普通 API/路径兼容修通及禁止变化。
7. 形成完整新工单；在控制面真实补交 `COMMITTED` 收据后正式签发，保留后续 gate/派发边界。
8. 保留业务未完、唯一接续及三项管理触发状态。

<a id="chart-data-plan"></a>
## 3. 图数方案

### 3.1 固定输入

| 维度 | 选择 |
|---|---|
| 品种 | `rb / hc / i` |
| K 线 | `30m` |
| 可见窗口 | `[2021-08-15 00:00:00, 2021-09-30 00:00:00)` |
| 窗口 ID | `BI01-CO05-C001` |
| Context 历史 | `2021-01-04` 至 `2021-10-31` |
| SOF / tlist | `GTQH_L1_20210104_20240229 / gtqh_four` |
| 日历 | 各品种源自身日历；rb 背景轴；现场核窗口内对齐 |

沿用该 45 天窗口，是为了直接服务 Owner 的“大尺度共同背景—中尺度具体用例”问题，并降低新增场景设计与工程不确定性；但采用最新 SOF 生成新 run，不把旧图当本轮正式输入。

### 3.2 图层与正式数据

图面固定为一张 Figure 同时展示 rb/hc/i，价格按相对比例归一化：

- `KLine(freq="30m")`；
- `ScaleTurnCalendar("large")`，三角形、17；
- `ScaleTurnCalendar("mid")`，菱形、12；
- 不启用 small。

small 不是当前两层问题的必要输入，先排除以降低密度；仅在后续需要解释中尺度内部反复时另行开启。

`build_board_run(..., reuse_core=True)` 必须与图共用 run/core，并能定位 rb/hc/i 的 30m KLine、large、mid 正式切片及 delivery manifest/索引。Worker 不需生成事件账本、方向映射、first-visible/revision 历史、全量审计或业务结论。

### 3.3 图数回来后的业务边界

同 run/core 图数只是必要输入。Professional 后续仍须区分实际与确认/事件位置，沿当时可知信息建立大尺度过程，在同一关键 T 检查中尺度充分性，再形成候选、排序或合法无候选，并检查确认滞后、阶段错位、反向负担和邻近失败片段。本轮没有把图数方案升级成市场规律。

<a id="script"></a>
## 4. 可执行脚本

- 路径：`runs/BI-01-CO-05/artifacts/professional-R0005/build_bi01_co05_r0005_chart_data.py`
- SHA-256：`a109c6c390eb8d1b4cf155c1fb6fbbf4c0d7ca48e0e780083b257eb57fa3811f`
- 输出根：`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0005_chart_data`

```bash
cd /dwdhome/fy/BASE_E6_2
python /dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0005/build_bi01_co05_r0005_chart_data.py
```

静态检查：`python -m py_compile: PASS`。该检查只证明语法通过；当前通道没有目标 aidata 运行时和 SOF 数据，不声称 import、API、数据、页面或正式交付通过。

Worker 只允许修正当前有权 API 的 import/签名/显式 rb-hc-i 选择/绘图 helper/序列化等兼容问题，不得更换品种、窗口、频率、SOF、tlist、large/mid 选择或加入 small，也不得修改共享源码、切换 checkout 或升级依赖。

<a id="worker-order-state"></a>
## 5. Worker 工单状态

### 5.1 旧工单

`runs/BI-01-CO-05/artifacts/professional-R0002/WORKER_ORDER.md`（`BI01CO05-AIDATA-EVIDENCE-01`）保留历史但不按原范围新投。本轮未删除、覆盖或宣称其已执行。

### 5.2 新正式工单

`runs/BI-01-CO-05/artifacts/professional-R0005/WORKER_ORDER.md`（`BI01CO05-CHART-DATA-R0005-01`）已包含完整身份、目标线程、两个工作区、冻结脚本/哈希/命令、图数交付、修通边界、写权及回原 Professional 的 `FULL_RESPONSE.md` 要求。该文件由本 Professional 在回读真实 `COMMITTED` 收据后签发。

### 5.3 签发依据与后续边界

现行合同要求签发轮：

```text
INVOCATION.json exists
+ SEND_RECEIPT.json has same identity
+ SEND_RECEIPT.state == COMMITTED
```

本轮最终回读：

```text
control_commit = 748de226b79aa66044d60c1dfa5a4b6ac48b138a
invocation_id = BI01-CO-05-R0005-39b928f3b0b1
assignment_token = 06b1e5482b6b4651a68af7fb774bc42
SEND_RECEIPT.state = COMMITTED
exact_round_marker_verified = true
payload_verification = exact_verified
```

该收据由控制面独立提交，Professional 没有改写或补造。依据现行合同，本轮可以签发，但签发不等于 gate、实际投递或结果：

```text
script_ready = true
order_content_frozen = true
formal_order_signed = true
worker_order_gate_run = false
dispatch_claimed = false
worker_result_claimed = false
```

<a id="business-state"></a>
## 6. 当前业务状态

没有新图页、正式数据或 Worker 回交，因此不能判断共同大尺度背景成立或不成立，不能判断中尺度充分性，不能给 rb/hc/i 排序，也不能形成市场层无候选。合格市场 T 仍为 `0`；脚本与工单不得冒充首个实践包。

<a id="owner-process-feedback"></a>
## 7. 方法反馈

最新 `07` 约定相较 R0002 旧工单更适配高频图数准备：Professional 固定图数和脚本，Worker 只执行、普通修通并核图数对应；不制造无消费者的大型技术报告，结果回原 Professional。大尺度背景—中尺度用例的两层业务过程、as-of 要求、合法无候选与自然挑战均保留。本轮不提出阈值、统一评分、新 Agent 或主过程替换。

<a id="materials-use"></a>
## 8. 材料使用

完整来源及主张映射见 `EVIDENCE_INDEX.md`。本轮实际使用的承重来源包括：

- R0005 `FULL_ASSIGNMENT.md`、`INVOCATION.json`、`SEND_RECEIPT.json`；
- 当前 `01_当前任务.md` 与 `OWNER_START.md`；
- 最新 `OWNER_CHANGE_20261102_CHART_DATA_PREPARATION.md` 与 `07_图数准备工单约定.md`；
- Owner resume、R0004 HOLD、Owner Intake snapshot exception；
- `overlay/12#worker-order-contract`；
- exploration 00—06、30m 工具参考及 Run Guide。

`unread_required: []`

当前不可用：目标 aidata checkout/runtime、最新 SOF 现场数据、新 run 图页和正式切片、合法派发后的 Worker 回交。

<a id="trigger-observations"></a>
## 9. 触发观察

| trigger_id | state | 理由 |
|---|---|---|
| `FIRST_PROCESS_PRACTICE_PACKAGE` | `NOT_YET` | 无实际图数、合格 T、第一层、第二层或挑战结果 |
| `CORE_INPUT_OR_PROCESS_CHANGE` | `NOT_YET` | 只执行 Owner 已授权的局部图数纠正，没有另提业务输入或主过程替换 |
| `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW` | `SATISFIED` | Invocation 记录本轮前有效调用为 1；本轮是第 2 次有效 Professional 调用 |

已形成 `MANAGEMENT_TRIGGER_NOTICE.md`，供控制器路由 `chatgpt:BI-01-CO-05:management`。本 Professional 不声称已实际发送，也不代替 Management 作决定；该触发不替代控制器对已签工单的 `worker-order` 校验和实际派发。

<a id="limitations"></a>
## 10. 限制

1. 脚本只完成静态语法检查。
2. 当前 helper 能否直接实现“一图三品种、相对比例归一化”需现场核；可用当前有权 helper 作不改变方案的兼容修通。
3. `blk@steel` 在最新 Context 是否恰好展开 rb/hc/i需现场核；不一致只改为显式同一集合。
4. 正式工单已签，但控制器尚未对确切签发 commit 运行 `worker-order`，也未实际派发。
5. 无新图数，故无市场结论。

<a id="remaining-scope"></a>
## 11. 完整未完

1. 控制器对包含正式 `WORKER_ORDER.md` 的确切签发 commit 运行现行 `worker-order` 校验。
2. 通过后实际投递至指定 Worker 线程并保留派发证据；不得把签发当作投递。
3. Worker 在固定环境执行、普通修通、实际打开图、读取正式数据并回原 Professional。
4. Professional 消费图数，从第一条合格 as-of T 开始第一层和中尺度充分性判断；有证据时才形成候选/排序/无候选和挑战结论。
5. Management 对本轮投入复看触发作决定，与技术图数结果分别记录。

<a id="continuation"></a>
## 12. 唯一接续

`same_work`

顺序：对确切签发 commit 合法校验 → 实际派发/Worker 回交 → 原 Professional 消费图数 → 从第一条可核 as-of T 开始业务观察。

下一专业问题不变：

> 在返回的同一 run/core 图数中，第一条能够使 rb/hc/i 的共同大尺度背景在当时变得可辨的 T 是什么？该 T 上 large/mid 正式数据是否足以形成具体中尺度候选、排序或合法无候选？

<a id="handoff"></a>
## 13. 回交

- `work_status`: `SUBMITTED`
- `route`: `same_work_after_worker_result_returns_to_issuer`
- `business_artifact_complete_for_this_round`: `true`
- `script_ready`: `true`
- `formal_worker_order_signed`: `true`
- `management_trigger_notice_ready`: `true`
- `first_process_practice_package_claimed`: `false`
- `market_result_claimed`: `false`

本轮成果可用于控制器校验、合法派发和 Management 投入复看，但不得接收为首个市场实践包。

<a id="self-check"></a>
## 14. 自查

- [x] 按最新 Owner 纠正缩窄 Worker 范围，未复投或改写旧工单。
- [x] Professional 自己确定品种、窗口、特征、图面和正式数据，提交完整脚本。
- [x] 使用最新 SOF/tlist，排除 small，要求图数同 run/core。
- [x] 未要求事件账本、方向映射或大型审计。
- [x] 区分静态语法通过与目标环境运行通过。
- [x] 回读控制面独立提交的真实 `COMMITTED` 收据后才签发；未虚构 gate、派发或 Worker 结果。
- [x] 未形成市场假结论；记录第二次有效调用的投入复看触发。
- [x] 保留完整未完与唯一接续。
