# 多品种用例研究：准备到实际运行

本文件负责本批运行接线，不另定义专业方法，不是 Owner GO。完整业务要求见 [专业入口](../../professional/case_observation/README.md)。

## 1. 仓库、环境与来源

| 对象 | 本次位置/职责 |
| --- | --- |
| 操作仓 | `daowei2026/cgpterm@fy/observation-iteration-agent-longrun-20261015`，原分支修改 controller |
| 专业及运行仓 | `daowei2026/observe-iterate@fy/multisymbol-case-observation-20261027`，本次新分支 |
| aidata 工作区 | `/dwdhome/fy/BASE_E6_2`，不是代码写权或数据版本 |
| 专业方法 | `professional/case_observation/`，以采用的 exact commit 为准 |
| 当前派发配置 | `runtime/config/COORDINATOR_DISPATCH.json`，稳定 work_id 为 BI-01 |

正式启动分别锁定两仓实际完成提交、现场工具/数据版本。不能从分支名推导 GO，不能把旧 fixed ZIP 或旧 N 特征作为本批默认输入。无需因换专业方法重装通用手机、连接、恢复、计时和调度机制。

## 2. 必要工具准备

消费 Codex 对两种 aidata 方式的真实验证：只有 1d 图和数据；1d 概览 + 选定窗口的 30min 大尺度图和数据。后者以行情和贴近转折为起点，Owner 查看需一个含全部图的平台页面。输入和调用说明见 [aidata 专业说明](../../professional/case_observation/03_AIDATA_USE.md)。

已存在且适用的验证直接复用，不重复基础环境预检；只有源码推断的不算实测。图暂缺时可以保留可靠数据上的研究，整批平台交付仍如实标未完，不以独立 URL 清单或 PNG 替代。

本次修改没有现场执行上述验证，也不授予工具仓/共享服务修改权限。确有缺口时由有权 Pro 按已知完整目标签具体技术工作，Worker 结果回原签发 Pro，不另建调度。

## 3. 旧运行与新运行隔离

本分支的 `runs/` 只保存新任务资料，旧 `BI-01-FO-01/` 与历史索引已移除；需要时从[运行索引中的旧分支及准确版本](../../runs/README.md)定向读取。原采用配置、专业方法和旧运行在 `9badfa6f30caebbe3156c5e4ee4deb43d22cacb5` 可完整取得。本新分支的默认 Workmap 是非活动准备状态，不继承旧等待、预算、轮次、Owner GO 或接收。

本次不替 Owner 宣告旧 run 已停止或完成。启动前核真实在途；若仍有有效旧操作，按原授权处理，不能通过清状态或切分支掩盖。新 run 用独立目录、聊天定位、token/marker、scheduler root 与任务。稳定 BI-01 work_id 不表示同一实际 run。

## 4. 有了真实 GO 后的接线

记录实际 Owner 启动原件及允许范围，确定真实 run_id，使用已有 M-START BOOTSTRAP。管理依据完整目标形成地图、任务、Binding 和适用接收；[通用模板](templates/)只提供结构，不预填业务完成或授权。

按 [ADOPTION_HANDOFF_CHECKLIST.md](ADOPTION_HANDOFF_CHECKLIST.md) 采用真实结果；沿既有 `ROLE_RETURN`/`QUESTION_WORK_RETURN`、GitHub 全文与手机短指引交付。轮次/ZIP 合同仍在 [V2_ROUND_RECORD_CONTRACT.md](V2_ROUND_RECORD_CONTRACT.md)，文件名兼容旧引用，正文已不固定历史 run 或专业阶段。

所有 `runtime/tools/bi01_run_gate.py` 调用显式给 `--run-id`；使用非默认 Binding 时也给 `--binding`。`workmap_gate.py` 的 snapshot/check/dispatch 同样用该 Binding，不能一个检查新 run、另一个读旧全局配置。

cgpterm 的 `sync-chatgpt-project-skills.sh` 默认五个 Skill 不包括观察 controller；确认现场直接读取本次 checkout 或已定向同步该目录，记录真实版本。提交不等于安装、发送或业务成功。

## 5. 本批正常执行与结束边界

完整任务一次覆盖 3–5 个用例，每例有位置和回看研究。方法由专业者自主选择，不把每个内部步骤拆成 R 或强制 Gate。没有依赖的工作可并行，实际接收义务依真实任务。

管理最终将真实批次入口交 Owner 一次性查看，正常反馈通过已有 CHANGE/任务修订路径返回；不新增固定反馈阶段或逐例人工批准。交齐本批不授权无限新批次或正式特征开发，后继由真实安排确定。无法完成的内容保留实物和具体未完，不伪造完整接收。
