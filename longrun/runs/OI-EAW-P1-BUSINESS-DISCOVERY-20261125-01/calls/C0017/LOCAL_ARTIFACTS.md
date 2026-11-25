# 本地冻结材料入口

根目录：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0017/`。ARTIFACT_INDEX.json给每项绝对/相对路径、bytes、SHA256；索引自身哈希由publication/RETURN_HANDOFF.json给出。

|内容|入口|
|---|---|
|本C正式原件|sources/INVOCATION.json、DELEGATION.json/.md、MANAGER_C0016_PRO_RETURN.json|
|原生问题/既有暴露|selection/R3_BASIS_FROZEN.json|
|同批来源/计量/完整性核查|report/SOURCE_AUDIT.json、RECEIPT_FIELD_CHECK.csv、SUPPLIED_FIELD_COVERAGE.csv|
|4个已暴露PG的12行回查|report/REUSED_QUOTE_ROWS.csv、REUSED_CASE_SOURCE_CHECKS.csv；CSV含原始file/行/asset_key|
|旧条件统计原件依赖|report/REUSED_CONDITIONAL_EVIDENCE.json；不作为本C新复现或已认证撤单计数|
|已有语义/不新增试查的决定|R3_DESIGN_POSITIONING.md、report/MINIMAL_INFORMATION_DECISION.json、report/R3_RESULT.json|
|核验及实际修正|report/VERIFICATION_EVIDENCE.json、METADATA_CLASSIFICATION_CORRECTION.json、EXECUTION_NOTES.md|
|准确来源、使用记录和代码|SOURCE_INDEX.json、report/SAMPLE_USE_CUMULATIVE.json、research/audit_sources_r3.py、assemble_records.py|

无新深入案例/图/未来价格实验；12行回查的原完整案例及图分别在C0009/cases/B2-05-B、B2-06-B和C0015/cases/R2-01、R2-04，对应上游ARTIFACT_INDEX仍有效。复用不当新独立市场复现。旧原件不改、不重跑生成器。

原包data只读，正式版本/receipt/独立方向/完整publication等局部待证如实保留。冻结索引不含会继续更新的进度、发布日志、Return/本地V2自检；这些事实由PUBLICATION_READBACK.json和publication/RETURN_HANDOFF.json另行记录。
