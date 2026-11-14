{-# LANGUAGE DeriveAnyClass #-}
{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE UndecidableInstances #-}

-- | P1 产品 DSU 的正式 writer。
--
-- 每个 writer 只物化自己的 typed product。批次外壳只保留同一 FRP
-- transaction 中的 0..N 条 occurrence 或本次变化的 current state；业务字段
-- 仍由产品 ADT 逐字段进入现有 DBA，不经 @show@ 文本化，也不形成 P1 总表。
module Frp.Instance.ISL.Eaw.P1.Publication
  ( dumpWallOutputs,
    dumpBuildOutputs,
    dumpAttackOutputs,
    dumpAbsorbOutputs,
  )
where

import Data.List.NonEmpty (NonEmpty (..))
import Data.Text qualified as Text
import Database.MongoDB (Val, (=:))
import Database.MongoDB qualified as BSON
import Frp.Apt.Bson (FromBSON (..), ToBSON (..))
import Frp.Core (Fao, FaoModel, dumpAdtEvent', withEventDump)
import Frp.Instance.ISL.Eaw.Interface.Common
import Frp.Instance.ISL.Eaw.Interface.PreL0 qualified as Spine
import Frp.Instance.ISL.Eaw.P1.AbsorbInteraction
import Frp.Instance.ISL.Eaw.P1.AttackSegmentBook
import Frp.Instance.ISL.Eaw.P1.BuildActivity
import Frp.Instance.ISL.Eaw.P1.Products
import Frp.Instance.ISL.Eaw.P1.WallLifecycle
import GHC.Generics (Generic)

-- P1 writer 的现有 DBA 只要求 BSON 实例。实例留在产品 writer 内，避免让
-- 共享接口脊柱反向承担 P1 的物理持久化责任；序列化对象仍是唯一 canonical
-- ADT，并未定义第二套业务 payload。
instance ToBSON InstrumentSymbol

instance FromBSON InstrumentSymbol

instance ToBSON UnitInterval

instance FromBSON UnitInterval

instance ToBSON WallSide

instance FromBSON WallSide

instance ToBSON AggressorDirection

instance FromBSON AggressorDirection

instance (Val a) => ToBSON (Measurement a)

instance (Val a) => FromBSON (Measurement a)

instance ToBSON WallRef

instance FromBSON WallRef

instance ToBSON BuildRef

instance FromBSON BuildRef

instance ToBSON AttackFormationScopeRef

instance FromBSON AttackFormationScopeRef

instance ToBSON SourceMaterialRef

instance FromBSON SourceMaterialRef

instance ToBSON FormationEvidenceRef

instance FromBSON FormationEvidenceRef

instance ToBSON AttackSegmentRef

instance FromBSON AttackSegmentRef

instance ToBSON AttackSegmentAttemptRef

instance FromBSON AttackSegmentAttemptRef

instance ToBSON AbsorbRef

instance FromBSON AbsorbRef

instance ToBSON BarrierRef

instance FromBSON BarrierRef

instance ToBSON ActiveFlowFrameRef

instance FromBSON ActiveFlowFrameRef

instance ToBSON LargeDealEventRef

instance FromBSON LargeDealEventRef

instance ToBSON MethodRef

instance FromBSON MethodRef

instance ToBSON Spine.Price

instance FromBSON Spine.Price

instance ToBSON Spine.Quantity

instance FromBSON Spine.Quantity

instance ToBSON Spine.Amount

instance FromBSON Spine.Amount

instance ToBSON Spine.TickDistance

instance FromBSON Spine.TickDistance

instance ToBSON Spine.OccurrenceCount

instance FromBSON Spine.OccurrenceCount

instance ToBSON Spine.WallBand

instance FromBSON Spine.WallBand

instance ToBSON Spine.WallPresence

instance FromBSON Spine.WallPresence

instance ToBSON Spine.WallLifecycleAvailability

instance FromBSON Spine.WallLifecycleAvailability

instance ToBSON Spine.WallEndReason

instance FromBSON Spine.WallEndReason

instance ToBSON Spine.WallLifecycleChange where
  toBSON change =
    case change of
      Spine.WallStarted band presence ->
        [ "_co" =: ("WallStarted" :: String),
          "band" =: band,
          "presence" =: presence
        ]
      Spine.WallBandUpdated band presence ->
        [ "_co" =: ("WallBandUpdated" :: String),
          "band" =: band,
          "presence" =: presence
        ]
      Spine.WallPresenceChanged band presence ->
        [ "_co" =: ("WallPresenceChanged" :: String),
          "band" =: band,
          "presence" =: presence
        ]
      Spine.WallEnded reason ->
        [ "_co" =: ("WallEnded" :: String),
          "reason" =: reason
        ]

instance FromBSON Spine.WallLifecycleChange where
  fromBSON document = do
    constructor <- BSON.lookup "_co" document :: Maybe String
    case constructor of
      "WallStarted" ->
        Spine.WallStarted
          <$> BSON.lookup "band" document
          <*> BSON.lookup "presence" document
      "WallBandUpdated" ->
        Spine.WallBandUpdated
          <$> BSON.lookup "band" document
          <*> BSON.lookup "presence" document
      "WallPresenceChanged" ->
        Spine.WallPresenceChanged
          <$> BSON.lookup "band" document
          <*> BSON.lookup "presence" document
      "WallEnded" -> Spine.WallEnded <$> BSON.lookup "reason" document
      _ -> Nothing

instance ToBSON Spine.WallLifecycleEvent

instance FromBSON Spine.WallLifecycleEvent

instance ToBSON Spine.BuildMilestone

instance FromBSON Spine.BuildMilestone

instance ToBSON Spine.BuildMilestoneValue

instance FromBSON Spine.BuildMilestoneValue

instance ToBSON Spine.BuildStopReason

instance FromBSON Spine.BuildStopReason

instance ToBSON Spine.BuildAvailability

instance FromBSON Spine.BuildAvailability

instance ToBSON Spine.BuildMeasurements

instance FromBSON Spine.BuildMeasurements

instance ToBSON Spine.BuildActivityChange where
  toBSON change =
    case change of
      Spine.BuildStarted measurements ->
        [ "_co" =: ("BuildStarted" :: String),
          "measurements" =: measurements
        ]
      Spine.BuildReachedMilestone milestone value measurements ->
        [ "_co" =: ("BuildReachedMilestone" :: String),
          "milestone" =: milestone,
          "value" =: value,
          "measurements" =: measurements
        ]
      Spine.BuildStopped reason measurements ->
        [ "_co" =: ("BuildStopped" :: String),
          "reason" =: reason,
          "measurements" =: measurements
        ]

instance FromBSON Spine.BuildActivityChange where
  fromBSON document = do
    constructor <- BSON.lookup "_co" document :: Maybe String
    case constructor of
      "BuildStarted" -> Spine.BuildStarted <$> BSON.lookup "measurements" document
      "BuildReachedMilestone" ->
        Spine.BuildReachedMilestone
          <$> BSON.lookup "milestone" document
          <*> BSON.lookup "value" document
          <*> BSON.lookup "measurements" document
      "BuildStopped" ->
        Spine.BuildStopped
          <$> BSON.lookup "reason" document
          <*> BSON.lookup "measurements" document
      _ -> Nothing

instance ToBSON Spine.BuildActivityEvent

instance FromBSON Spine.BuildActivityEvent

instance ToBSON Spine.AttackFormationReason

instance FromBSON Spine.AttackFormationReason

instance ToBSON Spine.AttackFormationAvailability

instance FromBSON Spine.AttackFormationAvailability

instance ToBSON Spine.AttackFormationSource

instance FromBSON Spine.AttackFormationSource

instance ToBSON Spine.AttackFormationBody where
  toBSON body =
    case body of
      Spine.AcceptedFormationMaterial source ->
        [ "_co" =: ("AcceptedFormationMaterial" :: String),
          "source" =: source
        ]
      Spine.UnresolvedFormationMaterial reason source ->
        [ "_co" =: ("UnresolvedFormationMaterial" :: String),
          "reason" =: reason,
          "source" =: source
        ]
      Spine.MethodLocalGapBreak reason source ->
        [ "_co" =: ("MethodLocalGapBreak" :: String),
          "reason" =: reason,
          "source" =: source
        ]
      Spine.ObservedNoAcceptedAttackInterval reason source ->
        [ "_co" =: ("ObservedNoAcceptedAttackInterval" :: String),
          "reason" =: reason,
          "source" =: source
        ]
      Spine.FormalFormationBarrier barrier reason ->
        [ "_co" =: ("FormalFormationBarrier" :: String),
          "barrier" =: barrier,
          "reason" =: reason
        ]
      Spine.ExcludedFormationMaterial reason source ->
        [ "_co" =: ("ExcludedFormationMaterial" :: String),
          "reason" =: reason,
          "source" =: source
        ]

instance FromBSON Spine.AttackFormationBody where
  fromBSON document = do
    constructor <- BSON.lookup "_co" document :: Maybe String
    case constructor of
      "AcceptedFormationMaterial" ->
        Spine.AcceptedFormationMaterial <$> BSON.lookup "source" document
      "UnresolvedFormationMaterial" ->
        Spine.UnresolvedFormationMaterial
          <$> BSON.lookup "reason" document
          <*> BSON.lookup "source" document
      "MethodLocalGapBreak" ->
        Spine.MethodLocalGapBreak
          <$> BSON.lookup "reason" document
          <*> BSON.lookup "source" document
      "ObservedNoAcceptedAttackInterval" ->
        Spine.ObservedNoAcceptedAttackInterval
          <$> BSON.lookup "reason" document
          <*> BSON.lookup "source" document
      "FormalFormationBarrier" ->
        Spine.FormalFormationBarrier
          <$> BSON.lookup "barrier" document
          <*> BSON.lookup "reason" document
      "ExcludedFormationMaterial" ->
        Spine.ExcludedFormationMaterial
          <$> BSON.lookup "reason" document
          <*> BSON.lookup "source" document
      _ -> Nothing

instance ToBSON Spine.AttackFormationMaterial

instance FromBSON Spine.AttackFormationMaterial

instance ToBSON Spine.AttackLaneQualification

instance FromBSON Spine.AttackLaneQualification

instance ToBSON Spine.PositiveGrade where
  toBSON value = ["positiveGradeValue" =: Spine.positiveGradeValue value]

instance FromBSON Spine.PositiveGrade where
  fromBSON document = do
    value <- BSON.lookup "positiveGradeValue" document
    either (const Nothing) Just (Spine.mkPositiveGrade value)

instance ToBSON Spine.LaneGradeObservation where
  toBSON observation =
    case observation of
      Spine.LaneAbsent -> ["_co" =: ("LaneAbsent" :: String)]
      Spine.LaneObserved grade ->
        [ "_co" =: ("LaneObserved" :: String),
          "grade" =: grade
        ]
      Spine.LaneUnavailable -> ["_co" =: ("LaneUnavailable" :: String)]

instance FromBSON Spine.LaneGradeObservation where
  fromBSON document = do
    constructor <- BSON.lookup "_co" document :: Maybe String
    case constructor of
      "LaneAbsent" -> Just Spine.LaneAbsent
      "LaneObserved" -> Spine.LaneObserved <$> BSON.lookup "grade" document
      "LaneUnavailable" -> Just Spine.LaneUnavailable
      _ -> Nothing

instance ToBSON Spine.AttackSegmentCloseReason

instance FromBSON Spine.AttackSegmentCloseReason

instance ToBSON Spine.AttackSegmentTimeSpan

instance FromBSON Spine.AttackSegmentTimeSpan

instance ToBSON Spine.AttackSegmentLoad

instance FromBSON Spine.AttackSegmentLoad

instance ToBSON Spine.AttackSegmentPricePath

instance FromBSON Spine.AttackSegmentPricePath

instance ToBSON Spine.AttackSegmentProximity

instance FromBSON Spine.AttackSegmentProximity

instance ToBSON Spine.AttackCountSemantics

instance FromBSON Spine.AttackCountSemantics

instance ToBSON Spine.AttackVolumeSemantics

instance FromBSON Spine.AttackVolumeSemantics

instance ToBSON Spine.QualifiedOccurrenceUtis where
  toBSON value =
    case Spine.qualifiedOccurrenceUtis value of
      first :| rest -> ["qualifiedOccurrenceUtis" =: (first : rest)]

instance FromBSON Spine.QualifiedOccurrenceUtis where
  fromBSON document = do
    values <- BSON.lookup "qualifiedOccurrenceUtis" document
    case values of
      [] -> Nothing
      first : rest -> either (const Nothing) Just (Spine.mkQualifiedOccurrenceUtis (first :| rest))

instance ToBSON Spine.AttackSegmentAtWall

instance FromBSON Spine.AttackSegmentAtWall

instance ToBSON Spine.AbsorbResolution

instance FromBSON Spine.AbsorbResolution

instance ToBSON Spine.AbsorbAvailability

instance FromBSON Spine.AbsorbAvailability

instance ToBSON Spine.AbsorbMeasurements

instance FromBSON Spine.AbsorbMeasurements

instance ToBSON Spine.AbsorbInteractionChange where
  toBSON change =
    case change of
      Spine.AbsorbInteractionStarted measurements ->
        [ "_co" =: ("AbsorbInteractionStarted" :: String),
          "measurements" =: measurements
        ]
      Spine.AbsorbConsumptionMilestone measurements ->
        [ "_co" =: ("AbsorbConsumptionMilestone" :: String),
          "measurements" =: measurements
        ]
      Spine.AbsorbInteractionResolved resolution measurements ->
        [ "_co" =: ("AbsorbInteractionResolved" :: String),
          "resolution" =: resolution,
          "measurements" =: measurements
        ]

instance FromBSON Spine.AbsorbInteractionChange where
  fromBSON document = do
    constructor <- BSON.lookup "_co" document :: Maybe String
    case constructor of
      "AbsorbInteractionStarted" ->
        Spine.AbsorbInteractionStarted <$> BSON.lookup "measurements" document
      "AbsorbConsumptionMilestone" ->
        Spine.AbsorbConsumptionMilestone <$> BSON.lookup "measurements" document
      "AbsorbInteractionResolved" ->
        Spine.AbsorbInteractionResolved
          <$> BSON.lookup "resolution" document
          <*> BSON.lookup "measurements" document
      _ -> Nothing

instance ToBSON Spine.AbsorbInteractionEvent

instance FromBSON Spine.AbsorbInteractionEvent

instance ToBSON Spine.WallAttackBarrierKind

instance FromBSON Spine.WallAttackBarrierKind

instance ToBSON Spine.WallAttackBarrier

instance FromBSON Spine.WallAttackBarrier

instance ToBSON Spine.LargeDealLaneGrade

instance FromBSON Spine.LargeDealLaneGrade

instance ToBSON Spine.LargeDealLaneQualification

instance FromBSON Spine.LargeDealLaneQualification

instance ToBSON Spine.DirectedLargeDealAvailability

instance FromBSON Spine.DirectedLargeDealAvailability

instance ToBSON Spine.DirectedLargeDealEvent

instance FromBSON Spine.DirectedLargeDealEvent

instance ToBSON FeatureRunIdentity

instance FromBSON FeatureRunIdentity

instance ToBSON AttackFormationMethodSnapshot

instance FromBSON AttackFormationMethodSnapshot

instance ToBSON F4QualificationHit

instance FromBSON F4QualificationHit

instance ToBSON AttackSegmentAvailability

instance FromBSON AttackSegmentAvailability

instance ToBSON FormationEvidenceKind

instance FromBSON FormationEvidenceKind

instance ToBSON FormationEvidenceAvailability

instance FromBSON FormationEvidenceAvailability

instance ToBSON AbsorbOccurrenceKind

instance FromBSON AbsorbOccurrenceKind

-- 2026-08-25 物理合同断点。旧 occurrence ref 曾内嵌 artifact path／完整
-- FeatureRunIdentity；新格式只允许 compact local ref，并用显式 schema 标记
-- 令旧 BSON 缓存无法被当前 decoder 静默复用。这里不提供双轨 decoder。
instance ToBSON OccurrenceRef where
  toBSON (OccurrenceRef ref) =
    [ "_p1_occurrence_ref_schema" =: ("compact-local-v2" :: String),
      "value" =: Text.unpack ref
    ]

instance FromBSON OccurrenceRef where
  fromBSON document = do
    schema <- BSON.lookup "_p1_occurrence_ref_schema" document :: Maybe String
    value <- BSON.lookup "value" document :: Maybe String
    if schema == "compact-local-v2"
      then Just (OccurrenceRef (Text.pack value))
      else Nothing

instance ToBSON WallIdentity

instance FromBSON WallIdentity

instance ToBSON BuildActivityIdentity

instance FromBSON BuildActivityIdentity

instance ToBSON AttackSegmentIdentity

instance FromBSON AttackSegmentIdentity

instance ToBSON AttackSegmentAttemptIdentity

instance FromBSON AttackSegmentAttemptIdentity

instance ToBSON AbsorbInteractionIdentity

instance FromBSON AbsorbInteractionIdentity

instance ToBSON WallLifecycleOccurrence

instance FromBSON WallLifecycleOccurrence

instance ToBSON BuildActivityOccurrence

instance FromBSON BuildActivityOccurrence

instance ToBSON AttackFormationMaterialOccurrence

instance FromBSON AttackFormationMaterialOccurrence

instance ToBSON AttackSegmentAtWall

instance FromBSON AttackSegmentAtWall

instance ToBSON WallAttackBarrierOccurrence

instance FromBSON WallAttackBarrierOccurrence

instance ToBSON AbsorbInteractionOccurrence

instance FromBSON AbsorbInteractionOccurrence

instance ToBSON DirectedLargeDealOccurrence

instance FromBSON DirectedLargeDealOccurrence

instance ToBSON WallBusinessState

instance FromBSON WallBusinessState

instance ToBSON BuildBusinessState

instance FromBSON BuildBusinessState

instance ToBSON AbsorbBusinessState

instance FromBSON AbsorbBusinessState

instance ToBSON WallCurrentView

instance FromBSON WallCurrentView

instance ToBSON BuildCurrentView

instance FromBSON BuildCurrentView

instance ToBSON AbsorbCurrentView

instance FromBSON AbsorbCurrentView

instance ToBSON P1IngressError

instance FromBSON P1IngressError

instance (Val productError) => ToBSON (P1ProductDiagnostics productError)

instance (Val productError) => FromBSON (P1ProductDiagnostics productError)

instance ToBSON WallLifecycleError

instance FromBSON WallLifecycleError

instance ToBSON BuildActivityError

instance FromBSON BuildActivityError

instance ToBSON AttackSegmentBookError

instance FromBSON AttackSegmentBookError

instance ToBSON AbsorbInteractionError

instance FromBSON AbsorbInteractionError

newtype WallOccurrenceBatch = WallOccurrenceBatch
  { wallOccurrences :: [WallLifecycleOccurrence]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype WallCurrentBatch = WallCurrentBatch
  { wallCurrentViews :: [WallCurrentView]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype WallDiagnostic = WallDiagnostic
  { wallDiagnosticError :: P1ProductDiagnostics WallLifecycleError
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype BuildOccurrenceBatch = BuildOccurrenceBatch
  { buildOccurrences :: [BuildActivityOccurrence]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype BuildCurrentBatch = BuildCurrentBatch
  { buildCurrentViews :: [BuildCurrentView]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype BuildDiagnostic = BuildDiagnostic
  { buildDiagnosticError :: P1ProductDiagnostics BuildActivityError
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype AttackSegmentBatch = AttackSegmentBatch
  { attackSegments :: [AttackSegmentAtWall]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype FormationEvidenceBatch = FormationEvidenceBatch
  { formationEvidenceOccurrences :: [AttackFormationMaterialOccurrence]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype WallBarrierBatch = WallBarrierBatch
  { wallBarrierOccurrences :: [WallAttackBarrierOccurrence]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype AttackDiagnostic = AttackDiagnostic
  { attackDiagnosticError :: P1ProductDiagnostics AttackSegmentBookError
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype AttackCurrentBatch = AttackCurrentBatch
  { publishedAttackSegments :: [AttackSegmentAtWall]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype AbsorbOccurrenceBatch = AbsorbOccurrenceBatch
  { absorbOccurrences :: [AbsorbInteractionOccurrence]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype AbsorbCurrentBatch = AbsorbCurrentBatch
  { absorbCurrentViews :: [AbsorbCurrentView]
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

newtype AbsorbDiagnostic = AbsorbDiagnostic
  { absorbDiagnosticError :: P1ProductDiagnostics AbsorbInteractionError
  }
  deriving (Eq, Show, Generic, ToBSON, FromBSON)

-- current_view 是按业务身份追加的最新状态更新表，不是每次更新都复制截至
-- 当时的全局快照。完整 current Map 仍由各 DSU 的 Dynamic 提供给 FRP 消费者。

dumpWallOutputs :: (Fao owner) => owner -> WallLifecycleOutputs -> FaoModel ()
dumpWallOutputs owner outputs = withEventDump owner $ do
  dumpAdtEvent' "wall_occurrences" (WallOccurrenceBatch <$> wallLifecycleOccurrences outputs)
  dumpAdtEvent' "wall_current_view" (WallCurrentBatch <$> wallLifecycleCurrentUpdates outputs)
  dumpAdtEvent' "wall_diagnostics" (WallDiagnostic <$> wallLifecycleDiagnostics outputs)

dumpBuildOutputs :: (Fao owner) => owner -> BuildActivityOutputs -> FaoModel ()
dumpBuildOutputs owner outputs = withEventDump owner $ do
  dumpAdtEvent' "build_occurrences" (BuildOccurrenceBatch <$> buildActivityOccurrences outputs)
  dumpAdtEvent' "build_current_view" (BuildCurrentBatch <$> buildActivityCurrentUpdates outputs)
  dumpAdtEvent' "build_diagnostics" (BuildDiagnostic <$> buildActivityDiagnostics outputs)

dumpAttackOutputs :: (Fao owner) => owner -> AttackSegmentBookOutputs -> FaoModel ()
dumpAttackOutputs owner outputs = withEventDump owner $ do
  dumpAdtEvent' "attack_segments" (AttackSegmentBatch <$> attackSegmentsAtWall outputs)
  dumpAdtEvent' "formation_evidence" (FormationEvidenceBatch <$> attackFormationMaterials outputs)
  dumpAdtEvent' "wall_attack_barriers" (WallBarrierBatch <$> wallAttackBarriers outputs)
  dumpAdtEvent' "attack_segment_book_current_view" (AttackCurrentBatch <$> attackSegmentsAtWall outputs)
  dumpAdtEvent' "attack_diagnostics" (AttackDiagnostic <$> attackSegmentBookDiagnostics outputs)

dumpAbsorbOutputs :: (Fao owner) => owner -> AbsorbInteractionOutputs -> FaoModel ()
dumpAbsorbOutputs owner outputs = withEventDump owner $ do
  dumpAdtEvent' "absorb_occurrences" (AbsorbOccurrenceBatch <$> absorbInteractionOccurrences outputs)
  dumpAdtEvent' "absorb_current_view" (AbsorbCurrentBatch <$> absorbInteractionCurrentUpdates outputs)
  dumpAdtEvent' "absorb_diagnostics" (AbsorbDiagnostic <$> absorbInteractionDiagnostics outputs)
