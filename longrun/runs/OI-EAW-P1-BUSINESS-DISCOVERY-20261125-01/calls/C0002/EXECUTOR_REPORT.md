# E1 专业回交｜C0002 / D002 / S01＋S02

本 D 的 S01、S02 已实际完成并逐步保存。S02 存在已明确的局部证据限制，仍具备任务书 S03 的合法后继。零 W；本次没有开展 S03～S09，也没有形成市场差异、候选迭代点或已确认的正式设计缺陷。Run 仍在进行。

## 身份、采用原件与授权

- run_id：OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01。
- call_id / token：C0002 / eaw-discovery-c0002-d002-20261125-1530。
- sender：codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01:executor:E1。
- return_to：codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01:manager。
- [D002 正式原件](https://github.com/daowei2026/observe-iterate/blob/9d4c87f77736e5a92eda33b7655065b698b6b4e9/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/delegations/D002/DELEGATION.json)；[本调用 INVOCATION](https://github.com/daowei2026/observe-iterate/blob/a40bab56069a275df0d8ec094c8e6688fbc3c807/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0002/INVOCATION.json)；[原 Manager Return](https://github.com/daowei2026/observe-iterate/blob/702de77e83070a10ba96bf9aeb7bc88ea5a4a59d/longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0001/PRO_RETURN.json) 均已亲自回读。
- 专业任务书及通用运行/角色指南采用 observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198；controller Skill 采用 cgpterm@da8dabfdaf9a46d563aab261bef77cb5d72d7782。已读任务书全文、S01/S02 实际所需原件和 executor 指南；未采用旧专业 control/、skills/，没有另制专业分析计划。
- 执行配置沿用本次正式派达：CODEX_NATIVE_DIRECT，gpt-6.1-sol/max，workers=[]，AUTONOMOUS，工作区 /dwdhome/fy/BASE_E6_2。物理模型/线程核验属于 controller 的派达事实；本报告不伪造独立物理回执。

Owner GO、Binding、最新粒度纠正均已读取。仅采用 operation=eaw-business-discovery-research-and-publish 的既有写面：授权工作区及目标分支的本 Run 路径。生产数据/代码只读；无生产重跑、参数更改、数据库写入或新增行情。D001 已被替代，本次只签认 D002。旧空 thread 与首次实际执行会话的补建关系按本调用原文保留，不将其解释为业务重做或新增执行者。

## 实际产出及关键认识

| 步骤 | 完成事实 | 产出 |
| --- | --- | --- |
| S01 | 已读原始叙事关键轮次、历史入口/稀疏化取舍、P1 架构/四 DSU/F4 合同及实际代码入口；明确四特征共同 Wall 依赖、互不消费关系、业务语义与三组对照所需信息 | [S01 理解记录](S01_UNDERSTANDING.md)、SOURCE_INDEX.json、sources/ |
| S02 | 已读取全部给定文件、核 manifest/字段/轴/时间/局部无效/重复及展示资料；核查实际版本证据，建立过程关联及发现/复现索引 | [S02 核查报告](S02_DATA_AUDIT.md)、audit/、research/、ARTIFACT_INDEX.json |

实际材料有 148 个 Tick 窗口、rb/hc/i、444 个窗口×品种单元；346,764 条报价按 symbol/UTI 去重后 328,920 条，17,844 条重复，0 重叠冲突。全部 2,924 个文件的 manifest 引用/字段/行数核对匹配；源文件哈希复核全部未变。局部无效仅涉及 i 的部分买侧及 1 行两侧非有限字段，已给准确位置，其余有效范围保留。

与后继最相关的证据边界：

1. 本批有效同价配对中，主买/主卖代理逐项等于对应盘口可见减少量；存在总成交为零而代理为正、代理和与总成交不等的记录。不能用该代理独立证明成交消耗或补单，更不能让 `Δq+C` 的同源恒等式成为循环证据。它仍可带来源标签参与任务允许的探索；依赖独立方向真值的判断局部受限。
2. 读到了 Wall、F4、Build、Attack、Absorb 展示材料，但没有取得/验证实际 producer commit、参数 receipt、exact upstream 或完整 FRP history/publication。source_key 不是已证实 Git commit。不能由展示缺失推断正式产品缺失，不能把无新事件或无展示段写成无墙，也不能把参考 TIS/FRP commit 写成本批版本。
3. 9 个窗口跨推定交易日期，21 个窗口内自然时间断点在三品种中形成 63 个配对断点。UTI 连续仍会跨休市；连续有效段、缺失与边界均已单列，禁止跨断点配平/观察。
4. 已在过程细节读取前按 metadata 冻结发现与复现分配：发现 95 窗口，预留 53 窗口；127 个保守过程组索引和 23 个更保守日期关联块。分配没有使用市场形态或后续结果；没有把这些索引数冒充真实独立攻防过程数。

S01 还核到历史 signed net_add、参考 Build reload proxy、Absorb consumed/visible/replenish 的度量差异；联合表达是否足够仍待后续真实对照与相容正式历史证明，本步没有把参考代码语义差异宣布为设计问题。

## 产物入口与自检

本地总目录：

```text
/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0002/
```

- `ARTIFACT_INDEX.json` 给全部冻结专业材料的准确本地路径、bytes、SHA-256；原始大表/详细源码保留本地，未要求逐份远端发布。
- `audit/FILE_INVENTORY.csv`、`SCHEMA_CATALOG.json`、`QUOTE_QUALITY.csv`、`INVALID_ROWS.csv`、`CONTINUITY_INDEX.csv`、`GAP_INDEX.csv`、`OVERLAP_CONFLICTS.csv` 给数据及有效范围。
- `audit/WINDOW_PROCESS_INDEX.csv`、`PROCESS_GROUPS.json`、`DEPENDENCE_LINKS.csv`、`SAMPLE_ALLOCATION_FROZEN.json`、`CASE_USE_LOG.csv` 给独立性与使用追溯。
- `SOURCE_INDEX.json` 保存专业来源、版本和哈希；任务书 exact SHA 与 D002 一致，controller 便利副本只多末尾空行。
- `research/audit_s02.py`、`research/verify_s02.py` 可重放本次核查，未导入或运行生产特征；`SELF_CHECK.json` 的 14 项实质一致性检查全部通过，包括源文件未变、去重守恒、连续段覆盖每条有效本侧行、分配互斥和已回读原件 blob 一致性。这个自检不替代主控独立物理回执核验。
- `TASK_PROGRESS.md`、`BUSINESS_PROGRESS.md` 是本调用的技术/业务进展，供原 Manager 更新 Run 全局双进度；E1 未覆盖 Manager 的全局记录。

## 专业完成判断及后继

D002 原生最低产出已满足：S01 有职责/依赖/语义/来源/版本差异记录；S02 有真实清单、字段和版本来源核查、有效/无效范围、限制及独立性记录。已取得的数据足以继续不依赖缺件的 S03；不需要因局部正式材料或独立方向真值不足停止整个 Run。

回原 Manager 消费上述成果，再安排单独 S03；S04/S05/S06、逐候选 S07＋S08、最后 S09 依 Owner 最新粒度推进。准确未执行范围与恢复入口见 [REMAINING_SCOPE.md](REMAINING_SCOPE.md)。后续复用真正执行本 C 的 E1 session。本调用以零 W、REPORTED_COMPLETE 回交，仅表示本 D 的报告状态；物理派达/回收及 Manager 消费由原主控完成，不冒称已送达或父任务完成。

本报告先作为独立 Git commit 发布；正式 PRO_RETURN 再引用该 exact commit，避免未来引用或循环引用。发布限定指定 Personal 连接与本 Run 路径，按当前分支 head 条件写入并 exact commit 回读。
