order_id: BI01CO05-FULLRANGE-CHART-DATA-R0008-01
work_id: BI-01
run_id: BI-01-CO-05
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-05:professional
issuer_invocation_id: BI01-CO-05-R0008-38f9aa094823
issuer_assignment_token: e81eb24808324350a2e7c24d6094
return_to: chatgpt:BI-01-CO-05:professional
target_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
target_workspace: /dwdhome/fy/cgpterm
state: SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH

# Worker Order：执行 rb/hc/i 30m 全段 large+mid 图数准备

## 0. 签发依据与状态

- control commit: `4f688c6185ea22cabcafc62af9572c05822f0386`
- R0008 `INVOCATION.json` 与 `SEND_RECEIPT.json` 的 invocation/token/recipient 同身份
- `SEND_RECEIPT.state = COMMITTED`
- 旧工单 `BI01CO05-CHART-DATA-R0005-01` 已永久停止新投，不得复用、改名或重派

本文件由当前 Professional 正式签发，但**不声称**已通过 controller `worker-order`、已调用 `codex queue`、已被 Worker 接收或已执行。控制器须以包含本文件的确切 commit 运行现行检查，通过后才能实际投递。

## 1. 唯一技术目标

在 Owner 指定的现有 aidata 环境中执行 Professional 给定脚本，交付：

1. 可实际打开的 `rb/hc/i` 30m 全段同图；
2. 全段主图固定覆盖 `[2021-01-04 00:00:00, 2024-03-01 00:00:00)`；
3. 主图只叠加 `ScaleTurnCalendar("large")` 与 `("mid")`，small 默认关闭；
4. 七个固定半年辅助图，仅用于阅读，不得替代全段主图；
5. 同一 run/core 的正式 30m KLine、large、mid 数据与 manifest/index；
6. 实际覆盖、缺失、重复、warm-up、图数身份和可复核哈希；
7. 完整技术结果返回原签发 Professional。

Worker 不做市场背景、关键 T、候选、排序、无候选、Owner 方法或管理接收判断。

## 2. 固定环境

```yaml
worker_workspace: /dwdhome/fy/cgpterm
aidata_execution_workspace: /dwdhome/fy/BASE_E6_2
aidata_code_dir: /dwdhome/fy/BASE_E6_2/mquant/aidata
sof_name: GTQH_L1_20210104_20240229
stk_tlist: gtqh_four
```

禁止切换 checkout、升级依赖、修改共享 aidata/mquant/tis/FRP 源码或配置、重启/重部署共享服务。

## 3. 脚本、哈希与命令

脚本：

`/dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py`

Professional 固定 SHA-256：

`5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`

执行前必须实测脚本哈希；不一致则停止并报告，不得运行来源不明替代脚本。

```bash
cd /dwdhome/fy/BASE_E6_2
python /dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py
```

目标输出根：

`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data`

## 4. Professional 固定的业务图数语义

```yaml
symbols: [rb, hc, i]
frequency: 30m
main_window: "[2021-01-04 00:00:00, 2024-03-01 00:00:00)"
layers:
  - KLine(freq=30m)
  - ScaleTurnCalendar("large")
  - ScaleTurnCalendar("mid")
small_enabled: false
layout: one_figure_multi_symbol
price_axis: relative_price_ratio_normalization
background_axis_symbol: rb
calendar_policy: source_symbol_own_calendar
identity: chart_and_formal_data_same_run_core
```

辅助窗口固定为 2021H1/H2、2022H1/H2、2023H1/H2 和 2024-01-01 至 2024-03-01。辅助图只能附加，不能替代主图、缩短正式数据范围或按最终走势重选。

以上是 Professional 的业务选择，Worker 不得替换。

## 5. 允许的普通修通

仅当当前有权 API 与脚本存在普通兼容差异时允许：

- import、函数签名、返回对象或序列化的兼容写法；
- 将 `blk@steel` 表达为当前 API 接受、但仍精确解析到 `rb/hc/i` 的等价选择语法；
- 使用当前已有绘图 helper 实现同一固定图面；
- 不改变数据/特征/图面/业务语义的路径修正。

修通必须发生在 Worker 交付目录中的脚本副本或本次 test-run 临时面，保留原脚本，并提交：

- `COMPATIBILITY_COPY.py`
- `COMPATIBILITY_PATCH.diff`
- 修改理由、实际命令和哈希

若修通需改变品种、主/辅窗口、频率、SOF/tlist、large/mid、小尺度状态、图面语义、共享源码、checkout 或依赖，立即停止并回原 Professional。

## 6. 必须实际完成的核验

### 6.1 页面

实际打开全段主图，并逐一核辅助图。仅 URL、路径或退出码不算完成。

`PAGE_INDEX.csv` 至少记录：

- run/core id（若暴露）
- window_id 与 main/aux role
- requested start/end
- page URL/HTML path 与静态导出
- opened 状态
- 可见品种、图层和时间首末
- 相对比例轴、rb 背景轴、日历对齐核验
- notes

主图必须有静态证据；辅助图也须有静态导出或等价可复核证据。

### 6.2 正式数据

实际读取 `build_board_run(..., reuse_core=True)` 返回的：

- delivery manifest
- feature-slice stats
- file index 或 manifest 中等价索引
- `rb/hc/i × KLine_30m/large/mid` 正式切片

`COVERAGE_AND_MISSING.csv` 每个 symbol × layer 至少记录：

- requested start/end
- actual first/last time
- row count
- null/duplicate count
- 空/缺区间说明
- feature effective start 或 warm-up
- source path 与 SHA-256

请求全段不等于实际全段。真实缺口按实报告，禁止补造。

### 6.3 同 run/core 身份

`PAGE_AND_DATA_IDENTITY.json` 至少记录：

- actual run_id
- core_id（若暴露；否则写 `NOT_EXPOSED`）
- page records
- manifest/stats/index 路径与哈希
- 正式切片路径与哈希
- 图与数据同 run/core 的证据
- 无法证明时的具体缺字段

`FORMAL_FILE_INDEX.csv` 逐项列路径、类型、字节、SHA-256、symbol/layer/window 和读取状态。

## 7. 写权与回交

允许写：

- `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data/`
- `runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CHART-DATA-R0008-01/`
- 本次执行产生的临时文件

禁止写共享源码、配置、数据库、其他 Run、原 Professional 脚本/报告/Return。

回交目录至少包含：

```text
FULL_RESPONSE.md
EXECUTION_RECEIPT.json
PAGE_INDEX.csv
COVERAGE_AND_MISSING.csv
PAGE_AND_DATA_IDENTITY.json
FORMAL_FILE_INDEX.csv
STATIC_EVIDENCE/
SHA256SUMS
```

技术结果必须返回 `chatgpt:BI-01-CO-05:professional`，不得向 Management 提交业务接收。

## 8. 失败与停止

任一承重项失败时，报告实际完成范围和具体缺件，不得把部分结果包装成完成：

- 脚本哈希不一致
- 目标环境/数据不可访问
- 全段主图未生成或未打开
- 辅助图替代主图
- 正式切片未实际读取
- 图数同 run/core 无法证明
- 普通修通将改变第 4 节语义
- 需要修改共享源码/checkout/依赖

## 9. Professional 验收边界

只有页面、正式数据、覆盖、身份与兼容修通同时可复核，结果才可进入 Professional 消费。技术 PASS 不等于首个过程实践包，也不等于市场背景或候选规律成立。

Professional 将在验收后从第一条合格 as-of T 开始业务观察；Worker 不得提前给出该结论。
