# BI-01 / RESTART-01 — I4/G4 限定通过，I5 Owner Pack 启动

**R0005_PROFESSIONAL_RETURN_RECEIVED / CASE02_G3_SCOPED_PASS / I4_G4_PASS / I5_STARTED / G5_PENDING / OWNER_NOT_YET_ASKED**。

<a id="common"></a>
## 运行身份与历史隔离

- run：`BI-01-RESTART-01`
- work：`BI-01`
- 当前 task：`BI01-RESTART-01-I5-OWNER-PACK-01`
- 当前 mode：`OBSERVATION_I5`
- 管理会话：`BI01-R01-管理`
- 下一专业会话：`new:BI01-RESTART-01-I5-OWNER-PACK`
- 旧 `BI-01-IT-01` I4 试跑不继承为本 run 的成果、Gate 或在途。
- R0003/R0005 是本 run 的 I4 专业结果；R0004/R0006 分别完成 Case-01 接收和 I4 阶段接收。

<a id="bi01"></a>
## 当前业务状态

R0006 已决定：

- Case-02 G3 `ScopedPass`；
- 接收 CF-02-01、CF-02-02、NI-02-01、DF-02-01；H-02-01 保持 Hypothesis；
- 当前 Reference/Shadow 范围内 I4/G4 `Pass`；
- I4 阶段结束，不追加第三 Case；
- I5 启动，目标是形成 Owner 可直接判断的 Pack；
- 当前不需要 I2/I3 补证、Worker 或正式工程；
- Owner 尚未收到选择题，G5 尚未判断。

核心业务边界：

```text
已成立：
  U2 对身份、时间、生命周期和证据定位有组织价值。

未成立：
  exact 组织是稳定机会边界；
  当前 Reference assessment 是正式 Quality；
  当前 U3 形成独立投资增量。
```

## 生效材料

- `00_长程推进地图.md`
- `01_当前任务.md`
- `reviews/MANAGEMENT_GATE_DECISION_R0006.md`
- `bindings/QUESTION_WORK_BINDING_I5.json`
- `artifacts/I4_R0003/REPORT.md`
- `artifacts/I4_R0005/REPORT.md`
- `runtime/config/WORKMAP_BINDING.json`

## Owner 决策框架

- **A（管理建议）**：保留组织/可追溯价值，暂停把成员选择与 Quality 当成既成能力，结束当前 reference 观察；
- **B**：只有具名 consumer 时，授权 formal 方法和独立 Case 的有界验证；
- **C**：直接正式工程，当前证据不足，不建议。

## 运行后继

管理落库不等于 I5 已发送。操作端必须在新 exact commit 上完成：

1. remote readback；
2. workmap snapshot / reader / intake；
3. binding 与 pre-dispatch；
4. 新 I5 专业聊天 NOT_SENT / 去重检查；
5. 通过后才创建并发送 I5 专业任务。

I5 Pack 完成后返回管理；管理判断 G5、定向补 Pack 或 WaitingOwner。不得自动进入 I6。
