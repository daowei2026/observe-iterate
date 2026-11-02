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
- R0008 `INVOCATION.json` 与 `SEND_RECEIPT.json` invocation/token/recipient 同身份；
- `SEND_RECEIPT.state = COMMITTED`；
- 本文件由原 Professional 按 Owner 全段纠正重新签发；
- 旧工单 `BI01CO05-CHART-DATA-R0005-01` 已停止新投，不得复用、改名或重复派发；
- 本文件不声称已运行 `worker-order`、已调用 `codex queue`、已被 Worker 接收或已执行。

控制器必须以包含本文件的确切 commit 运行现行 `worker-order` 检查，通过后才可投递至上述线程。

## 1. 技术目标

在 Owner 指定的现有 aidata 环境中，执行 Professional 已给定的 Python 脚本，交付：

1. 一张实际可打开的 `rb/hc/i` 30m 全段主图；
2. 主图固定覆盖 `[2021-01-04 00:00:00, 2024-03-01 00:00:00)`；
3. 图中只叠加 `ScaleTurnCalendar("large")` 与 `("mid")`，不默认启用 small；
4. 七张按固定半年边界切分的辅助可读图；辅助图不得替代主图；
5. 与上述图完全同一 run/core 的正式 30m KLine、large、mid 数据、delivery manifest、feature-slice stats 及可定位索引；
6. 对实际时间覆盖、缺失/空值/重复、图数身份和页面可读性的真实核验；
7. 一份完整、可由原 Professional 继续消费的 `FULL_RESPONSE.md`。

Worker 只执行、普通修通、实际开图、读取正式数据和回交，不判断市场背景、关键 T、候选、排序、无候选、Owner 方法或管理接收。

## 2. 固定环境

- Worker 聊天工作区：`/dwdhome/fy/cgpterm`
- aidata 执行工作区：`/dwdhome/fy/BASE_E6_2`
- aidata 目录：`/dwdhome/fy/BASE_E6_2/mquant/aidata`
- `sof_name="GTQH_L1_20210104_20240229"`
- `stk_tlist="gtqh_four"`
- 不切换 checkout，不升级依赖，不修改共享平台源码，不重启或重部署共享服务。

## 3. 确定脚本与命令

脚本：

`/dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py`

提交路径：

`runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py`

Professional 固定 SHA-256：

`5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`

执行前必须实测脚本 SHA-256 与上值一致；不一致则停止并报告，不运行来源不明替代脚本。

命令：

```bash
cd /dwdhome/fy/BASE_E6_2
python /dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py
```

目标输出根：

`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data`

## 4. Professional 已固定的图数语义

### 4.1 主输入

- 品种：`rb / hc / i`，必须恰好为这三个；
- K 线：`30m`；
- 主窗口：`[2021-01-04 00:00:00, 2024-03-01 00:00:00)`；
- 主窗口 ID：`BI01-CO05-FULL-20210104-20240301`；
- 正式图数层：
  - `KLine(freq="30m")`
  - `ScaleTurnCalendar("large")`
  - `ScaleTurnCalendar("mid")`
- 不启用 `small`；
- 一张 Figure 同时展示三品种；
- 价格线按相对价格比例归一化；
- `rb` 为背景轴；
- 各品种使用源自身日历，并核窗口内实际时间轴对齐。

这些是业务选择，不得由 Worker 替换。

### 4.2 固定辅助分段

辅助分段只为阅读，不缩短正式主范围：

| window_id | start | end_exclusive |
|---|---|---|
| `BI01-CO05-AUX-2021H1` | 2021-01-04 | 2021-07-01 |
| `BI01-CO05-AUX-2021H2` | 2021-07-01 | 2022-01-01 |
| `BI01-CO05-AUX-2022H1` | 2022-01-01 | 2022-07-01 |
| `BI01-CO05-AUX-2022H2` | 2022-07-01 | 2023-01-01 |
| `BI01-CO05-AUX-2023H1` | 2023-01-01 | 2023-07-01 |
| `BI01-CO05-AUX-2023H2` | 2023-07-01 | 2024-01-01 |
| `BI01-CO05-AUX-2024P` | 2024-01-01 | 2024-03-01 |

不得用这些辅助图替代全段主图。不得根据最终走势临场增加“看起来更好”的局部窗；后续业务局部放大由 Professional 在消费图数后另行决定。

## 5. 执行顺序

1. 在目标 workspace 核对确切工单 commit、脚本路径和 SHA-256。
2. 记录实际 checkout commit、Python 版本和命令；不做全仓 diff 审计。
3. 运行脚本；完整保存 stdout、stderr、退出码和 run_id。
4. 若发生普通 API/路径/序列化兼容问题：
   - 只能在 Worker 交付目录或本次 test-run 临时副本中修通；
   - 保留原脚本不变；
   - 生成修订脚本副本和精确 diff；
   - 不改变第 4 节的任何业务语义；
   - 如需修改共享源码、换 checkout、升级依赖或改变业务输入，立即停止并回原 Professional。
5. 实际打开全段主图，不得只凭 URL、路径或退出码判断成功。
6. 逐一打开/核验辅助图；辅助图失败不得包装成主图成功，主图失败则本工单未完成。
7. 实际读取 `build_board_run(..., reuse_core=True)` 返回的 delivery manifest、feature-slice stats、文件索引/manifest 引用及 rb/hc/i 三层正式切片。
8. 验证图与正式数据属于同一 run/core；记录可核字段、路径和哈希。若 core id 不暴露，明确写 `NOT_EXPOSED`，不得猜。
9. 按第 6 节输出技术回交；任一承重项失败时准确列缺任，不把部分结果包装成完成。

## 6. 必须核验和交付

### 6.1 页面

`PAGE_INDEX.csv` 至少包含：

- run_id / core_id_if_exposed
- window_id / role(main or auxiliary)
- requested_start / requested_end_exclusive
- actual_page_url_or_html_path
- static_export_path
- opened
- visible_symbols
- visible_layers
- visible_time_start / visible_time_end
- relative_ratio_axis_checked
- rb_background_axis_checked
- calendar_alignment_checked
- notes

全段主图必须另提供可复核静态导出；辅助图也提供静态导出或等价可打开证据。

### 6.2 正式数据覆盖

`COVERAGE_AND_MISSING.csv` 每个 `symbol × layer` 至少一行，字段：

- run_id / core_id_if_exposed
- symbol
- layer (`kline_30m / large / mid`)
- requested_start / requested_end_exclusive
- actual_first_time / actual_last_time
- row_count
- null_time_count
- duplicate_time_count
- empty_or_missing_interval_notes
- feature_effective_start_or_warmup_note
- source_path
- sha256

请求范围不是实际覆盖结论。源数据、交易日或特征有效覆盖不足时按真实值报告，不补造空缺。

### 6.3 同身份与索引

`PAGE_AND_DATA_IDENTITY.json` 至少记录：

- actual run_id；
- core_id（如暴露）；
- page records；
- delivery manifest path/hash；
- feature-slice stats path/hash；
- file index path/hash，或 manifest 中的确切索引定位；
- 每个正式切片的 path/hash；
- 图与数据同 run/core 的证据；
- 无法证明的身份字段。

`FORMAL_FILE_INDEX.csv` 逐项列路径、文件类型、字节数、sha256、对应 symbol/layer/window 和读取状态。

### 6.4 回交文件

写入：

`runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CHART-DATA-R0008-01/`

至少包含：

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

发生兼容修通时另含：

```text
COMPATIBILITY_COPY.py
COMPATIBILITY_PATCH.diff
```

`FULL_RESPONSE.md` 顶部必须保留：

- `order_id`
- `work_id`
- `run_id`
- `return_to`
- `issuer_invocation_id`

并准确记录实际执行、退出状态、页面是否打开、正式数据是否读取、修通、缺件及所有交付位置。

## 7. 写权

允许写：

- `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data/`
- `runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CHART-DATA-R0008-01/`
- 本次执行所需临时文件。

禁止写：

- 共享 aidata/mquant/tis/FRP 源码和配置；
- 本 Professional 原脚本、报告、Return；
- 旧 R0005 工单/脚本和其他 Run 成果；
- 数据库、服务配置或全局环境。

不得重启、重部署共享服务。

## 8. 业务边界与非目标

Worker 不得：

- 判断共同大尺度背景何时成立、改变或失效；
- 定义关键 T、候选、排序或无候选；
- 重建 first-visible/revision 事件账本；
- 做全面方向映射、字段审计或环境审计；
- 修改 Owner 05、正式任务、Binding 或管理决定；
- 宣称技术 PASS 等于首个业务实践包；
- 向 Management 交业务接收。

技术结果必须回原签发 Professional 消费。Professional 将在核验证据资格后从第一条合格 as-of T 开始业务观察。

## 9. Professional 验收条件

只有同时满足下列条件，结果才可进入 Professional 消费：

1. 全段主图实际打开，且窗口、品种、频率、large/mid、无 small 均核实；
2. 辅助图只是附加视图，不替代主图；
3. 正式 KLine/large/mid 数据实际读取；
4. actual coverage、缺失/空值/重复及特征有效起点如实列出；
5. manifest、stats、索引和切片路径可定位并有哈希；
6. 图与正式数据同一 run/core 有可复核依据；
7. 所有兼容修改未越过第 5 节边界；
8. 任何未满足项被明确标成失败或未知，而不是默认通过。

满足技术验收不等于市场背景、候选规律或 Owner 方法有效。后者仍由原 Professional 决定。
