# 第二阶段专业适配状态（进行中）

本分支以CYF完整保真复制 `4760638c2ebaa18c4501925499cc4fce95994b73` 为可追溯原始基线，未直接修改或删除该历史快照。当前为迁移工作分支候选，**禁止作为可运行BI-01正式Release**；不得发送手机消息、启动专业Agent或假称Gate已通过。

## 本批已改

- DR00：角色入口和专业方法选择改成BI-01的P00–P07，保留协调者／管理／承办者通用职责。
- DR06：保留完整目标管理、剩余工作、优先级、管理纠偏、预算和后继，改专业合同来源。
- DR12：CYF A/B/C专业题及S01–S25源替换为BI-01既有I1–I6与P00–P07准确来源；未形成的专业Router/独立审查标记缺失。
- DR13：保留管理题M-START/M-REASSESS/M-CLOSE及§6上下文、§8–10触发与处理；CYF A/B/C专属工作组合替换为BI-01 I1–I6、Worker与审查来源。
- DR14：保留BOOTSTRAP、BINDING、RETURN、routes、triggers、持续复看和主控顺序；替换固定Feature地图及C_WORK专属要求。
- Overlay13：保留原有角色回交、去重、权限和持续责任；将A/B/C具体交付义务改为BI-01专业来源引用。

## 连接中断后已恢复的第二批（2026-10-15）

- Overlay08：消息固定正文改为BI-01已存在的专业引用和BI01角色标记；原通用运输、Owner目标、工作身份、准确来源、回交和材料使用规则保留。对CYF专属正文的删除不等于BI-01专业能力已齐。
- `runtime/overlay/tools/management_prompt.py`：策略文件位置改为本仓实际路径；通用stage不再只允许A/B/C；同工作继续和新有权任务不再依赖CURRENT_C_WORK特殊标记；机械验签、指令来源和recipient核验保持。
- Overlay12：原有`workmap`、`prepare/verify`、去重及路由说明保留；命令入口改成`O=runtime/overlay`、`CONFIG=runtime/config/COORDINATOR_DISPATCH.json`；旧U2/U3配置和状态不作为BI-01授权。
- 固定Dispatch配置：将旧候选占位结构与现有脚本合同`coordinator-dispatch/v3`对齐，提供`BI-01`技术工作标识和`BI01`模板stage及候选mode；目标/数据来源来自`professional/`，但没有实际BOOTSTRAP/BINDING、接收者和合法任务前不得发送。采用边界见`runtime/config/ADOPTION_STATUS.md`。
- 第二批文件只在本PR工作分支提交，不动`main`和第一阶段保真提交；不做手机/Pro/业务试跑。

## 本次中断恢复与静态检查（2026-10-15）

- 恢复前最后有效提交：`d593d0a93b74c68be957699bb3a7c956728d860f`，不重复修改其中6份已完成DR/Overlay规则。
- 第二批恢复提交：`417141e3b9578761fc383e9503d6121a49147dbb`。文件范围仅Overlay08、Overlay12、`management_prompt.py`、Dispatch候选配置、采用状态与本页说明。
- 一次性静态检查：[Actions run 38736886419](https://github.com/daowei2026/observe-iterate/actions/runs/38736886419)；Python `ast.parse`、JSON配置结构、阶段/role模板标记、已有链接、工具与命令路径、`DO_NOT_DISPATCH`均PASS。
- 本轮没有调用`prepare_dispatch`派发业务任务，没有调用手机/模型，也没有运行依赖CYF A/B/C情形的旧端到端测试。一次性静态验证工作流完成后从分支删除，不作为常驻运行服务。
- 远端Git没有其他并发提交，且本分支Actions均已完成；但外部Codex本地工作树及未提交修改不能由GitHub远端证明，未冒称已检查。

## 尚待适配

DR01–05、07–11及管理Harness其他专业段落；Overlay00–07、09–11中CYF专属部分；其余程序／Schema／测试的BI-01场景覆盖、Release和生成视图、全库跨目录链接、cgpterm侧入口。配置虽已对齐消息组装工具的静态合同，但真实管理/专业Binding和路由尚未采用，不能声称端到端可运行。不得将当前文档已通用化等同整套系统已通用化。

## 方法

保留通用运行段落全文；只在真正的CYF专业段落换成BI-01准确专业引用，缺原文不得补造；每批复核Git diff和身份/授权/Return边界。已复制的`runtime/release/`继续视为CYF旧发布候选，不能成为本次正式Release。

本批仅静态文件变更，**没有运行手机、Pro任务或长程试跑**。
