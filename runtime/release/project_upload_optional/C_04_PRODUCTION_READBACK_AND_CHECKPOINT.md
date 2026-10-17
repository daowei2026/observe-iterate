<!--
canonical_source: agent_evolution/agent_candidates/mission-c-host-implementation-system-candidate-v0.2/canonical_methods/host/PLATFORM_REUSE_AND_PRODUCTION_IMPLEMENTATION_REFERENCE.md
source_parent_commit: b85af4a6578cf455a3da8884a999d98bd5fb1050
execution_revision: 2026-09-30-continuous-implementation
manual_edit: forbidden
-->

# PLATFORM_REUSE_AND_PRODUCTION_IMPLEMENTATION_REFERENCE

```yaml
mission: Mission C
round: C-R2
artifact_role: platform_reuse_production_writer_readback_method_reference
material_baseline: daowei2026/feature-refinement-implementation-agent-evolution@c4bb32290c749bf6c406bcb6ddb05ae5a5f9c16e
platform_examples_used_as: shape_and_api_evidence_only
live_host_code_claims: none
```

## 0. 目的与证据边界

Host Implementation 的工程主体不是“从零造一个能跑的技术世界”，而是把 accepted 市场过程合同落入**现有宿主和现有平台能力**，并沿正式入口闭合到 writer、load、readback 和 consumer。

本文件恢复三项方法：

```text
怎样调查并复用 Feature/Fao/Frame/DBA/CEPS/CFIS/codegen/host API；
怎样让 production root、writer、load、Python readback 和 consumer 属于同一正式链；
怎样在宿主内做不到时形成窄 Spike／platform backpressure，而不是重造第二真源。
```

平台文档和 PoC 只证明 frozen exact ref 下存在何种 API／示例形状，不能决定业务必须如何拆，也不能证明 2026-08-29 的 live Host 代码状态。任何当前 Host code claim 都必须重新查询 live head、报告 drift、选择 exact commit 后另行形成；C-R2 没有这样做。

---

# 一、平台不是一个统一黑箱

Host Builder 应把平台能力分成责任面，而不是笼统写“复用平台”。

|能力面|通常回答什么问题|Host 应怎样使用|不能取得什么权力|
|---|---|---|---|
|Feature／Python producer|参数、target、frequency、上游 Feature、计算与物化入口|复用现有 Feature 定义、运行和上游展开|不能决定业务产品语义或把 typed ingress 当新物理 Feature|
|Fao／Host runtime|Haskell/Python 同名 root、load/doImpl/dump、runtime context|接入正式 typed inputs、调用 Host 程序、走现有 cache/load/dump|不能因为 API 分支方便而省略合同规定 writer|
|Frame／wrapper|参数身份、target、SOF、DataFrame、to_df/to_dfs、multi-symbol|复用正式 wrapper、参数和 readback|不能由 wrapper 默认值定义业务方法、scope 或频率|
|DBA／PublicStorage|正式产品的物理存储、时间轴和字段读写|用 storage DTO 机械保存 canonical product|不能让物理 DTO 成为第二业务 ADT 或第二 writer 权力|
|ADT/codegen/export|Haskell 产品到 Python 可见类型和包导出|走现有注册、生成、export、正式求值上下文|不能手写 shadow ADT 绕开正式 codegen|
|CEPS／FRP|typed processor、Event/Dynamic/Behavior、composition、read-cut/state owner|表达已闭合业务图与状态过程|不能用操作符或调度顺序发明业务关系和 business time|
|CFIS／RulePack host|执行 resolved fuzzy assets，产生 direct outputs|复用正式 host、asset identity、输入输出 binding|不能在 CEPS/Host 重写 MF、rules、aggregation、centroid|
|测试／PoC|说明 Event 函数和 operator 的可运行范式|按 exact API 编写和执行定向测试|PoC 不是生产架构或业务 gold|
|Aidata／downstream readback|消费正式产品、观察图和数据切片|只读正式 readback 并记录版本/data cut|图不能替 writer/readback 对账，也不能决定业务真理|

这张表描述的是能力分类，不要求每个用例都具备全部平台层。

---

# 二、平台复用的调查顺序

## 2.1 从正式产品链倒推，而不是从平台目录正向扫

正确起点：

```text
Taskpack formal product / consumer
→ 谁应生产
→ 谁是 production caller
→ Host 内过程怎样形成
→ writer 怎样到达
→ load/readback 怎样消费
→ 每个接缝已有哪个平台 API。
```

错误起点：

```text
平台有很多 API
→ 选择一个熟悉的组合
→ 再把业务塞进去。
```

## 2.2 定向读取顺序

一次 Host 任务按需读取：

```text
1. 目标 repo owner docs、MANIFEST、package/cabal/config；
2. 正式 production root 与相邻真实 caller；
3. 当前产品的 writer/load/readback 实例；
4. 当前参数、schema、ADT、codegen 和 Python wrapper；
5. 方法资产 host 和现有调用者；
6. platform exact API source；
7. 最近邻可运行 example/test；
8. consumer 的正式字段和产品使用面。
```

不要：

```text
只读 README 后猜 API；
无目的全仓扫描；
把历史/PoC 模块当 current production；
把当前 consumer 只读一列误写成完整产品只该有一列；
把代码存在误写成正式可达。
```

## 2.3 RepoFact 与 Host Builder 分工

```text
RepoFact／engineering compiler：
  证明当前 API、调用链、状态承载、writer/readback、consumer 和平台限制；
  形成 accepted engineering task。

Host Builder：
  消费这些 facts，在授权写面落实现有方案；
  遇到 facts 漂移或未知时提出窄核对，不重新自由设计系统。
```

若 current Host fact 会承重结论，必须重新锁 live exact ref；不能只引用 2026-08-25 Project lock。

---

## 2.4 已有业务特征的理解与实际采用

当前任务涉及已有特征时，Pro 读取其业务说明、参数、输入输出及本次相关实现，弄清它回答什么、在什么材料到达时形成结果，以及当前消费者需要什么。不能只依据名称、字段类型、配置存在或工程师摘要判断业务含义。

在现有工程和交接中说明实际采用方式：调用已有方法、订阅正式 Feature 结果、读取已存产品，或仅参考其业务解释。给出实际模块、调用和所取输出；读过源码或导入类型不等于正式复用完成。与当前消费相关的时间、未形成／空、多结果、修订和状态须读到对应实现，未涉及部分不全量展开。

核对本次实际使用的输出形态。原运行值、存储读回和展示投影可能保留不同内容；只检查当前需要的信息与关系，不进行全库盘点。读取丢失的信息不能记成合法业务空，展示投影不能重新当作上游事实。

已接受工程已经给出接法时沿它完成。原特征能够满足要求则直接使用；存在具体缺项时，由原专业责任者决定最小必要处理，不在消费者中猜来源、补默认值或重复重算上游业务。说明与代码冲突时保留差异，代码存在不覆盖业务合同。

# 三、复用／Adapter／Spike／Backpressure 四分法

## 3.1 直接复用

适用：

```text
现有 API 能忠实表达 taskpack；
现有生产 caller 和 writer 模式可达；
产品身份与 consumer 接缝兼容；
不需要改变平台职责。
```

Host 只做：

```text
构造正式参数；
接 typed inputs；
调用现有 API；
按现有 registration/codegen/readback 闭合；
增加当前业务所需模块；测试和定向检查按实际问题安排，不默认同时扩写场景测试。
```

## 3.2 宿主 Adapter

Adapter 合法的条件：

```text
只机械转换已确定的类型、字段、包装或物理布局；
不做 selection、eligibility、knownness、identity、lifecycle 或 method interpretation；
不成为新持久化真源；
不引入独立配置权力；
输入输出可从现有正式产品唯一确定。
```

典型合法形状：

```text
Python DataFrame row → typed ingress occurrence；
canonical ADT ↔ storage DTO 无损转换；
正式 ports → Python DataFrame rows；
current platform API 要求的轻量 wrapper。
```

典型非法形状：

```text
adapter 内重新选 candidate；
adapter 自建 identity/receipt/dictionary；
adapter 将 unavailable 变 0；
adapter 为 consumer 重算上游业务；
adapter 成为第二 writer／第二 schema。
```

## 3.3 窄 Spike

只有技术事实未知，且它会改变 engineering design 时使用。

Spike 必须写：

```text
单一事实问题；
exact repo/ref/path/API；
为什么 docs/code 还不能回答；
最小实验或静态核对；
禁止改变的业务合同；
成功／失败怎样影响工程方案；
不产 production behavior；
不顺手改平台。
```

例如候选问题：

```text
现有 CEPS operator 是否能表达某个 typed composition？
现有 Fao load 是否返回 Event 还是 batch value？
现有 codegen 是否支持某种顶层 ADT？
Frame 的正式 wrapper 怎样解析多表输出？
```

这不是 C-R2 的实际 Spike，只是方法义务。

## 3.4 Platform backpressure

只有以下条件同时成立：

```text
业务合同已经闭合；
accepted engineering design 明确需要该能力；
已核对 exact live API；
宿主内合理实现与薄 adapter 不能忠实完成；
缺口不是对现有 API 不熟；
修改平台有明确最小范围；
不会把当前用例专名写进平台；
有拒绝第二套平台的方案。
```

Backpressure 至少包含：

```yaml
capability_needed: ...
contract_reason: ...
exact_platform_fact: ...
host_alternatives_examined: []
why_host_cannot_close: ...
minimal_api_delta: ...
observable_business_invariants: []
compatibility_and_migration: ...
tests_and_consumers: []
forbidden_second_systems: []
```

Host Builder 没有平台写权时，只形成 backpressure，不在下游私建替代实现。

---

# 四、禁止第二真源

## 4.1 第二真源的常见形态

```text
第二套业务 ADT；
第二套参数 identity；
第二套 receipt/path resolution；
第二套 writer／DBA；
第二套 FIS/CFIS backend；
第二套 Event scheduler／settlement engine；
consumer 侧重算 producer business fact；
sidecar/dictionary 取得正式产品权力；
旧 writer 与新 writer 并存且都像 authoritative。
```

## 4.2 单一真源检查

每个正式对象写清：

```text
business owner；
canonical in-memory type；
正式 producer；
唯一 writer；
物理 representation；
唯一 readback；
消费者允许的窄 projection；
版本和迁移方式；
legacy retirement。
```

## 4.3 复用不等于保留所有 legacy

```text
当前合同支持的既有能力：KEEP；
只是旧实现历史：provenance/anti-gold；
与新合同冲突：RETIRE/DELETE；
当前 consumer 仍依赖：显式 migration；
Taskpack 未要求：不保留永久 shim／双 writer／旁路。
```

“旧代码不好改”没有修改业务合同的权力。

---

# 五、薄而真实的 production root

## 5.1 production root 的允许责任

```text
加载 accepted program/profile/resolved bindings；
构造平台运行参数和正式 context；
连接真实 typed input sources；
实例化 child processors/state owners；
调用 Host composite；
汇总正式 ports；
接入唯一 writer/load/readback；
向平台返回正式结果或明确 failure。
```

## 5.2 production root 的禁止责任

```text
形成 evidence；
选择 candidate；
解释 RulePack numeric support；
决定 identity/lifecycle/finality；
直接 mutating WholeState；
建立业务 fallback；
补偿上游 receipt/identity；
重算 producer business fact；
吞异常变空结果；
维护第二套 public history。
```

## 5.3 “薄”不等于空壳

真实 root 必须明确显示：

```text
正式输入从哪里进入；
哪个业务程序被实例化；
哪些 state owners/child composites 被连接；
正式 ports 从哪里形成；
writer/readback 接在哪里。
```

一个只有 `return def`、fixture constructor、test helper 或未被平台正式入口调用的 root，不是 production root。

## 5.4 Root reachability chain

候选证据链：

```text
formal external entry
→ platform dispatch/Fao/Feature run
→ production root constructor
→ Host composite process
→ load-bearing Action symbol
→ method binding use point
→ state owner transition/apply
→ formal product port
→ writer call
→ storage artifact
→ load/readback
→ consumer call.
```

每条边要么由源码调用事实、运行 receipt 或正式 artifact 证明；不能靠文件名相似。

---

# 六、Action→symbol 与 method binding 的 production 闭合

## 6.1 Action reachability 不是 symbol inventory

对每个承重 Action 至少记录：

```text
Taskpack Action identity；
业务句子；
realization kind；
module/path/symbol；
parent child field 或调用者；
formal production root；
真实输入来源；
产生的 transition/product；
定向 test；
production evidence status。
```

阻断形式满足：

```text
函数只出现在注释；
同名函数未被 caller 调用；
test-only shadow；
旧 root 仍实际运行；
Action 被内联回大 reducer；
no-op／constant／pass-through；
method field 只存不读。
```

## 6.2 Method effective binding 的七段链

```text
业务方法问题
→ semantic method data
→ resolved binding／asset identity／version
→ production program constructor field
→ formal caller 传入
→ Host Action 使用
→ 输出影响正式 judgement/product。
```

需要区分：

|证据|能证明|不能证明|
|---|---|---|
|资产文件存在|有候选资源|production 使用了它|
|配置字段存在|对象可存该字段|正式 caller 传入|
|单元测试直接调用|函数可运行|production root 可达|
|constructor 接收 field|程序结构有入口|field 没被忽略|
|受控 binding 差异测试|方法会改变预期结果|真实 production 使用该版本|
|production receipt|该 exact run 使用了方法|其他版本/data cut 必然相同|

## 6.3 RulePack/CFIS 边界

Host 负责：

```text
加载 resolved asset；
形成正式业务输入 binding；
调用现有 host；
读取 direct outputs；
按 accepted interpretation 形成 judgement；
保留 asset identity/version/provenance。
```

Host 不负责：

```text
设计 MF；
编写完整规则表；
选择 aggregation/centroid；
建立第二 backend；
让 lifecycle 直接读取一套私有 numeric universe；
用代码默认数值替 semantic binding。
```

---

# 七、writer／load／DBA／readback／consumer 最小正式闭环

## 7.1 七个不同证据层

|层|要求|失败时不能声称|
|---|---|---|
|源码定义|canonical product、storage DTO、writer/load 函数存在|正式可达|
|构建/schema|module/ADT/codegen/registration 可生成|Python 可见、writer 已运行|
|fixture/定向测试|业务纯函数或 Event/state 行为受控|正式 caller 使用同一路径|
|Host 运行|正式输入进入 production root，Host ports 形成|writer 已落盘|
|writer/DBA|唯一 writer 实际写出产品和时间轴|load/readback 正确|
|load/Python readback|正式 wrapper 从同一 artifact 解析业务行|consumer 实际使用|
|consumer|正式下游按同一产品身份消费|campaign 完整或业务效果正确|

每层状态只能是：

```text
passed / failed / not_executed / not_applicable
```

不允许：

```text
源码存在 → round-trip passed；
schema 静态可见 → Python readback passed；
空 DataFrame → 正确业务空；
writer 函数存在 → production writer reached；
fixture 使用 → consumer integrated。
```

## 7.2 最小 formal round-trip

```text
正式 Python/host entry
→ 正式 producer/upstream product
→ typed ingress
→ Host CEPS/state process
→ formal product ports
→ unique writer
→ DBA/PublicStorage artifact
→ formal load
→ Python to_df/to_dfs 或等价 readback
→ actual consumer uses exact product.
```

短闭环可以只覆盖一个代表性 formal product，但必须说明完整 mandatory 产品范围仍在 Taskpack 中，未覆盖部分保持 `not_executed`，不能删除。

## 7.3 canonical ADT 与 storage DTO

```text
canonical business ADT：表达业务 identity、状态、产品语义；
storage DTO：机械、无损、可读写的物理布局；
Python generated/readback type：跨语言可见实现；
consumer projection：按用途读取的窄视图。
```

它们可以不同，但必须有明确双向或足够方向的无损映射。storage DTO 不得重新定义业务。

## 7.4 codegen/export 完整链

候选闭环：

```text
Haskell business/storage ADT
→ codegen registration
→ generated Python module
→ package exports/PrettyExport 等正式导出
→ formal evaluation/import context
→ DBA decode
→ wrapper to_df/to_dfs
→ consumer.
```

具体命令和路径属于 case/platform profile；common core 只保留这条责任链。

## 7.5 正确业务空的资格

只有同时证明：

```text
正式输入已准备；
production root 已运行；
Host process 收到预期 occurrence；
writer/load/readback 没有异常；
Taskpack 允许此 data cut 无业务 occurrence；
计数和 diagnostics 一致；
```

才能标记 `true_business_empty`。否则保持：

```text
input_not_ready / host_not_reached / writer_not_reached /
readback_failed / unsupported / unknown.
```

具体缺陷路由留 C-R3。

---

# 八、consumer-fit implementation

## 8.1 完整产品与窄 consumer ingress 分开

```text
完整 formal product：
  由 Taskpack 决定 occurrence/current/history/diagnostic/identity；

consumer ingress：
  只读取当前 consumer 真正需要的正式 occurrence 或 projection；
  不重算、不复制完整 metadata、不强迫加载无关 current/history。
```

## 8.2 consumer 不能缩减上游业务权力

当前 consumer 只读 occurrence，不能推出：

```text
上游 current view 应删除；
diagnostic 永远无价值；
完整历史不属于正式产品；
其他 consumer 不存在。
```

但工程方案必须避免：

```text
为了读取 occurrence 把整个高成本 FaoResult 常驻；
逐 occurrence 重复运行级 identity／长 Text；
consumer 自己重新形成 producer judgement；
consumer 通过 private sidecar 取得第二真源。
```

## 8.3 consumer readiness 进入 HostCheckpoint

```text
consumer 名称和正式入口；
所需 product/version/projection；
identity/keys/time semantics；
允许为空和 failure semantics；
仍需 IntegrationWave 才验证的义务；
```

HostCheckpoint 只声明“可接入条件已形成”，不冒充 consumer 已完成集成。

---

# 九、core-first 下的平台工作比例

## 9.1 主体优先

最小忠实 Host 焦点应同时触及：

```text
一个承重业务 Action；
一个真实 state/read-cut 或主要方法接缝；
一个 formal product；
一个 production caller；
一个 writer/readback 邻接面。
```

它不是“先把所有 adapter、validator、schema、proof 写完”。

## 9.2 合法前置工程

只有阻断主体且成本成比例时优先：

```text
module/cabal registration；
必要 typed ADT；
exact platform API 核对；
最小 codegen/export；
正式输入 wrapper；
```

## 9.3 周边膨胀信号

```text
大量 registry/sidecar/dictionary；
独立通用 serializer；
完整 artifact chain 先于业务过程；
测试 helper 越来越多但 root 不可达；
平台改造范围不断扩大；
只有 schema/manifest PASS；
```

Skill 应进入实施判断／偏差回压；候选 Harness 记录偏差，但不替 Builder 实现主体。

---

# 十、source-role 对账

|来源|支持本文件的内容|材料身份|不能推出|
|---|---|---|---|
|P1/P2/P3 accepted/active taskpacks|正式产品、producer/consumer、writer、平台复用和 engineering freedom 的 EAW 样本|EAW formal/active artifact|固定 P 包或跨语言拓扑不是 core|
|Taskpack reviews|暴露平台前提、production/readback、machine contract 缺口|review/anti-gold|不能覆盖 accepted contract|
|Implementation Skill 迁移方案|source package/runtime Skill/Goal/platform router 分层|已实施演进证据|不决定 C-R5 物理复用|
|CEPS Skill 03/05|exact platform ref、production root、operator、backpressure 方法|candidate 子能力|不证明 live Host 代码|
|frp-core exact source|CEPS class/operator API 形状|frozen platform fact|不决定业务图|
|frp-poc test guide|Event test 的平台范式|example/test guidance|不是 production evidence|
|Frame README|Feature/wrapper/target/to_df 等平台形状|frozen platform docs|默认值不决定业务|
|real_data_feedback|writer不可达、PrettyExport、identity/readback/consumer mismatch 后果|rolling incident evidence|不自动形成固定修复规则|

---

# 十一、本轮不做的判断

```text
不判断当前 FRP/TIS 哪些 caller/writer 已经正确；
不确认 2026-08-25 后 live platform API 未漂移；
不形成具体 Spike；
不提出平台 patch；
不定义 C-R3 缺陷 taxonomy；
不执行 round-trip；
不声明任何 consumer 已接入；
不决定最终 Repo Read Contract 的物理放置（C-R6）。
```

正式结果采用DataFrame／子表／结构化对象等适当可读形式，正式接口和消费者仍按合同。读取正确后按实施判断§3.5分析业务对象、关系和参数效果，不能停在格式／非空检查。
