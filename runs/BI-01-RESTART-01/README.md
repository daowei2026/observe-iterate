# BI-01 / RESTART-01 — 实际运行工作面

**R0001_M_START_RETURNED / MANAGEMENT_PUBLICATION_PENDING / WORKMAP_NOT_ADOPTED**。此运行已产生新 R0001 管理消息、唯一发送回执、完整原文及双 Return，不能再次执行首次 M-START。正式业务地图/当前任务、完整新专业 Binding 与管理 Intake 仍待真实物化和采用，尚未派发执行 Pro。最新已提交事实见 [PROGRESS.md](PROGRESS.md)，下一步沿 [R0001 恢复入口](../../runtime/operations/BI01_R0001_RECOVERY.md)；勿用本 README 的历史启动条款重置运行状态。

<a id="common"></a>
## 运行身份与历史隔离

- 唯一新运行空间为本目录；业务协调器固定 `work_id=BI-01`，但 `run_id=BI-01-RESTART-01`、所有新 invocation/token/marker、管理/执行 chat/thread 和 local long-task 身份必须重新建立且不继承旧账本。相同业务 work_id 不意味着旧试跑仍然活动。
- 旧业务仓 `complex-systems-vocabulary/.../observation-iteration-runs/BI-01-IT-01/` 是**已停止试跑的历史**，包括 10 月 13 日前三段、10 月 15 日第四段等 I4 结果/旧 G3 限定决定、旧轮次/聊天，全部**不继承**为新 run 的业务成果、当前任务、有效 Gate 或后继。Git 历史保留不等于接续。
- 可以从 `professional/source/00—07` 和实际设计/数据原件重新理解 I1–I3；是否从 I4 开始以及 G3 可消费范围由下一次管理 Pro 实际判断，不能预填已通过。
- 本次提交不是发消息授权，任何模型/手机业务行动需要之后的 Owner 明确开工和真实身份/来源/权限证据。

<a id="bi01"></a>
## 正式采用仍缺的文件

R0001 已收到完整管理原文，但以下文件应从原管理完整结果**保真物化并正式采用**，而不是照旧提交空模板或开始第二次 M-START：

- `00_长程推进地图.md`：由管理 Pro 对完整 I1–I6、Source/Method/Case/As-Of、已成/未成、Gate、反证和下一责任作真实业务关系解释。
- `01_当前任务.md`：由管理 Pro 签发本次当前专业任务、完整 scope、合法输入和 Gate/后继。
- `reviews/management-Rnnnn/`：管理 Pro 决定、真实接收/复看与签发证据；独立审查另列。
- `provenance/turns/Rnnnn/`：真实 Pro invocation 的 PROMPT、FULL_RESPONSE、身份、Return 和确证发送，R ≠ 手机 Episode。
- `artifacts/`：真实业务实物（有授权才包括 Worker 技术成果）。
- `PROGRESS.md`：操作端的 Owner 阅读投影；不能代替管理地图或 Gate。

准确流程：[BI-01 真实运行合同](../../runtime/operations/BI01_REAL_RUN_V1.md)；[轮次合同](../../runtime/operations/ROUND_RECORD_CONTRACT.md)。

唯一活动正本原则：开始后当前 map/task/管理回交/新 R 只在本工作面维护；旧业务仓内历史仍可读，但不再提供两个互相冲突的 CURRENT。
