# C0002 executor 报告｜D001 F800 最小当前理解

收件逻辑身份为 `codex:OI-F800-STAT-20261122-01:executor:E1`，原 D 为 `daowei2026/observe-iterate@092819b56eaf3e08764ed23650c0826c0fdadec1:longrun/runs/OI-F800-STAT-20261122-01/delegations/D001/DELEGATION.json`，回交 `codex:OI-F800-STAT-20261122-01:manager`。本 C 沿用该 D 的 `F800-U-001`，CODEX_NATIVE_DIRECT，零 W。

## 本次专业结论

已形成 [FeatureUnderstandingPackage](../../professional/D001/FeatureUnderstandingPackage.json) 和 [最小当前理解/delta](../../professional/D001/FEATURE_UNDERSTANDING_DELTA.md)。原生 `completion_status=PARTIAL`：受影响的对象、身份、时间、材料准入、2Δ 共同性、关闭/修订责任和字段合同已说明；准确实例尚无正式结果，真实引擎加载、原生配置解码和31表可用性待既定 X 验证。主要链足以进入 X，不以旧实例或归档统计冒充本 Run 成果。

关键事实：

- 本轮 FRP 为 `ac1927518ad6105f15ffbe37fea45e4be91ba574`，TIS 为 `2f460d663d821cf2ba25555eda13e78b697d0767`；现场相关 runtime 的10份 FRP 和6份 TIS 文件与锁定 Git 对象逐字节一致。主工作树另有不同 HEAD，不能作为本轮入口。
- 正常 make_features 构造的基线完整 F 参数与锁定 U2/U3 JSON 一致。复制 profile 后保存、重新解析完整配置，唯一差异为增加 observation_multiple=800，method.revision 保持1；delta=600、CalendarUTITick、rb/hc/i、5m、night_end_at_2300、steel、TA_updto20240229_DBA 与三年请求均保留。
- 当前配置 SHA-256 为 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。F800 full_dir 与默认实例不同，当前 fields.json 不存在。历史 F800 另改了 method.revision，不能直接作当前准确结果复用。
- K=800 使观察/首次准入窗口为4000个交易分钟，2Δ实际贴近仍为10分钟；修订尾仍6Δ=30分钟，handoff尾仍为修订终点后18Δ=90分钟。未知Clock等待仍6Δ。期限起点来自最早actual Clock，不从迟到confirm重新起算。
- 沿用已纠正的行情对象口径：原始转折、尺度贴近转折、共同候选组。组Life、组版本发生、成员行、原事件和pair是不同计数单位。F成员不能作为全上游分母；selected事件时间、几何confirm、接收known、组首次准入和revision不能混用。

## 证据与产物

- [SOURCE_AUDIT](../../professional/D001/SOURCE_AUDIT.json)：packet的25个精确来源、Git blob/SHA-256、adopted副本核对及复用材料身份。
- [INSTANCE_INSPECTION](../../professional/D001/INSTANCE_INSPECTION.json)：实际构造路径、源码核对、完整配置唯一差异、SOF/日期、full_dir与未取得的运行证据。
- [configuration](../../professional/D001/configuration.json)、[baseline](../../professional/D001/baseline-configuration.json)：保存并回读的完整参数。来源原件另存 [锁定U2/U3配置](../../professional/D001/inputs/fqv-kline-rb-hc-i.json)。
- [PUBLIC_TABLE_SCHEMA](../../professional/D001/PUBLIC_TABLE_SCHEMA.json)：锁定TIS读口声明的31表字段、dtype、存储路径与enum；当前数据可用性为UNCONFIRMED，未读正式表。
- [inspect_instance.py](../../professional/D001/inspect_instance.py)：本次实际执行的构造检查；[validate_delivery.py](../../professional/D001/validate_delivery.py) 与 [VALIDATION](VALIDATION.json) 保存交付校验及其范围。

构造检查经既有 runtime wrapper 执行，exit=0。没有运行 Feature、全量统计、合理性诊断或修改正式行为；没有读取Q/V产物。构造入口依约生成的Q/V参数对象没有被运行或记为专业成果。实际 ts 程序没有执行，不能把源码等价和Python配置回读说成生产引擎验收。

## 完成边界与回交

本次回交原生状态 PARTIAL；V2 的 `REPORTED_COMPLETE` 仅表示本次委派报告已交付，不宣称 Skill 的全部运行事实、manager消费、父任务、X/G、finding关闭或Release完成。剩余范围见 [REMAINING_SCOPE](REMAINING_SCOPE.md)，原 manager 接续入口见 [CONTINUATION](CONTINUATION.md)。

准确 full_dir 解析到 `/m3varK`，本 D 只读取其 fields 是否存在，没有向其写入；X仍须按Owner/资源绑定核真实写面授权和单写者。旧全量结果与历史finding只保留为线索，本 D没有替其重新诊断或关闭。

当前同版 longrun_gate.py 仍硬编码 chatgpt manager（已在C0001真实报告中记录 `BLOCKED: bad manager logical identity`）。本次按锁定schema及CODEX_NATIVE_DIRECT核身份/权限子集和产物引用，不修改正式协议或身份，也不声称原运行门已通过。物理线程、模型/强度、送达与资源锁仍由controller按真实设施验实。

专业产物先提交并推送取得exact refs，之后独立提交PRO_RETURN。Return引用先前已发布的本报告及接续文件；不引用未来提交。未签发后继D/W，未改manager的TASK_PROGRESS，未创建线程或向其他聊天发送消息。本executor在发布回交后等待原manager消费，不自行执行X。
