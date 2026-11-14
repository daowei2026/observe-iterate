# W002 当前 exact source/test 合同冲突台账

来源全部绑定 FRP `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`。这里只登记静态源码与断言；本W没有执行这些函数、生产decoder/lifecycle或旧suite。

## KCC-01 跨firing Start replay

`test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs:455` 的 `wallLifecycleMustBeProductSpecificAndIdempotent`：457行先把 `[wallStart]` 应用到empty state；459行用新batch在state上再次应用同一Start，并要求`requireRight "Wall duplicate"`；460行要求`sameState == state && null duplicatePublications`。

`src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs:91` 的 `applyWallOccurrenceBatch` 在95行每firing重置ledger；`applyWallOccurrence` 76行从active map取before；`validateWallTransition` 54行对已有identity再次Start返回`WallStartedTwice identity`。因此静态预测与旧跨firing幂等断言存在明确差异；不是实测结果，也不在本W决定修改implementation还是旧test。

## KCC-02 End后update仅检查任意Left

同一exact test `wallLifecycleTransitionTableMustBeComplete` 位于503行。527行构造完成End的state，537行的`requireLeft "Wall update after end" (...)` 没检查constructor。helper在1022–1024行定义，`requireLeft _ (Left _) = pure ()`，会接受任意错误。

current source `applyWallOccurrence` 81行在End时从active map删除identity；`validateWallTransition` 53行对Nothing+update返回`WallUpdateBeforeStart`，56行虽有`WallUpdateAfterEnd`分支，不能仅凭旧断言证明其真实可达。这里只登记静态区分，未运行End/update scenario。

## KCC-03 transaction/ingress边界不能被通用失败吞掉

`applyWallOccurrenceBatch` 96行`foldM`可能返回Left；`stepWall` 对Left保持原`wallTxnState`，只写结果字段。`FaoIngress.partitionIngressBatch` 158–164行在有decode error时返回无typed batch；`decodeWallNumericRow` 587–625行使用`required "core_price"`。未来target必须分别记录actual constructor/payload、ingress/state来源及committed pre/post A，不能把fold中途状态当提交状态。该项为设计记录，没有actual trace。

当前台账只使EP-SCENARIO-04具可审查静态子集（PARTIAL）；新harness及其manifest未构造，工程前置没有宣布接受。源码原件在`input/exact-base/`；hash见`audit/EXACT_SOURCE_BLOBS.json`，有限检索原始输出在`logs/exact-contract-lines.stdout`。未改现有断言或生产lifecycle语义。
