# CAEGraph 脚本包 / 数据包输入清单（2026-11-16）

> 状态：Owner 已向当前任务上传 `caegraph-scripts.zip`；本清单经逐项打开 ZIP 与 Python AST 检查形成。**ZIP 原件尚未通过本次 GitHub 写入接口发布到仓库**，不能把本清单当作脚本已入库、数据已可读或完成专业节点的证明。实际启动前须确认脚本原件可在新 Run 使用的 GitHub/Pro/Worker 物理通道取得。

## Owner 给定来源

- 脚本附件原文件名：`caegraph-scripts.zip`。
- 脚本附件 SHA-256：`5eaf500616316ef7764cd30eb7467f2db3a6c85e45aa3b4f958becbc7818e8eb`（31,319 字节）。
- 已有数据：Owner 指定在 Sources 中的 `caegraph-data-30tick.zip`；**当前未收到可核实际物理文件或 SHA-256**，绝不假报下载/解压/数据验证成功。须由主控在准确目标 Project 核对、转存到本 Run 所授权的共享区并由 Worker 读到，或者使用可信的同一数据文件直接作为可读输入。
- 图/数据输入包内自述源：附件里的 `caegraph-review/README.md`；完整源文件应该保留为实际可读取的代码，而非从本说明重写。

## 脚本目录（已从 ZIP 核实）

| 路径（解压后） | 字节数 | SHA-256 |
| --- | ---: | --- |
| `caegraph-review/caegraph_definitions.py` | 91955 | `acd395a48ea27de380233b78188f8bb9e0f69f83492fe2a7f8cc4e3acb0f6e39` |
| `caegraph-review/snapshot_data.py` | 5361 | `edbe17b148927c702a97e0af8dea9e0a272dfffe28486413c55e3489074da6e0` |
| `caegraph-review/run.py` | 6242 | `a9646fc36164115e054a503971d67b308cdf1d044a84d1dbdbc121b0009d98bc` |
| `caegraph-review/README.md` | 3358 | `4b8129b9ff8d7d864af991b00532d7b2ea37860a60ec6ca6d509981a34e75ce1` |

三个 Python 文件的语法树解析通过，**没有在真实 mquant 或市场数据环境执行**。

脚本/数据两个 ZIP 的预期合并目录：
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

**重要范围核查：**脚本 README 说的是钢铁板块 `rb/hc/i`、1 个日线长期概览、6 组 30min/1min/5s 组合、30 个 Tick 窗口。源码不自动证明本文件及数据包提供了 EAW P1 全部 Feature 的观察输出；正式新 Run 应在收到数据包 `manifest.json` 后准确核定其 `evidence_features`、实际对象和业务问题，不因项目名称推定 P1 适用性，也不擅自改掉 Owner 指定的 EAW P1 目标。

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

本文件只记录真实已收到的脚本结构、Owner 的数据文件名和建议路径。新 Run 正式 GO 还需要实际脚本字节位置、数据 ZIP 的真实读取能力和授权、独立 run_id/操作写面/精确采用版本；**不以缺少原始数据 ZIP 的当前状态冒充 DATA_READY**。
