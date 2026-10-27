# W03：四个已研究用例的正式30m/mid图数、原日线核对及同页交付

order_id: BI01-CO-01-W03-CASES-30M-MID
work_order_id: BI01-CO-01-W03-CASES-30M-MID
parent_task_id: BI01-CO-01-CASE-RESEARCH-01
work_id: BI-01
run_id: BI-01-CO-01
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-01:professional
issuer_invocation_id: BI01-CO-01-R0008-28f5214c76
issuer_assignment_token: 7d65846a3f3daaa525485c48795725a5
return_to: chatgpt:BI-01-CO-01:professional

本单由当前原执行Pro签发，**尚不表示已发送、Worker已执行或已有新平台URL**。W02已经完成并经R7实际机械复核，不重新派W02，不重取已有全范围日线。父任务仍是完整3–5例研究；本单取得当前四例的必要细粒度证据和原任务要求的整批同页图数，结果回原签发者实际消费。

## 1. 授权、执行者与允许写面

授权依据：`daowei2026/observe-iterate@d4ba5e043367fa4678eca339ba32b53044baaad9:runs/BI-01-CO-01/01_当前任务.md::#technical-work`；已由R5管理采用，不另开Reader或重复采用。专业方法仍固定`f7f2bffe9bcddd951d5bf218d56449e8f42999ae:professional/case_observation/`，现场代码版本、既有差异与本次实际运行分别记录。

沿Owner指定的既有Worker thread `01a17dd7-5033-7e63-b7a2-edd90b691c33`，聊天工作区`/dwdhome/fy/cgpterm`，业务环境`/dwdhome/fy/BASE_E6_2`，既有业务checkout`/dwdhome/fy/observe-iterate-bi01-co-01`。实际消息/执行身份由操作端和Worker如实记录，不用本Pro的invocation/token冒充Worker执行。

仅写现有分支`fy/multisymbol-case-observation-20261027`下本批`artifacts/batch-01/aidata/`的本次调用、组合脚本和交付证据，以及`artifacts/worker-BI01-CO-01-W03-CASES-30M-MID/`的正常回交。现场新run使用独立目录，保留W02冻结输出。不得新建分支、覆盖原数据/回执、改Intake/地图/预算、代写专业解释或管理接受。

本单授权调用脚本与现有组合代码的必要适配、普通错误修通和局部重试，不授权aidata/uplot/tis/frp等工具源码、共享服务、全局注册、安装或部署。已有配置初始化沿W02成功做法；若实际需要新的持久化注册或越权服务动作，保存具体错误交本Pro，不绕过aidata或借其他任务权限。

## 2. 直接输入：四例来自真实日线研究，不是示例日期

下列文件在共同提交`84e4152b626502281fea64a66e72c50091566010`均已存在：

- `runs/BI-01-CO-01/artifacts/batch-01/aidata/W03_CASE_INPUTS.json`：本次准确窗口；
- 同目录`run_cases.py`：现有方式二API调用程序；
- `runs/BI-01-CO-01/artifacts/batch-01/research/analyze_daily.py`、`DAILY_ANCHORS.csv`、`DAILY_METRICS.csv`：原W02数据的只读复核；
- 同批`research/DAILY_RESEARCH.md`和`cases/CO01-C01.md`至`CO01-C04.md`：窗口依据与待核问题。Worker读取本单和相关问题即可，不必加载项目全部历史、上传ZIP或U2/U3工程资料。

| Case | 核心收盘日期 | manual请求开始→结束边界 | 必须能核的直接后续 |
|---|---|---|---|
| CO01-C01 | 2021-03-09—03-31 | 2021-02-01→2021-04-07 | 2021-04-06 |
| CO01-C02 | 2021-08-23—09-30 | 2021-07-01→2021-10-15 | 2021-10-08—10-14 |
| CO01-C03 | 2022-05-10—06-08 | 2022-04-01→2022-06-24 | 2022-06-13—06-23 |
| CO01-C04 | 2023-08-10—09-28 | 2023-06-01→2023-10-12 | 2023-10-10—10-11 |

三个品种一起取数/显示。更早日线回看已有W02支持，不要求把整个此前历史再算成30m。manual是数据请求，不等于核心或图显示范围；日期映射和结束日是否覆盖由真实输出核对。若未覆盖上表必要时点，先核日期边界表达，沿现有接口定向修正，不擅自扩大业务问题或机械加一天冒充已经覆盖。

## 3. 固定业务配置和实际调用顺序

用已采用的`professional/case_observation/examples/aidata_inputs.py`的`make_case_brief`。该输入构造器在f7的blob为`8f44359b17dde2d30e985f20f4866e23742a8f28`，不导入带顶层执行的旧probe。

Context保持`sof_name="TA_updto20240229_DBA"`、`stk_tlist="tick_test_all57_takeout_lcNsiNcy"`、`startDay="2021-01-01"`、`endDay="2024-02-29"`；`blk=extract_time_syms="blk@steel"`，日历`night_end_at_2300`，`generation_depth="big"`，manual四窗。核实际展开rb/hc/i。

正式证据为`KLine(freq="1d")`及`KLine(freq="30m")`的`closeUti`，以及`ScaleTurnCalendar("mid")`实际点`x/y`。`big`是节点层级，`30m`是行情频率，`mid`是贴近转折参数，不生成mid子节点、不改成large。

实际调用：

```text
build_chart_run(brief, dry_run=False)
→ build_big_world_chart_pages(run, run_brief_input=brief, save=True)
→ build_board_run({**brief, run_id: run.run_id}, reuse_core=True, dry_run=False)
→ 现有CAEGraph/PlotSet组合到单页
→ 实际打开与交付
```

第二接口内部有overview，不为相同用途重复调用独立overview。方式二的1d正式切片只覆盖manual窗；完整共同历史仍引用W02正式日线。`reuse_core=True`不是追加节点接口，不改W02冻结core去塞新窗。

调用`run_cases.py`时显式传`--repo-root`、`--request`、`--output-root`和新的`--run-id`，记录实际cwd、解释器、参数和返回路径。脚本已在Pro容器做语法/CLI/请求范围解析检查，**未在mquant环境执行**；普通现场输入适配属于本单，不能据本地检查声称API通过。

脚本若页面异常仍尝试正式board，并以非零码保留缺口；不是全链PASS。已具备core时局部修通按真实支持方式复用，不无故重跑昂贵取数，重试保留理由和身份对应。

## 4. 不重取行情地直接核日线研究

W02原交付固定为`3a761c4ebf4a203ec39cabbd1e9d25413b204f5a`下：

`runs/BI-01-CO-01/artifacts/batch-01/aidata/delivery/bi01_co01_w02_1d_20261028_c4202eae70/`

本Pro实际读取了完整CSV正文，计算使用日期/收盘投影，没有在当前容器执行原字节读取。请用该目录中的已有原CSV执行：

```bash
python <实际repo>/runs/BI-01-CO-01/artifacts/batch-01/research/analyze_daily.py \
  --delivery-root <上述W02完整交付目录> \
  --anchors <实际repo>/runs/BI-01-CO-01/artifacts/batch-01/research/DAILY_ANCHORS.csv \
  --output <本次证据目录>/DAILY_RECOMPUTE.json
```

脚本先核3份已知SHA256、763行、共同时间与已知缺行情，再核73个锚点及重算12行核心统计。将重算与`DAILY_METRICS.csv`按case/symbol比较，记录实际差异和合理的文本舍入误差，不靠人工抄值声称通过。

不一致时给准确文件/行/字段/源值/派生值，交原Pro修正文句；不为了通过而改原CSV、放松hash或代写市场结论。可同时继续不依赖该差异的正式30m取数与页面工作。无不一致也只证明计算对应，不证明经济解释成立。

## 5. 同一平台页面：复用已经定位的原生组合，不另造平台

W02已定位现场组合脚本：

`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/mid_combined_revision/build_native_combined.py`

其已记录SHA256为`14a1c846a602cbf8583696d694694de5700bf0f77eaab6fc82fc3c3f572b6008`。实际读取现场代码并做本批参数/对象适配；若变化如实记，不把旧报告更正前的源码改造建议恢复为待办。

目标是**一个新的真实平台页面**，含本批完整2021起概览和四个Case的30m/mid图。完整概览优先复用W02现有图对象，保持与正式日线对应；若现有组合需使用本次方式二的全范围概览，须核其范围与W02同源而非只含四窗，并明确图对象及数据对应。不能拿四窗1d切片声称完整历史新交付。

旧概览`http://192.168.11.40:6244/graph/cae/6142/report`只作为W02证据，不能冒充四例统一页。新页图标题须能明确定位C01—C04、30m和mid，不要求依赖图序猜用例。颜色主要区分品种；适当缩放/显示余量可调整，但实际显示范围和正式切片范围分别记录。不得用本地PNG、Notebook或多个独立URL代替单页要求。

实际打开时核整页和全部Case，而非只确认HTTP200或URL存在。记录实际打开者、日期、页面/PlotSet对象、标题、图例、渲染错误和截图证据。Worker看图不登记成Pro或Owner看图；转折x/y不是确认时间。

## 6. 必须交回真正可读取的正式数据与对应

以实际`delivery_manifest_path`、`feature_slice_stats_path`、`manifest/timespan_index.csv`定位，不预填node序号、行数、默认参数组名或数据hash。每Case、每品种交完整正式30m及mid切片，保留方式二1d切片和manifest/stats/index，建立Case↔run/node/feature/原文件/副本/图标题的对应。适量文本CSV沿本批delivery新子目录提交，不只交head/tail或远程本机路径；确实过大则按既有合法运输使原Pro可取得。

逐Case核成员、实际首末、有效OHLC、空值、时间对应、mid字段及点落在何处。未提供确认字段时明确缺项，不推测确认时间；有确认字段须说明真实定义和来源，不能以字段名猜业务含义。缺行情保留，不能填零/前值/异时点。连续合约或调整未知继续保留；若具体图数差异依赖它，再准确定位核实。

新增本次`W03_INPUT_AND_CALLS.md`记录真实执行，不改W02的历史实际调用。记录代码/依赖实际版本和影响结果的既有差异，不为了“最新”重置工作区；日志必须脱敏凭据，不提交含认证串的原日志。正式数据本身不得为日志脱敏而改写。

四例将由Pro继续核：C01的两次i反弹是否在30m上确实难保持；C02钢材回落是否存在不同的反复负担；C03较大延伸是否掩盖较大逆向及6月失效；C04原优势换位、恢复保留和10月失效。这些是消费者问题，不授权Worker预填答案或选择新的赢家。

## 7. 交回与完整接续

回交位置：`runs/BI-01-CO-01/artifacts/worker-BI01-CO-01-W03-CASES-30M-MID/FULL_RESPONSE.md`，开头保留本单`order_id/work_order_id/work_id/run_id/issuer_role/issuer_ref/issuer_invocation_id/return_to`的准确同值对应，另列真实Worker执行身份。原签发token只是引用身份，不代作Workertoken。相关VALIDATION和实际证据按正常机制交付；不得再因缺`order_id`重复R7的机械修补。

技术结果仅回`chatgpt:BI-01-CO-01:professional`。正常调用、源核对、普通适配、单页组合和实际交付在本单内连续完成，不每个错误申请一次新Gate。遇真实越权/共享服务缺口保留具体限制和全部已成实物回原Pro，不冻结不依赖部分，也不越权修工具。

本Pro消费真实30m/mid、原字节重算与页面实物后，继续修正四例的支持/反证/当时可知边界、补齐Owner入口和全部图数定位，再按原任务交管理实质接收。技术PASS不等于研究通过，W03结束不关闭父任务，不另起无限批次。

原任务每两小时投入复看照常非阻塞运行，不因本单或新run_id重置起点，也不把投入复看变成再次批准取数的前置。本单提交本身未发送任何Worker或管理消息。
