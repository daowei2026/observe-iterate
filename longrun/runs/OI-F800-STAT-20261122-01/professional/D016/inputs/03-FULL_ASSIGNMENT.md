[OI-F800-STAT-20261122-01-C0035]
recipient=codex:OI-F800-STAT-20261122-01:manager

本C由本Run原manager消费原executor当前委派的最新合法回交。已核真实executor turn、模型/强度、发送token、原D归属和远端原件，不能把当前D完成扩大为业务任务完成。
Return=daowei2026/observe-iterate@fa3d050f1680bbf2e502c7c67c70a1b421642f45:longrun/runs/OI-F800-STAT-20261122-01/calls/C0034/PRO_RETURN.json
专业报告=daowei2026/observe-iterate@6e9521ffc437a307da7413727f80fc2621994d4f:longrun/runs/OI-F800-STAT-20261122-01/professional/D015/EXECUTOR_REPORT.md

按下附Owner最新指令消费原D真实回交。原Skill未完成则续原工作，完成后沿当前采用Workflow选择下一合法动作；已完成且有效部分复用，未完成部分不因历史说明被省略，不机械重复完整理解或有效X/G。保持原control-v0.3、CODEX_NATIVE_DIRECT和C/D/PRO_RETURN，workers=[]，复用本Run原E1；不要向其他聊天发消息、不要创建新线程。manager只协调，不代executor跑Feature/统计，不新造Skill或专业Gate。签发原Workflow规定的执行工作时，只绑定已有方法、准确来源、当前输入和Owner授权，不自写一套专业方法。先发布后继工单/报告/进度，再发布引用已有exact对象的本C Return。新的正式Feature行为变化仍需Owner确认。

Owner最新指令原文（逐字）：

【Owner 接续指令｜继续原 F800 Run，补做高置信不合理现象发现】

继续原 Run：

run_id = OI-F800-STAT-20261122-01

不新建 F Run，不重做已经有效的 U、正式三年 X、D008 全量 G，也不重复已经关闭的 GF001、GF002。

一、采用修正后的专业控制版本

本次以下三类角色统一采用：

daowei2026/observe-iterate@b8c2b513f0b08be6a1fa6782b71bf74a07faff0d

角色包括：

1. controller／主控会话；
2. 原 F manager 会话；
3. 原 F executor:E1 会话。

要求：

- controller 在接续调用中保留上述完整 commit；
- manager 将该 commit 写入 TASK_PROGRESS 和下一项 D；
- executor 在执行前读取该 commit 上的 Control、Skill、实践补充和本次接续输入；
- executor Return 明确记录实际采用的专业控制 commit；
- 不需要重建原 manager 或 executor 线程。

本次准确接续输入为：

daowei2026/observe-iterate@b8c2b513f0b08be6a1fa6782b71bf74a07faff0d:
task-inputs/wall-f-parallel-closure-20261122/F_CURRENT_RUN_CONTINUATION.md

二、当前 Release 处理

当前不接受 F800-REL-001 的有限释放候选。

当前有效事实继续保留：

- FRP = 39f02ec4548e68ba8dbd30061afc870546000994；
- TIS = 2f460d663d821cf2ba25555eda13e78b697d0767；
- D008 当前正式三年 F800 生产和 31 表独立读回有效；
- GF001、GF002 保持 CLOSED；
- 不因本次接续机械重跑 U/X/G。

三、下一项工作

manager 签发一项新的 G 补充工作，在当前正式 F800 结果上完成：

“覆盖面与高置信度并重”的 finding discovery pass。

要求：

1. 复用已有 FeatureUnderstandingPackage、FeatureRunResultBinding、GlobalBehaviorProfile 和 31 表读回；
2. 不在发现第一个候选后提前停止其他适用业务面的检查；
3. 不把仓库中的参考类别当作穷尽清单、固定阈值或自动判错规则；
4. executor 根据 F 的业务对象、身份、生命周期、上下游转化、时间语义、正式输出、全量结果和业务常识，自主判断哪些现象属于高置信候选；
5. 高置信候选不仅要有覆盖面，还要说明：
   - 为什么不是普通波动；
   - 与什么业务语义、对象合同或数量关系冲突；
   - 当前证据支持到什么程度；
   - 还需要 D 确认什么；
6. 形成：
   - FindingDiscoverySummary；
   - 与当前正式结果绑定的 CandidateFindingQueue；
   - ObservationsNotPromoted；
7. 候选队列快照只是当前结果的可追溯记录，不禁止后续证据增加新候选；
8. 原 GF001、GF002 不重复分析，除非新证据直接推翻其闭环。

四、Owner 指定候选

把下面现象登记为必须在 F Release 前完成判断的 Owner 候选：

finding_id = F-LIFE-PEAK-CONCURRENCY
candidate_origin = OWNER_RAISED
status = CANDIDATE
must_assess_before_release = true

observation：
当前正式报告给出峰值责任内 Life = 36。

business concern：
当前只有 rb、hc、i 三个品种；若这些 Life 表达当前仍有效或仍有业务维护意义的共同转折候选组，36 与该业务语义存在明显冲突风险。

不得预设：

- responsibility-in-scope Life 必然等于 active Life；
- 根因必然是历史 Life 累积；
- 根因必然来自 observation_multiple=800；
- 36 已经是确认的代码缺陷；
- 三个品种天然对应某个固定最大 Life 数量。

五、候选进入 D 后的要求

发现队列形成后，逐个进入 D。

F-LIFE-PEAK-CONCURRENCY 必须先形成 LogicLocalization，至少核对：

1. responsibility-in-scope、active、unconfirmed、historical、publication 的准确口径；
2. 峰值时点、持续时间和峰值时全部 36 个 Life；
3. create / revision / end / current 的数量与身份对账；
4. 每个 Life 的 identity、成员、方向、actual、known、age、最近 revision、expiry 和当前状态；
5. 是否存在历史残留、重复 Life、revision 被拆成新 Life、identity 漂移；
6. observation_multiple=800 与结束、revision、handoff 期限的关系；
7. 当前并发统计是否把 publication 持有区间、责任窗口或历史记录误解成业务 active；
8. 最早使该现象产生的责任逻辑，以及准确源码、配置和统计引用。

根据诊断结果：

A. 只是统计或结果绑定问题
→ 走 B；
→ 修正统计或绑定；
→ 更新 G；
→ 不重跑三年 Feature。

B. Feature 行为确实需要改变
→ 先形成责任逻辑定位、修改方案、影响范围和验证方案；
→ 回 Owner 确认；
→ 确认后实施；
→ 正式行为改变后完整重跑 X/G。

C. 证据证明 36 个是互不等价且业务上合理的并发组
→ 说明业务依据和每组的区别；
→ 可关闭为 REJECTED_AS_NON_ISSUE。

D. 证据不足
→ 如实保留未决边界；
→ 不得据此直接 Release。

六、Release 与后继

以下条件满足前：

- 不签 F FeatureReleaseGate；
- 不形成 F UpstreamReleasePackage；
- 不启动 Q 或 V。

条件包括：

- 本轮高置信发现 pass 完成；
- F-LIFE-PEAK-CONCURRENCY 完成判断；
- 同轮其他高置信候选有明确状态；
- 行为或绑定若有变化，已完成相应 X/G 回流。

F 完成后，Q 必须准确消费最终 F800 ReleasePackage，不能用旧 make_features(...) 重新构造默认 F6 并冒充当前上游；V 只在 Q 完成后启动。


历史真实Owner批准原文（仅适用于F800-MP-002既有范围；不扩大最新Owner接续授权）：
<send_user_message_question_reply>
[{"questionItemId":"[\"request_user_input_async\",\"call_bed1268b649643c2a9f881060dcaf00a\",0]","question":"是否批准 F800-MP-002：按确认包内 diff，将正常 KLine 的非有限 close（NaN/±Infinity）记为 InputMissing 并清除 previous 成功邻接状态，Clock 继续推进；保持 observation_multiple=800、delta=600、2Δ、PNV 和正式范围不变，实施真实适配回归、提交／推送并采用新 FRP，再完整运行 F 的 rb/hc/i、5m、2021—2023，完成 31 表独立读回与全量 G？Revision 发行和 UUID／引用链变化须新生产实测；不包含 Q/V 或 WALL 修改。确认包：https://github.com/daowei2026/observe-iterate/blob/2317bd6712e293c1e4c81f696d87192010eb753f/longrun/runs/OI-F800-STAT-20261122-01/calls/C0015/OWNER_REQUEST.md","answer":"批准 F800-MP-002，实施修复并完整复验"}]
</send_user_message_question_reply>

批准ref=daowei2026/observe-iterate@2fa5c26a739d8d97a733f6a7581092a271724e6e:longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/F800-MP-002/OWNER_APPROVAL.original.txt
采用Binding=daowei2026/observe-iterate@3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json
原提案范围内实施、提交/推送采用与完整X/G已有批准并已完成；本次接续不机械重跑。超出本提案的新正式行为修改仍需新Owner确认；旧WALL范围已由Owner终止，不恢复M001。

当前采用专业控制完整commit=b8c2b513f0b08be6a1fa6782b71bf74a07faff0d；按本次准确Owner继续指令和已完成的本D回交推进，不重复已有效工作。TASK_PROGRESS和新D记录该commit，Return原生结果报告明确实际采用commit。旧版本只作历史。
