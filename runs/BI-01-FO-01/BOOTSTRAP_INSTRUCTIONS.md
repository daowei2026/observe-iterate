# BI-01-FO-01 首次管理输入及运行接线

本文件是操作端对本次 Owner GO 与现有运行合同的定位，不能代替管理业务判断。Owner 完整原文为同目录 OWNER_START.md，新身份为 RUN_IDENTITY.json。

## 本次真实身份和成果位置

- work_id：BI-01；run_id：BI-01-FO-01。
- 仓库：daowei2026/observe-iterate；本轮写入分支：fy/bi01-feature-observation-prep-20261021。
- 专业方法源：4d501afa160179818a0563fc6d03656d1e879ded 的 professional/feature_observation/README.md 及其 00—04 全文。
- 本轮首先观察 U2NormalNodeBehaviorFrp。实际定义、实现、参数、输入输出和数据仍须按真实来源核定；四项工作可往返，不是四个固定 Gate。
- 真实成果根：runs/BI-01-FO-01/。每次真实 Pro 调用为 provenance/turns/Rnnnn/；手机 episode、Worker 操作、Git 提交不当作 Pro 轮。
- 首次管理接收者：chatgpt:细节叙事生成_金标:BI01-FO01-管理。新专业角色预留名称 BI01-FO01-执行；必要地图 Reader 预留名称 BI01-FO01-读图。预留名称不表示已创建、已派发或已获得角色授权，具体路线由真实管理 Binding 签发。

## 管理职责和交付接线

首次管理使用当前 DR13 的 M-START、DR06、DR08、DR14 和管理 Harness。管理须实际读取本次 Owner GO、当前专业方法和必要真实来源，然后签发本轮 00_长程推进地图.md、01_当前任务.md、reviews/management-R0001/ 中的决定与计划及实际专业 Binding。工作地图采用现有七个 anchors，任务使用实际 task_id，不能只交模板或把四项工作变成四阶段。

Workmap Binding 当前仍为 NOT_CONFIGURED。采用按 ADOPTION_HANDOFF_CHECKLIST.md、Overlay12 和 workmap_gate.py 的 snapshot/check/dispatch 执行；真实管理和适用 Reader 依据未形成之前，操作端不写成 ADOPTED，不派专业工作。若当前首次地图需要独立读图，须由本次管理具名签发实际 READER_TASK.md、#question-work-binding、#reader-pre-adoption/#adoption 和条件，不能继承旧运行的 Reader 例外。Reader task_id 与本轮前缀对应为 BI01-FO-01-WORKMAP-READER-01。

本轮专业 mode 为 FEATURE_OBSERVATION。专业判断、参数、展示、观察取舍和技术任务由有权角色形成；Worker Codex 在收到实际技术任务后才执行读取、制图与必要技术处理。实质成果和完整未完保留，真实观察后的管理复看和后继继续按现有 RESULT/CHANGE/EFFORT 机制安排。

## 当前已核环境事实及未核范围

操作 Skill 采用 cgpterm@1fb2f09f76df1fd25f55b6a249973ac00cef7480 的本仓版本；不因 CYF 参考分支覆盖当前配置。正式手机动作只能由每 episode 新建的零继承 executor 通过当前 MCP 执行。设备、控制权、调度状态及原始运输证据留在操作仓 gitignored artifacts。

本机跨仓工作区为 /dwdhome/fy/BASE_E6_2，aidata 位于 mquant/aidata。已读其 README，当前本机 aidata 为 f58ea95c358b9ac31659c92b7bc20fe9bf7f8264（codex/aidata-named-csv-features-20261019），工作树干净；这只是本机工具源事实，不等于本次 N 特征已接入或已制图。实际使用前由有权技术任务再核所用版本与接口。TIS/FRP 只读，未获额外写权不改源码；aidata 如需扩展按自身独立分支及真实授权施工，不在观察仓另建制图工具。

CYF 实际运行配置、OnlyRead 与管理接收来源由 professional/feature_observation/02_WORK_DETAILS.md 导航。旧 rb/i/hc 两个 ZIP 不是本轮唯一固定输入，旧完整 U2/U3 不是本轮默认任务。旧 V2-02 GO、Binding、地图、预算、Intake、R 轮和聊天均不继承。

## Gate 与回交

本轮 BI-01 Gate 每次显式使用 --run-id BI-01-FO-01。新运行路径、invocation 前缀 BI01-FO-01-Rnnnn-、首行 round_marker、原样 UTF-8 载荷及 exact Git 来源均需核验；不能用默认旧运行的检查结果代替。

真实发送前提交 INVOCATION.json/PROMPT.md 并核远端；真实回复后保存 FULL_RESPONSE、ROLE_RETURN、QUESTION_WORK_RETURN、实际实物与运输证据。管理业务决定及角色 Returns 必须来自真实 Pro，操作端只核、机械发布及接续，不填专业结论或签业务 Gate。GitHub 为优先回交，确不可写时按现有共享 ZIP 合同在本轮具名目录运输，再核真实原件与远端，不重复应用同轮 ZIP。
