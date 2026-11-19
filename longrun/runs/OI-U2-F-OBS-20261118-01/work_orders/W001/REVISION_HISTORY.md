# W001 修订历史

## 动作身份

```text
run_id=OI-U2-F-OBS-20261118-01
work_order_id=W001
parent_delegation_id=D005
worker=codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
```

W001 是同一个可去重动作。以下修订没有创建 W002，也没有改变原 D005、WI-E 或 M-E。

## 版本 1｜C0012 原始发布

- 正文：`daowei2026/observe-iterate@cfc1fabc0f910434743cea514ea28f674a35dcd0:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.md`
- 机读：`daowei2026/observe-iterate@17840c4dbc8493636ce75d07859ceecb31d885e7:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json`
- issuer call：`C0012`
- 动作事实：仅发布；未物理发送、未执行、未创建 Worker goal、无 Worker Return。
- 后来发现的限制：授权引用仍指旧 Binding；正文把“工作区内已有本 Run observe-iterate 工作树”作为未证实前提。

## 版本 2｜C0013 当前活跃修订

- 正文：`daowei2026/observe-iterate@973c0da06c28b0ce7f343205858d9002f97667c9:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.md`
- 机读：`daowei2026/observe-iterate@74562f258d93fdea8db0ab334fb0ebb23f1cfb99:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json`
- E1 基准：`daowei2026/observe-iterate@1a4d2e455a1175f1c20226fa9873c587c697021d:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E1_EXECUTION_AND_REVIEW_BASELINE_C0013.md`
- issuer call：`C0013`
- 动作事实：已发布、尚未物理发送或执行。

### 修订原因

1. Owner 已确认新的机读授权文本；
2. 当前 Run/Resource Binding 已登记修正后的绝对路径和真实 Worker binding；
3. 有限现场检查没有证实工作区内存在可直接运行的 observe-iterate 工作树。

### 修订内容

- grant 的 `operation / execution_context / allowed_writes / authority_quote` 与 `RUN_BINDING@4d2eb...` 精确对齐；
- input refs 增加 Owner 授权补正、新 Binding、物理 Worker binding、C0012 Return 和旧 W001 历史；
- 保持 `work_order_id=W001`；
- 采用授权工作区内、固定 D commit 的 run-local detached source staging；
- 把输出、日志、diff 和 staging report 固定在本 Run/W001 专用目录；
- 保留“不重跑 F producer、不得改变实例／位置／字段／展示语义”的原停止边界。

## 当前路由

主控只应派发 C0013 当前活跃机读工单。Worker Return 的 `order_ref` 必须指向：

`daowei2026/observe-iterate@74562f258d93fdea8db0ab334fb0ebb23f1cfb99:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json`

收到 Return 后继续原 `D005 / WI-E / M-E`，由原 executor:E1 进行 E2/E3 专业消费。发布、绑定、发送和运行均不能单独视为 E 完成。
