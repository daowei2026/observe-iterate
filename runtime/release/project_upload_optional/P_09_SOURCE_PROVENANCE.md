# 来源与导入边界

导入日期：`2026-09-14`。目标仓导入基线：`20254fb8bd36a769a00be02a73bf98ad36732494`。

## Python／Numba 来源

来源工作树是 `mquant/docs` 的 `docs/agent-workflow` 分支，检查时 `HEAD=f2972195eec5f51b0b2425856a8917b094333a7e`：

|文件|导入状态|
|---|---|
|`03A_output_contract_and_encoding_checks.md`|tracked clean|
|`03B_scope_and_artifact_boundary_checks.md`|tracked clean|
|`03C_runtime_shape_and_hotpath_checks.md`|相对 HEAD 有工作树修改；本包锁导入字节 SHA，不冒充 HEAD 原文|
|`07_cross_language_product_handoff.md`|尚未被来源仓跟踪；本包锁 filesystem bytes，不伪造 upstream commit|

## Haskell／FRP 来源

四份正文来自 `edh-universe/docs/ssot/frp/`。当前工作区没有为该路径发现可用 Git 根，因此只记录来源路径、导入字节数和 SHA-256，不声明不存在的 repo/ref。

## 维护规则

1. 上游文档继续是各自宿主职责内的来源；本包是 Agent 体系的单一 vendored snapshot。
2. 更新任一正文时，先取得新来源身份或诚实的 filesystem snapshot，逐项比较内容和适用边界。
3. 更新 `REFERENCE_MANIFEST.yaml` 与 `SHA256SUMS.txt`，并评估 Mission B 工程设计、B→实现者 handoff、Mission C 和 runtime projection 是否需要重基线。
4. 不在本包副本直接修订平台规则；规则变化先回上游 owner 文档，再导入新包版本。
5. 包内 snapshot 不证明当前源码 API、caller、writer、consumer 或 runtime 性能，任务仍须 exact live read。
