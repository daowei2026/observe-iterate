# BI-01 V2 全新真实长程运行入口（未启动）

## 状态与授权
`PREPARED_NOT_STARTED / NO_SEND`。本文件为 V2 接线说明，不是 Owner 的实际开工指令。只有未来真实 Owner GO 才能建立 `runs/BI-01-V2-01/OWNER_START.md`、BOOTSTRAP 和角色调用。不得拿本次“改版”指令代替开工授权。

版本：当前 V2 精确 Git commit（实际开工时再锁）；`work_id=BI-01`，`run_id=BI-01-V2-01`。新管理聊天、新专业聊天、新本地长任务 root、新 round/token/marker。旧 `BI-01-RESTART-01` 的聊天、Gate、在途、Return、成果均不继续、不重放、不转为新 run 任务完成。

## 工作来源
- 当前专业目的：`professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md`
- aidata S2：`professional/v2/01_AIDATA_CHART_AND_DATA.md`
- 观察想法 S3：`professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md`
- 工程/角色交接：`professional/v2/03_EXECUTION_HANDOFF.md`
- 任务按真实业务优先选择 S1/S2/S3（无 I1–I6 的活动业务枚举）。
- 无权自动改变 U2/U3 正式业务定义，四方面的确切内容须由实际可靠业务 Source 取得。

## 首次真实开工
1. 锁定仓库 V2 精确 commit 和 cgpterm V2 控制器，核对现场真实可用的通用手机/定时/运输技能；不从 moving main 猜版本。
2. 实际保存未来 Owner GO 原文和准确来源到本 run OWNER_START.md；再创建实际 `question-work/v2 BOOTSTRAP`。管理首次 BOOTSTRAP 可引用真实 Owner START 作 current task/task adoption，不能预造管理地图。
3. 通过现有 Overlay08/12 生成精确 payload，唯一首行标记 `[BI01-V2-01-R0001-<unique>]`；按 `runtime/operations/V2_ROUND_RECORD_CONTRACT.md` 持久化，远端读回并检查实时 NOT_SENT 后发送。
4. 管理 Pro 首次有权工作建立真实 `00_长程推进地图.md`、`01_当前任务.md`、专业 Binding、管理接收及 Workmap Intake。发布和远端读取成立之前，不得发第一条专业任务。
5. 第一次专业任务按 S1 总目标和必要 S2 入口授权。业务上可连续推进 S2、S3 并返回 S2 补图，不要求每次为小修复重新签管理任务。重大证据缺口、Owner 取舍、实质里程碑才触发管理复看。
6. Worker 仅在专业 Pro 的实际授权工单下运行 aidata。环境/数据缺项时记录具体阻断；通用工具新增只能改 aidata。S2 要交真实可打开的图和同源数据；S3 要交可以让 Owner 按图核验的业务认识。

## 机械边界
- 使用旧项目已测试的工作流、workmap、question-work/v2、longrun-return/v1 和通用 phone Skills；不复制新手机轮询/网络状态机。
- `runtime/config/WORKMAP_BINDING.json` 在准备版保持 `NOT_CONFIGURED`，不得凭预备模板将其设为 ADOPTED；新 run 首次管理签发并校验 intake 才能采用。
- `runtime/tools/bi01_run_gate.py` 只核新 run 的原样发送/结果关联，不批准业务、发送或 GATE。
- 当前 V2 分支只以本启动指南、V2 轮次合同和经真实管理签发的任务为运行依据。
