# W004 本地 EP 事实矩阵

R0-A0接线和sentinel前置已修复，kernel setup API成功；R0-A1在Python脚本bootstrap的ioctl(FIOCLEX)被拒后exit2，未进入R0-B/C和Phase1/2。以下继承C0012 E1状态，只记录当前工程事实，不替代专业判断。

| EP | 继承E1状态 | W004事实与缺口 |
|---|---|---|
| EP-WALL-SHARED-01 | NOT_ATTEMPTED | 无新snapshot/accessor、patch/typecheck |
| EP-WALL-SHARED-02 | NOT_ATTEMPTED | 无新DTO/schema/canonical roundtrip/hash |
| EP-WALL-SHARED-03 | UNSATISFIED | 只读stdin和policy安装有新成功子事实；必需probe、closure、预算/monitor仍未证 |
| EP-SCENARIO-01 | NOT_ATTEMPTED | 未构造dedicated target/component/main/manifest |
| EP-SCENARIO-02 | NOT_ATTEMPTED | 未构造exact-error synthetic serialization |
| EP-SCENARIO-03 | NOT_ATTEMPTED | 未构造transaction DTO和committed/uncommitted验证 |
| EP-SCENARIO-04 | PARTIAL（旧静态子集） | 保留旧ledger输入，未进入新target manifest，无current result |
| EP-SCENARIO-05 | NOT_ATTEMPTED | 未物化完整9/18/22 fixture，无static parse/count/order/hash |

SATISFIED=0，PARTIAL=1，UNSATISFIED=1，NOT_ATTEMPTED=6；本W新满足EP=0。所有single/partial/full scenario、normal、build/compile/serialization/current materials均0。来源为input/mirrors中C0012专业矩阵和本W真实回执/trace；不从源码或历史材料推断当前业务事实。
