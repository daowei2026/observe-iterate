---
name: caegraph-execution
stage: E
summary: 接收 D 的完整 CAEGraph 定义；由 E 自己完成专业判断、回流、核图、取数准入和数据一致性判断；真实运行／有限修复与核图通过后的正式取数分别通过两类 Worker 工单执行。
---

# E｜CAEGraph 执行／运行

## 定位

E 同时包含两种性质完全不同的工作，必须分开表达：

1. **E 的专业业务 Workflow**：由 E Agent 自己承担，负责消费 D、评价 Worker 回报、判断是否返回 B／C／D、核对最终图、批准正式取数、核对图与数据并形成交付；
2. **Worker 操作委派**：真实环境中的运行、权限内机械修复和正式图数据导出，由 Worker 按工单执行。

因此：

```text
E Agent 负责“判断和接受什么”
Worker 负责“按已批准工单实际运行和导出什么”
```

Worker 不负责决定图是否符合业务展示预期，也不负责批准正式取数。

## 为什么分成两类 Worker 工单

E 使用两种独立工单，不使用一张从运行一直授权到正式取数的统一大工单：

- **W1｜CAEGraph 运行与有限修复工单**：运行 D 定义，产生候选最终脚本、候选 HTML、日志和 patch；
- **W2｜CAEGraph 正式取图数据工单**：只有 E 已正式接受最终图后才签发，绑定已接受脚本／HTML／运行版本，导出正式图数据和元信息。

W2 不能在 W1 开始时提前授权，因为在最终图未通过 D／C 核对之前，尚不存在合法的正式取数基准。

详细派单合同见 [WORKER_DELEGATION.md](WORKER_DELEGATION.md)，两种模板分别见：

- [RUN_REPAIR_ORDER_TEMPLATE.md](RUN_REPAIR_ORDER_TEMPLATE.md)
- [DATA_EXPORT_ORDER_TEMPLATE.md](DATA_EXPORT_ORDER_TEMPLATE.md)

这些阶段模板补充专业内容；实际 C/D/W 身份、授权和回交仍须符合仓库通用 [WORKER_ORDER](../../../longrun/templates/WORKER_ORDER.md) 与长程协议。

## 输入概览

- D 阶段完整 CAEGraph 定义；
- C 阶段展示预期和预期展示 HTML；
- 外层特征实例；
- 实际运行环境、工作区和数据入口；
- 当前 D／Owner 授权和 Worker 操作边界。

字段级格式见 [IO_SPEC.md](IO_SPEC.md)。

## E 自己的专业 Workflow

见 [WORKFLOW.md](WORKFLOW.md)。该文件只写 E 的专业判断和阶段推进，不把 Worker 的命令、权限、修改清单和交付字段揉进业务步骤。

## Worker 派单与操作

见 [WORKER_DELEGATION.md](WORKER_DELEGATION.md)。该文件说明：

- 哪个专业节点触发 W1 或 W2；
- Worker 可以做什么、不能做什么；
- 两种工单各自输入和交付；
- Worker 结果如何原样回 E，由 E 作专业判断。

## 最终输出概览

- 实际可运行且被 E 接受的最终脚本；
- 被 E 接受的最终 CAEGraph HTML；
- W1 工单、运行、patch 和日志记录；
- 最终图与 D 完整定义的核对结果；
- 最终图与 C 展示预期／预期 HTML 的核对结果；
- W2 工单及正式 CAEGraph 图数据包；
- 图与数据的一致性核对；
- 已知限制和未解决问题。

## 完成条件

- W1 已在真实环境完成运行，所有 patch 和未决问题已回 E；
- E 已亲自核对最终脚本与 D、最终图与 C，并形成明确的图接受记录；
- 只有图被接受后才签发 W2；
- W2 导出的正式数据绑定被接受的脚本、HTML、特征实例、品种、时间和同一次有效运行；
- E 已核对图层、数据源、字段、数量、数据阶段和缺失含义；
- 最终脚本、HTML 和数据可相互追溯，或限制已准确记录。

## 不允许做的事

- 不把 E 的专业判断委派给 Worker；
- 不用一张工单提前同时授权运行修复和正式取数；
- 不让 Worker 自行选择观察位置、改变展示预期或决定图是否通过；
- 不以调试期间临时读取的数据冒充 W2 正式图数据；
- 不在最终图核对前签发正式取数工单；
- 不用脚本运行成功替代图形与业务语义核对；
- 不把图的数据只保存成前几行预览；
- 不从图像素或压缩显示值反推缺失原值。
