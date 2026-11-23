{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE OverloadedStrings #-}
-- | 有限形成材料的唯一owner：新枚举域与已发行候选修正依赖分别保留。
-- 输入只包含生产者本次成功接受的小值，不接受来源失败的半份材料。
module Frp.Instance.ISL.Opportunity.U2.GroupCandidateMaterial where
import Control.Monad (foldM,unless)
import Data.Int (Int64)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import Data.Text (Text)
import Frp.Instance.ISL.Opportunity.U2.Types (ExactRef)
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes
import Frp.Instance.ISL.Opportunity.U2.Source (finite,ChildOrigin)
import Frp.Instance.ISL.Opportunity.U2.BoundedRelations
import Frp.Instance.ISL.Opportunity.U2.Episode (CalendarClockValue(..))

-- | 明确Clock修订与未携带可选字段不同。Nothing只在成功修订输入中表示失知。
-- | Source拥有的当前未决原材料，不把已选锚点当未决候选。
data SourceDisposition=RawUndecided | RawConfirmed | RawExcluded | RawSupersededBeforeAdmission | RawAdmitted
  deriving (Eq,Ord,Show,Enum,Bounded)
data SourcePending=SourcePending
  { pendingOrigin :: !(Maybe ExactRef),pendingAdmission :: !(Maybe ExactRef)
  , pendingActual :: !Int64,pendingKnown :: !Int64,pendingClock :: !(Maybe FormationClock)
  , pendingDisposition :: !SourceDisposition }
  deriving (Eq,Show)
data SourceFrontier=SourceFrontier
  { frontierObject :: !Text,frontierActual :: !Int64,frontierPrepared :: !Bool,frontierKnown :: !Int64
  , frontierPending :: ![SourcePending],frontierExcluded :: ![SourcePending] }
  deriving (Eq,Show)
data FormationPatch = SourceStartAttempt !Text !ExactRef ![Int64] !Bool !Int64
  -- 原确认转换的真实目标；与Start尝试分别表达，只限制相交Turn。
  | SourceConfirmationAttempt !Text !ExactRef !Bool !Int64
  | AcceptedClock !Text !Int64 !(Maybe FormationClock) !Int64
  | AcceptedPrice !Text !Int64 !Double !Int64 | AcceptedSourceFrontier !SourceFrontier
  | AcceptedTurnOrigin !Text !ExactRef !ChildOrigin !(Maybe ExactRef) !Int64
  | AcceptedCoverageChange !Text ![(Double,Double)] ![(Double,Double)] !CoverageCondition !Int64 deriving (Eq,Show)
data FormationFrame = FormationFrame
  { frameProgress :: !Double, frameKnown :: !Int64, frameTurns :: ![GroupTurn]
  , framePatches :: ![FormationPatch], frameEnded :: !Bool, frameCoverage :: ![ObjectCoverage] }
  deriving (Eq,Show)
data MaterialTotals = MaterialTotals
  { observedTurns :: !(M.Map Text Int),peakMaterialTurns :: !Int,peakEnumerableTurns :: !Int
  , peakWaitingTurns :: !Int,failedCoverageFirings :: !Int,acceptedClockRevisions :: !Int,lateTurnOccurrences :: !Int
  , incompleteDomainFirings :: !Int,coverageRestorations :: !Int } deriving (Eq,Show)
data MaterialState = MaterialState
  { currentMaterial :: !FormationMaterial, unknownSince :: !(M.Map TurnKey Double)
  , objectCoverage :: !(M.Map Text ObjectCoverage), materialTotals :: !MaterialTotals }
  deriving (Eq,Show)
emptyMaterialState objects=MaterialState (FormationMaterial M.empty S.empty 0 0 S.empty False True) M.empty
  (M.fromList [(o,ObjectCoverage o CoverageColdStart Nothing Nothing) | o<-objects])
  (MaterialTotals M.empty 0 0 0 0 0 0 0 0)

advanceMaterial :: GroupMethod -> S.Set TurnKey -> FormationFrame -> MaterialState -> Either Text MaterialState
advanceMaterial method dependent frame old=do
  let before=currentMaterial old;u=frameProgress frame;known=frameKnown frame;delta=groupDelta method;observation=groupObservationDuration method
  unless (finite u && finite delta && delta>0 && finite observation && observation>0 && u>=materialProgress before && known>=materialKnown before)
    (Left "共同形成Calendar进展／知识回退或配置无效")
  installed<-foldM (install known) (materialTurns before) (frameTurns frame)
  changed<-foldM (patch known) installed (framePatches frame)
  coverage<-foldM acceptCoverage (objectCoverage old) (frameCoverage frame)
  let waits=M.union (unknownSince old) (M.fromList [(key,u) | (key,t)<-M.toList changed,groupTurnClock t==Nothing])
      eligible t=not (groupTurnRetracted t) && case groupTurnClock t of
        Just c->groupClockKnown c<=known && groupClockValue c+observation>=u
        Nothing->False
      enumerated=M.filter eligible changed
      waiting=M.filterWithKey (\key t->not (groupTurnRetracted t) && groupTurnClock t==Nothing &&
        maybe False (\first->u<=first+6*delta) (M.lookup key waits)) changed
      keep=S.unions [M.keysSet enumerated,M.keysSet waiting,dependent]
      retained=M.restrictKeys changed keep
      differences=S.fromList [key | (key,t)<-M.toList retained,M.lookup key (materialTurns before)/=Just t]
        `S.union` (M.keysSet (materialTurns before) `S.difference` M.keysSet retained)
      -- 覆盖按固定域逐对象判断。没有Turn仍可完整；另一对象发生不解除本对象限制。
      covered c=coverageCondition c==CoverageInapplicable ||
        (coverageCondition c==CoverageObserved && case (coverageFrom c,coverageThrough c) of
          (Just first,Just through)->first<=u-observation && through>=u
          _->False)
      incomplete=any (not . covered) (M.elems coverage) || not (M.null waiting)
      result=FormationMaterial retained (M.keysSet enumerated) u known differences (frameEnded frame) incomplete
      totals=materialTotals old
      nextTotals=MaterialTotals
        (M.unionWith (+) (observedTurns totals) (M.fromListWith (+) [(groupTurnObject t,1) | t<-frameTurns frame]))
        (max (peakMaterialTurns totals) (M.size retained)) (max (peakEnumerableTurns totals) (M.size enumerated))
        (max (peakWaitingTurns totals) (M.size waiting))
        (failedCoverageFirings totals+length [() | c<-frameCoverage frame,coverageCondition c==CoverageSourceFailure])
        (acceptedClockRevisions totals+length [() | AcceptedClock{}<-framePatches frame])
        (lateTurnOccurrences totals+length [() | t<-frameTurns frame,
          maybe False (\c->u>groupClockValue c+observation) (groupTurnClock t)])
        (incompleteDomainFirings totals+if incomplete then 1 else 0)
        (coverageRestorations totals+if materialCoverageIncomplete before && not incomplete then 1 else 0)
  pure (MaterialState result (M.restrictKeys waits (M.keysSet retained)) coverage nextTotals)
  where
    acceptCoverage values value=do
      unless (M.member (coverageObject value) values) (Left "覆盖对象不在固定声明域")
      unless (all finite (maybe [] pure (coverageFrom value)++maybe [] pure (coverageThrough value)) &&
        case (coverageFrom value,coverageThrough value) of
          (Just first,Just through)->first<=through && through<=frameProgress frame
          (Nothing,Nothing)->True
          _->False) (Left "当前覆盖边界非法")
      -- Source只发行本次成功点/相邻边。F保留当前连续覆盖区间；
      -- 只有同对象两段真实相接才合并，缺价/失知及未观察间隙断开。
      pure (M.insert (coverageObject value)
        (accumulateForwardCoverage (M.lookup (coverageObject value) values) value) values)
    install known turns t=do
      unless (groupTurnKnown t<=known && finite (groupTurnPrice t)) (Left "Turn未来知识或非法价格")
      case M.lookup (turnKey t) turns of
        Just prior | groupTurnRef prior==groupTurnRef t && prior/=t->Left "相同Turn exact不同正文"
        _->Right (M.insert (turnKey t) t turns)
    patch known turns change=case change of
      SourceStartAttempt{}->Right turns
      SourceConfirmationAttempt{}->Right turns
      AcceptedSourceFrontier _->Right turns
      AcceptedTurnOrigin{}->Right turns
      AcceptedCoverageChange{}->Right turns
      AcceptedClock object actual value valid->do
        unless (valid<=known && maybe True (\c->finite (groupClockValue c) && groupClockKnown c<=known) value)
          (Left "Clock修订含未来知识或非有限值")
        pure (M.map (updateClock object actual value) turns)
      AcceptedPrice object actual price valid->do
        unless (finite price && valid<=known) (Left "原价修订含未来知识或非有限值")
        pure (M.map (updatePrice object actual price valid) turns)

-- | 同对象的实际forward片段组成当前连续区间；失败和空洞不能被连接。
-- Source仍向需要区间增删的消费者发行原窄边，不把此状态反送给Source。
accumulateForwardCoverage :: Maybe ObjectCoverage -> ObjectCoverage -> ObjectCoverage
accumulateForwardCoverage previous value=
  case (previous,coverageFrom value,coverageThrough value) of
    (Just prior,Just first,Just through)
      | coverageObject prior==coverageObject value
      , coverageCondition prior==CoverageObserved && coverageCondition value==CoverageObserved
      , Just oldFirst<-coverageFrom prior,Just oldThrough<-coverageThrough prior
      , first<=oldThrough && through>=oldThrough ->value {coverageFrom=Just (min oldFirst first)}
    _->value

updateClock object actual value t
  | groupTurnObject t/=object=t
  | otherwise=let g=groupTurnGeometry t
                  point p@(at,price,_) | at==actual=(at,price,toClock <$> value)
                                       | otherwise=p
                  p=point <$> geometryP g;q=point (geometryT g);r=point (geometryC g)
              in t {groupTurnClock=if groupTurnActual t==actual then value else groupTurnClock t,
                groupTurnGeometry=geometryFromKnown (geometryPKnown g) (geometryTKnown g) (geometryCKnown g) p q r}
  where toClock c=CalendarClockValue (groupClockKnown c) (groupClockValue c)
updatePrice object actual price valid t
  | groupTurnObject t/=object=t
  | otherwise=let g=groupTurnGeometry t
                  point p@(at,_,clock) | at==actual=(at,price,clock)
                                       | otherwise=p
                  p=point <$> geometryP g;q=point (geometryT g);r=point (geometryC g)
              in t {groupTurnPrice=if groupTurnActual t==actual then price else groupTurnPrice t,
                groupTurnGeometry=geometryFromKnown
                  (if maybe False (\(a,_,_)->a==actual) (geometryP g) then Just valid else geometryPKnown g)
                  (if groupTurnActual t==actual then valid else geometryTKnown g)
                  (if (\(a,_,_)->a==actual) (geometryC g) then valid else geometryCKnown g) p q r}
