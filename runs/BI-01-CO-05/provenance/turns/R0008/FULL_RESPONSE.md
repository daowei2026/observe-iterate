# BI-01-CO-05 Professional R0008：全段图数脚本与新 Worker 工单

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-05`
- `invocation_id`: `BI01-CO-05-R0008-38f9aa094823`
- `assignment_token`: `e81eb24808324350a2e7c24d6094`
- `role`: `professional`
- `question_id`: `CASE-OWNER-PROCESS-PRACTICE-01`
- `effective_professional_call_after_R0006_reset`: `1`

<a id="decision-summary"></a>
## 1. 裁定摘要

本轮落实 Owner 全段纠正与 R0006 接续，交付全段图数设计、aidata 脚本和新 Worker 工单；不是市场观察结果。

```yaml
symbols: [rb, hc, i]
frequency: 30m
main_window: "[2021-01-04 00:00:00, 2024-03-01 00:00:00)"
layers: [KLine_30m, ScaleTurnCalendar_large, ScaleTurnCalendar_mid]
small_enabled: false
sof_name: GTQH_L1_20210104_20240229
stk_tlist: gtqh_four
identity: chart_and_formal_data_same_run_core
```

全段主图必需；七个半年分段仅辅助阅读。脚本静态检查通过，目标环境未执行。

新工单 `BI01CO05-FULLRANGE-CHART-DATA-R0008-01` 已签发，待 controller 校验与派发；签发不等于执行或结果。

当前：图数未取得；合格市场 T=`0`；两层观察未开始；路线=`same_work`。

<a id="completed-scope"></a>
## 2. 已完成范围

1. 读取 R0008 派发/身份，核 Binding、R0006 管理采用、R0007 关联补齐。
2. 落实 Owner 时间纠正：否定 45 天主窗，改为完整 SOF 范围。
3. 保留 `rb/hc/i`、30m、large/mid、无 small、最新 SOF/tlist、同 run/core。
4. 新建脚本，SHA-256：`5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`。
5. 接入 `build_chart_run → build_big_world_chart_pages → build_board_run(reuse_core=True)`，固定主窗与七个辅助窗。
6. 将 manifest、slice stats、index、覆盖/缺失和身份核验写入合同。
7. `py_compile` 与 AST 均 PASS；未冒充目标运行时。
8. 形成机器请求、静态校验、证据索引、正式工单和 manifest。
9. 明确 Worker 仅执行、普通修通、开图、读正式数据并回交。
10. 保留材料、限制、未完、触发和 Return 承重内容。

<a id="owner-correction"></a>
## 3. 全段图数合同

主范围：`[2021-01-04 00:00:00, 2024-03-01 00:00:00)`。

请求范围不等于实际覆盖。源数据首末、缺口、重复、空值、warm-up 与有效起点必须实测，不得补造。

主图：`rb/hc/i` 同一 Figure；相对价格比例归一化；`rb` 背景轴；各品种自身日历；large=L 三角形，mid=M 菱形；small 关闭。

辅助窗先验固定为 2021H1/H2、2022H1/H2、2023H1/H2、2024-01-01 至 2024-03-01，只辅助阅读。

<a id="script"></a>
## 4. 新脚本

`runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py`

```bash
cd /dwdhome/fy/BASE_E6_2
python /dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py
```

输出：`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data`

当前通道没有目标 checkout、SOF 或 runtime，故不声称 import、API、图页或数据通过。

<a id="worker-order"></a>
## 5. 新 Worker 工单

- `order_id`: `BI01CO05-FULLRANGE-CHART-DATA-R0008-01`
- 路径：`runs/BI-01-CO-05/artifacts/professional-R0008/WORKER_ORDER.md`
- 线程：`01a17dd7-5033-7e63-b7a2-edd90b691c33`
- workspace：`/dwdhome/fy/cgpterm`
- 签发依据：`4f688c6185ea22cabcafc62af9572c05822f0386`
- `SEND_RECEIPT.state`: `COMMITTED`

Worker 只执行脚本、普通兼容修通、实际开主/辅图、读取同 run/core KLine/large/mid，并回交覆盖、缺失、索引、哈希和身份。

排除事件账本、方向审计、关键 T、市场判断、方法/管理接收及共享源码变更。

本轮不声称 controller 已运行 `worker-order`、已派发、Worker 已执行或结果已被消费。

<a id="business-state"></a>
## 6. 业务状态

全段同身份图数尚未返回，共同背景可辨 T、背景演变、中尺度充分性、候选/排序/无候选和自然挑战均未知。

`qualified_market_T_count = 0` 是证据状态，不是“市场没有背景/候选”。技术 PASS 也不会自动产生合格 T；Professional 仍须核字段层级与 actual/confirm/event/revision。

<a id="process-feedback"></a>
## 7. 过程反馈

45 天窗不能承载大尺度形成与演变；全段主图、先验辅助图及同 run/core 数据足以进入下一步。请求范围与实际有效覆盖须分开，缺失/warm-up 按实报告。当前不替换 Owner 两层过程，也不新增规范、评分器或 Agent。

<a id="materials-use"></a>
## 8. 材料使用

已使用：R0008 派发/控制文件、当前任务/Binding、Owner 时间纠正、R0006 决定、R0007 补齐、R0005 原实现（只核影响）、exploration 00—07、30m 参考、Run Guide、`worker-order-contract`。

`unread_required: []`。未使用旧宽调查、45 天窗/旧身份、外部行情、平行数据库或结果倒选窗口。

<a id="trigger-observations"></a>
## 9. 触发观察

| trigger_id | state | 理由 |
|---|---|---|
| `FIRST_PROCESS_PRACTICE_PACKAGE` | `NOT_YET` | 无全段图数、合格 T 或两层判断 |
| `CORE_INPUT_OR_PROCESS_CHANGE` | `NOT_YET` | 只执行已授权时间纠正 |
| `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW` | `NOT_YET` | R0006 已重置；本轮为第 1 次有效调用 |

<a id="limitations"></a>
## 10. 限制

目标 runtime 不可用；脚本未执行；图、manifest/index 和切片未生成；覆盖/缺失/warm-up 未知；preflight、派发和回交未发生。

<a id="remaining-scope"></a>
## 11. 完整未完

1. 控制器以确切工单 commit 运行 `worker-order`，通过后真实派发。
2. Worker 核脚本 SHA、执行/普通修通，开主辅图并读 manifest/index/KLine/large/mid。
3. Worker 回交页面、覆盖、缺失、索引、哈希、同 run/core 身份和阻断。
4. 结果按 `worker-result` 返回原 Professional。
5. Professional 核字段层级、actual/confirm/event/revision、方向来源、日历和发展部分。
6. 从第一条合格 as-of T 开始第一层，并在同一 T 检查中尺度充分性。
7. 形成候选、排序或合法无候选，更新并检查滞后、错位、短空间、反向负担和邻近失败。
8. 形成业务成果与过程反馈，再按触发条件回 Management。

<a id="continuation"></a>
## 12. 唯一接续

`same_work`

```text
controller preflight → 实际派发 → Worker 回交 → worker-result 核验
→ 原 Professional 消费图数 → 从第一条合格 as-of T 开始两层判断
```

下一问题：在返回的同一 run/core 全段图数中，第一条使 `rb/hc/i` 共同大尺度背景当时可辨的 T 是什么；该 T 上 large/mid 是否足以形成中尺度候选、排序或合法无候选？

<a id="handoff"></a>
## 13. 回交

- `work_status`: `SUBMITTED`
- `route`: `same_work_after_worker_result_returns_to_issuer`
- `script_ready`: `true`
- `formal_worker_order_status`: `SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH`
- `worker_result_claimed`: `false`
- `first_process_practice_package_claimed`: `false`
- `market_result_claimed`: `false`

<a id="self-check"></a>
## 14. 自查

- [x] 未复用旧身份；全段主图不可由辅助窗替代。
- [x] 图数语义、SOF/tlist 与同 run/core 保持不变。
- [x] 区分静态 PASS 与运行时 PASS；未编造图数或市场结论。
- [x] Worker 只执行/修通/开图/读数/回交；未完与接续完整。
