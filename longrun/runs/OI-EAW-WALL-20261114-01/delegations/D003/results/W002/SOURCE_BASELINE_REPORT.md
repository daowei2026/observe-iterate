# W002 源码基线与未启动的 staging

UTC：2026-11-14T18:50:57.319315+00:00。结论：exact base 可读；未构造 staged source，未改源码。

FRP base `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`，tree `66c53649915731c4665536ad810823f50e4749d9`。8 个要求文件均从 exact Git blob读出并逐字保存至 `input/exact-base/`，与本次读取时工作副本字节一致。原有 unrelated dirty 不被带入 source staging。

| exact base path | bytes | sha256 | working copy byte match |
|---|---:|---|---|
| `src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs` | 7194 | `fcdb43fb1e61ed53b4a4e7cac52ca4c5eed41db11b9b52e9fe3e773e982f8382` | True |
| `src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs` | 71231 | `45e13a1d57856d44c9b3f8c1bdbcbb1cacfb93b94df9a3394580e8ce4b07a861` | True |
| `src/Frp/Instance/ISL/Eaw/P1/Products.hs` | 24420 | `213bc5e4d73de9fc2e87adc92921a53ecc99bacbc3d22fa1b5bb3b6613a6c0cd` | True |
| `src/Frp/Instance/ISL/Eaw/P1/Publication.hs` | 21294 | `9d9700a205c6aa88a0fe186320e8e0f8d56e106df112c22ad31fb492c05aa437` | True |
| `src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs` | 2095 | `568f3a5acb306f3c7dd2f23f40a416bb18f14404e35b6cf58455626e246ba2c8` | True |
| `test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs` | 52536 | `2c43f06be591d4bff3f91a23d963299b9eba36dfb59a2ac7bb2bf2fcef80542d` | True |
| `frp.cabal` | 11958 | `21e3a41cf35e06687ea96bddec135a2fc4b9f3d6632ec542a1776315287c1086` | True |
| `stack.yaml` | 2650 | `86fb1c29a4d682da4a75932cb99adea3ea847d075c418cd23ec53907dacd56c4` | True |

共享仓库初态由 `audit/SHARED_BEFORE.json` 固定；终态见 `audit/SHARED_AFTER.json` 与 `WRITE_SURFACE_AUDIT.json`。

- `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp`: HEAD `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`, branch `eaw/p123-integration-20260820`, initial status ' M src/Frp/Instance/BussinessUtils.hs\n'
- `/dwdhome/fy/BASE_E6_2/mquant/tis`: HEAD `ef887396e0a06d6e75be47efee0f1985ad7988a3`, branch `eaw/p123-integration-20260820`, initial status ' M frpExample/STCalendar.py\n'
- `/dwdhome/fy/BASE_E6_2/mquant/worker`: HEAD `da0475a9c7fa769c2db8c803a5376ff2cdf09e0d`, branch `e6.2`, initial status ' M __init__.py\n M params/__init__.py\n M params/cae/__init__.py\n M params/cae/nodes/ScaleTurnCAEGraph.py\n M params/cae/nodes/__init__.py\n?? params/cae/nodes/RecoveredStandardizedHFCAEGraph.py\n'

`audit/LOCAL_PACKAGE_CLOSURE.json` 记录 15 个明确具名 package root、repo root、HEAD和顶层 cabal 文件。该清单包括 exact stack 旧 extra-deps 与 BASE overlay 候选的并集，不表示15包都必须编译，也不表示 transitive Hackage closure 已解析。声明均与各自HEAD字节一致。

exact `frp/stack.yaml` 使用 lts-18.28，BASE overlay使用 lts-22.24。现场查询的GHC为9.4.8，浅层Stack snapshot/program索引也显示9.4.8；resolver/compiler兼容性与离线closure未闭合。`frp.cabal` 的现有 light-integration component依赖frp/frp-core，新scenario-evidence component尚不存在。

计划采用只读 `git archive` 从exact commit导出到W002/source，并只在独立副本初始化local history；本次没有执行archive、git init或任何local commit。`source/` 为空，staged tree/hash和prerequisite commit均不存在。

最小compile candidate是未来独立target的compile-only；依赖frp会涉及其library闭包，FaoIngress导入store/Fao相关模块。没有从“22条小输入”推导低构建成本。缓存调查只读取具名目录的浅层索引、包声明和元数据；未递归扫描大型缓存、未读取约915 MB pantry DB或约999 MB index tar、未复制全局缓存、未build探测依赖。

本报告是本W当前静态核验，不能替代生命周期执行结果。W001的原件保持冻结。
