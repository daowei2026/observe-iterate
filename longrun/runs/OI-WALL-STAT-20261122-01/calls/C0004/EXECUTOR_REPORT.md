# C0004｜D002 真实执行回交

本 C 沿原 D002、锁定 `feature-global-behavior-profiling` Skill 及适用补充执行 X/G。D001 已由 manager 接收，直接沿用其可用范围；没有重做完整理解。

rb 已按 TIS `6618d4d147d6ebbe634e61facddf2c9a0b996982` 的默认 WallAssembler、`TA_updto20240229_DBA`、`night_end_at_2300`、2021 全年新生产。243 个交易日、9,959,400 个输入拍、70,895 个 Wall、335,081 条 occurrence；全部 6 张原生表由独立进程经 Dao 读回，与完整导出逐行逐值相等。已完成所有可读取的对象、事件、状态、生命周期、结束原因、同刻、月份和钟时分箱剖面及统计守恒检查。

m 也已真实调用锁定默认正式实例，但在 `2021-03-12` 前因交易日分块缺口失败：`1792800 != 1792801`。本 C 保留失败现场，没有复用旧结果或采用原工作树输入处理。三自然日的隔离诊断确认了 1 条全空报价区间外行；候选排除该行后分块通过，保留字段逐值一致、原 frame 哈希未变。该结论没有扩写为本轮全年 17 行已验证，也不是正式采用。

为补齐 Owner 关注的上游转化与 D4 证据，本 C 使用未修改的锁定组件生成了独立诊断载体，并严格核对其全部 9,959,400 拍 trace 与 335,081 条事件均等于正式 rb 结果，随后才计算资格统计：bid/ask F1 命中 178,751/168,994 拍，F6 命中 178,673/168,560 拍，新建 Wall 36,197/34,698 个。对全部 10,159 个 far End 的原生 checkpoint 检查，有 support 的 far End 为 0、far 计数低于 hold 门的 far End 为 0。原生 WALL 没有这些资格列或完整逐拍 far 历史的事实仍保留；没有改输出合同或冒充原表已有字段。

已验证 rb 的 D1 事件/trace、D2 Dormant/End 检查均无冲突，未形成新的高置信结构 finding。D3 的严格已发布几何同位置薄触 End 后重建子模式为 6,847 对，保持 Owner 暂缓；m 未统计。场景问题与候选案例只是后继候选，没有选择或冻结正式场景。

整体 `FeatureRunResultBinding=PARTIAL`、`StatisticsInputReadiness=PARTIAL`、`GlobalProfileGate=BLOCKED`，专业回交 `WAITING_OWNER`。m 的数据处理差异在原 D 明确未授权采用，已形成可审阅的 M001 ModificationProposal：完整候选 diff 保留在本工作区忽略路径，仅文档、哈希和实证进入记录分支。正式 Feature 源码、参数、常量、范围和输出合同没有改变。Owner 确认后须沿原控制面安排实施、更新正式锁并完成原 rb/m 全范围 X/G 回环。

当前进度按 Owner 要求分别记录于本目录 `STATUS.json`。原生输出、完整中文剖面、结果位置与哈希、运行字段补证、输入阻断及提案在本 Run `artifacts/D002/`；入口为 `GLOBAL_PROFILE_REPORT.md` 和原生 `FeatureGlobalBehaviorProfilingResult.json`。

共享 flock 曾由另一授权 Run 持有，本 C 正常等待后真实取得并持有到生产结束；辅助重放也使用同一锁。两次持锁证据、真实 PID/fdinfo 与原始日志保存在 gitignored 现场目录；专业资源摘要及 SHA 随本包发布。rb 使用本 Run 新 native-cache，backup 写面为空，实际写面检查未发现其他写 FD。主生产及辅助进程均已退出、共享锁已释放。

没有创建线程、Worker、W、后继 D 或向其他聊天发送消息。原 Skill/协议/原件未改写；原 gate 对 Codex manager 身份的历史兼容限制没有伪装成 PASS。本 C 使用原 V2 schema 核协议，生产和统计结论来自真实加载、配置、运行、独立读回及全量证据。专业产物先发布取得 exact refs，随后独立提交 PRO_RETURN；manager 消费状态仍待真实后继确认。
