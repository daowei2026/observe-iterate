# 正式启动全新的 **Observe–Iterate V2 长程业务任务**。

**任务身份**

- `work_id`: `OI-EAW-WALL`
- `run_id`: `OI-EAW-WALL-20261116-01`（启动前核实未被占用）
- **唯一分析对象：`EawP1WallLifecycleFrp`**
- 业务任务：围绕该特征开展观察材料准备与业务合理性分析。上游特征只作为必要的输入、处理链和证据来源，不自动扩展为独立分析对象。

**采用版本**

主控 Skill：

`daowei2026/cgpterm@becfbcbc7eec3e4fc6a44cd0b0a7a934ec666ff8:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md`

业务控制面、长程协议及专业 Skill 统一采用：

`daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c`

本轮特征输入位于上述提交的：

`task-inputs/eaw-p1-wall-lifecycle/`

使用其中三个文件：

- `无二义性需求和实现文件.md`
- `设计文件.md`
- `实例运行脚本.py`

这些文件是专业调查依据和可复用运行入口，不预设其中的所有结论已经成立。不要再使用已删除的 `FEATURE_CONTEXT.md`。

**本轮执行要求**

观察材料准备 **步骤 0 按 Owner 指定跳过**，直接从 `control/02` 的步骤 1 开始，不安排完整资产盘点，也不将跳过记录为完成。

管理 Pro 按 Control 中的实际节点输入输出依赖组织工作、接收结果、决定后继。允许必要的复用和合并委派，但不得绕过影响后续工作的专业结果验收。

本轮观察材料应以真实市场数据经过实际业务处理链取得的结果为依据。人工构造的受控输入仅能辅助实现验证，不能替代正式业务观察材料。

**运行环境与授权**

- 管理 Pro、执行 Pro：ChatGPT Project `细节叙事生成_金标`，推理档位 `Pro`
- Worker：Linux `/dwdhome/fy/BASE_E6_2`，`GPT-6.1 Sol Max`
- 优先直接复用 BASE 工作区既有源码、数据和运行环境，不另建复杂隔离工程。
- 管理 Pro 在既定业务目标和实际操作权限内自主推进，Owner 定期检查，不逐项审批。

本 Run 一次性工具授权原文：
```swift
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2

operation=run-record-publish execution_context=github:daowei2026/observe-iterate:runs/OI-EAW-WALL-20261116-01 allowed_writes=longrun/runs/OI-EAW-WALL-20261116-01
```

授权限于本 Run 必要工作，不包括破坏性 Git 操作、覆盖现役正式成果或修改无关文件。按 V2 协议绑定实际工具权限和执行身份。

请创建全新 Run，派发管理 Pro 接管，按照业务 Control 组织专业执行、节点验收、M→R 交接、合理性分析及完成全景更新，持续运行至符合业务完成条件或有依据的阻断。

不复用旧 Run 的完成状态，不另安排测试 Run。
