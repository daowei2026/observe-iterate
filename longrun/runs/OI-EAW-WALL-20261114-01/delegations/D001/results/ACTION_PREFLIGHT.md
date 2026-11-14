# D001｜Action Preflight

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> source facts：W001 `ACTION_PREFLIGHT_FACTS.md`  
> execution performed：**NO**  
> current decision：**现有 integration runner 不具备直接 G-RUN 资格**

## 1. 为什么仍需要 preflight

W001 已找到并局部解码 historical legacy material；这足以完成 D001 的事实／材料／WORKING 预期基线，但不足以：

- 绑定 current canonical product；
- 验证 matching native reader；
- 观察 FRP active map；
- 验证 Dormant、重复／冲突、同 firing transaction、End 后事件和 late policy；
- 开展冻结 expectation 后的正式比较。

任何新运行都属于 manager 的后继 Gate，而不是 W001 完成后自动获得的授权。

## 2. 现有 runner 的准确性质

入口：

```text
/dwdhome/fy/BASE_E6_2/mquant/tis/test/integration/verify_eaw_p1_real_run.py
```

它要求 fixture，并在 `--execute-normal` 下：

- 要求 `EAW_P1_HEAVY_RUN_AUTHORIZED=YES`；
- 先 Stack build `trade-poc:exe:ts`；
- 依次生成 Wall、两组大单、Build、Attack、Absorb；
- 再运行四个 FRP 产品；
- `--evidence-dir` 只约束回执位置，不保证所有计算产物、Stack cache、task linker、migration log 都在 Run 写面。

结论：

```text
existing runner
≠ wall-only bounded action
≠ read-only probe
≠ current Owner grant 内可直接运行的命令
```

## 3. 当前不采用的窗口假设

三条 historical chain 的 writer firing 仅跨约 4.5 秒，但其 source artifact 目录为：

```text
2020-12-01 21:00:00 ~ 2021-02-22 20:00:00
```

WallAssembler 默认还涉及 `qt_n=30` 日、`w_depth_ref_ticks=1200` 等预热。直接把新运行窗口截为三条 firing 附近会：

- 改变 run identity；
- 可能没有足够预热；
- 不能保证重新产生 localNo=1 或同一 Wall；
- 不能保证上游只加载短窗。

所以本 D 不声称“4.5 秒窗口”是可运行最小窗口。

## 4. 后继动作分级

### A. Provenance recovery（优先、非运行）

目标：寻找 legacy product 的生成 manifest／binary/task record，使 product generation version 与 source artifact 绑定。

最低输出：

```text
product leaf
+ generating task/command
+ binary/code version
+ effective params
+ object/calendar/range
+ product schema
```

停止条件：需要无界检索、凭据、生产数据库查询或越出 Owner grant。W001 已在现有明确路径完成一次有界调查；若 manager 没有新的精确索引来源，不应简单重派相同扫描。

### B. Current canonical isolated material action（需要 G-RUN）

目标：在 current checkout 下产生一个**隔离、wall-only** 的最小可区分材料包。

最低产品：

- WallAssembler receipt、fields、sparse/packed、必要 producer trace；
- current `wall_occurrences / wall_current_view / wall_diagnostics`；
- matching generated wrapper/native read proof；
- FRP full active-map trace或可验证 replay；
- exact binary/code/params/target/calendar/range；
- command/exit/hash/size/time/cost receipt。

这不是现有 runner 原样执行；需有经过审查的 wall-only task 或等价隔离执行路径。

### C. Controlled scenario fixture（需要独立 Gate）

目标不是重放真实行情，而是区分 current lifecycle contract：

1. Present↔Dormant；
2. same-firing duplicate；
3. cross-firing duplicate；
4. same-ref different-payload；
5. legal + invalid same firing；
6. End 后 update/end/Start；
7. out-of-order UTI。

fixture 结果必须与真实行情材料分层，不能冒充自然样本。

## 5. G-RUN 前置条件

在 manager 允许任何 B/C 动作前，至少冻结：

| 前置项 | 必须明确 |
|---|---|
| business question | 本次动作具体区分哪个 expectation/scenario |
| target/calendar | 唯一值及来源 |
| Wall params | 完整 effective values，不用源码默认补齐 |
| source range/warmup | source cut、预热、Session 边界 |
| source/binary | exact commit、binary hash、build status |
| schema/reader | current ADT、wrapper、native reader |
| write surfaces | product、cache、Stack、TMP、task、log、migration 全部隔离 |
| cost budget | metadata、预计输入规模、内存、墙钟、文件数和 stop threshold |
| output contract | receipt、三路产品、A trace、manifest、hash、command log |
| single writer | 真实 cwd/thread/model/effort/lock |
| authorization | Owner grant 子集 + manager G-RUN |

## 6. 安全停止点

任一发生即停止，不进入下一阶段：

- fixture 或 effective params 仍有 `REPLACE`／未知值；
- 运行会自动 build，但 build 未获授权或 cache/write surface 未隔离；
- 会触发 Wall 之外的多产品链；
- source/warmup 可能隐式扩大但无 metadata 预检；
- 输出会覆盖历史目录或写出 Run 写面；
- matching wrapper/schema 仍未生成；
- active-map 观测方式未定义；
- 成本超过预先冻结阈值；
- 任何命令效果未知或回执不完整。

## 7. 最小区分力

### 正常 current chain

一个 current Start→nontrivial update→End chain + O/C/A/D 足以区分：

- current schema 是否可读；
- current update 与 A 的关系；
- End update 与删除；
- End measurement contract。

### Controlled invalid chain

每个高价值异常场景只需最小 occurrence batch + pre/post A + O/C/D，即可区分：

- same vs cross-firing dedup；
- transaction rollback；
- terminal identity；
- late policy。

不需要为这些问题启动全年／全品种运行。

## 8. E1 决定

```text
Run existing multi-product runner now: NO
Issue W002 now:                      NO
Submit bounded wall-only plan candidate: YES
Need manager G-RUN before execution: YES
```

D001 的专业基线可在 `PARTIAL_WITH_LIMITS` 状态回交。若 manager 决定继续，下一任务应先把 B 或 C 变成精确、可授权、可停止的动作，再签新的 W；不得沿用“先跑再看”的方式。
