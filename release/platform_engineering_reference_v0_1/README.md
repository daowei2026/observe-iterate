# Feature Platform Engineering Reference Pack candidate-v0.1.0

本包把 Python／Numba 与 Haskell／FRP 特征实现时依赖的宿主工程约束放在一个共享、可锁版本的固定冷参考面。Mission B、Mission C 和其他被正式指派的特征实现者共同消费这一个包；任何一方都不拥有第二份正文。

## 当前状态

```yaml
package_id: feature-platform-engineering-reference-pack-candidate-v0.1.0
material_class: FIXED_COLD_PLATFORM_ENGINEERING_REFERENCE
integration_status: source_snapshot_integrated_candidate
validated_runnable: false
owner_acceptance: pending
current_code_truth: false
```

`candidate` 指本包进入 Agent 体系后的集成成熟度，不降低原工程文档在各自宿主职责内的来源身份。包内 8 份正文均为导入时的字节副本；本包新增的 router 只负责选择和权力边界，不重写正文。

## 读取顺序

1. 先读 [`00_REFERENCE_ROUTER.md`](00_REFERENCE_ROUTER.md)。
2. 根据当前工程问题只读被触发的 reference，不默认把 8 份正文全部灌入上下文。
3. Mission B 把采用的 `package_id`、正文 SHA-256 和 `required_reference_ids` 写进工程设计／handoff。
4. Mission C 或其他实现者消费同一锁，不自行切换到另一份副本或未审查的 latest。
5. 涉及当前 API、symbol、caller、writer、readback 或性能形状时，继续读取目标 worktree 的 owner docs、源码、测试和必要 runtime evidence。

## 目录

- `python_numba/`：输出合同、artifact 边界、runtime shape 与 hot path。
- `cross_language/`：Python／Numba 到 DBA／Fao／Haskell 的产品交接。
- `haskell_frp/`：业务可读代码、状态身份与修正、Action/context/参数、RulePack/FIS。
- `REFERENCE_MANIFEST.yaml`：稳定 reference ID、包内路径和导入字节身份。
- `SOURCE_PROVENANCE.md`：上游工作树状态及不能声称的来源事实。
- `SHA256SUMS.txt`：除自身外的包成员校验。

## 非目标

- 不取得或修改业务合同权力；
- 不把 EAW 的 P1～P8、固定模块名或参数晋升为跨用例答案；
- 不用快照代替 live RepoFact；
- 不恢复旧的厚 preflight／report／逐节点审查流水线；
- 不授权修改共享平台、创建第二 writer／storage／identity／method backend。
