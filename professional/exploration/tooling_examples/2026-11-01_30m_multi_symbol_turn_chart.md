# 当前 30m 多品种转折图：完整背景说明

供直接使用同一工作区 \`/dwdhome/fy/BASE_E6_2\` 的 AI 阅读。以下为 2026-11-01 的当前画法与关键入口；具体实现直接读取工作区现有文件。

## 当前目标与页面

一张 Figure 内展示 rb、hc、i 的 30m 行情，并叠加 small、mid、big 三套贴近转折。当前只处理一个窗口，不需要恢复最初的“1d 概览加三个 30m 窗口”需求。

- 页面：\`http://192.168.11.40:5006/cae?node_id=6153\`
- run_id：\`GTQH_C001_three_turns_20261101_162005\`
- 窗口：TEST-C001，2021-08-15 00:00 至 2021-09-30 00:00；结束日期不包含 9 月 30 日全天。
- aidata 窗口节点 \`big_000001\` 的 big 是时间窗层级，与图例 big 转折含义不同。

## 数据与转折参数

数据源为 F 盘 \`/m3varF/BaseData/futures/GTQH_L1_20210104_20240208\`，可用范围为 2021-01-04 至 2024-02-08。Context 使用 \`sof_name="GTQH_L1_20210104_20240208"\`、\`stk_tlist="gtqh_four"\`、\`startDay=None\`、\`endDay=None\`；板块 \`blk@steel\` 为 rb/hc/i。转折按源的完整可用历史计算，画图时截取 C001。

| 图例 | ScaleTurnCalendar 实例 | 输入 | Zig 回撤 | 隶属度阈值 | specTerm | 模糊系统 | 标记 |
|---|---|---|---:|---:|---|---|---|
| small | \`small\` | 30m 收盘 | 0.1% | 0.3 | S | \`scaleturn_gauss_4\` | 圆点，8 |
| mid | \`mid\` | 30m 收盘 | 0.5% | 0.3 | M | \`scaleturn_gauss\` | 菱形，12 |
| big | \`large\` | 30m 收盘 | 0.5% | 0.3 | L | \`scaleturn_gauss\` | 三角形，17 |

用户已明确选择 big 使用同族 \`large\`，不是另一套 \`30m_big\`。参数中的 \`retracePct=0.5\` 表示 0.5%。准确对象定义以工作区 \`selected_turn_parameters.json\` 的实际展开参数为准。

ScaleTurnCalendar 根据在价格折线中增加折点的“贴近增益”，判断其对指定 S/M/L 尺度的模糊隶属度。它不是单纯按 Zig 回撤画点，三套结果也不保证严格嵌套。保留两轮 \`value1\`、\`value2\` 及重复事件。

散点画实际转折位置 \`x/y\`；\`xConfirm/yConfirm\` 表示确认位置，另行保留；\`event_ts\` 是事件输出索引。回画到实际位置不表示当时已经确认。

## 日历与组装方式

GTQH 当前采用品种自身日历。图以 rb 自身日历为背景，rb/hc/i 各自按 \`@\` 读取。本窗口三个品种的时间轴已确认一致；更换品种或窗口应核对对应时间轴。

当前时间窗解析使用 \`source_metadata/calendar/@ -> F盘calendar/rb\`，\`source_metadata/sof\` 为逐项链接原元数据的实际目录。该图不依赖旧的 \`night_end_at_2300\` 共享分支。

绘图关系为：\`TestCAE1 → CAEGraph → 一个 PlotSet → SpecEntitiesMainFig\`。\`PlotSet\` 的 \`calendar_name="@", blk=["rb"]\` 用于确定背景轴；\`SpecEntitiesMainFig\` 中显式指定 \`syms!blk@steel\`，仍绘制 rb/hc/i。

每品种使用一个 \`KPriceLine(KLine(freq="30m"), std_method="ratio")\`，加三套 \`MulFieldsGlyphs\` 散点。散点绑定 \`_csv_x/_csv_y\`、\`timefieldtype="uti"\`、\`dynstd_method=True\`，与对应品种价格共享比例归一化，纵轴显示相对价格。\`x_label_freq="1d"\` 只控制横轴标签，数据频率仍为 30m。

九组特征由原 E 数值程序生成在工作区暂存目录；当前通过 \`ReadOnlyCsvFeature\` 接入其已计算结果。CSV 在这里是读取与传输形式，不另算转折。\`make_point_anchor\` 定义证据，\`build_chart_run\` 冻结窗口，\`build_board_run(..., reuse_core=True)\` 生成同一 run 的切片；实际页面由现有 CAEGraph/PlotSet 组合持久化。

## 工作区入口

以下统一用 \`R\` 代表：

\`\`\`text
/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101
\`\`\`

| 用途 | 位置 |
|---|---|
| 实际绘图脚本，优先阅读 | \`R/build_three_turn_plot.py\` |
| 三套实际展开参数，优先阅读 | \`R/selected_turn_parameters.json\` |
| 完整持久化绘图参数 | \`R/three_turn_plot/single_three_turns.fason.txt\` |
| 生效数据源配置 | \`/dwdhome/fy/BASE_E6_2/m3sof/settings/sof/GTQH_L1_20210104_20240208.py\` |
| 日历及元数据入口 | \`R/source_metadata/\` |
| 原 E 计算准备及执行 | \`R/prepare_staged_turn_jobs.py\`、\`R/run_staged_turn_job.py\` |
| 原 E 计算结果及读取入口 | \`R/turn_staging/\`、\`R/three_turn_plot/\` |
| 当前 aidata run | \`R/three_turn_plot/GTQH_C001_three_turns_20261101_162005/\` |

查看当前页面无需重算；绘图脚本再次执行会创建新的 run 和平台节点。
