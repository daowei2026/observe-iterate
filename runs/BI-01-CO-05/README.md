# BI-01-CO-05：Owner 初版用例形成过程的真实实践

<a id="common"></a>
## 共同状态

- **Run**：`BI-01-CO-05`
- **Work**：`BI-01`
- **当前专业 mode**：`CASE_OBSERVATION`
- **当前状态**：R0008 已形成 Owner 指定全段图数脚本和正式工单；Worker 已真实执行一次，但在 actual core/run 创建前读取必需日历配置时发生单次 NFS `OSError(errno=5)`，未生成图页或正式切片。R0009 已消费该失败并触发投入复看；R0010 已有限接收技术成果、关闭原工单并授权一次性条件重入。
- **有权分支**：`fy/owner-led-case-exploration-optional-reader-20261102`
- **Owner GO**：[OWNER_START.md](OWNER_START.md)
- **Owner 全段时间纠正**：[OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md](OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md)
- **最终投资目的**：[00_BUSINESS_OBJECTIVE.md](../../professional/exploration/00_BUSINESS_OBJECTIVE.md)
- **当前探索直接目标**：[06_EXPLORATION_STAGE_GOAL.md](../../professional/exploration/06_EXPLORATION_STAGE_GOAL.md)
- **Owner 完整初版过程**：[05_OWNER_PROCESS_EXPLANATION.md](../../professional/exploration/05_OWNER_PROCESS_EXPLANATION.md)

本 Run 不继承 CO-01—CO-04 的任务、地图、Reader、预算、在途、Gate 或业务结论。当前业务目标仍是用真实特征与连续市场过程实践并迭代 Owner 的初版用例形成方式，不是证明旧图、旧参数、技术脚本或单一 Case 正确。

<a id="bi01"></a>
## BI-01 当前入口

### 当前业务关系

`Owner 初版过程与当前问题 → 同身份全段图/正式数据 → 证据资格核对 → 沿当时可知信息观察大尺度背景形成/改变 → 检查中尺度结构 → 形成并更新具体用例/前瞻判断 → 管理接收与方法反馈 → Owner 校准或下一轮专业实践`

### 当前已成

1. R0002 完成 fail-closed 输入资格：没有正式同身份图数时，不制造市场背景、候选或无候选；合格 market T 为 0。
2. R0006 采用 Owner 全段纠正并停止旧 45 天工单。
3. R0008 固定 `rb/hc/i`、30m、large+mid、small 关闭、`GTQH_L1_20210104_20240229 / gtqh_four`、主范围 `[2021-01-04 00:00:00, 2024-03-01 00:00:00)`、一张全段主图、七张先验辅助图及同 run/core 图—正式数据链；脚本 SHA-256 为 `5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`。
4. Worker 按 R0008 工单实际执行一次。原脚本字节匹配、无兼容 diff；在读取 `/m3varI/var/L1_data/sof/unit/affiliated_calendar_no_night.csv` 时发生一次 `OSError(errno=5)`，失败早于 actual core/run、页面和 board。
5. R0009 已把该结果裁定为执行环境 I/O 阻断，而非市场、特征或方法结论；R0010 已消费本段 EFFORT，关闭原 R0008 工单并授权一次性条件重入。

### 当前未成

尚未取得 actual run/core、可打开全段主图、七张辅助图、正式 KLine/large/mid 切片、manifest/FILE_INDEX、实际覆盖与字段语义；没有合格 market T、第一层连续市场过程、中尺度用例、候选/排序/合法无候选、自然挑战或对 Owner 过程的业务有效性结论。首个过程实践包未被接收。

### 当前正式工作面

- [长程推进地图](00_长程推进地图.md)
- [当前正式专业任务](01_当前任务.md)
- [R0010 阶段接收与条件重入决定](reviews/management-R0010/DECISION.md)
- [当前 Workmap Intake](reviews/WORKMAP_INTAKE_CURRENT.json)
- [运行采用状态](../../runtime/config/ADOPTION_STATUS.md)

### 下一实际动作

协调者在同一 exact commit 上核当前 Intake 与 unchanged formal task，运行 routine Professional dispatch preflight；通过后向 `chatgpt:BI-01-CO-05:professional` 发送完整任务与 R0010 决定。原 Professional 只需签发一个新 order：同一 Worker、workspace、解释器与权限身份先真实 `open/read` 精确日历文件；探针通过就在同一执行中从头运行 R0008 原全段脚本一次，探针失败则在昂贵运行前停止。R0008 原工单不得重派。

Worker 结果回原 Professional。技术成功时，Professional 必须在消费结果的同一调用内完成证据资格核对并从第一条合格 as-of T 开始第一层观察；同路径探针再次失败时不得签第三单，回 Management 决定终止当前 Case 或提出有权输入变化。

### 当前不能声称

本入口不证明日历文件已经恢复、条件重入工单已形成或派发、Worker 已再次执行、图数已取得、字段语义已核、共同背景或中尺度结构存在、候选规律成立、市场无候选、Owner 初版过程有效、独立业务审查通过，或当前探索阶段完成。
