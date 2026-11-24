# Build Run 启动核验｜受阻，尚未注册派发

- run_id：`OI-EAW-P1-BUILD-STAT-20261124-01`
- work_id：`OI-EAW-P1-BUILD-STAT`
- business_case_id：`EAW-P1-BUILD`
- execution_profile：`CODEX_NATIVE_DIRECT`；post_start_owner_policy：`AUTONOMOUS`
- 核验时间：2026-11-24 14:41（Asia/Shanghai）
- 当前状态：`STARTUP_BLOCKED_RESOURCE_NOT_RELEASED`
- 本文件仅记录主控启动检查。没有正式 RUN_BINDING、Registry 登记、新 manager/executor、C/D/W、Feature 运行或业务验收。记录分支建立不代表 Run 已启动。

## 锁定来源

- 专业控制：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25`
- 唯一业务输入：同提交 `task-inputs/eaw-p1-build-stat-20261124/BUILD_RUN_INPUT.md`
- 主控 Skill：`daowei2026/cgpterm@815c505c1cc3d965aaafa831d23c4c88368cb70a:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md`
- TIS 基线：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74`
- 已读取准确 Native/base 主控 Skill、相关启动/资源/归档卡、业务输入、现行 L0 与 longrun README/协议。专业角色尚未创建或采用 Binding，不以主控读取材料代替 U。

## 启动检查事实

1. `/dwdhome/fy/BASE_E6_2` 存在，realpath 同值，当前账户具有读写和穿越权限。
2. 实际 TIS checkout 是 `/dwdhome/fy/BASE_E6_2/mquant/tis`；HEAD 等于上述基线，仍位于原 `codex/wall-output-consistency-20261121`。Build/Wall 的 assembler 与 core 文件逐字对应该 commit。未切换或修改原分支。
3. 存在预先留下的未提交修改 `frpExample/STCalendar.py`（29 行新增、15 行删除）。来源/运行影响尚未验实；已保留。它不在本 Run 的 Build 修改范围内，不能覆盖或擅自提交为本 Run 修复。
4. 旧 `OI-ABSORB-STAT-20261123-01` 的当前可信索引为 `OWNER_PAUSED`，资源为 `RESERVED_OWNER_PAUSED`。其原主控最新真实 Owner 消息为“先暂停上述所有任务。”，不是终止或释放。App Server 读回旧主控 Goal 为 paused；两条旧角色最近 turn 已 completed、队列为空且当前 notLoaded。本机定向进程检查无匹配任务进程，旧重型锁非阻塞探测为未持有。上述事实仅证明当前没有观察到旧任务执行，不构成未结束 Run 的工作区释放。
5. 已核现有远端 App Server 进程、启动身份、Unix listener/真实 peer 及本主控 thread。未新起或接管 App Server。其 model/list 含 `gpt-6.1-sol` 且支持 `max`。新 Build 角色尚未创建，故没有它们的 thread/start、cwd/model/effort 读回或实际 turn 证据。
6. App Server 对指定工作区的 config/read 返回 `sandbox_mode=danger-full-access`、`approvals_reviewer=auto_review`、`approval_policy=null`；此配置读取不等于已批准后续所有命令。当前主控权限环境为 danger-full-access / never；新角色的实际审批策略必须在合法创建后另行读回，不以 Owner GO 或默认配置推定。
7. 两仓连接返回 push 权限；本机对指定 TIS/运行记录新分支的 `git push --dry-run` 均成功。dry-run 未推送任何修改。本运行记录分支随后从专业控制锁定 commit 建立；仅写本启动检查。TIS 修改分支尚未创建。

## U / X / G / D 与 exact Wall

- U、X、G、D 均未开始。未签 D、未分配 C，也未启动其他 Feature Run；workers=[]。
- Wall 的源码基线可核对；本 Build 实例需要的相同参数/SOF/rb+m/2021 全年/Calendar 的 exact Wall artifact、receipt、state trace 及 Build 对上游的准确引用尚未验实或物化。
- 未运行 Build、未读回完整 build-default 参数、未取得正式市场结果，未形成任何 GlobalProfileGate / FeatureReleaseGate / UpstreamReleasePackage。
- 旧 WALL 合理性未全面通过的事实保持不变。技术源码存在不构成 Wall 合理性 Release。

## 阻断与下一合法动作

锁定 Native Skill §3.1 要求“工作区存在、realpath 与其他活跃 Run 不重叠”；其基础 Skill 的多 Run 操作卡 §3.3 进一步规定，与其他未结束 Run 相同或包含的路径“均不得使用”。旧 Absorb 仍为手动暂停且资源保留，不能被本 Build GO 自动终止、恢复或释放。

因此不发布有效 RUN_BINDING 或更新 Registry，不创建角色，不占用共享生产结果。恢复条件是取得有权且真实完成的旧 Absorb 资源释放记录（包括在途/UNKNOWN 与写者对账），或出现合法的新工作区绑定。在此之前保留 Build GO、输入指纹、检查证据和所有旧成果；不增加 Owner 业务审批节点，不把当前空闲解释成已结束，不启用轮询/自动唤醒。

资源条件满足后，按原启动顺序继续：核单写者及真实权限 → 正式 Binding/Registry → 新 manager（sol/max）与 C → 消费首个合法 D → 新 executor:E1（sol/max）与 C。专业角色依锁定原 Skill 推进 U→X→G，按 finding 进入 D。

## 主控归档与证据

Owner GO 从本主控真实 App Server thread/read 提取，原件 UTF-8 7047 bytes / 4303 字符，sha256：`62d9ee065050ddfc16c65e1715b5e795b48d15ea65c7678cf77c292a6c3c914b`。物理标识、完整原始回执、进程/配置证据和本地指纹仅保存在 gitignored controller artifacts。

主控可见文本已通过锁定归档器的 renderer 从本主控真实 thread 生成并本地保存；未找到已核实且位于获准归档分支的独立 Git checkout。按归档卡不擅建或切换其他 Run 的工作区，公开归档记 `ARCHIVE_NOT_COMPLETE`；该欠账与专业资源阻断分别保留。未归档 manager/executor Chat。
