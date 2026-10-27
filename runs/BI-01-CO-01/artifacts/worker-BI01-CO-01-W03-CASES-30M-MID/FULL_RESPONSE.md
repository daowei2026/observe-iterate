---
order_id: BI01-CO-01-W03-CASES-30M-MID
work_order_id: BI01-CO-01-W03-CASES-30M-MID
parent_task_id: BI01-CO-01-CASE-RESEARCH-01
work_id: BI-01
run_id: BI-01-CO-01
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-01:professional
issuer_invocation_id: BI01-CO-01-R0008-28f5214c76
return_to: chatgpt:BI-01-CO-01:professional
worker_execution_id: BI01-CO-01-W03-dispatch-5e4fa62eaf
worker_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
---

# W03 完整技术回交

本单原日线重算、四窗正式30m/mid及窗口1d、原生五图同页和实际查看均已完成。代码/证据只写本单aidata目录及本回交目录，没有修改工具源码、服务、全局注册、业务目标、研究解释或冻结W02输出。

签发原件为 `f61e3c6d15c8150b2d183887a51341414e8d2a07:runs/BI-01-CO-01/artifacts/professional-R0008/WORKER_ORDER.md::full`，已完整消费。原issuer assignment token `7d65846a3f3daaa525485c48795725a5` 仅为签发来源引用，本Worker身份另列dispatch ID，不作为Worker token。专业/数据policy仍固定f7，没有用实现候选替换policy。

## 可直接消费的实物

- **[新的原生统一页6148](http://192.168.11.40:5006/cae?node_id=6148)**：一个平台页面内含W02完整2021起概览和C01—C04四张30m/mid。Worker于2026-10-28 07:22（UTC+08:00；原日志UTC 23:22）实际打开，随后查看整页和全部五张单图截图，无页面脚本/请求失败。并非只返回URL或检查HTTP200。
- **[36份完整正式CSV及manifest](../batch-01/aidata/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/)**：1d 753行、30m 8,928行、mid 503行；rb/hc/i，四个big节点，每个Case每品种三种feature。44份原输出文件均完整复制并核字节/hash相同；[Case/文件/图索引](../batch-01/aidata/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/CASE_FILE_PLOT_INDEX.csv) 给出准确定位。
- **[日线原字节重算](../batch-01/aidata/w03/DAILY_RECOMPUTE.json)**和[12行统计比较](../batch-01/aidata/w03/DAILY_METRICS_COMPARISON.json)：三份W02原hash及763行/品种核过，73锚点全通过；36个发表数值差异仅为文本舍入，最大绝对差约4.595e-10，日期/n完全相同。W02源文件及副本12项冻结检查也通过，没有重取W02行情。
- **[实际调用/版本/覆盖说明](../batch-01/aidata/W03_INPUT_AND_CALLS.md)**：完整实参、顺序、run、cwd/Python、窗口、版本/既有差异、原件/脱敏日志、必要适配和限制；[原生对象](../batch-01/aidata/w03/COMBINED_PAGE.json)、[浏览器证据](../batch-01/aidata/w03/BROWSER_REVIEW.json)、[截图](../batch-01/aidata/w03/screenshots/)、[图数对应](../batch-01/aidata/w03/RENDER_ALIGNMENT.json) 可分别读取。

## 验证结论与有效范围

实际run：`bi01_co01_w03_cases_20261028_5e4fa62eaf`。实际输出根：`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co_01_w03_cases_30m_mid_20261028_5e4fa62eaf`，新run子目录与冻结W02分开。core→第二接口（内部overview）→same-core board一次成功，原生组合一次创建成功；没有额外独立overview、重复core或取数重试。

| Case / node | 30m有效行/每品种 | 共同30m首→末收盘 | mid行 rb/hc/i | 必要后续 |
| --- | ---: | --- | --- | --- |
| C01 / big_000001 | 484 | 2021-02-01 09:30→04-06 23:00 | 24/22/44 | 04-06 已覆盖 |
| C02 / big_000002 | 820 | 2021-07-01 09:30→10-14 23:00 | 45/43/101 | 10-08—10-14 实际交易日已覆盖 |
| C03 / big_000003 | 636 | 2022-04-01 09:30→06-23 23:00 | 30/22/77 | 06-13—06-23 实际交易日已覆盖 |
| C04 / big_000004 | 1036 | 2023-06-01 09:30→10-11 23:00 | 25/24/46 | 10-10、10-11 已覆盖 |

四窗K线空OHLC行0、三个品种时间键相同、窗口日线与W02各字段全量一致。实际浏览器的11,217行K线原值/坐标及503个mid点与对应CSV全量一致，W02概览三个已知空OHLC保留为NaN。这里核的是源数据和展示对应，没有据此评价四例的经济解释。

## 交专业者的明确限制与未执行部分

1. **9行mid确认晚于manual终点**：实际点x/y均在窗内且等于对应正式30m close；真实确认字段来自后端confirm2D，最晚至2023-10-16 15:00。准确CSV行号和原字段在[未来确认清单](../batch-01/aidata/w03/MID_CONFIRMATIONS_OUTSIDE_REQUEST.json)。图只画actual x/y，不能把转折位置当作确认或当时可知时间，须由原Pro据此复看。
2. 结束日不作全天包含承诺；本次实际末行如表。1d首根可自前夜开盘，30m仅覆盖manual请求；未构造完整交易所时段表，不能宣称理论所有30m时槽齐全。完整共同历史仍是W02，概览复用6142原PlotSet且与W02正式数据全量一致。
3. UTI按同一natural_tsa索引解释，未猜Unix单位或源时区；原openTs的.500与导出秒级字段均保留。连续合约、换月及调整细则、源时区未知，未补造规则。ratio纵轴是动态比值而非价格；真实显示轴边距与正式切片范围分别记录。
4. 无待修的本单API/board/覆盖/统一页缺件，无越权服务动作。原专业者尚需实际消费这些数据/页面，继续四例解释、支持/反证与当时可知边界、Owner入口和整批管理接收。Worker未代专业者/Owner登记看图，未作研究完成或管理接受结论。

仅回原签发professional；本回交通过指定分支普通提交和fresh远端读取完成。具体机械核验见[VALIDATION.json](VALIDATION.json)，GitHub实物读取回执见[REMOTE_DELIVERY.json](REMOTE_DELIVERY.json)。本单交付后结束执行，不常驻轮询或自动接新工单，不关闭父任务。
