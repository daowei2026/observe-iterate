# 同事特征生产 Agent：外部 A/B 接收绑定与执行入口

binding_id: `AB_DIRECT_FEATURE_ADAPTER`
revision: `2026-09-29-pro-code-real-data-first`
status: `candidate_not_behaviorally_validated`

本文件可直接指定给获授权的Pro／执行端作为接收和实现角色；复用同事专业方法，不修改其仓库、原runner、handoff validator或team。采用本接入模式不冒充原版完整team的PASS。同事Agent是软件角色，不是同事本人。

## 1. exact外部来源与读取

上游为 `daowei2026/feature-production-agent`，构建时分支 `codex/m3-implementation-runtime-integrated`，基线 `4c85d1dc42df6398572f29e383967767e1322509`。这是此前实际读取的绑定基线，不是本轮声称外仓live已再验证。

每次首次采用先查该分支live，漂移记录old/new后选择受支持exact版本，不静默换规则。定向读该ref的：

- README.md：角色及完整／部分使用；
- `需求细化/agents/ResponsibilityBlockLogicStructuringAgent/harness.md`、`workflow.md`：完整业务值／函数逻辑／事件／采样；
- `需求细化到实现接口/agents/ImplementationPreparationAgent/harness.md`：原版归档、唯一事实和三份输入；
- `实现/agents/HaskellFeatImplAgent/harness.md`、`workflow.md`：Fao、真实doImpl、具名业务函数、中间Occ、注册和编译；
- 使用Python／验收／集成角色前，从同ref README/team路由取得实际harness/workflow，不猜名称和能力。

该基线原版Haskell要求完整顶层Feature、已归档需求和准备输入；Haskell角色本身不读运行实例，原版准备阶段要求feature_run_instance。准备不是B设计，Git集成不是业务接线和最终验收；这些事实不能无核对地外推未来版本。

若本任务涉及 Python／Numba、跨语言或 Haskell／FRP 宿主约束，同时读取当前 B 任务锁定的 `agent_evolution/platform_engineering_references/feature-platform-engineering-reference-pack-candidate-v0.1.0/00_REFERENCE_ROUTER.md` 与命中正文。该共享包不属于同事 Agent 或 Mission C 私有；本接入不得复制后改成自己的平台规则。

## 2. 原版与本接入版

**原版入口。** 原冻结档案、entry/task_key/feature_version_id、正式handoff、实现绑定、观察信息、输入特征及编译条件真实满足时按原角色运行。原版Owner归档遵循实际授权，不编造历史Agent已跑；完整team发布和集成另有明确范围与写权。

**AB_DIRECT_FEATURE_ADAPTER。** 负责人明确选择后，由当前Pro／执行端按本文件消费外部A/B输入，不调用entry_only runner伪装其ARCHIVED检查已通过。若要接入软件runner，实际修改适配入口并验证，不能靠本文声称部署。

接收的是一个业务上独立、边界清楚、B已设计好工程落点、可用滤波器体系和普通Reflex完整表达的Feature。普通Reflex可有事件／持续状态／采样；不因有状态就拒收为CEPS路线。内部helper、任意CEPS子图不是本版独立交付，它们可在父任务内借用方法；不把整个复杂用例塞成一个Fao，也不为分派而新造公共Feature。

## 3. 输入按实质组织

负责人／Compiler在既有任务目录提供一个冻结接收入口，先写设计与要交回的成果，再附必要身份。必须能完整读取：

1. 当前局部A：特征正面意义、完整方法树和可换步骤、类型／输入／输出、事件／状态／时间／回看／修订、合法空和有限结果、正式消费者。
2. 当前局部B：函数和处理器、真实接口及计划新增上游、方法构造调用、状态、模块／注册、存储／读回、组合责任、验证和allowed writes。
3. implementation_binding：真实工程身份及B新设计来源，不伪装成仓库已有。
4. verification_observation：真正业务链的中间事件，不新加业务判断／公共产品。
5. exact基线、外部Agent版本、原版／接入／借用身份、`platform_reference_lock`、Pro/Codex实际执行者、源码和运行授权、返回位置及组合者。

可把完整A/B投影到接收方熟悉的边界／责任块／内部逻辑文件，也可强制读取完整exact引用；每个映射指向实际源段，不只有摘要和文件名，不能产生两份分别手改的业务真源。原实现绑定／观察信息结构继续复用，不为管理重建业务schema。

必要身份示例只作实例化辅助：`receiver_mode=AB_DIRECT_FEATURE_ADAPTER`、`binding_revision=2026-09-29-pro-code-real-data-first`、`scope_kind=complete_direct_reflex_feature`、真实accepted_input_ref/business_body/engineering_body/implementation_binding/verification_observation/platform_reference_lock/executor_and_write_authority/return_location。占位未填不得由接收者猜。

B未作完的工程决定由B继续完成，不能变成永久外部前提。方法路线与代码仓分开，使用同事方法不等于把业务代码写入其Agent材料仓。

## 4. 对原版作出的明确调整

输入来源用真实冻结外部A/B与接纳记录，代替“原三位需求Agent均已PASS”的历史条件；不伪造原handoff。元数据导入可机械执行，内容接纳仍需本任务授权与实际证据。

读取面必须包含完整B，不能因implementation_binding只存名称而遗失工程决定；业务与工程决定各标来源。归档可以用生成的接收视图与本模式接纳记录，不声称原版archive通过；改回原版时重新满足全部原要求。

只读接收及本模式Haskell实现不以真实数据实例为前置，完整Feature运行／符合性验收仍需实例和授权，这项剩余工作保留。不得因此写原版ImplementationPreparationAgent PASS。

工程布局和标准构建按B已核实的实际仓库/宿主入口。完整Fao、真实中间事件、不得临时猜adapter等专业约束保留；固定目录／命令不同由B显式选择等价绑定，不能让实现者临场改业务或平台。当前TIS/FRP编译严格在edh-universe目录执行stack install，禁止添加其他参数。

职责终点按本次只读、Haskell实现或其他具名角色范围判断，默认不启动完整team、不自动推其他仓或merge。源码、构建、运行和最终验收分别报告。

## 5. 接收后真正实施

先恢复完整计算链，核方法主体、触发和结果。路径或缺文件由交付方修；存在两种业务解释或缺主要工程决定，给确切差异回A/B；保留可用部分，不靠旧聊天补猜。

按B图实现完整顶层Fao、业务结果类型、target/cal type和真实doImpl，需要正式缓存时完成load/dump。责任块使用真实上游结果，具名实现规定程序和参数调用，不能以no-op、外部结果参数或大闭包代替未实现方法。

verification_observation中的Occ来自真正计算链并被下游使用，字段语义完整，复用已有ADT存储能力；不另算诊断副本、不扩大FaoResult。交回实际dump_field、Occ/根类型、方法与位置供后续schema消费。

实际import、注册、模块暴露和手写接线尽量由Pro写全。Codex在有授权的工作区应用代码、执行生成工具、标准构建、实际测试和真实运行，保存命令、版本、退出码和日志。环境不足交具体执行任务，不在同一不可执行面空转；不改业务或删测试求绿色。

源码尽量由Pro完成，按[DR10](DR10_PRO_IMPLEMENTATION_AND_CODEX_ORDERS.md)向Codex交现场执行及确有理由委派的编码；不能因完整基础Feature可用同事方法表达就默认转给Codex主写。Codex按[DR11](DR11_CODEX_TWO_ROUTE_EXECUTION_AND_FEEDBACK.md)执行授权任务，可连续完成已明确的小修和调查；超出范围回Pro。编码者变化不改变完整普通Feature的边界、方法或父组合责任。

当前先完成业务与正式连接，诚实路径具备后尽早真实反馈，同时继续全部主体。不默认同步扩写测试程序，不以全场景/proof作为首次真实运行前置；当前具体问题作定向检查，后续实际需要再补回归。交回代码、实际方法/参数、正式结果及已执行/未执行证据，测试代码存在不算执行通过。

## 6. 返回与管理接收

只读请求只报接收检查，不报实现PASS；源码／接线、编译、实际运行、正式读回分别报告。未编译不能称本模式实现完成，未真实运行不能称完整符合性完成。包装／最终验证归明确后续角色，不由YAML自动满足。

普通实现／接收聊天保存本轮完整提示回答和实物，不维护公共README、长程推进地图、总工作量、资格或下一任务。管理／审查端按DR06与Overlay12实际接收、维护图和续接；原版、接入版及方法借用都不能绕过外层交付。A业务地图不是进度图，按业务任务处理。

失败保留已经完成的代码／正文、具体问题、影响和尝试，负责人跟到修订被消费。运行反馈进入Pro诊断／指令／复验，不能止于回传。首次真实采用的结果回到本绑定维护，不静默改上游原版，也不以方法文档存在声称跨用例或部署验证成功。
