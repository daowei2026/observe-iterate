{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE RecursiveDo #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE TypeFamilies #-}
-- | 薄父Fao：正常来源、有限材料、pair和候选生命各自拥有其局部状态。
module Frp.Instance.ISL.Opportunity.CommonPriceTurnGroupCandidates where
import Control.Monad (forM,unless)
import Control.Monad.IO.Class (liftIO)
import Data.Aeson
import Data.Aeson.Types (Parser)
import Data.Aeson.KeyMap qualified as KM
import Data.Maybe (fromMaybe)
import Data.Text (Text)
import qualified Data.Text as T
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import Reflex (mergeWith,foldDynM,updated,current,attachWith,fmapMaybe,never)
import Frp.Apt (FrpEvent,FrpBehavior,FrpDynamic)
import Frp.CEP (CEPS(..))
import Frp.Core
import Frp.Instance.ISLTC.AdtStorage (MulWrap(..))
import Frp.Instance.ISL.Opportunity.U2.Types
import Frp.Instance.ISL.Opportunity.U2.Source
import Frp.Instance.ISL.Opportunity.U2.SourceProducer (producerBinding)
import Frp.Instance.ISL.Opportunity.U2.NativeSource
import Frp.Instance.ISL.Opportunity.U2.Episode (PriceComparison(..))
import Frp.Instance.ISL.Opportunity.U2.EpisodeMaterialReader
import Frp.Instance.ISL.Opportunity.U2.Formation
import Frp.Instance.ISL.Opportunity.U2.TurnRelationsPipeline
  (domainConfiguration,parseDomainConfiguration,profileConfiguration,parseProfileConfiguration)
import Frp.Instance.ISL.Opportunity.U2.ThinNodeResults qualified as Thin
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateSource
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateKLineInput
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateStoredSource
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateMaterial
import Frp.Instance.ISL.Opportunity.U2.GroupCandidatePairs
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateEvolution
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateStorage
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateDba ()

data GroupSourceConfiguration = GroupSourceConfiguration
  { groupSourcePlan :: !NativeSourcePlan,groupSourceMarket :: !EpisodeMarketConfig }
  | GroupKLineConfiguration
  { groupKLineInput :: !GroupKLineInput,groupSourceMarket :: !EpisodeMarketConfig }
  deriving Show

groupSourceObject :: GroupSourceConfiguration -> Text
groupSourceObject (GroupSourceConfiguration plan _)=scopeObject (sourceScope (producerBinding (nativeSourceBinding plan)))
groupSourceObject (GroupKLineConfiguration input _)=inputSymbol input
groupSourceCalendar :: GroupSourceConfiguration -> CalendarName
groupSourceCalendar (GroupSourceConfiguration plan _)=nativeCalendar plan
groupSourceCalendar (GroupKLineConfiguration input _)=inputCalendar input

instance ToJSON GroupSourceConfiguration where
  toJSON x=let m=groupSourceMarket x
               fields=case x of
                 GroupSourceConfiguration plan _->["source" .= plan]
                 GroupKLineConfiguration input _->["input" .= input]
           in object (fields++["market" .= object
      ["calendar_position_field" .= marketCalendarPositionField m,"calendar_stride" .= marketCalendarStride m
      ,"duration_unit" .= marketDurationUnit m,"units_per_calendar_tick" .= marketUnitsPerCalendarTick m
      ,"units_per_open_minute" .= marketUnitsPerOpenMinute m
      ,"price_comparison" .= case marketPriceComparison m of
        ExactNumericPrice ref->object ["kind" .= ("ExactNumericPrice"::Text),"method" .= nativeReferenceValue ref]
        CanonicalTickPrice ref->object ["kind" .= ("CanonicalTickPrice"::Text),"method" .= nativeReferenceValue ref]
        _->Null
      ,"normalization" .= Null]])
instance FromJSON GroupSourceConfiguration where
  parseJSON=withObject "共同候选真实来源" $ \v->do
    input<-v .:? "input"
    market<-v .: "market" >>= withObject "真实Calendar换算" (\m->do
      comparison<-m .: "price_comparison" >>= withObject "真实原价比较" (\c->do
        kind<-c .: "kind";ref<-c .: "method" >>= parseNativeReference
        case (kind::Text) of
          "ExactNumericPrice"->pure (ExactNumericPrice ref)
          "CanonicalTickPrice"->pure (CanonicalTickPrice ref)
          _->fail "共同价格候选缺少真实原价比较方法")
      normalization<-m .:? "normalization" :: Parser (Maybe Value)
      unless (normalization==Nothing || normalization==Just Null) (fail "本项比较各自弯折，不选择跨对象价格归一化")
      EpisodeMarketConfig <$> m .: "calendar_position_field" <*> m .: "calendar_stride"
        <*> m .: "duration_unit" <*> m .: "units_per_calendar_tick" <*> pure comparison <*> pure Nothing
        <*> m .: "units_per_open_minute")
    either (fail . show) pure (validateEpisodeMarketConfig market)
    case input of
      Just value->pure (GroupKLineConfiguration value market)
      Nothing->GroupSourceConfiguration <$> v .: "source" <*> pure market

data CommonPriceTurnGroupCandidatesFrp = CommonPriceTurnGroupCandidatesFrp
  { groupSources :: ![GroupSourceConfiguration],groupDomain :: !FormationDomain
  , groupProfile :: !FormationProfile,groupOnlyRead :: !Bool
  , groupFormationObservationMultiple :: !(Maybe Double) } deriving Show
constructGroupCandidates :: [GroupSourceConfiguration] -> FormationDomain -> FormationProfile
  -> Either FormationError CommonPriceTurnGroupCandidatesFrp
constructGroupCandidates sources domain profile=do
  validateFormationConfiguration domain profile
  unless (not (null sources)) (Left (FormationContractError "候选缺少真实来源"))
  let bindings=[producerBinding (nativeSourceBinding p) | GroupSourceConfiguration p _<-sources]
      objects=map groupSourceObject sources
      units=map (marketUnitsPerOpenMinute . groupSourceMarket) sources
      ranges=[nativeInputRange p | GroupSourceConfiguration p _<-sources]
      unitsText=map (marketDurationUnit . groupSourceMarket) sources
  unless (length objects==S.size (S.fromList objects) && S.fromList objects==S.fromList (formationObjects domain)
    && (null ranges || all (==head ranges) ranges) && all (==head units) units && all (\u->finite u && u>0) units
    && all (==formationTimeUnit profile) unitsText)
    (Left (FormationContractError "共同候选对象域或显式正Δ/Calendar单位未绑定"))
  unless (all (\b->scopeContextRevision (sourceScope b)==formationContext domain &&
    scopeScale (sourceScope b)==formationScale domain && scopeCoherenceDomain (sourceScope b)==formationDomain domain &&
    sourceCalendar b==formationCalendar domain) bindings)
    (Left (FormationContractError "共同候选来源与声明语境/尺度/Calendar不一致"))
  pure (CommonPriceTurnGroupCandidatesFrp sources domain profile False Nothing)
-- | Optional profile field; omission preserves the original serialized configuration.
withGroupObservationMultiple :: Double -> CommonPriceTurnGroupCandidatesFrp
  -> Either FormationError CommonPriceTurnGroupCandidatesFrp
withGroupObservationMultiple multiple feature=do
  unless (finite multiple && multiple>0 && finite (multiple*formationDelta (groupProfile feature)))
    (Left (FormationContractError "Formation observation multiple must be finite and positive"))
  pure feature {groupFormationObservationMultiple=Just multiple}

groupProfileConfiguration :: CommonPriceTurnGroupCandidatesFrp -> Value
groupProfileConfiguration feature=
  let base=profileConfiguration (groupProfile feature)
  in case (groupFormationObservationMultiple feature,base) of
    (Just multiple,Object fields)->Object (KM.insert "observation_multiple" (toJSON multiple) fields)
    _->base

groupFormationMethod :: CommonPriceTurnGroupCandidatesFrp -> GroupMethod
groupFormationMethod feature=
  let profile=groupProfile feature
  in CompleteLinkPriceTurns (formationDelta profile) (formationTimeUnit profile)
    (fromMaybe 6 (groupFormationObservationMultiple feature))

instance ToJSON CommonPriceTurnGroupCandidatesFrp where
  toJSON x=object ["__tag__" .= ("CommonPriceTurnGroupCandidatesFrp"::Text),"sources" .= groupSources x
    ,"domain" .= domainConfiguration (groupDomain x),"profile" .= groupProfileConfiguration x
    ,"result_layout" .= groupCandidatesFormat]
instance FromJSON CommonPriceTurnGroupCandidatesFrp where
  parseJSON=withObject "共同价格转折候选组" $ \v->do
    layout<-v .: "result_layout"
    unless (layout==groupCandidatesFormat) (fail "共同候选布局不支持")
    sources<-v .: "sources";domain<-v .: "domain" >>= parseDomainConfiguration
    profileValue<-v .: "profile"
    profile<-parseProfileConfiguration profileValue
    observation<-withObject "Formation observation profile" (\p->p .:? "observation_multiple") profileValue
    readOnly<-v .:? "only_read" .!= False
    feature<-either (fail . show) pure (constructGroupCandidates sources domain profile)
    configured<-maybe (pure feature) (either (fail . show) pure . (`withGroupObservationMultiple` feature)) observation
    pure configured {groupOnlyRead=readOnly}
instance FaoMeta CommonPriceTurnGroupCandidatesFrp where
  propCalType x=if groupOnlyRead x then OnlyRead else Cache
  propTarType _=pure FuncTarType
instance Fao CommonPriceTurnGroupCandidatesFrp where
  type FaoResult CommonPriceTurnGroupCandidatesFrp=FrpEvent (Tick [GroupCandidatesRecord])
  ppname _="CommonPriceTurnGroupCandidatesFrp"
  getFaoConstr _="CommonPriceTurnGroupCandidatesFrp"
  ggjson=encodeNativeConfiguration
  load feature=withEventLoad feature $ do
    records<-loadAdtEvent @(MulWrap GroupCandidatesRecord) groupCandidatesFormat
    pure (fmap (\(MulWrap xs)->map checked xs) <$> records)
  dump=writeGroupCandidates

  doImpl feature=do
    either (liftIO . fail . show) (const (pure ())) (constructGroupCandidates (groupSources feature) (groupDomain feature) (groupProfile feature))
    (_,occurrences)<-buildStoredGroupFormation feature
    groupCandidatePublication feature occurrences

-- | F只保存自身同次带原时间的publication，不重建候选或来源。
writeGroupCandidates :: CommonPriceTurnGroupCandidatesFrp
  -> FrpEvent (Tick [GroupCandidatesRecord]) -> FaoModel ()
writeGroupCandidates feature records=
  withEventDump feature $ dumpAdtEvent groupCandidatesFormat
    (fmap (MulWrap . map checked) <$> records)

checked :: GroupCandidatesRecord -> GroupCandidatesRecord
checked record=case validateGroupRecord record of
  Left problem->error (T.unpack problem)
  Right x->forceGroupRecord x `seq` x
-- | KLine入口直接调用已有ScaleTurnCalendar；旧来源配置仅保留原存读入口。
buildStoredGroupFormation :: HasHisBack => CommonPriceTurnGroupCandidatesFrp
  -> FaoModel (FrpEvent (Tick [FormationFrame]),FrpEvent (Tick [CandidateOccurrence]))
buildStoredGroupFormation feature=do
  streams<-forM (groupSources feature) $ \source->
    withSymbol (groupSourceObject source) $ withCalendar (groupSourceCalendar source) $
      case source of
        GroupKLineConfiguration input market->buildKLineGroupSource input market
        GroupSourceConfiguration plan market->buildStoredGroupSource plan market
  let frames=mergeWith (\a b->Tick (atTickTs a) (atTickValue a++atTickValue b) Nothing)
        [fmap (fmap pure) stream | stream<-streams]
      profile=groupProfile feature
      method=groupFormationMethod feature
  (_,_,occurrences)<-commonTurnFormationCurrent method profile (formationObjects (groupDomain feature)) frames
  pure (frames,occurrences)

-- | 正常F与Q共用一次Source/C0/F图。额外依赖只保护来源准确Turn小值，
-- 不进入F的6Δ新枚举域；当前值沿Event直接交给消费者。
buildGroupFormation :: CommonPriceTurnGroupCandidatesFrp -> FrpBehavior (S.Set TurnKey)
  -> FaoModel (FrpEvent (Tick [FormationFrame]),FrpEvent (Tick [CandidateOccurrence]))
buildGroupFormation feature additional=do
    (frames,occurrences,_)<-buildGroupFormationWithCoverage feature additional M.empty
    pure (frames,occurrences)

-- | 同一个正常形成实例同时交出候选、逐对象frame及真实历史覆盖修正。
-- 原Source尚不发行历史修订时无此发生；显式合法producer事件接同一处理入口。
buildGroupFormationWithCoverage :: CommonPriceTurnGroupCandidatesFrp -> FrpBehavior (S.Set TurnKey)
  -> M.Map Text (FrpEvent GroupSourceInput)
  -> FaoModel (FrpEvent (Tick [FormationFrame]),FrpEvent (Tick [CandidateOccurrence]),FrpEvent (Tick [GroupCoverageCorrection]))
buildGroupFormationWithCoverage feature additional revisions=
  buildGroupFormationWithCoverageMany feature additional (M.map (fmap pure) revisions)

-- | 同一形成实例接受本拍有限修订批次，供多个合法观察lane共享实际producer。
buildGroupFormationWithCoverageMany :: CommonPriceTurnGroupCandidatesFrp -> FrpBehavior (S.Set TurnKey)
  -> M.Map Text (FrpEvent [GroupSourceInput])
  -> FaoModel (FrpEvent (Tick [FormationFrame]),FrpEvent (Tick [CandidateOccurrence]),FrpEvent (Tick [GroupCoverageCorrection]))
buildGroupFormationWithCoverageMany feature additional revisions=do
    (_,_,frames,occurrences,corrections)<-buildGroupFormationAppearanceCurrent feature additional revisions
    pure (frames,occurrences,corrections)

-- | 共享正常形成的当前有限参与和逐对象Clock/覆盖，不暴露整个Formation状态。
buildGroupFormationAppearanceCurrent :: CommonPriceTurnGroupCandidatesFrp -> FrpBehavior (S.Set TurnKey)
  -> M.Map Text (FrpEvent [GroupSourceInput])
  -> FaoModel (FrpDynamic [GroupSourceAppearanceCurrent],FrpDynamic ([CandidateOccurrence],S.Set Text),
      FrpEvent (Tick [FormationFrame]),FrpEvent (Tick [CandidateOccurrence]),FrpEvent (Tick [GroupCoverageCorrection]))
buildGroupFormationAppearanceCurrent feature additional revisions=mdo
    let profile=groupProfile feature
        method=groupFormationMethod feature
        needed=S.union <$> dependencies <*> additional
    streams<-forM (groupSources feature) $ \source->do
      let plan=groupSourcePlan source;object=scopeObject (sourceScope (producerBinding (nativeSourceBinding plan)))
      withSymbol object $ withCalendar (nativeCalendar plan) $
        buildGroupSourceAppearanceCurrent plan (groupSourceMarket source) method needed (M.findWithDefault never object revisions)
    let combined=mergeWith (\a b->Tick (atTickTs a) (atTickValue a++atTickValue b) Nothing)
          [fmap (fmap pure) stream | (_,stream)<-streams]
        frames=fmap (map fst) <$> combined
        corrections=fmap (concatMap snd) <$> combined
    (dependencies,candidates,occurrences)<-commonTurnFormationCurrent method profile (formationObjects (groupDomain feature)) frames
    let sources=sequenceA [view | (view,_)<-streams]
    pure (sources,candidates,frames,occurrences,corrections)

-- | 同一份已决定F发生的正常薄publication；配套保存不重算候选。
groupCandidatePublication :: CommonPriceTurnGroupCandidatesFrp -> FrpEvent (Tick [CandidateOccurrence])
  -> FaoModel (FrpEvent (Tick [GroupCandidatesRecord]))
groupCandidatePublication feature occurrences=do
    publication<-foldDynM (\tick (initial,_)->do
      let rows=atTickValue tick
          record=publishGroupOccurrences (if initial then Just (storeDefinition feature) else Nothing) rows
          output=(\value->Tick (atTickTs tick) [value] Nothing) <$> record
      pure (False,output)) (True,Nothing) occurrences
    pure (fmapMaybe snd (updated publication))

-- 正常publication与有限合同检查共用的真实包装／校验入口。
publishGroupOccurrences :: Maybe GroupDefinitionRecord -> [CandidateOccurrence] -> Maybe GroupCandidatesRecord
publishGroupOccurrences definition rows
  | definition==Nothing && null rows=Nothing
  | otherwise=Just (checked (GroupCandidatesRecord (maybe [] pure definition) (map storeGroupOccurrence rows)))

-- | 一个可组合的共同转折形成过程。输入是当前成功来源发生，输出为
-- 已决定的候选发生和当前有限依赖；来源本身仍由正常Fao共享。
data CommonTurnFormation = CommonTurnFormation !GroupMethod !FormationProfile ![Text]
instance CEPS CommonTurnFormation FaoModel where
  type Input CommonTurnFormation = FrpEvent (Tick [FormationFrame])
  type Output CommonTurnFormation = (FrpBehavior (S.Set TurnKey),FrpEvent (Tick [CandidateOccurrence]))
  processEvents (CommonTurnFormation method profile objects) frames=do
    (dependencies,_,occurrences)<-commonTurnFormationCurrent method profile objects frames
    pure (dependencies,occurrences)

-- | 原三个局部owner及其有限candidate current共用一次演化，不另建候选算法。
commonTurnFormationCurrent :: GroupMethod -> FormationProfile -> [Text] -> FrpEvent (Tick [FormationFrame])
  -> FaoModel (FrpBehavior (S.Set TurnKey),FrpDynamic ([CandidateOccurrence],S.Set Text),FrpEvent (Tick [CandidateOccurrence]))
commonTurnFormationCurrent method profile objects frames=mdo
    let dependencies=candidateDependencies . fst <$> current candidates
    material<-formationMaterialProcess method objects dependencies frames
    pairs<-formationPairProcess profile dependencies material
    candidates<-formationCandidateProcess method pairs
    pure (dependencies,(\(state,_)->(M.elems (activeCandidates state),retiredParticipationObjects state)) <$> candidates,fmapMaybe snd (updated candidates))

-- 每个过程实际拥有独立Dynamic；只用旧Behavior取依赖，当前材料沿事件传给下游。
formationMaterialProcess :: GroupMethod -> [Text] -> FrpBehavior (S.Set TurnKey) -> FrpEvent (Tick [FormationFrame])
  -> FaoModel (FrpEvent (Tick FormationMaterial))
formationMaterialProcess method objects dependencies events=do
  state<-foldDynM (\(needed,tick) (old,_)->do
    let fs=atTickValue tick
        -- 个别对象没有当前Clock时，沿已知公共进展判断其缺件；它不能
        -- 把其它对象已成功接受的进展倒回自己的旧Clock。
        frame=FormationFrame (max (materialProgress (currentMaterial old)) (maximum (map frameProgress fs)))
          (max (materialKnown (currentMaterial old)) (maximum (map frameKnown fs)))
          (concatMap frameTurns fs) (concatMap framePatches fs) (any frameEnded fs) (concatMap frameCoverage fs)
    next<-either (liftIO . fail . T.unpack) pure (advanceMaterial method needed frame old)
    if frameEnded frame then liftIO (putStrLn ("GROUP_MATERIAL_TOTALS "++show (materialTotals next))) else pure ()
    pure (next,Just (Tick (atTickTs tick) (currentMaterial next) Nothing)))
    (emptyMaterialState objects,Nothing) (attachWith (,) dependencies events)
  pure (fmapMaybe snd (updated state))
formationPairProcess :: FormationProfile -> FrpBehavior (S.Set TurnKey) -> FrpEvent (Tick FormationMaterial)
  -> FaoModel (FrpEvent (Tick PairView))
formationPairProcess profile dependencies events=do
  state<-foldDynM (\(needed,tick) (old,_)->do
    next<-either (liftIO . fail . T.unpack) pure (advancePairView profile needed (atTickValue tick) old)
    pure (pairBases next,Just (Tick (atTickTs tick) next Nothing)))
    (M.empty,Nothing) (attachWith (,) dependencies events)
  pure (fmapMaybe snd (updated state))
formationCandidateProcess :: GroupMethod -> FrpEvent (Tick PairView)
  -> FaoModel (FrpDynamic (CandidateState,Maybe (Tick [CandidateOccurrence])))
formationCandidateProcess method events=
  foldDynM (\tick (before,_)->do
    next<-advanceCandidates method (atTickValue tick) before
    (after,rows)<-either (liftIO . fail . T.unpack) pure next
    pure (after,Just (Tick (atTickTs tick) rows Nothing))) (emptyCandidateState,Nothing) events
storeDefinition :: CommonPriceTurnGroupCandidatesFrp -> GroupDefinitionRecord
storeDefinition feature=
  let d=groupDomain feature;p=groupProfile feature
  in GroupDefinitionRecord (Thin.definition (formationProfileRef p)) (Thin.definition (formationContext d))
    (Thin.definition (formationScale d)) (Thin.definition (formationCalendar d)) (Thin.definition (formationUniverse d))
    (formationDomain d) (formationObjects d) (formationDelta p) (formationTimeUnit p)
    [GroupCompatibilityRecord (directionCode a) (directionCode b) (code c) | ((a,b),c)<-M.toAscList (formationDirectionMatrix p)]
    [GroupCompatibilityRecord (code a) (code b) (code c) | ((a,b),c)<-M.toAscList (formationTypeMatrix p)]
