{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE TupleSections #-}
{-# LANGUAGE OverloadedStrings #-}
-- | 四项Required独立判断。局部pair过程只重算真实端点变化影响的pair；
-- 保留仍被已发行有限候选引用、但已退出新枚举的端点。
module Frp.Instance.ISL.Opportunity.U2.GroupCandidatePairs where
import Control.Monad (unless)
import Data.Maybe (maybeToList)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import Data.Text (Text)
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes
import Frp.Instance.ISL.Opportunity.U2.Source (finite)
import Frp.Instance.ISL.Opportunity.U2.Source
import Frp.Instance.ISL.Opportunity.U2.Formation (FormationProfile(..),Compatibility(..))
import Frp.Instance.ISL.Opportunity.U2.BoundedRelations hiding (PairKey)
import Frp.Instance.ISL.Opportunity.U2.Episode (CalendarClockValue(..))

coordinates p=[basisTime p,basisDirection p,basisType p,basisBend p]
pairDecision p
  | any veto (coordinates p)=PairVeto
  | all (==CoordinateSupports) (coordinates p)=PairPositive
  | otherwise=PairUnresolved
  where veto CoordinateVeto{}=True;veto _=False

assessPair :: FormationProfile -> Integer -> GroupTurn -> GroupTurn -> Either Text PairBasis
assessPair profile known a b=do
  unless (finite (formationDelta profile) && formationDelta profile>0) (Left "共同转折Δ无效")
  unless (groupTurnObject a/=groupTurnObject b) (Left "共同转折pair重复对象")
  direction<-semantic DirectionUnavailable DirectionOpposed (formationDirectionMatrix profile)
    (groupTurnDirection a) (groupTurnDirection b)
  kind<-semantic TurnTypeUnavailable TurnTypeOpposed (formationTypeMatrix profile)
    (groupTurnType a) (groupTurnType b)
  let distance=do
        x<-groupTurnClock a;y<-groupTurnClock b
        if toInteger (max (groupClockKnown x) (groupClockKnown y))>known then Nothing
          else Just (abs (groupClockValue x-groupClockValue y))
      temporal=maybe (CoordinateUnresolved ActualClockUnavailable)
        (\d->if d<=2*formationDelta profile then CoordinateSupports else CoordinateVeto ActualDistanceExceeded) distance
      bend=case (selected a,selected b) of
        (Right x,Right y) | x==BendCollinear || y==BendCollinear->CoordinateUnresolved SelectedCollinear
                         | x==y->CoordinateSupports
                         | otherwise->CoordinateVeto SelectedBendOpposed
        (Left gap,_)->CoordinateUnresolved gap
        (_,Left gap)->CoordinateUnresolved gap
      withdrawn=groupTurnRetracted a || groupTurnRetracted b
  pure (PairBasis (groupTurnRef a) (groupTurnRef b) distance
    (if withdrawn then CoordinateVeto SourceTurnWithdrawn else temporal) direction kind bend)
  where
    semantic gap reason matrix left right=case (left,right) of
      (Just x,Just y)->case M.lookup (x,y) matrix of
        Just Compatible->Right CoordinateSupports
        Just IncompatibleVeto->Right (CoordinateVeto reason)
        Just CompatibilityUndetermined->Right (CoordinateUnresolved gap)
        _->Left "实际方向／TurnType兼容配置缺失或冲突"
      _->Right (CoordinateUnresolved gap)
    selected t =
      let g = groupTurnGeometry t
          points = maybeToList (geometryP g) ++ [geometryT g, geometryC g]
          knowns = maybeToList (geometryPKnown g) ++ [geometryTKnown g, geometryCKnown g]
      in if any ((>known) . toInteger) knowns || any (maybe False ((>known) . toInteger . clockValueKnownFrom) . third) points
           then Left SelectedKnowledgeUnavailable
           else case geometryBend g of
             Right x -> Right x
             Left GeometryNoAnchor -> Left SelectedAnchorUnavailable
             Left GeometryClockMissing -> Left SelectedClockUnavailable
             Left GeometryInvalidLeg -> Left SelectedLegInvalid
             Left GeometryOverflow -> Left SelectedLegInvalid
    third (_,_,x)=x

advancePairView :: FormationProfile -> S.Set TurnKey -> FormationMaterial -> M.Map PairKey PairBasis
  -> Either Text PairView
advancePairView profile dependent material before=do
  let wanted=S.union dependent (materialEnumerable material)
      turns=M.restrictKeys (materialTurns material) wanted
      keys=[(ka,kb) | (ka,a)<-M.toAscList turns,(kb,b)<-M.toAscList turns,ka<kb,
        groupTurnObject a/=groupTurnObject b]
  values<-mapM (\key@(a,b)->case M.lookup key before of
    Just old | not (a `S.member` materialChanged material || b `S.member` materialChanged material)->Right (key,old)
    _->(key,) <$> assessPair profile (toInteger (materialKnown material)) (turns M.! a) (turns M.! b)) keys
  pure (PairView material (M.fromList values))
