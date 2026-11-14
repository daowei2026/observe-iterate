# W002 fixture/schema 状态与来源

状态：`NOT_ATTEMPTED_PHASE0_STOP`。没有物化fixture JSON或evidence DTO/schema，没有fixture hash、prerequisite commit或parse/count/roundtrip测试结果。

合同来源：D002 `CONTROLLED_SCENARIO_ACTION_DESIGN.md`，本地逐字镜像`input/C0006-remote-CONTROLLED_SCENARIO_ACTION_DESIGN.md`，sha256 `cd522ce16fd47888d927700119cd6bf36721414a7d2a8f302e73cec84efd9dea`。

合同要求（不是本W实际物化核验）：`FX-WALL-SCENARIO-001`，9 scenarios / 18 logical firings / 22 inputs，origin=CONTROLLED；Dormant/restore在core action外。每scenario需要business_question/source_prediction/firings/ordered inputs/identity/ref/UTI/payload/distinction/non-goals。

缺口：固定完整JSON/schema和provenance；deterministic ordering；9/18/22静态验证；source/prerequisite绑定与fixture hash。Phase0停止禁止开始Phase1，所以未用合同文本伪装成已冻结fixture。即便未来物化，也只允许本W静态parse/count/order/hash；把任何部分scenario送入production lifecycle/decoder仍被禁止。

本文件不是`FX-WALL-SCENARIO-001.json`的替代品；相应deliverable维持MISSING_GATED。
