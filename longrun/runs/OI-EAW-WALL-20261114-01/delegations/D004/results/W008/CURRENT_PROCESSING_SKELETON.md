# 当前处理骨架与实际观察层

静态生产链：WallAssembler occurrence/receipt/packed numeric rows → TIS WallOccurrenceFao OnlyRead → current FaoIngress decode/partition → applyWallOccurrenceBatch + FRP maintainWallLifecycle → dumpWallOutputs → wall_occurrences(O)/wall_current_view(C updates)/wall_diagnostics(D) → FrpDbaDao + generated wrapper/consumer。完整A是内部active map/FRP Dynamic，不是C append-update表。

本W实际执行的层：existing test形状typed input → live BASE current applyWallOccurrenceBatch → 实际returned occurrence和WallLifecycleState既有Show；独立执行current Publication occurrence ToBSON/FromBSON。未运行WallAssembler/packed ingress、FaoModel事件引擎或dumpWallOutputs，未物化DBA产品。9个current生产模块从live BASE直接编译，依赖现成installed package DB，Frp.Instance.BussinessUtils仍来自缓存ABI；不声称全checkout重新构建或依赖二进制生成版本已完整追回。

| 对象 | 真实取得 | 不能混同 |
|---|---|---|
| upstream/input | 4条人工typed normal input，两个已有test表达式输入 | 自然WallAssembler输出或产品生成receipt |
| O | reducer实际returned列表，normal各1/2/1，共4 | production event writer执行 |
| C | 实际state Show中的wallCurrentUpdateBatch，N2仅最后update，N3 Ended | full active snapshot、物化C或FRP Event |
| A | 实际state Show中的wallViews，End后fromList [] | producer A0 trace、FRP Dynamic实际提交 |
| D | scenario实际Left constructor和identity | wall_diagnostics通道实际发布或有效空 |
| consumer | current occurrence-level BSON adapter四条读回相等 | physical DBA reader/完整Batch/D roundtrip |

End当前typed change和BSON为WallEnded(reason)，没有band/core字段；不存在本W物化的价格0。最后合法更新band[101,103]/core102只在前一更新上下文，不能补进End原值。源值、Show、JSON记录、BSON文档层次分别保存；JSON是观察容器，不是新canonical product schema。

版本、HEAD/branch/status/diff及source metadata见BASE_ASSET_INVENTORY/BASE_SIDE_EFFECTS报告；相关源码逐字文本单独作为JSON证据归档，未复制为可构建源码树，现有源码无改动。
