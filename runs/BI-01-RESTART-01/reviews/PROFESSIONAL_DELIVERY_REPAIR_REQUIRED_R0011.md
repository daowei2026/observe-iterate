# R0011 专业回交仍需窄范围修复

## 结论

R0011 已由原专业角色在同一物理会话中真实执行，并形成相关联的远端 `turn complete`：

- invocation：`BI01-RESTART-01-R0011-afd3d0d18eeb71e22dd435b021194733`
- assignment token：`f2aada55acf9682f6d5f1cf3622746d0`
- turn-complete commit：`10d9ef61eab458257c2c45b44040aaecfde46b45`

原先的 `CONTINUATION_MISMATCH` 已修正：`question_work_check.association_errors=[]`；双 Return 中的 11 个唯一 Git locator 均能定位，所有非全文 selector 均唯一。

但本轮仍不能进入管理 G6。锁定的 `runtime/overlay/tools/longrun_handoff.schema.json` 对 R0011 `ROLE_RETURN.json` 的验证失败：

```text
Additional properties are not allowed ('active_conflict_ref', 'g6_self_check_ref' were unexpected)
```

失败位置为 `role_outputs.professional`。两个字段沿自 R0010，并非操作端或 R0011 运输阶段新增；这不改变“当前回交不符合锁定 schema”的事实。

## 合法处置

操作端不得自行删除、迁移、解释或改写专业字段。恢复手机并补齐 R0011 完整原答后，必须向同一个原专业角色会话 `BI01-RESTART-01-I6-ACTION-CLOSE` 派发新的窄范围 `DELIVERY_REPAIR` invocation，由原专业角色决定并交付：

1. 符合锁定 `longrun_handoff.schema.json` 的 `ROLE_RETURN`；
2. 与该新 invocation、assignment token 和原 I6 Binding 精确关联的 `QUESTION_WORK_RETURN`；
3. 保持已经形成的 I6 业务判断不扩写、不重判；
4. 保持 continuation、remaining 和 `question_work_ref` 关联一致。

在新一轮 schema、关联、locator、完整回复和通用 `after-return` 全部通过前：

- 不得派发管理 G6；
- 不得把 R0011 标为业务接收完成；
- 不得声明 I6 或本 run 已结案。

本记录是回交完整性 Gate，不代替专业或管理业务判断。
