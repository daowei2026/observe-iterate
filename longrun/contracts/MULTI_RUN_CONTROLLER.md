# 多 Run 主控合同 V0.1（候选；仅主控运行层）

> 来源：现有 LONGRUN_PROTOCOL_V2。状态：已规定如何教主控做事，尚未改动 cgpterm 主控 Skill 或完成真实物理通道联调。此文件不重新定义业务控制面或专业 Skill。

## 1. 目标与非目标

一个主控 Codex 可在多个独立 Run 之间交错完成真实派发、回收、对账、恢复和机械事实维护。每个 Run 的管理 Pro、执行 Pro、业务材料、Gate、进度和运行交接完全独立。一个 Run 等待外部回执时，其他合法 Run 可继续。

不建立多用例专业管理 Pro，不把多 Run 调度交给管理 Pro，不新增 M/R 专业步骤，不替换已有 C/D/W 合同，不开发第二套消息执行器/轮询器，不声称当前有生产级锁服务。当前单 Run 的完整协议仍由 LONGRUN_PROTOCOL_V2 规定。

## 2. 身份层次

- business_case_id：业务用例稳定标识；运行索引中的归类字段。未单独设定时可明确使用 work_id 作为归类值，不新增伪造业务任务。
- work_id：既有跨 Run 业务目标；同一用例可有不同工作目标。
- run_id：一次真实 Owner GO 对应的不可复用运行身份。
- (run_id, call_id)、(run_id, delegation_id)、(run_id, work_order_id)：独立路由键。C0001/D001/W001 可在不同 Run 重复；不同类型的键也不能互换。
- 业务 question_id/work_item_id/analysis_round_id/expectation_version 等继续只在所属 Run 的业务上下文解释。

每 Run 唯一管理 Pro。其他角色、授权、物理会话映射、具体成果、行动序列均带 run_id；不得把逻辑身份字符串当成真实 ChatGPT 会话或 Codex thread。

## 3. 首版 Linux 工作区规则（2026-11-16 Owner 补充）

**不同 run_id 使用不同 Linux 工作区，工作区由 Owner 在准备任务时先行准备并在各 Run 的真实 GO 中给出绝对路径。**

主控不自行创建、克隆、分配、搬迁或选择备用工作区；不得因为当前 cgpterm 旧文档提到 /dwdhome/fy/BASE_E6_2 就把它当成所有新 Run 的默认工作区。一个 Run 的实际 Linux Worker 线程应以该 Run 真实 GO 所指定路径为工作现场。

主控注册 Run 时须核：
1. 真实 GO 提供绝对 Linux 路径，写入 Run 资源绑定；
2. 与当前未结束的其他 Run 的工作区在路径上不相同、不存在父子包含；
3. 在目标 Linux Worker 主机上验证目录实际存在、realpath、目录权限，防止软链接指向相同目录；目标 Worker 所使用的实际工作目录和真实写权限在首次操作时还要核实；
4. 仅当该 Run 的真实 Owner grants 和 D/W 写面覆盖具体动作时，才允许执行；
5. Run 的本地目录互异，并不证明远端 Git 分支、数据库、缓存、共享文件/输出路径互异。若两个 Run 仍写入同一外部目标，应分别核实际单写者或只阻断冲突动作，不因此阻断无冲突的其他 Run。

资源路径变更必须依据新 Owner 指令/授权写入修订记录，重查与所有活跃 Run 的重叠关系。不可无痕改路径。第一版**不实现共享 Linux 工作区的自动锁管理器**；工作区冲突直接拒绝该 Run 的相关动作，要求改用 Owner 提供的另一个合法工作区。

## 4. 文件边界和唯一可信事实

- 单 Run 正式原件继续在 longrun/runs/<run_id>/ 内，结构不变；增加每 Run 的 RUN_RESOURCE_BINDING.json（操作现场与来源记录）。
- 全局 RUN_REGISTRY.json 只记录 Run→真实 Binding、资源、采用协议及 Owner 工作区路径的索引，提供寻址/交叉检查；不得在其中复制专业 Gate/TaskProgress 当作新权威。每个 runs[run_id] 条目固定包含 run_id、work_id、business_case_id、binding_ref、resource_binding_ref、owner_workspace_path、adopted_protocol_ref；其中三个 ref 均为实际存在的精确 Git 引用，路径分别指向所属 Run 的 RUN_BINDING.json、RUN_RESOURCE_BINDING.json 和所采用 LONGRUN_PROTOCOL_V2.md。该 Registry 是可重建的索引，不自动保存全部原始回执。
- 单 Run action ledger、物理发送回执和本次被接收的管理决定才是下一动作依据；索引若与已验证事实不一致，标记过时，先修复/重建，不用索引覆盖原始记录。
- RUN_REGISTRY 的空文件只代表尚无从本索引合法登记的 Run，不代表全仓或其他分支历史 Run 不存在。真实 GO 首次接收前必须对已有可信索引及远端实际 Run 身份做交叉核查。
- 采用的协议、业务控制面、管理/执行 Pro 指南与专业 Skill 均使用 owner/repo@40位commit:path。源版本和运行记录的后续 Git commit 是不同的身份；普通提交不自动升级既有 Run。
- 敏感物理会话凭证和不适合放仓库的传输日志保存在现有可信执行设施；索引只能放允许公开的精确引用，不将私密运行令牌作为公开 Git 记录。

## 5. Run 注册与接续的强制顺序

新 Run：核真实 GO → 核 run_id 不重复 → 核采用来源 → 先核 Owner 提供的路径与现役 Run 工作区不重叠 → 在 Linux 现场核目录/realpath/权限 → **先发布**单 Run Binding、资源记录并取得准确不可变 commit → 将这些实际存在的精确引用写入候选 Registry 并执行结构和 Linux 主机核查 → 以条件写入正式采用索引 → 开始按 V2 发送首个管理 Pro C。不能让 Registry 预先引用未发布的绑定原件；没有真实 GO 或资源未核实，不得假称 Run 已可派 Worker。

每次唤起主控：
1. 从可信执行账本/原物理通道收集新回执和 UNKNOWN 动作；不得先依 Registry 推断已经送达。
2. 按 (run_id, action_type, action_id) 核对原始 C/D/W、token、源 refs、物理端和提交；未知效果先查原发送端，禁止直接重发。
3. 将已验证结果路由至**同 Run 原签发人**；在需要专业业务决定时交回该 Run manager，不从结果文字推断新的 Gate 或后继。
4. 将合法已具备前置的待派动作按已声明优先级和进入待派队列次序处理；当前无优先级指令时仅使用先到先处理，不因业务题目自行排列优先级。
5. Run A 等待、阻断、暂停不占住 Run B 的非冲突工作。发生资源/权限冲突时只阻断受影响动作，保存解除条件。
6. 每次动作真实状态变化先持久化本 Run 事实，再按最新事实刷新索引；不能凭 GitHub 文件存在判断消息已送达。

现有 longrun_gate.py 继续按单 Run 可信快照执行机械检查；新 multi_run_check.py 是跨 Run **只读**结构/路径核查器；不发消息、不取锁、不取得 GitHub 或 Linux 远端凭证。

## 6. 版本与 Agent 能力演进

专业 Skill / Pro 指南、运输合同、主控实现三类版本分别登记。Run 按真实 GO 采用的精确专业来源执行；改变专业方法须由有权的该 Run 专业/Owner 流程形成明确采用记录，不因分支新提交自动切换。主控机械程序可以演进，但必须能解释旧 Run 采用的合同；不兼容时给出显式迁移和核验记录，不覆写旧 Run 事实。

不得为了升级共享 Agent 文档而直接改写多个活跃 Run 的专业状态或输出。新的 Run 可以采用新版来源，旧 Run 继续按原合同运行。

## 7. 当前生效限制与后续接线

本分支只是多 Run 合同、模板、只读检查器和测试；**没有修改 cgpterm**。现役 cgpterm@becfbcbc7eec3e4fc6a44cd0b0a7a934ec666ff8:.agents/skills/observe-iterate-longrun-v2-controller/SKILL.md 仍有旧 Linux BASE 路径与单 Run 主控步骤。其未完成多 Run 适配前，不能宣称不同 GO 路径已被现役主控支持，亦不得绕过现役 Skill 的真实发送规则。后续接入清单见 controller/CGPTERM_ADOPTION_PENDING.md。
