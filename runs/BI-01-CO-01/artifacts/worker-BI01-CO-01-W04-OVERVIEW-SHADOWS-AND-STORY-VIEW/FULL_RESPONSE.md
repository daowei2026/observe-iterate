---
order_id: BI01-CO-01-W04-OVERVIEW-SHADOWS-AND-STORY-VIEW
work_order_id: BI01-CO-01-W04-OVERVIEW-SHADOWS-AND-STORY-VIEW
parent_task_id: BI01-CO-01-CASE-RESEARCH-01
work_id: BI-01
run_id: BI-01-CO-01
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-01:professional
issuer_invocation_id: BI01-CO-01-R0013-e7e3db9f05
return_to: chatgpt:BI-01-CO-01:professional
cycle_id: owner-change-20261028
worker_execution_id: BI01-CO-01-W04-worker-ac26d5b83e
worker_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
worker_local_execution_turn_id: w04-b3576f243562448ba4659eb7dcfe9e71
started_at_utc: 2026-10-28T11:43:49.364154+00:00
result: PARTIAL_WITH_RUNTIME_GAPS
---

# W04 完整实际回交：候选代码已交，阴影及四例图面尚未通过

本单没有取得真实阴影/重开/缩放/显隐或四例故事图面PASS。已连续完成有限写面内的直接链路修复、定向回归、持久对象保存及独立回读、冻结文件保护、57项定向原值核对和真实浏览器重试；最终定位到两项不能在本单写面内处理的运行环境缺口，现将已成实物与全部未完回原签发professional。不以候选提交、参数回读、HTTP200或旧W03通过代替本次接收。

完整签发源 `ad7d3b94b04f93f2f188e99409b7ee39f10f4bbb:runs/BI-01-CO-01/artifacts/professional-R0013/WORKER_ORDER.md::full` 已核11530字节/SHA256 `3b5a1336be72b9601eba7357c84a2c25116ca13aa6b3b1e2b8c85e08f32c0316`。原Pro token `8d8f62f310e444221d56efc34755fe63` 仅引用签发来源，不冒作Worker身份。原生Codex turn ID未暴露/未从只读接口取得，不补造；本地执行turn、真实thread和UTC如头部/[执行记录](../batch-01/aidata/w04/WORKER_EXECUTION.json)。

## 已成实物

1. **aidata候选源码普通提交** `b5a752c2701dd8997b47583808f30bc5da5d9769`，现场既有分支 `codex/aidata-named-csv-features-20261019`，基线是开工实际HEAD f58ea95c358b9ac31659c92b7bc20fe9bf7f8264；未切/退/新建分支。只改 `big_world_chart.py` 及必要定向测试。[完整patch](../batch-01/aidata/w04/AIDATA_SHADOW_REPAIR.patch)和[commit/hash记录](../batch-01/aidata/w04/TOOL_COMMIT.json)随观察仓GitHub可读，不只交本机源码路径。工具仓未推送远端、未部署/刷新运行时；此为待专业消费的候选，不宣布current采用。
2. **持久对象6149**保存旧五图配置和W03四个显式冻结范围/Case标签。独立新进程从正常DAO回读，四范围、五PlotSet匹配且6148旧对象未变，[参数持久回读](../batch-01/aidata/w04/PERSISTENCE_READBACK.json)通过。当前[6149原生入口](http://192.168.11.40:5006/cae?node_id=6149)实际报参数定义错误，不能交作可用统一图页。
3. **34项定向回归通过**：日期/数值/单点范围、不可解析显式失败、原标记/显隐、默认overview行为和组合只标概览。最终真实pytest 34 passed/20.57s；fixture和生产边界在[VALIDATION.json](VALIDATION.json)分开，不冒称真实日历或像素通过。
4. **原件保护与字段定位**：W02/W03的56份源文件及Git副本hash前后相同；uplot/frame/quant/tis/m3sof既有状态/hash均保留。没有重取行情、重跑core/board或倒写旧报告。17个故事视口已准备，R0013的19组价格时间对×三品种=57项与正式原CSV相符；[字段核对](../batch-01/aidata/w04/FIELD_LOCATIONS.json)不代替实际看图。
5. [完整实际输入/调用记录](../batch-01/aidata/w04/W04_INPUT_AND_CALLS.md)、[保存对象及旧新对应](../batch-01/aidata/w04/SHADOW_PAGE.json)、[真实浏览器结果/错误截图](../batch-01/aidata/w04/browser/)、可复用脚本和脱敏日志均已交。原始日志只留gitignored，正式原数据未为脱敏改写。

## 两项真实运行缺口

**共享Bokeh运行端仍使用旧参数定义。** 6149正常恢复在参数实例化时拒绝新增 `combined_graph_config/overview_scope_rows_json`，错误中列出的允许字段仍为旧版。工程新进程可正常保存及回读参数，不能据此推断共享运行端已经采用；[准确错误全文](../batch-01/aidata/w04/browser/initial_error_sanitized.txt)及截图已保存。

**同一自然日历文件不可读。** 本地正常布局第一次尝试，以及旧[6148](http://192.168.11.40:5006/cae?node_id=6148)本次独立打开，都报：

```text
OSError: [Errno 5] Input/output error:
/m3varI/BaseData/futures/TA_updto20240229_DBA/sof/../calendar/night_end_at_2300/natural_tsa.dba
```

旧页真实调用链是 `CAEGraph.layout → PlotCtx → sof.tsa_of → DbArray`；[错误全文](../batch-01/aidata/w04/browser/fallback_error_sanitized.txt)可读。第二轮浏览器已给旧页360s恢复等待并取得该错误，未把一次短超时直接当根因。旧6148配置/正式数据未改，W03当时的历史成功仍保留。

工单§1及Owner有限授权只允许aidata相关页面组装、范围坐标及局部验证，明确禁止全局注册、部署或共享服务修改。因此未刷新共享运行时定义、重启服务、修NFS或更换日历/数据绑定。这是具体消费者和权限边界，不是把一个普通脚本错误另设审批。

## 全部未完及可继续位置

| 项目 | 实际状态与影响 |
| --- | --- |
| 四个冻结原日期/Case/node对应 | 已核并持久保存，取原W03四窗，不是核心区间或轴余量 |
| 原日期→真实数值UTI→最终阴影 | **未通过**；本地日历I/O失败，服务端新定义未采用；不给猜造数值，不用首末bar替代 |
| 四阴影像素、正常重开、缩放/显隐、遮挡 | **未核/未执行**；新旧正常入口均无价格图，HTTP200不是PASS |
| C01 | 三个拟核视口已准备；03-15前恢复、hc随后失效、22日后i反弹和hc后段推进，均未取得本次图面证据 |
| C02 | 四视口已准备；判断前两次恢复/回落、后续两次损害、i局部往返和10月反例，均未实看 |
| C03 | 五视口已准备；判断前较大反向/重新恢复、23日后再反向、5月31日延伸和6月失效，均未实看 |
| C04 | 五视口已准备；7月旧状态、21日前新依据、24—29日守位升级失败、9月/10月后续，均未实看；未以微小价差冒充明显可见 |

逐视口状态见[VISUAL_STATUS.json](../batch-01/aidata/w04/VISUAL_STATUS.json)。实际浏览器和错误页像素的查看者为Worker，不是Pro或Owner。无价格图就不补造ratio基数、hover结果或关系清楚结论；mid实际/确认、closeTs/closeUti_ts差异和历史接收限制继续保留。

原Pro可以立即消费候选代码、定向验证和字段材料，不必停止已有数据上的研究。后继需由有权责任者恢复同一日历的可读性并安排共享运行端采用候选定义；随后先复用现存6149正常重开及转换核验，不重复建core、取数或新增对象；再执行已交浏览器脚本完成四阴影与17视口，按真实结果修正文句和Owner入口，由原管理接收。Worker不自行签发部署或代作研究结论。

观察仓按原分支普通提交和fresh远端回读交付，机械记录见[REMOTE_DELIVERY.json](REMOTE_DELIVERY.json)。本次有限执行在准确回交已成及上述运行环境缺口后结束；不常驻轮询、不另派工、不关闭父任务。
