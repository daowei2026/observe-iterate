# 主控多 Run 操作规程 V0.1（待 cgpterm 接入）

> 面向执行主控的操作清单。专业工作的下一步只来自该 Run 管理 Pro 的有效决定；本规程只决定何时/发给谁/怎么复核。

## 0. 基本数据

可信原件：真实 Owner GO、每 Run RUN_BINDING.json、RUN_RESOURCE_BINDING.json、C/D/W、已验证物理发送与回执、单 Run action ledger、manager decisions/TASK_PROGRESS。

跨 Run 索引：controller/RUN_REGISTRY.json。索引不是第二套 Gate 状态库；其参考采用精确 commit，不能把实时业务完成情况机械复制到索引中。

每 Run 的 OWNER_START.md/GO 指定 Linux 工作区路径；该路径由 Owner 提前准备，不由主控自动创建。派 Worker 的实际线程应绑到该路径；使用 cgpterm 旧 Skill 时先确认其已允许本次工作区（当前尚未改动）。

## 1. register_run（新 Run）

输入：真实 GO 原文及其精确来源、business_case_id/work_id/run_id、采用源版本、Owner Linux 绝对工作区和已授权操作范围。

动作：
1. 检查真实 GO，不拿模板或旧聊天补权限；检查 run_id 与可信 Run 索引/原件不存在冲突，同一业务 case 可有多个不同 run_id。
2. 将 owner_workspace_path 加入候选注册表，运行 validate-registry；路径相同、父子嵌套或错误 exact ref 立即阻断。
3. 在实际 Linux Worker 主机运行 check-workspaces --on-worker-host，核目录存在、realpath 重叠、基础访问权限；再通过现有 Worker 设施核实际 thread cwd、仓库分支、写面和 Owner grants。此检查不能替代 Worker 身份或权限。
4. 写入 RUN_BINDING.json 和 RUN_RESOURCE_BINDING.json 并回读准确 commit；更新真实受控 Registry 指向这些来源。条件更新失败就重新读取事实并对账，禁止盲目覆盖索引。
5. 注册已验证后，才按原 V2 的 validate-binding/validate-invocation 准备该 Run 的 manager C0001；实际发送仍走现有手机/ChatGPT 发送设施。

输出：已核实 Run 索引及资源绑定；如未满足，输出待核实项，绝不伪造已绑定聊天或已完成发送。

## 2. controller_cycle（调度一次）

1. 加载所有未结束 Run 的可信状态（Registry 只是发现路径）；单 Run 未核实来源时标记未知，先对账。
2. 先接收已到达回执/未知动作核查；原样保留相同消息的幂等消费记录，不重新制造 C/D/W。
3. 构造候选动作：只使用已发布、受权、真实依赖已满足、且专业管理决定允许的准确下一动作。
4. 为每一动作核实原 Run 的物理 recipient、发件身份/token、来源提交、预计写面、工作区和其他非 Linux 共享资源。
5. 有 Owner 明确优先级则按其执行；同优先级按候选入队时间/稳定身份排序。主控不判断哪项分析业务上更重要。
6. 执行一个具备资格的动作并保存真实发送承诺/回执、效果未知或阻断状态；其余候选保持待办，等待下一合法唤起。不得承诺持续后台自动轮询。

这不是一个新的 scheduler 服务；继续复用 cgpterm 已有长任务/运输唤起设施，待后续 Skill 更新真正接线。

## 3. receive_result（回收）

输入：真实物理端送达及原始消息、准确提交引用、接收动作历史。

动作：匹配 (run_id, type, id) 与 token / sender / exact refs；核对应 V2 Return、真实 evidence 和消费状态 → 写该 Run 行动事实 → W 回该 Run 原 executor，executor D 回原 manager，manager 决定回到该 Run 的准确后继；索引刷新不触碰其他 Run 的业务全景。相同已确认回执幂等；来源冲突、UNKNOWN 先对账，绝不自动重发。

## 4. pause / resume / recover

- pause：在本 Run 的执行账本标记有权暂停与范围；只禁止新的相关动作，不取消未核实的在途副作用，也不暂停其他 Run。
- recover：逐 Run 读取 GO、Binding、精确 refs、物理线程、action ledger、工作区；对账 UNKNOWN 与旧占用后才能提出合法派发。Registry 落后时按已验证事实重建，不让其覆盖历史。
- source upgrade：业务 Skill/专业指南升级是专业授权/管理事项；主控机械升级需确认旧协议的读取兼容；不得悄然重写运行中的采用版本。
- complete：必须使用该 Run manager 的已确认业务完成决定及所有相关实物流和动作结案记录，绝不能以 Registry 显示零待办直接宣布完成。

## 5. 检查命令

~~~sh
python longrun/tools/multi_run_check.py validate-registry longrun/controller/RUN_REGISTRY.json
# 下条只允许在实际 Linux Worker 主机运行；不能用其他机器的文件系统代替证据
python longrun/tools/multi_run_check.py check-workspaces longrun/controller/RUN_REGISTRY.json --on-worker-host
python -m unittest discover -s longrun/tests -v
~~~

*工具结果为只读的结构/本机目录检查，不联网、不获取锁、不调用模型、不改变 cgpterm Skill，也不能验证 GO 权限、发送回执或 GitHub 当前分支的原子更新。*
