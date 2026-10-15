# BI-01：专业问题及原文来源索引

> 迁移来源：CYF DR12（锁定在 `c6a930887c9148e76ba75f8a026549b9a46c9e35`）。CYF A-1～C-2 的市场过程需求、RepoFact/Compiler 与 Host 题面不再作为观察迭代的当前专业题；其历史正文可从原始复制提交及CYF来源查证。以下只采用 [BI-01 既有 I1–I6 专业合同](../../professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md)确实支持的题，未确认的方法一律标记缺失。

## 0. 使用规则

原 DR12 的“完整题面不能代替方法、题号不授 mode 或写权、同工作可跨轮、来源须准确 commit/path/selector、先管理者形成真实工作再派发、既有有效阅读可复用”的规则继续有效。管理任务按[DR13](DR13_WORK_ARRANGEMENT_AND_CONTEXT.md)组织，工作绑定及回交按[DR14](DR14_QUESTION_WORK_CONTRACT.md)执行。不能用旧 CYF S01–S25 的文献索引给 BI-01 添加不存在的专业义务。

### BI-01 专业来源（仓库内实际可读取的已提取正文）

| 任务来源 | 已有专业正文 | 使用位置 |
|---|---|---|
| P00 | [观察迭代总体目标及六阶段 Input/Output/Gate](../../professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md) | 管理、专业执行及必要接收 |
| P01 | [I1–I3资格与G3定向复核](../../professional/source/01_I1_I3_PROFESSIONAL_CONTRACT.md) | 已有输入是否有合法观察资格 |
| P02 | [I4观察、反证、无增量与G4](../../professional/source/02_I4_OBSERVATION_AND_CHALLENGE.md) | 当前首段实质执行 |
| P03 | [阶段接续与就绪条件](../../professional/source/03_STAGE_HANDOFF_AND_READINESS.md) | Gate前后与定向回修 |
| P04 | [专业 Pro→Worker Codex 工单与验收](../../professional/source/04_PRO_WORKER_CODEX_HANDOFF.md) | 需要补算、图或有限工程任务时 |
| P05 | [角色及Gate接收职责](../../professional/source/05_ROLE_GATE_AND_HANDOFF_CONTRACT.md) | 管理、执行、审查的权限 |
| P06 | [管理首次及后续委派要求](../../professional/source/06_MANAGEMENT_AND_DISPATCH_REQUIREMENTS.md) | M-START/M-REASSESS/M-CLOSE |
| P07 | [专业角色与操作端责任边界](../../professional/source/07_PROFESSIONAL_OPERATION_BOUNDARY.md) | 业务完成与机械运输区分 |

完整的跨实例专业 Router / 深层独立审查方法尚无充分原文，当前分别见[任务 Router](../../professional/TASK_ROUTER.md)和[完成与审查](../../professional/interfaces/COMPLETION_AND_REVIEW.md)的缺失标识。**缺失不能被此题库自动补造成有权专业方法。**

## 1. 每题共同输入与交付

正式专业任务须取得Owner完整目标及权限直接来源、实际工作对象及总体位置、已做/已审/未完、本题完整方法及相邻依赖、实际交付与回路。原合同/accepted parent只在真实存在或原任务要求时必读：全新用例明确无parent，已有成果缺原件则具名REQUIRED_MISSING，不得借新建例外规避连续性。首次管理尚无计划/覆盖/预算时按DR14 §1.0的BOOTSTRAP开始，由管理者实际形成这些输出；主控及Owner不预填专业答案。已形成计划的专业派发采用DR14 §1.2完整BINDING。

管理提供已确定的当前采用、已撤旧要求、整体位置和已知问题处置；专业者据此取得必要正确正文，交实质答案、实际成果和合法续作，不代做管理的全局裁定。I4 的真实观察、对照、反例和替代解释必须有证据；I1–I3 的结果资格不能由摘要冒充，I5 的图不能代专业解释，I6 的建议不能冒充正式派发。管理与审查题按 DR06／DR13 的实际职责执行，不按题号新增聊天、模式或必须产物。

专业正文使用已有 artifact 结构和人可读解释。下列题目的“交付”是必须真实存在的内容，可放在同一正文不同锚点；无需逐项新增文件。每轮用 DR14 定位本轮重点和本段剩余，不要求填满全部题目。局部完成、candidate、handoff-ready、Owner accepted、运行已证各自保持原权力。

<a id="i1"></a>
## I1｜识别值得观察的业务问题

**准确专业来源：**P00 §2 I1、G1；P05。实际 Task Binding 的 `source_reads` 必须定位上表 P00–P07 对应原文件、真实采用的 exact commit 和必要章节；仅题面不构成已读方法。

**实质交付：**交被选观察问题、范围、业务意义与所需证据；由管理按 G1 判断。本阶段已有结果可在证据许可范围消费，缺少原件、授权或完成标准时保留 `MISSING`/待核查，不能用结构检查宣布通过。当前批次的重点不缩小完整阶段责任，专业执行与 Gate 接收遵循 P05。

<a id="i2"></a>
## I2｜使设计和数据成为可执行依据

**准确专业来源：**P00 §2 I2、G2；P01。实际 Task Binding 的 `source_reads` 必须定位上表 P00–P07 对应原文件、真实采用的 exact commit 和必要章节；仅题面不构成已读方法。

**实质交付：**交 source/method/case 版本、合法取得路径、缺项及参考/正式边界。本阶段已有结果可在证据许可范围消费，缺少原件、授权或完成标准时保留 `MISSING`/待核查，不能用结构检查宣布通过。当前批次的重点不缩小完整阶段责任，专业执行与 Gate 接收遵循 P05。

<a id="i3"></a>
## I3｜取得可信且可检查的具体业务结果

**准确专业来源：**P00 §2 I3、G3；P01、P03。实际 Task Binding 的 `source_reads` 必须定位上表 P00–P07 对应原文件、真实采用的 exact commit 和必要章节；仅题面不构成已读方法。

**实质交付：**交实际可读数据、关键复核、可追溯的观察资格范围；管理按 G3 限定接收。本阶段已有结果可在证据许可范围消费，缺少原件、授权或完成标准时保留 `MISSING`/待核查，不能用结构检查宣布通过。当前批次的重点不缩小完整阶段责任，专业执行与 Gate 接收遵循 P05。

<a id="i4"></a>
## I4｜AI 主动业务观察与挑战

**准确专业来源：**P00 §2 I4、G4；P02。实际 Task Binding 的 `source_reads` 必须定位上表 P00–P07 对应原文件、真实采用的 exact commit 和必要章节；仅题面不构成已读方法。

**实质交付：**交真实 Case 事实、增量/无增量、有据挑战、替代解释和继续检验问题。本阶段已有结果可在证据许可范围消费，缺少原件、授权或完成标准时保留 `MISSING`/待核查，不能用结构检查宣布通过。当前批次的重点不缩小完整阶段责任，专业执行与 Gate 接收遵循 P05。

<a id="i5"></a>
## I5｜支持 Owner 的真实业务判断

**准确专业来源：**P00 §2 I5、G5；P03、P04、P05。实际 Task Binding 的 `source_reads` 必须定位上表 P00–P07 对应原文件、真实采用的 exact commit 和必要章节；仅题面不构成已读方法。

**实质交付：**交Owner可阅读图和结果、证据及争议，Pro自查并由管理判断 G5。本阶段已有结果可在证据许可范围消费，缺少原件、授权或完成标准时保留 `MISSING`/待核查，不能用结构检查宣布通过。当前批次的重点不缩小完整阶段责任，专业执行与 Gate 接收遵循 P05。

<a id="i6"></a>
## I6｜把反馈转成下一轮实际行动

**准确专业来源：**P00 §2 I6、G6；P03、P05、P06。实际 Task Binding 的 `source_reads` 必须定位上表 P00–P07 对应原文件、真实采用的 exact commit 和必要章节；仅题面不构成已读方法。

**实质交付：**交具名下一轮目标/来源/责任/Gate或合法等待/停止；超授权归Owner。本阶段已有结果可在证据许可范围消费，缺少原件、授权或完成标准时保留 `MISSING`/待核查，不能用结构检查宣布通过。当前批次的重点不缩小完整阶段责任，专业执行与 Gate 接收遵循 P05。

## 2. 题目自己的检查

向后：本题必须保留原文正向业务、细度、例外、禁止、写权和新补充；不能只抽Owner口号而丢Pro已展开细节。向前：结果应能进入下一专业题/接收，主控无需猜重点，实际完整目标未被局部取代。schema、标题和引用存在不能证明这两项。

任务本身不适当时审查可以否定前提；改变真正Owner决定仍需原授权。后续经验修题库要明确旧成果影响，不能让一次方法发布自动升级运行资格或批量重做旧用例。
