# 执行修订的来源、连续性与验证边界

current_revision: `2026-09-14-management-repair`
repo_parent: `28c6f11dd961f5aca4da7aa5fb44812fa30f1510`

本次Owner要求按已讨论的方法修改agent_candidates并提交；最后明确纠正不能强制管理者找两种解释或制造通用工程形式主义。上次thinking失败没有可核实新成果，本次从fresh main继续。保留同日已提交的共享平台参考，不修改具体用例合同、推进状态或实施仓。

## 0. 已保留的2026-09-14平台工程参考包

规范源位于 `agent_evolution/platform_engineering_references/feature-platform-engineering-reference-pack-candidate-v0.1.0/`，材料类别为 `FIXED_COLD_PLATFORM_ENGINEERING_REFERENCE`。`REFERENCE_MANIFEST.yaml` 固定package id、reference id、字节数、SHA-256、上游路径、上游身份及导入时工作树状态；`SHA256SUMS.txt` 用于逐文件机械复验。Mission B只负责按任务相关性选择reference id并把package id、reference id及SHA-256写入工程包，Mission C、特征生产适配器和组合运行时消费同一锁，不各自维护文字副本。

本次导入的Python／Numba侧来源为 `mquant/docs/agent-workflow/pre-L0/03A`、`03B`、`03C` 与 `07` 四份文档；其中03A、03B在来源Git提交 `f2972195eec5f51b0b2425856a8917b094333a7e` 上为tracked clean，03C为该提交之上的tracked modified工作树快照，07为未跟踪工作树文件。FRP侧四份来源位于 `edh-universe/docs/ssot/frp/`，导入时无法发现其所属Git根，因此明确记为filesystem snapshot。不得把后两类来源误写成已提交、clean或可由提交号独立还原。

本包只提供稳定的平台工程约束与设计检查，不取得当前业务should-be、当前API、真实caller、构建图或运行事实的权威地位。每次Mission B分析及Mission C实现仍须现场解析live RepoFact；发现平台参考与当前代码漂移时，应显式记录冲突与风险，不得静默按参考包猜测。组合运行时保留一棵完整字节投影和面向Project上传的core／optional扁平投影，映射由 `PLATFORM_ENGINEERING_PROJECTION_MAP.yaml` 固定；所有语义修改先改规范源再重建投影。

## 0.1 本次管理、专业方法与执行修订

重点为业务轻重缓急与真实讨论价值、连贯批次和明确首版、适时调用管理及Owner校准、A/B完整方法使用、任务本身的盲点与防丢、实际投递与机械接收成本。具体来源和每项落点见仓库根路径 `agent_evolution/agent_candidates/refinement_wave_reports/20260914_management_repair/DELIVERY_AND_COVERAGE.md`。

DR06改实际判断方法，DR08改调用和派发，DR02补选择—细化—回装及工程义务保真；A的RUNTIME/CURRENT、B的CURRENT和Overlay绑定接回完整专业方法；新增MANAGEMENT_METHOD_HARNESS是触发型检查，不是新常驻角色或固定任务表。撤回强制两种理解／多方案、把细节逐个独占回合、任意返修全停、快速恢复便不补Skill/Harness等误推。

workmap_gate保留v1并增加显式v2；阅读输入不含阅读报告，兄弟线普通说明隔离但共同Owner／方法仍受监测。execution_handoff原样准备任务、核载荷、汇总真实管理信号并去重，不自行发送或判业务。未自动迁移用例绑定，不更改已签发任务、shared intake或阶段门。

本次不做全面历史法证或EAW重抽，不只修改已知用例错误。已有明确重要方法或Harness缺口直接补本次规范源及运行入口；未知高成本假设留后续真实运行。正反机械回归与人工正文自查如实记录，不冒充fresh Pro行为测试或本机部署。

此前2026-09-12的地图修订仍保留其来源和有效要求，以下记录属于当时成果，不因本次文档更新复活旧资格。

## 1. 本次直接来源与最终纠正

Owner附件 `U2和U3任务说清楚安排和进度.md`，128945bytes，SHA-256 `a69ff32adbb1fa36abd2258540aa789f83e9b1dae4fd7b6fccaf06ec3b54a79f`。原附件完整字节在本次下载交付的 `20260912_OWNER_DISCUSSION.zip` 中保留，二进制原件未写入本仓。仓库根相对路径 `agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/provenance/20260912_OWNER_INTENT_AND_CHANGE_COVERAGE.md` 保存五轮原始Owner提示、原件hash、行号及逐项落点。当前本轮提示和完整交付回答另外入库；普通运行不以取得全部历史回答为前提。

2026-09-12 10:18要完整U2/U3安排与进展；11:05指出地图已有义务但实际退化；13:26要求工作量、实物引用、后续实施和真实运行；14:08纠正十多轮只是审查顺利情形预期、不可预排子任务次数、重要意图词要解释，并质疑纯文字约束；14:37最终澄清分路是滤波器体系／普通Reflex与CEPS等复杂表达，以及普通执行者只交实物、管理／审查维护图。当前本轮明确授权将这些实际写回。

不采用早期回答的2/3/4轮预算表、不采用单次计算／持续状态二分、不继续要求业务Builder维护推进图或下一任务。保留完整工作、条件性预期、真实证据、管理维护与可检验失败处理的分析细节；不把被纠正回答反向晋升Owner意图。

## 2. 义务与实际落点

DR01原位说明表达分路，不按状态／数据频率分类。DR02保留A/B递归方法、参数、控制器、事件和状态的完整深度。DR03/DR07分清正式委派、接入、借用、执行者与代码仓，明确Codex源码按Pro任务。DR04继续要求真实工程设计与接收。DR05保留组合链、关键主体和真实反馈被消费。DR06/DR08落实管理端维护、普通执行者交实物、当前问题接续与失败返回。

Overlay09恢复完整阅读面、意义、条件性投入和版本连续性；10分别处理业务审查与新读者检验；11按角色保存实物、接收和运行；12连到实际workmap_gate及Git回归测试。00/01/03/04/05/07/08/CURRENT与A/B/C CURRENT同步去除旧职责。公共pilot README承担共同意图／阶段／预期，子推进图展开各线真实成果／依赖／当前问题；两份当前任务只改交付责任，不改业务验收。

## 3. 保留的2026-09-10形成依据

前次组合发布parent为 `80ab154cc55fb85133e000e4de8f04a7f24bbb18`，前读基线 `761c2c1932253230fe811d5aabf843521200dc84`。其来源附件 `初步抽出的agent试跑的产物评估讨论-202609100210.md`，1058592bytes，SHA-256 `21ff85ce80a62a5bb317631ed2e32dc9ef1740745e1f8a7e915fa10dc29334ee`。

该次Owner依据仍保留：09-08 19:39的Pro自存本轮、不补历史、实物去重；09-09 13:36的分工／管理接缝；09-10 10:46的方法／事件／规模区别和四种粒度；12:54的A/B细度、递归方法及接收转换；13:21的软件Agent委派而非本人、完整特征及三种使用身份；13:41的工程主体、不得转嫁设计欠账和组合跟到实际完成。最新09-12纠正只改同一问题的定义和职责，不删除这些仍有效方法。

学习同事Binder的收取、状态呈现、检查和派发经验，实际作为本次附件中的已读分析来源使用。没有把其内部epoch、固定节点、shell/目录、阈值或分支特例复制成通用规则，也不声称本次再次审计其全部live实现。其“规则改变未触发、检查漏执行、有检查无修复”的反例，转成这里的rule/Owner fingerprint、真实派发前置和具名失败任务。

## 4. 规范源、投影与既有成果

原A/B/C完整专业reference未clean-room重写；Overlay活跃执行成员在原路径修订。当前清单按新字节核对，历史原seal留在Git而不误称继续证明已改成员。本组DR以规范源为准，向runtime和project_upload生成同一blob；RELEASE_SET登记新组合和未改原组件的边界。

用例已形成的业务结果、审查、原H1、缺口和代码候选保留；推进图资格可解释地降级，不抹掉实物和实际投入。没有用本次管理任务裁BC32/F01–F03或重新激活任何真实业务阶段。

## 5. 检查能证明什么

工具测试是真实临时Git仓上的机械回归，检查input/rule/Owner变化、范围、引用、投入、角色越界和派发现场；不证明自然语言含义、fresh独立性或运行证据真实性。重要地图变化仍需新读者复述与source对照。

当前可运行CLI与执行端接入说明已提供，但本地routine实际加载／失败转管理／成功投递、一次真实后续地图维护尚需现场执行。不得将规则提交、测试数量、静态检查或候选文档自动晋级为自治维护已验证、业务完成或production。
