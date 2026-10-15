# 第二阶段专业适配状态（进行中）

本分支以CYF完整保真复制 `4760638c2ebaa18c4501925499cc4fce95994b73` 为可追溯原始基线，未直接修改或删除该历史快照。当前为迁移工作分支候选，**禁止作为可运行BI-01正式Release**；不得发送手机消息、启动专业Agent或假称Gate已通过。

## 本批已改

- DR00：角色入口和专业方法选择改成BI-01的P00–P07，保留协调者／管理／承办者通用职责。
- DR06：保留完整目标管理、剩余工作、优先级、管理纠偏、预算和后继，改专业合同来源。
- DR12：CYF A/B/C专业题及S01–S25源替换为BI-01既有I1–I6与P00–P07准确来源；未形成的专业Router/独立审查标记缺失。
- DR13：保留管理题M-START/M-REASSESS/M-CLOSE及§6上下文、§8–10触发与处理；CYF A/B/C专属工作组合替换为BI-01 I1–I6、Worker与审查来源。
- DR14：保留BOOTSTRAP、BINDING、RETURN、routes、triggers、持续复看和主控顺序；替换固定Feature地图及C_WORK专属要求。
- Overlay13：保留原有角色回交、去重、权限和持续责任；将A/B/C具体交付义务改为BI-01专业来源引用。

## 尚待适配

DR01–05、07–11及管理Harness的其他专业段落；Overlay00–12；`management_prompt.py`的A/B/C代码分支与配置v3接线、Schema/测试、Release及生成视图、全部跨目录链接、cgpterm侧入口。不得将当前文档已通用化等同整套系统已通用化。

## 方法

保留通用运行段落全文；只在真正的CYF专业段落换成BI-01准确专业引用，缺原文不得补造；每批复核Git diff和身份/授权/Return边界。已复制的`runtime/release/`继续视为CYF旧发布候选，不能成为本次正式Release。

本批仅静态文件变更，**没有运行手机、Pro任务或长程试跑**。
