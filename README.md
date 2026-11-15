# 观察迭代 Agent

这是观察迭代专业 Agent 的长程运行仓库候选。第一轮以 CYF 的“专业 Agent 长程运行”体系为母版：保留通用运行机制，将仅声明性使用 Mission A/B/C 的地方改成角色化表达；真正需要专业内容的地方改为读取 `professional/` 和当前有权任务。

```yaml
status: candidate_scaffold
validated_runnable: false
owner_acceptance: pending
real_phone_pilot: PRIOR_EXPERIMENT_STOPPED_NEW_RUN_NOT_STARTED
professional_interface_completeness: PARTIAL
```

## 当前内容

- `runtime/`：长程运行规则、协议、工具、配置和发布候选。
- `professional/source/`：只提取原 00—08 中与观察迭代专业 Agent 直接相关的内容；不复制其它业务资料。
- `professional/interfaces/`：运行系统消费的专业接口；没有来源支持的部分保持 `MISSING`。
- `runs/BI-01-RESTART-01/`：下一次独立新运行的预备工作面；不继承旧 I4/Gate/聊天。下一次真正管理才形成地图、当前任务及 R 轮。运行入口见 `runtime/operations/BI01_REAL_RUN_V1.md`。
- `migration/`：CYF 基线、角色—文件—依赖分析和迁移状态。

## 边界

主控只处理身份、来源、派发、回交和合法接续，不生成专业判断。管理 Pro 负责完整目标、任务签发、Gate 接收和后继。执行 Pro 负责观察、挑战、证据、结果及原任务内续作。Worker Codex 只承担有权计算、制图或工程工作。

当前 repository 不是已部署系统。测试通过只证明相应结构与代码路径，不证明专业判断、手机发送、真实采用或端到端运行。
