# 本地冻结材料核查入口

根目录：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0015/`。ARTIFACT_INDEX.json列每项相对/绝对路径、bytes和SHA256；索引自身hash由publication/RETURN_HANDOFF.json给出。大表、原始提取、图和代码留本地。

|内容|入口|
|---|---|
|正式委派/调用/上游Manager原件|sources/DELEGATION.json、DELEGATION.md、INVOCATION.json、MANAGER_C0014_PRO_RETURN.json|
|问题/暴露与选样冻结|selection/R2_BASIS_FROZEN.json、SELECTION_FROZEN.json|
|全批定向联合记录|scan/JOINT_OCCURRENCES.csv.gz、DEDUP_OCCURRENCES.json、SCAN_SUMMARY.json、QUOTE_INPUTS_USED.csv|
|真实分母、按PG/活动敏感性、既有字段恢复|report/R2_STATISTICS.json、PRIMARY_SENSITIVITY.csv、PG_BALANCED_PRIMARY.csv、BUILD_BALANCED_PRIMARY.csv、EXISTING_FIELD_RECOVERY.csv|
|四例与图|R2_CASEBOOK.md、cases/R2-01～04/、figures/各例.png/.pdf|
|可用P1与原始来源|report/P1_SOURCE_AVAILABILITY.csv、INPUTS_USED.csv、VERIFICATION_EVIDENCE.json|
|43PG两标签与逐行核查|probe/三CSV、report/MINIMAL_PROBE_SUMMARY.json、MINIMAL_PROBE_VERIFICATION.json|
|使用记录与版本来源|report/SAMPLE_USE_CUMULATIVE.json、SOURCE_INDEX.json|
|复现脚本/实际异常记录|research/各.py、EXECUTION_NOTES.md|

不重跑冻结选样或旧根生成器。原始数据目录仍只读；按CSV的source_refs文件/行及manifest/FILE_INVENTORY入口即可核查。研究脚本属于独立计算，没有生产实现变更。formal actual版本/receipt/identity/publication未补齐，参考版本不是其替代。
