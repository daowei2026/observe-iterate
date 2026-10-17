# BI-01 V2：正式长程运行

<a id="common"></a>
## 运行身份
- work_id：`BI-01`（业务路由键）
- run_id：`BI-01-V2-01`
- status：**R0001_MANAGEMENT_PLAN_ISSUED / INITIAL_WORKMAP_ADOPTION_PENDING**
- 业务总目标：[V2 00](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)
- 重要既有业务底稿：[V2 04](../../professional/v2/04_BI01_BUSINESS_BASELINE.md)（复用 I1/I2/I3 的业务事实，不复用旧 run 状态）
- 固定数据与位置：[V2 05](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md)
- U2/U3 叙事与细节设计：[V2 06 来源导航](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)

<a id="bi01"></a>
## 本轮不再选择数据或重新验算

固定对象 `rb/i/hc`，输入为已提前验算、位于 **`/dwdhome/fy/资金管理`** 的两份 ZIP：
- `steel_U2_U3_执行结果_20261010.zip`；
- `rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`。

先检查 U2 共同机会簇的实际位置/边界，再检验这些位置 U3 四方面对品种好不好做的辨别效果。S2 **优先用现有 aidata** 对固定数据画图并取得对应数据，S3 专业 Pro 读同源数据形成业务认识；图交 Owner。**现阶段不让 AI 视觉看图，不因缺少视觉工具要求改造 aidata。** 发现数据具名疑问时核查/反馈，不暗中重新生产或替换。

aidata 任何必要的通用修改都须在其新建的工作分支施工，不修改当前分支，不在本仓建第二套画图工具。

## 运行资格

本次 Owner 已明确 GO，原文见 [OWNER_START.md](OWNER_START.md)。R0001 管理已经形成[完整推进地图](00_长程推进地图.md)、[当前 S1—S3 专业任务](01_当前任务.md)和[实质采用/处置决定](reviews/management-R0001/DECISION.md)。首次独立地图读者、Workmap Intake 和专业实际首发仍需真实完成；此状态不代表图或业务认识已生成。旧 run 的 Gate、聊天和成果绝不继承。

## 轮次和已检查的运行前提

- V2 仍按 `BI01-V2-01-Rnnnn-<unique>` 记录每次实际管理/专业调用，S1/S2/S3 不等于固定三轮。
- Owner 已确认 `/dwdhome/fy/BASE_E6_2` 的 aidata 基础运行和 MCP H 盘 ↔ 操作 Codex 共享目录检查完成；这些不是需要再次安排的启动前工作。此前检查不能替代以后每次真实图、数据与 ZIP 的验收；本次真实 Owner GO 已记录；不得用此前检查代替新轮产物验收。

## 锁定版本和进度入口

- observe-iterate 启动基线：`11626f64bc64ae21e52108b2e47fafbbc1023615`。
- cgpterm 操作基线：`a65739e8adecfa1e6c09d97a11a1b020bf765126`。
- 两仓远端 `fy/observation-iteration-v2-20261017` 启动时均与 Owner 指定一致；后续运行增量不静默替换固定方法。
- [真实进度](PROGRESS.md)；[各 R 轮次](provenance/turns/)。管理地图、当前任务及 `reviews/` 的签发已经形成；接收、Intake 与实际投递按真实后继记录，不以文档存在代替发生。
