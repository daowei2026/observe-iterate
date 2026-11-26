# C0020／D010 本地交付入口

工作根：`/dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0020/`。

正式主报告 `EXECUTOR_REPORT.md` 以R2/R1/R3真实业务认识、准确过程/对照、范围、反例、已有联合信息、参考设计、等级和后继问题为主。`EVIDENCE_INDEX.md`给原8包exact索引、69案例、代码/参数/数据及版本已知与未知。`SOURCE_INDEX.json`逐项给43原签输入、3个Manager上下文及旧冻结包来源；`ARTIFACT_INDEX.json`冻结本C详细原件的准确相对/绝对路径、bytes、SHA-256，自身与可变运输事实另列。

|入口|内容|
|---|---|
|`report/FINAL_RESULT.json`|D010实际范围、最强等级、目标部分达成、结束理由、未决项、父Run未完成|
|`report/CANDIDATE_REGISTER.json`|三条线索保留原结果/出处及等级，按影响/证据/成本给后继取证顺序；不签新D|
|`report/COMPLETION_EVIDENCE.json`|S01～S09三入口/三组/逐候选实际覆盖、分母及结束依据|
|`report/CASE_REGISTER.json`|69次旧深入的指标、图/表、PG/日期块与SHA；66PG／19日期块不等于因果独立样本|
|`report/SAMPLE_USE_CUMULATIVE.json`|261旧记录不变、S09追加17来源回查，现278；深入仍69；事件/区间/复查计数单位和暴露区分|
|`report/REPLAY_AUDIT.json`、`FROZEN_FILE_AUDIT.json`、`RAW_FILE_AUDIT.json`|718旧冻结文件和2,924源文件大小/hash，脚本/图结构核查；未重执行旧生产/研究全扫描|
|`report/VISUAL_SPOT_REVIEW.json`|6张既有业务图实际复看；33张全部解码，未称全部PDF逐页渲染|
|`research/S09_LOOKBACK_BASIS.json`、`report/S09_THIRD_ONLY_LOOKBACK.json`|先冻结问题后查全部11个第三入口独占片段/17旧区间，不据未来筛选|
|`report/S09_LOOKBACK_RAW_VERIFICATION.json`|200唯一原始行／258来源行／12源文件的17区间回核PASS，仅量变段不取新future|
|`report/S09_LOOKBACK_RAW_VERIFICATION_ATTEMPT_01.json`、`EXECUTION_NOTES.md`|本C初版研究核查脚本方向映射错误、保留失败和修正说明；不是生产Bug|
|`research/audit_s09.py`、`lookback_s09.py`、`verify_lookback_s09.py`、`assemble_s09.py`、`check_delivery.py`|本C实际只读研究/汇总及冻结复核入口；旧代码不被改写|
|`sources/`|D010、真实C0020 INVOCATION、C0018 Return、C0019未送达记录和43份exact输入、3个Manager上下文|
|`TASK_PROGRESS.md`|持续记录原件、真实动作、已知/受限、下一步与最终交回状态|
|`publication/`、`PUBLICATION_READBACK.json`|实际head/路径/条件意图、写回响应、exact commit读回与父链；最后零W Return及Git交回事实|

旧8包共718项继续位于同级C0002/C0005/C0007/C0009/C0011/C0013/C0015/C0017，由EVIDENCE_INDEX的不可变远端索引进入；不把详细本地表伪造为单独远端ref。Owner原始数据目录只读，所有本C输出在独立研究根，未新增行情或生产重跑。

本地只读复核命令：`python /dwdhome/fy/BASE_E6_2/artifacts/oi-eaw-p1-business-discovery-20261125-01/calls/C0020/research/check_delivery.py`。它检查冻结文件/关键计数/旧使用记录保留，不修改原件。实际producer复现仍受缺相容receipt/正式完整历史限制。

本D完成不代替父Run最后Manager消费/controller归档；真实回交固定C0020/D010身份，remaining_scope_ref=null仅针对D010。报告先发布，PRO_RETURN后引用已发布exact报告。
