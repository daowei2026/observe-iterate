Owner 新指令：重新启动 F Run 的 E 阶段。

Run：`OI-U2-F-OBS-20261118-01`

**一、主控规程变更**

本次后续主控动作明确采用 `daowei2026/cgpterm@d4ba9f8711f5d20633f789cacfe41c1aa8ba686a` 的 `observe-iterate-longrun-v2-controller/SKILL.md`，特别是“主控职责的硬边界”。

请核实当前执行环境实际加载了该版本，记录本次 Owner 变更，不静默覆盖旧采用记录。

专业 Workflow、A～E Skill 和业务输入仍采用原 `observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288`，不擅自修改。

**二、收束旧 E 执行链**

先核对 W005 的真实物理状态。W005 不得继续自动派发。若未发送，按 V2 有据记录替代；若在途，先安全停止并取得明确状态；若未知，先对账，不启动冲突的新 Worker 操作。

W001～W005、D005 和全部历史产物保留，不清理、不伪称完成。

**三、从 E 重新开始**

保持同一 Run。A、B、C、D 已完成的本 Run 正式产物继续有效，不重跑。

请把本次 Owner 重启指令正式发送给原 Workflow manager Chat，由 manager 更新 TASK_PROGRESS，并按现行 Workflow **重新签发一次 E Skill 工作**，使用新的合法委派／执行实例，不继续使用原 D005/W005 的执行方案。

manager 只规定任务身份、E Skill 和有效 A～D 输入，不替 E 执行 Chat 设计具体 Worker 工单。

优先考虑新建独立的 E Skill 执行 Chat，避免沿用原 E1 的环境拼装方案；实际聊天创建及绑定由主控按已有授权处理。

**四、E 执行要求**

E 执行 Chat 应完整采用原 E SKILL、WORKFLOW、WORKER_DELEGATION、W1/W2 短执行卡。

W1 应优先在真实现有环境中运行 D；Worker 可以按模板在授权范围内处理确定性的机械问题，不是一报错就返回。

这次重点避免重复之前的错误：

- 不自行加入 Landlock、namespace 或额外沙箱；
- 不默认重建 TIS package、做 overlay 或混合新旧源码；
- 不先制作大量环境报告、审计证据或运输包；
- 如果现有运行环境确实不能找到 FQV 构造模块，由 E Skill 判断真实原因和处理边界，不由主控设计修复方案。

历史上成功运行过的 FQV 现场可以用于定位正常运行方式，但其旧结果不得冒充本次 E 的正式交付。

本次仍只观察 F，不启动 Q/V、不执行全历史 producer、不进入合理性分析。

**五、实际执行**

请不要只形成重启计划。完成必要旧动作对账后，实际调用原 manager，取得新的正式 E 委派，再依据合法工单继续派发。

新 E 的实际任务开始后，报告新委派身份、执行 Chat、Worker 状态和第一个真实业务运行里程碑；不要用文件发布数量代替工作进度。**补充：E 阶段重跑时必须纠正 FRP/TIS 仓库路径混淆。**

本 Run 有两套不同代码来源：

- FRP Haskell 仓库：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`，实际源码仓库应定位到本 Run 工作区对应的 `edh-universe/frp/frp`。
- TIS Python 仓库：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`，Python 构造入口为 `frp/fqv_kline_example.py`，运行导入名为 `mquant.tis.frp.fqv_kline_example`。

注意 `mquant.tis.frp` 不是 FRP Haskell 仓库。

请由重新签发的 E Skill 执行 Chat 在 E1 建立运行基准时，把这两套来源区分清楚，并给 Worker 准确的运行定位信息。

参考 2026-11-16 已成功运行 FQV 的正常 Python 包装方式，但须按 FY 实际工作区核对当前源码和运行包来源，不直接使用当时其他工作区的绝对路径。

Worker 可以处理唯一确定的 import、文件路径和 API 接线问题，但不得自行切换仓库版本、补装重建平台、构造 TIS overlay 或混合 package。

若当前运行环境与本次锁定版本不匹配，由 E1 根据实际证据判断问题性质及后继，不由主控自行设计修复方案。

此补充不改变 A～D 的已完成结果，不扩大 F 的业务范围，也不增加独立环境建设任务。
