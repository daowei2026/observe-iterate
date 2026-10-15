# 专业问题的任务绑定、回交与主控逐步处理

修订：2026-10-10-question-work-v2-complete-goal-map。使用 [BI-01专业题与原文](DR12_PROFESSIONAL_QUESTION_CATALOG.md)、[DR13工作组合/管理题](DR13_WORK_ARRANGEMENT_AND_CONTEXT.md) 和 [Overlay13](../overlay/13_角色回交与主控接续协议.md)。专业正文保持自然语言，结构只定位已形成内容。v2修首次输入、续作、触发与试跑连接，并为新采用的EFFORT增加显式持续复看；保留v1及既有v2读取，不追造旧调用采用资格。离线检查不证明语义、发送或部署，旧自动gate未改造。

## 1. 从启动输入到正式绑定

### 1.0 首次管理先取得输入，再产生计划

从未形成计划的新任务采用 `QUESTION_WORK_BOOTSTRAP`（schema=`question-work/v2`, kind=`BOOTSTRAP`）。它只承载已给事实，不要求预先提交业务地图、覆盖、工作分段、四条后续路线或AI预算。主控按Owner已给来源机械填定位，直接投递本节固定启动文字及DR13的M-START；没有明确可识别的目标/授权时仅返回真实缺项，不编业务。

|字段|实际内容及责任|
|---|---|
|work_id|沿用原管理工作身份；首次确无身份时按既有运行规则分配，不能与未来专业工作混用|
|goal_ref / authority_ref|Owner完整目标和授权原文，可为同一条消息；由提供者给出或主控机械定位|
|entry_sources|实际已给的来源，至少一项；无需Owner先整理方法答案|
|existing_work_refs|已存在工作/成果的准确定位；新用例可空，已知旧成果不得隐藏|
|parent|status、ref、reason_ref，按下面规则填写|
|recipient_ref / return_to_ref|本次管理聊天和实际回交接收者的既有身份；不预先发明未来审查者|
|question_ref|本版锁定DR13 `m-start` 的repo/ref/path/selector|
|instructions_ref|本次完整启动消息的实际位置，或本节固定文字与原输入的绑定|

`parent.status`：`NOT_APPLICABLE_NEW_CASE`表示确属新建、当前无accepted parent；`PRESENT`必须引用可取得的exact parent；`REQUIRED_MISSING`必须说明旧用例需要的原件及影响，ref保持null。新建例外不用于规避已有parent连续性。reason_ref指实际解释。缺原件可先恢复目标和安排不受影响工作，不能伪造完整修订/接受。

固定启动文字：
> 按本次Owner完整目标、授权及给定来源执行DR13的M-START。先实际理解用例与已有实物，再形成全部重要剩余、当前可连续执行的安排、必要Owner事项和条件性投入预期。计划、覆盖与预算是本次输出，无需Owner或主控预填。明确未完管理责任；只签发已有充分判断且获授权的工作，不为通过字段检查制造未来成果。交完整管理回答、ROLE_RETURN及引用它的QUESTION_WORK_RETURN。

管理未完成：RETURN.binding_ref指BOOTSTRAP，focus_results仅M-START，batch_remaining_ref交清管理未完，trigger_observations为空；继续同一管理事项。存在合法独立工作时按旧授权继续。管理完成后：原role_outputs.management指向真实判断/计划/签发任务；为获指派的专业工作形成下面的BINDING。不得先签一个空计划再让下游猜。已有有效计划的恢复直接使用实际绑定，不因v2升级重开启动会。

### 1.1 引用格式与材料权力

Git方法、旧实物和任务用 `repo`、40位 `commit`、仓库根 `path`、`selector`；selector为准确标题/锚点/行范围，目录不能替正文。当前完整回答内可用 `{answer_ref: '#实际锚点'}`；保存后按包含它的原始回答身份解析，跨回答必须引用原回答载体，不能将旧锚点指向新回答。

非Git来源保留原身份：
- Owner消息：`source_kind=OWNER_MESSAGE, conversation_id, message_id, selector, snapshot_ref`。snapshot_ref为原样归档的Git引用或null，不以新摘要替原文。没有系统消息ID时用已保存原始记录的唯一定位，不猜不可见ID。
- 附件/ZIP：`source_kind=ATTACHMENT, attachment_id, filename, selector, sha256`。selector说明成员路径/原文范围；实际可核hash就填，未取得填null并说明可用性；不得假造hash。接收者拿不到原件时应先原样转交或归档，原权力保持。

方法锁、用例来源锁分开。live变化只触发影响核对，不能静默换已消费版本。输入失败或selector不存在，由原责任者补定位/材料。可取、读取计划、目标角色实际读取、实际使用分别记录。

### 1.2 正式绑定的字段合同

`QUESTION_WORK_BINDING`置于原签发任务正文（schema=`question-work/v2`, kind=`BINDING`）；`QUESTION_WORK_RETURN`置于本轮完整回答。无需新用例目录、全局注册或第二任务正文。以下定位可复用现有真实正文，不能用ID或空泛句代替。

|字段|必须表达的内容|
|---|---|
|work_id|持续工作身份，普通续作不换|
|goal_ref / plan_ref / full_scope_ref|Owner完整现行目标、由有权管理区分当前安排或历史复核的计划、本段全部范围；不能以最近 remaining 代替完整目标，也不能让已替代旧计划继续发相反行动指令|
|batch_result|本段应形成的可检查观察/证据/图或后续行动，不能只写“推进I4”|
|parent|与§1.0同义；由实际来源判断，不强求新用例虚造父合同|
|question_ids|DR12 I1–I6题号、M-START/M-REASSESS/M-CLOSE/AUDIT或下面受控CASE问题|
|question_definitions|无CASE时空数组；有CASE时逐项给定义、依据和授权|
|professional_mode|当前 BI-01 有权专业 Router／实际任务规定的mode；Router 缺失不得从题号推断写权；兼任职责由真实委派确定|
|focus_ref|首次签发时的集中重点；本段内最新接续按§1.4确定|
|coverage_ref|全部适用义务→题目→真实成果/未完的既有对应；未选本轮仍保留|
|source_reads|来源、requirement、purpose、reuse_evidence；管理／任务责任者区分当前执行、保留业务、待整改对象及历史事实，主控按原profile与DR12准确装配|
|deliverables_ref / completion_ref|本段交付和完整委派的语义完成条件；已否技术项退出，正确业务保留，不复制第二套schema|
|budget_ref|Owner原预期、AI预测、已知投入、偏差和复看条件；历史未知不取消当前预测责任|
|routes|same_work、accept、decide、return_repair四条有权角色/接收者/完整消息；准确可投递|
|triggers|具名RESULT/EFFORT/CHANGE及管理委派，按§1.3|
|explicit_no_trigger_reason_ref|triggers为空时必须有权解释结束/返回为何足够，否则null|

**上述字段的完整目标解释：每次实质业务推进必须朝完整做完所属用例当前阶段全部约定工作进行。禁止把单个Case、一组局部观察、一个入口/文件或最近修复清单设为本轮目标和停点。**full_scope_ref保留全部责任；batch_result记录实际交回增量，focus_ref只决定顺序，completion_ref不得用局部交付结算全目标。真实容量或依赖限制如实说明，其他已明确工作继续；不得为每个地图节点创建一轮任务。

BI-01 管理／专业／审查任务的source_reads必须包含当前阶段完整专业目标、Input/Output/Gate、实际已采用成果、Case/Method/As-Of、证据限制及必要完整方法，按[阶段合同](../../professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md)和[专业材料索引](../../professional/source/INDEX.md)选取。I4须能读取实际观察、挑战和无增量方法，I5制图须保留Pro的业务问题与真实证据，I6后继须保留Owner与Gate权限。当前不存在 CYF 固定 Feature依赖地图的一律必读义务；有证据需要Worker任务时，完整的输入及输出依赖通过[Pro→Worker合同](../../professional/source/04_PRO_WORKER_CODEX_HANDOFF.md)定义。任务索引不得压缩、删除或替代正确专业正文。

普通题内具名子问题优先引用原题，不发新编号。真实必要问题确超出题库时，管理/有权Pro可使用本工作内 `CASE-...`：definition_ref给出业务问题、当前输入、交付、结束/返回和与原义务关系；authority_ref给实际授权；parent_question_id可指相关固定题，确无则null。每个CASE均须定义，未使用的定义不塞入绑定。CASE不自动进入通用core，不扩权限、不豁免其他义务。

`source_reads.requirement`：MODE_FULL是完整mode方法，FOCUS_FULL是当前重点正文，BOUNDARY是相邻合同，PROVENANCE_TRIGGER是具体命中的历史追溯。枚举只表示用途。`reuse_evidence=null`表示本次不主张复用，尚需实际取得；绝不表示已经读过。非空仅在同一上下文已读、未变且仍可使用时成立，目标角色实际阅读/使用写回材料记录。

`FOCUS_FULL` 要求所选正文完整读取，不表示脚本把该来源正文嵌入消息。Owner 要求原文出现在实际消息时，当前任务正文须实际包含全文。已撤完整任务不能继续标为当前执行 `FOCUS_FULL`；追溯使用现有 `PROVENANCE_TRIGGER` 并说明用途。历史正文保留，旧行动不重新取得当前权力。管理已裁定事项由推进者采用，新冲突按原责任处理。

默认专业来源由DR12 的 P00–P07和当前被采用的专业Router/任务Binding共同决定；不能把上游CYF S01–S25当作BI-01必读，也不能让每轮管理者重新发明清单。首次必读负担仍需实际观察，题面不替全文。Owner校准与分支读取 [Overlay02](../overlay/02_Source版本任务授权与人类参与_v0.3.md) §§3–6。

routes每项含recipient_role、recipient_ref、instructions_ref。模板可复用，但占位必须以已有决定/事实填实；新范围或新阶段仍需原授权。技术工单存在不自动指派Worker，也不自动放行专业Gate。

### 1.3 管理触发、稳定责任与无新回交时的处理

trigger保留 `trigger_id, kind, condition_ref, signal_key, route, blocking, effort_limit`，增加 `obligation_id, cycle_id, rearm_ref`；v2的EFFORT可选`repeat=ONCE|WHILE_WORK_ACTIVE`，缺省为ONCE，RESULT/CHANGE只能ONCE。condition_ref是有权Pro写清的真实条件；route指准确管理接收者及M题、完整目标和本次专业结果。blocking只限制具名受影响工作。旧记录没有repeat时继续按一次性解释，不静默改历史。

- RESULT：具名范围的实际形成/接收结果，专业者判定并交证据，不用commit数或小测试替代。
- CHANGE：Owner/方法/业务前提/反馈的具体变化；专业者判性质，主控转交原文。直接Owner纠正不等待Builder批准。
- EFFORT：effort_limit含unit（EFFECTIVE_CALLS/ELAPSED_HOURS）、正limit、count_from_ref。计数基于实际专业/必要管理/审查结果；重复回执和无回答不冒充有效进展。时间按原起点及真实记录，不假填。复看条件不强制通过、缩范围或全线停工。

**管理责任键是 `(work_id, obligation_id, cycle_id)`，证据SHA和计划文件新SHA不进入该键。**trigger_id识别条件；多个条件可指向同一责任键，必须给相同路由/阻塞关系。新证据只更新该责任的依据：PENDING可补输入；IN_FLIGHT/RETURNED附加待消费证据，不再创建并行同项；CONSUMED不因证据升级重发。一次性里程碑在本cycle消费后结束。`WHILE_WORK_ACTIVE`明确授权同一间隔的后继段：首段使用原cycle_id，随后由运行端确定性使用`cycle_id/repeat-2`、`/repeat-3`等稳定键；第N段以原count_from_ref累计值达到`limit×N`为准，累计投入和原起点不清零。

除已明确采用`WHILE_WORK_ACTIVE`的后继间隔外，重新打开同一管理事项必须由有权管理交rearm_ref、理由、范围、新cycle_id和完整消息。持续间隔不授权改变预算、范围、路由或阻塞关系；这些变化仍需正式修订。计划重签默认继承原obligation/cycle及未完状态，不借换SHA重新触发；改名/拆并必须交旧新承接。新的Owner纠正按原权力立即处理，不能用旧CONSUMED屏蔽新事项。

**触发检查也进入既有主控运行循环，无新回答时照做。**在正常循环检查点、从中断恢复、实际计数/时钟更新以及WAIT状态复看时，读取活动绑定和未消费管理责任，核到期EFFORT及已知RESULT/CHANGE；不增加手机轮询/网络频率，不另设调度平台。`WHILE_WORK_ACTIVE`仅在完整工作状态为ACTIVE时形成下一段；IN_FLIGHT/RETURNED先消费当前段，PAUSED/HANDED_OFF/COMPLETE不形成后继。到期采用原消息发管理；未到期只记录，不开管理。运行端停止时不承诺能唤醒自己，恢复后的首次循环补查原起点，不清零。

未知计数标为缺口，使用已签发时间条件；若两者皆缺，按绑定decide交清无法执行的条件，禁止永远当未到期。NOT_YET长期不等于免检：独立投入复看必须检查真实成果和里程碑是否合理。未提供RESULT判断时只向原责任者补判定，不由主控读算法定案。

### 1.4 本轮回交、持续约束与最新接续

RETURN保留schema、kind、work_id、invocation_id、binding_ref、focus_results、material_use_ref、trigger_observations、continuation_ref；v2增加 `batch_remaining_ref`。binding_ref指本次实际派发的BOOTSTRAP或BINDING，不自行追最新。

focus_results每项有question_id、completed_ref、remaining_ref、affected_refs。完成位置可如实写“本轮无实质新增”；remaining_ref只描述当前题，batch_remaining_ref描述本段全部未完，二者不可互相替代。后者应与ROLE_RETURN.remaining_scope_ref解析到同一正文；本轮局部完成不隐去其他责任。

每项触发回state（SATISFIED/NOT_YET/UNKNOWN）及evidence_ref。SATISFIED/UNKNOWN须定位证据或具体缺口，NOT_YET也应给判断依据，确无新增可引用上次观察；不得不回触发来使它消失。BOOTSTRAP尚无批触发，数组为空。EFFORT以实际运行记录核对，不能只信专业者猜时间。

**持续约束**是完整scope、question义务、mode/权限、完成条件、方法锁、预算和接收/触发关系；只由有权修订的正式绑定改变。**最新重点**在原约束内由承办者交清，不要求每轮管理重签。

`continuation_ref`是本轮唯一的实际续作/交接正文。ROLE_RETURN.handoff.instructions_ref必须解析到它；正常CONTINUE时professional.continuation_ref也同指。原binding.focus_ref仅表示初始重点，routes.same_work是固定消息骨架，不得覆盖本轮已授权的最新重点。主控拼装原骨架＋最新同一续作正文＋既有完整范围/源位置，不概括改义。

承办者交自己实际已成、具体未完和合法续作；管理接收、全局预算、全局状态与新范围签发不转给专业者。续作不能缩完整任务；当前任务被有权新采用替代时，旧续作只作历史，不能覆盖新任务。

同回答锚点在两份回交中写相同`#锚点`；Git引用可用 `github:repo@commit:path::selector` 作为ROLE_RETURN的文本定位；消息/附件来源采用已保存的真实载体引用，主控先解析成同一目标再比较。旧回交不可用新回答同名锚点冒名。冲突时退回本次原责任者只修一致性；实质新范围则保持未完交decide，不从两份指令里择一。

两份回交还须与实际派发的work/invocation/token、binding_ref、question_work_ref及真实来源相符。旧结果只留历史，不覆盖新有效指令。结构正确不证明这些引用真实可取或业务在授权内。

### 当前专业工作说明：不特设 CYF C 工作段

当前任务及最新合法continuation的权责，继续完全沿用上面的§1.4。BI-01 专业执行的当前阶段、Scope、Output/Gate和必读材料，分别由[六阶段合同](../../professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md)、[阶段接续](../../professional/source/03_STAGE_HANDOFF_AND_READINESS.md)以及实际Binding提供。不得将CYF的五段Host工作或`CURRENT_C_WORK`当作新的BI-01机器阶段、必填标记或模板。新签工作或旧任务被替代时取有权`current_task_ref`完整正文；同工作合法续作时取最新`continuation_ref`，不得缩小完整范围。原`ROLE_RETURN`和`QUESTION_WORK_RETURN`字段不变。

### 1.5 可直接试跑的完整输入

完整三组数据、原始合成回答、绑定、消息、前序记录、变体和预期在原Overlay的 [question_work_trial_inputs.json](../overlay/tests/question_work_trial_inputs.json)，执行说明见同目录 [question_work_trial_walkthrough.md](../runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/tests/question_work_trial_walkthrough.md)。无未来SHA和待补业务占位。所有CYF原有市场例子均为历史测试输入，不具有生产/Owner用例权力。

## 2. 主控的确定处理顺序

本协议适用于受控人工/模型主控。主控只补位置、身份、版本及已观察执行事实，不生成业务范围、优先级、标准或新限制。

0. 首次无计划按§1.0取得BOOTSTRAP并投递M-START；恢复按真实活动绑定。既有循环同时执行§1.3无回交触发检查。
1. 完整保存原回答与实物，按原派发核work/invocation/token/来源。收取不全不归咎角色漏交；重复NOOP，旧结果仅补历史。
2. 解析恰好一个ROLE_RETURN，再取得question_work_ref、RETURN及其确切输入。核schema、职责、题目定义、mode和引用；按§1.4核最新重点及两份回交同义。
3. 缺结构/定位/指令一致性按原return_repair定向补。缺实质分析继续原专业/管理工作；同一机械补交一次仍失败交decide窄处理，不无限重试或全面重审。BOOTSTRAP缺项返回原提供/承办者，不让Owner先填计划。
4. 核Owner/方法/任务变化的实际影响。普通检查点不收回原授权，已知错误只限制依赖动作。旧gate冲突报告，不静默跳过或造PASS。
5. 主动作按原ROLE_RETURN：IN_PROGRESS/CONTINUE续原工作；SUBMITTED交原接收；NEEDS_DECISION交有权判断；WAITING_INPUT具名等待；交付INCOMPLETE补交付。管理尚未完成不派依赖未定判断的新方向。
6. 独立核全部trigger和稳定责任记录，无论主动作CONTINUE/SUBMIT/WAIT。RESULT/CHANGE消费专业原判，EFFORT核实际记录。到期管理、非阻塞专业续作和已签独立接收分别保留；冲突/UNKNOWN不默认未触发。工作ACTIVE但所有一次性复看都已结算、又没有持续复看或等价管理／交接时，返回“持续管理安排缺失”，交原管理者补关系，不由主控挑新数值。
7. 按原任务/固定操作文字＋最新一致的续作正文＋准确原文入口生成消息。管理输入保留完整目标与重要工作位置。主控不润色业务，不自行增加完成压力；必须原样传递Owner已明确的完整推进目标及禁止局部停点要求，不将其改成必须虚报一轮完成。
8. 按稳定责任键记录PENDING/IN_FLIGHT/RETURNED/CONSUMED/SUPERSEDED。准备不等于发送，收到不等于消费。已有循环可顺序投递不同聊天，不宣称后台并行。
9. 管理返回核总体判断、后继、地图/预算/Owner事项及未完。只有决定实际进入有效任务/下一输入后才CONSUMED；管理部分完成续同事项，不受影响专业工作仍可继续。
10. 原mode的实质接收和本段条件决定关闭；全目标另核全部义务。拆并/改派交身份承接、未完finding和触发迁移，历史投入不清零。

C正常消息额外原样带选定当前工作说明，按Overlay08取源；当前任务已被新采用时不再用旧续作。主控不改说明，原完整任务／范围／两份回交及管理触发仍保留。

## 3. 主动作与管理责任并存

一批I4专业观察已有部分可信事实、必要挑战仍未完。RETURN回CONTINUE并报告某项已绑定非阻塞管理条件SATISFIED：主控发送原专业续作及已签发M-REASSESS两条消息。重复同回交不重派。后续消费者修订改变证据SHA：原管理在途则补证据，已消费则只记新证据，不重新发同一回看。需要新判断由有权Pro开新cycle并说明依据。前提被否定且影响后续时仅暂停该依赖，不能所有trigger都设成不阻塞或全线阻塞。

## 4. 固定操作文字

普通续作：“继续〔原工作/实际binding〕。完整范围与权限仍按原任务；本次采用〔最新完整RETURN的continuation_ref〕，已完/全部未完见〔对应正文〕，方法与相邻输入见〔确切来源〕。朝完整完成本用例当前阶段全部约定工作持续推进，当前重点只决定顺序，禁止单Case或局部修复完成即停；不重做无新依据成果；发生重要变化具名返回。交完整实物、材料使用、全部触发观察及一致的两份回交。”

补回交：“原回答与实物见〔位置〕。只补〔确切字段/引用/两份续作不一致/兼任职责缺项〕。保留原实质和资格；缺的是分析就保持未完并继续原工作。不得为过格式检查新增业务决定。”

补交付：“已成判断见〔位置〕，原承诺〔确切实物〕尚未取得。完成原交付；确实还欠专业工作则交清原工作未完。主控没有新增业务要求。”

审查：“按已签发独立审查委派，对〔exact候选/范围/新依据〕使用〔DR12题和完整方法〕复做承重判断，返回实际finding和影响；已有覆盖见〔位置〕。探针/Builder自评不代替独立资格，局部不升整包。”

管理回看：“执行稳定责任〔work/obligation/cycle或repeat段〕，本次条件与证据见〔位置〕。按〔M题〕消费〔完整目标、重要工作位置、相应专业成果和原文〕，完成投入取舍/剩余/预算/地图/具体后继。任务仍继续时交清下一段工作和复看安排；已有持续间隔可有据保留或调整，本轮返回不取消看管。原专业及已签接收按〔既定阻塞关系〕继续、收取或仅暂停受影响动作。新证据更新已有事项；未完继续同一管理事项。”

启动采用§1.0。所有括号来自已有决定和真实位置，必须填实后发送。机械补交与发布收尾不升实质里程碑，完成后接回原主体。

普通专业续作在上述原骨架之外带最新合法续作正文。具体目的和后继由原Pro形成，主控只投递；没有标记的旧材料按Overlay08兼容，不能补编阶段。

## 5. Harness、离线检查与真实试跑

[question_work.schema.json](../overlay/tools/question_work.schema.json)区分v1/v2及BOOTSTRAP/BINDING/RETURN。[question_work_check.py](../runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/tools/question_work_check.py)只核可观察关联和返回待处理责任，不发消息、不写运行状态、不判断专业语义/授权。引用存在与实际阅读另核。

语义检查仍用当前BI-01实际授权的专业审查依据及管理Harness，核题目与输入是否适当、原义务是否实做、重要反馈是否被消费。向后追Owner与完整方法，向前核接收者无需猜。schema通过不等于读懂、选题正确、独立审查或部署。

原question_work_cases.json保留16项覆盖提纲；三组完整试跑材料先验证启动、连续工作/管理并存与无回交到期、回交冲突。记录实际recipient、原样prompt、context、状态、未消费责任与重复次数。STRUCTURE_CHECKED、PROTOCOL_WALKTHROUGH、ROLE_RUN_OBSERVED分开；预期输出不能填成实际观察。

## 6. 采用与升级

README→DR12/13/14→本次适用专业方法→BOOTSTRAP或有权BINDING→实际角色RETURN→主控准确投递构成采用链。旧v1结构继续可读；只有有权管理在原接收中明确迁移，才对新调用采用v2。迁移保留work/来源/已审/预算/在途/触发消费，记录旧新绑定承接，不追改原回答或重开一轮业务审查。

本次没有接通自动发送或修改workmap_gate；`question_work_check.py`只计算显式持续段并报告连续性缺口，不写ledger。实际入口若仍加载旧上传包，应取得本版规范路径和真实版本；旧seal只证明旧字节，不能假称已采用。管理未被唤起、下一消息未送达或真实角色未试跑，分别如实报告。

已明确撤销的非实质任务必须从当前工程正文、工作单、前置、验收和后继定点删除，相关只服务它的代码和检查由原实现者删除；不得列为未来必做或暂缓欠账。其余正确正文禁止压缩、摘要替换或仅留历史引用。新方法、完整Goal、地图与实际任务同步采用；已确认跑错的在途任务停止受影响部分，正确在途版本和真实已完成事实保留。发布材料不声称已经向其他聊天或工程师送达。
