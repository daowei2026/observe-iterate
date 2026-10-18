# BI-01-V2-02 R0010：六场景 S2 消费与 S3 业务观察

invocation_id: `BI01-V2-02-R0010-20261018T175239Z-75847f6b`  
assignment_token: `BI01-V2-02-PRO-CONSUME-5754a4a7d26045d689b1e008a016a987`  
run_id: `BI-01-V2-02`  
professional_mode: `OBSERVATION_SCOPE`  
status: **S1/S2/S3 PROFESSIONAL RESULT SUBMITTED FOR MANAGEMENT REVIEW — NOT OWNER ACCEPTED**

## 1. 本轮实际消费的证据及资格

本轮不是把 Worker 的“17 图／1,928 CSV 已完成”转述成业务结论，而是把它们重新接回六个场景的业务问题。

### 1.1 Worker S2 技术结果

实际消费：

- `worker-R0006/WORKER_RETURN.md`
- `CURRENT_NODE_INDEX.csv`
- `FIXED_INPUT_BINDING.json`
- `TECHNICAL_VALIDATION_SUMMARY.json`
- `PUBLICATION_MANIFEST.json`
- `READING_GUIDE.md`
- `SIX_SCENE_OBJECT_BINDING_CHECKS.json`
- `FOCAL_ORIGINAL_FACT_CHECKS.json`
- `SCN01_R02_VS_N_IDENTITY_ALIGNMENT.csv`
- 17 个节点的浏览器验收记录及图包索引

Worker 技术资格为：

```text
17 / 17 current-run nodes
1,928 aidata export_plot_view_data CSV
17 / 17 source-coordinate checks
17 / 17 real Chromium/Bokeh checks
technical pending = 0
business gate = not signed
```

图是给 Owner 读市场过程的；本 Pro 没有读取图像像素。专业判断使用固定源的结构化原行、Worker 的 node/window/As-Of/source binding、SCN-01 原行对齐，以及本轮从同一固定 member payload 提取的路径事实。页面中的 `shared_view; not_primary_evidence` 合同保持不变。

### 1.2 固定数据身份

A 包：

```text
steel_U2_U3_执行结果_20261010.zip
SHA256 = 7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c
```

Worker 与专业附件完全一致。

B 包存在外层 ZIP 差异：

```text
Worker actual outer ZIP = ff3215126461a0cda564c82c4a6e42b99bf94cb7b6a8320df9c8ba93d269d70a
Project attachment outer ZIP = 4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987
```

本轮进一步逐 member 比较了 Worker `FIXED_INPUT_BINDING.json` 与项目附件的 17 个非目录 member。结果是：

```text
17 / 17 bytes 相同
17 / 17 SHA256 相同
outer ZIP bytes 仍不同
```

因此，本轮六场景所消费的 KLine、Zig、mid ScaleTurn、manifest 和说明正文在 member payload 层已经闭合；只保留“外层归档字节不等”这一来源事实，不再把“15 个 CSV 是否一致”列为本轮业务结论的未知。没有依据判断外层差异究竟来自压缩参数、顺序还是元数据，故不作原因推断。逐 member 证据见 `B_MEMBER_PAYLOAD_EQUIVALENCE.csv`。

### 1.3 资格纪律

- C1 broad records 是 raw/reference candidates，不是正式 Cluster。
- SCN-01 的完整 reference chain 仍是一个 Case × 五个 As-Of，不是五个 Case。
- R02 是 `ShadowOpportunityClusterMemberEpisode` objective facts；R03 的正式 Quality 和 Capital Use 全部 `WITHHELD`。
- C2 没有 official cluster commit，也没有 official H1。
- 广域场景没有正式 U3；C0/N/C1 raw 只能作为基础事实、基线或 U3 设计需求，不能改名为 U3。
- 后验固定 4/12/24/48 bar 路径仅用于检验与反证，不能回填历史 Current，也不是正式 Outcome 合同。
- raw quote progress 不跨品种直接排名。本文出现的“占起点价格比例”是专业观察辅助归一化，不是正式 U3 normalization 或 calibration。

## 2. S2 图与同源数据定位

完整 17 行索引见 `S2_CHART_AND_DATA_INDEX.csv`。最关键入口如下：

| 场景 | 基础图 | Evidence / As-Of 图 | 正式观察窗口 |
|---|---|---|---|
| SCN-01 | [6101](http://192.168.11.40:6244/graph/cae/6101/report) | [6102](http://192.168.11.40:6244/graph/cae/6102/report)，五个 As-Of 为 [6103](http://192.168.11.40:6244/graph/cae/6103/report) / [6104](http://192.168.11.40:6244/graph/cae/6104/report) / [6105](http://192.168.11.40:6244/graph/cae/6105/report) / [6106](http://192.168.11.40:6244/graph/cae/6106/report) / [6107](http://192.168.11.40:6244/graph/cae/6107/report) | 2021-04-26 09:30 — 2021-05-20 15:00 |
| SCN-02 | [6114](http://192.168.11.40:6244/graph/cae/6114/report) | [6115](http://192.168.11.40:6244/graph/cae/6115/report) | 2021-05-14 09:30 — 2021-05-24 15:00 |
| SCN-03 | [6112](http://192.168.11.40:6244/graph/cae/6112/report) | [6113](http://192.168.11.40:6244/graph/cae/6113/report) | 2021-11-04 09:30 — 2021-11-12 15:00 |
| SCN-04 | [6108](http://192.168.11.40:6244/graph/cae/6108/report) | [6109](http://192.168.11.40:6244/graph/cae/6109/report) | 2021-11-17 09:30 — 2021-11-25 15:00 |
| SCN-05 | [6116](http://192.168.11.40:6244/graph/cae/6116/report) | [6117](http://192.168.11.40:6244/graph/cae/6117/report) | 2021-10-25 09:30 — 2021-11-02 15:00 |
| SCN-06 | [6110](http://192.168.11.40:6244/graph/cae/6110/report) | [6111](http://192.168.11.40:6244/graph/cae/6111/report) | 2021-07-28 09:30 — 2021-08-05 15:00 |

这些链接是 Worker 已真实浏览器核验的内部服务入口；本文不把它们的网络可达性等同于 Owner 已经实际阅读。

---

# 3. SCN-01：同刻三成员，原机会身份与当前单品种状态分离

## 3.1 市场事实与 U2 位置

hc、i、rb 在 `2021-04-30 15:00` 同时出现 mid trough、预期方向 Up；三者共同可知时间为 `2021-05-06 10:00`。这使“同一轮共同启动候选”具有清楚的 actual-time 基础。

U2 判断：

- **支持**：三成员属于同一初始机会身份的组织是合理的。
- **资格限制**：raw candidate `refonly-d7ea0ed7945a722aaa` 不是正式 Cluster；完整 reference Case `refonly-ad8824a52552d7bffa91` 也没有 official commit/H1。
- **反证边界**：Universe 恰好就是 hc/i/rb，`outside_count=0` 与 `ValidEmptyAlternatives` 只说明没有当前 Universe 内的 outsider，不能证明 External Separation。

## 3.2 2021-05-06：Progress 与 Friction/Retention 给出冲突证据

三个 anchored episode 都是 `WorkingSoFar`、观察 2 bar。用起点价格作探索性归一化：

| 成员 | 净推进/起点 | path efficiency | 最大反向/起点 | retained fraction |
|---|---:|---:|---:|---:|
| hc | 3.54% | 0.944 | 0.11% | 0.971 |
| rb | 4.09% | 0.932 | 0.15% | 0.965 |
| i | 4.36% | 0.821 | 0.47% | 0.902 |

市场事实是：i 的早期 Progress 略高，但 Friction 更大、Retention 代理更差。由此只能形成：

> i 早期推进较快，但路径更不稳。

不能形成“i 最好”或“i 最差”。这支持 U3 把四束分开，也反对用字段票数或单一总分替代业务叙事。

## 3.3 2021-05-07：先比较 lifecycle，再比较数值

- hc：原 anchored episode `WorkingSoFar`，14 bar，progress 277。
- rb：原 anchored episode `WorkingSoFar`，14 bar，progress 268。
- i：原 anchored episode `Completed`，1 bar，progress 51、efficiency 1.0。

i 的 efficiency 1.0 来自一根 bar 的短促完成路径，不能与 hc/rb 的 14-bar Working 路径直接排名。

更重要的是，N 在同一 As-Of 已经进入 i 的另一个 current working episode：

```text
R02 anchored i episode = refonly-22321a4b963e925b7c
stage = Completed
progress = +51

N current i episode = refonly-2cf06752c4866b9236
stage = Working
progress = -53.5
```

这不是数据冲突，而是两个不同业务问题：

- R02：原共同机会中的 i member episode 发生了什么；
- N：i 此刻当前单品种 episode 发生了什么。

## 3.4 2021-05-11—05-18：anchored episode 分化

- rb 在 5 月 11 日已经完成 33-bar anchored episode，raw progress 707，探索性约为起点的 13.14%。
- hc 在 5 月 11 日仍 Working 38 bar、progress 670，随后以 33-bar completed episode、progress 798 完成，约为起点的 14.04%。
- i 的原 anchored episode 一直保持 1-bar completed、progress 51，约为起点的 4.83%。

因此，在 **episode-lineage** 语义下，rb/hc 的原机会延伸明显超过 i。

但是，固定 24/48 bar KLine 显示 i 后来仍继续上涨，而且固定窗口累计幅度可能更大。那段运动跨越了后续 Episode。它不能自动写回原 anchored episode 的 Retention。

这要求设计明确分开：

```text
episode-lineage Outcome
fixed-future-horizon Outcome
```

## 3.5 基线增量

KLine/C0/N 已经可以告诉我们“i 当前转弱、hc/rb 仍在延伸”。U2+R02 的真实增量不是简单发现涨跌，而是：

1. 保留原机会的 member-episode identity；
2. 即使 N 已滚到新 Episode，仍能追踪原机会中的成员何时结束；
3. 避免把后来新 Episode 的上涨或下跌误归到原共同机会；
4. 支持重复暴露和机会级追溯。

尚未证明的是：

> U3 是否比 KLine/C0/N 更早、更稳定地提高成员选择质量。

R03 仍全部 Withheld，所以本 Case 支持“组织和可追溯性增量”，不支持正式 Quality 或 Allocation。
