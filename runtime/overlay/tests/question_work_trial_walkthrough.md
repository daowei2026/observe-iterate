# 三组完整问题工作试跑输入

身份：合成协议输入与预期。没有真实Pro/主控执行结果，不具有市场定义或生产授权。与旧question_work_cases.json的16项覆盖提纲互补。本文件不要求现场补业务或编试题。

## 1. 取得材料与运行边界

在包含本次修订的仓库工作副本执行。输入为同目录`question_work_trial_inputs.json`。`documents`包含完整Owner原文、业务来源、首次请求、示范管理回答、已签任务、两次专业回答及管理消费结果。`bootstrap`、`binding`、`returns`、`role_returns`是这些原文的结构对象。`method_sources`给真实exact原方法；`current_contract_files`指当前工作副本DR12/13/14。试跑前记录副本实际commit，不替换为预填未来SHA。

方法原文仍按其入口取得；这些路径不是需要试跑者再编的业务内容。Git材料不可取得就报告确切缺失，不用示范原文冒充已读。逻辑附件`synthetic:文件名`仅指本JSON的documents成员；装载时保持文件名和完整文本，不声称是真实上传ID。所有`answer_ref`按各自原回答解析，原任务锚点按plan.md解析，禁止跨答案同名锚点串用。

## 2. 第一组：没有计划时启动

给管理角色仅T1.give_only中的原文、bootstrap对象及当前通用规范。不要把plan.md、专业回交和预期管理回答作为已接受答案送入上下文。发送T1.prompt。

观察它是否实际恢复目标与来源、识别尚欠边界、形成合法A-1或已有合格输入下的局部安排。不能要求Owner先填计划/预算，不能假称新用例已有parent，不能机械抄示范对象。输出须包含本次管理完整结果和一致两份回交；未完成则保持同一管理事项。

评估者在角色作答后才使用示范管理结果及T1预期。示范计划是可能的后续形态，不是唯一业务答案；实际需要先建图时，合格返回A-1同样通过组织检查。PRESENT无原件、REQUIRED_MISSING假装新建、BOOTSTRAP强塞plan_ref均应失败。格式缺项仅定向补交，业务未定继续原管理。

## 3. 第二组：连续推进、到期管理及证据更新

给主控T2.give全部文档及已签绑定、两份对应回交。角色不需要设计方法，只执行协议。第一回交须产生T2.expected_messages两条完整消息，分别送synthetic-builder及synthetic-manager；可顺序发送，不宣称真实后台并行。记录实际文本，含义不能被主控改写。

按steps顺序喂入：重复第一回交；第二回交且管理在途；管理决定已被专业输入消费；同一形成链的新证据。第一回交两项责任分别一次；重复回交零新增；第二回交可产生新的专业续作，不能新开同一管理；CONSUMED后证据升级不重开。要重开必须取得有权rearm_ref和新cycle。

另从初始空ledger分支测试：无专业回交，既有循环在02:30恢复，elapsed实际值2.5。须采用投入条件发同一管理责任，形成链状态保持未知。不得等待下一专业回答或谎报形成链已经成立。单位与起点均来自合成已签计划，不能推广成所有用例统一2小时。

## 4. 第三组：两份续作矛盾

给T3指定完整材料，将原ROLE_RETURN.handoff.instructions_ref改为#wrong-next，并附给定故意错误段落。主控必须向原承办者发送T3.expected_message，只修冲突，不从“重做方法并启动B”与“原消费者修订”中自行选业务。该冲突不取消其他独立合法责任。

修后两份均指原#next，恢复原工作；重复补交零新增派发。若原承办者声称确要改变scope，则交原decide，不能用定位修补暗扩授权。

## 5. 离线检查及记录

运行：
```sh
python agent_evolution/agent_candidates/runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/tests/test_question_work_repair.py
```

这只验证schema、引用关联、稳定责任计算及合成变体。`question_work_check.py`无网络/写状态/发送功能；pending_reviews返回待核责任建议，主控真实运行仍须采用原指令及实际记录。

真实试跑时每组在已有运行记录保存：材料commit与实际取得范围、所给完整输入、原始角色输出、实际recipient/prompt、工作及管理责任前后状态、重复次数、失败处置和实际结果。未跑保持NOT_EXECUTED_REAL_ROLES；人工/模型协议走读与真实角色调用分账，不把expected填成observed。无需新增全局台账。
