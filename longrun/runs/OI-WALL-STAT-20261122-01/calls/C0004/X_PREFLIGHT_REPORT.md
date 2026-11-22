# C0004｜X 实际加载与实例预检

D001 已由 manager 按最新 Owner 最小核对范围接收。本 C 沿原 D002 开始 X，采用新生产计划；当前源与参数准入核验已经取得真实证据。

- 主实现实际文件：`/dwdhome/fy/BASE_E6_2/.runtime/OI-WALL-STAT-20261122-01/code/tis/hf/prel0/wall_assembler.py`。
- core 实际文件属于同一隔离检出；TIS HEAD 为 `6618d4d147d6ebbe634e61facddf2c9a0b996982`。
- 已加载且受 Git 跟踪的 TIS 源文件 44 份逐字匹配锁定对象；原工作树两项既有修改未恢复或采用。
- 锁定仓库未追踪生成包初始化文件。隔离运行使用既有生成包文件，并追加原生成模块的后备搜索目录；固定检出优先。生成文件的完整哈希单独记录为运行依赖，不冒充提交内源码。
- rb/m 两个默认实例的全部 28 项 ppdict 与代码默认值一致，已保存完整配置并独立从文件回读；Calendar、SOF、日期和 symbols 沿 Owner 硬输入。
- 旧原生缓存 receipt 的代码不是最终锁定提交；最终 core 隔离重放也未满足完整 producer、配置、输入处理和正式结果身份的全部复用证明。本轮不采用旧结果。
- 通过框架原生 `TmpStoreEnv(WallAssembler, ...)` 只改变本 Feature 的结果存储位置，仍调用默认 `WallAssembler().run()`；没有 backup 写面。上游 CC 是 Cal，不落盘；QT 已有缓存将按正常只读加载路径消费。
- 共享生产锁、单写者检查和实际正式调用证据由运行进程产生；预检成功不等于生产完成。资源锁尚未取得时，不宣称正式 Feature 已运行。

独立结果存储根：`/dwdhome/fy/BASE_E6_2/.runtime/OI-WALL-STAT-20261122-01/native-cache`。实际单品种 full_dir 见工作区 `preflight.json`；物化目录是否存在、是否成功及独立读回应以随后真实执行记录为准。

D1/D2/D4 的锁定仓库自带三组固定例回归退出码均为 0。它们不替代本 Run 全量统计或 D4 逐拍计数验证。

工作区证据：`preflight.json`、`generated-package-bootstrap.json`、`reuse-candidate-review.json`、`locked-fixture-checks/summary.json`、`statistics-specification.json`。后两项分别为固定例核验及 G 的预先口径，没有将旧统计数字或代码内部变量当作本轮结果。
