# 启动 BI-01-CO-01 长程任务

现在由 Owner 正式授权启动并持续运行新的长程任务 `BI-01-CO-01`。

**本条是新 Run 的 Owner GO，不是准备、离线测试，也不是旧 Run 的接续。**

## 一、运行身份与版本

**操作仓库**

- 仓库：`daowei2026/cgpterm`
- 分支：`fy/observation-iteration-agent-longrun-20261015`
- 采用提交：`86dec991abb27a927c1b5c22af1e51b3f39b918b`

**专业及运行仓库**

- 仓库：`daowei2026/observe-iterate`
- 分支：`fy/multisymbol-case-observation-20261027`
- 采用提交：`f7f2bffe9bcddd951d5bf218d56449e8f42999ae`

`work_id=BI-01`，`run_id=BI-01-CO-01`，从 `R0001` 开始。

本次运行成果提交到上述专业及运行仓库的指定分支，不另建分支。

## 二、完整任务来源与首次启动

完整业务目标采用专业仓当前版本中的：

`professional/case_observation/00_PURPOSE_AND_OUTPUTS.md`

具体专业方法、交付和数据工具要求，以同一版本的 `professional/case_observation/` 为准。

首先按现有 **M-START BOOTSTRAP** 机制建立新运行，保存本条真实 Owner GO，派发首次 Management Pro，由其根据完整目标和适用方法形成管理地图、当前任务、Binding 及后续专业安排。

完成真实管理采用后，按既有机制持续运行本次完整任务。

主控不代替 Management Pro 安排专业工作，也不自行理解、重编专业方法。

## 三、主控读取限制

首次只读取以下必要入口：

- `cgpterm/AGENTS.md`（如已自动加载，不重复）
- `cgpterm/.agents/skills/observation-iteration-longrun-controller/SKILL.md`
- `observe-iterate/runtime/overlay/08_自然语言运行提示_v0.3.md`
- `observe-iterate/runtime/config/COORDINATOR_DISPATCH.json`

进行首次管理启动时，才按需要定向读取：

`runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md`

以及其指向的首次采用必要内容。

其他业务正文由对应专业角色按实际职责读取。主控只需依据配置和实际任务，取得派发所需的准确来源及原文字节，不自行通读整个专业目录。

**禁止无明确任务需要而递归读取全仓、历史 runs、旧分支、runtime/release、无关专业 Source、全部 Skill、测试文件及实现源码。**

后续确有具体操作或故障需要时，只定向取得对应文件的必要部分。已经读取且版本未变的规则不重复读取。

## 四、Worker Codex

本次 Worker Codex 使用 Owner 指定的已有聊天：

- `threadId`：`01a17dd7-5033-7e63-b7a2-edd90b691c33`
- 预期聊天工作区：`/dwdhome/fy/cgpterm`

不另建 Worker 聊天，不自行改用其他聊天。

首次出现合法 Worker 技术工单时，核实该 `threadId` 对应的真实聊天及其工作区，确认无误后，按既有工程师派工机制向该聊天发送任务。

若聊天不存在、工作区不符或无法正常派工，新建一个聊天。

此目录是 Worker 聊天工作区，实际技术任务涉及的源码、数据和执行目录仍以具体工单为准。没有 Worker 技术任务时，不提前读取其历史或进行无关检查。

## 五、运行

完成首次管理采用和合法派发后，持续推进本次完整业务目标。

专业任务、Worker 派工、独立审查、GitHub 成果、回交、管理接收与后继处理，均按仓库已采用的正常机制执行。

不因完成一个局部步骤而主动停止，也不自行扩大 Owner 授权范围。
