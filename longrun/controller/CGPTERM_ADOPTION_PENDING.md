# cgpterm 主控 Skill 后续接入清单（本轮不修改）

本轮明确**不修改 daowei2026/cgpterm**，因为现役主控还在使用。

待改文件：
daowei2026/cgpterm@becfbcbc7eec3e4fc6a44cd0b0a7a934ec666ff8:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md

只读核实的现役事实：
- 现役步骤按单个 Run 的 GO→C/D/W→原角色 Return 组织；
- 现役 Linux 目标文字固定为 /dwdhome/fy/BASE_E6_2；
- 使用 chatgpt-terminal-business-flow、codex-existing-chat-dispatch、long-task-status；不得另造手机/Worker执行器；
- 现役 Skill 已明确没有 observe-iterate V2 自身的持久多 Run 注册/锁程序；
- ChatGPT Pro 项目与 Worker 模型目标仍沿用既有 Owner 规定，本轮不探测模型。

后续实际接入时才做：
1. 让主控在同一实例中读取多 Run Registry 与每 Run 可信行动事实，按 Run 作用域派发和接收；
2. 将固定 BASE 路径改为读取各真实 Owner GO 指定的独立 Linux 工作区，且不得自动创建、默认为固定路径；
3. 接线本仓 MULTI_RUN_CONTROLLER、CONTROLLER_OPERATIONS 和 multi_run_check.py，对当前 Run 的工作区、身份和远端写面做实际前置核查；
4. 保持原 C/D/W、物理收发、UNKNOWN 对账、业务/机械责任边界不变；
5. 验证多个真实 Run 的交错派发、同编号路由、一个 Run 阻断而其他继续、主控恢复及升级兼容。

**界限：**本仓的协议提交不等于上述现役 Skill 已生效。尤其当新 GO 的工作区不是旧 Skill 的固定路径时，应先完成或明确授权相容的主控接线；不能为了宣称可并行而忽略旧 Skill 的实际限制。
