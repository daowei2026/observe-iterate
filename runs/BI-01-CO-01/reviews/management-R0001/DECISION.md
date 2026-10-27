# R0001 管理决定：签发完整研究任务及首轮只读采用检查

work_id: BI-01
run_id: BI-01-CO-01
role: management
invocation_id: BI01-CO-01-R0001-7be1958ac0
assignment_token: e54daafab7ff4edea048b452e45340f8

<a id="decision"></a>
## 决定全文与范围

本决定的完整实质判断、来源处置、业务链、全部未完、投入预期和材料使用见[本轮完整回答](https://github.com/daowei2026/observe-iterate/blob/215bc3ae1c4817fdbc3be4494fb1b6b674103da4/runs/BI-01-CO-01/provenance/turns/R0001/FULL_RESPONSE.md)。本文件物化签发与接线决定，不替代 00–04 完整专业方法。

采用 `observe-iterate@f7f2bffe9bcddd951d5bf218d56449e8f42999ae:professional/case_observation/` 的 README、00–04，以及 `0c00de3312d8428ff94b76352a6a24f8a190b843:runs/BI-01-CO-01/OWNER_START.md`。本次是新 run；旧 GO、数据、预算、Gate、任务和资格不继承。

DR08 §3 的旧四项业务指定、MANAGEMENT_METHOD_HARNESS 的 P00–P07/I1–I6/工作2→3→4 旧依赖、Overlay12 §5 的旧 FEATURE_OBSERVATION 说明，不是本次当前义务；完整回答 #decision 已完成具体裁定。它们没有进入本次专业任务/Binding/验收/后继。通用身份、回交、真实证据、独立性和持续管理仍适用。不要求专业执行者重判这些已知事项，也不签通用材料重写或全仓审计。

<a id="plan"></a>
## 完整工作安排

签发 `runs/BI-01-CO-01/01_当前任务.md`，task_id=`BI01-CO-01-CASE-RESEARCH-01`，mode=`CASE_OBSERVATION`，逻辑接收者 `chatgpt:BI-01-CO-01:professional`。完整责任是本批 3–5 例的位置与回看研究、同一平台页和真实调用证据，不是先做一例或只修工具。当前签发不冒充已完成采用或已发送。

首版请求范围为 rb/hc/i、2021-01-01 至请求 endDay=2024-02-29；正式覆盖依本次实际输出，不能称已覆盖结束日全天。先方式一全范围 1d 正式数据，再按真实候选窗口使用方式二 30m/mid。自由回看、相关补数和不相互依赖工作可连续推进，不新增逐步 Gate。页面暂缺不冻结已具资格数据上的研究，但统一页面未交不能称整批完成。

管理维护地图、采用与全局安排。执行 Pro 负责业务分析、技术工单签发和对 Worker 结果的消费。实际 Worker 沿 Owner START 的指定 thread/workspace 与回原签发 Pro 规则；没有实际工单不提前读其历史。本次不授予工具仓/共享服务源码改动权。

专业 Binding 采用完整批次 RESULT、重大 CHANGE 和每累计两实际小时的持续 EFFORT；详见当前任务的具名条件和路线。计时起点是专业首次合法发送的实际回执，不因管理返回重置。回看不是强制完工或停工点。

<a id="adoption"></a>
## 本轮采用权力及尚未采用部分

本轮管理**已经采用上述专业方法，并签发启动候选地图、完整研究任务和首轮只读任务**。允许的即时后继仅为下述首轮 Reader 的独立阅读与返回本管理。

本轮没有独立 Reader 证据，没有 workmap-intake，不将 WORKMAP_BINDING.status 写成 ADOPTED，不放行依赖该正式采用的首次专业发送。主控不得以本段的“采用方法”偷换为“地图 Intake 已采用”，不得把初始阅读改记 ROUTINE_RESULT。

Reader 结果回原管理后，由管理实际核其发现与输入版本，决定接收/定向返修；只有真实决定和相应实物齐全才机械建立 Intake、检查并激活专业任务。不预签 Reader PASS，不给未来证据编 SHA，不授权主控代裁。

<a id="reader-pre-adoption"></a>
## 新 run 首轮 Reader 的具名预采用授权

依据本次 Owner GO、ADOPTION_HANDOFF_CHECKLIST、V2_ROUND_RECORD_CONTRACT 及 Overlay12 的新意图独立阅读要求，现签发：

- 任务路径：`runs/BI-01-CO-01/reviews/management-R0001/READER_TASK.md`。
- task_id：`BI01-CO-01-WORKMAP-READER-01`。
- role/mode：`review` / `INDEPENDENT_REVIEW`。
- 逻辑接收者：`chatgpt:BI-01-CO-01:review`，由主控绑定真实未参与本候选编写的独立上下文；此名称不是已验证 UI 聊天 ID。
- 结果接收者：`chatgpt:BI-01-CO-01:management`，原管理继续承担实际采用判断。
- 独立产物窄目录：`runs/BI-01-CO-01/reviews/independent/workmap-01/`；读者另交自己的真实 R 回执，不改管理候选或全局状态。

Reader 的输入必须是同一准确提交中的 run README、地图、专业当前任务及当前 `runtime/config/WORKMAP_BINDING.json`，加完整 Owner START、专业方法及本管理依据。该输入提交由本轮 Reader 任务中的 source_reads 固定；计划引用本决定 #reader-pre-adoption，task_adoption_ref 引本决定 #adoption。不得把根目录名当正文。

主控使用现有 `bi01_run_gate.py` 的 first-reader 路径（`--run-id BI-01-CO-01`，全链同一 Binding），建立真实 INVOCATION、原样载荷和发送记录；这是在没有 Intake 时生产真实阅读证据的限定授权，不是普通专业派发豁免。机械执行 snapshot、保存真实指纹可以由主控做，但不等于 Reader 已读。

Reader 检查：目标与两项产出是否完整；3–5 例和自主回看有无缩水/新增 Gate；aidata 与方式一/二的数据边界、2021/mid/统一页面、实际/确认时间是否清楚；角色写面、来源采用和旧任务退出是否准确；连续工作、接收、预算和后继能否无需猜测地执行。需要报告具体冲突及影响，不能只签“可读”。本次不审不存在的市场结论、不会要求读者生成 Case 或先跑全基础设施。

Reader 任务签发不产生新业务 Run，不沿用旧 Reader 的身份/通过/特例，不增加常驻角色。受审候选变动只核真实影响；独立输出本身不循环污染 reader_fingerprint，完整管理指纹仍记录相关变化。

<a id="delivery-scope"></a>
## 本轮交付与接收边界

本轮交付：完整管理回答、此决定、run README、长程推进地图、完整专业任务及其 QUESTION_WORK_BINDING、具体化但未激活的 Workmap Binding、首轮 Reader 任务及其 QUESTION_WORK_BINDING，以及 R0001 的独立 QUESTION_WORK_RETURN/ROLE_RETURN。

这些是本次首次管理成果，不包含实际行情、Case、平台 URL、Reader PASS、Intake 或专业发送证明。后续管理承担真实 Reader 接收、专业结果/重大变化/投入复看和最终批次收拢；本轮已完成签发不取消持续管理。

<a id="continuation"></a>
## 唯一实际后继

执行完整回答 #continuation。先核远端本轮全部产物和真实身份，按本决定派首轮只读 Reader；阅读结果经原管理真实接收后再采用并派完整专业任务。机械问题定向回原责任者，不能重开全仓审计、用旧 mode 绕过，或让执行 Pro 代填管理缺件。
