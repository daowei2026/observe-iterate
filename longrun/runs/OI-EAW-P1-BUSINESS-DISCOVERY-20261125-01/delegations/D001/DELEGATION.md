# D001｜EAW P1 挂单—成交演化的业务迭代点发现（两轮，S01～S09）

- Run：OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01
- issuer_call_id：C0001
- issuer：codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01:manager
- recipient：codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01:executor:E1
- return_to：codex:OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01:manager
- 具名工作：EAW P1 同批 Tick 窗口两轮业务迭代点发现。
- task_ref：daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:ai_chat/业务有效性/EAW_P1_挂单成交演化_迭代点发现任务_V0.4_长程执行版_20261125.md
- business_context_ref：daowei2026/observe-iterate@5b645cff6ec45b89c4f8979f9627f5400a0714e3:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/OWNER_START.md

## 范围与实际接续

亲自读取 task_ref 全文及 §8.0 S01～S09，按其中实际依赖顺序执行。本 D 合并这九项连续步骤，可跨多个 C 在原 D、原 executor 线程中接续。内部步骤和候选切换时按任务书保存实际成果，不等待逐步另签 D 或审批。S07～S08 按候选逐条闭环，再按 §8.4 的原生结束条件进入 S09。专业方法、证据等级、完成口径及输出要求均直接来自 task_ref；本正文不新增专业分析计划、Gate 或审批。

唯一 executor 按 CODEX_NATIVE_DIRECT 在 /dwdhome/fy/BASE_E6_2 直接执行；workers=[]。本 D 是首次专业委派，manager 尚未收到研究成果或 executor 送达回执，S01～S09 均未被确认为开始或完成。

## 当前有效输入与版本

- daowei2026/observe-iterate@2629799314e5b26966d58f9e10caeff52fe724d0:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0001/FULL_ASSIGNMENT.md
- daowei2026/observe-iterate@8d057c69afc384af92a2f634b61e3ed29d8aa3fa:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/calls/C0001/INVOCATION.json
- daowei2026/observe-iterate@5b645cff6ec45b89c4f8979f9627f5400a0714e3:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/OWNER_START.md
- daowei2026/observe-iterate@bc30c55fff35f81de5102ed43c0e168eb7a8de11:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/RUN_BINDING.json
- daowei2026/observe-iterate@bc30c55fff35f81de5102ed43c0e168eb7a8de11:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/RUN_RESOURCE_BINDING.json
- daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:ai_chat/业务有效性/EAW_P1_挂单成交演化_迭代点发现任务_V0.4_长程执行版_20261125.md
- daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:longrun/README.md
- daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:longrun/contracts/LONGRUN_PROTOCOL_V2.md
- daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:longrun/CONTROL_PLANE_ADAPTER.md
- daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:longrun/CODEX_NATIVE_EXECUTION_PROFILE.md
- daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:longrun/professional/PRO_MANAGER_GUIDE.md
- daowei2026/observe-iterate@b1bf8025dd49091e71c8814caf36c2e02aced198:longrun/professional/PRO_EXECUTOR_GUIDE.md
- daowei2026/cgpterm@da8dabfdaf9a46d563aab261bef77cb5d72d7782:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md

Owner 数据路径（原任务书 §3.1）：

`/home/dw/.codex/visualizations/2026/11/16/01a1e335-cd15-7f72-a7d9-f53c52feb09e/caegraph-delivery-30/caegraph-review/data/`

两轮均使用上述同批窗口。实际数量、品种、日期、字段、产物版本及历史完整性由 executor 按 S02 实际核查，本次 manager 未将其预先认定。TIS/FRP 在任务书中的参考提交不等于本批数据已核实生产版本。

已读取的本地精确任务书副本：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0001/sources/TASK_V0.4.md`，SHA-256 `fa80b5eaf52a03edde167b5e13dc463c5b92c6dbea11a03f420e1c3e11a80089`。其他通用运行原件的准确副本在同级 `sources/longrun/`；主控已提供副本亦可使用：`/dwdhome/fy/cgpterm/artifacts/eaw-discovery-controller/source/longrun/`。这些路径只帮助读取，采用来源仍为上述 exact refs。不采用原专业 control/、skills/。

## expected_outputs（任务书原要求）

以下逐项直接摘自 §8.0 的产出列，详见原件输入与工作列，不构成新增验收：

| 步骤 | 任务书规定产出 / 进入下一步的条件 |
| --- | --- |
| S01 业务及特征理解 | 一份简短的业务与特征理解记录：职责、依赖、语义及来源链接、待核实的版本差异。理解到能够解释三组对照所需信息即可，不做全面代码正确性验收。→ S02 |
| S02 数据接入与实际版本核查 | 数据清单、字段和版本来源、有效/无效范围、已知限制、独立性记录。只在整体无法取到数据且没有其他实质工作时回报阻碍。→ S03 |
| S03 全范围候选检索 | 可重放的检索程序、统一候选表、三入口计数/重合/排除说明、全部有效范围扫描记录。→ S04 |
| S04 第一轮 B1 对照 | B1 对照组清单、证据图/数值、业务差别、初步表达核查及候选迭代点；不足的原因和补救。→ S05 |
| S05 第一轮 B2 对照 | 独立的 B2 结果、真实对照、表达核查、候选点及不足说明；不能用 B1 结果替代 B2。→ S06 |
| S06 第一轮 B3 对照及线索归并 | B3 实际结果、第一轮汇总、逐项候选与证据等级、后继取证清单。不是提交给 Owner 审批的计划；直接进入 S07。 |
| S07 第二轮逐条深入取证 | 每条候选的真实证据及适用范围、业务影响、条件统计分母、复现与反例、缺失证据；完成一条后进入其 S08，不等待其他候选。 |
| S08 第二轮逐条设计定位与最小信息试查 | 该条迭代点记录、证据等级、准确设计出处、下一轮设计问题；尚不足则标待证。保存后回 S07 处理下一条，或按新增线索继续本批分析。 |
| S09 总体归并与交付 | 最终报告和证据索引；交付最强可支持的结论，不以存在一个迭代点、预设案例数或输出文件数量作为唯一停止标准。 |

运行记录的最低要求：启动时创建一份持续更新的任务进度记录（可命名为 `TASK_PROGRESS.md`，存于本次执行工作区的结果目录）。记录当前步骤、实际输入引用、已完成动作、产出路径、已确认发现、局部限制、待补证、下一步；步骤或候选切换时更新。按实际工作量分批保存候选表、代码、统计和案例证据，避免长程中断后只能看到最后一段聊天。每步状态可用“待开始 / 进行中 / 已完成 / 局部受限”，局部受限要说明是否可继续及已完成部分。恢复时读取已落盘产物，继续当前步骤或尚未完成的候选，不把已写计划当作已完成、也不从头盲目重跑。执行者可自行确定具体研究文件命名和目录布局，不新增多套 Workflow/Skill 或审批节点。

### §8.5 最终交付（原文）

最终报告以迭代点为主，每项必须包括：

- 实际过程及对照、准确品种/日期/时间/价位和原始数值与图；结论范围、独立复现和反例。
- 获得的初步业务知识、对上层叙事哪项问题的影响、必要时价格和后续交互对照及发生规模；说明证据充分程度。
- 现有单特征/联合可用信息，缺失或过迟之处，原始设计选择及现行合同。
- 需要重新审视的具体设计、改进应解决的问题、下一轮验证需求。不要求最终算法。
- 证据不足或存在不可辨识限制的地方，明确标识；实现问题另列。

附候选研究表、检索及统计代码、案例索引、版本/参数及数据引用、扫描覆盖及取样记录。记录每组实际工作量、每条候选的证据等级和去向、剩余研究方向。按业务影响、证据强度及后续成本排序，不把研究线索与已可交接的迭代点混在一起。不得制造问题或拿大量统计代替设计反馈。

## 实际授权与写面

真实授权来源为上述 OWNER_START.md 和 RUN_BINDING.json，机读 D 仅采用下列研究及发布 grant：

```text
operation=eaw-business-discovery-research-and-publish execution_context=/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2,daowei2026/observe-iterate:feat/statistics-driven-feature-closure-v0.3-20261122:longrun/runs/OI-EAW-P1-BUSINESS-DISCOVERY-20261125-01/
```

具体合法操作及生产边界按 Owner GO 与任务书 §1、§3、§8.4；不修改生产特征、参数、公共上游或数据库，不新增行情或重跑生产特征。研究代码、大表、图与详细证据可按原件保存于本 Run 的本地独立研究目录，由专业报告提供准确可核查入口；具体布局由 executor 按原任务自行确定。远端角色写面仅限本 Run 路径，使用 Personal 连接 `link_6ab37f74c7288191a52eb23d2ca1e2c8`，由 controller 串行交接当前 Git 写任务、按当前 head 条件写入并回读 exact commit，不覆盖其他工作。controller 的 Registry/自身 Chat 归档授权不向本 D 扩展。

## 回交与未完成范围

按 V2 向原 manager 提交真实专业报告及 PRO_RETURN，载明实际采用来源、工作范围和版本、准确成果入口、当前步骤/候选、未完成及局部限制、下一实际工作或任务书结束依据。零 W 时 issued_order_refs=[]、accepted_worker_refs=[]。局部缺件按任务书记录影响并继续独立工作；完整研究仍为未完成。manager 依据真实回交更新双进度，controller 负责核验和物理接续。

D 只记录 issuer_call_id，不引用尚未发布的 manager Return。
