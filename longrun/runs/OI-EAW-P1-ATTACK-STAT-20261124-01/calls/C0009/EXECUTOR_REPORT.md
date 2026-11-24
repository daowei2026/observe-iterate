# C0009｜原D002 m剩余X工程回交

`FeatureRunResultBinding.binding_status=INCOMPLETE_WITH_RECORDED_ENGINEERING_GAP`，`formal_complete=false`、`eligible_for_G=false`。本C实际取得原flock并完成m Wall全量只读复用核验；两组m F4在原生交易日区间校验失败，m Attack未启动，原D002完整X仍未完成。回交保持IN_PROGRESS，remaining与continuation均指向本C既存未完成原件。

亲读C0009 INVOCATION（bd9d243）、原D002 JSON及同commit正文（c974298，签发者仍C0004）、C0008 Return（e38beb1）及报告（d085c40）、C0007 continuation和完整原生Binding（0837509）。身份仍为本Run原executor:E1，回原manager，无新D，workers=[]。实际输入ref/blob与本地原件逐字节核对见[evidence/source_read_manifest](../../professional_results/D002/C0009/evidence/source_read_manifest.json)。

专业控制9877826236e0995e7255e6cbfedc2d1b89dea6da，执行原L0已有X工程操作；唯一业务输入、Owner/Binding与授权面不变。cwd为/dwdhome/fy/BASE_E6_2_copy，TIS HEAD为179016111ed0394f92025313e46bd13534932a74，专用分支保留且tracked代码无改。正式AttackFlowAssembler()和Wall/tactical/structural默认业务参数、SOF、日历、rb/m及2021全年不变。P1写面仍为本Run A03隔离store，市场基础Feature仅原生Cal读源/内存计算，不保存共享缓存；未消费Build业务成果。

A05是本C新尝试，实际2026-11-24T10:32:35.526739+00:00开始，2026-11-24T10:33:22.500724+00:00结束。同一原锁/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock，device=83、inode=15061041，2026-11-24T10:32:35.964933+00:00实际获得，2026-11-24T10:33:22.500193+00:00释放，内容始终0字节、SHA256未变。runner与观察器已结束，无本Run遗留占锁；后检探测获取并释放，不是预约。未改锁、另造锁或中断其它生产者。

A04在开始前已核终态与无Feature effects，m新目标原本不存在；历史attempt和640个既存产物文件有前后清单及摘要核验。本C使用原生stk_tlist=m，实测symbols=['m']、symbol_index=0、trading_unit=10，原运行上下文遗漏已补正。m Wall 5张表的key/shape/index/dtype及每列全数组摘要与A03一致，原receipt一致，并对当前原生cc轴与source_scope再次核验通过，没有重做Wall或rb生产。

| 品种 | 对象 | 当前有效状态 |
|---|---|---|
| rb | wall | EXECUTED_AND_FULL_READBACK_VERIFIED |
| rb | tactical | EXECUTED_AND_FULL_READBACK_VERIFIED |
| rb | structural | EXECUTED_AND_FULL_READBACK_VERIFIED |
| rb | attack | EXECUTED_AND_FULL_READBACK_VERIFIED_AFTER_READONLY_RECONCILIATION |
| m | wall | REUSED_CURRENT_RUN_AND_FULL_READBACK_VERIFIED |
| m | tactical | EXECUTION_OR_READBACK_FAILED |
| m | structural | EXECUTION_OR_READBACK_FAILED |
| m | attack | BLOCKED_MISSING_CURRENT_UPSTREAM |

m两组F4均实际调用Gen，原生异常链经过pressure_big_deal.py:615/230，到tick_quote_context.py:238：`交易日区间在 2021-03-12 00:00:00 前不连续: 1792800 != 1792801`。它们未返回完整结果，未取得成功receipt或完整读回；不以命令exit=0、默认构造或原Wall receipt代替成功运行。m Attack缺少有效上游而未启动。异常是本X中的原生运行事实，未执行专业诊断、归因或产品修复。

失败后两个F4目录各有6个DBA文件，共12个、677,239,968字节；[失败effects清单](../../professional_results/D002/C0009/evidence/failed_F4_effect_manifest.json)记录逐文件摘要。这些半成品保留，完整性未通过，不作为Feature结果或后继G输入，也不能直接覆写重试。Attack目录不存在。原先640个产物文件大小/mtime、全部既有JSON摘要、21个历史记录文件、31个C0007发布文件和原Return逐字节核对未变；原U blob15817e6保持PARTIAL。

当前[FeatureRunResultBinding](../../professional_results/D002/C0009/FeatureRunResultBinding.json)保留全部历史错误及既有rb有效资格，明确m Wall本C只读核验和F4失败的真实新effects；[未完成与恢复](../../professional_results/D002/C0009/REMAINING_SCOPE.md)交原manager按原Workflow协调。没有重做完整U，没有G、业务诊断、TIS产品修改/提交或Feature释放；本次X回交不表示Feature验收。controller负责独立物理回执、完整executor_return校验和真实跨Chat运输。
