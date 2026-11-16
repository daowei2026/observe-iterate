# CAEGraph 原始脚本 / 数据包输入清单（2026-11-16）

> 状态：Owner 通过 `caegraph-scripts.zip` 提供源文件；**已将其解压为 4 个原始源文件逐一提交到 GitHub**：`daowei2026/observe-iterate@0082ae1e79aaa7ca0a15cadf2a89d799aa6c7fa6:task-inputs/eaw-p1-integrated/caegraph-review/`。**当前分支不保留该脚本 ZIP**。已回读核对四文件原始字节大小。真实数据 ZIP 没有并入本目录，也不代表脚本在 Linux 执行成功或专业节点完成。

## Owner 给定来源

- Owner 原始上传附件名：`caegraph-scripts.zip`（仅用于来源追溯，**实际交付为解压后的 4 个普通文件，不提交脚本压缩包**）。
- 脚本附件 SHA-256：`5eaf500616316ef7764cd30eb7467f2db3a6c85e45aa3b4f958becbc7818e8eb`（31,319 字节）。
- 已有数据：Owner 指定在 Sources 中的 `caegraph-data-30tick.zip`。**已在本次 ChatGPT 任务附件中取得并逐项检查原件**：16,654,307 字节；SHA-256=`73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233`；ZIP CRC 全项通过；共 446 个成员，其中 442 个 `*.csv.gz`、`data/manifest.json`、`timespans.csv`、`included_tick_nodes.csv`、`calendar.npz`。`data/manifest.json` 有 442 项 assets、12 条 `evidence_features`，`data_scope` 为 overview=1、big_30m=6、mid_1m=18、small_5s=54、tick=30，涉及 `rb/hc/i` 以及 `wall_events/wall_segments`、`build_events`、`attack_segments`、`absorb_events`、`f4_tactical/f4_structural` 等图证据字段。**这只证明本任务附件确实存在、归档完整且结构内容可读取，不证明 cgpterm 主控/原执行 Pro/指定 Linux Worker 已经获得物理文件，也不证明数据实例已经通过专业验证。** 正式派发时仍由主控核准确 Project Sources 访问/附件转存和共享写面，Worker 对其实际取得的文件重复核哈希、确认源及用途。
- 图/数据输入包内自述源：附件里的 `caegraph-review/README.md`；完整源文件应该保留为实际可读取的代码，而非从本说明重写。

## GitHub 原始脚本目录（由上传 ZIP 逐项核验）

| GitHub 文件位置（`task-inputs/eaw-p1-integrated/` 下） | 字节数 | SHA-256 |
| --- | ---: | --- |
| `caegraph-review/caegraph_definitions.py` | 91955 | `acd395a48ea27de380233b78188f8bb9e0f69f83492fe2a7f8cc4e3acb0f6e39` |
| `caegraph-review/snapshot_data.py` | 5361 | `edbe17b148927c702a97e0af8dea9e0a272dfffe28486413c55e3489074da6e0` |
| `caegraph-review/run.py` | 6242 | `a9646fc36164115e054a503971d67b308cdf1d044a84d1dbdbc121b0009d98bc` |
| `caegraph-review/README.md` | 3358 | `4b8129b9ff8d7d864af991b00532d7b2ea37860a60ec6ca6d509981a34e75ce1` |

三个 Python 文件的语法树解析通过，**没有在真实 mquant 或市场数据环境执行**。

**独立原始文件提交现状：**`caegraph-review/` 的 `caegraph_definitions.py`、`snapshot_data.py`、`run.py`、`README.md` 均已提交并回读；**应直接以这些已入库源码为脚本入口**，不再获取脚本 ZIP 解压。附带的独立数据文件仍须从 Owner 的 Sources 实际取得并放到 `data/` 或用 `--data-dir` 指向它。

原始脚本和单独数据 ZIP 解压后形成的预期运行目录：
```text
caegraph-review/
  caegraph_definitions.py
  snapshot_data.py
  run.py
  README.md
  data/
    manifest.json
    timespans.csv
    included_tick_nodes.csv
    calendar.npz
    frame_*.csv.gz
    window_*.csv.gz
```

依包内 README：
- `python run.py --list`：列出图窗。
- `python run.py --check`：依次构造可用图窗并检查，依赖完整 data 和现役库。
- `python run.py`：本地 Bokeh Server 页面，**不是导出 HTML 文件**。
- `python run.py --data-dir /path/to/data`：数据解压目录可以另置。
- mquant/uplot/frame/quant、m3tt、Bokeh、pandas、numpy 由实际环境提供；包内没有这些依赖源码。

**重要范围核查：**脚本 README 说的是钢铁板块 `rb/hc/i`、1 个日线长期概览、6 组 30min/1min/5s 组合、30 个 Tick 窗口。源码不自动证明本文件及数据包提供了 EAW P1 全部 Feature 的观察输出；新 Run 的专业 Pro 应以已读取的 `manifest.json` 核对其 `evidence_features` 与原需求，并在 Linux 实际文件取得后准确核定这些图证据对本轮业务问题的适用性，不因项目名称推定 P1 适用性，也不擅自改掉 Owner 指定的 EAW P1 目标。

## 两端路径与暂定交付方式

Owner 指定的共享根：
- Windows MCP Server：`H:\fy`
- Linux Worker：`/dwdhome/fy`

**待主控在两端实际验证**是否为相同物理存储/双向同步；不能因为路径字符串相似就认为映射成功。Linux Worker 工作区仍为 Owner 指定的 `/dwdhome/fy/BASE_E6_2`。在路径映射真实成立时，建议本 Run 独立交换位置：
- Linux：`/dwdhome/fy/BASE_E6_2/.runtime/observe-iterate/OI-EAW-P1-20261116-01/handoff/`
- Windows：`H:\fy\BASE_E6_2\.runtime\observe-iterate\OI-EAW-P1-20261116-01\handoff\`

该推荐路径在本 Run 已指定 Linux 工作区之内；两端创建/读取/写入仍受实际 GO grants、物理写权限和其他 Run 占用限制。

对于 Worker **以后新生成**的数据：先写在本 Run 工作区的必要产物目录，打包 ZIP，并由经授权的 MCP Server/手机传输通道传到**原执行 Pro 既有聊天**。主控核实附件真实送达，执行 Pro 对数据专业消费后正常回管理 Pro；不把 ZIP 大文件默认重复上传 GitHub。现役聊天附件 Skill 对**新聊天**支持较明确，对已有角色聊天的 ZIP 发送须在真实执行时核接线。GitHub 继续保存机器 Return、业务报告、必要清单/哈希/提交与传输状态。

## 继续条件

本文件记录了已入库的 4 个 **原始脚本/说明文件**、Owner 数据 ZIP 的已核文件身份与推荐的跨端路径。新 Run GO 可引用 `daowei2026/observe-iterate@0082ae1e79aaa7ca0a15cadf2a89d799aa6c7fa6:task-inputs/eaw-p1-integrated/caegraph-review/`，无需脚本 ZIP；仍须核实 cgpterm / Pro / Worker 对数据 ZIP 的真实读取能力、工作区/跨端共享与授权，并登记独立 run_id/精确采用版本。**不以尚未在 Worker 现场读取并被专业接收的数据冒充 DATA_READY**。
