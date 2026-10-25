# 固定来源与实际消费关系

本单order/invocation/token/return_to见FULL_RESPONSE文首。R38原三件逐字校验在 `evidence/INPUT_VERIFICATION.json`，场景原件另外保留；未以运输头代原单。

|来源|准确Git定位/用途|
|---|---|
|当前任务/Binding|observe `78cc9a813777b9996d365f8242fc6ca318066972:runs/BI-01-FO-01/01_当前任务.md`，全文沿W09准确未变记录复用|
|M37|`2baa81e2e3235b424f7c6a91a4fa2a3c9df643d3:runs/BI-01-FO-01/reviews/management-R0037/FULL_RESPONSE.md`，本次全文读取，5B限定续作|
|专业方法|`21dd5971f493a6d724948b84dacb7b200ff43b54:professional/feature_observation/README.md`及00—04，准确未变适用正文沿W09已读记录复用|
|R38完整报告|`0cfc9d91e38d3f1aea772726ea72a5a78af6b7c4:runs/BI-01-FO-01/artifacts/professional-R0038/FULL_RESPONSE.md`|
|原工单|`b8d4c45c8d9d127775b1f68524502e1cf34456db:同R38目录/WORKER_ORDER.md`|
|原场景|`91887f0dfff9c4d5d6182bde49124ba0e832323f:同R38目录/TIME_EXPRESSION_PLAN.json`，8847bytes/SHA d2ec28a1fcc8834cfb3969676d6bcfb6d65fa3b9ed8901553d6512407f0b617d|
|W09主Notebook/读取谱系|`35e1836f6a0ef8a123d0441070d3e8e4e760a816:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-BOUNDED-DISPLAY-09/N_observation_Worker09.ipynb`，blob b271fe3541166a1e04d216bd845d59e8f7b25123；本次清旧输出后改版新执行|
|W02正式rb三切点/两品种原价|`081e31241a0c88e47631f80a8b9b8dd43b2b569c:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/` 下 `data/selected_cuts/{before_confirmation,at_or_after_confirmation,final}/`，`data/same_bound_price/rb_5m_price_calendar.csv`及 `data/i_missing_context/i_5m_price_calendar.csv`|
|W03正式i三切点|`d04f3b08892ccf334a06028f3caab994743566a0:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/data/crossk/{i_before_missing_recovery,i_recovery,i_after_recovery}/`|
|旧正确认识|P9 `401b9f37719373978880b8f2893d74864010956c:.../professional-R0009/FULL_RESPONSE.md` C1/C2；P11正文从35e1836f的 `.../professional-R0011/FULL_RESPONSE.md` C1核时间/恢复关系，不恢复旧图资格或任务|
|aidata|基线25a9fd8b1333aafd4c56fd1b288e7f8d3c8c3113；本次独立候选033710194e62dbdcf6a38f0985234a75bb752673；原基础图形配置0.3.0-worker09、本次领域模块0.5.3-worker10、场景0.5.1-worker10分别记录|
|uplot|实际13badc6c079eebe7242abd65e56b328c45dcee2a及preexisting dirty，详情见RUNTIME_BOUNDARIES；手册0a4fcd54059782572a3f7e82fad041121e8c65ad只作能力参考|

正式参数/方法未变：原R30三sources、5m、night_end_at_2300、N6/LOO3、normalization=null、compact_history/core.v2。FRP5154c407249c130a6e048c8541b76dfdec3ea48c、TIS3ff34c72be8ef025f68e18b097fe7b8f1f472668、workerADT cd5c307dcb3483ef76242b5c37177a969c5fcbd2均无写入。本单不实例化产品，因此没有按摘要重拼嵌套配置。

`SOURCE_READS.json` 是当前kernel实际消费的固定源hash清单，`FORMAL_CUT_EXPECTATIONS.json` 保留原标量行和p/k/a/r，`RB_MEMBER_ROLE_CHANGES.json` 保留完整Life、UInt64字符串和原window/child坐标。新数值点仍来自原正式字段，不由本报告数字生成。

场景到调用：rb/i cuts决定允许K；price_start决定显示域但完整K合法原价仍用于原成员投影；optional_panels启用duration/rhythm/waiting_time；`prepare_time_query` 只做本K时间/成员资格注记；`prepare_cut_comparison` 只拼列示原点并形成显示身份；二者都交 `evidence_composition.compose_prepared_display`。事后图共同轴、原K ticker及数值标签偏移在Notebook `finish_comparison_axes`，不改变数据或计算。Notebook不执行sparse/evolution，不将场景JSON键伪称公共API。
