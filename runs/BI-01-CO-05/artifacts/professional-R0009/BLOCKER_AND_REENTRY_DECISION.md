# BLOCKER_AND_REENTRY_DECISION — R0009

## 裁定

```yaml
blocker: EXECUTION_ENVIRONMENT_IO_BLOCKER
location: /m3varI/var/L1_data/sof/unit/affiliated_calendar_no_night.csv
observed_exception: OSError(errno=5)
attempts: 1
persistence: UNKNOWN
core_created: false
market_data_read_reached: false
immediate_retry: NOT_AUTHORIZED
new_worker_order_this_round: NONE
recommended_route: MANAGEMENT_DECIDE
recommended_decision: CONDITIONAL_CONTINUE_AFTER_RECOVERY_EVIDENCE
```

## 为什么不是市场结果

失败发生在 aidata 默认日历解析阶段，先于 core/run、页面和 board。于是：

- 不能说行情为空、SOF 不存在或 2024-02-29 无数据；
- 不能说 large/mid 没有对象；
- 不能说共同大尺度背景不存在；
- 不能形成候选、排序或合法无候选；
- 覆盖、行数、空值、重复和 warm-up 均是 `UNKNOWN`，不是 0。

## 为什么不直接重复派发

1. 原 Worker 已按停止条件终止，queue 为空，无自动重试。
2. 只有一次文件读取失败，持久性未知；在恢复证据前重复派发没有新增信息价值。
3. 当前任务段已使用一个 Worker，R0009 又达到两次有效 Professional 调用的投入复看点。
4. 修共享 NFS、复制日历文件或替换 resolver 超出原 Worker 写权。
5. 替换日历来源可能改变输入身份，不能伪装成普通兼容修通。

## 恢复证明

由有权限方在**同一目标 workspace、同一 Python 入口、同一权限身份**下提供：

```text
exact path open/read succeeds
+ observed timestamp
+ byte count
+ sha256
+ exit code and stderr
+ current /m3varI mount source
+ no stale copy / no alternative source
```

仅 `ls`、`stat`、路径存在、挂载存在或远端 ping 不足以证明恢复。

## 恢复后的分支

### A. 原文件恢复，输入身份不变

- 保留 R0008 脚本 SHA 和全部业务参数；
- 原 Professional 签发一个新的窄重试工单；
- controller 机械校验并真实派发；
- Worker 从头执行，不复用失败 attempt 的预请求 run_id；
- 技术结果回原 Professional 消费。

### B. 需要替代文件、绕过 resolver 或新数据入口

先停止重试，提交 `CORE_INPUT_OR_PROCESS_CHANGE` 评估，说明：

- 新旧 calendar source；
- 对成员展开、交易日、夜盘边界、UTI 和正式切片的影响；
- 图与正式数据是否仍能保持同 run/core；
- 哪些既有主张失效。

未经决定不得把 B 路径当作 A 的兼容修通。

## 业务接续

恢复并取得合格图数后，Professional 才从第一条合格 as-of T 开始：

1. 核 actual/confirm/event/revision 与方向来源；
2. 识别共同大尺度背景何时可辨、变化或失效；
3. 在同一 T 检查中尺度充分性；
4. 形成候选、排序或合法无候选；
5. 随新信息更新并检查自然挑战。
