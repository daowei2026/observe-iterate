# BI-01 / RESTART-01 — Case-01 限定接收，I4 继续成员选择增量检验

**R0003_PROFESSIONAL_RETURN_RECEIVED / G3_SCOPED_PASS / CASE01_G4_SCOPED_PASS / I4_CONTINUES / I5_NOT_STARTED**。

<a id="common"></a>
## 运行身份与历史隔离

- run：`BI-01-RESTART-01`
- work：`BI-01`
- 当前 task：`BI01-RESTART-01-I4-EXECUTION-01`
- 当前 mode：`OBSERVATION_I4`
- 管理会话：`BI01-R01-管理`
- 专业会话：`BI01-RESTART-01-I4-EXECUTION`
- 旧 `BI-01-IT-01` I4 试跑不继承为本 run 的成果、Gate 或在途。
- R0001 是首次 M-START；R0002 只修机器接线；R0003 是首个专业轮；R0004 是阶段接收与后继管理。

<a id="bi01"></a>
## 当前业务状态

R0004 已接收 R0003 的限定结果：

- Case-01 的输入身份、时间、路径和 N 基线达到 G3 限定消费资格；
- `completed_recovery_events` 的“触及 prior peak”解释为 Withheld；
- Case-01 的 CF-01、CF-02、NI-01、MF-01、MF-02 达到 G4 ScopedPass；
- I4 不结束，I5 不启动；
- 当前 focus 是 `refonly-671359b4c10f73db5c`：2021-05-10 21:30 的 HC/RB Peak/Down same-actual 诊断候选；
- 当前要检验 HC/RB 成员边界相对静态 HC/RB/I 集合是否有业务增量；
- 当前无 Owner 决策、无 Worker 工单、无专业续作已发送声明。

## 生效材料

- `00_长程推进地图.md`
- `01_当前任务.md`
- `reviews/MANAGEMENT_GATE_DECISION_R0004.md`
- `bindings/QUESTION_WORK_BINDING_I4.json`
- `artifacts/I4_R0003/REPORT.md`
- `runtime/config/WORKMAP_BINDING.json`

## 运行后继

管理落库不等于专业续作已经发送。操作端必须在新 exact commit 上完成：

1. remote readback；
2. workmap snapshot / reader / intake；
3. binding 与 pre-dispatch 检查；
4. 原专业会话在途和重复发送检查；
5. 通过后才发送同工作续作。

专业结果返回管理后，下一次管理必须在进入 I5、定向补证或有据停止/修订之间作决定，不自动追加第三 Case。
