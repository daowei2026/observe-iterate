# W02：取得本批正式全范围日线，回原专业者开展多品种研究

work_order_id: BI01-CO-01-W02-FULL-HISTORY-1D
parent_task_id: BI01-CO-01-CASE-RESEARCH-01
work_id: BI-01
run_id: BI-01-CO-01
issued_by: chatgpt:BI-01-CO-01:professional
issuer_invocation_id: BI01-CO-01-R0006-f352c5b081
issuer_assignment_token: a21908ab367a401eb0f50d0c5a94f0a0
return_to: chatgpt:BI-01-CO-01:professional

本单由原执行 Pro 正式签发；签发不表示已经送达 Worker、已经调用 aidata 或已经取得数据。实际派工沿既有工程师机制，由操作端记录真实发送与执行身份，不沿用签发 Pro 的 invocation 冒充 Worker 调用。

<a id="authority"></a>
## 1. 权力、目的和完整责任

授权来自 [完整专业任务的技术工作段](https://github.com/daowei2026/observe-iterate/blob/d4ba5e043367fa4678eca339ba32b53044baaad9/runs/BI-01-CO-01/01_当前任务.md#technical-work)，该完整任务已由 [R0005 管理采用](https://github.com/daowei2026/observe-iterate/blob/d814fd492552f48923321249b0245cd6226f3433/runs/BI-01-CO-01/reviews/management-R0005/DECISION.md#adoption)。不申请重复采用，也不重开 Reader。

父任务仍是 rb/hc/i 的 3–5 个实质不同的多品种差异用例、逐例自主回看解释、正式图数、同一平台页面和 Owner 入口。本单提供尚缺的共同历史正式输入，不把父任务改成取数验收或一个用例。Worker 不代选赢家、不预填用例日期、不写投资结论。技术结果回原签发 Pro 消费，不能直接替代整批管理接收。

本单执行范围是：按已确定业务输入构造并调用现有 aidata，取得完整共同范围 1d 正式数据及概览定位，核足以支撑下一步研究的真实覆盖和口径，并将可消费文件交回。普通输入适配、研究脚本调整、日志整理和局部重试在此单内连续完成；不得把第一次报错或只生成 URL 当成完成。

## 2. 执行者、环境与写面

按 [Owner START](https://github.com/daowei2026/observe-iterate/blob/0c00de3312d8428ff94b76352a6a24f8a190b843/runs/BI-01-CO-01/OWNER_START.md)：Worker 使用已有 thread `01a17dd7-5033-7e63-b7a2-edd90b691c33`，预期聊天工作区 `/dwdhome/fy/cgpterm`。操作端依原授权核真实聊天/工作区，异常按 Owner START 已有规定处置，不提前通读无关历史。业务执行环境为 `/dwdhome/fy/BASE_E6_2`，沿用现场已有 Python、配置和必要环境入口。

结果及本单相关调用脚本写入 `daowei2026/observe-iterate` 的现有分支 `fy/multisymbol-case-observation-20261027`，范围限 `runs/BI-01-CO-01/artifacts/batch-01/aidata/` 及本次正常 Worker 回交位置。运行输出在业务环境下为本批新建独立目录并记录实际路径，不覆盖原测试或其他 run。不另建分支，不改公共地图、Intake、管理决定、发送回执或全局配置。

本单不授权修改 aidata/uplot/tis/frp 源码、共享服务、全局注册、依赖安装或部署。已有配置初始化不等于允许新增全局 Feature 或改变共享服务。确有这种需要，保存具体错误、直接消费者与受阻范围回签发 Pro；不绕过接口取数，不借其他任务写权，不冻结已能取得的可靠数据。没有 Haskell 修改，不做无关编译或全环境审计。

## 3. 实际使用的源和调用程序

完整当前用法：[03_AIDATA_USE.md](https://github.com/daowei2026/observe-iterate/blob/f7f2bffe9bcddd951d5bf218d56449e8f42999ae/professional/case_observation/03_AIDATA_USE.md)。结果记录要求：[02_OWNER_DELIVERY.md](https://github.com/daowei2026/observe-iterate/blob/f7f2bffe9bcddd951d5bf218d56449e8f42999ae/professional/case_observation/02_OWNER_DELIVERY.md)。输入构造复用同版本 `professional/case_observation/examples/aidata_inputs.py`，blob `8f44359b17dde2d30e985f20f4866e23742a8f28`，不是导入带顶层执行的旧 `probe.py`。

本 Pro 已提供调用脚本：

`daowei2026/observe-iterate@eacadfa7d16493ad792de56123f69f1f1c19a864:runs/BI-01-CO-01/artifacts/batch-01/aidata/run_overview.py`

脚本只调用现有接口并记录 stdout；没有平行取数、特征实现或新的数据平台。已在当前 Pro 容器 Python 3.13.5 执行 `py_compile` 和 `--help`；未在业务 Python/mquant 环境实跑，不把本地语法检查当成 API、数据或页面通过。

执行时向脚本传入三个真实参数：`--repo-root` 为包含上述输入构造器的实际 observe-iterate checkout；`--output-root` 为本批新运行输出目录；`--run-id` 为本次 aidata 唯一运行身份。记录实际命令、cwd、解释器、输出目录与参数。已有运行身份冲突时先核实际产物，不覆盖或无故重复昂贵计算；重试记录真实理由和新旧对应。

脚本沿用原成功调用中的 `ensure_profile_runtime()` 配置准备，不将自定义 brief 称为标准 Profile v4。现场必要差异以真实代码/配置为准；若该步骤实际要求未授权的持久化注册或服务改动，停该操作并精确回交，不据注释扩大权限。

## 4. 本次固定请求与真实覆盖

| 项 | 本次输入 |
| --- | --- |
| 对象 | `blk="blk@steel"`，`extract_time_syms="blk@steel"`；预期 rb/hc/i，核实际展开 |
| 数据集 | `sof_name="TA_updto20240229_DBA"`，`stk_tlist="tick_test_all57_takeout_lcNsiNcy"` |
| OptContext | `startDay="2021-01-01"`，`endDay="2024-02-29"` |
| 日历 | `calendar_override="night_end_at_2300"` |
| 节点 | `generation_depth="big"`，`big_source.mode="manual"` |
| 全范围窗口 | `("2021-01-01", "2024-02-29", "full_history")` |
| 正式证据 | `KLine(freq="1d")`，`uti_fields="closeUti"`，`feature_key="kline_1d"`，`slice_levels=["big"]`，行情 sidecar |

通过既有 `make_overview_brief` 构造，不绕过 aidata 调用 KLine/数据库。记录实际 aidata checkout、相关依赖/配置版本、会影响本次结果的既有本地差异和数据绑定；不为了记录版本而更换工作区到 latest，也不把原测试缩写 SHA 补造成当前完整 SHA。

执行顺序：`build_chart_run` → `build_run_overview_chart_page` → 同 core 的 `build_board_run(..., reuse_core=True)`。本单不调用 `build_big_world_chart_pages`，不伪记第二接口或单页组合已经执行。

概览页面调用失败时，脚本仍尝试同 core 的正式 board 交付，并以非零退出码保留页面缺口；这不是全链 PASS。core/board 失败则如实保留错误。已建立 core 的合法复用与页面局部重试按现有 API 完成，不通过修改冻结节点求成功。

日期字符串是请求边界，不是结束日全天包含承诺。必须给每品种原始时间字段、按真实平台口径解释的首末时间、总行/有效 OHLC 行/缺失行及主要缺口；记录共同有效范围及缺失是否影响可比性。不要猜 UTI 单位、时区或日历映射，不把空行情填零，不拼接异时点。若实际成员或数据集与稳定请求不同，明确反馈差异，不悄悄改对象。

记录连续合约/换月与归一化口径中已能核实的部分；查不清的具体项标未知及影响。不把显示坐标当价格，不声称范围内每行都有效，也不声称 2021 前不存在历史。

## 5. 必须回交可读取的数据，而不只是路径

以本次 `board.delivery_manifest_path`、`board.feature_slice_stats_path`、`manifest/timespan_index.csv` 及其真实引用为准定位正式 CSV，不硬写测试节点/参数组名/行数。

回交内容包括实际入参和调用脚本/日志、manifest/stats/timespan index，以及 rb/hc/i 的完整正式日线 CSV。三份日线在体量合适时以原文件副本放入本单 aidata 目录的实际 delivery 子目录，记录副本到源文件、run/node/feature_key 的准确对应；不要只交 head/tail 或抽样表。大文件保持原输出位置并经已有合法运输使原 Pro 真正可取得，不上传工作区、缓存或凭据。仅有远端本地路径而接收者仍读不到文件，不算已完成输入交付。

在 `aidata/INPUT_AND_CALLS.md` 中写本次实际事实：完整 Context/窗口、成员展开、实际版本和必要差异、各 API 实参/顺序/成功或失败、真实 run/output_root、文件定位、覆盖/缺项、时间/换月/归一化说明。尚未执行的调用写未执行，不能把本单预期抄成调用记录。

概览若成功，交真实 URL、平台对象和图内名称；实际打开者与结果另记。未打开或只有程序返回 URL 时如实写，不能替专业者声称看过像素。本次概览不是最终包含全部 Case 的统一页面。

现场方便取得时，可同时定位原测试目录 `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/mid_combined_revision/补充测试报告.md` 及其真实引用的组合脚本，保留准确位置供后续复用。没有取得不阻塞正式日线回交；不重跑原 2013/large 测试，不把旧 URL 当本批页面，不再签已经被更正的源码改造方案。

## 6. 交回、限制与正常后继

Worker 在实际回交说明已经执行和未执行的部分、有效数据范围、具体失败及原单内可继续动作，返回 `chatgpt:BI-01-CO-01:professional`。无工具源码修改时不制造工具仓 commit；技术成功也不填写管理接受、Owner 认可或投资研究完成。

本单完整结果是可消费的正式共同日线、真实调用及覆盖说明和实际概览状态。正式数据一旦具备，原专业者直接消费，完成全批候选比较和回看；如仍有页面缺件，只保留页面依赖，不等待其修完才研究。之后由原 Pro 根据真实选出的 3–5 例及回看需要给出方式二窗口，继续取得 30m/mid 与统一页面。此为原完整任务内部依赖，不增加管理 Gate，不把 W02 返回当父任务完成。

本单没有授权 Worker 自行确定新的业务目标、解释规则、用例日期或完整任务接收结论。实际权限缺口回原签发 Pro，必要时由其按原 Binding 交管理；普通调用与脚本修通不逐错误另行批准。
