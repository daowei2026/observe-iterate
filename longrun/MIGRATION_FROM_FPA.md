# 从旧 feature-production-agent/longrun 提取与舍弃的决定

旧仓库基线：`daowei2026/feature-production-agent` 的 `codex/m3-implementation-runtime-integrated/longrun`。本目录不是原仓历史 Run 的继续，不修改原目录及其历史记录。

| 旧文件/能力 | 新版处置 | 说明 |
|---|---|---|
| `LONGRUN_PROTOCOL_V1.md` 的任务/Run/R/W 区分 | 抽取到 `LONGRUN_PROTOCOL_V2.md` | 增加 D 专业委派、分别路由 Executor/Worker 返回，取消“固定一个 Pro 作为所有 Worker return_to” |
| `longrun_schema_v1.json` | 全新 V2 schema | Binding 含 manager/executors/workers；专业委派与工单分开，禁止用旧 schema 校验新实体 |
| `fpa_longrun_gate.py` | 只保留适用的机械校验原则；新建 `longrun_gate.py` | 保留身份、精确引用、授权子集、回执与状态对账概念；去掉特征 key、Runner/团队身份等硬编码 |
| `fpa_evidence_manifest.py` | 不整体复制 | 旧工具可作为精确 GitHub SHA 证据的参考；新版尚未重新实现远端哈希核验 |
| `PRO_MANAGER_GUIDE.md` | 不迁入 | 特征生产阶段/Runner/Agent/归档的专业用法，专业负责人新职责另备 |
| `WORKER_EXECUTION_GUIDE.md` | 不迁入 | 旧 Worker 围绕特征生产 Runner 的特定操作；通用执行约束通过 V2 合同+具体 W 表达 |
| `PRO_DECISION_TEMPLATE.md` | 不整体迁入 | 专业决定不能等同 Owner 授权；新业务决定格式由各专业域管理 |
| `OWNER_GO_Hp3LtCompressionProfile.md`、`OWNER_GO_AUTONOMOUS_FEATURE_PRODUCTION.md` | 不迁入 | 历史横盘/夜间特征生产授权、固定 Linux 路径不通用 |
| `runs/FPA-*` | 继续保存在旧仓库 | 真实旧证据不会改名伪装成新 Run；以后可用做迁移回归 |
| 旧的 `cgpterm` 主控 Skill | 尚未更换或联调 | 另仓的物理收发、线程绑定、任务接续需要独立升级和真实验收 |

## 为什么不是照搬 V1

旧校验实际写死：`pro=chatgpt:<run>:pro`、`worker=codex:<run>:worker`，且工单 `issuer_ref == return_to == pro`；后继只能按 `worker / continuation` 路由回原专业负责人。新关系有独立的“专业执行任务 D”：管理 Pro 签 D；执行 Pro 签 W；Worker 回执行 Pro；执行 Pro 回管理 Pro；执行 Pro 也可零 W 自行完成。直接更名字段会把签发权、接受权及完成条件搞错。

## 当前验收断言

本次只迁移**通用长程运行层**，不让原特征生产流程成为通用流程；业务控制层的 L0/L1/L2、专业 Skill、候选 Gate 继续原地保留，不在 `longrun/` 重复一套。旧实现任何曾经成功的局部离线测试，也不等于 V2 新角色的真实物理收发已经验收。
