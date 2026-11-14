{-# LANGUAGE OverloadedStrings #-}

-- 轻量合同测试；不声称执行过真实数据重型运行。
module Main (main) where

import Control.Monad (unless)
import Data.Aeson (Value, eitherDecode, encode, object, (.=))
import Data.ByteString.Lazy qualified as BL
import Data.Either (isLeft)
import Data.Int (Int64)
import Data.Map.Strict qualified as Map
import Data.Text qualified as Text
import Frp.Apt.Bson (FromBSON (fromBSON), ToBSON (toBSON))
import Frp.Instance.ISL.Eaw.Interface.Common
import Frp.Instance.ISL.Eaw.Interface.PreL0 qualified as Spine
import Frp.Instance.ISL.Eaw.P1
import Frp.Instance.ISL.Eaw.P1.Internal.UpstreamReference
import System.Directory (createDirectoryIfMissing, getTemporaryDirectory, removeDirectoryRecursive, removeFile)
import System.FilePath ((</>))
import System.IO (hClose, openTempFile)

main :: IO ()
main = do
  realRunFeatureParametersMustDecode
  thinReceiptAndStructuredIdentityMustBePreserved
  thinReceiptSidecarMustNotRequireCommitMarker
  exactWallCatalogMustBeArtifactBasedAndFailClosed
  attackProductsMustComeFromOneProducerRun
  typedIngressMustFailClosedOnMissingOrInvalidFields
  ingressDiagnosticBatchMustBeAtomic
  typedF4MustKeepFeatureInstanceFamilyGradeAndLocalIdentity
  wallLifecycleMustBeProductSpecificAndIdempotent
  wallLifecycleMustKeepBidAndAskWallsIndependent
  wallLifecycleTransitionTableMustBeComplete
  dependentDsusMustUseFixedExactWallCatalog
  buildAndAbsorbTransitionTablesMustBeComplete
  sameUtiPermutationMustNotChangeAttackBook
  attackCurrentViewMustNotCopyOccurrenceHistory
  productBatchesMustNotPartiallyPublish
  p2HandoffFixtureMustReadFullProducerPayload
  putStrLn "EAW_P1_V1_6_1_FRP_SMOKE_PASS"

realRunFeatureParametersMustDecode :: IO ()
realRunFeatureParametersMustDecode = do
  let source tag =
        object
          [ "__tag__" .= (tag :: Text.Text),
            "__tar_type__" .= object ["__tag__" .= ("SymbolType" :: Text.Text)],
            "__on_date_range__" .= True
          ]
      wall = source "WallAssembler"
      build = source "BuildAssembler"
      attack = source "AttackFlowAssembler"
      absorb = source "AbsorbAssembler"
      wallParams =
        object
          [ "__tag__" .= ("EawP1WallLifecycleFrp" :: Text.Text),
            "wallLifecycleInput"
              .= object
                [ "__tag__" .= ("WallOccurrenceFao" :: Text.Text),
                  "wallOccurrenceSource" .= wall
                ]
          ]
      buildParams =
        object
          [ "__tag__" .= ("EawP1BuildActivityFrp" :: Text.Text),
            "buildActivityInput"
              .= object
                [ "__tag__" .= ("BuildOccurrenceFao" :: Text.Text),
                  "buildOccurrenceSource" .= build,
                  "buildWallSource" .= wall
                ]
          ]
      attackParams =
        object
          [ "__tag__" .= ("EawP1AttackSegmentBookFrp" :: Text.Text),
            "attackSegmentInput"
              .= object
                [ "__tag__" .= ("AttackSegmentFao" :: Text.Text),
                  "attackSegmentSource" .= attack,
                  "attackSegmentWallSource" .= wall
                ],
            "attackFormationInput"
              .= object
                [ "__tag__" .= ("FormationEvidenceFao" :: Text.Text),
                  "formationEvidenceSource" .= attack,
                  "formationEvidenceWallSource" .= wall
                ],
            "attackBarrierInput"
              .= object
                [ "__tag__" .= ("WallBarrierFao" :: Text.Text),
                  "wallBarrierSource" .= attack,
                  "wallBarrierWallSource" .= wall
                ]
          ]
      absorbParams =
        object
          [ "__tag__" .= ("EawP1AbsorbInteractionFrp" :: Text.Text),
            "absorbInteractionInput"
              .= object
                [ "__tag__" .= ("AbsorbOccurrenceFao" :: Text.Text),
                  "absorbOccurrenceSource" .= absorb,
                  "absorbWallSource" .= wall
                ]
          ]
  requireDecoded "EawP1WallLifecycleFrp" (eitherDecode (encode wallParams) :: Either String EawP1WallLifecycleFrp)
  requireDecoded "EawP1BuildActivityFrp" (eitherDecode (encode buildParams) :: Either String EawP1BuildActivityFrp)
  requireDecoded "EawP1AttackSegmentBookFrp" (eitherDecode (encode attackParams) :: Either String EawP1AttackSegmentBookFrp)
  requireDecoded "EawP1AbsorbInteractionFrp" (eitherDecode (encode absorbParams) :: Either String EawP1AbsorbInteractionFrp)
  where
    requireDecoded label = either (fail . ((label <> " 参数无法由平台注册 JSON 解码: ") <>)) (const (pure ()))

scope :: SourceScope
scope = SourceScope "rb" "SHFE-night" "uti:1..20" "market-cut-A"

wallReceipt :: ProductReceipt
wallReceipt =
  ProductReceipt
    "wall_lifecycle"
    "WallAssembler:wall-params-A"
    "wall-params-A"
    scope
    (object [])
    (object [])
    []
    Nothing
    "wall_lifecycle-v1.6.1"
    "wall-code-A"
    "/artifact/wall-A"
    "success"
    Nothing

asUpstream :: ProductReceipt -> DirectUpstreamArtifact
asUpstream receipt =
  DirectUpstreamArtifact
    (receiptProductKind receipt)
    (receiptFeatureInstance receipt)
    (receiptParameterSetId receipt)
    (receiptArtifactLocation receipt)
    (receiptSchemaVersion receipt)
    (receiptCodeVersion receipt)

f3Receipt :: ProductReceipt
f3Receipt =
  wallReceipt
    { receiptProductKind = "active_directional_pressure_dense",
      receiptFeatureInstance = "AggressorPressureTick:f3-A",
      receiptParameterSetId = "f3-A",
      receiptSchemaVersion = "active_directional_pressure_dense-v1.6.1",
      receiptArtifactLocation = "/artifact/f3-A"
    }

f4Receipt :: ProductReceipt
f4Receipt =
  wallReceipt
    { receiptProductKind = "directed_large_deal_stream",
      receiptFeatureInstance = "DirectedBigDealTick:tactical:f4-tactical-A",
      receiptParameterSetId = "f4-tactical-A",
      receiptActualBusinessParameters = object ["qualification_family" .= ("tactical" :: Text.Text)],
      receiptSchemaVersion = "directed_large_deal_stream-v1.6.1",
      receiptArtifactLocation = "/artifact/f4-tactical-A"
    }

f4StructuralReceipt :: ProductReceipt
f4StructuralReceipt =
  f4Receipt
    { receiptFeatureInstance = "DirectedBigDealTick:structural:f4-structural-A",
      receiptParameterSetId = "f4-structural-A",
      receiptActualBusinessParameters = object ["qualification_family" .= ("structural" :: Text.Text)],
      receiptArtifactLocation = "/artifact/f4-structural-A"
    }

buildReceipt :: ProductReceipt
buildReceipt =
  wallReceipt
    { receiptProductKind = "build_activity",
      receiptFeatureInstance = "BuildAssembler:build-A",
      receiptParameterSetId = "build-A",
      receiptDirectUpstreamArtifacts = [asUpstream wallReceipt, asUpstream f3Receipt],
      receiptSchemaVersion = "build_activity-v1.6.1",
      receiptArtifactLocation = "/artifact/build-A"
    }

attackReceipt :: ProductReceipt
attackReceipt =
  wallReceipt
    { receiptProductKind = "attack_segment",
      receiptFeatureInstance = "AttackFlowAssembler:attack-A",
      receiptParameterSetId = "attack-A",
      receiptActualBusinessParameters =
        object
          [ "p_attack_ticks" .= (3 :: Int),
            "t_gap_attack_ticks" .= (2 :: Int),
            "lane_merge_policy" .= ("union_keep_labels" :: Text.Text),
            "selected_f4_streams"
              .= ( [ object
                       [ "feature_instance" .= receiptFeatureInstance f4Receipt,
                         "parameter_set_id" .= receiptParameterSetId f4Receipt,
                         "source_scope" .= scope,
                         "artifact_location" .= receiptArtifactLocation f4Receipt,
                         "schema_version" .= receiptSchemaVersion f4Receipt,
                         "code_version" .= receiptCodeVersion f4Receipt
                       ],
                     object
                       [ "feature_instance" .= receiptFeatureInstance f4StructuralReceipt,
                         "parameter_set_id" .= receiptParameterSetId f4StructuralReceipt,
                         "source_scope" .= scope,
                         "artifact_location" .= receiptArtifactLocation f4StructuralReceipt,
                         "schema_version" .= receiptSchemaVersion f4StructuralReceipt,
                         "code_version" .= receiptCodeVersion f4StructuralReceipt
                       ]
                   ] ::
                     [Value]
                 )
          ],
      receiptDirectUpstreamArtifacts = [asUpstream wallReceipt, asUpstream f4Receipt, asUpstream f4StructuralReceipt],
      receiptMethodSnapshotFingerprint = Just "sha256:attack-method-A",
      receiptSchemaVersion = "attack_segment-v1.6.2",
      receiptArtifactLocation = "/artifact/attack-A"
    }

formationReceipt :: ProductReceipt
formationReceipt =
  attackReceipt
    { receiptProductKind = "attack_formation_evidence",
      receiptSchemaVersion = "attack_formation_evidence-v1.6.2"
    }

barrierReceipt :: ProductReceipt
barrierReceipt =
  attackReceipt
    { receiptProductKind = "wall_relation_barrier",
      receiptDirectUpstreamArtifacts = [asUpstream wallReceipt],
      receiptSchemaVersion = "wall_relation_barrier-v1.6.1"
    }

absorbReceipt :: ProductReceipt
absorbReceipt =
  wallReceipt
    { receiptProductKind = "absorb_interaction",
      receiptFeatureInstance = "AbsorbAssembler:absorb-A",
      receiptParameterSetId = "absorb-A",
      receiptDirectUpstreamArtifacts = [asUpstream wallReceipt],
      receiptSchemaVersion = "absorb_interaction-v1.6.1",
      receiptArtifactLocation = "/artifact/absorb-A"
    }

localNo :: Int64
localNo = 999

runIdentity :: FeatureRunIdentity
runIdentity = featureRunIdentityFromFaoContext wallReceipt

wallIdentity :: WallIdentity
wallIdentity = WallIdentity localNo

wallCatalog :: WallIdentityCatalog
wallCatalog = formWallIdentityCatalog [localNo]

otherWallIdentity :: WallIdentity
otherWallIdentity = WallIdentity (localNo + 1)

twoWallCatalog :: WallIdentityCatalog
twoWallCatalog = formWallIdentityCatalog [localNo, localNo + 1]

measuredBand :: Measurement Spine.WallBand
measuredBand = Measured (Spine.WallBand (Spine.Price 99) (Spine.Price 101) (Spine.Price 100))

wallStart :: WallLifecycleOccurrence
wallStart =
  WallLifecycleOccurrence
    wallIdentity
    (OccurrenceRef "wall-occurrence-1")
    (Spine.WallLifecycleEvent (wallRefOf wallIdentity) (InstrumentSymbol "rb") BidWall 10 (Spine.WallStarted measuredBand Spine.WallAlive) Spine.WallLifecycleAvailable)

askWallStart :: WallLifecycleOccurrence
askWallStart =
  WallLifecycleOccurrence
    otherWallIdentity
    (OccurrenceRef "ask-wall-occurrence-1")
    (Spine.WallLifecycleEvent (wallRefOf otherWallIdentity) (InstrumentSymbol "rb") AskWall 10 (Spine.WallStarted measuredBand Spine.WallAlive) Spine.WallLifecycleAvailable)

thinReceiptAndStructuredIdentityMustBePreserved :: IO ()
thinReceiptAndStructuredIdentityMustBePreserved = do
  _ <- requireRight "wall receipt" (validateReceiptKind "wall_lifecycle" wallReceipt)
  _ <- requireRight "build receipt" (validateReceiptKind "build_activity" buildReceipt)
  let WallRef exactRef = wallRefOf wallIdentity
  unless (Text.pack (show localNo) `Text.isInfixOf` exactRef) $ fail "WallIdentity 未保留 producer 局部编号"
  unless (targetRef runIdentity == "rb" && timeRangeRef runIdentity == "uti:1..20") $ fail "FeatureRunIdentity 没有保留结构化运行上下文"
  requireLeft "wrong receipt kind" (validateReceiptKind "build_activity" wallReceipt)

thinReceiptSidecarMustNotRequireCommitMarker :: IO ()
thinReceiptSidecarMustNotRequireCommitMarker = do
  temporaryRoot <- getTemporaryDirectory
  (temporaryPath, handle) <- openTempFile temporaryRoot "eaw-p1-v161-receipt"
  hClose handle
  removeFile temporaryPath
  createDirectoryIfMissing True (temporaryPath </> "p1_receipts")
  BL.writeFile (temporaryPath </> "p1_receipts" </> "wall_lifecycle.json") (encode wallReceipt)
  _ <- requireRight "thin receipt without marker" =<< readThinProductReceipt temporaryPath "wall_lifecycle"
  removeDirectoryRecursive temporaryPath

exactWallCatalogMustBeArtifactBasedAndFailClosed :: IO ()
exactWallCatalogMustBeArtifactBasedAndFailClosed = do
  unless (containsWallIdentity wallIdentity wallCatalog) $ fail "exact Wall artifact catalog 未保留 WallIdentity"
  _ <- requireRight "known exact Wall" (validateDependentWallIdentity localNo wallCatalog)
  requireLeft "unknown Wall" (validateDependentWallIdentity (localNo + 1) wallCatalog)
  _ <- requireRight "matching upstream receipt" (validateExactUpstreamReceipt "wall_lifecycle" buildReceipt wallReceipt)
  let otherScope = wallReceipt {receiptSourceScope = scope {sourceMarketCut = "market-cut-B"}}
  requireLeft "mismatched upstream scope" (validateExactUpstreamReceipt "wall_lifecycle" buildReceipt otherScope)

attackProductsMustComeFromOneProducerRun :: IO ()
attackProductsMustComeFromOneProducerRun = do
  _ <- requireRight "matching Attack product receipts" (validateAttackProductReceiptSet attackReceipt formationReceipt barrierReceipt)
  requireLeft
    "mixed Attack parameter sets"
    ( validateAttackProductReceiptSet
        attackReceipt
        formationReceipt {receiptParameterSetId = "attack-B"}
        barrierReceipt
    )
  requireLeft
    "mixed Attack artifacts"
    ( validateAttackProductReceiptSet
        attackReceipt
        formationReceipt {receiptArtifactLocation = "/artifact/attack-B"}
        barrierReceipt
    )
  requireLeft
    "mixed Attack method snapshots"
    ( validateAttackProductReceiptSet
        attackReceipt
        formationReceipt {receiptMethodSnapshotFingerprint = Just "sha256:attack-method-B"}
        barrierReceipt
    )
  requireLeft
    "mixed Attack Wall upstreams"
    ( validateAttackProductReceiptSet
        attackReceipt
        formationReceipt
        barrierReceipt
          { receiptDirectUpstreamArtifacts =
              [asUpstream (wallReceipt {receiptArtifactLocation = "/artifact/wall-B"})]
          }
    )

typedIngressMustFailClosedOnMissingOrInvalidFields :: IO ()
typedIngressMustFailClosedOnMissingOrInvalidFields = do
  let row =
        Map.fromList
          [ ("side_code", 1),
            ("uti", 10),
            ("availability_code", 1),
            ("event_type_code", 4),
            ("band_lo", 99),
            ("band_hi", 101),
            ("core_price", 100),
            ("status_code", 1)
          ]
  occurrence <- requireRight "complete Wall numeric row" (decodeWallNumericRow wallReceipt "wall__999" row)
  sameOccurrence <- requireRight "transport-split Wall numeric row" (decodeWallNumericRow wallReceipt "wall__999__occ0001" row)
  unless (wallOccurrenceRef occurrence == wallOccurrenceRef sameOccurrence) $
    fail "transport ordinal 进入了 Wall occurrence identity"
  let compactRow = Map.insert "wall_id" (fromIntegral localNo) row
  compactOccurrence <- requireRight "compact Wall numeric row" (decodeWallNumericRow wallReceipt "wall__stream" compactRow)
  compactSplit <- requireRight "transport-split compact Wall numeric row" (decodeWallNumericRow wallReceipt "wall__stream__occ0001" compactRow)
  unless
    ( wallOccurrenceIdentity compactOccurrence == wallIdentity
        && wallOccurrenceRef compactOccurrence == wallOccurrenceRef compactSplit
    )
    (fail "紧凑 Wall 流没有从行内 wall_id 恢复同一业务 occurrence")
  requireLeft
    "legacy Wall key and row wall_id must agree"
    (decodeWallNumericRow wallReceipt "wall__1000" compactRow)
  requireLeft "missing field must not default to zero" (decodeWallNumericRow wallReceipt "wall__999" (Map.delete "core_price" row))
  requireLeft "invalid Wall band must fail closed" (decodeWallNumericRow wallReceipt "wall__999" (Map.insert "core_price" 102 row))
  requireLeft
    "source-missing Wall row must be diagnostic-only and must not form Wall.End"
    ( decodeWallNumericRow
        wallReceipt
        "wall__999"
        ( Map.insert
            "reason_code"
            1
            (Map.insert "event_type_code" 7 (Map.insert "availability_code" 2 row))
        )
    )
  let unavailableBuildStop =
        Map.fromList
          [ ("wall_local_no", fromIntegral localNo),
            ("uti", 10),
            ("availability_code", 5),
            ("cum_reload_proxy", 0),
            ("same_band_continuity_code", 1),
            ("event_type_code", 10)
          ]
  requireLeft
    "calculation-unavailable Build row must be diagnostic-only and must not form Build.Stop"
    (decodeBuildNumericRow buildReceipt wallCatalog "build__7" unavailableBuildStop)

ingressDiagnosticBatchMustBeAtomic :: IO ()
ingressDiagnosticBatchMustBeAtomic = do
  let row =
        Map.fromList
          [ ("side_code", 1),
            ("uti", 10),
            ("availability_code", 1),
            ("event_type_code", 4),
            ("band_lo", 99),
            ("band_hi", 101),
            ("core_price", 100),
            ("status_code", 1)
          ]
      complete = decodeWallNumericRow wallReceipt "wall__999" row
      invalid = decodeWallNumericRow wallReceipt "wall__1000" (Map.delete "core_price" row)
  case partitionIngressBatch [complete, invalid] of
    (Nothing, Just [MissingNumericField "core_price"]) -> pure ()
    other -> fail ("同拍 ingress 错误没有拒绝整个产品 batch 并形成 diagnostic: " <> show other)

typedF4MustKeepFeatureInstanceFamilyGradeAndLocalIdentity :: IO ()
typedF4MustKeepFeatureInstanceFamilyGradeAndLocalIdentity = do
  let row =
        Map.fromList
          [ ("producer_local_no", fromIntegral localNo),
            ("uti", 10),
            ("qualification_code", 1),
            ("qualification_family_code", 1),
            ("lane_code", 1),
            ("grade", 4),
            ("directional_hit_volume_proxy", 3),
            ("deal_amt", 300)
          ]
  occurrence <- requireRight "typed F4" (decodeDirectedLargeDealNumericRow f4Receipt "buy" row)
  transportSplit <- requireRight "typed F4 transport split" (decodeDirectedLargeDealNumericRow f4Receipt "buy__occ0001" row)
  unless
    ( largeDealOccurrenceLocalNo occurrence == localNo
        && largeDealQualificationFamily occurrence == "tactical"
        && largeDealQualificationGrade occurrence == 4
    )
    (fail "F4 typed source 丢失 Feature instance／family／grade／producer 局部编号")
  unless (largeDealOccurrenceRef occurrence == largeDealOccurrenceRef transportSplit) $
    fail "transport ordinal 进入了 F4 occurrence identity"
  requireCompactBson
    "DirectedLargeDeal occurrence"
    [receiptArtifactLocation f4Receipt, receiptParameterSetId f4Receipt]
    occurrence
  nextOccurrence <-
    requireRight
      "typed F4 distinct producer occurrence"
      (decodeDirectedLargeDealNumericRow f4Receipt "buy__occ0001" (Map.insert "producer_local_no" (fromIntegral (localNo + 1)) row))
  unless (largeDealOccurrenceRef occurrence /= largeDealOccurrenceRef nextOccurrence) $
    fail "不同 producer-local F4 occurrence 被错误合并"
  requireBsonRoundTrip "DirectedLargeDeal occurrence" occurrence

wallLifecycleMustBeProductSpecificAndIdempotent :: IO ()
wallLifecycleMustBeProductSpecificAndIdempotent = do
  (state, published) <- requireRight "Wall start" (applyWallOccurrenceBatch emptyWallLifecycleState [wallStart])
  unless (published == [wallStart]) $ fail "Wall state 与 public occurrence 没有原子推进"
  (sameState, duplicatePublications) <- requireRight "Wall duplicate" (applyWallOccurrenceBatch state [wallStart])
  unless (sameState == state && null duplicatePublications) $ fail "相同 Wall occurrence 重放必须幂等且不得重复公开"
  let conflict = wallStart {wallOccurrenceIdentity = otherWallIdentity}
  requireLeft "conflicting duplicate" (applyWallOccurrenceBatch state [conflict])

wallLifecycleMustKeepBidAndAskWallsIndependent :: IO ()
wallLifecycleMustKeepBidAndAskWallsIndependent = do
  (startedState, starts) <-
    requireRight
      "same-UTI bid and ask Wall starts"
      (applyWallOccurrenceBatch emptyWallLifecycleState [wallStart, askWallStart])
  unless (starts == [wallStart, askWallStart]) $
    fail "同一 UTI 的 bid／ask Wall.Start 没有作为两个独立 occurrence 原子公开"
  let bidDormant =
        wallStart
          { wallOccurrenceRef = OccurrenceRef "wall-occurrence-bid-dormant",
            wallOccurrencePayload =
              Spine.WallLifecycleEvent
                (wallRefOf wallIdentity)
                (InstrumentSymbol "rb")
                BidWall
                11
                (Spine.WallPresenceChanged measuredBand Spine.WallDormant)
                Spine.WallLifecycleAvailable
          }
      askDormant =
        askWallStart
          { wallOccurrenceRef = OccurrenceRef "wall-occurrence-ask-dormant",
            wallOccurrencePayload =
              Spine.WallLifecycleEvent
                (wallRefOf otherWallIdentity)
                (InstrumentSymbol "rb")
                AskWall
                11
                (Spine.WallPresenceChanged measuredBand Spine.WallDormant)
                Spine.WallLifecycleAvailable
          }
  (_, presenceChanges) <-
    requireRight
      "independent bid and ask Wall transitions"
      (applyWallOccurrenceBatch startedState [bidDormant, askDormant])
  unless (presenceChanges == [bidDormant, askDormant]) $
    fail "bid／ask Wall 的独立身份在 DSU current map 中被覆盖"

wallLifecycleTransitionTableMustBeComplete :: IO ()
wallLifecycleTransitionTableMustBeComplete = do
  let wallChange ref occurredAt change =
        wallStart
          { wallOccurrenceRef = OccurrenceRef ref,
            wallOccurrencePayload =
              Spine.WallLifecycleEvent
                (wallRefOf wallIdentity)
                (InstrumentSymbol "rb")
                BidWall
                occurredAt
                change
                Spine.WallLifecycleAvailable
          }
      bandUpdated = wallChange "wall-occurrence-2" 11 (Spine.WallBandUpdated measuredBand Spine.WallAlive)
      becameDormant = wallChange "wall-occurrence-3" 12 (Spine.WallPresenceChanged measuredBand Spine.WallDormant)
      becamePresent = wallChange "wall-occurrence-4" 13 (Spine.WallPresenceChanged measuredBand Spine.WallAlive)
      ended = wallChange "wall-occurrence-5" 14 (Spine.WallEnded (Spine.WallEndReason "producer-end"))
      lifecycle = [wallStart, bandUpdated, becameDormant, becamePresent, ended]
      startedDormant = wallChange "wall-occurrence-invalid-start" 10 (Spine.WallStarted measuredBand Spine.WallDormant)
      samePresent = wallChange "wall-occurrence-invalid-same-present" 11 (Spine.WallPresenceChanged measuredBand Spine.WallAlive)
      bandChangesPresence = wallChange "wall-occurrence-invalid-band-presence" 11 (Spine.WallBandUpdated measuredBand Spine.WallDormant)
      sameDormant = wallChange "wall-occurrence-invalid-same-dormant" 13 (Spine.WallPresenceChanged measuredBand Spine.WallDormant)
      dormantBandChangesPresence = wallChange "wall-occurrence-invalid-dormant-band" 13 (Spine.WallBandUpdated measuredBand Spine.WallAlive)
  (endedState, publications) <- requireRight "complete Wall transition table" (applyWallOccurrenceBatch emptyWallLifecycleState lifecycle)
  unless (publications == lifecycle) $ fail "Wall transition table 没有逐 occurrence 原子公开"
  requireLeft "Wall cannot start Dormant" (applyWallOccurrenceBatch emptyWallLifecycleState [startedDormant])
  requireLeft "Wall update before start" (applyWallOccurrenceBatch emptyWallLifecycleState [bandUpdated])
  (presentState, _) <- requireRight "Wall present state" (applyWallOccurrenceBatch emptyWallLifecycleState [wallStart])
  requireLeft "Wall same-state Present change" (applyWallOccurrenceBatch presentState [samePresent])
  requireLeft "Wall band update cannot change presence" (applyWallOccurrenceBatch presentState [bandChangesPresence])
  (dormantState, _) <- requireRight "Wall dormant state" (applyWallOccurrenceBatch presentState [becameDormant])
  requireLeft "Wall same-state Dormant change" (applyWallOccurrenceBatch dormantState [sameDormant])
  requireLeft "Wall dormant band update cannot change presence" (applyWallOccurrenceBatch dormantState [dormantBandChangesPresence])
  requireLeft "Wall update after end" (applyWallOccurrenceBatch endedState [bandUpdated {wallOccurrenceRef = OccurrenceRef "wall-occurrence-6"}])
  mapM_ (uncurry requireBsonRoundTrip) (zip ["Wall start", "Wall band update", "Wall dormant", "Wall present", "Wall end"] lifecycle)

buildStart :: BuildActivityOccurrence
buildStart =
  let identity = BuildActivityIdentity 7
      continuity = requirePureRight "unit interval" (mkUnitInterval 1)
      measurements = Spine.BuildMeasurements (Measured (Spine.Quantity 3)) (Measured continuity)
   in BuildActivityOccurrence
        identity
        wallIdentity
        (OccurrenceRef "build-occurrence-1")
        (Spine.BuildActivityEvent (buildRefOf identity) (wallRefOf wallIdentity) 10 (Spine.BuildStarted measurements) Spine.BuildAvailable)

absorbStart :: AbsorbInteractionOccurrence
absorbStart =
  let identity = AbsorbInteractionIdentity 9
      measurements = Spine.AbsorbMeasurements (Measured (Spine.Quantity 2)) (Measured (Spine.Quantity 1)) (Measured (Spine.TickDistance 0))
   in AbsorbInteractionOccurrence
        identity
        wallIdentity
        (OccurrenceRef "absorb-occurrence-1")
        AbsorbStartedOccurrence
        Nothing
        Nothing
        (Spine.AbsorbInteractionEvent (absorbRefOf identity) (wallRefOf wallIdentity) 10 (Spine.AbsorbInteractionStarted measurements) Spine.AbsorbAvailable)

formation :: AttackFormationMaterialOccurrence
formation =
  AttackFormationMaterialOccurrence
    wallIdentity
    (OccurrenceRef "formation-occurrence-1")
    (Just (attackSegmentAttemptRefOf (AttackSegmentAttemptIdentity 17)))
    AcceptedMaterialEvidence
    10
    10
    10
    FormationEvidenceAvailable
    Nothing
    (Spine.AttackFormationMaterial (AttackFormationScopeRef "formation-scope-1") (wallRefOf wallIdentity) (InstrumentSymbol "rb") AggressiveSell 10 Spine.FormationMaterialAvailable (Spine.AcceptedFormationMaterial (Spine.FormationWallSource (wallRefOf wallIdentity))))

dependentDsusMustUseFixedExactWallCatalog :: IO ()
dependentDsusMustUseFixedExactWallCatalog = do
  requireLeft "Build without exact Wall" (applyBuildFrame (emptyBuildActivityState emptyWallIdentityCatalog) [buildStart])
  (_, builds) <- requireRight "Build with exact Wall catalog" (applyBuildFrame (emptyBuildActivityState wallCatalog) [buildStart])
  unless (builds == [buildStart]) $ fail "Build 未从固定 exact Wall catalog 接纳"
  requireLeft "Absorb without exact Wall" (applyAbsorbFrame (emptyAbsorbInteractionState emptyWallIdentityCatalog) [absorbStart])
  (_, absorbs) <- requireRight "Absorb with exact Wall catalog" (applyAbsorbFrame (emptyAbsorbInteractionState wallCatalog) [absorbStart])
  unless (absorbs == [absorbStart]) $ fail "Absorb 未从固定 exact Wall catalog 接纳"
  _ <- requireRight "Attack with exact Wall catalog" (applyAttackFrame (emptyAttackSegmentBookState wallCatalog) [] [formation] [])
  requireLeft "Attack without exact Wall" (applyAttackFrame (emptyAttackSegmentBookState emptyWallIdentityCatalog) [] [formation] [])

buildAndAbsorbTransitionTablesMustBeComplete :: IO ()
buildAndAbsorbTransitionTablesMustBeComplete = do
  let buildIdentity = buildOccurrenceIdentity buildStart
      continuity = requirePureRight "unit interval" (mkUnitInterval 1)
      buildMeasurements = Spine.BuildMeasurements (Measured (Spine.Quantity 3)) (Measured continuity)
      buildChange ref occurredAt change =
        buildStart
          { buildOccurrenceRef = OccurrenceRef ref,
            buildOccurrencePayload =
              Spine.BuildActivityEvent
                (buildRefOf buildIdentity)
                (wallRefOf wallIdentity)
                occurredAt
                change
                Spine.BuildAvailable
          }
      buildMilestone =
        buildChange
          "build-occurrence-2"
          11
          (Spine.BuildReachedMilestone (Spine.BuildMilestone "half") (Spine.BuildMilestoneRatio continuity) buildMeasurements)
      buildStopped = buildChange "build-occurrence-3" 12 (Spine.BuildStopped (Spine.BuildStopReason "producer-stop") buildMeasurements)
      buildLifecycle = [buildStart, buildMilestone, buildStopped]
      buildReboundToOtherWall =
        buildStart
          { buildOccurrenceWallIdentity = otherWallIdentity,
            buildOccurrenceRef = OccurrenceRef "build-occurrence-other-wall",
            buildOccurrencePayload =
              Spine.BuildActivityEvent
                (buildRefOf buildIdentity)
                (wallRefOf otherWallIdentity)
                11
                (Spine.BuildReachedMilestone (Spine.BuildMilestone "half") (Spine.BuildMilestoneRatio continuity) buildMeasurements)
                Spine.BuildAvailable
          }
  (buildState, buildPublications) <- requireRight "complete Build transition table" (applyBuildFrame (emptyBuildActivityState wallCatalog) buildLifecycle)
  unless (buildPublications == buildLifecycle) $ fail "Build transition table 没有逐 occurrence 原子公开"
  requireLeft "Build milestone before start" (applyBuildFrame (emptyBuildActivityState wallCatalog) [buildMilestone])
  requireLeft "Build update after stop" (applyBuildFrame buildState [buildMilestone {buildOccurrenceRef = OccurrenceRef "build-occurrence-4"}])
  (twoWallBuildState, _) <- requireRight "Build start with two valid Walls" (applyBuildFrame (emptyBuildActivityState twoWallCatalog) [buildStart])
  requireLeft "Build identity cannot switch exact Wall" (applyBuildFrame twoWallBuildState [buildReboundToOtherWall])
  (sameBuildState, duplicateBuildPublications) <- requireRight "Build exact duplicate" (applyBuildFrame buildState [buildStart])
  unless (sameBuildState == buildState && null duplicateBuildPublications) $ fail "Build exact duplicate 不是幂等重放"
  requireLeft "Build conflicting duplicate" (applyBuildFrame buildState [buildStart {buildOccurrenceIdentity = BuildActivityIdentity 8}])
  mapM_ (uncurry requireBsonRoundTrip) (zip ["Build start", "Build milestone", "Build stop"] buildLifecycle)

  let absorbIdentity = absorbOccurrenceIdentity absorbStart
      absorbMeasurements = Spine.AbsorbMeasurements (Measured (Spine.Quantity 2)) (Measured (Spine.Quantity 1)) (Measured (Spine.TickDistance 0))
      absorbChange ref occurredAt kind milestoneLevel resolvedReason change =
        absorbStart
          { absorbOccurrenceRef = OccurrenceRef ref,
            absorbOccurrenceKind = kind,
            absorbOccurrenceMilestoneLevel = milestoneLevel,
            absorbOccurrenceResolvedReason = resolvedReason,
            absorbOccurrencePayload =
              Spine.AbsorbInteractionEvent
                (absorbRefOf absorbIdentity)
                (wallRefOf wallIdentity)
                occurredAt
                change
                Spine.AbsorbAvailable
          }
      absorbMilestone =
        absorbChange
          "absorb-occurrence-2"
          11
          AbsorbConsumptionMilestoneOccurrence
          (Just 0.5)
          Nothing
          (Spine.AbsorbConsumptionMilestone absorbMeasurements)
      absorbResolved =
        absorbChange
          "absorb-occurrence-3"
          12
          AbsorbResolvedOccurrence
          Nothing
          (Just "breakthrough")
          (Spine.AbsorbInteractionResolved (Spine.AbsorbResolution "breakthrough") absorbMeasurements)
      absorbLifecycle = [absorbStart, absorbMilestone, absorbResolved]
      absorbReboundToOtherWall =
        absorbStart
          { absorbOccurrenceWallIdentity = otherWallIdentity,
            absorbOccurrenceRef = OccurrenceRef "absorb-occurrence-other-wall",
            absorbOccurrenceKind = AbsorbConsumptionMilestoneOccurrence,
            absorbOccurrenceMilestoneLevel = Just 0.5,
            absorbOccurrencePayload =
              Spine.AbsorbInteractionEvent
                (absorbRefOf absorbIdentity)
                (wallRefOf otherWallIdentity)
                11
                (Spine.AbsorbConsumptionMilestone absorbMeasurements)
                Spine.AbsorbAvailable
          }
  (absorbState, absorbPublications) <- requireRight "complete Absorb transition table" (applyAbsorbFrame (emptyAbsorbInteractionState wallCatalog) absorbLifecycle)
  unless (absorbPublications == absorbLifecycle) $ fail "Absorb transition table 没有逐 occurrence 原子公开"
  requireLeft "Absorb milestone before start" (applyAbsorbFrame (emptyAbsorbInteractionState wallCatalog) [absorbMilestone])
  requireLeft "Absorb update after resolution" (applyAbsorbFrame absorbState [absorbMilestone {absorbOccurrenceRef = OccurrenceRef "absorb-occurrence-4"}])
  (twoWallAbsorbState, _) <- requireRight "Absorb start with two valid Walls" (applyAbsorbFrame (emptyAbsorbInteractionState twoWallCatalog) [absorbStart])
  requireLeft "Absorb identity cannot switch exact Wall" (applyAbsorbFrame twoWallAbsorbState [absorbReboundToOtherWall])
  (sameAbsorbState, duplicateAbsorbPublications) <- requireRight "Absorb exact duplicate" (applyAbsorbFrame absorbState [absorbStart])
  unless (sameAbsorbState == absorbState && null duplicateAbsorbPublications) $ fail "Absorb exact duplicate 不是幂等重放"
  requireLeft "Absorb conflicting duplicate" (applyAbsorbFrame absorbState [absorbStart {absorbOccurrenceIdentity = AbsorbInteractionIdentity 10}])
  mapM_ (uncurry requireBsonRoundTrip) (zip ["Absorb start", "Absorb milestone", "Absorb resolved"] absorbLifecycle)

sameUtiPermutationMustNotChangeAttackBook :: IO ()
sameUtiPermutationMustNotChangeAttackBook = do
  let second = formation {formationOccurrenceRef = OccurrenceRef "formation-occurrence-2"}
  (forward, _) <- requireRight "forward" (applyAttackFrame (emptyAttackSegmentBookState wallCatalog) [] [formation, second] [])
  (reversed, _) <- requireRight "reversed" (applyAttackFrame (emptyAttackSegmentBookState wallCatalog) [] [second, formation] [])
  unless (forward == reversed) $ fail "同拍 formation 物理顺序改变了 AttackSegmentBook current view"

-- 2026-08-25 owner 修正后，旧的“current view 保存完整 Formation／Barrier
-- history”测试已过期：历史只由各自 append-only writer 保存，current view
-- 不得再复制 occurrence payload。
attackCurrentViewMustNotCopyOccurrenceHistory :: IO ()
attackCurrentViewMustNotCopyOccurrenceHistory = do
  (state, _) <-
    requireRight
      "Attack occurrence history is published without entering current view"
      (applyAttackFrame (emptyAttackSegmentBookState wallCatalog) [] [formation] [])
  unless (currentAttackSegmentBookView state == emptyAttackSegmentBookCurrentView) $
    fail "Attack current view 仍复制了 Formation／Barrier occurrence history"

productBatchesMustNotPartiallyPublish :: IO ()
productBatchesMustNotPartiallyPublish = do
  let conflictingWall = wallStart {wallOccurrenceIdentity = otherWallIdentity}
      conflictingBuild = buildStart {buildOccurrenceIdentity = BuildActivityIdentity 8}
      conflictingAbsorb = absorbStart {absorbOccurrenceIdentity = AbsorbInteractionIdentity 10}
      conflictingFormation = formation {formationOccurrenceReason = Just "conflicting-replay"}
  requireLeft
    "Wall transaction must reject the complete batch"
    (applyWallOccurrenceBatch emptyWallLifecycleState [wallStart, conflictingWall])
  requireLeft
    "Build transaction must reject the complete batch"
    (applyBuildFrame (emptyBuildActivityState wallCatalog) [buildStart, conflictingBuild])
  requireLeft
    "Absorb transaction must reject the complete batch"
    (applyAbsorbFrame (emptyAbsorbInteractionState wallCatalog) [absorbStart, conflictingAbsorb])
  requireLeft
    "Attack transaction must reject all simultaneous product streams"
    (applyAttackFrame (emptyAttackSegmentBookState wallCatalog) [] [formation, conflictingFormation] [])
  (_, wallPublished) <- requireRight "Wall remains clean after rejected batch" (applyWallOccurrenceBatch emptyWallLifecycleState [wallStart])
  (_, buildPublished) <- requireRight "Build remains clean after rejected batch" (applyBuildFrame (emptyBuildActivityState wallCatalog) [buildStart])
  (_, absorbPublished) <- requireRight "Absorb remains clean after rejected batch" (applyAbsorbFrame (emptyAbsorbInteractionState wallCatalog) [absorbStart])
  _ <- requireRight "Attack remains clean after rejected batch" (applyAttackFrame (emptyAttackSegmentBookState wallCatalog) [] [formation] [])
  unless (wallPublished == [wallStart]) $ fail "Wall rejected batch leaked partial state/publication"
  unless (buildPublished == [buildStart]) $ fail "Build rejected batch leaked partial state/publication"
  unless (absorbPublished == [absorbStart]) $ fail "Absorb rejected batch leaked partial state/publication"

p2HandoffFixtureMustReadFullProducerPayload :: IO ()
p2HandoffFixtureMustReadFullProducerPayload = do
  let segmentRow =
        Map.fromList
          [ ("segment_id", 17),
            ("attack_segment_attempt_local_id", 17),
            ("wall_local_no", fromIntegral localNo),
            ("side_code", 2),
            ("start_uti", 10),
            ("business_end_uti", 12),
            ("closed_at_uti", 13),
            ("close_reason_code", 1),
            ("lane_mask", 3),
            ("hit_occurrence_count_v0", 2),
            ("occurrence_utis_count", 2),
            ("directional_hit_volume_proxy_total_v0", 9),
            ("amount_total_v0", 900),
            ("vol_tactical_overlap_view", 4),
            ("vol_structural_overlap_view", 5),
            ("largest_directional_hit_volume_proxy_v0", 6),
            ("max_grade", 4),
            ("entry_price", 100),
            ("exit_price", 102),
            ("min_price", 99),
            ("max_price", 103),
            ("net_progress_ticks", 2),
            ("max_retreat_from_best_ticks", 1),
            ("max_dist_deal_to_core_ticks", 3),
            ("last_dist_deal_to_core_ticks", 1),
            ("max_wall_core_shift_ticks", 1),
            ("availability_code", 1)
          ]
      qualifiedRows =
        [ Map.fromList [("segment_id", 17), ("ordinal", 0), ("qualified_uti", 10)],
          Map.fromList [("segment_id", 17), ("ordinal", 1), ("qualified_uti", 12)]
        ]
      qualificationHitRows =
        [ Map.fromList
            [ ("segment_id", 17),
              ("ordinal", 0),
              ("selected_stream_ordinal", 0),
              ("qualification_family_code", 1),
              ("grade", 2)
            ],
          Map.fromList
            [ ("segment_id", 17),
              ("ordinal", 1),
              ("selected_stream_ordinal", 1),
              ("qualification_family_code", 2),
              ("grade", 4)
            ]
        ]
  segment <-
    requireRight
      "P2 full AttackSegment compact fixture"
      (decodeAttackSegmentNumericRow attackReceipt wallCatalog "segment__stream" segmentRow qualifiedRows qualificationHitRows)
  snapshot <- requireRight "P2 Attack run-level method snapshot" (attackFormationMethodSnapshotFromReceipt attackReceipt)
  let hitSummary = fmap (\hit -> (qualificationFamily hit, qualificationGrade hit)) (attackOccurrenceQualificationHits segment)
      Spine.AttackSegmentAtWall
        { Spine.attackSegmentAttempt = segmentAttemptRef,
          Spine.attackSegmentTimeSpan = timeSpan,
          Spine.tacticalLaneGrade = tacticalGrade,
          Spine.structuralLaneGrade = structuralGrade,
          Spine.attackSegmentLoad = load,
          Spine.attackSegmentPricePath = pricePath,
          Spine.attackSegmentProximity = proximity
        } = attackOccurrencePayload segment
  unless
    ( qualificationParameterSets snapshot == ["f4-tactical-A", "f4-structural-A"]
        && laneMergePolicy snapshot == "attack-segment-local-union-keep-labels"
        && hitSummary == [("tactical", 2), ("structural", 4)]
        && attackOccurrenceAvailability segment == AttackSegmentAvailable
        && attackOccurrenceUnavailableReason segment == Nothing
        && segmentAttemptRef == attackSegmentAttemptRefOf (AttackSegmentAttemptIdentity 17)
        && tacticalGrade == Spine.LaneObserved (requirePureRight "P2 fixture tactical grade" (Spine.mkPositiveGrade 2))
        && structuralGrade == Spine.LaneObserved (requirePureRight "P2 fixture structural grade" (Spine.mkPositiveGrade 4))
        && Spine.attackSegmentStart timeSpan == 10
        && Spine.attackSegmentBusinessEnd timeSpan == 12
        && Spine.attackSegmentClosedAt timeSpan == 13
        && Spine.attackHitOccurrenceCount load == requirePureRight "P2 fixture occurrence count" (Spine.mkOccurrenceCount 2)
        && Spine.attackEntryPrice pricePath == Measured (Spine.Price 100)
        && Spine.attackLastDistanceFromWallCoreTicks proximity == Spine.TickDistance 1
    )
    (fail "P2 fixture 无法读取完整 AttackSegment payload／method snapshot")
  let tacticalOnlyRow =
        Map.insert "lane_mask" 1
          . Map.insert "max_grade" 2
          $ segmentRow
  tacticalOnly <- requireRight "P2 tactical-only AttackSegment fixture" (decodeAttackSegmentNumericRow attackReceipt wallCatalog "segment__stream" tacticalOnlyRow qualifiedRows (take 1 qualificationHitRows))
  unless
    ( Spine.tacticalLaneGrade (attackOccurrencePayload tacticalOnly)
        == Spine.LaneObserved (requirePureRight "P2 tactical-only grade" (Spine.mkPositiveGrade 2))
        && Spine.structuralLaneGrade (attackOccurrencePayload tacticalOnly) == Spine.LaneAbsent
    )
    (fail "P2 fixture 没有区分实际 tactical grade 与未参与的 structural lane")
  requireLeft
    "merged max_grade cannot replace preserved lane grades"
    (decodeAttackSegmentNumericRow attackReceipt wallCatalog "segment__stream" (Map.insert "max_grade" 9 segmentRow) qualifiedRows qualificationHitRows)
  requireLeft
    "final AttackSegment must retain the same producer-local attempt id"
    (decodeAttackSegmentNumericRow attackReceipt wallCatalog "segment__stream" (Map.insert "attack_segment_attempt_local_id" 18 segmentRow) qualifiedRows qualificationHitRows)
  requireLeft
    "per-segment result key must not remain a supported Attack transport"
    (decodeAttackSegmentNumericRow attackReceipt wallCatalog "segment__17" segmentRow qualifiedRows qualificationHitRows)
  case decodeAttackSegmentTransportBatch
    attackReceipt
    wallCatalog
    ( ("segment__stream", segmentRow)
        : fmap ((,) "segment_qualified_uti__stream") qualifiedRows
          <> zipWith
            (\ordinal row -> (if ordinal == (0 :: Int) then "segment_qualification_hit__stream" else "segment_qualification_hit__stream__occ0001", row))
            [0 ..]
            qualificationHitRows
    ) of
    [Right reconstructed] | attackOccurrenceIdentity reconstructed == attackOccurrenceIdentity segment -> pure ()
    _ -> fail "紧凑 Attack 主流与两个明细流没有在同一闭段 occurrence 上重组"
  case decodeAttackSegmentTransportBatch
    attackReceipt
    wallCatalog
    (fmap ((,) "segment_qualified_uti__stream") qualifiedRows) of
    [] -> fail "紧凑 Attack 明细流在缺主行时没有产生 diagnostic"
    diagnostics | all isLeft diagnostics -> pure ()
    _ -> fail "紧凑 Attack 明细流在缺主行时没有 fail closed"

  let formationRow =
        Map.fromList
          [ ("formation_local_id", 8),
            ("source_material_local_ref", 7),
            ("attack_segment_attempt_local_id", 0),
            ("uti", 16),
            ("interval_start_uti", 14),
            ("interval_end_uti", 16),
            ("available_at_uti", 16),
            ("availability_code", 1),
            ("body_kind_code", 4),
            ("reason_code", 4)
          ]
  interval <- requireRight "P2 FormationEvidence interval fixture" (decodeAttackFormationNumericRow attackReceipt wallCatalog ("formation__" <> Text.pack (show localNo) <> "__ask") formationRow)
  unless
    ( formationOccurrenceKind interval == ObservedNoAcceptedAttackIntervalEvidence
        && formationOccurrenceAttemptRef interval == Nothing
        && formationOccurrenceStartUti interval == 14
        && formationOccurrenceEndUti interval == 16
        && formationOccurrenceAvailableAt interval == 16
        && formationOccurrenceAvailability interval == FormationEvidenceAvailable
        && formationOccurrenceReason interval == Just "observed_no_accepted_attack_interval"
        && case Spine.attackFormationBody (formationOccurrencePayload interval) of
          Spine.ObservedNoAcceptedAttackInterval _ _ -> True
          _ -> False
    )
    (fail "P2 fixture 丢失 FormationEvidence 区间角色或边界")
  let acceptedFormationRow =
        Map.fromList
          [ ("formation_local_id", 9),
            ("source_material_local_ref", 12),
            ("attack_segment_attempt_local_id", 17),
            ("uti", 12),
            ("available_at_uti", 12),
            ("availability_code", 1),
            ("body_kind_code", 1),
            ("reason_code", 0)
          ]
      formationKey = "formation__" <> Text.pack (show localNo) <> "__ask"
      expectedAttemptRef =
        attackSegmentAttemptRefOf
          (AttackSegmentAttemptIdentity 17)
  acceptedFormation <-
    requireRight
      "accepted FormationEvidence attempt fixture"
      (decodeAttackFormationNumericRow attackReceipt wallCatalog formationKey acceptedFormationRow)
  unless (formationOccurrenceAttemptRef acceptedFormation == Just expectedAttemptRef) $
    fail "accepted FormationEvidence 没有保留所属 AttackSegment attempt"
  requireLeft
    "accepted FormationEvidence without attempt must fail closed"
    (decodeAttackFormationNumericRow attackReceipt wallCatalog formationKey (Map.insert "attack_segment_attempt_local_id" 0 acceptedFormationRow))
  requireLeft
    "FormationEvidence cannot become available before its business interval ends"
    (decodeAttackFormationNumericRow attackReceipt wallCatalog formationKey (Map.insert "available_at_uti" 15 formationRow))

  let capabilityRow reasonCode =
        Map.fromList
          [ ("formation_local_id", fromIntegral reasonCode),
            ("source_material_local_ref", 7),
            ("attack_segment_attempt_local_id", 0),
            ("uti", 16),
            ("interval_start_uti", 14),
            ("interval_end_uti", 16),
            ("available_at_uti", 16),
            ("availability_code", 6),
            ("body_kind_code", 6),
            ("reason_code", fromIntegral reasonCode)
          ]
      capabilityReasons =
        [ (6, "near_miss_not_observed_current_v0"),
          (7, "retreat_trace_unavailable_current_v0"),
          (8, "band_shift_trace_unavailable_current_v0")
        ]
  capabilities <-
    mapM
      ( \(reasonCode, _) ->
          requireRight
            "P2 FormationEvidence capability fixture"
            (decodeAttackFormationNumericRow attackReceipt wallCatalog ("formation__" <> Text.pack (show localNo) <> "__ask") (capabilityRow reasonCode))
      )
      capabilityReasons
  unless
    ( and
        [ formationOccurrenceKind occurrence == CapabilityUnavailableEvidence
            && formationOccurrenceAvailability occurrence == FormationEvidenceUnavailable
            && formationOccurrenceReason occurrence == Just reason
          | (occurrence, (_, reason)) <- zip capabilities capabilityReasons
        ]
    )
    (fail "P2 fixture 没有无损读取 near-miss／retreat／band-shift unavailable 声明")

  let barrierRow =
        Map.fromList
          [ ("barrier_local_id", 3),
            ("source_material_local_ref", 7),
            ("uti", 17),
            ("barrier_kind_code", 1)
          ]
  barrier <- requireRight "P2 formal barrier fixture" (decodeWallBarrierNumericRow attackReceipt wallCatalog ("barrier__" <> Text.pack (show localNo) <> "__ask") barrierRow)
  unless (Spine.wallAttackBarrierKind (barrierOccurrencePayload barrier) == Spine.WallEndedBarrier) $ fail "P2 fixture 没有读取 formal Wall.End barrier"
  requireLeft "unsupported barrier source" (decodeWallBarrierNumericRow attackReceipt wallCatalog ("barrier__" <> Text.pack (show localNo) <> "__ask") (Map.insert "barrier_kind_code" 2 barrierRow))

  let absorbBase =
        Map.fromList
          [ ("wall_local_no", fromIntegral localNo),
            ("uti", 18),
            ("availability_code", 1),
            ("consumed_proxy_cum", 2),
            ("replenishment_proxy", 1),
            ("price_progress_ticks", 1)
          ]
      milestoneRow = Map.insert "level" 0.5 (Map.insert "event_type_code" 12 absorbBase)
      resolvedRow = Map.insert "resolved_type_code" 1 (Map.insert "event_type_code" 13 absorbBase)
  milestone <- requireRight "P2 Absorb milestone fixture" (decodeAbsorbNumericRow absorbReceipt wallCatalog "absorb__9" milestoneRow)
  resolved <- requireRight "P2 Absorb resolved fixture" (decodeAbsorbNumericRow absorbReceipt wallCatalog "absorb__9" resolvedRow)
  unless
    ( absorbOccurrenceKind milestone == AbsorbConsumptionMilestoneOccurrence
        && absorbOccurrenceMilestoneLevel milestone == Just 0.5
        && absorbOccurrenceResolvedReason milestone == Nothing
        && absorbOccurrenceKind resolved == AbsorbResolvedOccurrence
        && absorbOccurrenceResolvedReason resolved == Just "breakthrough"
    )
    (fail "P2 fixture 丢失 Absorb milestone level 或 resolved reason")
  (attackState, _) <-
    requireRight
      "AttackSegmentBook accepts all three product streams"
      (applyAttackFrame (emptyAttackSegmentBookState wallCatalog) [segment] [interval] [barrier])
  (sameAttackState, _) <-
    requireRight
      "AttackSegmentBook exact duplicate"
      (applyAttackFrame attackState [segment] [interval] [barrier])
  unless (sameAttackState == attackState) $ fail "AttackSegmentBook exact duplicate 不是幂等重放"
  requireLeft
    "AttackSegmentBook conflicting duplicate"
    (applyAttackFrame attackState [segment {attackOccurrenceAvailability = AttackSegmentTechnicalTruncated}] [] [])
  requireBsonRoundTrip "Wall occurrence" wallStart
  requireCompactBson "Wall occurrence" [receiptArtifactLocation wallReceipt, receiptParameterSetId wallReceipt] wallStart
  requireBsonRoundTrip "Build occurrence" buildStart
  requireCompactBson "Build occurrence" [receiptArtifactLocation buildReceipt, receiptParameterSetId buildReceipt] buildStart
  requireBsonRoundTrip "AttackSegment occurrence" segment
  requireCompactBson
    "AttackSegment occurrence"
    [ receiptArtifactLocation attackReceipt,
      receiptParameterSetId attackReceipt,
      "f4-tactical-A",
      "f4-structural-A",
      "sha256:attack-method-A"
    ]
    segment
  requireBsonRoundTrip "FormationEvidence occurrence" interval
  requireCompactBson "FormationEvidence occurrence" [receiptArtifactLocation attackReceipt, receiptParameterSetId attackReceipt] interval
  requireBsonRoundTrip "Barrier occurrence" barrier
  requireCompactBson "Barrier occurrence" [receiptArtifactLocation attackReceipt, receiptParameterSetId attackReceipt] barrier
  requireBsonRoundTrip "Absorb milestone occurrence" milestone
  requireCompactBson "Absorb milestone occurrence" [receiptArtifactLocation absorbReceipt, receiptParameterSetId absorbReceipt] milestone
  requireBsonRoundTrip "Absorb resolved occurrence" resolved

requireRight :: (Show error) => String -> Either error value -> IO value
requireRight label = either (fail . ((label <> ": ") <>) . show) pure

requireLeft :: String -> Either error value -> IO ()
requireLeft _ (Left _) = pure ()
requireLeft label (Right _) = fail (label <> " unexpectedly accepted")

requireBsonRoundTrip :: (Eq value, ToBSON value, FromBSON value) => String -> value -> IO ()
requireBsonRoundTrip label value =
  let document = toBSON value
   in unless (fromBSON document == Just value) $ fail (label <> " BSON round-trip failed: " <> show document)

requireCompactBson :: (ToBSON value) => String -> [Text.Text] -> value -> IO ()
requireCompactBson label forbidden value = do
  let rendered = Text.pack (show (toBSON value))
  unless ("compact-local-v2" `Text.isInfixOf` rendered) $
    fail (label <> " BSON 没有新 compact occurrence schema 标记")
  if any (`Text.isInfixOf` rendered) forbidden
    then fail (label <> " BSON 仍逐 occurrence 重复运行级长身份／artifact path")
    else pure ()

requirePureRight :: (Show error) => String -> Either error value -> value
requirePureRight label = either (error . ((label <> ": ") <>) . show) id
