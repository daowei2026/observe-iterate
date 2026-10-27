# Worker 工单：修通首次阅读的既有运输与原签发者回报链

order_id: BI01-CO-01-W01-READER-TRANSPORT-REPAIR
work_id: BI-01
run_id: BI-01-CO-01
issuer_role: management
issuer_ref: chatgpt:BI-01-CO-01:management
issuer_invocation_id: BI01-CO-01-R0002-3ee411679c
issuer_assignment_token: 3de1c23ae8ff4b26b64efba16976ae64
return_to: chatgpt:BI-01-CO-01:management
worker_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
expected_chat_workspace: /dwdhome/fy/cgpterm
repository: daowei2026/observe-iterate
branch: fy/multisymbol-case-observation-20261027

<a id="authority"></a>
## 1. 真实签发及目标

由本轮管理[完整裁定](https://github.com/daowei2026/observe-iterate/blob/1503a17f4d0e408393544f47f686804240011107/runs/BI-01-CO-01/provenance/turns/R0002/FULL_RESPONSE.md#decision)签发。本工单可以在首次 Workmap Intake 尚未产生时执行；其用途正是修复生产首次阅读证据所需的运行链，不需要虚造 Intake 才能施工。它不授权 Reader 通过或首次专业研究发送。

实际业务仍为 rb/hc/i 的 3–5 个多品种差异用例及逐例回看解释，正式数据经 aidata，最终交统一平台页。本单不选 Case、不运行行情、不改业务方法；修复完成后回原管理，使其恢复真实 Reader 和专业研究。

**在一个有限工单内连贯完成已定位故障及同一链条直接消费者的必要兼容修改、定向验证和可接收交付。** 不以消掉一个错误或改好一个函数为主动停点，也不扩大为全仓审计、运行平台重建或全部历史规则清理。

本单是工程执行授权，不是已派发/已启动证明。首次派工由主控按 Owner START 核准确线程和真实工作区；异常按 Owner 已给后备处理，不并发第二个写者。聊天工作区不是 observe-iterate checkout 路径，实际定位并记录源码目录及其分支、起始提交和相关本地差异。

<a id="sources"></a>
## 2. 必要输入与读取边界

| 准确来源 | 用途与读取范围 |
| --- | --- |
| `observe-iterate@1503a17f4d0e408393544f47f686804240011107:runs/BI-01-CO-01/provenance/turns/R0002/FULL_RESPONSE.md` | #decision、#diagnosis、#plan、#continuation、#worker-reception；已经完成的管理裁定、具体问题、写权和回报，不重新研究全局目标。 |
| `observe-iterate@46e60ed697f2b1e9ab791c7d64ba3100dca376ed:runs/BI-01-CO-01/provenance/turns/R0002/DISPATCH_BLOCKER.md`、`PRE_DISPATCH_RESULT.json` | 两份全文；唯一实际触发的错误、未发送事实及验证基线。 |
| `observe-iterate@6767da04ec7d6d98c576b348ed38cc2209b81c20:runtime/tools/bi01_run_gate.py` | 实际故障基线；first_reader、first_reader_reception、pre_dispatch、after_return 及直接依赖。 |
| 同提交 `runtime/overlay/tools/management_prompt.py` | source/locator、prepare_dispatch、github_reference_message、load_return_sources、verify/recipient 及 CLI 接合；复用现成实现。 |
| `observe-iterate@f7f2bffe9bcddd951d5bf218d56449e8f42999ae:runtime/overlay/12_管理接收与地图校验.md` §3、§5，及 `13_角色回交与主控接续协议.md` §2–§5、§8 | 已采用的短指引、独立 JSON、真实身份、原签发接收和资格边界，不采用其中已被管理明确替换的旧业务工作名称。 |
| 同一 f7 提交的 `runtime/overlay/tools/workmap_gate.py` 的 worker_result 及相关字段读取 | 区分已采用工作流的 worker-result 与本次没有 Intake 的原签发者问题回报；不能伪造 accepted base。 |
| `observe-iterate@56e7b84cc78f75828ebb602cf0bc74a7c4aa6a1a:runs/BI-01-CO-01/provenance/turns/R0002/INVOCATION.json`、`DISPATCH.json`、`SEND_RECEIPT.json` | 本次管理回报的真实形状。读取 INVOCATION 指向的确切归档未发 Reader 准备，仅为复现本次故障；不是读取所有旧 runs。 |
| `observe-iterate@c133f1069bda8f11f116653e724fb69deb38265d:runs/BI-01-CO-01/reviews/management-R0001/READER_TASK.md` 的身份、#input、#question-work-binding；`observe-iterate@989e732fc6a017669184184e8e132947cb1685c3:runs/BI-01-CO-01/reviews/management-R0001/DECISION.md` 的 #adoption、#reader-pre-adoption | 核对本次原签发授权、合法角色/route、冻结输入。必要校验可读取其真实引用，但不要求 Worker 重做市场专业分析。 |
| `observe-iterate@0c00de3312d8428ff94b76352a6a24f8a190b843:runs/BI-01-CO-01/OWNER_START.md` | 真实分支、Worker 和运行授权。 |
| 当前实际 checkout 的 `runtime/tests/test_bi01_run_gate.py` 及直接命中的既有提示/回交测试 | 查找并扩充能复现该问题的现有 fixture 和断言；不递归读取全部测试。 |

固定政策与方法基线仍是 f7；现有源码已核基线为 6767，施工时记录实际 current。若相关代码已有其他真实变动，按差异追实际依赖，不倒退覆盖。没有具体依赖时，不读旧 ZIP、完整 U2/U3、无关专业 Source、cgpterm 历史聊天或 aidata 代码。

<a id="repair"></a>
## 3. 已确定的修复责任

### 3.1 首轮 Reader 的手机字节核验

原 `first_reader` 将 `prepare_dispatch` 生成的长全文直接与手机短 `PROMPT.md` 比较，实际报 MESSAGE_CHANGED。接入已经存在的 `github_reference_message(repo, prepared, loc)`，先核 exact Git 全文等于完整 prepared，再核转换后的短字节、recipient 和本轮身份。

`prepare_dispatch` 本身没有 `github_message_ref` 参数，不通过传一个不存在的参数解决。真实 INVOCATION 的 `full_assignment_ref` 带 blob 元数据，现有 source locator 只接受 repo/commit/path/selector；按真实接口投影并核对其余已有元数据。保留全文与手机两个摘要的不同含义，不让错误摘要、错全文位置或正文篡改被“兼容”放过。

### 3.2 Reader 成果的接收

`first_reader_reception` 同样接入一致的短指引核验，消除其对旧运输形式的额外要求。利用现有 `load_return_sources` 处理完整报告、独立 QUESTION_WORK_RETURN 和独立 ROLE_RETURN；保持原 schema、token、work/invocation、binding、原角色与 route、最终提交树中报告和 Q-Return 字节一致等检查。旧合法内嵌回交保留兼容，但不强迫新回交同时在报告里重复内嵌 JSON。

`accept` 仍必须有实际 Reader 的合法派发、真实发送及完整有效回交，不能用技术报告替代 Reader。代码通过不表示候选地图已独立通过。

### 3.3 原签发者问题与本单技术结果的回报

当前 R0002 的 `decide` 是 Reader 未发时的实际阻断回报，不存在 Reader latest_response/latest_return；不能继续以“Reader 已完成”作为这项管理问题回报的前提。

沿现有 `decide` 与证据引用支持限定的原签发者回报：核同 run、原 Reader task/Binding、管理签发依据和准确管理接收者；输入必须定位真实阻断及受影响准备，或本轮已签工单及其真实技术结果。不得仅凭 role=management、route=decide、一个自报错误字符串或 status=NOT_CONFIGURED 放行任意消息。

本单结果回原管理也属于这一限定问题处理链。没有初始 Intake 时不调用既有 worker-result 并伪造 accepted base；保留该工具对已采用工作流的保护。在现有检查器/共享适配中容纳本次有依据的回报，检查工单 order_id、签发 invocation/token、return_to、实际结果与工单关联，以及原签发调用的真实发送事实。主控先完成本次管理发送记录对账；Worker 不替手机端补造发送证据。

问题回报通过仅说明可把事实交回原签发管理者，不等于允许专业发送、地图采用或技术候选已发布为 current。无需新 Return schema、自由正文入口、人工 skip 开关或第二状态机。

### 3.4 冻结输入、历史与实际调用

保留原 task/decision/source/fingerprint/run 身份及未发送/在途/去重等校验，不通过删除断言换取通过。错误对比应改为对正确载体的等强核验。

历史 R0002 管理已进入本对话，原未发 Reader 已归档。不得把任何一个改成另一个角色，不能覆盖原 PROMPT/INVOCATION/失败证据或复用其 token 做新实发。隔离 fixture 可复现旧输入并明确其身份；真实下次 Reader 由主控产生新调用。

本单技术报告位于受监控 artifacts，会影响冻结输入。保留这个真实变化，不从 watch_roots 排除整个业务面，不自行改 Reader 输入或地图。管理实际接收后再用真实提交刷新四项冻结输入，并取得新 snapshot；测试须如实区分运输兼容通过和当前冻结输入仍需要合法刷新，不能掩盖后者。

<a id="write-scope"></a>
## 4. 写面、施工与非目标

允许在既有分支修改 `runtime/tools/bi01_run_gate.py`、直接必要的 `runtime/overlay/tools` 共享运输/回交适配及其已有相关测试，提交本单技术实物。若复用现成函数即可，不复制一套转换器或 Returns 解析器。实际必要的相邻调用点在同单内连贯修复，不设封闭文件白名单或逐错误申请。

不另建分支，不 force push、不重写历史；与别的真实写者冲突时先对账，不覆盖他人变化。正常已有 Python/Git 环境即可，不为本单安装或升级共享依赖。工具实现候选的准确提交与固定政策、专业方法来源分别记录，不能自动把全 run 改为 latest policy。

不修改本批业务要求、R0001 决定、公共 README/地图/专业当前任务、WORKMAP_BINDING/Intake、Owner START、原派发/发送事实；不改 cgpterm、aidata、uplot、tis/frp、共享服务、聊天数据库、Goal/调度器或生产凭据。不执行真实手机发送、不生成假 Reader PASS、不自动放行专业任务。实际写权超出本单时，说明具体依赖回管理；普通单内工程选择无需逐项请示。

<a id="validation"></a>
## 5. 定向验证与完成条件

先用现有测试和本次 exact 输入确认实际原因，再改直接路径，完成必要正常与拒绝分支。至少覆盖：

| 检查 | 必须保留的实际含义 |
| --- | --- |
| 正常短指引 | 原 prepared 全文、已提交全文、转换后的手机短文分别核对；不再因长短不同误报 MESSAGE_CHANGED。 |
| 篡改与错配 | 改全文、手机字节、接收者、关键身份或 exact 来源仍被拒绝；不能只测一个正例。 |
| 独立 JSON 回交 | 合法完整报告/Q-Return/ROLE_RETURN 可被原管理接收路径解析，身份/引用或最终树不一致仍被拒绝；已有 inline 合同不被无故破坏。 |
| 限定原签发者问题回报 | 本次真实 NOT_SENT 阻断及本工单关联的技术结果可用于原管理 decide；不存在真实 Reader 时不能走 accept，任意其他管理者/任务/无依据豁免仍不能通过。 |
| 输入与运行边界 | 冻结输入变化、错 run/role、未对账的实际发送状态等继续可见且不被兼容修复吞掉。 |

这里是本次具体反例的最小相关验证，不要求构造所有故障排列、全系统回归或新测试启动平台。运行实际适用的已有测试并写出命令、准确代码版本、退出结果及失败内容；必要 fixture 与实际本 run 的只读重放分别说明，不把 fixture 内人为状态当作现场 COMMITTED。

完成标准：同一链条的修复代码和必要相关测试已提交；实际错误得到定向复现与修复证据；报告讲清哪些消费者已验证、哪些真实发送/Reader/管理采用仍未执行。若实际剩余是需要管理刷新 Reader 冻结输入，准确交出证据，不自行修改该业务任务；这不同于还漏做运输/接收兼容。尚有单内可完成项则继续，真实环境/权限阻断才交具名缺口和全部剩余，不用局部文件完成结算整单。

<a id="delivery"></a>
## 6. 交付与返回

代码、测试和技术报告提交到本单指定分支。报告固定位置：

`runs/BI-01-CO-01/artifacts/worker-BI01-CO-01-W01-READER-TRANSPORT-REPAIR/FULL_RESPONSE.md`

报告头保留 `order_id/work_id/run_id/issuer_invocation_id/return_to` 的本单准确值，记录实际执行身份和现场来源，不冒用 R0002 的管理身份。必要测试记录可放同一技术产物目录，不复制全工作区或上传敏感值。

报告必须说明：实际 checkout/前后提交及差异；对上述具体原因的处理；测试命令与结果；真实 vs fixture 证据边界；保留的保护条件；影响哪些当前动作；全部未完、具体停止原因和原管理应消费的位置。GitHub 普通提交后 fresh 回读，按既有 Worker 回交渠道交准确 commit/报告位置，不创建额外业务控制表或第三种 Return。

**结果只回 `chatgpt:BI-01-CO-01:management`，由原签发者按[技术接收任务](https://github.com/daowei2026/observe-iterate/blob/1503a17f4d0e408393544f47f686804240011107/runs/BI-01-CO-01/provenance/turns/R0002/FULL_RESPONSE.md#worker-reception)实际消费。** 主控只按本单准确来源接回，不因没有 accepted Intake 改投其他角色，也不让 Worker 自己宣布运行版本采用。

管理接收足够后，才明确采用工具提交、刷新 Reader exact 输入并签恢复。后续是真实独立阅读、管理 Intake 和完整 CASE_OBSERVATION，不是再开一次启动规划或让 Worker 代做研究。代码候选完成不关闭 BI-01 的完整目标。
