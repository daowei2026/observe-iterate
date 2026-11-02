order_id: BI01CO05-CHART-DATA-R0005-01
work_id: BI-01
run_id: BI-01-CO-05
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-05:professional
issuer_invocation_id: BI01-CO-05-R0005-39b928f3b0b1
issuer_assignment_token: 06b1e5482b6b4651a68af7fb774bc42
return_to: chatgpt:BI-01-CO-05:professional
target_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
target_workspace: /dwdhome/fy/cgpterm
state: SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH

# Worker Order：执行 rb/hc/i 30m large+mid 图数准备

## 0. 签发状态

`SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH`

签发依据：控制面提交 `748de226b79aa66044d60c1dfa5a4b6ac48b138a` 中，本轮 `INVOCATION.json` 与 `SEND_RECEIPT.json` 的 invocation/token/recipient 同身份，`SEND_RECEIPT.state=COMMITTED`，并记录 `exact_round_marker_verified=true`、`payload_verification=exact_verified`。本 Professional 回读后签发本工单；没有修改或补造控制收据。

本文件是正式签发工单，但不声称已通过 `worker-order` 机械检查、已调用 `codex queue`、已被 Worker 接收或已执行。控制器必须以包含本文件的确切 commit 运行现行检查，通过后才可投递。订单内容不得在校验/派发时被操作主控重新选择或改写。

## 1. 技术目标

在 Owner 指定的现有 aidata 环境中执行 Professional 已给定脚本，必要时做普通兼容修通，并实际交付：

1. 一张可实际打开的 rb/hc/i 30m 同图；
2. 图中叠加 large 与 mid 两套 `ScaleTurnCalendar` 转折，不画 small；
3. 三品种价格按相对价格比例归一化，rb 作为背景轴；各品种使用源自身日历，并核本窗口时间轴是否对齐；
4. 与该图同一 run/core 的正式 30m KLine、large、mid 数据及可定位这些切片的 delivery manifest/索引；
5. 一份简明 `FULL_RESPONSE.md`，把真实执行、页面、数据、对应关系、修正与缺件返回原 Professional。

Worker 不决定业务背景、关键 T、候选、排序、无候选或 Owner 方法。

## 2. 固定执行环境

- Worker 聊天工作区：`/dwdhome/fy/cgpterm`
- aidata 实际执行工作区：`/dwdhome/fy/BASE_E6_2`
- aidata 代码目录：`/dwdhome/fy/BASE_E6_2/mquant/aidata`
- 固定 Context：
  - `sof_name="GTQH_L1_20210104_20240229"`
  - `stk_tlist="gtqh_four"`
- 不切换 checkout、不升级依赖、不修改共享平台。

## 3. 确定脚本与命令

脚本：

`/dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0005/build_bi01_co05_r0005_chart_data.py`

提交内相对路径：

`runs/BI-01-CO-05/artifacts/professional-R0005/build_bi01_co05_r0005_chart_data.py`

Professional 固化的脚本 SHA-256：

`a109c6c390eb8d1b4cf155c1fb6fbbf4c0d7ca48e0e780083b257eb57fa3811f`

执行命令：

```bash
cd /dwdhome/fy/BASE_E6_2
python /dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/professional-R0005/build_bi01_co05_r0005_chart_data.py
```

输出根：

`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0005_chart_data`

执行前须核实际脚本 SHA-256 与上值一致；不一致则停止并报告，不运行来源不明的替代脚本。

## 4. Professional 已固定的输入与图面

- 品种：`rb / hc / i`，必须恰好是这三个；
- K 线频率：`30m`；
- 图窗：`[2021-08-15 00:00:00, 2021-09-30 00:00:00)`；
- 窗口 ID：`BI01-CO05-C001`；
- 正式图数层：
  - `KLine(freq="30m")`；
  - `ScaleTurnCalendar("large")`；
  - `ScaleTurnCalendar("mid")`；
- 不启用 `small`；
- 一张 Figure 同时展示三品种；
- 价格线使用相对价格比例归一化；
- large：三角形、17；mid：菱形、12；
- 各品种采用源自身日历，rb 背景轴；须核窗口内时间轴实际对齐。

这些是业务选择，不得由 Worker替换。

## 5. 允许的普通修通

仅在当前有权工作区的实际 API 与示例调用存在普通差异时允许：

1. 修改 import、函数签名、返回对象序列化或本次输出路径的兼容写法；
2. 若 `blk@steel` 在当前 API 中未**恰好**展开为 rb/hc/i，用当前 API 的明确品种选择语法表达同一固定集合；
3. 若通用页面 helper 未直接形成既定“一图三品种、相对比例归一化”页面，调用当前有权 checkout 的既有绘图 helper 实现同一固定图面；
4. 修复不改变数据、特征或图面语义的局部工程故障。

所有修正须在 Worker 交付目录中的脚本副本或本次 test-run 临时面完成并记录 diff；不得覆盖 Professional 原脚本或共享源码。

以下变化必须停止并回原 Professional，不得自主决定：

- 更换品种、窗口、频率、SOF、stk_tlist 或 large/mid 特征；
- 增加 small；
- 改用其他历史 run 或其他数据源；
- 改变转折计算语义、重定义方向/确认/首次可见；
- 修改 aidata/mquant/tis/FRP 共享代码、切换 checkout、升级依赖；
- 新建业务规则、关键 T、候选筛选或专项审计。

## 6. 必须实际核验的交付

仅“退出码 0”“路径存在”或“返回 URL”不算完成。Worker 必须：

1. 实际打开生成页面，确认可见且是 rb/hc/i 同一 Figure；
2. 确认窗口、30m 价格线、large 和 mid 图层；
3. 确认相对价格比例归一化、rb 背景轴及三品种时间轴；
4. 实际读取 `build_board_run(..., reuse_core=True)` 返回的 delivery manifest 和正式数据索引/切片；
5. 确认图与正式数据属于同一 run/core，品种、窗口、特征相互可定位；
6. 返回人可访问的页面 URL/节点和 AI 可读取的正式数据位置；
7. 若任一项失败，准确报告已完成范围和具体缺件，不得把部分结果包装成完成。

不要求：`KEY_T_EVENT_LEDGER`、`FIELD_QUALIFICATION`、`DIRECTION_MAPPING_RECEIPT`、全量环境 diff、哈希清单或业务解释。

## 7. 写权

允许写：

- `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0005_chart_data/`
- `/dwdhome/fy/cgpterm/runs/BI-01-CO-05/artifacts/worker-BI01CO05-CHART-DATA-R0005-01/`
- 为本次执行产生的临时文件。

不得写：

- 共享 aidata/mquant/tis/FRP 源码和配置；
- Professional 原始脚本与成果；
- 其他 Run/工单成果；
- 数据库、服务配置或全局环境。

不得重启、重部署共享服务。

## 8. 回交

在：

`runs/BI-01-CO-05/artifacts/worker-BI01CO05-CHART-DATA-R0005-01/FULL_RESPONSE.md`

记录：

- 本工单全部身份字段；
- 实际执行命令与退出状态；
- 实际 run_id；
- 图页 URL/节点与是否实际打开；
- 正式 delivery manifest、索引和必要切片位置与是否实际读取；
- 图数同 run/core 对应关系；
- 实际 rb/hc/i、窗口、图层、归一化与日历核对；
- 每项普通兼容修正及其局部 diff；
- 缺件或阻断；
- 明确 `return_to: chatgpt:BI-01-CO-05:professional`。

技术结果必须返回原签发 Professional 消费。Worker 不向管理提交业务接收，不宣布首个过程实践包，不形成候选规律。
