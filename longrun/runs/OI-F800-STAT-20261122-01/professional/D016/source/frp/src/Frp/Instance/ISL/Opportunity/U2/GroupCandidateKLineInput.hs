{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE PatternSynonyms #-}
{-# LANGUAGE OverloadedStrings #-}
-- | F/Q直接消费正常ScaleTurnCalendar和KLine，不生产或读取Source产品。
module Frp.Instance.ISL.Opportunity.U2.GroupCandidateKLineInput where

import Control.Applicative ((<|>))
import Control.Monad.IO.Class (liftIO)
import Data.Int (Int64)
import Data.Ratio (denominator,numerator)
import qualified Data.Map.Strict as M
import Data.Aeson
import qualified Data.Text as T
import Geometry (pattern Point2)
import Reflex (foldDyn,updated,fmapMaybe,mergeWith)
import Frp.Apt (FrpEvent)
import Frp.Core
import Frp.Core.Fao.Tis qualified as K
import Frp.Instance.ISL.Geometry.ScaleTurn.ScaleTurn qualified as ST
import Frp.Instance.ISL.Geometry.ScaleTurn.STCalendar (ScaleTurnCalendar(..))
import Frp.Instance.ISL.Wave.ZigN qualified as Zig
import Frp.Instance.ISL.Opportunity.U2.Source (SourceRound(..))
import Frp.Instance.ISL.Opportunity.U2.Types
import Frp.Instance.ISL.Opportunity.U2.Episode (CalendarClockValue(..))
import Frp.Instance.ISL.Opportunity.U2.EpisodeMaterialReader (EpisodeMarketConfig(..))
import Frp.Instance.ISL.Opportunity.U2.NativeSource (exactUTI)
import Frp.Instance.ISL.Opportunity.U2.BoundedRelations (geometryFromKnown)
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateMaterial

-- 一个成员的正常上游参数；不是独立Fao或保存产品。
data GroupKLineInput = GroupKLineInput
  { inputSymbol :: !T.Text, inputCalendar :: !CalendarName
  , inputScaleTurn :: !ScaleTurnCalendar, inputFrequency :: !Freq }
  deriving Show
instance ToJSON GroupKLineInput where
  toJSON x=object ["symbol" .= inputSymbol x,"calendar" .= inputCalendar x
    ,"scale_turn" .= inputScaleTurn x,"freq" .= inputFrequency x]
instance FromJSON GroupKLineInput where
  parseJSON=withObject "KLine转折输入" $ \v->GroupKLineInput
    <$> v .: "symbol" <*> v .: "calendar" <*> v .: "scale_turn" <*> v .: "freq"

-- 固定秒/分钟频率换算到源UTI的离散步长。Double单位按其实际值精确解释；
-- 非整数步长、Tick及非固定开放时长的日/周/月不能靠舍入或容差假装相邻。
klineUTIStep :: Freq -> Double -> Double -> Either T.Text Int64
klineUTIStep frequency unitsPerMinute unitsPerTick
  | freq_type frequency `notElem` [SecondFreq,MinuteFreq]
    || freq_interval frequency<=0 || freq_ns frequency<=0=
      Left "KLine coverage requires a positive fixed second/minute frequency"
  | any (\units->isNaN units || isInfinite units || units<=0) [unitsPerMinute,unitsPerTick]=
      Left "KLine coverage requires finite positive Calendar unit conversions"
  | denominator step/=1 || numerator step<=0 || numerator step>toInteger (maxBound::Int64)=
      Left "KLine frequency/Calendar conversion has no positive exact Int64 UTI step; refusing rounding"
  | otherwise=Right (fromInteger (numerator step))
  where step=fromIntegral (freq_ns frequency)*toRational unitsPerMinute/
          (60000000000*toRational unitsPerTick)

-- Source只发行当前成功点或一条真实相邻边；大坐标不先做浮点除法。
-- Integer差避免源Int64两端相减溢出，冷启动和真实缺口仍重启覆盖。
klineForwardCoverage :: Int64 -> T.Text -> Maybe (Int64,Double) -> (Int64,Double) -> ObjectCoverage
klineForwardCoverage step object previous (at,u)=ObjectCoverage object CoverageObserved
  (Just (case previous of
    Just (prior,old) | toInteger at-toInteger prior==toInteger step->old
    _->u)) (Just u)

-- close、closeUti本来就在同一个KLine收盘事件中；时间坐标直接使用原UTI。
groupKLineEvents :: HasHisBack => GroupKLineInput -> EpisodeMarketConfig
  -> FaoModel (FrpEvent (Tick (Double,Int64,Double,Double)))
groupKLineEvents plan market=do
  _<-either (liftIO . fail . T.unpack) pure
    (klineUTIStep (inputFrequency plan) (marketUnitsPerOpenMinute market) (marketUnitsPerCalendarTick market))
  let frequency=inputFrequency plan
      kline=K.KLine frequency
      -- Q报价位置接口保持原换算；覆盖不再依赖这个Double商。
      step=fromIntegral (freq_ns frequency)/1e9/60*marketUnitsPerOpenMinute market
  fields<-doGenericFaoResult kline
  let price=fields M.! "close";uti=fields M.! "closeUti"
      joined=mergeWith combine
        [(\x->(Just x,Nothing)) <$> price,(\x->(Nothing,Just x)) <$> uti]
      combine (p,u) (q,v)=(p<|>q,u<|>v)
      row (Just (Tick _ p _),Just (Tick ts u _))=Just (Tick ts
        (p,either (error . show) id (exactUTI u),u/step,marketUnitsPerCalendarTick market*u) Nothing)
      row _=Nothing
  pure (fmapMaybe row joined)

-- 持有上一轮锚点及其后的Zig类型；引用定位到上游结果行，不另发行Source身份。
buildKLineGroupSource :: HasHisBack => GroupKLineInput -> EpisodeMarketConfig
  -> FaoModel (FrpEvent (Tick FormationFrame))
buildKLineGroupSource plan market=do
  utiStep<-either (liftIO . fail . T.unpack) pure
    (klineUTIStep (inputFrequency plan) (marketUnitsPerOpenMinute market) (marketUnitsPerCalendarTick market))
  let feature=inputScaleTurn plan
      object=inputSymbol plan
  root<-getFullDir feature
  (first,second)<-runFao feature
  firstTicks<-wrapTickEvent first
  secondTicks<-wrapTickEvent second
  quotes<-groupKLineEvents plan market
  zig<-runFao (falter feature)
  zigTicks<-wrapTickEvent zig
  let input=mergeWith merge
        [(\t->fmap (\x->(Just x,Nothing,Nothing,Nothing)) t) <$> firstTicks
        ,(\t->fmap (\x->(Nothing,Just x,Nothing,Nothing)) t) <$> secondTicks
        ,fmap (\x->(Nothing,Nothing,Just x,Nothing)) <$> quotes
        ,fmap (\x->(Nothing,Nothing,Nothing,Just x)) <$> zigTicks]
      merge a b=let (p,q,r,v)=atTickValue a;(s,t,u,w)=atTickValue b
        in Tick (atTickTs a) (p<|>s,q<|>t,r<|>u,v<|>w) Nothing
      clock known at=FormationClock (marketUnitsPerCalendarTick market*fromIntegral at) known
      point known (Point2 at price)=(round at,price,
        Just (CalendarClockValue known (marketUnitsPerCalendarTick market*at)))
      selected types roundValue anchor known value=
        let t@(Point2 at price)=ST.actual value;c@(Point2 confirmation _)=ST.confirm value
            actual=round at;confirmed=round confirmation
            rowName=if roundValue==FirstRound then "value1" else "value2"
            location=T.pack root<>"/"<>rowName<>"/"<>T.pack (show confirmed)
            ref=ExactRef "ScaleTurnCalendar" "Turn" location location
            source=ExactRef "ScaleTurnCalendar" "Result" (T.pack root) rowName
            (polarity,turnKnown)=types M.! actual
            direction=(\positive->if positive then DirectionDown else DirectionUp) <$> polarity
            kind=(\positive->if positive then SourcePeakTurn else SourceTroughTurn) <$> polarity
            geometry=geometryFromKnown (snd <$> anchor) turnKnown known
              ((\(p,k)->point k p) <$> anchor) (point turnKnown t) (point known c)
        in GroupTurn ref source object actual price confirmed known direction kind roundValue
             geometry (Just (clock turnKnown actual)) False Nothing
      advance tick (anchor,previous,types,_)=
        let (a,b,Just (price,known,_,u),z)=atTickValue tick
              :: (Maybe ST.CompleteScaleTurn,Maybe ST.CompleteScaleTurn,
                  Maybe (Double,Int64,Double,Double),Maybe Zig.ZigWithStatusOcc)
            currentTypes=case z of
              Just v->let polarity=case compare (Zig.pivot1 v*Zig.price1 v) 0 of
                            GT->Just True;LT->Just False;EQ->Nothing
                      in M.insertWith (\_ old->old) (round (Zig.posUTI1 v)) (polarity,known) types
              Nothing->types
            selectedAnchor value=let t=ST.actual value;Point2 at _=t
                                 in (t,snd (currentTypes M.! round at))
            firstTurns=maybe [] (pure . selected currentTypes FirstRound anchor known) a
            nextAnchor=case a of Just v->Just (selectedAnchor v);Nothing->anchor
            secondTurns=maybe [] (pure . selected currentTypes SecondRound nextAnchor known) b
            after=case b of Just v->Just (selectedAnchor v);Nothing->nextAnchor
            validPrice=not (isNaN price || isInfinite price)
            coverage=[if validPrice then klineForwardCoverage utiStep object previous (known,u)
              else ObjectCoverage object CoverageInputMissing Nothing Nothing]
            frame=FormationFrame u known (firstTurns++secondTurns) [] False coverage
            before=if validPrice then Just (known,u) else Nothing
            retained=case after of
              Just (Point2 at _,_)->M.filterWithKey (\uti _->uti>=round at) currentTypes
              Nothing->currentTypes
        in (after,before,retained,Just (fmap (const frame) tick))
  result<-foldDyn advance (Nothing,Nothing,M.empty,Nothing) input
  pure (fmapMaybe (\(_,_,_,row)->row) (updated result))
