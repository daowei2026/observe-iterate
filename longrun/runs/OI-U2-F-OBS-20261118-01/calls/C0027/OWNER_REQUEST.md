# C0027｜Owner 请求：为 D006 明确锁定 FQV runtime 前置

## 1. 请求身份

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `requester`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `return_via`: `chatgpt:OI-U2-F-OBS-20261118-01:manager`
- `call_id`: `C0027`

专业分类原件：

`daowei2026/observe-iterate@982ec813a5bccb2f798417adeab92b31eb38d808:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W009_RESULT_CLASSIFICATION_AND_OWNER_RUNTIME_PREREQUISITE_D006_C0027.md`

## 2. 已确认的阻断

W009 已确认：

- 候选已有入口可用；
- 锁定 TIS 的构造文件和 F/Q/V wrappers 字节一致；
- 候选本地 TIS 所需包路径存在；
- 候选 provenance 记录锁定 FRP commit；
- 13 个指定模块均可导入；
- 但一次真实 origin probe 加载的 260 个 `mquant*` 模块中，有 165 个物理来源解析到候选 runtime 根之外。

精确分类：

```text
EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

这意味着当前候选的整体 `mquant` import closure 仍是混源，不能在 Owner 已明确的“不得重建 TIS package、不得构造 overlay、不得混合 package、不得自行切换版本”边界内继续运行原 D。

## 3. 请 Owner 明确选择

### A｜指定现有合格 runtime

请提供或指定一个已存在、获准且可复核的 runtime／入口，使：

```text
- TIS 对应锁定 tis@2f460d663d821cf2ba25555eda13e78b697d0767；
- FRP 对应锁定 frp@67711c492da909ed0f044f357beb278abf7fc71c；
- 全部实际 mquant* import closure 来自一个明确、单一、可追溯的 runtime；
- 不需要 overlay、混包、安装、构建、复制或版本切换；
- 实际工作区、入口和当前 Binding／授权相符。
```

选择 A 后，D006 从新的 W1 运行原 D 继续；A～D 不重跑，不直接启动 W2。

### B｜授权独立环境对齐工作

若没有现有合格 runtime，请另行明确：

```text
- 目标 runtime／源码版本组合；
- operation；
- execution_context；
- allowed_writes；
- 允许／禁止的构建、安装、复制、symlink、版本切换动作；
- 单一运行来源的验收证据。
```

该工作不属于当前 D006 已有机械修复授权。选择 B 后，应先由 manager 在新授权与更新后的 Binding 下安排环境前置；前置完成后再恢复 D006。

### C｜停止 D006/E

若不提供现有合格 runtime，也不授权环境对齐，请明确停止本次 D006/E。收束记录必须保留：

```text
- 没有候选 HTML；
- 没有 E3 图接受；
- 没有 E4/W2 正式取数；
- DATA_READY=false；
- F 产品不存在未被证明；
- A～D 既有成果没有被 W009 反证。
```

## 4. 当前状态与恢复条件

```text
professional_state = WAITING_OWNER
issued_order_refs = []
current blocker = EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

只有 Owner 对 A／B／C 作出明确选择，并由 manager／主控完成相应合法调用、Binding 与授权后，D006 才能继续或被有据收束。
