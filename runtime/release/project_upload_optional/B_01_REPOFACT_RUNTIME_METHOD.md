<!--
virtual_source_id: MB-RUNTIME-REPOFACT
candidate: Mission B v0.2
canonical_sources:
  - 10_methods/02_REPOFACT_INVESTIGATION_FULL_REFERENCE.md
  - 60_repo_router/LIVE_EXACT_REF_AND_DRIFT_PROTOCOL.md
manual_edit: forbidden
-->

# RepoFact Runtime Method

1. 锁 task authority、repo roles、旧锁和 live head。
2. 发现 drift 时列 old/new SHA、影响问题，并选择一个 exact commit。
3. 先读 owner docs／MANIFEST，再定向读 production entry、caller、state、method asset、writer、readback、consumer。
4. 每条结果标 `DIRECT_FACT / INFERENCE / CANDIDATE / GAP`。
5. 不提出 to-be，不把当前代码当业务应然。
6. 将结果冻结为单写者 S0；Compiler 只读。
7. 后续事实变化形成 S0 delta／invalidation，不静默覆盖。
