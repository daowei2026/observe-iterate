# W001 payload 读取前的路径选择

记录时点：实际 payload 读取前；实际命令起止见 COMMANDS.jsonl。

- `BINDING.json` 已由现役类在指定同值上下文中取得 feature/source 的实际 full_dir。此前旧报告只作精确路径线索；本次实例化已经独立核实同一路径，不采用其旧计数/样例或成功状态。
- 不调用 `.run()`、`.rerun()` 或 `.F`。框架 `lang/internal/base.py:1708` 的 Cache 分支会在 load miss 后运行上游和 `_impl`，因此不能仅用 fields 存在作保障。
- 直接复用 `FrpDbaDao.loadWith` 的现役 ADT 读取层：`NormalField.from_str(...).adt_class` → `DbaStore(full_dir/key, class)`；时间轴由 `DbaUtil.read_field_ts(..., True)`。各路独立读取，失败不回补。
- 依据：`mquant/frame/lang/internal/dao/frp/dba.py:55` 后无 producer 路径；`core/store.py:778` 显式 mmap.ACCESS_READ；`pydim/dim/dbas.py:23` 使用缺 shape 的 DbArray；`pydim/dim/rt.py:118–152` 此分支仅 `rb` 和 mmap.ACCESS_READ，缺文件报错，不创建文件。`__arm_store__` 缺文件可能降为 EmptyDbaStruct，调查必须据实际类型/日志判别，不能据无异常判成功。
- 仅扫描约万级外层 pointer/anchor 元数据选择最多三处批次，不全量 decode 业务 payload。超过64行的单批不展开并显式标注。
- diagnostics 按实际 schema 单独处理 envelope 和内部 errors；不沿用原示例脚本的通用 business_rows 逻辑。
- source 通过同一 DbArray(shape=None, ACCESS_READ) 映射必要列，仅在已选 UTI/local_no 上定位；不加载整表 DataFrame、不整窗 join、不运行 assembler。
- Python 禁止 bytecode；临时文件和启动日志转入本 W；Python audit 阻止 W 外持久写入和未经证明的 subprocess，profile 阻止特征执行入口。这些额外保护不替代上述源码证明。
