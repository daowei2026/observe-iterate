[BI01-FO-01-R0002-20261022T030102Z-ab9c51f4]
work_id: BI-01
invocation_id: BI01-FO-01-R0002-20261022T030102Z-ab9c51f4
assignment_token: BI01-FO-01-READER-4fec4d972a5841ce9c298b803c6f0f52
role: review
recipient: chatgpt:细节叙事生成_金标:BI01-FO01-读图
当前阶段：专业任务 BI01
当前职责：专业任务 BI01 独立只读审查
对应专业工作：具名独立只读审查（不自动通过）

本角色仅在存在真实独立审查委派与可取得exact被审对象时使用。按照[当前专业方法](../../professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md)及本次真实被审业务目标和方法实际核对专业主张、反例、证据适用范围及影响；不信作者自评，不代写候选后自签。当前专业审查方法仍为PARTIAL时，如需超出现有合同的正式独立审查，明确MISSING并请求有权补充，不因通用role/review模板存在就报告PASS。管理Gate、执行自查、Worker技术验收、Owner决定彼此不能替代。
本轮独立审查若 GitHub 提交不可用，同样可以依 [V2 轮次 ZIP 合同](../../runtime/operations/V2_ROUND_RECORD_CONTRACT.md) 将原审查结果 ZIP 写入 MCP server 可写的 `H:\fy\observe-iterate-share`，由操作 Codex 在 `/dwdhome/fy/observe-iterate-share` 检查并合法发布；必须保留真实评审权限和完整 Return，不能因 ZIP 出现而自称审查/管理已接收。

## Owner完整目的

# 具体特征观察：专业主干及其关系

## 1. 当前专业工作目标

以**具体已实现、可取得数据的特征**为研究对象，了解实际特征的含义、输入、输出与参数，在实际市场数据上探索怎样合理展示和理解它，检查特征正确性及其结果是否符合普通投资者对市场过程的正常解读。观察中产生的新认识可以反过来调整参数、展示方式和实际绘图安排。

这是一套**可迭代的工作起点**，不是要求运行前已经形成完美的方法体系。原有 U2/U3 总体设计按需要提供背景和原意图；不再以完成整套 U2/U3 业务观察作为本轮目标。

## 2. 四项专业工作

| 工作 | 本身解决什么 | 本轮需要考虑的内容 |
| --- | --- | --- |
| **1. 初始合理参数** | 让具名特征具备第一轮可观察的实际配置 | 先理解特征含义、输入、输出、参数及参数层次；基于既有实现和资料考虑初始参数 |
| **2. 特征展示方式** | 决定特征应该画什么、怎样画才容易理解 | 哪些内容必要；文字说明图中对象和含义；单品种先看还是直接多品种看，按具体特征决定 |
| **3. 使用 aidata 实际制图** | 将观察需要的内容放到真实市场图与对应数据中 | 先判断已有长期概览和大—中—小尺度图方式是否合适；合适时再决定相应配置；不把工具问题与展示设计本身混为一谈 |
| **4. 观察分析** | 从实际结果获得对特征的认识 | 检查特征的正确性，以及按普通投资者对真实市场情况的正常理解和解读，特征结果是否合理；记录问题、认识、后续调整 |

这四项是**工作内容**，不是四个硬性的串行阶段。通常可以先了解配置与展示，再实际绘图和观察；若后一步暴露前一步的问题，应返回修正，不能为维持阶段顺序而继续错误假设。

## 3. 边界

- **具体特征是本轮研究主体**；不是直接在 U2/U3 大叙事与细节字段之间来回跳转。
- U2/U3 的 Narrative、Use Case 或处理依赖，只在解释这个特征的原意图、来源及后续用途时按需查阅，不承担原来的整体业务验收目标。
- 旧 S1–S3 的专业工作划分退出；既有专业知识和工具经验是否复用，以对当前四项工作是否仍然适用为准。
- 特征显示方式与 aidata 实际绘图分开研究；第二项预期形成的可复用展示配置，未来可考虑放在 aidata 的 feature_configs 目录，**何时放入、由谁实现尚未确定**。
- 不预设所有特征都必须先单品种、或必须直接多品种；不预设必须先把每个参数调到最终最优后才能画图。
- 本方案不预设四项工作各占一轮 Pro、四轮 R 或四个管理 Gate；实际推进由有权管理根据专业需要持续安排。

## 4. 怎样推进和返回

专业执行者依据特征实际情况决定本次重点，保留**为什么改变**的依据。例如看到结果后发现画法遗漏必要内容，可返回工作 2；发现图层配置不合理，可调整工作 3；发现某个参数使特征产生有疑问的结果，可返回工作 1。返回并不是重新开始全部工作，已有有效结果应沿用并记录变化。

专业探索中尚未确定的结论允许保留疑问；已知、可识别且会直接影响夜间长程推进的重要执行障碍，不能仅以“交给后续迭代”为由忽略。这类运行准备问题在**仓库修改后**的准备 3 中统一核查。

## 5. 已知第一个观察对象的实际边界（背景事实）

CYF 当前第一项 U2NormalNodeBehaviorFrp 位于 U2 较上游，主要描述单品种单尺度近期已完成过程和当前未完成过程，而非直接识别跨品种同轮机会簇或完成 U3 的资金依据。CYF 已说明它值得进行一轮投资业务观察，但不能承诺收益预测增量或完整 U2 投资解释能力。

因此第一轮应以这个具体特征实际能输出和能观察的内容为范围；后续具体例子、参数、展示组合由四项专业工作实际推进，不由本纲要提前代做。

来源：daowei2026/observe-iterate@4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md::full

## 本轮当前工作

# BI-01-FO-01 首次独立地图可读性检查

task_id: BI01-FO-01-WORKMAP-READER-01
work_id: BI-01
run_id: BI-01-FO-01
role: review
professional_mode: INDEPENDENT_REVIEW
recipient_ref: chatgpt:细节叙事生成_金标:BI01-FO01-读图

签发人为本 run 的 R0001 管理，原 invocation 为 BI01-FO-01-R0001-20261022T021624Z-f9d83a32；Reader 自己的实际 invocation/token 由主控合法派发生成，不能借用管理 token。

采用依据：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::#adoption`。采用前路径说明是同文件 `#reader-pre-adoption`。当前 Workmap 未 ADOPTED，本任务经已有 first_reader 入口取得真实独立阅读证据，不借旧运行许可、不绕 Gate。

<a id="scope"></a>
## 1. 要解决的问题及独立性

对本 run 新的工作地图和完整专业任务作真实只读检查：另一个没有参与编写的人/上下文能否从这些正文理解 Owner 要做什么、当前具体特征是什么、真实数据与专业结果从哪里来、可消费资格是什么、哪些已做哪些未做，以及下一步应由谁做什么而不让主控补业务判断。

直接对照 Owner 完整目标、原四项方法和本次候选原文，不只核作者概述自洽。只读，不编写或修改被读方案、当前任务、管理决定、Intake、参数/展示方案或源码。真实独立性按实际参与说明；新聊天名本身不构成独立证明。此任务不是整个 N 的独立业务/算法验收，也不是全仓审计。

<a id="inputs"></a>
## 2. 冻结的被读对象

四项输入统一冻结于 `daowei2026/observe-iterate@89aacaa9b8d7068a567b77c2ca078cb2939c347d`，必须取全文：

- `runs/BI-01-FO-01/README.md`
- `runs/BI-01-FO-01/00_长程推进地图.md`
- `runs/BI-01-FO-01/01_当前任务.md`
- `runtime/config/WORKMAP_BINDING.json`

Owner START 全文是同仓 `9508df84d01856d9d0037b9d627b0f6499c6dba2:runs/BI-01-FO-01/OWNER_START.md`；Owner 完整专业目标及四项原方法为 `4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/00—04` 的实际文件。管理决定全文为上述 8146eb3 提交，不把 later/latest 猜成本次输入。

主控使用实际本地 Git 对上述冻结输入运行已有 workmap_gate snapshot，保存真实 input_commit、reader_fingerprint、task 字节身份并送达；本任务不预填任何指纹。若没有取得实际快照，Reader 如实说明，不将路径/自报读过/关键词匹配当实际阅读。若当前候选发生变化，按既有 first_reader 输入一致性检查交管理，不暗自换版本。

<a id="checks"></a>
## 3. 实际检查内容

恢复这张业务关系：真实行情/Calendar和具体方法 → 正常 N 保存及修后具名读者 → 对应实例/范围/时点的图与数据 → 正确性、普通投资者解释及反例 → 调整/管理接收/Owner判断。检查每一重要主体的实际生产者与消费者、必要/条件性依赖、证据限制和未完能否读清。

尤其检查当前专业目标是否确实从旧完整 U2/U3 任务变成具名 N 特征观察；四项是否可往返而非四 Gate；旧 V2 的 Workmap/授权、I1—I6/S1—S3、固定 ZIP 和已撤工程是否仍藏在当前任务、前置、接收或后继；正确的时间、状态、身份、方法和消费者是否因撤旧而被误删。管理提供的历史 R30/R33 是否被准确标成历史支持，而非本 run 已取数或已观察。

检查实际下一责任是否明确：Reader只供可读性证据；本管理消费后才形成真实采用；专业 Pro 负责完整观察和有需要时的 Worker 工单；Worker 只做实际技术范围；TIS/FRP写权和aidata独立工程边界清楚；主控只装配原文而不补业务。关注多表 N 不能直接 to_df、aidata实际源404等已知边界是否限定了真实受影响结论，而非冻结全部业务。

检查持续管理是否有可执行的 RESULT/CHANGE/EFFORT 条件、原起点及后继；提交/文件数量不能替业务进展。普通细节无需先穷举；不因自己偏爱某种画法就要求重建专业方案。发现关键含混给准确位置、业务影响和应返回责任者，不泛称“建议全面完善”。

<a id="output"></a>
## 4. 交付、资格和停止条件

报告写入本 run `reviews/independent/WORKMAP_READER_01/`；保存完整实质回答、必要引用、自检及两份 Return，GitHub正常快进提交且fresh回读。禁止写候选地图/专业任务/管理Intake。主控运输事实由主控保存，Reader不重抄其提示。

报告应有实际读取清单、独立复述的完整业务关系、结论及每个具体 finding 的位置/影响、仍未确定或未读事项、后继。以 PASS、REPAIR_REQUIRED、INSUFFICIENT_EVIDENCE 之一给出**仅针对本版地图可读性及任务关系**的 verdict。没有问题可如实 PASS，不为证明独立而凑 finding；缺关键正文则不能 PASS。PASS 不代表 N 计算/市场结论、现场工具、投资价值、完整 BI-01 或 Workmap 已采用。

本次独立工作是一个有明确对象与返回者的只读任务，不设“四项业务阶段”，不需要先跑实际行情或设计图。若未完成继续同一受派阅读；真实完成后直接交原管理消费，不自行循环签自己新写的方案。管理与专业完整责任不因本 Reader 结束而关闭。

<a id="return"></a>
## 5. 回交主控与管理

ROLE_RETURN 的 role_outputs.review 如实填 review_target_ref、review_scope_ref、verdict、findings_ref、remaining_review_ref；QUESTION_WORK_RETURN 回 CASE-BI01-FO01-WORKMAP-READABILITY，binding_ref指本次实际派发所采用的本文件#question-work-binding。两份 continuation 与 remaining 指向同一真实正文。接收路由为本管理 BI01-FO01-管理，不自行写管理接收或全局状态。

主控在真实独立报告形成后按 DECISION#reader-accept 投递管理，带完整报告、exact输入及快照。字段缺件回原Reader；管理缺件回原管理。实际发送前按本run身份、在途、原始载荷和 `bi01_run_gate.py --run-id BI-01-FO-01` 现有 first_reader 路径核验，不能拿专业已采用入口替代。

<a id="question-work-binding"></a>
## QUESTION_WORK_BINDING

```json
{
  "schema":"question-work/v2",
  "kind":"BINDING",
  "work_id":"BI-01",
  "goal_ref":{"repo":"daowei2026/observe-iterate","commit":"4d501afa160179818a0563fc6d03656d1e879ded","path":"professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md","selector":"full"},
  "plan_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-pre-adoption"},
  "full_scope_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-scope"},
  "batch_result":"对固定本run完整地图和当前专业任务形成独立可读性与工作关系判断，交原管理实际消费；不代替专业正确性或Workmap采用。",
  "parent":{"status":"NOT_APPLICABLE_NEW_CASE","ref":null,"reason_ref":{"repo":"daowei2026/observe-iterate","commit":"9508df84d01856d9d0037b9d627b0f6499c6dba2","path":"runs/BI-01-FO-01/OWNER_START.md","selector":"full"}},
  "question_ids":["CASE-BI01-FO01-WORKMAP-READABILITY"],
  "question_definitions":[{"question_id":"CASE-BI01-FO01-WORKMAP-READABILITY","definition_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-scope"},"authority_ref":{"repo":"daowei2026/observe-iterate","commit":"9508df84d01856d9d0037b9d627b0f6499c6dba2","path":"runs/BI-01-FO-01/OWNER_START.md","selector":"full"},"parent_question_id":null}],
  "professional_mode":"INDEPENDENT_REVIEW",
  "focus_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-scope"},
  "coverage_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#coverage"},
  "source_reads":[
    {"source":{"repo":"daowei2026/observe-iterate","commit":"89aacaa9b8d7068a567b77c2ca078cb2939c347d","path":"runs/BI-01-FO-01/README.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"冻结被读公共入口，恢复完整共同意图与当前位置","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"89aacaa9b8d7068a567b77c2ca078cb2939c347d","path":"runs/BI-01-FO-01/00_长程推进地图.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"冻结被读七锚点地图，独立核业务关系/进度/未完/后继","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"89aacaa9b8d7068a567b77c2ca078cb2939c347d","path":"runs/BI-01-FO-01/01_当前任务.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"冻结完整当前专业任务及Binding，不只审管理概述","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"89aacaa9b8d7068a567b77c2ca078cb2939c347d","path":"runtime/config/WORKMAP_BINDING.json","selector":"full"},"requirement":"FOCUS_FULL","purpose":"冻结本run接线输入，仍NOT_CONFIGURED，不冒充采用","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"9508df84d01856d9d0037b9d627b0f6499c6dba2","path":"runs/BI-01-FO-01/OWNER_START.md","selector":"full"},"requirement":"MODE_FULL","purpose":"直接对照真实新Owner授权及非继承边界","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"4d501afa160179818a0563fc6d03656d1e879ded","path":"professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md","selector":"full"},"requirement":"MODE_FULL","purpose":"原完整业务目标，不以候选摘要自证","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"4d501afa160179818a0563fc6d03656d1e879ded","path":"professional/feature_observation/01_OUTPUT_BASE_FORMAT.md","selector":"full"},"requirement":"BOUNDARY","purpose":"原成果表达/真实完成界限","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"4d501afa160179818a0563fc6d03656d1e879ded","path":"professional/feature_observation/02_WORK_DETAILS.md","selector":"full"},"requirement":"MODE_FULL","purpose":"原四项完整细节和特征依据，用以核当前任务未遗漏主体","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"4d501afa160179818a0563fc6d03656d1e879ded","path":"professional/feature_observation/03_REUSE_FROM_V2.md","selector":"full"},"requirement":"BOUNDARY","purpose":"原旧知识复用与不继承边界","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"4d501afa160179818a0563fc6d03656d1e879ded","path":"professional/feature_observation/04_AIDATA_USE.md","selector":"full"},"requirement":"BOUNDARY","purpose":"原专业展示与实际工具职责，不冒充现场验证","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"full"},"requirement":"BOUNDARY","purpose":"真实管理签发/撤销/保全/预算/后继与本次只读权限，仍须对原目标独立核查","reuse_evidence":null}
  ],
  "deliverables_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-completion"},
  "completion_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-completion"},
  "budget_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#budget"},
  "routes":{
    "same_work":{"recipient_role":"review","recipient_ref":"chatgpt:细节叙事生成_金标:BI01-FO01-读图","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-same-work"}},
    "accept":{"recipient_role":"management","recipient_ref":"chatgpt:细节叙事生成_金标:BI01-FO01-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-accept"}},
    "decide":{"recipient_role":"management","recipient_ref":"chatgpt:细节叙事生成_金标:BI01-FO01-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-decide"}},
    "return_repair":{"recipient_role":"review","recipient_ref":"chatgpt:细节叙事生成_金标:BI01-FO01-读图","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-repair"}}
  },
  "triggers":[],
  "explicit_no_trigger_reason_ref":{"repo":"daowei2026/observe-iterate","commit":"8146eb3bb394fbf4378bdf441d6dd43284550499","path":"runs/BI-01-FO-01/reviews/management-R0001/DECISION.md","selector":"#reader-no-trigger"}
}
```

来源：daowei2026/observe-iterate@f4783ab2984c4c4667102f077d9e247d4ff86bf3:runs/BI-01-FO-01/reviews/management-R0001/READER_TASK.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::#reader-same-work`
当前生效任务：`daowei2026/observe-iterate@f4783ab2984c4c4667102f077d9e247d4ff86bf3:runs/BI-01-FO-01/reviews/management-R0001/READER_TASK.md::full`
当前任务采用依据：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::#adoption`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@f4783ab2984c4c4667102f077d9e247d4ff86bf3:runs/BI-01-FO-01/reviews/management-R0001/READER_TASK.md::L66-L104`
接收完整范围：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::#reader-scope`
本次接收重点：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::#reader-scope`
接收交付：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::#reader-completion`
接收完成条件：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::#reader-completion`
本次实际证据：`daowei2026/observe-iterate@28973893df34042a61212c96105e92bc4f35af1e:runs/BI-01-FO-01/provenance/turns/R0002/INPUT_SNAPSHOT.json::full`
本次实际证据：`daowei2026/observe-iterate@9ed1c76e22c7f74ede036f49489f37fc95d07003:runs/BI-01-FO-01/reviews/management-R0001/FULL_RESPONSE.md::full`

## 本次直接读取的上下文

- FOCUS_FULL：`daowei2026/observe-iterate@89aacaa9b8d7068a567b77c2ca078cb2939c347d:runs/BI-01-FO-01/README.md::full`
  用途与边界：冻结被读公共入口，恢复完整共同意图与当前位置
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@89aacaa9b8d7068a567b77c2ca078cb2939c347d:runs/BI-01-FO-01/00_长程推进地图.md::full`
  用途与边界：冻结被读七锚点地图，独立核业务关系/进度/未完/后继
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@89aacaa9b8d7068a567b77c2ca078cb2939c347d:runs/BI-01-FO-01/01_当前任务.md::full`
  用途与边界：冻结完整当前专业任务及Binding，不只审管理概述
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@89aacaa9b8d7068a567b77c2ca078cb2939c347d:runtime/config/WORKMAP_BINDING.json::full`
  用途与边界：冻结本run接线输入，仍NOT_CONFIGURED，不冒充采用
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@9508df84d01856d9d0037b9d627b0f6499c6dba2:runs/BI-01-FO-01/OWNER_START.md::full`
  用途与边界：直接对照真实新Owner授权及非继承边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md::full`
  用途与边界：原完整业务目标，不以候选摘要自证
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/01_OUTPUT_BASE_FORMAT.md::full`
  用途与边界：原成果表达/真实完成界限
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/02_WORK_DETAILS.md::full`
  用途与边界：原四项完整细节和特征依据，用以核当前任务未遗漏主体
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/03_REUSE_FROM_V2.md::full`
  用途与边界：原旧知识复用与不继承边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@4d501afa160179818a0563fc6d03656d1e879ded:professional/feature_observation/04_AIDATA_USE.md::full`
  用途与边界：原专业展示与实际工具职责，不冒充现场验证
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@8146eb3bb394fbf4378bdf441d6dd43284550499:runs/BI-01-FO-01/reviews/management-R0001/DECISION.md::full`
  用途与边界：真实管理签发/撤销/保全/预算/后继与本次只读权限，仍须对原目标独立核查
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

运行事实（来自现有记录）：
观察时间：2026-10-22T03:01:02.050213+00:00

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
