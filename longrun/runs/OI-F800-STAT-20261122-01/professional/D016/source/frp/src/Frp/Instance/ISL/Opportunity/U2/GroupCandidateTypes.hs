{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE NoOverloadedLists #-}
-- | 共同价格转折候选的业务值。局部依据、备选关系、观察结果分别表达；
-- 不承接后段成立判断、方向组织、组外分离或机会簇职责。
module Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes where
import Frp.Instance.ISL.Opportunity.U2.FormationParticipationFacts (FormationParticipation)
import Data.Int (Int64)
import Data.Map.Strict (Map)
import Data.Set (Set)
import Data.Text (Text)
import GHC.Generics (Generic)
import Frp.Instance.ISL.Opportunity.U2.Types
import Frp.Instance.ISL.Opportunity.U2.Source (SourceRound)
import Frp.Instance.ISL.Opportunity.U2.BoundedRelations (SelectedGeometry)

-- | 一个实际对象内、原Source拥有的Turn生命，不以坐标重建身份。
type TurnKey = (Text,Text)
type PairKey = (TurnKey,TurnKey)
data GroupMethod = CompleteLinkPriceTurns
  { groupDelta :: !Double, groupTimeUnit :: !Text, groupObservationMultiple :: !Double }
  deriving (Eq,Show,Generic)

-- | First-confirmation observation duty is independent of pair proximity.
-- Revision tail and unknown-clock waiting retain their existing six-Delta rules.
groupObservationDuration :: GroupMethod -> Double
groupObservationDuration method=groupObservationMultiple method*groupDelta method

data GroupTurn = GroupTurn
  { groupTurnRef :: !ExactRef, groupTurnSource :: !ExactRef
  , groupTurnObject :: !Text, groupTurnActual :: !Int64, groupTurnPrice :: !Double
  , groupTurnConfirmation :: !Int64, groupTurnKnown :: !Int64
  , groupTurnDirection :: !(Maybe TurnDirection), groupTurnType :: !(Maybe SourceTurnType)
  , groupTurnRound :: !SourceRound, groupTurnGeometry :: !SelectedGeometry
  , groupTurnClock :: !(Maybe FormationClock)
  , groupTurnRetracted :: !Bool
  , groupTurnOriginOrder :: !(Maybe ProvenOriginOrder) }
  deriving (Eq,Show)
-- Clock值与可知时点一同保留；无值的明确修订由Material输入表达。
data FormationClock = FormationClock
  { groupClockValue :: !Double, groupClockKnown :: !Int64 }
  deriving (Eq,Show,Generic)
turnKey :: GroupTurn -> TurnKey
turnKey t=(groupTurnObject t,refLife (groupTurnRef t))
pairKey :: TurnKey -> TurnKey -> PairKey
pairKey a b=if a<b then (a,b) else (b,a)
data RequiredGap = ActualClockUnavailable | DirectionUnavailable | TurnTypeUnavailable
  | SelectedAnchorUnavailable | SelectedClockUnavailable | SelectedKnowledgeUnavailable
  | SelectedCollinear | SelectedLegInvalid
  deriving (Eq,Ord,Show,Enum,Bounded,Generic)
data RequiredVeto = ActualDistanceExceeded | DirectionOpposed | TurnTypeOpposed
  | SelectedBendOpposed | SourceTurnWithdrawn
  deriving (Eq,Ord,Show,Enum,Bounded,Generic)
data RequiredCoordinate = CoordinateSupports | CoordinateUnresolved !RequiredGap
  | CoordinateVeto !RequiredVeto deriving (Eq,Ord,Show,Generic)
data PairBasis = PairBasis
  { basisLeft :: !ExactRef, basisRight :: !ExactRef
  , basisDistance :: !(Maybe Double)
  , basisTime :: !RequiredCoordinate, basisDirection :: !RequiredCoordinate
  , basisType :: !RequiredCoordinate, basisBend :: !RequiredCoordinate }
  deriving (Eq,Show)
data PairDecision = PairPositive | PairUnresolved | PairVeto deriving (Eq,Ord,Show)
data LocalBasis = Supported | Incomplete | Contradicted deriving (Eq,Ord,Show,Enum,Bounded,Generic)
data AlternativeResolution = Unambiguous | UnresolvedOverlap deriving (Eq,Ord,Show,Enum,Bounded,Generic)
data ObservationState = Open | ClosedSupported | ClosedInsufficient | Withdrawn
  | Subsumed | EndedByScope deriving (Eq,Ord,Show,Enum,Bounded,Generic)
data MemberStatus = ConfirmedMember | CandidateMember deriving (Eq,Ord,Show,Enum,Bounded,Generic)
-- | 原观察问题不因后来知识到达而续期。当前期限只能收紧。
data FormationQuestion = FormationQuestion
  { questionAnchor :: !Double, questionDeadline :: !Double, questionRevisionEnd :: !Double }
  deriving (Eq,Ord,Show)
type CandidateKey = (FormationQuestion,[TurnKey])
data CandidateBody = CandidateBody
  { candidateMembers :: ![(GroupTurn,MemberStatus)]
  , candidatePairs :: ![PairBasis]
  , candidateBasis :: !LocalBasis, candidateAlternatives :: !AlternativeResolution
  , candidateObservation :: !ObservationState, candidateDomainIncomplete :: !Bool
  , candidateAnchor :: !Double, candidateDeadline :: !Double, candidateRevisionEnd :: !Double
  , candidateClosed :: !Bool
  , candidateOverlaps :: ![Text], candidateCoveredBy :: ![Text] }
  deriving (Eq,Show)
data CandidateOccurrence = CandidateOccurrence
  { candidateReference :: !ExactRef, candidatePrevious :: !(Maybe ExactRef)
  , candidateQuestion :: !FormationQuestion, candidateKnown :: !Int64
  , candidateBody :: !CandidateBody, candidateParticipation :: !(Maybe FormationParticipation) }
  deriving (Eq,Show)
-- | 当前对象最近一段输入的覆盖，不发行身份，不保存逐报价历史。
-- Observed允许没有Turn；不适用只能由明确的业务事实输入。
data CoverageCondition = CoverageColdStart | CoverageObserved | CoverageInputMissing
  | CoverageClockUnknown | CoverageSourceFailure | CoverageInapplicable
  deriving (Eq,Show)
data ObjectCoverage = ObjectCoverage
  { coverageObject :: !Text, coverageCondition :: !CoverageCondition
  , coverageFrom :: !(Maybe Double), coverageThrough :: !(Maybe Double) }
  deriving (Eq,Show)
-- | 私有材料过程向pair过程交付当前合法小值；不带Source owner或旧状态。
data FormationMaterial = FormationMaterial
  { materialTurns :: !(Map TurnKey GroupTurn), materialEnumerable :: !(Set TurnKey)
  , materialProgress :: !Double, materialKnown :: !Int64
  , materialChanged :: !(Set TurnKey), materialScopeEnded :: !Bool
  , materialCoverageIncomplete :: !Bool }
  deriving (Eq,Show)
data PairView = PairView
  { pairMaterial :: !FormationMaterial, pairBases :: !(Map PairKey PairBasis) }
  deriving (Eq,Show)
