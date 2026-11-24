# 主控多 Run 操作规程 V0.1（待 cgpterm 接入）

> 面向执行主控的操作清单。专业工作的后继来自该 Run 多层 Workflow 运行协调 Chat 依据既定 Workflow 和 Skill 真实结果形成的具名续作／派发；本规程只负责机械发送、接收与核验，不增加专业判断。

## 0. 基本数据

可信原件：真实 Owner GO、每 Run RUN_BINDING.json、RUN_RESOURCE_BINDING.json、C/D/W、已验证物理发送与回执、单 Run action ledger、Workflow 状态/TASK_PROGRESS。

跨 Run 索引：controller/RUN_REGISTRY.json。索引不是第二套 Gate 状态库；其参考采用精确 commit，不能把实时业务完成情况机械复制到索引中。

每 Run 的 OWNER_START.md/GO 指定 Linux 工作区路径；该路径由 Owner 提前准备，不由主控自动创建。派 Worker 的实际线程应绑到该路径；仍须按当前真实采用的 cgpterm 版本核 Worker 工作区与权限，不从文件记载推断已经支持。

## 1. register_run（新 Run）

输入：真实 GO 原文及其精确来源、business_case_id/work_id/run_id、采用源版本、Owner Linux 绝对工作区和已授权操作范围。

动作：
1. 检查真实 GO，不拿模板或旧聊天补权限；检查 run_id 与可信 Run 索引、历史原件是否冲突。同一业务 case 可有多个不同 run_id。
2. **先核路径、后引用新原件**：把拟用 Owner 路径与当前已登记未结束 Run 的工作区做路径及父子包含比较；在实际 Linux Worker 主机核 proposed path 和现存工作区的目录、realpath、基础权限。不能先要求校验一条尚不存在的 Git exact ref。
3. 核准后发布本 Run 的 RUN_BINDING.json、RUN_RESOURCE_BINDING.json；资源绑定必须记录 Owner 实际给的路径与 Linux 核验凭据。回读 GitHub 准确 commit、路径与真实 grants；尚未发任何 C 时也不得伪称消息已送达。
4. 用这些**已经存在的精确提交引用**构造候选 Registry；运行 validate-registry；在实际 Linux 主机上用同一候选 Registry 运行 check-workspaces --on-worker-host，确保不同 Run 不同工作区且不通过符号链接重合。再次核 Worker 实际 cwd、仓库/分支、共享远端写面与授权。
5. 采用受保护/条件 Git 更新发布 Registry 并回读；若发生并发更新，重新读取已核实 facts 再对账重试，不能盲目覆盖。完成注册后才进入待派状态，并按原 V2 的 validate-binding/validate-invocation 准备 manager C0001，实际发送仍走现有运输设施。

输出：已核实 Run 索引及资源绑定；如未满足，输出待核实项，绝不伪造已绑定聊天或已完成发送。

## 2. controller_cycle（调度一次）

新 Run 采用 `AUTONOMOUS` 后，主控只按初始 GO 已覆盖权限与既定 Workflow/Skill 的真实后继派达；不新增运行中 Owner 确认点。授权不足时阻断对应动作并记录可检查的恢复条件，不将它转成逐次审批请求。

1. 加载所有未结束 Run 的可信状态（Registry 只是发现路径）；单 Run 未核实来源时标记未知，先对账。
2. 先接收已到达回执/未知动作核查；原样保留相同消息的幂等消费记录，不重新制造 C/D/W。
3. 构造候选动作：只使用已发布、受权、真实依赖已满足、且已有正式 Workflow 后继或原 Skill 续接依据的准确下一动作。
4. 为每一动作核实原 Run 的物理 recipient、发件身份/token、来源提交、预计写面、工作区和其他非 Linux 共享资源。
5. 有 Owner 明确优先级则按其执行；同优先级按候选入队时间/稳定身份排序。主控不判断哪项分析业务上更重要。
6. 执行一个具备资格的动作并保存真实发送承诺/回执、效果未知或阻断状态；其余候选保持待办，等待下一合法唤起。不得承诺持续后台自动轮询。

这不是一个新的 scheduler 服务；继续复用 cgpterm 已有长任务/运输唤起设施，待后续 Skill 更新真正接线。

## 3. receive_result（回收）

输入：真实物理端送达及原始消息、准确提交引用、接收动作历史。

动作：匹配 (run_id, type, id) 与 token / sender / exact refs；核对应 V2 Return、真实 evidence 和消费状态 → 写该 Run 行动事实 → W 回该 Run 原 executor，executor D 回原 manager（运行协调 Chat），按已定义 Workflow 的准确后继接续；索引刷新不触碰其他 Run 的业务全景。相同已确认回执幂等；来源冲突、UNKNOWN 先对账，绝不自动重发。

## 4. pause / resume / recover

- pause：在本 Run 的执行账本标记有权暂停与范围；只禁止新的相关动作，不取消未核实的在途副作用，也不暂停其他 Run。
- recover：逐 Run 读取 GO、Binding、精确 refs、物理线程、action ledger、工作区；对账 UNKNOWN 与旧占用后才能提出合法派发。Registry 落后时按已验证事实重建，不让其覆盖历史。
- source upgrade：业务 Skill/运行指南升级必须有真实采用授权和版本记录；主控机械升级需确认旧协议的读取兼容；不得悄然重写运行中的采用版本。
- complete：必须根据该 Run 已采用的任务范围、专业 Skill 结果、Workflow 状态和所有相关动作的真实结案证据，绝不能以 Registry 显示零待办直接宣布完成。

## 5. 检查命令

~~~sh
python longrun/tools/multi_run_check.py validate-registry longrun/controller/RUN_REGISTRY.json
# 下条只允许在实际 Linux Worker 主机运行；不能用其他机器的文件系统代替证据
python longrun/tools/multi_run_check.py check-workspaces longrun/controller/RUN_REGISTRY.json --on-worker-host
python -m unittest discover -s longrun/tests -v
~~~

*工具结果为只读的结构/本机目录检查，不联网、不获取锁、不调用模型、不改变 cgpterm Skill，也不能验证 GO 权限、发送回执或 GitHub 当前分支的原子更新。*
