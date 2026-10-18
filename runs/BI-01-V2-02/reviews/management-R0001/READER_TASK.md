# BI-01-V2-02 首次 Workmap 独立只读接收任务

task_id: BI01-V2-02-WORKMAP-READER-01
work_id: BI-01
run_id: BI-01-V2-02
professional_mode: INDEPENDENT_REVIEW
recipient_role: review
recipient_ref: chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01
signed_by: BI01-V2-02-R0001-20261018T130131Z-7f26abeb

本任务由 R0001 管理在既有 review 职责中签发，是一次性、只读、独立的首次 Workmap 接收。新上下文尚未创建、尚未发送、尚未返回。它不新增常驻角色，不授 U2/U3 业务独立审查 PASS，也不允许参与候选形成的人仅通过换聊天获得独立性。

> **R0004 格式纠正说明：**上述句子保留 R0001 签发时点的历史事实。R0003 后来已经完成同一冻结输入的独立阅读并形成真实报告；当前重新使用本任务时，只允许按 R0004 管理决定做一次有限 Return 格式修复。不得重做审查、重写报告、改变 verdict 或把格式修复解释成第二次独立 PASS。

<a id="scope"></a>
## 1. 受托范围

独立阅读下列 exact 管理输入，从 Owner 完整目的而不是文件作者的状态名称，确认一个未参与编写的执行者能否准确恢复：

1. 本轮究竟要检验什么市场业务问题；
2. 固定数据怎样进入 S1/S2/S3、每层证据有什么资格；
3. 为什么必须先从基础行情自主找场景，再核 U2、U3、后续和基线；
4. 广域 raw 与单 Case 完整链分别能回答什么、不能回答什么；
5. 执行 Pro、Worker、管理与 Owner 的生产/消费关系；
6. 哪些旧 V2-01 要求已撤销，哪些正确业务、时间、状态、方法和消费者仍完整保留；
7. 完整任务、局部阻塞、完成条件、触发和真实后继是否一致且可执行。

只判地图/任务/Binding 的可理解性、完整性和前后一致性。不得改写候选，不替管理签预算/采用，不重新选择场景，不核 U2/U3 算法正确性，不审固定计算质量，不签 S1/S2/S3 或 Owner 业务 PASS。发现问题时给出 exact 位置、原文、会造成的具体执行误解和受影响范围；没有问题不凑 finding。

<a id="target"></a>
## 2. 冻结输入

候选输入锁定 `daowei2026/observe-iterate@5e8e4c1bb184a97bfe47bc40493c667bb7b8185d`：

- `runs/BI-01-V2-02/README.md::full`，overview anchors `common/bi01`；
- `runs/BI-01-V2-02/00_长程推进地图.md::full`，anchors `goal/stage/evidence/progress/remaining/management/next`，blob `368681d65d2196b3cc52180da1a1d74b889db85f`；
- `runs/BI-01-V2-02/01_当前任务.md::full`，含 `#question-work-binding`，task_id `BI01-V2-02-S123-SCENE-OBSERVATION-01`，blob `8f90121bd9d1657992313b6c9a78d44fcd3a546f`；
- `runs/BI-01-V2-02/reviews/management-R0001/DECISION.md::full`，blob `6335c8964f545a74e24d9bf68008dbad4eecc90a`；
- `runtime/config/WORKMAP_BINDING.json::full`，当前必须仍为 `NOT_CONFIGURED`；
- `runs/BI-01-V2-02/OWNER_START.md::full`；
- `professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`、`07_BUSINESS_SCENE_OBSERVATION_METHOD.md::full`，以及地图/任务列出的适用 01—06、DR14、Overlay13、Workmap 工具合同。

管理候选之后的 reader task、provenance、Return 或进度提交不重新定义业务输入。实际发送前，操作端必须核上述业务输入没有实质漂移；如 map/task/decision/Owner/rules 改变，以新有权输入重新绑定，不能拿旧报告冒充新报告。

<a id="focus"></a>
## 3. 必须恢复和挑战的承重点

以下是容易误读的承重关系，不是只检查这些关键词：

- 业务链是“U2/U3 原问题 → 基础行情自主选位置 → U2 位置/成员 → U3 四束当时差异 → 后续支持/反证 → 基线增量 → 行动”。
- 广域基础行情、C0/N/C1 raw 与单一完整参考 Case × 五 As-Of 是互补证据面；raw 不是正式 Cluster，五 As-Of 不是五个 Case。
- 两成员 raw 才能在固定三品种 Universe 内观察第三对象；三成员 raw 和完整 Case 都不能制造非空组外优势。
- U3 四方面是四个 Movement Evidence Bundles，不是四类 Allocation Evidence；R02 只是客观路径事实，R03 全部 Withheld。
- `WorkingSoFar/Completed`、实际 bar 数、raw price 单位、actual/confirm/known/As-Of 必须进入可比性，不允许单数值直接排名赢家。
- `OBSERVATION_SCOPE` 是首发 mode，不缩掉 S2/S3；首个场景可尽快进入 S2/S3，但不成为主动停点。
- 执行 Pro 可在具名场景后签 Worker 工单；Worker 只做图、同源数据及普通工程修通，不签业务判断。
- 不重算/替换固定包，不预设场景类别/阈值/配额，不先清仓库，不建设视觉链，不修改 aidata 现有分支，不在观察仓另造图工具。
- 旧 V2-01 的任务、Workmap、Reader、Gate、R10、选样与完成状态全部退出；原 I1— I3 业务 Source 和经核版本的技术图/数据并没有被删除。
- `WORKMAP_BINDING.json=NOT_CONFIGURED` 是当前正确状态，Reader PASS 也不自动等于 ADOPTED；仍需真实 snapshot/Intake/check/dispatch。

需要核是否存在“管理正文宣称撤销，而任务/Binding 又继续要求”的相反正文；也要核是否因强调新方法而误删了 Owner 要求的正确业务字段、状态、时间、方法或消费者。

<a id="coverage"></a>
## 4. 输出与 verdict

将完整只读报告交到：

`runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md`

报告至少记录：

- 本次真实 invocation/recipient；
- 实际读取 commit、task blob、map/decision/config 身份；
- 是否未参与候选形成；
- 你恢复出的完整业务关系与真实后继；
- 每个实质歧义的 exact 位置、误解方式和影响；
- 未读、不可得、超出本次资格的部分；
- verdict。

verdict：

- `PASS`：在当前狭义 Workmap 可理解性范围内，没有会改变执行方向或责任边界的实质歧义；
- `REPAIR_REQUIRED`：存在会使执行者做错业务问题、证据范围、职责、停点或后继的实质歧义；
- `INSUFFICIENT_EVIDENCE`：输入不全、发生漂移、独立性不足或无法取得必要正文。

`PASS` 只覆盖这次地图/任务可理解性，不覆盖固定数据正确性、场景选择、U2/U3 业务结论、S3 完成、管理 Gate、Owner 接收或生产资格。

<a id="completion"></a>
## 5. 完成、预算与非循环性

预计一次有效独立 review 回交完成本受托范围，不强制 PASS。真正缺输入或实质判断未完则如实接续，不以补字段冒充完成；不扩成全仓审计或算法验收。

本受托事项不另设 RESULT/CHANGE/EFFORT 循环。主业务的持续复看由专业任务 Binding 和管理责任承担。纯 Return 缺件可有限补交；相同交付错误一次补交仍失败，回管理接管。

<a id="same-work"></a>
## 6. 只读续作

只继续相同 exact 输入上尚未实际阅读/判断的部分，保留已成；不得修改候选、切换为专业执行、重新选择场景或重做已完成的独立判断。输入若实质改变，不再沿用本任务的旧 verdict。

<a id="accept"></a>
## 7. PASS 后的合法消费

完整回交运输回原操作端/管理路由。只有在：

- 实际 Reader 报告可取得；
- exact reader-input 未变；
- verdict 为狭义 `PASS`；
- 独立性、ROLE_RETURN、QUESTION_WORK_RETURN 完整；
- 既有 `workmap_gate.py snapshot/check/dispatch` 真实通过；

操作端才可按 R0001 管理 `DECISION.md#reader-decision` 机械形成 `runs/BI-01-V2-02/reviews/WORKMAP_INTAKE_CURRENT.json`，将 config 从 `NOT_CONFIGURED` 转为 `ADOPTED`，再准备专业首发。不得由操作端把 finding 改判为 PASS，不得把 Reader PASS 写成专业业务 PASS，也不得以 Reader 任务存在声称 Intake 已发生。

<a id="decide"></a>
## 8. 歧义、漂移或权限问题

路由到 `chatgpt:细节叙事生成_金标:BI01-V202-管理`，M-REASSESS。带 exact 输入、具体歧义/漂移、影响的工作和消费者、已读范围与未完。管理负责定向修 map/task/Binding 和重新采用；Reader 不代写候选，不把局部问题扩大成全历史审计。

<a id="parent"></a>
## 9. 父关系

本任务是新 `BI-01-V2-02` 首张 Workmap 的首次独立只读接收，`parent.status=NOT_APPLICABLE_NEW_CASE`。旧 V2-01 Reader 资格不继承。本任务不取消 BI-01 完整管理与专业责任。

<a id="question-work-binding"></a>
## 10. QUESTION_WORK_BINDING

R0002 首次补齐的 Binding 使用了未受控题号 `WORKMAP-READABILITY`。R0003 已完成实质阅读后，操作端在真实 schema 校验中发现该题号无效。以下 Binding 由 `BI01-V2-02-R0004-20261018T143706Z-4e789f60` 纠正为 DR12 固定题 `AUDIT`，并把当前调用严格限制为原 Reader 对既有报告的一次 Return 格式修复。原业务输入、报告和 verdict 均不因本格式纠正重做或改变。

```json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
    "path": "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md",
    "selector": "full"
  },
  "plan_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
    "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
    "selector": "#reader-pre-adoption"
  },
  "full_scope_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "e3d65aa5131be591416b861343afa9953eaf6661",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
    "selector": "full"
  },
  "batch_result": "保留 R0003 已完成的独立报告和狭义 PASS，仅以 DR12 固定题 AUDIT 补交一个新 invocation 的合法 ROLE_RETURN 与 QUESTION_WORK_RETURN，纠正原 Binding/Return 的题号连接；不重读、重写或重判 Workmap。",
  "question_ids": [
    "AUDIT"
  ],
  "professional_mode": "INDEPENDENT_REVIEW",
  "focus_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
    "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
    "selector": "#reader-return-repair"
  },
  "coverage_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
    "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
    "selector": "#review-scope"
  },
  "source_reads": [
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runs/BI-01-V2-02/README.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "保留并核对 R0003 已读的 frozen overview；不重新解释业务",
      "reuse_evidence": {
        "repo": "daowei2026/observe-iterate",
        "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
        "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
        "selector": "#review-target"
      }
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runs/BI-01-V2-02/00_长程推进地图.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "保留并核对 R0003 已完成的完整业务地图阅读",
      "reuse_evidence": {
        "repo": "daowei2026/observe-iterate",
        "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
        "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
        "selector": "#review-scope"
      }
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "保留并核对 R0003 已完成的专业任务和 Binding 阅读",
      "reuse_evidence": {
        "repo": "daowei2026/observe-iterate",
        "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
        "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
        "selector": "#review-scope"
      }
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runtime/config/WORKMAP_BINDING.json",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "核当前 frozen Workmap 仍为 NOT_CONFIGURED 且 reader input 未变",
      "reuse_evidence": {
        "repo": "daowei2026/observe-iterate",
        "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
        "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
        "selector": "#review-target"
      }
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "04fea2ae48eb6bb50144e2b8b2e3fccca17ec7ea",
        "path": "runs/BI-01-V2-02/OWNER_START.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "保留 R0003 已核 Owner GO、旧运行暂停和新 run 权限边界",
      "reuse_evidence": {
        "repo": "daowei2026/observe-iterate",
        "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
        "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
        "selector": "#review-target"
      }
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "177e81a32203665cb86ea04e8155dd030782c697",
        "path": "runs/BI-01-V2-02/reviews/management-R0001/DECISION.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "保留 R0003 已核的管理采用、撤销、预算和专业后继",
      "reuse_evidence": {
        "repo": "daowei2026/observe-iterate",
        "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
        "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
        "selector": "#review-target"
      }
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
        "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "取得已完成的独立报告、PASS、独立性、材料使用和资格边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "f0bb3089da99bf9664c1f0c45fb058a292cb5f9f",
        "path": "runs/BI-01-V2-02/provenance/turns/R0003/BINDING_FORMAT_CORRECTION_REQUIRED.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "取得原 Binding/Return 题号格式失败和合法修复责任",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "f0bb3089da99bf9664c1f0c45fb058a292cb5f9f",
        "path": "runs/BI-01-V2-02/provenance/turns/R0003/TRANSPORT_PROVENANCE.json",
        "selector": "full"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "取得原全文与两份 Return 的字节身份、schema 失败路径和未采用状态",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "f0bb3089da99bf9664c1f0c45fb058a292cb5f9f",
        "path": "runs/BI-01-V2-02/provenance/turns/R0003/ROLE_RETURN.json",
        "selector": "full"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "取得已通过 schema 的原 review Role Return 并保持历史",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "f0bb3089da99bf9664c1f0c45fb058a292cb5f9f",
        "path": "runs/BI-01-V2-02/provenance/turns/R0003/QUESTION_WORK_RETURN.json",
        "selector": "full"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "取得只在 question_id 上失败的原 QWR；不得倒改",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
        "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "取得固定题 AUDIT 的管理裁定、有限修复范围、完成条件和采用授权",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/dual_route_execution/DR12_PROFESSIONAL_QUESTION_CATALOG.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "核 AUDIT/INDEPENDENT_REVIEW 是已有固定审查题，无需造 CASE",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "核固定题、Binding、return_repair 和历史不倒改合同",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/overlay/tools/question_work.schema.json",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "以锁定 schema 校验 AUDIT Binding 与新 Return",
      "reuse_evidence": null
    }
  ],
  "deliverables_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
    "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
    "selector": "#repair-deliverables"
  },
  "completion_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
    "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
    "selector": "#repair-completion"
  },
  "budget_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
    "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
    "selector": "#reader-pre-adoption"
  },
  "routes": {
    "same_work": {
      "recipient_role": "review",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
        "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
        "selector": "#reader-return-repair"
      }
    },
    "accept": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
        "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
        "selector": "#accept-after-repair"
      }
    },
    "decide": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
        "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
        "selector": "#decide"
      }
    },
    "return_repair": {
      "recipient_role": "review",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
        "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
        "selector": "#reader-return-repair"
      }
    }
  },
  "triggers": [],
  "explicit_no_trigger_reason_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
    "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
    "selector": "#reader-pre-adoption"
  },
  "parent": {
    "status": "PRESENT",
    "ref": {
      "repo": "daowei2026/observe-iterate",
      "commit": "485a796b1d709be81957f25851e62e8c56ddd688",
      "path": "runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md",
      "selector": "full"
    },
    "reason_ref": {
      "repo": "daowei2026/observe-iterate",
      "commit": "af50358f6de756d56759bc004baacf7ed596a2d0",
      "path": "runs/BI-01-V2-02/reviews/management-R0004/DECISION.md",
      "selector": "#parent"
    }
  },
  "question_definitions": []
}
```
