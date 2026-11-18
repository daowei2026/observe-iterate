# E1｜执行与核图基准

## 1. 身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `delegation_id`：`D005`
- `issuer_call_id`：`C0012`
- `executor`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `definition_id`：`OI-U2-F-OBS-20261118-01-D-CAEGRAPH-V1`

## 2. 唯一运行输入与核图依据

- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- D 集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- C3 表准备／展示代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- B 位置：`OI-U2-F-OBS-20261118-01-B-POS-001`

## 3. 真实环境入口

- 工作区实路径：`/dwdhome/fy/BASE_E6_2_copy`
- Worker 应在该工作区内找到包含下列相对路径的 `daowei2026/observe-iterate` 工作树，不新建 clone、不切换到其他 Run 工作区：

```text
longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py
```

- 进入该 `observe-iterate` 工作树根目录后，核对分支／工作树对应本 Run，再运行：

```bash
mkdir -p longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/u2_f_caegraph

python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/u2_f_caegraph \
  > longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/w1_run.log \
  2>&1
```

Worker 必须保存实际退出码；若当前环境的正式 Python 入口不是命令名 `python`，可在不改变环境或业务语义的前提下使用该工作区已经配置的等价 Python 入口，并在日志中记录实际命令。

## 4. W1 可以直接修的范围

仅限不改变业务含义的确定性机械问题：

- Python 语法、import、模块或文件路径；
- 锁定版本中已经核实的 API 名称／参数差异；
- 明确的类型转换；
- 输出目录、文件名、日志和静态 HTML 接线；
- 为使本次候选运行可复现而必须补充的、没有业务选择空间的运行入口接线。

有修改时保存 `git diff`；无修改时明确写无。

## 5. 必须停止并回 E 的情况

- 精确 F 实例没有既存 `fields.json`；不得调用 `f.rerun()`，不得执行被 Owner 排除的全历史 producer 重跑；
- 需要改变 `TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i`；
- 需要改变 B 的 `2021-01-01` 至 `2022-12-31` 位置；
- 需要删除、增加、替换业务字段或另算近似值；
- 需要改变 C2 的主图／附图、图元、时间表达、标准化、交互或阅读语义；
- 正确修法不唯一，或无法判断是否影响业务语义；
- 需要访问或写入本 Run 授权范围外的位置；
- 工作区冲突、已有同一 W 在途或动作效果未知。

## 6. W1 最小回报

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
最终脚本：<path 或 commit>
候选 HTML：<path；未生成则写无>
运行日志：<path>
实际修改：<git diff 引用；无修改写无>
当前阻断：<首个真实阻断；无则写无>
definition_run_report：<path；没有则写无>
```

如果失败由环境／数据版本造成，额外回报实际 `cwd`、Git 分支／HEAD、Python 入口和首个相关版本事实；其他情况下不先制作完整环境快照。

## 7. E2／E3 核对基准

E 收到 W1 Return 后至少核对：

1. 是否生成可打开的候选 HTML；
2. 最终脚本是否仍只读取 `make_features(...)[0]` 的 F，且没有重跑 producer；
3. SOF、日历、品种、时间和 `groupKnownFrom` 是否保持；
4. `git diff` 是否只含上述机械修复；
5. 候选图是否保持 C2 的结构：每品种 5m 原价与成员证据、候选 revision 面板、Required 四坐标审计；
6. member actual、confirmation、member-known 与 candidate `groupKnownFrom` 是否仍分开；
7. definition-only publication 是否未被画成候选 occurrence；
8. `groupFormationParticipation` 缺口、raw-turn 可选叠加和 overlap／covered-by 目标精确点边界是否未被伪造解决。

E 的候选结论只能是：接受、限域接受、返回 B、返回 C、返回 D 或阻塞；Worker 不作此判断。

## 8. W1 副产物与正式取数边界

D 脚本当前会在候选运行目录中顺带写出 `prepared_tables/`、`plot_data/` 和 `definition_run_report.json`。在 W1 阶段：

- 它们只作为运行诊断副产物；
- 不属于 E4 正式取数准入；
- 不得被回报为 W2 正式数据；
- 不得据此标记 `DATA_READY`。

只有 E3 接受最终图并形成 E4 取数清单后，才能另行签发 W2，将明确列出的图层／对象和数据阶段导出为正式数据。

## 9. 当前动作事实

- E1 基准已形成；
- 逻辑 Worker：`codex:OI-U2-F-OBS-20261118-01:worker:W1`；
- 当前资源记录中的 `actual_worker_thread_binding_ref=null`；
- 本记录不构成物理派发、Worker 执行或结果接受；
- 下一合法动作是主控核验物理 Worker、模型／强度、cwd、单写者及修正后的权限范围，然后发送正式 `W001`。
