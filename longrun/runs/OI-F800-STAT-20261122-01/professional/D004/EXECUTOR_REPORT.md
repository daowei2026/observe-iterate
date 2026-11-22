# D004｜F800-MP-001 实施回交

已完成 Owner 批准的正常 KLine 相邻覆盖修复、原生回归及准确新 FRP 版本提交/推送/采用。原生返回见 [ImplementationFixReturn.json](ImplementationFixReturn.json)。新代码 **be57d6752c9d43d10f1d670e1d2993bb8153ea7c**；finding 为 **FIXED_PENDING_RERUN**，FeatureReleaseGate 为 **RERUN_REQUIRED**。

本次 C0010/E1 亲自执行原 D004，workers=[]，回原 manager。39 项准确 Git 对象与当前输入逐字节一致，批准原文与 packet 原件一致；D004 另经 GitHub 连接器准确提交读回。见 [SOURCE_REF_AUDIT.json](SOURCE_REF_AUDIT.json)、[REMOTE_INPUT_READBACK.json](REMOTE_INPUT_READBACK.json)。

## 实施及支持合同

覆盖边使用源 Int64 UTI 的 Integer 差，比较经频率/Calendar 换算得到的正整数步长，避免两个大浮点商之差严格等于1。previous 仅持源 UTI 和 Clock，首次或真实缺口只给当前点。原 Material 严格累计及候选演化保持。

固定秒/分钟频率下，准确原始步长为 `freq_ns / 60000000000 × units_per_open_minute / units_per_calendar_tick`，用实际 Double 值的精确有理数计算；有限、正、整数且在 Int64 内才接受。Tick 和名义日/周/月不能据 ns 推定开放时长，明确拒绝。非整数步长/原UTI不做盲目 round 或添加 epsilon；源UTI复用既有 exactUTI。当前 5m × 120 / 1 = 600UTI。详见 [EXACT_STEP_DESIGN.md](EXACT_STEP_DESIGN.md)。

仅改变适配器和现有回归入口两个文件，见 [IMPLEMENTATION.patch](IMPLEMENTATION.patch) 与 [准确代码提交](https://github.com/daowei2026/frp/commit/be57d6752c9d43d10f1d670e1d2993bb8153ea7c)。完整配置字节 SHA-256 仍为 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；800、delta600、CalendarUTITick、实际2Δ=1200、method.revision1、inputs/sources/domain/result_layout、TIS@2f460d663d821cf2ba25555eda13e78b697d0767 均按批准保持。

## 实际验证与采用

隔离运行时已构建 dbaw、原生窗口检查与 ts，构建退出0。原基线窗口检查 27 项和修后 64 项全部通过，原检查全部保留。新检查将实际生产 helper 的覆盖边送入原 Material：真实2^17数值边界旧guard失败而新边保持800Δ完整覆盖；真实1200UTI缺口、冷启动、SourceFailure 后恢复与未知Clock不会被桥接；Clock明确修订可恢复；支持/拒绝的频率和单位换算有实测。原窗口、revision/handoff、方向、期限和真实1200/1201UTI的2Δ边界均通过。

证据：[TEST_RESULTS.json](TEST_RESULTS.json)、[fixed-window-checks.log](fixed-window-checks.log)、[baseline-window-checks.log](baseline-window-checks.log)、[BUILD_STATUS.json](BUILD_STATUS.json)、[完整构建日志](build.log.gz)。测试为 FI 回归，未启动正式 Feature。源文件构建前后SHA及新二进制路径/hash有绑定；目标授权分支经真实推送、ls-remote 和 GitHub 两个文件准确提交读回，见 [CODE_PUBLICATION_READBACK.json](CODE_PUBLICATION_READBACK.json)。

首次构建观察脚本把ps空子进程返回1当异常退出，没有将未知编译状态登记成功；核对原构建已不在运行后修正监控，重新构建，验收取本次真实退出0。原状态保留在 [BUILD_ATTEMPT1_MONITOR_FAILURE.json](BUILD_ATTEMPT1_MONITOR_FAILURE.json)。

新版本及隔离运行时已采用用于下一 X，见 [CodeVersionAdoption.json](CodeVersionAdoption.json)。旧 D002 源码、3个二进制 hash保持，D002结果/D003诊断没有覆盖。TIS 冻结副本与原 D002 路径相同；未把父 Git 仓库 HEAD 当 TIS 版本证明。

TIS正常构造器及F Python参数类另以锁定2f提交从GitHub准确读回，与实际冻结副本的Git blob逐一吻合，见 [TIS_PIN_READBACK.json](TIS_PIN_READBACK.json)。

## 影响与后继

对象、身份、业务状态/事件、生命周期和结果布局没有结构变化；相关合同文件字节未变。因此按原 L0 §9 和 FI Gate 直接 **X→独立31表读回→G**，无需重做完整 U。D001 已接收的最小理解及 D002 缺口处置保留。

F/Q共享形成适配器，因此 Q 会取得修后的覆盖边；Q 的报价四元组/Double位置换算保持。源码还显示 Q 的运动模块另有归一化位置相邻判断，此独立逻辑未改、未正式运行，不能据本修复声称 Q 路径覆盖通过。V 经真实依赖间接受影响。详见 [ContractAndDependencyImpact.json](ContractAndDependencyImpact.json)。本Run仅F，不扩为Q/V或WALL修改。

覆盖变化可能改变 candidate affected/body、Revision密度、exact引用及UUID链。局部回归不承诺正式只减少22个观点或保持原随机ID。完整三年新生产、原22位置、全部结构/密度与既有4项场景问题必须由后继 X/G 实测；当前无新正式结果和 UpstreamReleasePackage。

原 manager 消费本返回后，按已批准范围签发下一 X，无需再请 Owner 确认。准确代码/运行时、原完整配置和未创建的新store建议位置在 [RERUN_HANDOFF.json](RERUN_HANDOFF.json)；新D中重新核真实单写者/加载/配置/结果身份并持实际 flock。旧 X/G 留历史对照，不充当新版本 Gate 证据。

Owner七项进度：D001已接收且不重做；旧X完成、修后X待正式后继；旧结果来自D002一次新生产；本C只构建/回归而未运行正式ts生产；当前正式结果目录仍是D002/store旧基线，新store未创建；旧G1–G8完成而修后G未开始；本D无未解决事实阻断，释放受完整复验未完成约束。

D004 FI职责已完成，完整Run仍未完成。先发布本专业产物，再以已存在的 exact 提交形成 C0010 原 V2 PRO_RETURN；没有创建 Worker、委派或跨线程发送，也不声称 manager 已消费。
