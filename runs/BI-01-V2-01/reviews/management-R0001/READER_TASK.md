# BI-01 V2 首次地图独立只读接收任务

task_id: BI01-V2-WORKMAP-READER-01
work_id: BI-01
run_id: BI-01-V2-01
professional_mode: INDEPENDENT_REVIEW
recipient_role: review
recipient_ref: chatgpt-project:细节叙事生成_金标/chat:new:BI01-V2-地图只读接收-01

此为 R0001 管理在既有 review 职责中的一次性、只读工作安排；新上下文尚未创建、未发送、未返回。不新增常驻角色或审查系统，不授 U2/U3 全业务独立审查 PASS。真正曾参与这份候选形成的承办者不得作为独立读者，即使换聊天也不独立。

<a id="scope"></a>
## 1. 完整受托范围

按既有 Workmap 首次采用合同，独立阅读下列 exact 输入，从 Owner 完整目的而不是地图作者的状态名称，确认：一个没有参加编写的读者能否理解业务要检验什么、已有真实数据和其资格、当前完整任务、生产者/消费者、局部阻塞边界、未完和实际后继。

只判地图/任务可理解性及前后一致性。不得编制、改写或修补地图/任务，不替管理签预算/全局接受，不给 U2/U3 公式、图、数据或投资判断做未实际执行的专业验证。发现问题给具体位置、原文、导致何种执行误解和受影响范围；非问题不凑 finding。

必须区分首次地图阅读与 AI 视觉看行情：此处读的是管理/任务文字；本轮 Owner 看 aidata 图，业务执行 Pro 读图对应结构化数据，不要求像素进入模型。

<a id="target"></a>
## 2. 已冻结的实际输入

工作输入锁 `daowei2026/observe-iterate@ff84e7e9d22d4c6d6e2633c9701404afcca1b827`：

- `runs/BI-01-V2-01/README.md::full`；
- `runs/BI-01-V2-01/00_长程推进地图.md::full`，七个业务锚点 goal/stage/evidence/progress/remaining/management/next；
- `runs/BI-01-V2-01/01_当前任务.md::full`，包含 `#question-work-binding`，task_id `BI01-V2-S123-OBSERVATION-01`，task blob `442c47cc30226796a16b6f7420af9748d0d1e00e`；
- `runs/BI-01-V2-01/reviews/management-R0001/DECISION.md::full`；
- `runtime/config/WORKMAP_BINDING.json::full`。

Owner 原文锁 `11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`，真实启动 `e07034fbab080df85af57da4362d5a24119a8bbe:runs/BI-01-V2-01/OWNER_START.md::full`。同一 policy lock 的 V2 04/05/06/01/02/03、ADOPTION_HANDOFF_CHECKLIST、DR14、Overlay13 和原 Workmap 工具是适用方法。读者不需要为地图可读性重做 EAW 全公式审计，也不能仅凭管理概述认为算法已被独立验过。

上述输入后的 R0001 回交、读取任务及 provenance 提交不是重新定义业务。操作端在发送前确认 reader-input 仍一致；若 map/task/Owner/rules 发生实质变化，用实际有权的新 input 重新绑定，不能把旧 reader 报告冒充新输入报告。

<a id="focus"></a>
## 3. 需要实际恢复出来的业务关系

用自己的话完整说明这项业务如何从固定 rb/i/hc 数据，经过 S1 观察问题、S2 aidata 真实图/同源数据，到 S3 事实/反证/增量认识与管理/Owner 下一行动。以下是当前容易发生误读而需核查的承重点，不是让你只审几条而忽略完整范围：

304 条同实际 UTI raw 候选与一个 Case 五个 As-Of 是两个不同证据层；只有前者中的两成员候选可在三品种内看第三对象，完整 Case 组外数为零。四方面为 Movement Bundles，不是四资金接口。Working/Completed、actual/known/As-Of 和 Reference/Shadow/Withheld 不混同。初始 OBSERVATION_SCOPE 绑定 S1/S2/S3 完整职责，而不是 S1 做完就停，也不允许未经管理改机器 mode/角色。

同时恢复明确的排除项：不重算/替换固定数据，不等待正式 H1，不做 AI 像素看图，不重测已确认基础环境，不在观察仓建第二套图工具；必要 aidata 通用修改只在独立新分支。核是否存在“管理说排除、实际当前任务又要求”的相反正文。对正确业务字段、状态、时间、方法和消费者不能用删除来消歧。

<a id="coverage"></a>
## 4. 输出、完成与资格

交完整只读报告到 `runs/BI-01-V2-01/reviews/independent/WORKMAP_READER_R0001_INPUT.md`，标明实际调用身份、实际输入 commit、task blob、真实阅读范围、是否真正未参与候选形成、恢复出的完整业务关系、确切歧义及其影响。没有实质歧义才可将本次狭义地图阅读 verdict 写 PASS；有歧义写 REPAIR_REQUIRED，资料或独立性不足写 INSUFFICIENT_EVIDENCE。PASS 只覆盖此次地图可理解性，不覆盖固定计算正确性、S3 完成、正式质量或 Owner 接收。

<a id="completion"></a>
完成指上述范围已真实阅读并报告结论，必要原文不足及未审部分如实披露，附原 ROLE_RETURN 的 review 输出和 QUESTION_WORK_RETURN；不能因 report 文件存在就称独立接收发生。不得修改候选；受本次委托可提交自己的独立报告及本轮回交。操作端按真实新 R 记录，不把这次待派任务预记为已发生 R0002。

<a id="budget"></a>
## 5. 预算与不中断完整业务责任

当前预测一次有效只读调用即可完成本受托范围，不是强制一次 PASS。确欠输入/独立性或实质分析未完按真实限制接续，不能以补字段冒充完成；不把阅读扩成全仓审计或 U2/U3 算法验收。它计入原 BI-01 V2 的必要 Pro 实际投入，不新建总预算、不清零 R0001 起点。

<a id="no-extra-trigger"></a>
不为这项一次性地图接收另设 RESULT/CHANGE/EFFORT 循环：完整工作持续复看已由专业任务 Binding 的三个触发及本管理承担；本受托事项按一次完成/缺件/实质歧义路由返回，不能与主工作并行重复同一管理义务。

<a id="same-work"></a>
## 6. 只读续作/有限补交

继续相同 exact 输入的本地图只读受托范围，仅补尚未实际阅读/判断的部分，保留真实已成；不能修改地图或切换成业务执行。纯回交缺字段只补确切缺件，不重做已成判断。相同交付错误一次有限补交后仍失败，交当前管理接管，不无限回到读者重复同句。

<a id="accept"></a>
## 7. 实际收取与已签采用路径

完整回交运输回原操作端 `codex-thread:01a14a59-7f26-7921-b549-3e7cd9be5119`。该接收者是既有操作 Codex，不是新业务裁定角色。其合法业务依据为 R0001 管理 `DECISION.md#authority`：独立读者能完整恢复任务且无实质歧义时，允许对同一 reader-input 按既有工具机械发布 Workmap Intake 与采用，无需 Owner 再批启动；实质歧义必须走下节管理决定，不由操作端看 finding 自行判业务通过。

操作端需要从真实 local Git 执行原 `runtime/overlay/tools/workmap_gate.py snapshot`，记录观察输入及 fingerprint。提交真实 reader 报告后，以实际最新 Git 中相同 map/task/Owner/rules 的输入核 `reader_fingerprint`；reader-input 未变可复用该真实报告，不因它自己的报告加入 result tree 而重复开读者。Intake 的 manager decision_report 绑定实际 R0001 决定 blob，reader 绑定真实 report/input_commit/input_snapshot；不得填假 reader、snapshot 或 validation_claim。

Intake 写在原配置的 `runs/BI-01-V2-01/reviews/WORKMAP_INTAKE_CURRENT.json`，新任务按首次签发而非 ROUTINE_RESULT 处理；原始 Owner GO、policy、专业 Binding 与完整 task_payload 原样保留。实物/前置校验满足后，再机械将 config 标 ADOPTED，并使用原 check/dispatch、真实发送端 NOT_SENT 和任务载荷身份核验。`provenance/turns` 不纳入业务 watch 根。这个过程不启动 U2/U3 重算，也不改变专业完整任务。

采用时的 base 为首次真实管理开始前的 `2e817e2e8408b714185be55aa8f443e389b92ddf`：当时已有模板 config，但 map/task/intake 尚不存在。原工具若不能把这个真实首建状态作为合法比较基础，准确报告机械缺口回管理，不随意拿 current 充当旧已接收 base，也不自己改工具或关闭 gate。读取、记录、发布和 actual send 分别报告。

<a id="decide"></a>
## 8. 歧义、前提冲突或权限问题

交 `chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理`，M-REASSESS。带 exact input、具体歧义、对哪个工作/消费者的实际影响、你的真实阅读结论及未完。管理负责修 map/task/Binding 和重新采用，不让读者代写候选；不把局部问题升级成全部业务或全历史审计。没有实质问题就不发明新限制。

<a id="parent"></a>
本次是新 run 首张地图的首次独立只读接收，没有旧 run 可复用的 reader 资格。parent 为 NOT_APPLICABLE_NEW_CASE；这是受托事项关系，不取消 BI-01 完整管理和专业责任。
