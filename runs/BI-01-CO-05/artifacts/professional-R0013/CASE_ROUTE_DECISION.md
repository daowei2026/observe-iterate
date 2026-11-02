# CASE_ROUTE_DECISION — R0013

## 当前事实

```yaml
order_id: BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01
worker_status: FAILED_PROBE_EVIDENCE_INCOMPLETE
probe_launcher_attempts: 1
python_probe_started: false
exact_target_open_attempts: 0
exact_target_read_calls: 0
full_run_attempted: false
actual_run_core_created: false
conditional_reentry_quota: CONSUMED_FAILED
same_path_retry_remaining: 0
qualified_market_T_count: 0
```

本次没有得到目标日历文件级别的成功或失败结论。launcher/child 在 Python 探针开始回执前中断，会话返回 143，原因未知。宿主仍观察到 `/m3varI` NFS mount，但没有目标 fd、文件 SHA、fstat 或 Python 异常。

## R0010 退出约束已经满足

R0010 管理已明确：

1. 新工单只允许一次同路径条件重入；
2. 精确探针失败或身份/来源证据不完整时，在全段调用前停止；
3. 不再签第三个同路径 Worker；
4. 管理在“终止当前 Case”与“向 Owner 明示申请改变输入来源/路径”之间决定。

Worker 已按该分支停止并标记 `CONSUMED_FAILED`。因此本 Professional 不再具备同路径续派空间。

## Professional 推荐

`STOP_CURRENT_CASE_ON_CURRENT_INPUT_PATH`

理由：

- 一次管理授权的条件重入已经真实消耗；
- 两次真实 Worker 执行均未产生 actual run/core、图页、正式切片或合格 market T；
- 本次甚至没有进入精确文件 open，继续同路径只能重复未知 launcher/环境状态；
- 原业务问题和 Owner 方法仍未被市场证据检验，不能用更多同类技术轮次替代；
- 继续所需的 calendar source/path/resolver 或正式入口变化，已经不是普通兼容。

该推荐只关闭**当前 Case 的当前输入路径**，不关闭 Owner 的长程研究问题，也不形成市场或方法失败结论。

## Management 的两个合法选项

### A. 终止当前 Case（推荐）

```yaml
decision: STOP_CURRENT_CASE_ON_CURRENT_INPUT_PATH
reason_class: AUTHORIZED_EXECUTION_PATH_AND_ENVIRONMENT_COST_EXHAUSTED
market_conclusion: NONE
method_conclusion: UNTESTED
preserve:
  - R0008 full-range design and fixed script
  - R0008 Worker failure evidence
  - R0011 conditional-reentry order
  - R0011 Worker failure evidence
  - R0013 Professional consumption
```

Management 更新完整推进位置并关闭本 Case。不得写成“市场没有背景”“特征不足”或“Owner 方法失败”。

### B. 向 Owner 申请核心输入变化

```yaml
decision: REQUEST_OWNER_AUTHORIZATION_FOR_CORE_INPUT_CHANGE
immediate_worker_dispatch: FORBIDDEN
required_before_execution:
  - explicit new source/path/resolver/formal-entry proposal
  - impact on calendar, members, trading sessions, UTI and feature locations
  - identity plan for chart and formal data
  - invalidated versus reusable prior evidence
  - Owner confirmation and new authorized task
```

可能变化包括 calendar source/path、resolver 或正式数据入口。任何一项都不得伪装成脚本兼容、复制旧日历、临时旁路或第三次同路径重试。

## 不允许的后继

- 重新派 `BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01`；
- 签第三个同路径 Worker；
- 等待无责任主体的环境恢复后自动继续；
- 从 R0008 errno 5 推断本次文件状态；
- 使用 mount 存在、路径存在或 exit 143 代替文件可读性；
- 建立平行数据库或外部行情入口；
- 在无图数时形成背景、候选或无候选。

## 若 Owner 授权新输入后的完整业务未完

1. 建立新输入身份、版本、日历、成员、覆盖和图数同身份合同；
2. 生成并实际打开全段主图及必要辅助图；
3. 程序读取正式 KLine/large/mid 及 manifest/index；
4. 核 actual/confirm/event/revision、方向来源和当前发展部分；
5. 从第一条合格 as-of T 开始第一层；
6. 同 T 检查中尺度充分性，形成候选、排序或合法无候选；
7. 随新信息更新并检查自然挑战；
8. 回交首个可消费实践包与 Owner 过程反馈。
