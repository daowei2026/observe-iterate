# BigNode Packet Validation / big_000001

- status: `WARN`
- file_count: `33`
- feature_slice_evidence_rows: `12`
- source_occurrence_evidence_rows: `0`
- market_sidecar_rows: `36`
- 规则：本包必须自带当前 big 子树的内容主证据和定位主证据本体。
- 规则：market sidecar 是复查材料，不是默认主读材料。
- 规则：合并表不能包含 priority / score / candidate_type / head_tail 等解释字段。