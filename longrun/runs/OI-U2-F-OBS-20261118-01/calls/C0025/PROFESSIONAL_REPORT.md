# C0025｜D006 E Skill：消费 W007、收敛运行环境分类并签发 W008

## 1. 调用身份

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `call_id`: `C0025`
- `invocation_token`: `6f166f47846b4b40889bfcca98826524`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `physical_chat`: `FOBS-1119-E2`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:manager`

本调用继续原 D006 和当前工作项／阶段实例；没有新建 D，没有恢复 D005/W005，没有重跑 A～D，没有启动 Q/V。

## 2. 已正式消费的 W007

正式 Return：

`daowei2026/observe-iterate@4566786786e8e754700c9cf2cafbbf66b44f030b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W007/WORKER_RETURN.json`

本 executor 已核对并接受 W007 的 `run_id / work_order_id / order_ref / worker / return_to`、事实报告和 manifest 所列必要证据。本次 V2 Return 只把这份正式 Worker Return 登记到 `accepted_worker_refs`。

### 2.1 W007 的真实事实

- 当前 `m3rc` Python 是 `/m3c3/Linux/apps/anaconda3/bin/python` 3.10.13；
- 当前活跃 `mquant.tis.frp` 中，构造模块和 F/Q/V 三个 wrapper 的 `find_spec` 均不存在；
- 活跃 TIS root 为 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis`；
- 活跃 TIS HEAD=`10010b89f8fc79a91affd26f985b6d9bf2d33c6c`，不是锁定 `2f460d663d821cf2ba25555eda13e78b697d0767`；
- 本次所需四个 TIS 文件均不存在且未 tracked；准确含义是当前活跃 TIS 对 FQV 不完整，不是已经证明的本地脏修改；
- 固定 Haskell FRP root 为 `/dwdhome/fy/BASE_E6_2_copy/edh-universe/frp/frp`；
- FRP HEAD=`37c790c0f456fe3022bb00609219d3e92a5c2f9b`，不是锁定 `67711c492da909ed0f044f357beb278abf7fc71c`；锁定 commit 不是当前 HEAD 祖先，目标 F 文件与锁定版本有差异；
- W007 按工单准入失败，因此 D 启动 0 次，无退出码；
- F 未构造，`fields.json` 未检查；
- 没有 HTML、`definition_run_report`、prepared tables 或 plot data；
- 没有安装、构建、切版本、overlay、文件复制、producer、Q/V 或 W2 动作。

所以 W007 证明的是**默认 FY 入口不符合 D006 锁定组合**；它没有证明 F 产品不存在，也没有证伪 B、C 或 D 的业务成果。

### 2.2 W007 暴露的唯一候选

W007 在当前工作区内进行一次精确、有界查找，唯一命中：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/mquant/tis/frp/fqv_kline_example.py
```

该候选：

- 位于本 Run 固定工作区；
- 不属于旧 `observe-iterate-runs/**` staging；
- 具有可见 package 边界；
- 未被证明是完整、单一、正常、锁定版本一致的 runtime；
- 未被导入或执行。

## 3. E2 专业分类

原生产物：

`daowei2026/observe-iterate@f7ab7dcaf526e17f1ed796e9665014e35d0c74a2:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W007_CLASSIFICATION_AND_W008_RUNTIME_GATE_D006_C0025.md`

分类：

```text
DEFAULT_FY_RUNTIME_LOCKED_FQV_MISMATCH
+
SINGLE_IN_WORKSPACE_DEDICATED_RUNTIME_CANDIDATE_UNRESOLVED
```

### 3.1 为什么不返回 B／C／D

- **不返回 B**：真实 F 尚未构造，未触达观察位置或正式表；
- **不返回 C**：没有候选图，C2 展示合同没有被实际结果证伪；
- **不返回 D**：D 使用的是 Owner 锁定的正常 import；实例、字段、位置和 C3 均未被 W007 改动或反证。

### 3.2 为什么不能进入 E3／E4

- 没有 HTML，不能核图；
- 没有被接受的图，不能形成正式取数准入；
- W2 不得启动；
- `DATA_READY=false`。

### 3.3 为什么仍允许一次 W1 revision

Owner 明确允许用历史成功 FQV 现场定位正常运行方式，但禁止旧结果冒充本次交付；同时禁止重建、补装、overlay、package 混合和版本切换。

W007 已经把候选空间收敛为当前工作区内唯一一个非旧 Run staging 的 dedicated runtime。原 E Workflow 允许在基准不变、仍属于 import／路径／已确认运行入口问题时续发 W1。因此，专业上允许做一次只针对该精确候选的来源准入和条件运行；不允许继续泛化搜索或建设环境。

## 4. 已签发 W008

### 4.1 正文

`daowei2026/observe-iterate@afb179352fe81420f250152d9994148be6c4f267:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W008/ORDER.md`

### 4.2 机读工单

`daowei2026/observe-iterate@3916814afc03f39408e4d992efda8a0ddd85f683:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W008/ORDER.json`

### 4.3 W008 的唯一专业目的

判断：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
```

是否已经是无需安装、构建、切版本、复制、软链、overlay 或 package 混合即可使用的单一正常、锁定来源 FQV runtime。

W008 必须依次通过：

1. 候选自身已有正常入口；
2. 构造文件和 F/Q/V wrappers 与锁定 TIS commit 字节一致；
3. 正常所需 TIS 模块来自同一个候选 TIS root；
4. 候选自身已有 provenance 明确绑定锁定 FRP commit；
5. 不修改 `sys.path`／package `__path__` 的 origin probe 通过。

只有五项全部成立，才允许使用候选已有入口运行原 D 一次。

### 4.4 W008 不会做什么

- 不搜索第二个 runtime；
- 不建立 wrapper、activation、`.pth`、`sitecustomize`；
- 不把候选 TIS 与当前活跃 TIS 分层组合；
- 不执行 `seed_inits`／`pretty-exports`；
- 不复制或软链文件；
- 不 checkout、切版本、安装或构建；
- 不修改 TIS、FRP、m3、uplot、平台包、D 或 C3；
- 不调用 producer，不读取 Q/V，不启动 W2。

## 5. W008 的确定后继

### 5.1 准入通过并生成 HTML

```text
W008 Return
→ E2 消费脚本／来源／运行事实
→ E3 核对最终图与 D/C2
```

### 5.2 准入通过但 D 出现新阻断

```text
W008 Return
→ E2 消费新的首个真实阻断
→ 按原 E Workflow 分类
```

### 5.3 runtime 准入失败

```text
EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

此时 E 不再签发环境探测型 W1；下一步由本 executor 向原 manager／Owner 明确提出运行前置。主控和 Worker 不得自行设计 overlay、构建或版本切换方案。

## 6. 当前真实状态

| 项目 | 状态 |
|---|---|
| D006 | 继续有效 |
| W007 | `STOP`；已由 E2 正式消费 |
| E2 分类 | 已完成 |
| W008 | 已发布，**尚无真实物理发送回执** |
| 物理 Worker | `codex:OI-U2-F-OBS-20261118-01:worker:W1`；C0025 输入表明当前 idle、无在途、工作区租约已释放 |
| 原 D 本次运行 | W006 两次失败；W007 0 次；W008 尚未运行 |
| 候选 HTML | 无 |
| E3 | 未开始 |
| E4/W2 | 未准入、未签发 |
| DATA_READY | `false` |
| E 专业状态 | `IN_PROGRESS` |

发布 W008 文件不等于物理派发，不等于候选 runtime 已通过，也不等于 E 完成。

## 7. 主控最小后继

主控只需按现行 V2 做 W008 派发前核验：

- 收件线程仍是本 Run 专用 W1；
- W007 已结束，当前没有 UNKNOWN／IN_FLIGHT 冲突；
- cwd 仍为 `/dwdhome/fy/BASE_E6_2_copy`；
- 当前 Binding 的 `caegraph_run_and_repair` grant、写面、ORDER.md／ORDER.json 和 `issuer_call_id=C0025` 成立；
- 原样发送，不增加第二 runtime、overlay、构建、版本切换或环境修复方案。

W008 完整 Return 必须回本 `executor:E2`。收到后继续同一：

```text
D006
OI-U2-F-OBS-20261118-01-WI-E-R1
OI-U2-F-OBS-20261118-01-M-E-R1
```

## 8. 本次专业状态

```text
professional_state = IN_PROGRESS
accepted_worker_refs = [W007]
issued_order_refs = [W008]
continuation = W008 Worker Return → original executor:E2
owner_request = null for this call
```

本调用没有声明 E 完成、没有声明图通过、没有声明 F 产品不存在、没有声明 `DATA_READY`。
