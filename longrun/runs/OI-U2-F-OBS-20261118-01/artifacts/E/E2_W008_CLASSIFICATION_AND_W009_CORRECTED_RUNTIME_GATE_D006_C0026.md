# E2｜消费 W008，纠正过宽的 symlink 准入门并建立 W009

## 1. 身份与已消费 Return

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `call_id`: `C0026`
- 已消费 Worker Return：`daowei2026/observe-iterate@be3f2f9c2102fc182909140234921f7ad3d4457b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/WORKER_RETURN.json`

W008 的身份、原工单引用、Worker 和回交路径成立。本 E2 接受其事实与实物。`outcome=STOP` 合法结束 W008，但不自动结束 D006/E。

## 2. W008 真正证明了什么

W008 只完成候选目录检查的最前一步：

```text
CANDIDATE=/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
```

已证明：

1. 候选根、`runtime/`、`runtime/mquant/`、`runtime/mquant/tis/` 都存在，且这些必需路径本身不是 symlink；
2. 候选根存在普通文件 `provenance.json`，大小 1217 bytes；
3. `runtime/.codex` 是指向 `/dwdhome/fy/BASE_E6_2_copy/.codex` 的外部 symlink；
4. Worker 没有跟随该链接、没有读取目标、没有加载候选代码；
5. 目录清单在该点立即停止，`bounded_listing_complete=false`；
6. 候选已有入口、TIS 四文件、TIS 完整性、FRP provenance、origin probe、D/C3 hash 和原 D 运行均未检查；
7. D 启动 0 次，没有 HTML 或 definition report，也没有环境或业务修改。

所以 `DEDICATED_RUNTIME_EXTERNAL_SOURCE_LEAK` 只能解释为：

> W008 的目录级门禁观察到候选根外 symlink。

它不能解释为：

> Python 已经从外部来源导入；候选 TIS 是混合包；候选 runtime 不符合锁定版本；或当前必须建设新环境。

## 3. 对 C0025/W008 专业门禁的纠正

W008 Worker 严格执行了 ORDER；错误不在 Worker。

问题在于 C0025 签发的 W008 将“候选三层以内存在任意外部 symlink”设为一票否决。这一条件：

- 不是原 E Skill／Workflow 的完成条件；
- 不是 D006 绑定的额外验收 Gate；
- 未限定 symlink 是否属于 Python 入口、`sys.path`、package origin 或实际 import closure；
- 导致尚未读取候选已有 provenance、尚未识别入口、尚未核验包来源就提前停止；
- 与原 E Skill 的“先取得真实运行反馈，机械 import／路径问题在基准不变时续发 W1”不一致。

因此，C0025 中“W008 任一 runtime gate 失败即直接收敛为 `EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED`”在本次事实下不能直接适用。该承诺被本 C0026 **限域修订**：只有实际入口／import closure／锁定来源核验失败，才形成外部运行前置。

## 4. E2 专业分类

```text
W008_ORDER_GATE_FALSE_POSITIVE
+
DEDICATED_RUNTIME_PROVENANCE_AND_IMPORT_CLOSURE_UNRESOLVED
```

| Workflow 后继 | 判断 |
|---|---|
| 返回 B | 否；未触达观察位置或真实 F 表 |
| 返回 C | 否；没有图，展示合同未被证伪 |
| 返回 D | 否；D/C3 未被修改或反证 |
| 进入 E3 | 否；没有 HTML |
| 进入 E4/W2 | 否；图未接受 |
| 基准不变时续发 W1 | **是；签发一次纠偏后的 W009** |

本次不搜索第二个 runtime，不建设环境，不恢复旧 overlay。W009 仍只检查 W007 已发现的同一候选。

## 5. W009 的纠偏边界

### 5.1 `.codex` symlink 的处理

```text
runtime/.codex
```

只记录，不跟随，也不因其“存在”本身判 FAIL。

只有当候选已有 launcher／activation 实际依赖它，或 origin probe 表明 Python executable、`sys.path`、`mquant*` 模块来自该外部目标，才判定真实外部来源泄漏。

### 5.2 必须完成的有界检查

1. 读取候选已有 `provenance.json` 和候选自身已有的入口／manifest 文件；
2. 识别候选已经存在的正常入口，不新建 wrapper／activation／`.pth`／`sitecustomize`；
3. 比较 FQV 构造文件及 F/Q/V wrappers 与锁定 TIS commit；
4. 核对运行所需 `mquant.tis` 模块是否来自单一候选 TIS root；
5. 核对候选 provenance 是否明确绑定锁定 FRP commit；
6. 用候选已有入口做不调用 `make_features` 的 origin probe；
7. 仅在来源单一且锁定一致时运行原 D 一次。

### 5.3 继续禁止

- 第二 runtime 搜索；
- overlay、分层 `__path__` 或多 TIS 拼接；
- 安装、构建、切换版本、复制或软链 package 文件；
- 修改 TIS／FRP／m3／uplot／D／C3；
- producer、Q/V、W2 或正式数据导出。

## 6. W009 后的确定后继

```text
来源准入通过 + 生成 HTML
→ E3 核图。

来源准入通过 + 原 D 新阻断
→ E2 按首个真实阻断继续分类。

入口、TIS 锁定、FRP provenance 或 import closure 失败
→ EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
→ 不再签发环境探测型 W1
→ 向原 manager／Owner 提出明确运行前置。
```

## 7. 当前续接点

```text
D006 / WI-E-R1 / M-E-R1
E state = IN_PROGRESS
accepted worker = W008
next native action = W009 corrected W1
E3 = not started
E4/W2 = not admitted
DATA_READY = false
```
