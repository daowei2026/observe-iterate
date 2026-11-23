{-# LANGUAGE DeriveAnyClass #-}
{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE OverloadedStrings #-}
-- | 本项薄核心：配置只在首个正常发生保存，候选只保存真实变化。
-- 分类编号是本模块具名sum的固定物理表示，不由文本推断业务。
module Frp.Instance.ISL.Opportunity.U2.GroupCandidateStorage where
import Frp.Instance.ISL.Opportunity.U2.FormationParticipationFacts
import Control.DeepSeq (NFData,rnf)
import Control.Monad (unless)
import Data.Int (Int64)
import Data.Text (Text)
import qualified Data.Set as S
import GHC.Generics (Generic)
import Frp.Apt.Bson (ToBSON,FromBSON)
import Frp.Instance.ISL.Opportunity.U2.Types
import Frp.Instance.ISL.Opportunity.U2.Source (SourceRound(..),finite)
import Frp.Instance.ISL.Opportunity.U2.Formation (FormationProfile(..),FormationDomain(..))
import Frp.Instance.ISL.Opportunity.U2.BoundedRelations
import Frp.Instance.ISL.Opportunity.U2.Episode (CalendarClockValue(..))
import Frp.Instance.ISL.Opportunity.U2.ThinNodeResults (ThinId,ThinReference,ThinDefinition)
import qualified Frp.Instance.ISL.Opportunity.U2.ThinNodeResults as Thin
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes

data GroupClockRecord = GroupClockRecord
  { clockCoordinate :: !Double,clockKnownFrom :: !Int64 }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupPointRecord = GroupPointRecord
  { pointActual :: !Int64,pointPrice :: !Double,pointKnownFrom :: !Int64
  , pointClock :: ![GroupClockRecord] }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupMemberRecord = GroupMemberRecord
  { memberObject :: !Text,memberTurn :: !ThinReference,memberSource :: !ThinReference
  , memberActual :: !Int64,memberPrice :: !Double,memberConfirmation :: !Int64,memberKnownFrom :: !Int64
  , memberDirection :: !Int64,memberType :: !Int64,memberRound :: !Int64
  , memberClock :: ![GroupClockRecord],memberP :: ![GroupPointRecord]
  , memberT :: !GroupPointRecord,memberC :: !GroupPointRecord
  , memberStatus :: !Int64,memberRetracted :: !Int64 }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupRequiredRecord = GroupRequiredRecord
  { requiredVerdict :: !Int64,requiredGap :: !Int64,requiredVeto :: !Int64 }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupDistanceRecord = GroupDistanceRecord {distanceValue :: !Double}
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupPairRecord = GroupPairRecord
  { pairLeft :: !ThinReference,pairRight :: !ThinReference,pairDistance :: ![GroupDistanceRecord]
  , pairTime :: !GroupRequiredRecord,pairDirection :: !GroupRequiredRecord
  , pairType :: !GroupRequiredRecord,pairBend :: !GroupRequiredRecord }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupOccurrenceRecord = GroupOccurrenceRecord
  { groupReference :: !ThinReference,groupPrevious :: ![ThinReference],groupKnownFrom :: !Int64
  , groupOriginalAnchor :: !Double,groupOriginalDeadline :: !Double,groupOriginalRevisionEnd :: !Double
  , groupAnchor :: !Double,groupDeadline :: !Double,groupRevisionEnd :: !Double
  , groupLocalBasis :: !Int64,groupAlternative :: !Int64,groupObservation :: !Int64
  , groupCoverageIncomplete :: !Int64,groupClosed :: !Int64
  , groupMembers :: ![GroupMemberRecord],groupRequired :: ![GroupPairRecord]
  , groupOverlaps :: ![ThinId],groupCoveredBy :: ![ThinId],groupFormationParticipation :: ![FormationParticipation] }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupCompatibilityRecord = GroupCompatibilityRecord
  { compatibilityLeft :: !Int64,compatibilityRight :: !Int64,compatibilityResult :: !Int64 }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupDefinitionRecord = GroupDefinitionRecord
  { definitionMethod :: !ThinDefinition,definitionContext :: !ThinDefinition
  , definitionScale :: !ThinDefinition,definitionCalendar :: !ThinDefinition
  , definitionUniverse :: !ThinDefinition,definitionDomain :: !Text,definitionObjects :: ![Text]
  , definitionDelta :: !Double,definitionTimeUnit :: !Text
  , definitionDirections :: ![GroupCompatibilityRecord],definitionTypes :: ![GroupCompatibilityRecord] }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data GroupCandidatesRecord = GroupCandidatesRecord
  { groupDefinitions :: ![GroupDefinitionRecord],groupOccurrences :: ![GroupOccurrenceRecord] }
  deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
groupCandidatesFormat :: Text
groupCandidatesFormat="common_price_turn_groups.core.v2"

storeGroupOccurrence row =
  let body=candidateBody row;q=candidateQuestion row
  in GroupOccurrenceRecord (Thin.exact (candidateReference row)) (maybe [] (pure . Thin.exact) (candidatePrevious row))
      (candidateKnown row) (questionAnchor q) (questionDeadline q) (questionRevisionEnd q)
      (candidateAnchor body) (candidateDeadline body) (candidateRevisionEnd body)
      (code (candidateBasis body)) (code (candidateAlternatives body)) (code (candidateObservation body))
      (code (candidateDomainIncomplete body)) (code (candidateClosed body))
      (map storeMember (candidateMembers body)) (map storePair (candidatePairs body))
      (map Thin.identifier (candidateOverlaps body)) (map Thin.identifier (candidateCoveredBy body)) (maybe [] pure (candidateParticipation row))
  where
    storeMember (t,status) =
      let g=groupTurnGeometry t
          p=case (geometryP g,geometryPKnown g) of (Just value,Just known)->[storePoint known value];_->[]
      in GroupMemberRecord (groupTurnObject t) (Thin.exact (groupTurnRef t)) (Thin.exact (groupTurnSource t))
        (groupTurnActual t) (groupTurnPrice t) (groupTurnConfirmation t) (groupTurnKnown t)
        (maybe (-1) directionCode (groupTurnDirection t)) (maybe (-1) code (groupTurnType t))
        (code (groupTurnRound t)) (maybe [] (pure . storeClock) (groupTurnClock t)) p
        (storePoint (geometryTKnown g) (geometryT g)) (storePoint (geometryCKnown g) (geometryC g))
        (code status) (code (groupTurnRetracted t))
    storePoint known (actual,price,clock)=GroupPointRecord actual price known
      (maybe [] (\c->[GroupClockRecord (clockValue c) (clockValueKnownFrom c)]) clock)
    storeClock c=GroupClockRecord (groupClockValue c) (groupClockKnown c)
    storePair p=GroupPairRecord (Thin.exact (basisLeft p)) (Thin.exact (basisRight p))
      (maybe [] (pure . GroupDistanceRecord) (basisDistance p))
      (storeCoordinate (basisTime p)) (storeCoordinate (basisDirection p))
      (storeCoordinate (basisType p)) (storeCoordinate (basisBend p))
storeCoordinate CoordinateSupports=GroupRequiredRecord 0 (-1) (-1)
storeCoordinate (CoordinateUnresolved gap)=GroupRequiredRecord 1 (code gap) (-1)
storeCoordinate (CoordinateVeto reason)=GroupRequiredRecord 2 (-1) (code reason)
code :: Enum a => a -> Int64
code=fromIntegral . fromEnum
directionCode DirectionUp=0
directionCode DirectionDown=1

-- 正常存读边界检查有限本产品，不重算Source、pair或完整形成算法。
validateGroupRecord :: GroupCandidatesRecord -> Either Text GroupCandidatesRecord
validateGroupRecord record=do
  unless (length (groupDefinitions record)<=1) (Left "候选定义重复")
  mapM_ occurrence (groupOccurrences record)
  pure record
  where
    occurrence r=do
      unless (length (groupFormationParticipation r)<=1) (Left "原F参与决定重复")
      mapM_ (validateFormationParticipation (groupKnownFrom r)) (groupFormationParticipation r)
      unless (all (\f->null (participationOutsideNotifications f) && participationInputConflict f==0) (groupFormationParticipation r))
        (Left "原F发行不得吸收承接期外通知/消费者冲突")
      let members=groupMembers r;n=length members
      unless (n>=2 && S.size (S.fromList (map memberObject members))==n) (Left "候选成员对象重复或不足")
      unless (length (groupRequired r)==n*(n-1) `div` 2) (Left "候选Required不完整")
      unless (all finite [groupOriginalAnchor r,groupOriginalDeadline r,groupOriginalRevisionEnd r,
        groupAnchor r,groupDeadline r,groupRevisionEnd r] && groupDeadline r<=groupOriginalDeadline r &&
        groupRevisionEnd r<=groupOriginalRevisionEnd r && groupOriginalAnchor r<groupOriginalDeadline r &&
        groupOriginalDeadline r<groupOriginalRevisionEnd r && groupDeadline r<=groupRevisionEnd r)
        (Left "候选期限非法或被延长")
      unless (groupLocalBasis r `elem` [0..2] && groupAlternative r `elem` [0..1] && groupObservation r `elem` [0..5] && groupCoverageIncomplete r `elem` [0,1] && groupClosed r `elem` [0,1])
        (Left "候选F分类未知")
      unless (groupClosed r==0 || groupObservation r/=code Open) (Left "已关闭候选不能重新Open")
      mapM_ (\m->unless (finite (memberPrice m) && memberKnownFrom m<=groupKnownFrom r &&
        memberDirection m `elem` [-1,0,1] && memberType m `elem` [-1,0,1] && memberRound m `elem` [0,1] &&
        memberStatus m `elem` [0,1] && memberRetracted m `elem` [0,1] && length (memberClock m)<=1 && length (memberP m)<=1)
        (Left "候选成员数值／分类／知识非法")) members
      mapM_ (\m->do
        mapM_ (clock (groupKnownFrom r)) (memberClock m)
        mapM_ (point (groupKnownFrom r)) (memberP m++[memberT m,memberC m])) members
      mapM_ (\p->do
        unless (pairLeft p `elem` map memberTurn members && pairRight p `elem` map memberTurn members && pairLeft p/=pairRight p)
          (Left "Required端点未对应成员")
        unless (length (pairDistance p)<=1 && all (\d->finite (distanceValue d) && distanceValue d>=0) (pairDistance p)) (Left "Required距离数值非法")
        mapM_ coordinate [pairTime p,pairDirection p,pairType p,pairBend p]) (groupRequired r)
    clock known c=unless (finite (clockCoordinate c) && clockKnownFrom c<=known)
      (Left "候选Clock非有限或包含未来知识")
    point known p=do
      unless (finite (pointPrice p) && pointKnownFrom p<=known && length (pointClock p)<=1)
        (Left "候选selected点非法或包含未来知识")
      mapM_ (clock known) (pointClock p)
    coordinate c=unless (case requiredVerdict c of
      0->requiredGap c==(-1) && requiredVeto c==(-1)
      1->requiredGap c `elem` [0..7] && requiredVeto c==(-1)
      2->requiredGap c==(-1) && requiredVeto c `elem` [0..4]
      _->False) (Left "Required分支不合法")
forceGroupRecord :: GroupCandidatesRecord -> ()
forceGroupRecord=rnf
