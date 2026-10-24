# 接续 BI-01-FO-01 长程任务

接管并接续既有长程任务 `BI-01-FO-01`。这是新的操作 Codex Chat，不是新的业务 Run。

**操作仓库**

- `daowei2026/cgpterm`
- 分支：`fy/observation-iteration-agent-longrun-20261015`

**专业及运行仓库**

- `daowei2026/observe-iterate`
- 分支：`fy/bi01-feature-observation-prep-20261021`
- Owner 已认可的专业规范修改 commit：`21dd5971f493a6d724948b84dacb7b200ff43b54`

`work_id=BI-01`，`run_id=BI-01-FO-01`。

**本次接续性质：Owner CHANGE 后，原执行 Pro 对既有专业问题进行实质再判断，并继续长程任务。**

本次专业规范修改已得到 Owner 认可。按照现有运行机制完成必要的规范采用与合法派发，**将下述专业任务交回原 `BI01-FO01-执行` ChatGPT 聊天，由执行 Pro 负责完成：**

> 对 R0022—R0025 中工作3不兼容问题、N 专用 aidata 路由及既有处理方案重新进行专业判断。
>
> 从完整业务预期出发，搞清楚相关既有特征、参数、正式输出、工作2展示、uplot、aidata 及其消费者的性质、定位、真实能力和相互关系。
>
> 根据实际源码、输入输出、运行结果及已有证据，调查究竟哪些地方不符合预期、可能有哪些根因及相互影响，再判断合理的解决方案和修改位置。不能预设当前 N 专用路由正确或错误，也不能因为问题发生在 aidata 就认定必须修改 aidata。
>
> 尽可能完成充分、清晰、有依据的分析并有效推进。暂时不能可靠确定结论时，也应充分交清已查事实、不同解释及其依据、尚缺的关键证据和实际取得办法；需要现场技术调查时，可按既有权限签发 Worker 工单。
>
> 在现有授权内自行处理能够决定的专业事项。涉及已有管理认可、重要跨工作取舍、受保护上游、共享平台公共行为或新增权限时，带具体依据和建议交原 Management Pro 处理；真正需要 Owner 决定的事项再由管理提出。

**本次首要实质专业工作由执行 Pro 承担，不要求 Management Pro 代做根因分析或预先决定技术方案。** 如果现有 Owner CHANGE 路由必须先由 Management Pro 采用新规范或更新授权，则先按原机制完成必要的采用与签发，并将上述任务交原执行 Pro，不扩展为管理 Pro 自行重做方案研究。

操作 Codex 按既有机制读取：

- `cgpterm/AGENTS.md`
- `cgpterm/.agents/skills/observation-iteration-longrun-controller/SKILL.md`
- `observe-iterate/runtime/config/COORDINATOR_DISPATCH.json`
- `observe-iterate/runtime/overlay/08_自然语言运行提示_v0.3.md`

其他材料按实际操作入口定向取得，不自行扩大为全仓审查。主控不自行解读专业问题、选择技术方案或代写新的业务任务。

先核实原 Run 的真实暂停、在途、交付及已处理状态，不重发旧工单、不重做已完成的机械工作，不清零原运行历史。新 commit 只按实际采用关系影响后续合法调用，不倒改历史。

执行 Pro 回交后，按真实结果和既有管理接收、授权及继续运行机制接续整个长程任务。
