# Worker 工单：BI-01-V2-02 首批六场景 aidata 图与同源数据

authority: execution Pro  
invocation_id: `BI01-V2-02-R0006-20261018T154801Z-a5ec3f46`  
status: **SIGNED BY PROFESSIONAL RESULT; NOT EXECUTED IN THIS CHAT ENVIRONMENT**

## 1. 业务目的

这不是“把 304 个 raw candidate 全部重画”的工单。六个场景已经由执行 Pro 从固定基础行情独立选择；Worker 只负责：

1. 用 aidata 形成 Owner 可实际查看的图；
2. 导出与图同 run/node/timespan 的结构化数据；
3. 核实真实浏览器渲染；
4. 准确回交技术事实。

Worker 不决定 U2/U3 是否合理，不签 G4，不重算正式 Feature。

## 2. 固定输入和工作区

### 原件

目录：`/dwdhome/fy/资金管理`

- `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`
  - SHA256 `4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987`
- `steel_U2_U3_执行结果_20261010.zip`
  - SHA256 `7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c`

aidata 工作区：`/dwdhome/fy/BASE_E6_2`

执行开始时记录：

- aidata repo、branch、HEAD；
- Python/environment；
- 实际固定源路径与 SHA；
- 使用的 adapter/API；
- 服务启动命令和端口；
- 是否复用旧 V2-01 产物及其 exact 版本。

不得把复制后的临时包声明为新正式源。

## 3. 工具边界

优先使用现有：

- `build_chart_run`
- `build_big_world_chart_pages`
- `build_board_run(..., reuse_core=True)`
- `build_chart_review_requests`
- `render_review_nodes`
- `export_plot_view_data`

先读当前 HEAD 的 `README.md`、`OWNER_INTENT_AND_RATIONALE.md`、`TODO.md`、`docs/DEVELOPMENT_GUIDE.md`、`docs/RUN_BRIEF_INPUT_CONTRACT.md` 和真实 API。

若任意 CSV 接入不通：

1. 先查已有 adapter/API/TODO；
2. 只做阻断本工单的最小通用修复；
3. 必须在 `daowei2026/aidata` **新独立分支**上施工；
4. 不改 aidata 当前 main/CYF 分支；
5. 不在 observe-iterate/cgpterm 建第二套画图工具；
6. 不现场重算 U2/U3。

旧修复分支 `codex/bi01-v2-chart-render-fix-20261018@adea9b46ce4016045eee714121f7a322924e14a3` 仅是 DataTable/BokehJS 历史参考，不自动代表当前全部页面已通过。

## 4. run/node 合同

统一：

```text
run_id = BI-01-V2-02
```

每个场景至少两个节点：

```text
SCN-xx-BASE
SCN-xx-EVIDENCE
```

SCN-01 再按五个 As-Of 形成子节点或同节点可切换视图：

```text
SCN-01-ASOF-20210506T1000
SCN-01-ASOF-20210507T1000
SCN-01-ASOF-20210511T1000
SCN-01-ASOF-20210514T1000
SCN-01-ASOF-20210518T1000
```

人图和 AI 导出必须同一 `run_id/node_id/timespan`。视觉 `extra_time` 要单独记录，不能替换 evidence window。

## 5. 六个场景

| node | evidence anchor | chart timespan | direction | base members / third |
|---|---|---|---|---|
| SCN-01 | 2021-04-30 15:00 | 2021-04-26 09:30 — 2021-05-20 15:00 | Up | hc/i/rb |
| SCN-02 | 2021-05-18 09:30 | 2021-05-14 09:30 — 2021-05-24 15:00 | Down | hc/i/rb |
| SCN-03 | 2021-11-08 10:30 | 2021-11-04 09:30 — 2021-11-12 15:00 | Up | hc/i/rb |
| SCN-04 | 2021-11-19 14:00 | 2021-11-17 09:30 — 2021-11-25 15:00 | Up | hc/rb；i 为第三对象 |
| SCN-05 | 2021-10-27 22:00—23:00 | 2021-10-25 09:30 — 2021-11-02 15:00 | Up | i/rb/hc 近邻 2 bar；非 exact |
| SCN-06 | 2021-07-30 15:00 | 2021-07-28 09:30 — 2021-08-05 15:00 | Down | hc/rb；i 为第三对象 |

执行顺序：

1. SCN-01，尽早形成首个真实闭环；
2. SCN-04/SCN-06，检验第三对象边界的正反例；
3. SCN-03/SCN-02，检验整组弱与整组强；
4. SCN-05，检验 exact-UTI baseline 的错时边界。

该顺序不是停点；六个场景全部是当前工单范围。

## 6. 基础图层

每个 `BASE` 节点必须显示：

- rb/hc/i 的真实 30m KLine；
- 每个品种独立价格轴或明确归一化视图，不能把 raw price 强塞同一轴；
- small Zig；
- mid actual turn；
- mid confirm/known marker；
- expected direction；
- anchor 和 chart evidence window；
- 成员与第三对象身份。

图注至少说明：

```text
actual time
knowledge/confirm time
retrospective selection
formal evidence window
extra visual context
```

不能用后续图形声称当时可知。

## 7. Evidence 图层

### SCN-01

叠加/并列：

- C1 Formation/Qualification/Validity 与 four-gate reference；
- C2 `official_cluster_committed=NO`、`official_h1_emitted=NO`；
- S `outside_count=0`、`ValidEmptyAlternatives`；
- U3 R02 五个 As-Of 的 member-episode stage、observed bars、progress、efficiency、counter、retained；
- N 同 As-Of 当前 working episode；
- R03 `WITHHELD`。

必须能在图/同源数据中区分：

```text
R02 anchored member episode
vs
N current single-node working episode
```

### SCN-02/03/04/06

叠加/并列固定包已有的：

- exact C1 raw/reference candidate；
- actual/known time；
- C0 episode/working cuts；
- N current/historical metrics；
- third object path（SCN-04/06）。

明确显示 `NOT_ISSUED...`、`NOT_EVALUATED...`，不得把 raw candidate 画成正式 cluster。

### SCN-05

只有基础 KLine/Zig/mid turns + C0/N：

- 标出 i/rb/hc 三个实际 turn 的先后；
- 明确 `NOT_IN_EXACT_UTI_C1_RAW`；
- 不构造假 C1/U2 overlay。

## 8. 同源数据导出

每个节点输出：

- `plot_view_data` 或等价 aidata 正式导出；
- KLine rows；
- Zig/mid turn markers；
- actual/confirm/known timestamps；
- node metadata；
- 图层 visibility；
- source file + row key；
- As-Of；
- evidence/extra_time；
- adapter/version。

SCN-01 额外输出 R02、N、C1/S/C2/R03 对应 rows。

禁止用 Pro 本地 `S1_SCENE_BASE_FACTS.csv` 冒充 aidata S2 同源导出；它只能作为选窗/核对输入。

## 9. 浏览器验收

每张图都实际打开浏览器，至少核：

1. KLine 蜡烛/线真实可见；
2. 三品种价格轴/图例可辨；
3. Zig 与 mid actual/confirm marker 可见；
4. evidence layers 与标记时间对应；
5. 拖动/缩放后图层仍正常；
6. 无 BokehJS `DataTable` 注册错误或空白页面；
7. 网络请求成功之外，DOM/Canvas 中确有数据；
8. URL 在 Worker 回交时仍可打开。

HTTP 200、文件存在或 URL 生成均不算渲染通过。

## 10. Worker 回交

回交至少包含：

- aidata exact commit/branch；
- 固定源 SHA；
- 每个 node 的 report URL；
- 每个 node 的同源数据路径和 SHA；
- browser check 时间、结果、失败页面；
- 实际命令与配置；
- 旧图是否复用及复用依据；
- 新分支/代码改动/测试（若有）；
- 未完成项与准确阻断；
- `ROLE_RETURN`，但不写 U2/U3 业务裁定。

## 11. 禁止事项

- 不重新生产正式 U2/U3；
- 不改变固定 CSV；
- 不把 N 改名 U3；
- 不补算正式 Quality/Allocation；
- 不修改 observe-iterate 形成绘图实现；
- 不因首张图完成而停止；
- 不让 Worker 签业务结论。
