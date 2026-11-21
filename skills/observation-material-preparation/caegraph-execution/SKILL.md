---
name: caegraph-execution
stage: E
summary: 由同一 Codex E executor 连续完成真实 CAEGraph 运行、诊断修复、核图、正式取数和一致性核对；专业完成条件与上游回流不变。
---

# E｜CAEGraph 执行／运行

## 执行主体与定位

本 Skill 默认由**独立 Codex Skill executor** 在本 Run 已授权的 Linux 工作区直接执行。E1～E6 是同一项专业 Skill 内部工作，不默认派发独立 Worker、W1 或 W2；普通诊断、修复和重试不要求跨 Chat 重新签工单。正式 Run 仍以 Owner GO、D 委派、RUN_BINDING、真实物理线程与授权为准；本文件本身不创建线程或增加授权。

E 自己负责：真实运行、授权范围内的工程诊断与修复、候选结果分类、必要的共享 Feature 理解或 B/C/D 回流、按 D/C2 核对图、图接受后形成正式取数准入、导出图数据、检查一致性并交付。

## 执行优先

- E1 只固定 D 完整脚本、C2 当前预期 HTML、真实工作区/运行入口、输出目录与已有授权；不得先制造大型环境审计作为正常前置。
- 直接尝试真实运行，依据日志和现场事实连续定位、修复、再运行。可自主探索**获准范围内**的工程路径；不能因为一次普通 import、路径或 API 错误就停止整个 Skill。
- 环境来源、版本和依赖仅在实际影响运行、语义、可复现性或授权时展开；不能凭无关 symlink 或自行增加的准入条件一票否决。
- 日志、diff 和实际运行结果优先承载事实，报告保持最小充分。旧 W1/W2 模板不是本模式的必经输入或输出。

## 输入与输出

输入：当前有效 FeatureUnderstandingPackage、D 完整 CAEGraph 定义、C2 当前展示预期和 HTML、外层特征实例与 B 位置、真实工作区和运行入口、输出位置、Owner/D 授权及所锁定的版本。字段级合同见 [IO_SPEC.md](IO_SPEC.md)。

最终应交付：真实运行的最终脚本和 HTML、运行/修复日志及 diff、与 D 和 C2 的核图结果、正式取数准入、对应图层的数据及最小映射、图与数据一致性检查、限制和未完成项。内部方法见 [WORKFLOW.md](WORKFLOW.md)。

## 必须保留的边界

- 不自行更换品种、观察时间、尺度、实例、字段、数据入口、图元或展示业务含义；这些改变按原 Workflow 返回 B/C/D；对象、状态、事件和字段的语义来源不清时返回共享 Feature 理解。
- 不用合成/预览/近似数据冒充真实特征结果；不执行任务明确排除的 producer，不暗中切换锁定源码版本。
- 可自行**调查和提出**环境修复方案，但安装、重建、改变受保护平台、混用未经验证的 package 或超出 Owner grants 的写入，须先取得合法授权；不把“需授权动作”伪装成机械小修。
- E3 必须核对真实图与 D/C2，不能以生成 HTML 或静态检查代替视觉/数据验证；环境无法可靠核图时说明限制，不虚报接受。
- **只有 E3 接受图后才能进入 E4 正式取数；**正式数据必须来自已接受的脚本、HTML、实例及有效运行，E5 核对后才可标为 DATA_READY。
- Codex executor 直接执行时的权限、实际 cwd、单写者与线程回执必须在主控合法派达前按 V2 核验，不因为零 W 而省略。

## 完成条件

真实图经过与 D/C2 的核对并明确接受，正式图数据已取得且与图一致，脚本、HTML、数据与执行事实可追溯，所有影响下游的限制已说明，方可报告 DATA_READY。尚缺必需材料则按实际范围报告 PARTIAL_WITH_LIMITS 或 BLOCKED，不以一次执行结束代替专业完成。

历史 Web executor + Worker 方式曾使用 [WORKER_DELEGATION.md](WORKER_DELEGATION.md)、[RUN_REPAIR_ORDER_TEMPLATE.md](RUN_REPAIR_ORDER_TEMPLATE.md)、[DATA_EXPORT_ORDER_TEMPLATE.md](DATA_EXPORT_ORDER_TEMPLATE.md)；它们只供历史 Run 按原锁定版本解释，**不是本版 Codex 直接执行的附加前置**。
