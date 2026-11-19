# C0026｜D006 E Skill：消费 W008、纠正假阻断并签发 W009

## 1. 调用身份

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `call_id`: `C0026`
- `invocation_token`: `55912772627a49c9a9f5946c28146ad0`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `physical_chat`: `FOBS-1119-E2`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:manager`

本调用继续原 D006 和当前工作项／阶段实例；没有新建 D，没有恢复 D005/W005，没有重跑 A～D，没有启动 Q/V。

## 2. 已正式消费 W008

正式 Return：

`daowei2026/observe-iterate@be3f2f9c2102fc182909140234921f7ad3d4457b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/WORKER_RETURN.json`

本 executor 已核对并接受 W008 的 `run_id / work_order_id / order_ref / worker / return_to`、事实报告和 manifest 所列必要证据。本次 V2 Return 只把这份正式 Worker Return 登记到 `accepted_worker_refs`。

### 2.1 W008 的真实事实

W008 固定检查：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
```

已确认：

- 候选根、`runtime/`、`runtime/mquant/`、`runtime/mquant/tis/` 均存在且自身不是 symlink；
- 候选根存在普通文件 `provenance.json`，大小 1217 bytes；
- `runtime/.codex` 指向候选根外的 `/dwdhome/fy/BASE_E6_2_copy/.codex`；
- Worker 没有跟随该链接、没有读取其目标、没有加载任何候选或外部代码；
- 按 W008 ORDER 的“一旦发现任意外部 symlink 立即 FAIL”规则，在此停止；
- 候选已有入口、TIS 四文件、TIS 完整性、FRP provenance、origin probe 和原 D 均未检查；
- D 启动 0 次，无退出码、无 HTML、无 definition report；
- 无环境、业务或源码修改。

W008 的 `outcome=STOP` 对其自身工单是合法的，且 Worker 执行正确。

## 3. E2 对 W008 的专业纠正

原生产物：

`daowei2026/observe-iterate@a3cd1b34702e7658d8ea5e69d157e187c9fcabd3:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W008_CLASSIFICATION_AND_W009_CORRECTED_RUNTIME_GATE_D006_C0026.md`

分类：

```text
W008_ORDER_GATE_FALSE_POSITIVE
+
DEDICATED_RUNTIME_PROVENANCE_AND_IMPORT_CLOSURE_UNRESOLVED
```

### 3.1 为什么不是实际 runtime 泄漏

W008 只观察到一个目录结构中的外部 symlink；它没有证明：

- 候选入口依赖该 symlink；
- `sys.path` 包含该目标；
- Python executable 或任一 `mquant*` 模块来自该目标；
- 候选使用混合 TIS；
- 候选与锁定 TIS／FRP 不一致。

W008 自己也明确把分类范围限定为“结构准入失败”，并说明没有发生运行时导入来源泄漏。

### 3.2 为什么不能直接形成 Owner 运行前置

C0025/W008 增加的“候选三层内存在任意外部 symlink 即一票否决”不是原 E Skill／Workflow 的完成条件，也不是 D006 的验收 Gate。它没有限定 symlink 是否属于 Python 入口、package origin 或实际 import closure，因而在尚未读取候选 provenance 和入口前产生了假阻断。

原 E Workflow 对此类问题的要求是：

```text
只是 import／路径／已确认 API 等机械问题
且 D/C/实例/位置基准未变
→ 续发新的 W1 revision
```

因此，C0025 中“W008 任一门禁失败即收敛为 `EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED`”被本调用限域修订：只有真实入口、锁定来源或 import closure 核验失败，才形成外部运行前置。

### 3.3 B／C／D／E3 分流

- **不返回 B**：没有触达 F 表或观察位置；
- **不返回 C**：没有候选图，展示合同未被证伪；
- **不返回 D**：D/C3 未修改，实例、字段、位置和展示接线未被反证；
- **不进入 E3**：没有 HTML；
- **不进入 E4/W2**：图尚未接受，`DATA_READY=false`。

## 4. 已签发 W009

### 4.1 正文

`daowei2026/observe-iterate@25134e058ab944a2e5f1a40684790b4b4c2b49ef:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W009/ORDER.md`

### 4.2 机读工单

`daowei2026/observe-iterate@320425cd9892294409135acea5657f6fdacf2b17:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W009/ORDER.json`

### 4.3 W009 的唯一专业目的

仍只核验同一现有候选：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
```

W009 不跟随 `runtime/.codex`，但也不因它存在本身判 FAIL。只有候选实际入口或 origin probe 证明代码／模块来自该外部目标时，才判真实外部来源泄漏。

W009 必须完成：

1. 读取候选已有 `provenance.json` 和候选自身已有入口／manifest；
2. 识别既有正常入口，不新建任何运行包装；
3. 将 FQV 构造文件和 F/Q/V wrappers 与锁定 TIS commit 做字节／hash 核对；
4. 核对构造所需 `mquant.tis` 模块来自同一候选 TIS root；
5. 核对候选自身 provenance 是否绑定锁定 FRP commit；
6. 使用候选既有入口做不调用 `make_features` 的 origin probe；
7. 只有来源单一、锁定一致时，才运行原 D 一次。

### 4.4 边界没有扩大

W009 继续禁止：

- 第二 runtime 搜索；
- overlay、分层 `__path__` 或多 TIS 拼接；
- 安装、构建、版本切换、文件复制或软链；
- 新建 wrapper／activation／launcher／`.pth`／`sitecustomize`；
- 修改 TIS、FRP、m3、uplot、D 或 C3；
- producer、Q/V、W2 和正式导出。

## 5. W009 后的确定分流

### 5.1 来源准入通过并生成 HTML

```text
W009 Return
→ E2 消费来源与运行事实
→ E3 核对最终图与 D/C2
```

### 5.2 来源准入通过但 D 出现新阻断

```text
W009 Return
→ E2 消费新的首个真实阻断
→ 按原 E Workflow 分类
```

### 5.3 真实来源准入失败

若既有入口、TIS 锁定、TIS 单一完整来源、FRP provenance 或 origin probe 任一失败：

```text
EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

此时不再签发环境探测型 W1；由本 executor 向原 manager／Owner 提出明确运行前置。主控和 Worker不得自行设计 overlay、构建或版本切换方案。

## 6. 当前真实状态

| 项目 | 状态 |
|---|---|
| D006 | 继续有效 |
| W008 | `STOP`；已由 E2 正式消费 |
| W008 分类 | 工单门禁假阳性；候选真实来源仍未核验 |
| W009 | 已发布，**尚无真实物理发送回执** |
| 物理 Worker | `codex:OI-U2-F-OBS-20261118-01:worker:W1`；C0026 输入确认当前 idle、无在途、workspace 租约已释放 |
| 候选 HTML | 无 |
| E3 | 未开始 |
| E4/W2 | 未准入、未签发 |
| DATA_READY | `false` |
| E 专业状态 | `IN_PROGRESS` |

发布 W009 文件不等于物理派发，不等于候选 runtime 通过，更不等于 E 完成。

## 7. 主控最小后继

主控只需按现行 V2 做 W009 派发前核验：

- 收件线程仍为本 Run 专用 W1；
- W008 已结束，当前没有 UNKNOWN／IN_FLIGHT 冲突；
- cwd 仍为 `/dwdhome/fy/BASE_E6_2_copy`；
- 当前 Binding 的 `caegraph_run_and_repair` grant、写面、ORDER.md／ORDER.json 与 `issuer_call_id=C0026` 成立；
- 原样发送，不重新加入 W008 的“任意外部 symlink 一票否决”，也不增加第二 runtime、overlay、构建或版本切换。

W009 完整 Return 必须回本 `executor:E2`。收到后继续同一：

```text
D006
OI-U2-F-OBS-20261118-01-WI-E-R1
OI-U2-F-OBS-20261118-01-M-E-R1
```

## 8. 本次专业状态

```text
professional_state = IN_PROGRESS
accepted_worker_refs = [W008]
issued_order_refs = [W009]
continuation = W009 Worker Return → original executor:E2
owner_request = null for this call
```

本调用没有声明 E 完成、没有声明图通过、没有声明 F 产品不存在、没有声明 `DATA_READY`。
