# E1｜D006 最小执行与核图基准

## 1. 身份

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `issuer_call_id`: `C0023`

本基准重新开始完整 E Skill，不继续 `D005 / W005`。A～D 当前正式成果继续有效且不重跑。

## 2. 唯一运行与核图输入

### D 完整脚本

`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`

### C2 当前唯一预期 HTML

`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`

### C3 表准备／展示代码

`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`

### D 集成与定义级检查

- `daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- `daowei2026/observe-iterate@37f81088985ff3f1d8c2e7fa409db7529586073f:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/DEFINITION_CHECKS.json`

D 已完成定义级语法、实例、B 位置、A 字段、C2 展示合同和禁止 F producer 重跑检查；真实平台导入、既存 F 产品读取、Bokeh 布局和 HTML 仍必须由 E/W1 在实际环境完成。

## 3. 实例与范围

本次仅观察正常 `make_features(...)` 返回的第一项 `f`：

```text
CommonPriceTurnGroupCandidatesFrp
SOF: TA_updto20240229_DBA
block: steel
calendar: night_end_at_2300
frequency: 5m
symbols: rb, hc, i
time: 2021-01-01 through 2022-12-31
candidate position: groupKnownFrom
```

不读取 Q/V，不调用 F producer，不进入合理性分析。

## 4. FRP Haskell 与 TIS Python 的运行定位

两套来源必须分开，不得把 `mquant.tis.frp` 当成 FRP Haskell 仓库：

1. **FRP Haskell 源码来源**
   - 锁定：`daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`
   - 文件：`src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs`
   - 本 Run 工作区对应源码仓库预期定位：`/dwdhome/fy/BASE_E6_2_copy/edh-universe/frp/frp`
   - 该路径用于核对 F 的 Haskell 实现来源，不作为 Python import 路径。

2. **TIS Python 构造来源**
   - 锁定：`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`
   - 文件：`frp/fqv_kline_example.py`
   - 正常运行 import：`mquant.tis.frp.fqv_kline_example`
   - 构造：`make_features(**FEATURE_PARAMS)`，只消费返回值中的 `f`。

W1 应直接使用 FY 当前真实运行环境的 Python 包解析；不得构造 TIS overlay、混合两套 package、重建／补装平台，亦不得把 Haskell 源码树加入 Python package 路径。

## 5. 工作区、入口与输出

- 工作区：`/dwdhome/fy/BASE_E6_2_copy`
- Worker：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- 运行入口：从实际存在且能回查到上述 D/C3 精确原件的 `observe-iterate` 源码根目录运行：

```bash
python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/output/u2_f_caegraph
```

- W006 运行日志：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/logs/w006_run.log`
- 候选输出：`.../W006/output/u2_f_caegraph/u2_f_caegraph.html`
- 运行报告：`.../W006/output/u2_f_caegraph/definition_run_report.json`

历史 W001 的 exact detached source 可以作为已有精确 D/C3 原件位置候选，但旧运行结果、旧 overlay 和旧修复方案不能冒充本次结果；W006 必须产生自己的运行日志、输出和 Return。

## 6. W1 可直接处理的机械问题

首轮必须先真实运行一次。之后只允许处理不改变业务含义且修法唯一的问题：

- Python 语法、确定性的 import／模块／文件路径；
- 锁定版本中已核实的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、文件名、日志、静态 HTML 接线；
- D/C3 的 run-local 修复副本及对应 diff。

任何修复不得修改 TIS、FRP、uplot、m3、mquant 平台源码或安装，不得切换版本，不得建立 overlay；若需修 D/C3，只能在 W006 自己的 run-local 目录保留副本和 diff。

## 7. 必须返回 E 分类的事项

- 需要改变 SOF、品种、日历、5m 尺度、2021～2022 位置或 `groupKnownFrom`；
- 需要改变 A 字段、C2 主附图／图元／时间表达／标准化／交互；
- 需要读取 Q/V、另算近似值或执行 F producer；
- 当前 TIS Python 包、FRP Haskell 来源或运行环境与锁定版本出现无法唯一机械处理的差异；
- 正确修法不唯一，或可能影响业务语义；
- 写入超出当前 grant，或现场效果未知／存在并发冲突。

## 8. 首轮里程碑与状态

本基准形成时，尚无 D006/W006 的真实业务运行结果。第一个真实里程碑定义为：

```text
W006 在当前真实环境启动原 D 脚本，
并产生可打开的候选 HTML，或产生本次新的第一个真实阻断及 definition_run_report。
```

在该里程碑发生前，E 状态为 `IN_PROGRESS / WAITING_FOR_W006_RETURN`；不得宣称图已接受或 `DATA_READY`，也不得启动 W2。