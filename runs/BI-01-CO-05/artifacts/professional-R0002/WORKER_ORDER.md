order_id: BI01CO05-AIDATA-EVIDENCE-01
work_id: BI-01
run_id: BI-01-CO-05
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-05:professional
issuer_invocation_id: BI01-CO-05-R0002-a60d58cf183f
issuer_assignment_token: 1f902426303447e1a117ecaa1da002e6
return_to: chatgpt:BI-01-CO-05:professional

# Worker Order：回收并核验同一 aidata run/core 的可知性证据

## 1. 签发状态

`SIGNED_PENDING_CONTROLLER_VALIDATION_AND_DISPATCH`

本文件由当前 Professional 签发，但不声称已通过 `worker-order` 机械检查、已调用 `codex queue`、已被 Worker 接收或已执行。控制器必须以包含本文件的确切 commit 运行现行检查，通过后才可投递。

- Owner 指定 Worker 线程：`01a17dd7-5033-7e63-b7a2-edd90b691c33`
- 预期 workspace：`/dwdhome/fy/cgpterm`
- 技术结果必须回 `chatgpt:BI-01-CO-05:professional`
- Worker 不得做业务结论、方法反馈、管理接收或 Owner 决定

## 2. 直接技术目标

对既有候选 run：

`GTQH_C001_three_turns_20261101_162005`

先只读回收并核验同一 run/core 的正式证据，使 Professional 能按首次可知时点建立大/中尺度关键 T 账本。

已有实物足够时禁止重跑。只有缺失正式 board/ledger、且既有 run/core 可复用时，才使用当前 aidata 标准调用做最小补齐。不得创建直连数据库或另一套平行取数通道。

## 3. 既知定位

- 候选执行环境：`/dwdhome/fy/BASE_E6_2`
- 数据源：`/m3varF/BaseData/futures/GTQH_L1_20210104_20240208`
- 工具工作根：`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101`
- 当前 run：`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101/three_turn_plot/GTQH_C001_three_turns_20261101_162005/`
- 页面：`http://192.168.11.40:5006/cae?node_id=6153`
- 对象：`rb / hc / i`
- K 线：`30m`
- 文档展示窗：`2021-08-15 00:00` 至 `2021-09-30 00:00`，终点不含 9 月 30 日全天
- 优先尺度：`large + mid`；small 只作为可选解释层
- 当前业务输入文档：`professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md`

## 4. 必做顺序

### 4.1 身份与版本

1. 核真实 checkout、aidata 与相关 mquant/tis/frp 版本。
2. 记录与该 run 语义有关的本地未提交差异；不清洁、不改写。
3. 回读 `selected_turn_parameters.json`，保存展开参数及文件 sha256。
4. 回读 run/core manifest、run summary、timespan index、chart manifest。

### 4.2 正式数据链

5. 检查同一 run/core 是否已有 board：
   - `DELIVERY_MANIFEST`
   - `FILE_INDEX`
   - feature slice stats
6. 如已有，直接回收；如缺失但已有 run/core 可复用，才调用正式 `build_board_run(..., reuse_core=True)` 最小补齐。
7. 取得 `rb/hc/i`：
   - 30m K 线正式切片；
   - large 与 mid 正式对象切片；
   - 必要的上游 zig/direction 映射；
   - `actual / confirm / event / first-visible / revision` 相关字段。
8. 统计每份正式切片：
   - 首末有效时间；
   - 行数、缺失、重复、空值；
   - 窗口内与跨窗对象；
   - 方向覆盖；
   - 上游映射覆盖；
   - 额外无方向贴近点。
9. 证明图与正式切片属于同一 run/core；不能仅以相同 run_id 字符串推断。

### 4.3 可知性账本与静态证据

10. 按首次可见/确认顺序输出纯事实 `KEY_T_EVENT_LEDGER.csv`，每行至少含：
    - symbol / scale / source object id；
    - actual position/time；
    - confirm or first-visible time；
    - event/publication time；
    - revision identity；
    - direction and provenance；
    - predecessor/current-development relation；
    - formal source path/hash。
11. 对现有图页做实际只读打开与静态导出：
    - 一个全局窗口；
    - 仅在密度需要时做局部放大；
    - 明确多品种标准化、图层、窗口终点及各品种日历。
12. 如展示窗不足以覆盖必要前史，只报告不足；不得自行改业务窗口。最小扩窗建议另列，由 Professional 消费后决定。

## 5. 写权

仅允许写入：

`runs/BI-01-CO-05/artifacts/worker-BI01CO05-AIDATA-EVIDENCE-01/`

以及执行环境的临时导出目录。

不得修改或覆盖：

- 共享 aidata/mquant/FRP/tis 源码；
- 服务配置、数据库、日历或全局环境；
- 既有 run/core；
- 当前 Professional 报告和 Return；
- 其他 Run 的任何成果。

不得重启或重部署共享服务。

## 6. 业务边界

Worker 只运输和核验技术事实，不得：

- 判断共同大尺度背景是否成立；
- 判断哪个品种更强或应成为候选；
- 形成候选规律、无候选裁定或自然挑战结论；
- 修改 Owner 两层过程；
- 判定管理接收、RESULT/CHANGE/EFFORT 触发；
- 把平台窗口节点 `big_000001` 当成大尺度 Feature；
- 用最终 actual 位置代替首次可知时点；
- 从截图反造正式字段；
- 因缺数据而补造方向或修订。

## 7. 预期交付

在允许写面中交：

```text
FULL_RESPONSE.md
INPUT_IDENTITY.json
VERSION_AND_DIFF_RECEIPT.json
FORMAL_FILE_INDEX.csv
FIELD_QUALIFICATION.csv
SLICE_COVERAGE.csv
KEY_T_EVENT_LEDGER.csv
DIRECTION_MAPPING_RECEIPT.csv
STATIC_EVIDENCE/
COMPACT_FORMAL_SLICES/
SHA256SUMS
```

`FULL_RESPONSE.md` 顶部必须保留与本工单一致的：

- `order_id`
- `work_id`
- `run_id`
- `return_to`
- `issuer_invocation_id`

并说明：

- 实际执行状态；
- 是否重跑及原因；
- 每个缺件；
- 所有输出路径、字节数与 sha256；
- 页面是否实际打开；
- 任何不可恢复的可知性边界。

## 8. Professional 验收条件

结果只有同时满足以下条件才可进入业务消费：

1. 每条关键对象能放到正确的首次可知 T；
2. actual 与 confirm/event/revision 分开；
3. 方向明确区分正式字段、可靠上游映射或未知；
4. 图与正式切片属于同一 run/core；
5. formal coverage、前史和跨窗对象可核；
6. 在不使用未来信息的前提下可以开始第一层；
7. 若仍不能，缺口已窄到具体字段、文件或正式调用，而不是笼统“数据不可用”。

通过不等于业务背景、候选规律或 Owner 过程已经成立；这些仍由原签发 Professional 决定。
