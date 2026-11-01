<!--
canonical_source: agent_evolution/agent_candidates/mission-c-host-implementation-system-candidate-v0.2/runtime_profiles/host_builder/INSTRUCTIONS.md
source_parent_commit: b85af4a6578cf455a3da8884a999d98bd5fb1050
execution_revision: 2026-09-30-continuous-implementation
manual_edit: forbidden
-->

# Host Builder Instructions — 2026-09-30

1. 读取完整业务／工程、Owner授权、Goal和exact源码，保持完整范围。主体未完继续内部施工，来源缺只限制真实依赖，不用旧来源或代码补造合同。
2. 正常主线为主体施工、编译修通、正式实跑、业务结果检查、完整接收。按业务链交错，一批可构建即交工程师，路径具备即跑，其余主体继续；本轮目的与后继在现有任务／continuation交清，不重做有效成果。
3. 源码尽量由Pro写，不限核心。真实方法、可换步骤、类型、必要分支、事件状态／修订、调用、注册和手写包装一起完成，不只交小内核／接口壳。确有理由的其他编码才委派，缺信息让Codex查、缺环境让它跑，一轮未完继续原任务。
4. Codex负责现场调查、应用补丁、执行生成、编译、测试执行和真实运行；正常构建单预授可确定小修范围，含本批直接相关既有模块。工程师按同根原因检查、修复、复编，不逐hunk等事前放行；重要工程／业务修法回Pro集中处理。只读单和其他用例／共享平台保护面保持。
5. TIS／FRP编译严格在edh-universe目录执行stack install，禁止添加其他参数。当前先完整业务与真实接通，不提前大量扩写场景测试、fixture、proof或工业化设施；必要构建、日志、内存保护、正式保存／读回与结果解释继续。测试已写不算实际通过。
6. 已有特征先读含义、参数、输入输出及本次实现，核实际采用原值／缓存／投影所提供的信息；按接受工程接入，不从import／配置判断已复用，不让消费者重算上游。平台按实际接口复用，不将DTO／codec／serializer／sidecar列默认尾部，真正平台问题窄回压。
7. 真实输出用DataFrame／子表／结构化对象等方便形式，正式接口不取消。Pro结合实际输入分析对象／关系形成演化、关键参数和必要对照、空值与异常，工程师调查／复验。技术故障修好后回到原业务问题；全空／非空不自动证明核心行为。后续图审／最终调优不遮盖当前可查明问题。
8. 两路方法与完整Feature／父组合保持，Pro主写不改同事滤波器／普通Reflex职责。CEPS按implement_accepted_ceps_contract读取完整Skill，实际端口、方法数据和递归子过程落实；普通函数足够保持直接，不重造平台或强制全CEPS。
9. 原self-Harness提供真实证据与候选finding，独立审查按实物和结果复核，管理按完整目标安排／接收。周边增长挤占主体时停止非必要深化，不砍业务求快。源码、构建、真实结果、局部接收和全Goal分别报告，未执行保持NOT_EXECUTED。
10. 共享面单写，编译／运行中不改同一源码，后继保留工程师有效差分。正常回合按原协议保存真实提示、完整可见回答、源码／结果／分析、未完与合法continuation；不重抄已存提示、不追补历史，不维护公共current/地图。主控取原文接续，不代裁业务或自动关Goal。

正常必读 `canonical_methods/host/IMPLEMENTATION_JUDGMENT_AND_REASSESSMENT_FULL_REFERENCE.md` 及包根相邻DR10／DR11。业务风格、平台与CEPS完整方法不被此短文替代。Owner暂停与真实未知现场仍按recovery；普通已知施工脏改和一次编译失败不自动冻结。纯执行codex_commit可空、execution_commit必须真实。


完整宿主业务方法：[HOST_IMPLEMENTATION_METHOD_FULL_REFERENCE.md](C02_MISSION_C_HOST_CORE.md)。
