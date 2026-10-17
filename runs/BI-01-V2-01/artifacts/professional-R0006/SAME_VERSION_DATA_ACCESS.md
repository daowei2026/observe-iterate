# R0006 同版本图数取用情况与有界运输需要

work_id: BI-01
run_id: BI-01-V2-01
invocation_id: BI01-V2-01-R0006-fe69b0114945aca3db55f8f2
assignment_token: 414f9171be0c0306828a3826c0f5513f
role: professional

## 性质与既有授权

本件是执行 Pro 对已有图数的取用记录及输入运输需要，不是重新画图工单、主控派发或管理接收。采用 R5 已定处置和实际 `worker-R0004/final/WORKER_RETURN.md`：`BI01V2-R0004-AIDATA-FIXED-01` 已技术完成，不能因本件重派或重新运行。

权威输入为 `daowei2026/observe-iterate@1917f868d61f8de7110b7165ee9125e5b156c4d2:runs/BI-01-V2-01/artifacts/worker-R0004/final/`；run `BI01V2_R0004_fixed_20261018_033648`，aidata `e59fd90de5237b8a6756de00e54bdf841832fad4`，坐标检查 revision 2。main1 当前包为 `8dd8824509375c57a1f47756d30403bc0fca92a0d6ab38c1ce839b174467f86c`，不是旧144CSV或中间146CSV包。原R5已允许不能直接取得Git二进制时，由原Worker/操作端运输同版本CSV正文及范围/源引用；不新增Owner批准前置。

## 本轮已经实际取得什么

已逐段读取当前五个As-Of的 MAIN_R02_15、MAIN_N1_15、MAIN_N2_120、MAIN_R03_15及MAIN_R02_AND_N_CURRENT_EPISODE_SOURCE_ALIGNMENT的完整CSV正文。已进入 `6ea55f5a3351106e9e3e2bf731ae81cbf9507c37` 的main1可读目录，读取对应VIEW、SOURCE_BINDING、manifest及有关真实图层CSV；专业正文将列实际消费范围，不把目录有146文件写成146文件全部已读。

另实际从 `chart_data_packets/C1_ROW_0033.zip` 的GitHub base64分段响应取出四个完整原CSV成员（known/C1、GATE、MEM、N1），解压长度和各成员ZIP CRC均相符，并直接读取其原值/源行/As-Of/node字段。这说明该二进制不是完全无法读取；同时，这不等于本轮已取得整个ZIP或所有视图。

已消费的C1_ROW_0033同图记录中，i原锚定Down段为Completed进展-5，rb原锚定段为Working进展+77；图中组外hc的N1实际存在，Working进展+89。相应源行和方向连接正在进入本轮业务分析，不能因为尚未完整取到其他包而搁置这些已取得证据。

## 具体取用限制

GitHub `fetch` 不支持二进制下载；`fetch_file(encoding=base64)`提供分段文本，但没有把仓库ZIP挂载成当前Python可直接打开的文件。当前只对上述一个包完成有限成员提取，未取得320包的可批量消费原件。不能由图索引、包哈希或Worker的技术通过摘要补造尚未读取的CSV值。

本轮对已知44MB的 `LAYER_DISPLAY_SCOPE_INDEX.csv` 实际调用 `fetch_file(...,start_line=1,end_line=4)`，返回blob `acb1e0d401fb8853d1beba8fa58f67d3cfda928b` 但 `content=""`。这是当前读取接口未返回正文，不是CSV合法空、市场Pending或图层不存在。现有相应Worker验证记录仍有效；不为此重测Owner已经核过的环境。

两份固定源ZIP已经在本项目可读，不能把来源原件缺失与图层导出取用缺件混为一谈。原源可以有界辅证，但不能冒充某个尚未真正消费的aidata图层导出。

## 原运行端可直接处理的运输内容

优先提供现成 `final/chart_data_packets/` 中原版本数据包的可读取附件/既有共享运输，附当前 `CURRENT_VIEW_VERSION_INDEX.csv`、`REQUEST_WINDOW_NODE_MAP.csv` 和对应VIEW/SOURCE_BINDING。只复制已存在字节；不重新导出一批近似结果、不重新画图、不改固定输入或aidata。

若现有运输更适合GitHub文本，按原47请求对应的51个As-Of，复制原包内供本次业务消费的CSV正文（保留全部原列及_aidata字段），而非只给索引。优先补主Case2–5的价格/实际-可知/段端点图层，35个已选C1窗口的known C1/MEM/N1/N_WORKING_ORIGIN及三品种OHLC/turn层，以及11个未覆盖turn窗口的对应层。N2及进一步图层按已经明确的业务判断实际需要连同运到。可以为运输顺序拼接同schema的原行，但须保留node、可见性、As-Of、原包成员名、原行与原包SHA，不计算新的字段值；不在观察仓写第二套切片工具。

完整320节点的材料仍保留。先后顺序不成为删除全范围或停止专业观察的理由；更广范围新命中具体反例时仍沿现有节点/包取用。无需为文件数量建立新的控制表或发布系统。

本件只陈述已发布的输入需要，未声称操作Codex已收到、已经发消息或运输成功。后续按原同工作续作回本专业聊天消费。已取得部分的S3与其他不受影响工作继续，完整未完由本轮FULL_RETURN记载。
