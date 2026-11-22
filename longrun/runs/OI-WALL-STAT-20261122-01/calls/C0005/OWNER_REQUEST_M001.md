# C0005｜M001 Owner 确认项索引

本文件整理并索引 executor 已发布的原提案，不替换原提案，也不表示批准。当前决定状态仍为 `PENDING_OWNER_CONFIRMATION`；本 C 的 `owner_request_ref` 保持指向原 M001 正文。

原件：

- 正文：`daowei2026/observe-iterate@af85146d2b314b4fbad14929a05df347507b2c27:longrun/runs/OI-WALL-STAT-20261122-01/artifacts/D002/MODIFICATION_PROPOSAL_M001.md`
- 字段与验证方案：同提交同目录 `MODIFICATION_PROPOSAL_M001.json`，`proposal_id=MP-WALL-M-INPUT-20261122-01`。
- 失败、诊断与读回证据：同提交的 `M_FORMAL_FAILURE.json`、`M_INPUT_DIAGNOSTIC.json`、`INDEPENDENT_READBACK.json`。

原提案的具体问题为：

> 是否批准本MP的严格空占位处理，更新正式代码锁，并按原范围完整重跑rb/m及G？

本项需要 Owner 权力的原因是正式输入处理将改变。原 Owner GO 明确要求 `ModificationProposal → 影响范围和验证方案 → 回 Owner 确认 → 确认后才实施、提交和采用`：

`daowei2026/observe-iterate@6ba49120d4b620b48c93c76bc9dcdbafc3bf357c:longrun/runs/OI-WALL-STAT-20261122-01/OWNER_START.md`

当前正式生产、品种、年份与默认参数已有授权；这里等待的是 M001 的具体输入处理选择。

已成立的当前证据：m 的锁定默认正式入口真实失败，异常为 `2021-03-12` 前覆盖不连续 `1792800 != 1792801`，尚无合格 m 结果。三自然日诊断窗为 124,200 行，识别 1 条未覆盖且五个报价字段全空的行 `2021-03-11 21:00:00.500`；候选隔离排除该行后剩余 124,199 行、分块通过，保留字段逐值一致、原 frame 哈希不变。此诊断只覆盖该窗口，不是全年“17 行”已验证，也不是正式过滤或 m 生产成功。

原候选仅涉及 `hf/prel0/wall_assembler.py` 的 Wall 输入包装层：分时段首个半秒五个报价字段全空、下一半秒报价完整才排除，仍拒绝有效行情或其他未覆盖缺口，原始 Sof 不改写。core、默认参数、期限与四类事件合同仍按原提案保持。可审阅 [候选 diff](/dwdhome/fy/BASE_E6_2/.runtime/OI-WALL-STAT-20261122-01/proposals/M001/candidate-wall-input-filter.diff) 为 3,150 字节，SHA-256 为 `6d5fa9068a75922406233e884721a76130255a0594136460d0e5242726b98b1b`；本 C 只核文件身份，与原提案一致，未采用候选。

原提案明确保留的影响：wrapper 源指纹与正式代码锁改变；trace 采样行集合改变，跨特征须按 timestamp/UTI 对齐；删除观测拍可能影响按处理拍递推的基线／计数节奏，不能由保留报价逐值相等推断所有行为不变。符合谓词的全年行数和 source scope 排除时间仍需验证。当前 rb 结果及剖面作为 `6618d4d…` 对照保留，不转作改变后新版本的 Gate 证据。

采用后验证严格沿原 M001 JSON 的 `validation_plan`，逐项为：

1. 核全年rb/m输入，仅排除符合三条件的空占位；有效报价和linear_ts逐值一致；原始Sof文件保持。
2. 保留连续覆盖保护，验证非空/异常缺口仍失败；核完整默认ppdict及派生值未变。
3. 既有D1/D2/D4回归及输入处理定向检查；不改D3暂缓决定。
4. Owner确认正式代码锁后，使用本Run新attempt目录完整运行rb/m2021全年；fields/receipt/config/hash及独立Dao逐行读回。
5. 重新完成两品种G，复验已知问题并保留NOT_EXPOSED范围；不将本次部分rb剖面升格为新版本完整结论。

原提案的其他选择为保持 `6618d4d` 及 m 阻断，等待 Owner 指定已认可的规范输入处理／版本，或由 Owner 确认另一个明确输入合同。本 manager 不代选、不把未答复当批准，也不缩减正式范围。

controller 按本 C 回交转交原提案与此索引，不能代作专业采用判断。只有真实 Owner 决定形成准确来源后，才在新的合法接续中安排获确认内容的实施、正式锁与 X/G 回环；本 C 不签发这种执行工作。
