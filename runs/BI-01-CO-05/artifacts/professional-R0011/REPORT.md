# BI-01-CO-05 Professional R0011：一次性条件重入 Worker 工单签发

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-05`
- `invocation_id`: `BI01-CO-05-R0011-e186238bf811`
- `assignment_token`: `ade5d48ee39949aa99991f4b0a39`
- `role`: `professional`
- `question_id`: `CASE-OWNER-PROCESS-PRACTICE-01`
- `route`: `same_work`
- `effective_professional_call_after_R0010_reset`: `1`

<a id="decision-summary"></a>
## 1. 裁定摘要

本轮严格执行 R0010 管理决定，只把已采用的“一次性同身份探针→条件全段执行”转成新的正式 Worker 工单；没有重做来源调查、重新设计图数、等待无责任主体的外部证明，也没有把旧工单改名继续。

正式签发：

```yaml
order_id: BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01
order_path: runs/BI-01-CO-05/artifacts/professional-R0011/WORKER_ORDER.md
target_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
target_workspace: /dwdhome/fy/cgpterm
state: SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH
```

签发依据为控制面提交 `4699c3c947753f65d0a3f3ff044f5c74d68fdc3b`：R0011 `INVOCATION.json` 与 `SEND_RECEIPT.json` 同身份，`SEND_RECEIPT.state=COMMITTED`。

本工单保持 R0008 原脚本及全部业务输入不变：

- `rb/hc/i`；
- 30m；
- large+mid，small 关闭；
- `GTQH_L1_20210104_20240229 / gtqh_four`；
- 主范围 `[2021-01-04 00:00:00, 2024-03-01 00:00:00)`；
- 全段主图加七个先验辅助图；
- 图与正式数据同 run/core；
- 原脚本 SHA-256 `5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`。

唯一新增的是 R0010 已授权的执行反馈回路：同一 Worker、同一目标 workspace/Python/权限身份先对精确日历文件做一次真实 `open/read-to-EOF`；失败则在全段脚本前停止且同路径额度耗尽；通过则立即从头执行原脚本一次并交全段图数。

当前未运行 controller preflight，未实际派发，Worker 未执行，图数未返回，合格 market T 仍为 `0`。这不是市场无背景或无候选结论。

<a id="completed-scope"></a>
## 2. 本轮已完成范围

1. 全文读取 R0011 派发、当前任务、Owner 目的、专业模式、图数工具/数据边界、Owner 完整过程、Run Guide 与现行 Worker 合同。
2. 读取 R0010 完整管理回交及第 6 节一次性条件重入决定，直接采用其已完成的材料裁定、旧要求撤销和执行安排。
3. 核 R0011 invocation/token/recipient、Binding、route 和 `COMMITTED` 发送记录。
4. 核 R0008 原脚本仍在当前分支，Git blob 未变，固定 SHA-256 保持有效。
5. 核上次真实执行入口、业务 Python、精确失败文件、mount source 和失败发生位置。
6. 新建独立 `order_id`，使用 R0011 真实签发身份；旧 R0008 order 保持终态，不复用。
7. 把同身份探针、通过/失败分支、一次性额度、普通兼容边界、停止条件、写权、图数验收和回交要求完整写入正式工单。
8. 明确 controller 必须对包含该 order 的确切提交运行 `worker-order`，通过后才可真实派发。
9. 保留业务未完、触发状态、材料使用、限制和两份 Return 所需承重内容。

<a id="order-content"></a>
## 3. 新工单的承重内容

### 3.1 探针

精确文件：

`/m3varI/var/L1_data/sof/unit/affiliated_calendar_no_night.csv`

同一 Worker 执行记录：workspace、cwd、uid/euid/gid/groups、Python launcher/executable/version、当前 `/m3varI` mount source、精确路径/realpath、read-to-EOF 字节数、fstat size、SHA-256、时间、exit/stdout/stderr 与异常。

通过条件要求 mount 仍为 `/m3varI`、source 仍为 `192.168.9.79:/m3varI`，且未使用复制、旧快照、替代 source/resolver、权限切换或平行入口。

### 3.2 探针失败

- 全段脚本不运行；
- 不作第二次探针；
- `conditional_reentry_quota=CONSUMED_FAILED`；
- 回交精确失败与身份/mount 证据；
- 原 Professional 消费后不得签第三个同路径工单，回 Management 决定停止 Case或申请有权输入变化。

### 3.3 探针通过

在同一 Worker 执行中立即：

- 重新核原脚本 SHA；
- 用 `/dwdhome/fy/BASE_E6_2/run-python.sh` 从头运行原脚本一次；
- 使用 fresh dynamic run_id；
- 不复用旧失败 attempt 的预请求 id；
- 实际开全段主图和七个辅助图；
- 实际读取同 run/core manifest/index/KLine/large/mid；
- 回交覆盖、缺失、warm-up、哈希和图数身份。

普通兼容修通仍受 R0008 原边界限制；若需要第二次昂贵业务运行、改变 source/resolver/calendar/NFS/共享源码/checkout/依赖或业务参数，停止并回原 Professional。

<a id="business-state"></a>
## 4. 当前业务状态

| 项目 | 状态 |
|---|---|
| 原 R0008 order | `TERMINAL_NO_REDISPATCH` |
| 新 R0011 order | `SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH` |
| controller `worker-order` | 未运行/未声称 |
| 实际派发 | 未发生/未声称 |
| Worker 结果 | 无 |
| 全段图数 | 无 |
| 合格 market T | `0`（证据资格状态） |
| 第一层 | 未开始 |
| 第二层 | 未开始 |
| 首个实践包 | 未满足 |

本轮只完成已授权技术委派，不形成市场、特征不足、候选、无候选或 Owner 方法结论。

<a id="materials-use"></a>
## 5. 材料使用记录

已读取并实际使用：

- R0011 `FULL_ASSIGNMENT.md`、`INVOCATION.json`、`DISPATCH.json`、已提交 `SEND_RECEIPT.json`；
- 当前 `01_当前任务.md` 与 Question Work Binding；
- R0010 `FULL_RESPONSE.md`、`DECISION.md`、两份 Return，重点采用第 6 节和 continuation；
- R0008 原脚本、原工单和 Professional 报告；
- Worker R0008 失败执行 `EXECUTION_RECEIPT.json`；
- R0009 Worker 结果消费与管理触发；
- `overlay/12_管理接收与地图校验.md#worker-order-contract`；
- `professional/README.md`、exploration 00—07、30m 工具参考、Run Guide、Owner GO。

`unread_required: []`

明确未重新开展：旧宽输入调查、45 天窗设计、事件账本/全面方向审计、外部行情、平行数据库或新的业务方法设计。

<a id="trigger-observations"></a>
## 6. 触发观察

| trigger_id | state | 理由 |
|---|---|---|
| `FIRST_PROCESS_PRACTICE_PACKAGE` | `NOT_YET` | 无图数、合格 T、第一/第二层判断 |
| `CORE_INPUT_OR_PROCESS_CHANGE` | `NOT_YET` | 工单保持 R0008 输入和 Owner 过程不变 |
| `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW` | `NOT_YET` | R0010 已重置；本轮为新段第 1 次有效 Professional 调用 |

<a id="limitations"></a>
## 7. 限制

1. 本通道不能执行 controller 的本地 `workmap_gate.py worker-order` 或目标 Worker 任务。
2. 本轮没有目标环境运行、探针结果、图页、manifest/index 或正式切片。
3. 技术执行结果只能由实际 Worker 回交，不能从已签工单推断。
4. 签发不等于派发、执行、技术 PASS 或业务接收。

<a id="remaining-scope"></a>
## 8. 完整未完

1. 控制器以包含本工单的确切 commit 运行现行 `worker-order` preflight。
2. 通过后真实投递到线程 `01a17dd7-5033-7e63-b7a2-edd90b691c33`。
3. Worker 先执行同身份精确文件读探针，按工单分支停止或运行原 R0008 全段脚本一次。
4. Worker 技术结果按 `worker-result` 返回原 Professional。
5. 探针失败：Professional 同调用消费后不签第三单，回 Management 决定停止当前 Case或提出有权输入变化。
6. 技术成功：Professional 同调用核证据资格并立即从第一条合格 as-of T 开始第一层业务观察。
7. 第一层后在同一 T 检查中尺度充分性，形成候选、排序或合法无候选并随新信息更新。
8. 检查自然挑战和失败片段，形成业务成果与 Owner 过程反馈。

<a id="continuation"></a>
## 9. 唯一接续

`same_work_after_worker_result_returns_to_issuer`

```text
controller worker-order preflight
→ 实际派发新 order
→ 同身份精确读探针
→ [失败：停止且额度耗尽，回 Management]
   或
   [通过：原 R0008 全段脚本单次执行]
→ Worker 回交 / worker-result
→ 原 Professional 消费
→ 技术成功则立即开始 as-of 第一层业务观察
```

<a id="handoff"></a>
## 10. 回交

- `work_status`: `SUBMITTED`
- `route`: `same_work_after_worker_result_returns_to_issuer`
- `formal_worker_order_signed`: `true`
- `controller_preflight_claimed`: `false`
- `worker_dispatch_claimed`: `false`
- `worker_result_claimed`: `false`
- `first_process_practice_package_claimed`: `false`
- `market_result_claimed`: `false`

<a id="self-check"></a>
## 11. 自查

- [x] 使用新 order_id 和 R0011 真实签发身份；未改名复用旧 order。
- [x] 签发前核到同轮 `SEND_RECEIPT.state=COMMITTED`。
- [x] 保留 R0008 原脚本和全部业务参数。
- [x] 只加入 R0010 已授权的一次性探针反馈回路。
- [x] 探针通过/失败、额度、停止、写权和回交均明确。
- [x] 未宣称 preflight、派发、执行、图数或市场结果。
- [x] 未重做来源调查、图数设计或 Owner 方法。
- [x] 保留完整未完和唯一接续。
