# C0001｜controller 接续入口

run_id=`OI-F800-STAT-20261122-01`；当前正式后继是 D001，recipient=`codex:OI-F800-STAT-20261122-01:executor:E1`，return_to=`codex:OI-F800-STAT-20261122-01:manager`。同批 DELEGATION.md/json 由后发 PRO_RETURN 的 issued_delegation_refs 精确绑定。

当前无已发送后继，E1 物理线程尚不存在。controller 回收本 C 的真实 Return 和正式 D001 后，按 Owner GO、Binding、CODEX_NATIVE_DIRECT 和原 V2 核验实际来源、操作权限、专属线程、模型/effort、工作区及当前直接操作所需写面，再创建本 Run 独立 E1、赋予新的真实 C 调用并派发 D001。manager 不占用未来 C 编号、不签 W、不代 controller 创建或发送。

D001 所做 U 与后继 X/G/诊断/Release 均依 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md` 及已采用 Skill。E1 Return 应回原 manager，经 controller 的真实新 C 接续后才消费；目前不能登记已收到/已接受。可继续的 PARTIAL 结果和真实 BLOCKED 结果依 Skill 原文处理，不追加完整旧 A～E 准备 Gate。

锁定 longrun_gate.py 的真实 validate-binding 输出为退出2 / `BLOCKED: bad manager logical identity`，已保留原输入及 stdout/stderr；同版 schema 可接受真实 Codex 字符串。按本 C 明示要求保留真实角色和自然语言 Owner 授权作用域映射，不修改原 gate、Owner 原文或 receipt 来取得 PASS。其逐字 quote 范围规则的兼容问题亦见 VALIDATION.md。controller 须知这是工具限制；manager 的记录不替代 controller 独立物理回执或资源核验。

本 C 交付范围是签发并发布首个 D001、维护状态并回交；发布后结束本 C。后续等待真实 controller C，不建立计时器、轮询、自动唤醒或自行发起专业生产。
