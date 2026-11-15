# D004｜直接 BASE 观察材料计划与当前执行状态

## 0. 当前标签

```text
method          = control/02 original Skill steps 0–7
material status = PLAN_READY
actual current data obtained in C0017 = NO
continuation    = W008
```

`PLAN_READY` 只表示当前入口、材料取舍和执行合同已形成；它不替代真实取数，不构成 `DATA_READY`，也不支持正式 current comparison。

## 1. Step 0｜入口与现有资产

### 1.1 直接工作区

```text
/dwdhome/fy/BASE_E6_2
```

本轮直接复用已有源码、数据、构建环境、test、trace、reader、Notebook/CAEGraph和历史结果，不再建设独立源码副本、Landlock/seccomp、全局零外写或 clean closure 前置。

### 1.2 已知入口

来自 D001/D002 的已核线索：

- TIS：`/dwdhome/fy/BASE_E6_2/mquant/tis`
- FRP：`/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp`
- frp-core：`/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core`
- historical WallAssembler receipt/sparse/trace和legacy O/C/D product；
- current source modules：`WallLifecycle.hs`、`FaoIngress.hs`、`Products.hs`、`Publication.hs`、`OccurrenceLedger.hs`、`P1EndToEndSpec.hs`；
- legacy bounded physical reader；
- current writer names：`wall_occurrences / wall_current_view / wall_diagnostics`；
- existing light integration tests和 current source static findings。

W008 必须重新核当前 BASE 的 HEAD/branch/status/diff/hash/mtime，不能把 D001 时点直接贴成当前运行绑定。

## 2. Step 1｜业务处理骨架与真实输出核对

本轮需要更新并用真实 BASE 事实绑定：

```text
WallAssembler / upstream occurrence or trace
→ TIS/Fao ingress and decode
→ occurrence ledger + lifecycle active/current state
→ publication
   ├─ wall_occurrences (O)
   ├─ wall_current_view (C: current update stream)
   └─ wall_diagnostics (D)
→ actual reader / consumer / analysis material
```

需要分开的输出角色：

| 对象 | 业务角色 | 当前已知 | 本轮要核 |
|---|---|---|---|
| upstream occurrence/trace | 业务输入和身份/时间锚 | historical可对账 | current exact input或controlled input |
| O | occurrence事实 | legacy存在 | current生成/结构/顺序 |
| C | 本 firing current-update | source静态已知 | current真实值、last-update与identity |
| D | decode/state diagnostic | legacy非空、identity弱 | current exact constructor、firing/identity关联 |
| A | full active map或等价state | source内部存在 | 是否已有可读state trace；不是开工前强制全量建设 |
| reader/consumer | 业务可消费路径 | legacy bounded reader | current existing path、转换损失和真实可执行性 |

## 3. Step 2｜三个父问题的材料取舍

### 3.1 `Q-WALL-IDENTITY-LIFECYCLE`

| 材料 | 取舍 | 理由 |
|---|---|---|
| current code/data/params/calendar/object/time binding | **必需** | 否则无法声称current |
| upstream controlled input或现有current trace | **必需** | identity和transition锚 |
| current normal Start→update→End O/C | **必需** | 最小current lifecycle判断 |
| A full active map或等价state trace | **有条件需要** | End删除/active continuity需它；若现有test已给等价pre/post可用 |
| End→update / End→Start | **有条件需要，高优先** | 区分terminal policy |
| same/cross-firing duplicate | **有条件需要，高优先** | 区分ledger scope与existing conflict |
| 全部九场景 | **暂不准备为整包** | 不是本轮开工前置；按高区分度最小取材 |

### 3.2 `Q-WALL-PUBLICATION-STATE`

| 材料 | 取舍 | 理由 |
|---|---|---|
| upstream→O/C/D同firing对账 | **必需** | publication主问题 |
| C current-update与A state区别 | **必需到可回答深度** | 防止把update stream当active snapshot |
| current reader/consumer实际路径 | **必需** | 判断材料能否用于业务 |
| End measurement转换 | **必需** | legacy已有信息损失候选 |
| one legal + invalid same firing transaction | **有条件需要** | 只有existing test/低成本时取 |
| identity-specific D mapping | **有条件需要** | 若D无法关联，将限制error解释 |

### 3.3 `Q-WALL-BUSINESS-SUITABILITY`

| 材料 | 取舍 | 理由 |
|---|---|---|
| current normal chain + binding + reader | **必需** | 最低 suitability 基础 |
| 至少一个高区分度 terminal/replay/transaction/time场景 | **有条件需要，高优先** | 支撑“只正常链”之外的边界 |
| natural current market sample | **可选建议** | controlled evidence不等于自然频率；现有可得则取 |
| CAEGraph 图 | **暂不强制** | 本轮可先用纯数据/trace；不为AI强制画图 |

缺单项只限制对应问题，不整包冻结其他材料。

## 4. Step 3｜观察方法

本用例优先采用确定性、可追溯的纯数据/trace方法，不强制套用候选绘图 Skill：

1. exact source/status/hash核验；
2. existing reader/test/trace/runner；
3. targeted test selector或窄窗口 controlled input；
4. 对 upstream、O、C、D、A/等价state 按 firing/ref/localNo/UTI/time 对账；
5. 对 current reader/consumer做实际执行或明确不可执行；
6. 如已有 Notebook/CAEGraph 能直接给 identity/time/state 视图，作为补充，不重做完整图。

每份材料必须区分：

```text
static source
controlled test
synthetic engineering test
natural data
business observation
```

同一 trace 导出的 O/C/A/D 是同源证据，不重复计票。

## 5. Step 4｜最小落地

### 5.1 优先顺序

1. 复用现有 test/runner/reader/trace；
2. 使用已有参数和现有构建环境；
3. 只在 W008 root 新增小脚本、selector、转换和导出；
4. 本首轮不修改现有源码文件；若唯一阻断需要小范围修改，记录精确 candidate、目标文件现状、patch建议和回退方式，回 E1 决定，不在 W008 擅改。

### 5.2 允许的实际动作

- 有界只读 inventory、git status/diff/hash；
- 现有 target/test 的低成本定向运行；
- 窄窗口 controlled input；
- 现有 product/trace 的只读解码；
- W008 root 内临时脚本、数据、日志、manifest；
- 工具不可避免的 BASE 内 build/cache 写入，须事前列路径、不得 clean/reset/delete，事后报告真实变化。

### 5.3 停止点

- 命令会无界/full-year重算；
- 预计或实际单命令超过30分钟、产生超过5 GiB新数据，且没有更窄替代；
- 会覆盖现役结果或他人未提交修改；
- 需破坏性Git、正式源码push或生产写入；
- 版本/身份混淆会制造伪current证据。

停止对应动作，不停止其他可继续材料。

## 6. Step 5｜W008 实际取材优先级

### P1｜current binding与链路

- BASE当前HEAD/branch/status/diff；
- exact source/build/test入口；
- params/calendar/object/time/data binding；
- processing skeleton和真实输出角色。

### P2｜current normal chain

优先用现有 target/test/runner获得最小 controlled normal chain：

```text
Start
→ one or two legal updates
→ End
```

尽可能取得 upstream、O、C、D 和 A/等价pre-post state。没有A不阻止先交O/C，但要明确限制。

### P3｜reader/consumer

实际验证 current product/trace 如何被读取或转换；若没有current materialization，精确区分“入口不存在”“数据不存在”“schema/wrapper不匹配”“命令不可执行”。

### P4｜高区分度场景

只在 existing test/低成本路径存在时，按优先级取得最多两个：

1. cross-firing duplicate Start；
2. after-End update/End/Start 中现有test最接近的一项；
3. one legal + one invalid same firing；
4. out-of-order UTI。

不建设9场景整包，不新增dedicated target作为本轮前置。

## 7. Step 6｜质量检查

W008材料必须至少核：

- exact current source/data version；
- object/calendar/parameter/data stage；
- actual/confirm/known/firing time可得性；
- identity key及其scope；
- O/C/D/A角色，不把working-state/debug当committed output；
- `NoOccurrence / ValidEmpty / DataUnavailable / InsufficientHistory / Pending`不混；
- original value、postprocessed、display转换和损失；
- command/cwd/input/output/exit/elapsed/bytes/副作用；
- controlled/static/natural证据类别；
- legacy/current版本不混。

## 8. Step 7｜交付与状态

W008 返回：

- actual asset inventory；
- processing skeleton；
- material selection表；
- real data/trace/test outputs；
- current material manifest与review；
- exact缺口和可/不可回答问题；
- `DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED`之一。

只有计划而无真实current材料时不得返回 `DATA_READY`。Worker不作业务合理性结论、expectation freeze或父问题完成判断。

## 9. C0017 当前状态

```text
plan and method contract = READY
real current material    = NOT YET OBTAINED
formal current comparison= NOT STARTED
next action              = W008
D004                      = IN_PROGRESS
```
