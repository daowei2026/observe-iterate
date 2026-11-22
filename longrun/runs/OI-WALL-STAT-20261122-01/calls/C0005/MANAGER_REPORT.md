# C0005｜消费真实部分 X/G 与 M001 Owner 请求

已消费本 C 指定的 C0004 真实回交。rb 的锁定版本正式生产、独立读回和已支持 G 是当前有效的部分成果；m 的锁定正式入口真实失败。原回交 `WAITING_OWNER`、原生 `GlobalProfileGate=BLOCKED` 与 M001 未批准状态均保持。整项 D002 和 rb/m 闭环尚未完成。

当前来源为：

- 本 C 派工：`daowei2026/observe-iterate@65ec07cdd713836a6454cc25beba36d34ad9f789:longrun/runs/OI-WALL-STAT-20261122-01/calls/C0005/FULL_ASSIGNMENT.md`；其明确当前没有 M001 批准，最新 Owner 继续原文逐字保留。
- 实际 Return：`daowei2026/observe-iterate@8e74efe8b62a60cb25d5e27671159e8d4958e8dd:longrun/runs/OI-WALL-STAT-20261122-01/calls/C0004/PRO_RETURN.json`。
- 原生 G：`daowei2026/observe-iterate@af85146d2b314b4fbad14929a05df347507b2c27:longrun/runs/OI-WALL-STAT-20261122-01/artifacts/D002/FeatureGlobalBehaviorProfilingResult.json`。
- 原 Owner 请求：`daowei2026/observe-iterate@af85146d2b314b4fbad14929a05df347507b2c27:longrun/runs/OI-WALL-STAT-20261122-01/artifacts/D002/MODIFICATION_PROPOSAL_M001.md`。

本 C 依据原专业产物消费可用范围，没有重新读 Feature 源码、重跑 rb、重算统计或重做理解。

| 已消费事项 | 准确范围及状态 |
|---|---|
| 源与实例 | 正式调用来自锁定 TIS `6618d4d147d6ebbe634e61facddf2c9a0b996982` 的隔离检出；44 份已加载 tracked 源字节匹配、28 项默认 ppdict 保存回读。原工作树差异未被采用 |
| rb 正式 X | 本 Run 新生产，243 个交易日、9,959,400 个输入拍；6 张原生表经独立进程 Dao 逐行逐值读回通过；70,895 个 Wall、335,081 条 occurrence |
| m 正式 X | 实际调用锁定默认入口，因交易日覆盖缺口失败；失败目录不是合格结果，m 缺失不计为零 |
| rb 已支持 G | 已完成该层可读剖面；辅助诊断载体与全部正式事件／trace 等价后用于资格和 checkpoint 统计，未改正式输出合同 |
| finding 边界 | 已验证 rb 的 D1/D2 检查无适用冲突；D4 是固定例及 rb 10,159 个 far End checkpoint 范围，完整逐拍 far 历史仍未暴露，m 未验证。没有全 Run 关闭结论 |
| D3 与新问题 | D3 保持 Owner 暂缓；6,847 对仅是 rb 已发布几何同位置的薄触 End 后重建子模式，不是全部 D3。已验证 rb 无新高置信结构 finding；场景寿命问题仍只是原队列候选 |
| 整体绑定与 Gate | FeatureRunResultBinding、StatisticsInputReadiness 及统计覆盖均为 PARTIAL；原 GlobalProfileGate 为 BLOCKED。没有 FeatureReleaseGate／ReleasePackage 完成结论 |

原 C0003 的加载一致性待核已由 C0004 的精确隔离加载证据推进；不能继续用陈旧“尚未加载／未生产”状态，也不能把这个推进等同 m 输入处理已获采用。当前真正需要 Owner 权力的是 M001：正式 Wall 输入包装层的严格空日历占位过滤会改变输入采样与 wrapper 指纹。三日诊断通过不代替全年验证，也不代替正式采用确认。

本 C 在 `OWNER_REQUEST_M001.md` 整理原提案的具体 Owner 问题、现象与影响、已验证候选身份、原验证方案和替代选择。原 M001 md/json 及候选均不改写；`owner_request_ref` 仍指向原 md。采用后验证方案直接取原 JSON，不另写专业方法：全年两品种输入保持与异常保护、默认参数、D1/D2/D4 定向及回归、正式新锁和新 attempt 的完整 rb/m X、独立 Dao 读回、两品种 G 与未暴露边界。新锁会使当前 rb 旧版本成果仅作对照，不能作为新版本 Gate。

资源事实来自同 `af85146d2b314b4fbad14929a05df347507b2c27` 的 `RESOURCE_AND_WRITE_SUMMARY.json`、C0004 `STATUS.json` 与回交：主生产及辅助进程已退出，两次本 Run heavy lease 均已释放，没有后台正式生产留给 manager。`business_control/RESOURCE_STATUS.md` 记录该证据范围、当前成果目录和下次准入边界；不将它扩大为整个工作区／其他 Run 的实时释放证明，不改写原 RUN_RESOURCE_BINDING。

Owner 要求的七项进度已更新：D001 最小核对保持已接收；X 已开始但未全量完成；本 Run 新生产而非旧结果复用；正式进程确实运行过、据 C0004 证据当前已退出；rb 有有效 full_dir，m 只有失败现场；G 已开始且只完成支持的 rb 层；m 输入处理待确认 M001 是实际阻断。完整 rb/m 范围、默认参数、Calendar 与 SOF 不变。

当前没有 M001 批准，不签发把候选输入处理当作已批准的 D 或正式生产。本 C `issued_delegation_refs=[]`、`issued_order_refs=[]`、`accepted_worker_refs=[]`，`professional_state=WAITING_OWNER`；剩余范围及合法接续具名保存。controller 只转交原提案给 Owner；manager 不向其他聊天发送消息、不创建线程。已有有效成果保留，不重复当前锁定版本已完成的 rb 工作。

发布顺序为本 C 报告、确认项索引、资源／进度及剩余范围先提交推送，再独立发布引用已有精确对象的本 C PRO_RETURN。协议身份与记录权限按原 schema、原 Binding 和 CODEX_NATIVE_DIRECT 核实；锁定 gate 的既有身份兼容问题继续如实保留，不伪造物理回执或 PASS。

本 C 的 Binding、C0005 Invocation、C0004 Return 三对象通过原 schema；manager 本次只使用原 `run_record_write`。原 gate 的 `validate-binding` 实际退出 2、首行仍为 `BLOCKED: bad manager logical identity`，完整输出存于本调用 `checks/LOCKED_GATE_VALIDATE_BINDING.txt`。M001 原 JSON 已由 GitHub connector 按精确提交读回并逐字核对；五项原 validation_plan 均保留在确认项索引中。
