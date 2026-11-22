# C0001｜来源、角色与授权核对

## 采用原件

派工 FULL_ASSIGNMENT、INVOCATION、Owner GO、Binding、资源绑定、BusinessTaskInput 与采用合同均按 packet 的 exact ref 读取。逐字节与 SHA-256 核对见 SOURCE_AUDIT.json。Owner 原文在 OWNER_START 中逐字保留；每项 Binding.grants.authority_quote 均可在该真实 GO 中找到。

## 同版 schema 与原生 profile

使用 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:longrun/contracts/longrun_schema_v2.json` 的 Draft 2020-12 定义核验 binding、invocation、delegation：均通过。依据同提交 CODEX_NATIVE_EXECUTION_PROFILE 和 PRO_MANAGER_GUIDE 以及本 C 原件，manager 为 `codex:OI-F800-STAT-20261122-01:manager`，D001 发至 `codex:OI-F800-STAT-20261122-01:executor:E1`、回原 manager，workers=[]；E1 仍待 controller 新建，未伪造物理绑定或送达回执。

D001 的 operation 为 Binding 已授权项的子集；allowed_writes 为相应 grant 已有工作区与本 Run 路径。Owner 已允许主控分配独立 Run 身份和记录路径；这些 operation 编码与路径映射不增加 Feature 修改权限。D001 只委派 U 的原生专业工作。

上述来源/身份/权限核对不证明 E1 已创建、模型/effort 已独立回读、工作区/缓存/数据库已取得实时独占，亦不证明专业结果。真实设施与派发前检查继续由 controller/executor 按原 profile 执行。

## 原机械工具实际结果

原工具 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:longrun/tools/longrun_gate.py` 与导出文件字节一致，未修改。实际执行 validate-binding，退出码 `2`；stdout 与 stderr 原样分别保存在 GATE_BINDING.stdout.txt / GATE_BINDING.stderr.txt，输入在 GATE_BINDING_SNAPSHOT.json。

实际 stderr 首行为 `BLOCKED: bad manager logical identity`。原脚本第84行仅接受 chatgpt manager，与已采用 CODEX_NATIVE_DIRECT 的真实 Codex manager 不兼容；脚本第103—105行还要求 operation、execution_context、每个 allowed_writes 字符串逐字包含在 authority_quote 内，该规则不能表达 Owner 自然语言 GO 下已明确允许的主控作用域分配。后者为原规则静态核对事实，当前调用先在身份处退出，不能称已动态运行到该检查。

按 FULL_ASSIGNMENT 原文继续使用真实 Codex 身份与同版 schema 核验，不更换 manager 前缀、不改 Owner 原文、不补造 receipt、不把该工具结果记录为 PASS。工具不兼容事实随本次 manager Return 交回 controller；它不代表 Owner GO 不存在或需要重复询问已经明确的授权。
