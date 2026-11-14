{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE OverloadedStrings #-}

-- | EAW P1 v1.6.1 产品特定身份、薄 receipt、occurrence 与 current view。
--
-- 本模块不定义 P1 总产品、跨运行 stable identity、revision/source-correction
-- 或 publication trace。FeatureRunIdentity 只属于一次 Fao/receipt 运行上下文；
-- occurrence 与 DSU 内只保存 producer 给出的无损局部编号。
module Frp.Instance.ISL.Eaw.P1.Products
  ( SourceScope (..),
    DirectUpstreamArtifact (..),
    ProductReceipt (..),
    FeatureRunIdentity (..),
    featureRunIdentityFromFaoContext,
    validateReceiptKind,
    exactUpstreamArtifacts,
    receiptBusinessParameterText,
    AttackFormationMethodSnapshot (..),
    attackFormationMethodSnapshotFromReceipt,
    F4QualificationHit (..),
    AttackSegmentAvailability (..),
    FormationEvidenceKind (..),
    FormationEvidenceAvailability (..),
    AbsorbOccurrenceKind (..),
    P1IngressError (..),
    P1ProductDiagnostics (..),
    mergeP1ProductDiagnostics,
    OccurrenceRef (..),
    WallIdentity (..),
    BuildActivityIdentity (..),
    AttackSegmentIdentity (..),
    AttackSegmentAttemptIdentity (..),
    AbsorbInteractionIdentity (..),
    wallRefOf,
    buildRefOf,
    attackSegmentRefOf,
    attackSegmentAttemptRefOf,
    absorbRefOf,
    WallLifecycleOccurrence (..),
    BuildActivityOccurrence (..),
    AttackFormationMaterialOccurrence (..),
    AttackSegmentAtWall (..),
    WallAttackBarrierOccurrence (..),
    AbsorbInteractionOccurrence (..),
    DirectedLargeDealOccurrence (..),
    WallIdentityCatalog (..),
    emptyWallIdentityCatalog,
    containsWallIdentity,
    WallBusinessState (..),
    BuildBusinessState (..),
    AbsorbBusinessState (..),
    WallCurrentView (..),
    BuildCurrentView (..),
    AttackSegmentBookCurrentView,
    emptyAttackSegmentBookCurrentView,
    attackCurrentSegments,
    recordFormedAttackSegment,
    AbsorbCurrentView (..),
  )
where

import Data.Aeson
import Data.Aeson.Key qualified as Key
import Data.Aeson.KeyMap qualified as KeyMap
import Data.ByteString.Lazy qualified as BL
import Data.Int (Int64)
import Data.Map.Strict (Map)
import Data.Map.Strict qualified as Map
import Data.Set (Set)
import Data.Set qualified as Set
import Data.Text (Text)
import Data.Text qualified as Text
import Data.Text.Encoding qualified as TextEncoding
import Frp.Instance.ISL.Eaw.Interface.Common
import Frp.Instance.ISL.Eaw.Interface.PreL0 qualified as Spine
import GHC.Generics (Generic)

data SourceScope = SourceScope
  { sourceTarget :: Text,
    sourceCalendarOrSession :: Text,
    sourceTimeRange :: Text,
    sourceMarketCut :: Text
  }
  deriving (Eq, Ord, Show, Generic)

instance FromJSON SourceScope where
  parseJSON = withObject "SourceScope" $ \o ->
    SourceScope
      <$> o .: "target"
      <*> o .: "calendar_or_session"
      <*> o .: "time_range"
      <*> o .: "market_source_cut"

instance ToJSON SourceScope where
  toJSON value =
    object
      [ "target" .= sourceTarget value,
        "calendar_or_session" .= sourceCalendarOrSession value,
        "time_range" .= sourceTimeRange value,
        "market_source_cut" .= sourceMarketCut value
      ]

data DirectUpstreamArtifact = DirectUpstreamArtifact
  { upstreamProductKind :: Text,
    upstreamFeatureInstance :: Text,
    upstreamParameterSetId :: Text,
    upstreamArtifactLocation :: Text,
    upstreamSchemaVersion :: Text,
    upstreamCodeVersion :: Text
  }
  deriving (Eq, Ord, Show, Generic)

instance FromJSON DirectUpstreamArtifact where
  parseJSON = withObject "DirectUpstreamArtifact" $ \o ->
    DirectUpstreamArtifact
      <$> o .: "product_kind"
      <*> o .: "feature_instance"
      <*> o .: "parameter_set_id"
      <*> o .: "artifact_location"
      <*> o .: "schema_version"
      <*> o .: "code_version"

instance ToJSON DirectUpstreamArtifact where
  toJSON value =
    object
      [ "product_kind" .= upstreamProductKind value,
        "feature_instance" .= upstreamFeatureInstance value,
        "parameter_set_id" .= upstreamParameterSetId value,
        "artifact_location" .= upstreamArtifactLocation value,
        "schema_version" .= upstreamSchemaVersion value,
        "code_version" .= upstreamCodeVersion value
      ]

data ProductReceipt = ProductReceipt
  { receiptProductKind :: Text,
    receiptFeatureInstance :: Text,
    receiptParameterSetId :: Text,
    receiptSourceScope :: SourceScope,
    receiptActualBusinessParameters :: Value,
    receiptProducerPrivateParameters :: Value,
    receiptDirectUpstreamArtifacts :: [DirectUpstreamArtifact],
    receiptMethodSnapshotFingerprint :: Maybe Text,
    receiptSchemaVersion :: Text,
    receiptCodeVersion :: Text,
    receiptArtifactLocation :: Text,
    receiptStatus :: Text,
    receiptError :: Maybe Text
  }
  deriving (Eq, Show, Generic)

instance FromJSON ProductReceipt where
  parseJSON = withObject "ProductReceipt" $ \o ->
    ProductReceipt
      <$> o .: "product_kind"
      <*> o .: "feature_instance"
      <*> o .: "parameter_set_id"
      <*> o .: "source_scope"
      <*> o .: "actual_business_parameters"
      <*> o .:? "producer_private_parameters" .!= object []
      <*> o .: "direct_upstream_artifacts"
      <*> o .:? "method_snapshot_fingerprint"
      <*> o .: "schema_version"
      <*> o .: "code_version"
      <*> o .: "artifact_location"
      <*> o .: "status"
      <*> o .:? "error"

instance ToJSON ProductReceipt where
  toJSON value =
    object
      [ "product_kind" .= receiptProductKind value,
        "feature_instance" .= receiptFeatureInstance value,
        "parameter_set_id" .= receiptParameterSetId value,
        "source_scope" .= receiptSourceScope value,
        "actual_business_parameters" .= receiptActualBusinessParameters value,
        "producer_private_parameters" .= receiptProducerPrivateParameters value,
        "direct_upstream_artifacts" .= receiptDirectUpstreamArtifacts value,
        "method_snapshot_fingerprint" .= receiptMethodSnapshotFingerprint value,
        "schema_version" .= receiptSchemaVersion value,
        "code_version" .= receiptCodeVersion value,
        "artifact_location" .= receiptArtifactLocation value,
        "status" .= receiptStatus value,
        "error" .= receiptError value
      ]

data FeatureRunIdentity = FeatureRunIdentity
  { featureClassName :: Text,
    parameterSetId :: Text,
    targetRef :: Text,
    calendarRef :: Text,
    timeRangeRef :: Text,
    sourceScopeRef :: Text,
    artifactRef :: Text,
    schemaVersion :: Text,
    codeVersion :: Text
  }
  deriving (Eq, Ord, Show, Generic)

instance ToJSON FeatureRunIdentity where
  toJSON value =
    object
      [ "feature_symbol" .= featureClassName value,
        "parameter_set_id" .= parameterSetId value,
        "target" .= targetRef value,
        "calendar_or_session" .= calendarRef value,
        "time_range" .= timeRangeRef value,
        "input_source_scope" .= sourceScopeRef value,
        "artifact_location" .= artifactRef value,
        "schema_version" .= schemaVersion value,
        "code_version" .= codeVersion value
      ]

instance FromJSON FeatureRunIdentity where
  parseJSON = withObject "FeatureRunIdentity" $ \o ->
    FeatureRunIdentity
      <$> o .: "feature_symbol"
      <*> o .: "parameter_set_id"
      <*> o .: "target"
      <*> o .: "calendar_or_session"
      <*> o .: "time_range"
      <*> o .: "input_source_scope"
      <*> o .: "artifact_location"
      <*> o .: "schema_version"
      <*> o .: "code_version"

sourceScopeText :: SourceScope -> Text
sourceScopeText = TextEncoding.decodeUtf8 . BL.toStrict . encode

featureRunIdentityFromFaoContext :: ProductReceipt -> FeatureRunIdentity
featureRunIdentityFromFaoContext receipt =
  let scope = receiptSourceScope receipt
   in FeatureRunIdentity
        { featureClassName = receiptFeatureInstance receipt,
          parameterSetId = receiptParameterSetId receipt,
          targetRef = sourceTarget scope,
          calendarRef = sourceCalendarOrSession scope,
          timeRangeRef = sourceTimeRange scope,
          sourceScopeRef = sourceScopeText scope,
          artifactRef = receiptArtifactLocation receipt,
          schemaVersion = receiptSchemaVersion receipt,
          codeVersion = receiptCodeVersion receipt
        }

knownProductKinds :: Set Text
knownProductKinds =
  Set.fromList
    [ "wall_lifecycle",
      "directed_large_deal_stream",
      "build_activity",
      "attack_segment",
      "attack_formation_evidence",
      "wall_relation_barrier",
      "absorb_interaction"
    ]

expectedUpstreamKinds :: Text -> Set Text
expectedUpstreamKinds "wall_lifecycle" = Set.empty
expectedUpstreamKinds "directed_large_deal_stream" = Set.empty
-- F3 主动流是在 Build 的有界交易日分块内即时计算、即时消费的内部量，
-- 不形成持久产品，也不是 Build receipt 的 direct upstream artifact。
expectedUpstreamKinds "build_activity" = Set.singleton "wall_lifecycle"
expectedUpstreamKinds "attack_segment" = Set.fromList ["wall_lifecycle", "directed_large_deal_stream"]
expectedUpstreamKinds "attack_formation_evidence" = Set.fromList ["wall_lifecycle", "directed_large_deal_stream"]
expectedUpstreamKinds "wall_relation_barrier" = Set.singleton "wall_lifecycle"
expectedUpstreamKinds "absorb_interaction" = Set.singleton "wall_lifecycle"
expectedUpstreamKinds _ = Set.singleton "unknown"

validateReceiptKind :: Text -> ProductReceipt -> Either Text ProductReceipt
validateReceiptKind expected receipt
  | expected `Set.notMember` knownProductKinds = Left "unknown P1 product kind"
  | receiptProductKind receipt /= expected = Left "P1 thin receipt product kind mismatch"
  | receiptSchemaVersion receipt /= expectedSchemaVersion expected = Left "P1 thin receipt schema version mismatch"
  | receiptStatus receipt /= "success" = Left "P1 thin receipt is not successful"
  | any Text.null requiredText = Left "P1 thin receipt contains an empty required field"
  | actualKinds /= expectedUpstreamKinds expected = Left "P1 thin receipt direct upstream products mismatch"
  | (expected == "attack_segment" || expected == "attack_formation_evidence")
      && null [() | item <- receiptDirectUpstreamArtifacts receipt, upstreamProductKind item == "directed_large_deal_stream"] =
      Left "Attack product must name at least one selected F4 artifact"
  | otherwise = Right receipt
  where
    scope = receiptSourceScope receipt
    requiredText :: [Text]
    requiredText =
      [ receiptFeatureInstance receipt,
        receiptParameterSetId receipt,
        sourceTarget scope,
        sourceCalendarOrSession scope,
        sourceTimeRange scope,
        sourceMarketCut scope,
        receiptSchemaVersion receipt,
        receiptCodeVersion receipt,
        receiptArtifactLocation receipt
      ]
    actualKinds = Set.fromList (fmap upstreamProductKind (receiptDirectUpstreamArtifacts receipt))

expectedSchemaVersion :: Text -> Text
expectedSchemaVersion "attack_segment" = "attack_segment-v1.6.2"
expectedSchemaVersion "attack_formation_evidence" = "attack_formation_evidence-v1.6.2"
expectedSchemaVersion productKind = productKind <> "-v1.6.1"

exactUpstreamArtifacts :: Text -> ProductReceipt -> [DirectUpstreamArtifact]
exactUpstreamArtifacts kind = filter ((== kind) . upstreamProductKind) . receiptDirectUpstreamArtifacts

data AttackFormationMethodSnapshot = AttackFormationMethodSnapshot
  { eligibleWallDistanceTicks :: Int,
    segmentContinuationGapTicks :: Int,
    selectedF4Streams :: [FeatureRunIdentity],
    qualificationParameterSets :: [Text],
    laneMergePolicy :: Text,
    methodSnapshotFingerprint :: Text
  }
  deriving (Eq, Ord, Show, Generic)

lookupObject :: Text -> Value -> Maybe Value
lookupObject key (Object values) = KeyMap.lookup (Key.fromText key) values
lookupObject _ _ = Nothing

valueText :: Text -> Value -> Maybe Text
valueText key value = case lookupObject key value of
  Just (String item) -> Just item
  _ -> Nothing

valueInt :: Text -> Value -> Maybe Int
valueInt key value = case lookupObject key value of
  Just (Number item) -> Just (round item)
  _ -> Nothing

receiptBusinessParameterText :: Text -> ProductReceipt -> Maybe Text
receiptBusinessParameterText key = valueText key . receiptActualBusinessParameters

selectedIdentity :: Value -> Maybe FeatureRunIdentity
selectedIdentity value = do
  feature <- valueText "feature_instance" value
  parameter <- valueText "parameter_set_id" value
  artifact <- valueText "artifact_location" value
  schema <- valueText "schema_version" value
  code <- valueText "code_version" value
  scopeValue <- lookupObject "source_scope" value
  scope <- case fromJSON scopeValue of Success parsed -> Just parsed; Error _ -> Nothing
  pure (featureRunIdentityFromFaoContext (ProductReceipt "directed_large_deal_stream" feature parameter scope (object []) (object []) [] Nothing schema code artifact "success" Nothing))

attackFormationMethodSnapshotFromReceipt :: ProductReceipt -> Either Text AttackFormationMethodSnapshot
attackFormationMethodSnapshotFromReceipt receipt = do
  distance <- maybe (Left "Attack receipt misses eligible_wall_distance_ticks") Right (valueInt "p_attack_ticks" params)
  gap <- maybe (Left "Attack receipt misses segment_continuation_gap_ticks") Right (valueInt "t_gap_attack_ticks" params)
  selected <- case lookupObject "selected_f4_streams" params of
    Just (Array values) -> traverse (maybe (Left "Attack selected F4 identity is incomplete") Right . selectedIdentity) (foldr (:) [] values)
    _ -> Left "Attack receipt misses selected_f4_streams"
  producerLanePolicy <- maybe (Left "Attack receipt misses lane_merge_policy") Right (valueText "lane_merge_policy" params)
  lanePolicy <-
    if producerLanePolicy == "union_keep_labels"
      then Right "attack-segment-local-union-keep-labels"
      else Left "Attack receipt lane_merge_policy is not the frozen local union policy"
  fingerprintValue <- maybe (Left "Attack receipt misses method_snapshot_fingerprint") Right (receiptMethodSnapshotFingerprint receipt)
  if null selected
    then Left "Attack receipt selected_f4_streams is empty"
    else
      Right
        ( AttackFormationMethodSnapshot
            distance
            gap
            selected
            (fmap parameterSetId selected)
            lanePolicy
            fingerprintValue
        )
  where
    params = receiptActualBusinessParameters receipt

data F4QualificationHit = F4QualificationHit
  { qualificationStreamOrdinal :: Int,
    qualificationFamilyCode :: Int,
    qualificationFamily :: Text,
    qualificationGrade :: Int
  }
  deriving (Eq, Ord, Show, Generic)

-- | 完整 AttackSegment 的公开可用性；technical close 不能伪装成正常闭段。
data AttackSegmentAvailability
  = AttackSegmentAvailable
  | AttackSegmentTechnicalTruncated
  | AttackSegmentUnavailable
  deriving (Eq, Ord, Show, Enum, Bounded, Generic)

-- | P2 字段合同冻结的 FormationEvidence 角色。它只标注 producer 已给出的
-- 同一行材料，不在 Haskell 重新形成段或 Continuity cut。
data FormationEvidenceKind
  = AcceptedMaterialEvidence
  | OrdinaryGapBreakEvidence
  | SameUtiOrderUnresolvedEvidence
  | ObservedNoAcceptedAttackIntervalEvidence
  | AvailabilityIntervalSummaryEvidence
  | CapabilityUnavailableEvidence
  deriving (Eq, Ord, Show, Enum, Bounded, Generic)

data FormationEvidenceAvailability
  = FormationEvidenceAvailable
  | FormationEvidenceMissing
  | FormationEvidenceStale
  | FormationEvidenceSessionInvalid
  | FormationEvidenceUnavailable
  deriving (Eq, Ord, Show, Enum, Bounded, Generic)

data AbsorbOccurrenceKind
  = AbsorbStartedOccurrence
  | AbsorbConsumptionMilestoneOccurrence
  | AbsorbResolvedOccurrence
  deriving (Eq, Ord, Show, Enum, Bounded, Generic)

data P1IngressError
  = MissingNumericField Text
  | NonFiniteNumericField Text Double
  | NonIntegralNumericField Text Double
  | InvalidResultKey Text
  | UnknownNumericCode Text Int
  | InvalidNumericDomain Text Text
  | QualifiedUtiCountMismatch Int Int
  | MissingExactUpstream Text
  | ExactUpstreamMismatch Text
  | MissingAttackMethodSnapshot
  | AttackProductReceiptMismatch Text
  | MissingWallLocalNo Int64
  | ReceiptSourceScopeMismatch Text
  deriving (Eq, Ord, Show, Generic)

-- | 一次产品 transaction 的正式 diagnostic envelope。Ingress 错误和
-- 产品 DSU 状态错误可以在同一拍同时出现，因而都保留且不互相覆盖。
data P1ProductDiagnostics productError = P1ProductDiagnostics
  { p1IngressDiagnostics :: [P1IngressError],
    p1StateDiagnostics :: [productError]
  }
  deriving (Eq, Ord, Show, Generic)

mergeP1ProductDiagnostics :: [P1ProductDiagnostics productError] -> P1ProductDiagnostics productError
mergeP1ProductDiagnostics values =
  P1ProductDiagnostics
    (concatMap p1IngressDiagnostics values)
    (concatMap p1StateDiagnostics values)

newtype OccurrenceRef = OccurrenceRef {unOccurrenceRef :: Text}
  deriving (Eq, Ord, Show, Generic)

newtype WallIdentity = WallIdentity
  { wallIdentityLocalNo :: Int64
  }
  deriving (Eq, Ord, Show, Generic)

newtype BuildActivityIdentity = BuildActivityIdentity
  { buildIdentityLocalNo :: Int64
  }
  deriving (Eq, Ord, Show, Generic)

newtype AttackSegmentIdentity = AttackSegmentIdentity
  { attackIdentityLocalNo :: Int64
  }
  deriving (Eq, Ord, Show, Generic)

newtype AttackSegmentAttemptIdentity = AttackSegmentAttemptIdentity
  { attackAttemptLocalNo :: Int64
  }
  deriving (Eq, Ord, Show, Generic)

newtype AbsorbInteractionIdentity = AbsorbInteractionIdentity
  { absorbIdentityLocalNo :: Int64
  }
  deriving (Eq, Ord, Show, Generic)

localText :: Int64 -> Text
localText = Text.pack . show

wallRefOf :: WallIdentity -> WallRef
wallRefOf (WallIdentity localNo) = WallRef ("wall:" <> localText localNo)

buildRefOf :: BuildActivityIdentity -> BuildRef
buildRefOf (BuildActivityIdentity localNo) = BuildRef ("build:" <> localText localNo)

attackSegmentRefOf :: AttackSegmentIdentity -> AttackSegmentRef
attackSegmentRefOf (AttackSegmentIdentity localNo) = AttackSegmentRef ("attack-segment:" <> localText localNo)

attackSegmentAttemptRefOf :: AttackSegmentAttemptIdentity -> AttackSegmentAttemptRef
attackSegmentAttemptRefOf (AttackSegmentAttemptIdentity localNo) = AttackSegmentAttemptRef ("attack-segment-attempt:" <> localText localNo)

absorbRefOf :: AbsorbInteractionIdentity -> AbsorbRef
absorbRefOf (AbsorbInteractionIdentity localNo) = AbsorbRef ("absorb:" <> localText localNo)

data WallLifecycleOccurrence = WallLifecycleOccurrence
  { wallOccurrenceIdentity :: WallIdentity,
    wallOccurrenceRef :: OccurrenceRef,
    wallOccurrencePayload :: Spine.WallLifecycleEvent
  }
  deriving (Eq, Ord, Show, Generic)

data BuildActivityOccurrence = BuildActivityOccurrence
  { buildOccurrenceIdentity :: BuildActivityIdentity,
    buildOccurrenceWallIdentity :: WallIdentity,
    buildOccurrenceRef :: OccurrenceRef,
    buildOccurrencePayload :: Spine.BuildActivityEvent
  }
  deriving (Eq, Ord, Show, Generic)

data AttackFormationMaterialOccurrence = AttackFormationMaterialOccurrence
  { formationOccurrenceWallIdentity :: WallIdentity,
    formationOccurrenceRef :: OccurrenceRef,
    formationOccurrenceAttemptRef :: Maybe AttackSegmentAttemptRef,
    formationOccurrenceKind :: FormationEvidenceKind,
    formationOccurrenceStartUti :: TickUTI,
    formationOccurrenceEndUti :: TickUTI,
    formationOccurrenceAvailableAt :: TickUTI,
    formationOccurrenceAvailability :: FormationEvidenceAvailability,
    formationOccurrenceReason :: Maybe Text,
    formationOccurrencePayload :: Spine.AttackFormationMaterial
  }
  deriving (Eq, Ord, Show, Generic)

data AttackSegmentAtWall = AttackSegmentAtWall
  { attackOccurrenceIdentity :: AttackSegmentIdentity,
    attackOccurrenceWallIdentity :: WallIdentity,
    attackOccurrenceRef :: OccurrenceRef,
    attackOccurrenceQualificationHits :: [F4QualificationHit],
    attackOccurrenceAvailability :: AttackSegmentAvailability,
    attackOccurrenceUnavailableReason :: Maybe Text,
    attackOccurrencePayload :: Spine.AttackSegmentAtWall
  }
  deriving (Eq, Ord, Show, Generic)

data WallAttackBarrierOccurrence = WallAttackBarrierOccurrence
  { barrierOccurrenceWallIdentity :: WallIdentity,
    barrierOccurrenceRef :: OccurrenceRef,
    barrierOccurrencePayload :: Spine.WallAttackBarrier
  }
  deriving (Eq, Ord, Show, Generic)

data AbsorbInteractionOccurrence = AbsorbInteractionOccurrence
  { absorbOccurrenceIdentity :: AbsorbInteractionIdentity,
    absorbOccurrenceWallIdentity :: WallIdentity,
    absorbOccurrenceRef :: OccurrenceRef,
    absorbOccurrenceKind :: AbsorbOccurrenceKind,
    absorbOccurrenceMilestoneLevel :: Maybe Double,
    absorbOccurrenceResolvedReason :: Maybe Text,
    absorbOccurrencePayload :: Spine.AbsorbInteractionEvent
  }
  deriving (Eq, Ord, Show, Generic)

data DirectedLargeDealOccurrence = DirectedLargeDealOccurrence
  { largeDealOccurrenceLocalNo :: Int64,
    largeDealOccurrenceRef :: OccurrenceRef,
    largeDealQualificationFamily :: Text,
    largeDealQualificationGrade :: Int,
    largeDealOccurrencePayload :: Spine.DirectedLargeDealEvent
  }
  deriving (Eq, Ord, Show, Generic)

-- | exact upstream receipt 在流级别冻结 producer run；逐 occurrence 的业务
-- 身份只保留 run 内 local wall_id。旧 fixture 可精确枚举，正式紧凑流只记录
-- receipt 已验证，不再把运行身份复制进每条 occurrence，也不重读整段 Wall 历史。
data WallIdentityCatalog = WallIdentityCatalog
  { wallIdentityNamespaceValidated :: Bool,
    wallIdentities :: Set WallIdentity
  }
  deriving (Eq, Ord, Show, Generic)

emptyWallIdentityCatalog :: WallIdentityCatalog
emptyWallIdentityCatalog = WallIdentityCatalog False Set.empty

containsWallIdentity :: WallIdentity -> WallIdentityCatalog -> Bool
containsWallIdentity identity catalog =
  Set.member identity (wallIdentities catalog)
    || (wallIdentityNamespaceValidated catalog && wallIdentityLocalNo identity > 0)

data WallBusinessState = WallPresent | WallDormantState | WallEndedState deriving (Eq, Ord, Show, Generic)

data BuildBusinessState = BuildInProgress | BuildStoppedState deriving (Eq, Ord, Show, Generic)

data AbsorbBusinessState = AbsorbInProgress | AbsorbResolvedState deriving (Eq, Ord, Show, Generic)

data WallCurrentView = WallCurrentView
  { wallCurrentIdentity :: WallIdentity,
    wallCurrentState :: WallBusinessState,
    wallCurrentOccurrence :: WallLifecycleOccurrence
  }
  deriving (Eq, Ord, Show, Generic)

data BuildCurrentView = BuildCurrentView
  { buildCurrentIdentity :: BuildActivityIdentity,
    buildCurrentWallIdentity :: WallIdentity,
    buildCurrentState :: BuildBusinessState,
    buildCurrentMilestoneCount :: Int,
    buildCurrentOccurrence :: BuildActivityOccurrence
  }
  deriving (Eq, Ord, Show, Generic)

-- | 贴墙攻势段簿的当前业务投影。
--
-- 已形成段按业务身份寻址。FormationEvidence 与 formal Barrier 由各自的
-- append-only occurrence writer 保存，不复制进 current view。
newtype AttackSegmentBookCurrentView = AttackSegmentBookCurrentView
  { attackCurrentSegmentIndex :: Map AttackSegmentIdentity AttackSegmentAtWall
  }
  deriving (Eq, Ord, Show, Generic)

-- | 空的贴墙攻势段簿当前投影。
emptyAttackSegmentBookCurrentView :: AttackSegmentBookCurrentView
emptyAttackSegmentBookCurrentView = AttackSegmentBookCurrentView Map.empty

-- | 返回全部已形成段；Map key 是正式 AttackSegment 业务身份。
attackCurrentSegments :: AttackSegmentBookCurrentView -> Map AttackSegmentIdentity AttackSegmentAtWall
attackCurrentSegments = attackCurrentSegmentIndex

-- | 把一个 producer 已完整形成的 AttackSegment 登记进段簿当前投影。
recordFormedAttackSegment :: AttackSegmentAtWall -> AttackSegmentBookCurrentView -> AttackSegmentBookCurrentView
recordFormedAttackSegment segment current =
  current
    { attackCurrentSegmentIndex =
        Map.insert (attackOccurrenceIdentity segment) segment (attackCurrentSegmentIndex current)
    }

data AbsorbCurrentView = AbsorbCurrentView
  { absorbCurrentIdentity :: AbsorbInteractionIdentity,
    absorbCurrentWallIdentity :: WallIdentity,
    absorbCurrentState :: AbsorbBusinessState,
    absorbCurrentMilestoneCount :: Int,
    absorbCurrentOccurrence :: AbsorbInteractionOccurrence
  }
  deriving (Eq, Ord, Show, Generic)
