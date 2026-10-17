# BI-01 V2 全新长程运行指南（准备，不是发送授权）

## 0. 业务目标及本轮固定输入

完整业务意图：[00 总目标](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)。**不是“让 AI 多做几轮”，而是看既有 U2 机会簇位置是否合理、U3 四方面是否真的能辨别成员好不好做，并拿到具体不合理处、原因、反证及业务增量判断。**

本轮观察范围与数据不可任意重选：
- rb、i、hc；已提前验算的 `steel_U2_U3_执行结果_20261010.zip`；
- 上游 `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`。
- 必须先消费[04：原 I1–I3 业务起点](../../professional/v2/04_BI01_BUSINESS_BASELINE.md)与[05：固定数据位置和完整清单](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md)，而不是重新执行 I1–I3 或把它们的业务内容丢掉。
- **预先验算结果固定**：不派“先重新算一版 U2/U3”或“找到正式 Feature 就替换这批数据”的工作；实际发现字段、算法或哈希异常时准确说明影响、反馈并做必要的有界核对。
- U3 的“四方面”须按原业务定义和固定 CSV 已有输出对应；C2/H1 的 Shadow/未提交与 R03 Withheld 不能变成正式 Quality。

## 1. 当前身份和真实开工

`PREPARED_NOT_STARTED / NO_SEND`。本文件不授权手机或 Pro 发消息。只有 Owner **以后明确 GO**，才可建立 `runs/BI-01-V2-01/OWNER_START.md`、BOOTSTRAP 和角色调用。不能把本轮仓库修改当开工授权。

- `work_id=BI-01`（固定业务路由），`run_id=BI-01-V2-01`（全新身份）；新的管理/专业聊天、调度 root、invocation/token/marker/ledger。
- 开工时锁定 observe-iterate V2 和 cgpterm V2 各自的精确提交，核准本次机器工具；不用 moving main 代替已采用版本。
- 旧 run 的聊天、Gate、在途、Owner 回答、业务诊断不进入本轮；原 I1–I3 的业务信息通过 04/05 与来源文件消费，不算旧运行继承。

## 2. 首次真实开工步骤

1. 新 Owner GO 原文进入 `OWNER_START.md`，以此形成真实 `question-work/v2 BOOTSTRAP`；首次管理阶段可引用该次 Owner START 作 current_task_ref 与 task_adoption_ref，不伪造已存在的管理地图。
2. 使用 Overlay08/12 准备未经改写的完整载荷，首行唯一 `[BI01-V2-01-R0001-<unique>]`；按 `V2_ROUND_RECORD_CONTRACT.md` 保存、Git 远端读回、pre-dispatch 和实际 NOT_SENT 检查后才允许发送。
3. 管理 Pro 按完整目标、原 I1–I3 背景和固定数据签出实际 `00_长程推进地图.md`、`01_当前任务.md`、专业 Binding、管理接收和 Workmap Intake；有权生效前不得派专业工作。
4. 正式专业任务以 S1 整理观察问题、S2 对固定数据用 aidata 设计并实际画图、S3 以**同图数据**形成业务想法；必要时在不替换预计算数据的前提下返回 S2 补图。不可把单 Case 或制图完成视为整体完成。
5. Worker 在实际技术工单下以**只读固定数据、尽量不修改 aidata**为优先。先查 aidata 的 `OWNER_INTENT_AND_RATIONALE.md`、`README.md`、`TODO.md` 及现有 API。实在需修改 aidata，必须**新建 aidata 独立分支**；不能修改主分支/既有分支，也不在 observe-iterate 另造制图/取数系统。
6. 本轮不要求 AI 看图片像素；Owner 看实际图，AI 读图的对应原始/图层结构化数据。无法取得同源数据应如实反馈，但不能因无视觉模型而停工或新增视觉建设。

## 3. 机械与业务边界

- 通用 `ROLE_RETURN`、`QUESTION_WORK_RETURN`、Workmap/管理 Gate、手机 Skills 和 GitHub 记录机制保持原样，不建立第二套手机消息调度器。
- `runtime/config/WORKMAP_BINDING.json` 准备时必须是 `NOT_CONFIGURED`，实际管理签发、读回、intake 通过后才有权转为 ADOPTED。
- `runtime/tools/bi01_run_gate.py` 只能核身份、原样载荷、实物和 Return 关联，不证明业务正确、实际发送或专业结果完成。
- 没有真实图、实际取得的同源数据或 Owner 可审阅分析时，如实记录阻断/未完，不能声称已经完成 S2/S3。
