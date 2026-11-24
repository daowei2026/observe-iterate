# AttackFlowAssembler 首轮理解包

本包采用专业控制 `9877826236e0995e7255e6cbfedc2d1b89dea6da`，理解 TIS `179016111ed0394f92025313e46bd13534932a74` 的当前 `attack-default`。原生状态为 **PARTIAL**：核心模型已说明；当前版本正式结果字段可读性尚未确认，X 可继续、G 尚无有效输入。

详细原生记录见 [FeatureUnderstandingPackage.json](FeatureUnderstandingPackage.json)，未确认与接续范围见 [REMAINING_SCOPE.md](REMAINING_SCOPE.md)。

| 正式产品 | 当前实现中的业务角色 | 自身发生位置与身份 |
|---|---|---|
| attack_segment | 已完整形成的攻势段；主输出 | closed_at；本source run的segment_id；两个明细流是同一payload附件 |
| attack_formation_evidence | accepted、unresolved、gap、无accepted区间、availability与能力声明；中间处理产品 | 点位置或区间末端；全结果排序后的formation_local_id |
| wall_relation_barrier | 正式关系屏障；当前仅来自Wall.End | 源Wall.End位置；全结果排序后的barrier_local_id |

Attack 先按 exact Wall/F4 取输入，同侧 Wall 事件同 UTI 的 F4 进入 unresolved 材料；其余 F4 在同半秒方向材料上合并资格，金额/量须一致，family grade 取最高。Alive Wall、对应方向成交价与 Wall core 距离通过后形成 atom。首 atom 开段；后继 atom 续段，或在最早 wall cut、gap timeout、反向离墙 Tick、Wall/side 切换处关闭旧段。

`business_end` 是最后材料位置，`closed_at` 是真实闭段触发位置。gap 找第一个 UTI 严格大于末材料 UTI 加6的真实 Tick；retreat 比较方向性的 last price 到当前 exact Wall core 的反向距离，严格大于默认派生2跳才触发。它与 `max_retreat_from_best_ticks` 的诊断含义不同。

同材料双lane只累计一次段总量；tactical/structural overlap view允许重叠。F4资格行数、半秒材料次数、唯一段数、形成材料条数和区间长度是不同粒度。DBA同刻多行按 `__occNNNN` 物理分流，业务时间不改；读者须汇集全部流，不能只读基流或按时间去重。

在建段和资格book跨物理chunk传递；chunk_end和全范围结束均不无条件形成完整段。carry、完整atom、chunk summary/checkpoint虽在helper或_frames内存在，当前 `_impl` 的正式 `.F` 只保留三产品流，不能声称它们是现成统计字段。

本次真实构造参数、ppdict/ppid及加载路径见 [instance_introspection.json](evidence/instance_introspection.json)。探针禁用运行入口。对准确构造目录的receipt查询发现：rb的三Attack、Wall和两F4均是其它git代码版本；m的Wall也是其它版本，m的三Attack和两F4位置没有receipt。均未采纳，见 [candidate_receipt_check_summary.json](evidence/candidate_receipt_check_summary.json)。没有运行Feature或读取/统计历史市场结果。

设计来源与实现事实分别保存：原始A3文本的FRP组段/chunk内建议与当前TIS producer组段/carry不同；指定FRP参考期待Attack v1.6.2和attempt/available_at字段，而当前TIS声明v1.6.1且无这些字段；参考段簿实现每次firing重建current view。详见原生包UQ05/UQ06，未将这些差异升级为合理性结论。

本 D 没有修改产品代码，没有生成 FeatureRunResultBinding、GlobalBehaviorProfile、DiagnosisReport 或 FeatureReleaseGate。原 Skill 完成条件核对及缺口均在原生包中，不能把本次交付当作父 Run 已完成。
