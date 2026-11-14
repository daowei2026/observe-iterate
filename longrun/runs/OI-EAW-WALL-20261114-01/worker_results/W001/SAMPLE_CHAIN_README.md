# W001 真实局部链说明

本文件说明 `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/SAMPLE_CHAIN.jsonl`。它有 **3 条真实物理数据记录**，不是新测试 Run，也不是当前源码的通过证明。

- 产品原件：`/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/2020-12-01 21:00:00~2021-02-22 20:00:00/EawP1WallLifecycleFrp/1/c/b/0/c/1/4/44aea11813b85d33becc06242f43621b6/rb.night_end_at_2300`。
- 同身份上游：`/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/2020-12-01 21:00:00~2021-02-22 20:00:00/WallAssembler/8/8/5/1/d/6/1/b25bd29dd0d30a972dfabd41edcdf0518/rb.night_end_at_2300`；receipt schema `wall_lifecycle-v1.6.1`，receipt code version 原样保存在每条 sample 的 `version` 中。
- 对象/日历：上游 receipt 为 `rb / night_end_at_2300`。Wall 局部号为 1；当前 canonical `FeatureRunIdentity` 没有从旧产品中取得，显式 null 并给 reason。
- 旧产品物理类型：`MulWrap P1WallOccurrenceStorage`、`MulWrap P1WallCurrentStorage`、`MulWrap P1DiagnosticStorage`。产品自身生成 code version 没有回执，不用当前 HEAD 补齐。

| 原物理行 | writer 触发 epoch 的 ISO Z 数值表示 | stored change | stored current | stored UTI |
|---:|---|---|---|---:|
| 0 | 2021-01-14T09:04:10.000000000Z | started | present | 72335299 |
| 1 | 2021-01-14T09:04:11.500000000Z | band_updated | present | 72335302 |
| 2 | 2021-01-14T09:04:14.500000000Z | ended | ended | 72335308 |

第一条 band/core 为 4270；第二条 band low 为 4269、core 约 4269.8527778236985，属于确有数据变化的 BandUpdate。第三条上游 sparse 的 band low/high/core 均为 4269，而旧 occurrence 的对应数值均为 0，measurement 为 `not_present`。这些差异原样保留，不把零自动当作缺失，也不由 Worker 判为实现错误。该链未出现 Dormant/恢复；未寻找或合成全场景链。

额外物理校验见 `evidence/CHAIN_RECONCILIATION_VALIDATION.json`：短窗三路全部 root `mul` list references 都与 firing 行号精确顺序一致，排除了未检查 root pointer 就直接套用 anchor 的歧义；样本的 source path、localNo、UTI 和 trigger timestamp 精确对齐。此项另读 240,424 bytes。

抽取使用 `bounded_dba_reader.py`（仅 Python 标准库、所有数据 open 为 rb）。DBA header 按 `pydim/dim/rt.py:69` 的 24-byte `<iiiiq` 验证 offset、item size、有效长度与容量；Text 使用 `pydim/dim/dbas.py:14` 的 anchor/payload UTF-8 规则。按 list anchor 把 value row 对到 firing row；每条保留 occurrence ref 和 payload、同 firing 的 current update、全部 diagnostics 时间列上的同 firing 计数、同 Wall/UTI 的 sparse 与 packed row。upstream trace 通过有界二分 seek 后再核 exact UTI；只声明找到的真实点，不由未命中推断不存在。

抽取读取 1255773 bytes；有 4 MiB、18 秒、90 文件上限。被读文件的 size/mtime 在探针前后均一致。trace 是 WallAssembler 上游状态，**不是 FRP DSU 完整 active map**；后者明确缺失。没有从 current update 缺行补状态。

三条链的同 firing diagnostics 均为 0；这是精确时间对齐范围内未观察到诊断，不表示整份 diagnostics 为空。短窗整体另有 328 个 diagnostic firing，前三条实测为 ingress / InvalidNumericDomain / wall_band，要求 `band_lo <= core_price <= band_hi`。这些样本不证明错误分支正确。

初次严格 JSON 写出遇到原始 IEEE NaN 而失败，留下的空文件保存在 `evidence/460-SAMPLE_CHAIN.empty.failed`。修正只做 JSON 表示：原始 NaN 写为 null，每项在 `nonfinite_stored_values` 保留 JSON 路径、`nan` 原值表示及原因，未插补数值。重读后生成本文件所述样本。失败和修正命令均在日志内。

时间说明：ISO Z 由文件中 epoch ns 做数值转换；未核交易所当地时区解释。`p1WallLifecycleOccurredAt` 的 Int 在这 3 条记录与上游 UTI 精确一致，不称其为 epoch actual time。独立 actual/confirm/known 字段未取得，均为 null 加 reason。

这只是可复核的历史物化局部样本。E1 决定能否复用、还需哪些材料；Worker 不判断业务合理性、冻结资格或正式接受。
