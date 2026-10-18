# BI-01 V2-02：下一轮启动、业务与角色运行指南

## 1. 只准备，不发送

**PREPARED_NOT_STARTED / NO_SEND**。本分支准备下一轮 `run_id=BI-01-V2-02`（`work_id=BI-01` 不变）。旧 `BI-01-V2-01` 已按 Owner 要求暂停，原 R1–R10、R10 SUBMITTED、320图/包及旧管理接受均保留历史，未经 Owner 新授权不恢复旧M-CLOSE，也不借用旧GO、Binding、Gate或定时任务。

只有未来新的明确 Owner GO 才能把原文存到 `runs/BI-01-V2-02/OWNER_START.md`，准备新 `M-START` BOOTSTRAP、独立管理/专业聊天、调度 root 与 `BI01-V2-02-R0001-<unique>`。每轮原样发送和真实返回按 [轮次合同](V2_ROUND_RECORD_CONTRACT.md)，不凭文件/测试当实际发送。管理真正形成新地图、Task和Binding、合法读者/Workmap Intake后才能更新本分支 `runtime/config/WORKMAP_BINDING.json` 从 `NOT_CONFIGURED` 到 `ADOPTED` 并派发专业工作。旧 R0002 的具名首次读者授权不属于新 run；如要 reader 须有新管理真实签发。

## 2. 实质业务如何执行

[00 目标](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)与 [07 业务场景观察方法](../../professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md) 为本次方法重点；专业者先经 [06](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)实际阅读 U2/U3 Owner Decision、Narrative/Use Case（必要的 Witness/Method），**不是只看链接或字段清单**。理解 `DirectionalReleaseIntent` 下的共同方向机会、品种之间强弱和 U3 四方面为何需要，然后优先根据真实基础 K 线、Zig、贴近转折图选择有意义的市场位置；**具体类型、样本数、强弱阈值、研究顺序由执行过程据实形成，本指南不预设分类或赢家**。

S1：叙事到真实行情位置与为何值得研究；S2：先基础行情图和同源 CSV，再定向对照 U2 实际位置成员与 U3 四方面；S3：合法 As-Of 下成员的四束证据、可能强弱/无法判断、后续运动支持或反证、既有 C0/N/简单关联的增量和修订价值。三步可多 R 循环，但字段缺项、状态错误或工程数量不是主业务目标。必须实际观察至少有能力检验“共同方向机会中较强运动与成员差别”的场景；如果固定数据找不到，应给可追溯原因，而非制造优质机会或退化成无限局部检查。回顾性发现典型行情不自动证明提前选对；要检验辨别力须分开历史 Current 和未来 Outcome/探索显示范围。

## 3. 现有固定数据、图数和浏览器

两份预验算 ZIP 路径 `/dwdhome/fy/资金管理`、身份和不一致见 [05](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md)，原业务背景见 [04](../../professional/v2/04_BI01_BUSINESS_BASELINE.md)。aidata 工作区 `/dwdhome/fy/BASE_E6_2`。不默认重算 U2/U3、换数据或从 N 冒出正式 U3；广域 C0/N/C1 raw 只有参考机会入口，一个完整单尺度参考 Case 五As-Of、U3 R02 15行，R03 WITHHELD。这是四束充分性检验的实际证据边界。

技术图数可复用旧 `BI-01-V2-01` 锁定的源/窗口/图和对应 CSV，避免重新输出320图，但不能继承旧 S1 场景选择或已接受的业务判断。**Owner 实际能打开、看到K线/图层**才是图交付：旧图5785曾出现 `DataTable` 模型注册错误，已在 Trier 独立本地分支 `codex/bi01-v2-chart-render-fix-20261018`、提交 `adea9b46ce4016045eee714121f7a322924e14a3` 现场修复，核四张代表图，未证明全部320页及未来重启后仍正确；实际需要的页面按需核浏览器，不以 HTTP200/会话通过替代渲染。AI 本轮只读取同图结构化数据，不视觉看图片像素。aidata 尽量不改，确需通用改动只在新的 aidata 独立分支执行。

## 4. 专业成果与管理接收

把 **为何按叙事选这个场景—基础行情原图—U2 对照—U3 四方面在当时对成员强弱的分析—之后行情/合法Outcome—支持反证与缺口—相对 C0/N 的增量** 组织成 Owner 可直接点图核查的业务认识。专业 Pro 形成实际研究、管理 Pro 检查完整目标与阶段接收、Worker 只执行实际图数、操作端不替专业者挑场景。未产生完整 U3 时具体说明不够的证据，不能假称已验证充分性或自动补算。

## 5. 原有长程机制与备用路径

原 DR12/13/14、Overlay08/12/13、Workmap Gate、`ROLE_RETURN`/`QUESTION_WORK_RETURN`、M-START/M-REASSESS/M-CLOSE 与合法 Rnnnn 续作不变。基础环境和共享目录检查已确认，无须重新做同样预检。Pro 实际无法 GitHub 提交、且同轮远端无可信结果时，才从 MCP server `H:\fy\observe-iterate-share` → Codex `/dwdhome/fy/observe-iterate-share` 接收真实 ZIP，逐轮核 SHA、scope、完整 Return、安全路径并非 force 推送后 fresh readback；详细见轮次合同。不增加第二状态机。本分支离线检查不授权任何真实 send。
