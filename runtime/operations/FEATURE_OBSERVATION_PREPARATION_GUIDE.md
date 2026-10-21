# 具体特征观察：准备到真实运行的衔接说明

**此文件仅说明衔接，不是 Owner 授权或启动提示词。** 不新建默认 run_id，不代管理签发工作地图，不预填 Intake 或 ADOPTED Binding。

## 1. 新的专业内容

- 专业目标：professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md。
- 基本输出：professional/feature_observation/01_OUTPUT_BASE_FORMAT.md。
- 工作细节：professional/feature_observation/02_WORK_DETAILS.md。
- 旧知识复用：professional/feature_observation/03_REUSE_FROM_V2.md。
- aidata 实际使用：professional/feature_observation/04_AIDATA_USE.md。

四项专业工作是可往返的业务活动，不按四个阶段依次签收。U2/U3 仅按当前具名特征需要读取。

## 2. 准备 3：修改后再审查

当前完成新方法文档与入口修改后，审查实际改动：
- 专业总目标、工作内容、成果表达是否一致；旧 S1–S3、固定 ZIP、完整 U2/U3 任务要求是否被误继承；
- 角色与 Router/Coordinator modes 是否仍为同一专业目标提供入口；是否错误地以旧 run 的 Owner GO、Binding、Workmap 或已接收成果替代新授权；
- 针对**实际选定特征和运行环境**，已知/高概率会使夜间执行无法推进的重要工具、取数、展示或交付依赖是否已有处理方案与必要验证；
- 发现确定问题则修正；当前没有依据的专业问题留给真实观察和后续迭代，不要求提前穷举。

## 3. 真正开始新长程运行时

1. Owner 另行明确新的 GO、任务范围和相应 run 身份；锁定专业仓、控制仓与实际特征实现/数据的版本与读取方式。
2. 按 runtime 既有协议建立真实管理任务/地图、具体特征与需要做的工作、准确 source_refs、Binding/Intake、角色接收者与后继；不能使用旧 BI-01-V2-02 的已采用配置。
3. 管理 Pro 按四项可往返专业工作安排，而不是使用旧 S1/S2/S3 的强制划分；Worker 根据有权技术工单实际使用 aidata。
4. 操作端在真实身份、准确 payload、前置条件和 Gate 成立后才发送，保存真实回交并依法续作。未满足条件时反馈准确缺项，不能自签 Owner GO。
5. 现有手机操作、Workmap、QUESTION_WORK_RETURN、ROLE_RETURN、Git 提交及备用运输能力优先沿用既有通用机制；本文件不重建平台。

新任务的非活动模板位于 [feature_observation/templates/](feature_observation/templates/)；必须在新 Owner GO 后填成具名的新 run、实际特征、管理地图、当前任务、Binding 与 Intake，模板中 `<NEW_RUN_ID>` 不能用于真实派发。`BI01_V2_RUN_GUIDE.md` 与 `runtime/operations/v2/templates/` 保存的原 V2-02 具体运行内容只作历史参考，不能沿用旧专业职责、数据或已采用资格。
