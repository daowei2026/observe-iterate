order_id: BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01
work_id: BI-01
run_id: BI-01-CO-05
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-05:professional
issuer_invocation_id: BI01-CO-05-R0011-e186238bf811
issuer_assignment_token: ade5d48ee39949aa99991f4b0a39
return_to: chatgpt:BI-01-CO-05:professional
target_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
target_workspace: /dwdhome/fy/cgpterm
state: SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH

# Worker Order：一次性同身份日历读探针，通过后执行 rb/hc/i 30m 全段图数

## 0. 签发依据、唯一性与当前状态

本工单落实：

- `daowei2026/observe-iterate@0776c5645be4bf1d38c7151baa8662def243e26b:runs/BI-01-CO-05/reviews/management-R0010/DECISION.md::#reentry`
- `daowei2026/observe-iterate@0776c5645be4bf1d38c7151baa8662def243e26b:runs/BI-01-CO-05/provenance/turns/R0010/FULL_RESPONSE.md::#reentry-decision`

签发身份依据：

- control commit：`4699c3c947753f65d0a3f3ff044f5c74d68fdc3b`
- R0011 `INVOCATION.json` 与 `SEND_RECEIPT.json` 的 invocation/token/recipient 同身份
- `SEND_RECEIPT.state = COMMITTED`
- 当前 Professional 为原业务问题和本次新工单的真实签发者

旧工单 `BI01CO05-FULLRANGE-CHART-DATA-R0008-01` 已经真实执行并终态关闭。禁止重派、自动重试、改名复用或把旧 order 作为 deferred/future required。本工单是新的、唯一一次同路径条件重入，具有独立 `order_id` 和 R0011 签发身份。

本文件已由 Professional 签发，但不声称：

- controller 已运行 `workmap_gate.py worker-order`；
- 已调用 `codex queue` 或实际投递；
- Worker 已接收、执行或回交；
- 技术结果或业务结果已被接收。

控制器必须对**包含本文件的确切提交**运行现行 `worker-order` 检查，通过后才可向指定线程实际投递。

## 1. 唯一技术目标

在同一个 Worker 执行中：

1. 先以与上次实际执行相同的 Worker 线程、目标 workspace、Python 启动入口和权限身份，对精确日历文件做一次真实 `open/read-to-EOF` 探针；
2. 探针失败或身份/来源证据不完整：在昂贵全段调用前停止，交精确证据，同路径重入额度耗尽；
3. 探针通过：立即在同一次 Worker 执行中，从头运行 R0008 原始全段脚本一次，生成 fresh dynamic run_id；
4. 按原 R0008 业务参数交付全段主图、七个固定辅助图和同 run/core 正式 KLine/large/mid 数据；
5. 所有技术实物返回原签发 Professional，由其消费后进入业务观察。

Worker 不判断大尺度背景、关键 T、中尺度充分性、候选、排序、合法无候选、Owner 方法或 Management 接收。

## 2. 固定环境、原脚本与不可变业务输入

### 2.1 环境

```yaml
worker_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
worker_workspace: /dwdhome/fy/cgpterm
aidata_execution_workspace: /dwdhome/fy/BASE_E6_2
aidata_python_launcher: /dwdhome/fy/BASE_E6_2/run-python.sh
previous_observed_business_python: /m3c3/Linux/apps/anaconda3/bin/python
previous_observed_python_version: 3.10.13
aidata_code_dir: /dwdhome/fy/BASE_E6_2/mquant/aidata
sof_name: GTQH_L1_20210104_20240229
stk_tlist: gtqh_four
```

不得 `sudo`、`su`、切换容器/用户/权限身份、切换 checkout、升级依赖、修改共享 aidata/mquant/tis/FRP 源码或配置、修改 NFS、重启或重部署共享服务。

### 2.2 原脚本

仓库相对路径：

`runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py`

接受版本：

`daowei2026/observe-iterate@34198df6d4435feaa089baeae73e934559bd8b19`

固定 SHA-256：

`5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`

执行前必须实测脚本 SHA-256。Worker 现场若把 observe-iterate 仓库物化到不同绝对路径，可使用该实际物化路径，但必须记录：物化根、Git commit、相对路径、字节数和 SHA-256；哈希不一致时立即停止，不运行替代脚本。

### 2.3 不可变业务参数

```yaml
symbols: [rb, hc, i]
frequency: 30m
main_window: "[2021-01-04 00:00:00, 2024-03-01 00:00:00)"
main_window_id: BI01-CO05-FULL-20210104-20240301
features:
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

七个辅助窗固定为：

- `2021-01-04 → 2021-07-01`
- `2021-07-01 → 2022-01-01`
- `2022-01-01 → 2022-07-01`
- `2022-07-01 → 2023-01-01`
- `2023-01-01 → 2023-07-01`
- `2023-07-01 → 2024-01-01`
- `2024-01-01 → 2024-03-01`

辅助图只帮助阅读，不得替代全段主图、缩短正式数据范围或按最终走势重选。

目标输出根保持：

`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data`

禁止删除或覆盖上次失败 attempt 的历史证据；新运行使用脚本生成的 fresh dynamic run_id 和新文件名。

## 3. 同身份精确文件读探针

### 3.1 探针对象

只允许读取这个精确路径：

`/m3varI/var/L1_data/sof/unit/affiliated_calendar_no_night.csv`

上次实际观察的 mount source：

`192.168.9.79:/m3varI`，`nfs`

### 3.2 必须记录

在 `/dwdhome/fy/BASE_E6_2` 中，以 `/dwdhome/fy/BASE_E6_2/run-python.sh` 启动探针；与随后业务脚本保持同一 Worker 执行、同一线程、同一权限身份。至少记录：

- UTC start/end；
- cwd；
- `id -u/-g/-G/-un` 或 Python 等价的 uid/euid/gid/egid/groups/username；
- `sys.executable` 与 Python 版本；
- `/proc/self/mountinfo` 中对目标文件生效的最长匹配 mount，及 `findmnt -T` 等价结果；
- mount point、fs type 和 source；
- 精确打开路径与 `realpath`；
- 单次打开后读到 EOF 的字节数、read call 数、`fstat` size、SHA-256；
- exit code、stdout、stderr、异常类型、errno、filename 和 traceback；
- 明确布尔记录：未使用 stale copy、未使用 alternate source、未绕过 resolver。

探针不得只做 `ls`、`stat`、路径存在、mount 存在、远端 ping 或缓存副本读取。这些不能替代真实 `open/read-to-EOF`。

### 3.3 探针通过条件

必须同时满足：

1. 以同一权限身份从精确路径成功打开并读到 EOF；
2. 文件非空，读出字节数与同一 fd 的 `fstat().st_size` 一致；
3. SHA-256 已记录；
4. 对目标文件生效的 mount point 为 `/m3varI`，source 为 `192.168.9.79:/m3varI`；
5. 没有复制日历、旧快照、替代文件、替代 source、resolver bypass 或权限切换；
6. 探针执行证据完整可复核。

### 3.4 探针失败分支

任一条件不满足：

- 立即停止，不调用 R0008 全段脚本；
- 不在本次 Worker 中第二次探针；
- 不修 NFS、不复制文件、不切换 source/resolver/checkout/依赖；
- 交 `PROBE_RECEIPT.json`、`BLOCKER_EVIDENCE.json`、原始 stdout/stderr、身份与 mount 证据；
- 标记 `conditional_reentry_quota=CONSUMED_FAILED`；
- 明确 `full_run_attempted=false`；
- 返回原 Professional。

同路径一次性额度由此耗尽。不得自动重派、建议第三单或自行提出平行输入；后继由 Management 在停止当前 Case与向 Owner 明示申请输入变化之间决定。

## 4. 探针通过后的单次全段执行

探针通过后，不另起 Worker、不等待新 Gate，在同一次 Worker 执行中立即：

1. 重新核脚本 SHA-256；
2. 从头执行原 R0008 脚本一次；
3. 让脚本生成 fresh dynamic run_id；
4. 不复用失败 attempt 的预请求 run_id；
5. 不删除失败 attempt 的合同、日志或回交。

标准命令语义：

```bash
cd /dwdhome/fy/BASE_E6_2
/dwdhome/fy/BASE_E6_2/run-python.sh \
  <actual-observe-iterate-root>/runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py
```

实际绝对路径可以反映当前合法物化，但相对路径、接受 commit 和 SHA-256 必须一致。

### 4.1 普通兼容修通

只允许 R0008 原工单已授权的普通兼容范围：

- import/API 签名、返回对象、路径、序列化兼容；
- 将 `blk@steel` 表达成当前 API 接受但仍精确展开为 `rb/hc/i` 的等价选择；
- 使用当前已有 helper 实现已固定图面；
- 不改变数据、特征、图面和业务语义的局部修正。

任何修通只能发生在本 Worker 交付目录的副本或本次 test-run 临时面；保留原脚本，交 `COMPATIBILITY_COPY.py` 与 `COMPATIBILITY_PATCH.diff`。若兼容修通需要在已经开始一次完整 `build_chart_run` 后再次重跑昂贵全段脚本，停止并报告；本条件重入只允许一次业务脚本尝试。

必须停止并回原 Professional的变化：

- 改品种、范围、频率、SOF、tlist、large/mid、小尺度状态或图面；
- 替代 calendar source/resolver、复制日历或使用旧快照；
- 修改 NFS、共享源码/配置、checkout 或依赖；
- 新建平行数据库/正式数据入口；
- 重新定义关键 T、方向、first-visible/revision 或业务规则。

这些不是普通兼容，涉及输入身份时按 `CORE_INPUT_OR_PROCESS_CHANGE` 处理。

## 5. 探针通过后必须实际核验的图数

### 5.1 页面

实际打开全段主图，并逐一打开/核验七个辅助图。仅 URL、路径或退出码不算交付。

`PAGE_INDEX.csv` 至少记录：

- actual run_id 与 core_id（若 API 暴露）；
- window_id 与 main/aux role；
- requested start/end；
- actual page URL/HTML path、静态导出路径和 SHA-256；
- opened 状态；
- 可见 symbols、layers 和时间首末；
- 相对比例轴、rb 背景轴、日历对齐核验；
- notes。

全段主图必须有静态证据；辅助图必须有静态导出或等价可复核证据。任一辅助图失败不得包装成全部完成，主图失败则整单不满足图面交付。

### 5.2 正式数据

实际读取同一 run/core 下 `build_board_run(..., reuse_core=True)` 返回的：

- delivery manifest；
- feature-slice stats；
- file index 或 manifest 内等价索引；
- `rb/hc/i × KLine_30m/large/mid` 正式切片。

`COVERAGE_AND_MISSING.csv` 每个 symbol × layer 至少记录：

- requested start/end；
- actual first/last time；
- row count；
- null time、duplicate time；
- empty/missing interval notes；
- feature effective start 或 warm-up；
- source path、bytes、SHA-256。

请求范围不等于实际覆盖。真实数据首末、缺口、交易日断点和 feature warm-up 按实报告，禁止填零、插值或补造。

### 5.3 图数同身份

`PAGE_AND_DATA_IDENTITY.json` 至少记录：

- actual run_id；
- core_id（若未暴露写 `NOT_EXPOSED`）；
- page records；
- manifest/stats/index path/hash；
- 正式切片 path/hash；
- 图与数据同 run/core 的可复核证据；
- 无法证明时的具体缺字段。

`FORMAL_FILE_INDEX.csv` 逐项列出路径、文件类型、字节、SHA-256、symbol/layer/window、读取状态和对应 manifest/index 位置。

## 6. 写权、必交付和回交

### 6.1 允许写

- `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data/`
- `runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/`
- 本次执行所需临时文件

### 6.2 禁止写

- 共享 aidata/mquant/tis/FRP 源码和配置；
- 数据库、NFS、服务配置或全局环境；
- 原 Professional R0008/R0011 脚本、报告、工单和 Return；
- 旧 Worker 目录和其他 Run；
- 任何受保护业务实物。

不得重启、重挂载或重部署共享服务。

### 6.3 每个分支都必须交

```text
FULL_RESPONSE.md
REENTRY_OUTCOME.json
PROBE_RECEIPT.json
MOUNT_AND_IDENTITY.json
EXECUTION_RECEIPT.json
PROBE_STDOUT.log
PROBE_STDERR.log
SHA256SUMS
```

探针失败时再交：

```text
BLOCKER_EVIDENCE.json
```

探针通过并运行全段脚本时再交：

```text
PAGE_INDEX.csv
COVERAGE_AND_MISSING.csv
PAGE_AND_DATA_IDENTITY.json
FORMAL_FILE_INDEX.csv
STATIC_EVIDENCE/
FULL_RUN_STDOUT.log
FULL_RUN_STDERR.log
```

发生普通兼容修通时再交：

```text
COMPATIBILITY_COPY.py
COMPATIBILITY_PATCH.diff
```

`FULL_RESPONSE.md` 顶部必须保留与本工单一致的：

- `order_id`
- `work_id`
- `run_id`
- `return_to`
- `issuer_invocation_id`

并准确记录：探针、分支决定、实际命令、attempt 数、退出状态、fresh run_id、图页是否实际打开、正式数据是否实际读取、兼容修通、缺件和所有产物位置/哈希。

所有技术结果必须返回 `chatgpt:BI-01-CO-05:professional`。Worker 不向 Management 提交业务接收。

## 7. Professional 消费边界

- 探针失败：Professional 同次消费后不得签第三个同路径 order；回 Management 决定停止当前 Case或提出有权输入变化。
- 探针通过但完整运行其他失败：只限制受影响输出，说明可继续范围；不得自动升级为市场或方法否定。
- 完整技术成功：结果回原 Professional；Professional 在消费同一结果的调用内核证据资格，并从第一条合格 as-of T 开始第一层业务观察，不再停在技术验收。

技术 PASS、图页存在或 board 生成都不等于首个过程实践包，不形成共同背景、候选、排序或无候选结论。
