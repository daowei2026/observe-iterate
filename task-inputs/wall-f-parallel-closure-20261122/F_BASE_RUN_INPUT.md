# F 基础 Feature Run 输入

> **状态：业务范围、FRP 版本和 `observation_multiple=800` 已锁定。** 正式启动仍须完成工作区占用对账、真实配置回读和 Codex 物理线程预检。不得用旧脚本原样调用默认 6。

## 1. 目标 Feature、用例与精确版本

```yaml
feature_name: CommonPriceTurnGroupCandidatesFrp
business_name: F｜共同价格转折候选组
use_case_ref: task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md
base_instance_sources:
  - task-inputs/u2-fqv-observation/实例运行脚本.py
  - task-inputs/u2-fqv-observation/无二义性需求和实现文件.md
  - daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json
instance_selection: make_features(...) returned object f only
frp_repository: daowei2026/frp
frp_branch: codex/f-observation-multiple-20261122
frp_commit: ac1927518ad6105f15ffbe37fea45e4be91ba574
tis_repository: daowei2026/tis
tis_commit: 2f460d663d821cf2ba25555eda13e78b697d0767
tis_constructor: frp/fqv_kline_example.py::make_features
python_feature_class: frp/CommonPriceTurnGroupCandidates.py::CommonPriceTurnGroupCandidatesFrp
```

旧 U2/U3 输入继续锁定对象、构造关系和除本次 override 外的参数。旧 FRP commit 只作为对照；正式 F 代码必须实际加载上述新提交。

## 2. Owner 锁定的新实例

本次只增加以下 profile 字段：

```yaml
profile.observation_multiple: 800
```

其他基线参数与 U2/U3 `fqv-kline-rb-hc-i` 实例保持一致，尤其包括：

```yaml
profile.delta: 600
profile.unit: CalendarUTITick
market.units_per_open_minute: 120
symbols: [rb, hc, i]
frequency: 5m
calendar: night_end_at_2300
```

因此：

```text
Δ = 600 CalendarUTITick = 5 个开盘交易分钟
800Δ = 480000 CalendarUTITick = 4000 个开盘交易分钟
```

`800` 不是 800 分钟，也不是 800 根 K 线。新 FRP 版本仍保持 actual 转折之间的 `2Δ` 贴近条件不变；`observation_multiple` 只进入观察／首次准入和相关有限责任窗口。不得把 2Δ 一并放大。

## 3. 正式实例怎样构造

旧 `task-inputs/u2-fqv-observation/实例运行脚本.py` 会直接执行：

```python
f, q, v = make_features(**PARAMS)
```

该旧入口没有 `observation_multiple` 形参，原样运行会继续使用默认 6。正式 F800 实例必须在正常构造基线 F 后，复制其 profile 并仅加入一项 override。

任务内允许的构造方式如下；若现场平台对象接口有细小差异，执行者应沿同一正常参数对象完成等价构造，不得回退到默认 6：

```python
from mquant.tis.frp.fqv_kline_example import make_features
from mquant.tis.frp.CommonPriceTurnGroupCandidates import (
    CommonPriceTurnGroupCandidatesFrp,
)

base_f, _, _ = make_features(**BASE_PARAMS)
profile = dict(base_f.P.profile)
profile["observation_multiple"] = 800

if base_f.P.inputs is not None:
    f800 = CommonPriceTurnGroupCandidatesFrp(
        inputs=base_f.P.inputs,
        domain=base_f.P.domain,
        profile=profile,
        result_layout=base_f.P.result_layout,
    )
elif base_f.P.sources is not None:
    f800 = CommonPriceTurnGroupCandidatesFrp.from_sources(
        base_f.P.sources,
        domain=base_f.P.domain,
        profile=profile,
    )
else:
    raise RuntimeError("F baseline has neither inputs nor sources")
```

运行前必须保存并核对序列化配置，至少证明：

1. `profile.observation_multiple == 800`；
2. `profile.delta == 600`；
3. `rb/hc/i`、5m、Calendar、domain、sources 与基线一致；
4. 除新增 `observation_multiple` 外，没有未声明的参数差异；
5. `inspect.getfile(...)` 和实际加载模块对应 FRP commit `ac192751...`；
6. F800 的 `full_dir` 不能与默认 6 实例目录混同。

任何一项不成立都应停止正式运行并报告，不得静默回退。

## 4. Owner 锁定的正式运行范围

```yaml
sof_name: TA_updto20240229_DBA
industry: steel
symbols: [rb, hc, i]
sampling: 5m
requested_start_time: 2021-01-01
requested_end_time: 2023-12-31
calendar: night_end_at_2300
workspace: /dwdhome/fy/BASE_E6_2_copy
scope_change_policy: FIXED_AT_START  # 不在运行中征询 Owner；越界则局部阻断
```

实际首末交易时点由锁定日历决定，但不能据此把正式请求改写成较短年份。局部短窗口只允许用于诊断，不能替代三年正式结果。

## 5. 已有结果与重跑规则

FRP 提交说明记录了使用 `observation_multiple=800` 对 `rb/hc/i`、2021—2023 运行并做独立公开表读回；但该结果包路径、`fields.json` 身份和 SHA 并未随本任务输入锁定。

因此启动时：

1. 先在正式工作区查找该精确实例结果；
2. 只有代码、完整序列化配置、日期范围、Calendar、结果目录和公开表读回全部一致时才可复用；
3. 复用时记录结果路径、`fields.json`／配置哈希、31 张公开表读回和实际首末时间；
4. 不满足时只重跑 F800，不把 Q、V 作为本基础 Run 的专业产物；
5. 不能复用默认 6 的旧 F 结果。

## 6. 既有理解复用

起点包括：

- `ai_chat/根据统计找不合理点/F特征：统计线闭环.md`；
- U2/U3 原实例、需求与实现索引；
- 旧实例运行结果；
- 本次 FRP 提交的新旧差异。

执行 AI 只核对新参数影响相关的最小事实：材料准入、actual／confirm／selected／create／revision 时间、观察关闭、修订责任和输出字段。Owner 不需要重新整理一份完整 FeatureUnderstandingPackage。

## 7. Owner 锁定的统计与分析问题

本轮首先回答：

1. 从输入贴近转折到候选组有哪些真正业务对象／业务概念，各自属性如何按业务处理组织；
2. 上下游对象的处理、时序逻辑和正式 Feature／Event／occurrence／字段映射；
3. 每个品种原有多少贴近转折，经过各层资格、关系和期限后形成多少候选组 identity 与候选组 occurrence；
4. 比较上游对象与下游对象的次数、转化、发生位置和首次阻断；
5. 区分 actual、confirm、selected、group create、revision 等时间，并解释 Δ 与 `observation_multiple=800` 的实际作用；
6. 说明 800 恢复了哪些原被期限挡住的对象，新增对象是否仍满足共同转折的业务条件；
7. 检查过密、重复、长期开组、修订责任冲突及其他新 finding；
8. 所有正式表格行说明计数单位、分母和业务含义。

候选组数量变多、某一个迟到案例通过、新参数无报错，都不能单独证明 F 已合理。

## 8. 新 finding 与修改确认

若诊断确认需要改变参数、常量、期限关系、代码、数据处理或输出合同，执行者先形成责任逻辑定位、影响分析与验证依据。**在本 Run 初始 GO 已明确授权的自主迭代范围内**，直接实施、必要回归、完整重跑 X/G 并继续闭环，不另设 Owner 确认。

初始 GO 尚未授权的正式变更不得凭本输入文件自行实施；只将受影响工作登记为局部阻断并保留修复方案、证据和恢复条件，不发起运行中 Owner 请求。诊断性实验不自动升级为正式实例修改。历史已锁定 Run 的 GO 和权限不被本次文档更新倒灌改写。

## 9. 运行配置

```yaml
execution_profile: CODEX_NATIVE_DIRECT
run_id: ASSIGN_AT_REAL_GO
workspace: /dwdhome/fy/BASE_E6_2_copy
manager: fresh Codex thread for this run
executor: fresh Codex thread for this run
workers: []
```
