# 观察研究 Agent：多品种差异用例与回看研究

当前专业方法是[多品种差异用例观察](professional/case_observation/README.md)，替换旧具体特征四项工作。运行机制继续复用，不另建调度或回交系统。

**本分支为方法与运行接线准备；本次修改没有启动长程任务。** 新任务仍须真实 Owner GO、独立 run 身份和管理采用。旧运行资料只在旧分支及准确历史版本读取，不保留在本分支 `runs/`，不能据此推定新任务已授权。

## 当前专业入口

- [完整目标及两项具体产出](professional/case_observation/00_PURPOSE_AND_OUTPUTS.md)
- [初步研究方法](professional/case_observation/01_RESEARCH_METHOD.md)
- [Owner 阅读入口、统一平台图及调用记录](professional/case_observation/02_OWNER_DELIVERY.md)
- [aidata 三接口及两种图数使用方式](professional/case_observation/03_AIDATA_USE.md)
- [U2/U3 与旧知识的按需复用](professional/case_observation/04_SOURCES_AND_REUSE.md)

当前一批为 3–5 个有明显好坏分化的多品种用例，每例完成位置发现与投资者视角的自主回看。数据必须经 aidata；Owner 从一个汇总文档和一个包含 1d 概览及各例大尺度图的平台链接查看。本批暂不深入用例间关系，不把特征实现与完整 U2/U3 验证变成前置。

## 运行与版本

- 操作仓：`daowei2026/cgpterm`，分支 `fy/observation-iteration-agent-longrun-20261015`。
- 本专业及运行仓的新分支：`fy/multisymbol-case-observation-20261027`，从 `fy/bi01-feature-observation-prep-20261021@9badfa6f30caebbe3156c5e4ee4deb43d22cacb5` 建立。
- [通用运行入口](runtime/README.md)、[本批启动准备](runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md)、[采用状态](runtime/config/ADOPTION_STATUS.md)。
- [运行记录入口](runs/README.md)：本分支只保存新任务运行资料，旧 FO-01 及更早记录到旧分支定向读取。旧专业正文以以上准确历史提交读取，不并列为当前规范。

后续实际启动分别锁定两仓真实完成提交、aidata 现场版本及本次任务来源；分支名、模板、代码检查或图数试验不代替授权。当前尚未有本批实际用例、平台链接或 aidata 现场验证结果。
