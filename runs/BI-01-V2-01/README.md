# BI-01 V2：正式长程运行

<a id="common"></a>
## 运行身份
- work_id：`BI-01`（业务路由键）
- run_id：`BI-01-V2-01`
- status：**S1_ACCEPTED / S2_TECHNICAL_DELIVERY_COMPLETE / S3_FIRST_GROUNDED_FINDINGS_ACCEPTED_FULL_SCOPE_ACTIVE**
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

本次Owner已明确GO，原文见[OWNER_START.md](OWNER_START.md)。[完整地图](00_长程推进地图.md)和[原S1—S3任务](01_当前任务.md)继续有效，原专业任务/Binding未改。R3独立地图、首次Intake、R4专业S1、R5接收/定位适配及b60增量采用已实际完成；R6已消费部分同图数据，R7接受首次有据业务认识，详见[R7完整管理决定](provenance/turns/R0007/FULL_RESPONSE.md)。R7采用已经128586实际Intake并进入R8；R8原发送和一次同原稿恢复后无可取得正文/Return，不计有效结果，不倒改为取消或完成。[R9当前管理决定](provenance/turns/R0009/FULL_RESPONSE.md)停止R8运输恢复，签发原完整任务的新正常接续：按业务问题及时形成并保存实证正文，再连续补全所有重要问题，不等全部CSV穷尽才交实物。原聊天/模型/task/Binding不变，不增Worker或控制表。R6原IN_PROGRESS/INCOMPLETE及R8实际记录保留；本R9新Intake仍须按真实Git登记，不用状态标题冒充机械通过或完整业务完成。

[原图数最终回交](artifacts/worker-R0004/final/WORKER_RETURN.md)已技术完成，320节点/包保留；原47请求的51个AsOf有[可直接读取的原CSV文本](artifacts/worker-R0004/readable_views/REQUESTED_51_CURRENT/READING_GUIDE.md)。原Worker不重跑，R6运输停止条件已退出当前前置。专业者继续未完整覆盖的广域/未覆盖turn及主Case剩余层，完成四束、反证与增量分账，不以首批发现或图数结案。known行可能携带事后辅助字段，严格用途见[R7时间边界](provenance/turns/R0007/FULL_RESPONSE.md#time-boundary)。当前146CSV坐标修正版与旧144/146中间版各保留，内网页面与相应包版本配套。

## 轮次和已检查的运行前提

- V2 仍按 `BI01-V2-01-Rnnnn-<unique>` 记录每次实际管理/专业调用，S1/S2/S3 不等于固定三轮。
- Owner 已确认 `/dwdhome/fy/BASE_E6_2` 的 aidata 基础运行和 MCP H 盘 ↔ 操作 Codex 共享目录检查完成；这些不是需要再次安排的启动前工作。此前检查不能替代以后每次真实图、数据与 ZIP 的验收；本次真实 Owner GO 已记录；不得用此前检查代替新轮产物验收。

## 锁定版本和进度入口

- observe-iterate 启动基线：`11626f64bc64ae21e52108b2e47fafbbc1023615`。
- cgpterm 操作基线：`a65739e8adecfa1e6c09d97a11a1b020bf765126`。
- 两仓远端 `fy/observation-iteration-v2-20261017` 启动时均与 Owner 指定一致；后续运行增量不静默替换固定方法。
- [真实进度](PROGRESS.md)；[各R轮次](provenance/turns/)；[当前管理处置](provenance/turns/R0009/FULL_RESPONSE.md)。输入有效7份，R8两次发送不计结果；R9完整收到后才可能计8，原起点/间隔不变。达到8后的同范围复看与非阻塞接续按R9#effort真实登记，不预填消费、不提前关闭累计12。技术完成、实际读取、管理采用、独立资格和真实投递分别记录，不以文档存在代替发生。旧run的Gate、聊天和成果不继承。
