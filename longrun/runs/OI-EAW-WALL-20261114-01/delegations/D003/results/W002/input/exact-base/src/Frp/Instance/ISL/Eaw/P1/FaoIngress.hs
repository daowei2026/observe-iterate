{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE DerivingVia #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE ImplicitParams #-}
{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE RecordWildCards #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE TypeFamilies #-}

-- | 现有 DBA/genericLoad 到 P1 typed occurrence 的产品特定接缝。
module Frp.Instance.ISL.Eaw.P1.FaoIngress
  ( NumericRow,
    P1DecodedIngress (..),
    P1IngressError (..),
    WallOccurrenceFao (..),
    BuildOccurrenceFao (..),
    AttackSegmentFao (..),
    FormationEvidenceFao (..),
    WallBarrierFao (..),
    AbsorbOccurrenceFao (..),
    DirectedLargeDealOccurrenceFao (..),
    readThinProductReceipt,
    loadProductReceiptFrom,
    validateAttackProductInputs,
    groupResultKeyFields,
    mergeGenericFaoRows,
    partitionIngressBatch,
    decodeWallNumericRow,
    decodeBuildNumericRow,
    decodeAttackSegmentNumericRow,
    decodeAttackSegmentTransportBatch,
    decodeAttackFormationNumericRow,
    decodeWallBarrierNumericRow,
    decodeAbsorbNumericRow,
    decodeDirectedLargeDealNumericRow,
    toWallLifecycleOccurrences,
    toWallLifecycleIngress,
    toBuildActivityOccurrences,
    toBuildActivityIngress,
    toAttackSegmentOccurrences,
    toAttackSegmentIngress,
    toFormationEvidenceOccurrences,
    toFormationEvidenceIngress,
    toWallBarrierOccurrences,
    toWallBarrierIngress,
    wallIdentityCatalogFromArtifact,
    loadWallIdentityCatalogFrom,
    toAbsorbInteractionOccurrences,
    toAbsorbInteractionIngress,
    toDirectedLargeDealOccurrences,
    wallOccurrenceEvent,
    wallOccurrenceIngress,
    buildOccurrenceEvent,
    buildOccurrenceIngress,
    buildOccurrenceIngressWithCatalog,
    attackSegmentEvent,
    attackSegmentIngress,
    attackProductIngresses,
    formationEvidenceEvent,
    formationEvidenceIngress,
    wallBarrierEvent,
    wallBarrierIngress,
    absorbOccurrenceEvent,
    absorbOccurrenceIngress,
    absorbOccurrenceIngressWithCatalog,
    directedLargeDealEvent,
  )
where

import Control.Monad (forM, forM_, unless, when)
import Control.Monad.IO.Class (liftIO)
import Control.Monad.Trans.Class (lift)
import Data.Aeson
import Data.Char (isDigit)
import Data.Convertible (convert)
import Data.Either (partitionEithers)
import Data.Functor ((<&>))
import Data.Int (Int64)
import Data.List (sortOn)
import Data.List.NonEmpty (NonEmpty (..))
import Data.Map.Strict (Map)
import Data.Map.Strict qualified as Map
import Data.Maybe (fromMaybe)
import Data.Set qualified as Set
import Data.Text (Text)
import Data.Text qualified as Text
import Data.Vector.Storable qualified as VS
import Data.Word (Word64)
import Frp.Apt (FrpEvent, StructJSON (..), Timestamp)
import Frp.Core
import Frp.Core.Fao.Store.Base (FDtypeJson (..), loadFieldDtypes, readDbaAsVectorDouble)
import Frp.DbaStore (loadBitsDba)
import Frp.Instance.ISL.Eaw.Interface.Common
import Frp.Instance.ISL.Eaw.Interface.PreL0 qualified as Spine
import Frp.Instance.ISL.Eaw.P1.Internal.UpstreamReference
import Frp.Instance.ISL.Eaw.P1.Products
import Frp.Instance.ISLTC.Fao (Generic2AdtFao (..))
import GHC.Generics (Generic)
import Reflex (fmapMaybe, mergeMap, mergeWith, never)
import System.Directory (doesFileExist)
import System.FilePath (normalise, (<.>), (</>))

{-# ANN module ("HLint: ignore Redundant bracket" :: String) #-}

type NumericRow = Map Text Double

-- | P1 的 Python DBA 一行就是一条业务 occurrence。平台通用
-- 'genericLoad' 会把一行的每个数值字段分别注册成历史事件；对宽 occurrence
-- 表会按字段数放大底层事件。这里仍读取同一份 fields.json／DBA 文件，但
-- 每个 result key 只注册一条行事件，列只在该行触发时组装成 NumericRow。
data PackedNumericRowsHistoryData = PackedNumericRowsHistoryData
  { packedRowTimestamps :: VS.Vector Timestamp,
    packedRowColumns :: Map Text (VS.Vector Double)
  }

instance HasFrpHistoryTs PackedNumericRowsHistoryData where
  atHistoryTs = packedRowTimestamps

instance HasFrpHistoryData PackedNumericRowsHistoryData NumericRow where
  lookupHistoryData PackedNumericRowsHistoryData {..} index =
    ( packedRowTimestamps VS.! index,
      Map.map (VS.! index) packedRowColumns,
      Nothing
    )

loadPackedNumericRows :: FilePath -> Text -> Map Text Text -> IO PackedNumericRowsHistoryData
loadPackedNumericRows fullDir resultKey fields = do
  timestamps <-
    loadBitsDba @Word64 (fullDir </> Text.unpack (resultKey <> ".__ts__") <.> "dba")
      <&> VS.map convert
  columns <-
    Map.traverseWithKey
      (\field dtype -> readDbaAsVectorDouble fullDir (Text.unpack resultKey <> "." <> Text.unpack field) dtype)
      fields
  let expected = VS.length timestamps
  forM_ (Map.toList columns) $ \(field, values) ->
    unless (VS.length values == expected) $
      error
        ( "P1 packed occurrence row length mismatch: "
            <> Text.unpack resultKey
            <> "."
            <> Text.unpack field
            <> " has "
            <> show (VS.length values)
            <> " values but "
            <> show expected
            <> " timestamps"
        )
  pure (PackedNumericRowsHistoryData timestamps columns)

data P1DecodedIngress value = P1DecodedIngress
  { ingressOccurrences :: FrpEvent [value],
    ingressDiagnostics :: FrpEvent [P1IngressError]
  }

partitionIngressBatch :: [Either P1IngressError value] -> (Maybe [value], Maybe [P1IngressError])
partitionIngressBatch values =
  case partitionEithers values of
    ([], accepted) -> (nonEmpty accepted, Nothing)
    (diagnostics, _rejectedWholeBatch) -> (Nothing, nonEmpty diagnostics)
  where
    nonEmpty items = if null items then Nothing else Just items

readThinProductReceipt :: FilePath -> Text -> IO (Either Text ProductReceipt)
readThinProductReceipt fullDir kind = do
  let receiptPath = fullDir <> "/p1_receipts/" <> Text.unpack kind <> ".json"
  receiptExists <- doesFileExist receiptPath
  if not receiptExists
    then pure (Left ("P1 thin receipt sidecar is missing: " <> kind))
    else do
      receiptResult <- eitherDecodeFileStrict' receiptPath
      pure $ do
        receipt <- either (Left . Text.pack) Right receiptResult
        validateReceiptKind kind receipt

loadProductReceiptFrom :: PyAny -> Text -> FaoModel ProductReceipt
loadProductReceiptFrom source kind = do
  fullDir <- getFullDir source
  result <- liftIO (readThinProductReceipt fullDir kind)
  receipt <- either (error . Text.unpack) pure result
  when
    (normalise (Text.unpack (receiptArtifactLocation receipt)) /= normalise fullDir)
    (error ("P1 thin receipt artifact_location 与实际 Fao source 不一致: " <> fullDir))
  pure receipt

loadGenericArtifact :: (HasHisBack) => PyAny -> Text -> FaoModel GenericFaoResult
loadGenericArtifact source kind = do
  loaded <- genericLoad source
  case loaded of
    Nothing -> do
      fullDir <- getFullDir source
      error (Text.unpack kind <> " requires a committed DBA artifact: " <> fullDir)
    Just generic -> pure generic

loadGenericProduct :: (HasHisBack) => PyAny -> Text -> FaoModel GenericFaoResult
loadGenericProduct source kind = do
  _ <- loadProductReceiptFrom source kind
  loadGenericArtifact source kind

loadPackedProductMetadata :: PyAny -> [Text] -> FaoModel (FilePath, Map Text (Map Text Text))
loadPackedProductMetadata source prefixes = do
  fullDir <- getFullDir source
  metadata <- liftIO (loadFieldDtypes fullDir)
  fields <- maybe (error ("P1 packed occurrence fields.json is missing: " <> fullDir)) pure metadata
  let selected =
        Map.mapMaybe
          ( \case
              FDtypeMapJson nested -> Just nested
              FDtypeTextJson _ -> Nothing
          )
          (Map.filterWithKey (\key _ -> any (`Text.isPrefixOf` key) prefixes) fields)
  when (Map.null selected) $
    error
      ( "P1 packed occurrence product has no matching result key in "
          <> fullDir
          <> ": "
          <> show prefixes
      )
  pure (fullDir, selected)

-- | 同一物理行的全部字段只形成一条历史事件，避免按宽表字段数放大事件数。
loadPackedProductRows :: PyAny -> [Text] -> FaoModel (FrpEvent [(Text, NumericRow)])
loadPackedProductRows source prefixes = do
  (fullDir, groups) <- loadPackedProductMetadata source prefixes
  target <- getTarName source
  events <-
    forM (Map.toList groups) $ \(resultKey, fields) -> do
      let ?hisBack = BackNumber 0
      event <-
        lift $
          newAdtFrpEvent4His @PackedNumericRowsHistoryData @NumericRow
            (packEventName source target ("__eaw_occurrence_row__." <> resultKey))
            (BackNumber 0)
            (loadPackedNumericRows fullDir resultKey fields)
      pure ((\tick -> [(resultKey, atTickValue tick)]) <$> event)
  pure (mergeWith (<>) events)

newtype WallOccurrenceFao = WallOccurrenceFao {wallOccurrenceSource :: PyAny}
  deriving (Generic, Show, PyParams)
  deriving (ToJSON, FromJSON) via (StructJSON WallOccurrenceFao)

data BuildOccurrenceFao = BuildOccurrenceFao
  { buildOccurrenceSource :: PyAny,
    buildWallSource :: PyAny
  }
  deriving (Generic, Show, PyParams)
  deriving (ToJSON, FromJSON) via (StructJSON BuildOccurrenceFao)

data AttackSegmentFao = AttackSegmentFao
  { attackSegmentSource :: PyAny,
    attackSegmentWallSource :: PyAny
  }
  deriving (Generic, Show, PyParams)
  deriving (ToJSON, FromJSON) via (StructJSON AttackSegmentFao)

data FormationEvidenceFao = FormationEvidenceFao
  { formationEvidenceSource :: PyAny,
    formationEvidenceWallSource :: PyAny
  }
  deriving (Generic, Show, PyParams)
  deriving (ToJSON, FromJSON) via (StructJSON FormationEvidenceFao)

data WallBarrierFao = WallBarrierFao
  { wallBarrierSource :: PyAny,
    wallBarrierWallSource :: PyAny
  }
  deriving (Generic, Show, PyParams)
  deriving (ToJSON, FromJSON) via (StructJSON WallBarrierFao)

data AbsorbOccurrenceFao = AbsorbOccurrenceFao
  { absorbOccurrenceSource :: PyAny,
    absorbWallSource :: PyAny
  }
  deriving (Generic, Show, PyParams)
  deriving (ToJSON, FromJSON) via (StructJSON AbsorbOccurrenceFao)

newtype DirectedLargeDealOccurrenceFao = DirectedLargeDealOccurrenceFao
  { directedLargeDealSource :: PyAny
  }
  deriving (Generic, Show, PyParams)
  deriving (ToJSON, FromJSON) via (StructJSON DirectedLargeDealOccurrenceFao)

instance FaoMeta WallOccurrenceFao where
  propTarType = const $ pure (CalendarTarType SymbolType)
  propCalType = const OnlyRead

instance FaoMeta BuildOccurrenceFao where
  propTarType = const $ pure (CalendarTarType SymbolType)
  propCalType = const OnlyRead

instance FaoMeta AttackSegmentFao where
  propTarType = const $ pure (CalendarTarType SymbolType)
  propCalType = const OnlyRead

instance FaoMeta FormationEvidenceFao where
  propTarType = const $ pure (CalendarTarType SymbolType)
  propCalType = const OnlyRead

instance FaoMeta WallBarrierFao where
  propTarType = const $ pure (CalendarTarType SymbolType)
  propCalType = const OnlyRead

instance FaoMeta AbsorbOccurrenceFao where
  propTarType = const $ pure (CalendarTarType SymbolType)
  propCalType = const OnlyRead

instance FaoMeta DirectedLargeDealOccurrenceFao where
  propTarType = const $ pure (CalendarTarType SymbolType)
  propCalType = const OnlyRead

instance Fao WallOccurrenceFao where
  type FaoResult WallOccurrenceFao = GenericFaoResult
  load f = Just <$> loadGenericProduct (wallOccurrenceSource f) "wall_lifecycle"
  dump f _ = error (show (ppname f) <> " is read-only")
  doImpl f = loadGenericProduct (wallOccurrenceSource f) "wall_lifecycle"

instance Fao BuildOccurrenceFao where
  type FaoResult BuildOccurrenceFao = GenericFaoResult
  load f = Just <$> loadGenericProduct (buildOccurrenceSource f) "build_activity"
  dump f _ = error (show (ppname f) <> " is read-only")
  doImpl f = loadGenericProduct (buildOccurrenceSource f) "build_activity"

instance Fao AttackSegmentFao where
  type FaoResult AttackSegmentFao = GenericFaoResult
  load f = Just <$> loadGenericProduct (attackSegmentSource f) "attack_segment"
  dump f _ = error (show (ppname f) <> " is read-only")
  doImpl f = loadGenericProduct (attackSegmentSource f) "attack_segment"

instance Fao FormationEvidenceFao where
  type FaoResult FormationEvidenceFao = GenericFaoResult
  load f = Just <$> loadGenericProduct (formationEvidenceSource f) "attack_formation_evidence"
  dump f _ = error (show (ppname f) <> " is read-only")
  doImpl f = loadGenericProduct (formationEvidenceSource f) "attack_formation_evidence"

instance Fao WallBarrierFao where
  type FaoResult WallBarrierFao = GenericFaoResult
  load f = Just <$> loadGenericProduct (wallBarrierSource f) "wall_relation_barrier"
  dump f _ = error (show (ppname f) <> " is read-only")
  doImpl f = loadGenericProduct (wallBarrierSource f) "wall_relation_barrier"

instance Fao AbsorbOccurrenceFao where
  type FaoResult AbsorbOccurrenceFao = GenericFaoResult
  load f = Just <$> loadGenericProduct (absorbOccurrenceSource f) "absorb_interaction"
  dump f _ = error (show (ppname f) <> " is read-only")
  doImpl f = loadGenericProduct (absorbOccurrenceSource f) "absorb_interaction"

instance Fao DirectedLargeDealOccurrenceFao where
  type FaoResult DirectedLargeDealOccurrenceFao = GenericFaoResult
  load f = Just <$> loadGenericProduct (directedLargeDealSource f) "directed_large_deal_stream"
  dump f _ = error (show (ppname f) <> " is read-only")
  doImpl f = loadGenericProduct (directedLargeDealSource f) "directed_large_deal_stream"

instance FaoRable WallOccurrenceFao

instance FaoRable BuildOccurrenceFao

instance FaoRable AttackSegmentFao

instance FaoRable FormationEvidenceFao

instance FaoRable WallBarrierFao

instance FaoRable AbsorbOccurrenceFao

instance FaoRable DirectedLargeDealOccurrenceFao

groupResultKeyFields :: GenericFaoResult -> Map Text GenericFaoResult
groupResultKeyFields = Map.foldrWithKey addField Map.empty
  where
    addField fullName stream groups =
      let (resultKey, suffix) = Text.breakOn "." fullName
       in if Text.null resultKey || Text.null suffix
            then groups
            else Map.insertWith Map.union resultKey (Map.singleton (Text.drop 1 suffix) stream) groups

mergeGenericFaoRows :: GenericFaoResult -> FrpEvent NumericRow
mergeGenericFaoRows fields = Map.map atTickValue <$> mergeMap fields

required :: Text -> NumericRow -> Either P1IngressError Double
required name row = case Map.lookup name row of
  Nothing -> Left (MissingNumericField name)
  Just value -> finiteNumeric name value

finiteNumeric :: Text -> Double -> Either P1IngressError Double
finiteNumeric name value
  | isNaN value || isInfinite value = Left (NonFiniteNumericField name value)
  | otherwise = Right value

integerValue :: Text -> Double -> Either P1IngressError Int
integerValue name raw = do
  value <- finiteNumeric name raw
  let rounded = round value
  if fromIntegral rounded == value
    then Right rounded
    else Left (NonIntegralNumericField name value)

integer :: Text -> NumericRow -> Either P1IngressError Int
integer name row = required name row >>= integerValue name

int64 :: Text -> NumericRow -> Either P1IngressError Int64
int64 name row = fromIntegral <$> integer name row

nonNegative :: Text -> NumericRow -> Either P1IngressError Double
nonNegative name row = do
  value <- required name row
  if value >= 0 then Right value else Left (InvalidNumericDomain name "must be non-negative")

optionalInteger :: Text -> NumericRow -> Either P1IngressError (Maybe Int)
optionalInteger name row = case Map.lookup name row of
  Nothing -> Right Nothing
  Just value
    | isNaN value || isInfinite value -> Right Nothing
    | otherwise -> Just <$> integer name row

readInt64Text :: Text -> Either P1IngressError Int64
readInt64Text value =
  case reads (Text.unpack value) of
    [(parsed, "")] -> Right parsed
    _ -> Left (InvalidResultKey value)

parseObjectKey :: Text -> Text -> Either P1IngressError Int64
parseObjectKey prefix resultKey =
  case Text.splitOn "__" resultKey of
    [actualPrefix, local] | actualPrefix == prefix -> readInt64Text local
    [actualPrefix, local, ordinal]
      | actualPrefix == prefix && "occ" `Text.isPrefixOf` ordinal -> readInt64Text local
    _ -> Left (InvalidResultKey resultKey)

-- | result key 只描述物理承载。旧 fixture 可把 local number 放在 key 中；
-- 正式紧凑流使用 @prefix__stream[@__occNNNN]@，身份必须来自行字段。
parseObjectTransportKey :: Text -> Text -> Either P1IngressError (Maybe Int64)
parseObjectTransportKey prefix resultKey =
  case Text.splitOn "__" resultKey of
    [actualPrefix, "stream"]
      | actualPrefix == prefix -> Right Nothing
    [actualPrefix, "stream", ordinal]
      | actualPrefix == prefix && validOccurrenceOrdinal ordinal -> Right Nothing
    _ -> Just <$> parseObjectKey prefix resultKey

validOccurrenceOrdinal :: Text -> Bool
validOccurrenceOrdinal value =
  case Text.stripPrefix "occ" value of
    Just digits -> not (Text.null digits) && Text.all isDigit digits
    Nothing -> False

positiveLocalNo :: Text -> Int64 -> Either P1IngressError Int64
positiveLocalNo fieldName value =
  if value > 0
    then Right value
    else Left (InvalidNumericDomain fieldName "must be a positive producer-run local number")

objectLocalNoFromRow :: Text -> Text -> Text -> NumericRow -> Either P1IngressError Int64
objectLocalNoFromRow prefix fieldName resultKey row = do
  keyLocalNo <- parseObjectTransportKey prefix resultKey
  rowLocalNo <- case Map.lookup fieldName row of
    Nothing -> case keyLocalNo of
      Just value -> positiveLocalNo fieldName value
      Nothing -> Left (MissingNumericField fieldName)
    Just _ -> int64 fieldName row >>= positiveLocalNo fieldName
  case keyLocalNo of
    Just value
      | value /= rowLocalNo ->
          Left (InvalidNumericDomain fieldName "row local number does not match legacy result key")
    _ -> Right rowLocalNo

loadWallLocalNumbersFromGroup :: FilePath -> (Text, Map Text Text) -> IO (Either P1IngressError (Set.Set Int64))
loadWallLocalNumbersFromGroup fullDir (resultKey, fields) =
  case Map.lookup "wall_id" fields of
    Nothing ->
      pure $ do
        keyLocalNo <- parseObjectTransportKey "wall" resultKey
        case keyLocalNo of
          Just value -> Set.singleton <$> positiveLocalNo "wall_id" value
          Nothing -> Left (MissingNumericField "wall_id")
    Just dtype -> do
      values <- readDbaAsVectorDouble fullDir (Text.unpack resultKey <> ".wall_id") dtype
      pure $ do
        keyLocalNo <- parseObjectTransportKey "wall" resultKey
        VS.foldl'
          ( \acc raw -> do
              localNumbers <- acc
              localNo <- fromIntegral <$> integerValue "wall_id" raw >>= positiveLocalNo "wall_id"
              case keyLocalNo of
                Just expected
                  | expected /= localNo ->
                      Left (InvalidNumericDomain "wall_id" "row local number does not match legacy result key")
                _ -> Right (Set.insert localNo localNumbers)
          )
          (Right Set.empty)
          values

loadWallIdentityCatalogWithReceipt :: ProductReceipt -> PyAny -> FaoModel WallIdentityCatalog
loadWallIdentityCatalogWithReceipt _receipt _source =
  pure formWallIdentityNamespace

parseRelationKey :: Text -> Text -> Either P1IngressError (Int64, Text)
parseRelationKey prefix resultKey =
  case Text.splitOn "__" resultKey of
    [actualPrefix, wallLocal, direction] | actualPrefix == prefix -> (,direction) <$> readInt64Text wallLocal
    [actualPrefix, wallLocal, direction, ordinal]
      | actualPrefix == prefix && "occ" `Text.isPrefixOf` ordinal -> (,direction) <$> readInt64Text wallLocal
    _ -> Left (InvalidResultKey resultKey)

parseRelationTransportKey :: Text -> Text -> Either P1IngressError (Maybe (Int64, Text))
parseRelationTransportKey prefix resultKey =
  case Text.splitOn "__" resultKey of
    [actualPrefix, "stream"]
      | actualPrefix == prefix -> Right Nothing
    [actualPrefix, "stream", ordinal]
      | actualPrefix == prefix && validOccurrenceOrdinal ordinal -> Right Nothing
    _ -> Just <$> parseRelationKey prefix resultKey

sideName :: Int -> Either P1IngressError Text
sideName 1 = Right "bid"
sideName 2 = Right "ask"
sideName code = Left (UnknownNumericCode "side_code" code)

relationReferenceFromRow :: Text -> Text -> NumericRow -> Either P1IngressError (Int64, Text)
relationReferenceFromRow prefix resultKey row = do
  keyReference <- parseRelationTransportKey prefix resultKey
  wallLocalNo <- case Map.lookup "wall_local_no" row of
    Nothing -> case keyReference of
      Just (value, _) -> positiveLocalNo "wall_local_no" value
      Nothing -> Left (MissingNumericField "wall_local_no")
    Just _ -> int64 "wall_local_no" row >>= positiveLocalNo "wall_local_no"
  directionName <- case Map.lookup "side_code" row of
    Nothing -> case keyReference of
      Just (_, value) | value == "bid" || value == "ask" -> Right value
      Just _ -> Left (InvalidResultKey resultKey)
      Nothing -> Left (MissingNumericField "side_code")
    Just _ -> integer "side_code" row >>= sideName
  case keyReference of
    Just (keyWallLocalNo, keyDirection)
      | keyWallLocalNo /= wallLocalNo || keyDirection /= directionName ->
          Left (InvalidNumericDomain "wall_local_no/side_code" "row relation reference does not match legacy result key")
    _ -> Right (wallLocalNo, directionName)

wallSide :: Int -> Either P1IngressError WallSide
wallSide 1 = Right BidWall
wallSide 2 = Right AskWall
wallSide code = Left (UnknownNumericCode "side_code" code)

aggressorDirection :: Int -> Either P1IngressError AggressorDirection
aggressorDirection 1 = Right AggressiveSell
aggressorDirection 2 = Right AggressiveBuy
aggressorDirection code = Left (UnknownNumericCode "side_code" code)

occurrenceRefFor :: Text -> Int64 -> Int -> Int64 -> OccurrenceRef
occurrenceRefFor productKind localNo uti discriminator =
  OccurrenceRef
    ( productKind
        <> ":"
        <> Text.pack (show localNo)
        <> ":"
        <> Text.pack (show uti)
        <> ":"
        <> Text.pack (show discriminator)
    )

-- | `__occNNNN` 只解决 DBA 同拍物理装箱，不得进入业务 same/new。
transportBaseResultKey :: Text -> Text
transportBaseResultKey resultKey =
  case reverse (Text.splitOn "__" resultKey) of
    ordinal : rest
      | Just digits <- Text.stripPrefix "occ" ordinal,
        not (Text.null digits),
        Text.all isDigit digits,
        not (null rest) ->
          Text.intercalate "__" (reverse rest)
    _ -> resultKey

instrumentFrom :: ProductReceipt -> InstrumentSymbol
instrumentFrom = InstrumentSymbol . targetRef . featureRunIdentityFromFaoContext

wallAvailability :: NumericRow -> Either P1IngressError Spine.WallLifecycleAvailability
wallAvailability row =
  integer "availability_code" row >>= \case
    1 -> Right Spine.WallLifecycleAvailable
    2 -> Right Spine.WallLifecycleSourceMissing
    3 -> Right Spine.WallLifecycleStale
    4 -> Right Spine.WallLifecycleSessionInvalid
    5 -> Right Spine.WallLifecycleCalculationUnavailable
    code -> Left (UnknownNumericCode "availability_code" code)

decodeWallNumericRow :: ProductReceipt -> Text -> NumericRow -> Either P1IngressError WallLifecycleOccurrence
decodeWallNumericRow receipt resultKey row = do
  localNo <- objectLocalNoFromRow "wall" "wall_id" resultKey row
  side <- integer "side_code" row >>= wallSide
  occurredAt <- integer "uti" row
  availability <- wallAvailability row
  unless
    (availability == Spine.WallLifecycleAvailable)
    (Left (InvalidNumericDomain "availability_code" "unavailable Wall source is diagnostic-only and cannot drive lifecycle state"))
  eventCode <- integer "event_type_code" row
  change <-
    if eventCode == 7
      then Spine.WallEnded . Spine.WallEndReason . ("producer-reason-code-" <>) . Text.pack . show <$> integer "reason_code" row
      else do
        low <- required "band_lo" row
        high <- required "band_hi" row
        core <- required "core_price" row
        unless (low <= core && core <= high) (Left (InvalidNumericDomain "wall_band" "band_lo <= core_price <= band_hi is required"))
        presence <-
          integer "status_code" row >>= \case
            1 -> Right Spine.WallAlive
            2 -> Right Spine.WallDormant
            code -> Left (UnknownNumericCode "status_code" code)
        let band = Measured (Spine.WallBand (Spine.Price low) (Spine.Price high) (Spine.Price core))
        case eventCode of
          4 -> Right (Spine.WallStarted band presence)
          5 -> Right (Spine.WallBandUpdated band presence)
          6 -> Right (Spine.WallPresenceChanged band presence)
          code -> Left (UnknownNumericCode "event_type_code" code)
  let identity = WallIdentity localNo
      payload =
        Spine.WallLifecycleEvent
          (wallRefOf identity)
          (instrumentFrom receipt)
          side
          occurredAt
          change
          availability
  pure (WallLifecycleOccurrence identity (occurrenceRefFor "wall" localNo occurredAt (fromIntegral eventCode)) payload)

buildAvailability :: NumericRow -> Either P1IngressError Spine.BuildAvailability
buildAvailability row =
  integer "availability_code" row >>= \case
    1 -> Right Spine.BuildAvailable
    2 -> Right Spine.BuildSourceMissing
    3 -> Right Spine.BuildStale
    4 -> Right Spine.BuildSessionInvalid
    5 -> Right Spine.BuildCalculationUnavailable
    code -> Left (UnknownNumericCode "availability_code" code)

decodeBuildNumericRow :: ProductReceipt -> WallIdentityCatalog -> Text -> NumericRow -> Either P1IngressError BuildActivityOccurrence
decodeBuildNumericRow _receipt wallCatalog resultKey row = do
  localNo <- objectLocalNoFromRow "build" "build_id" resultKey row
  wallLocalNo <- int64 "wall_local_no" row
  occurredAt <- integer "uti" row
  availability <- buildAvailability row
  unless
    (availability == Spine.BuildAvailable)
    (Left (InvalidNumericDomain "availability_code" "unavailable Build calculation is diagnostic-only and cannot drive activity state"))
  cumulative <- Spine.Quantity <$> nonNegative "cum_reload_proxy" row
  continuityCode <- integer "same_band_continuity_code" row
  continuity <-
    if continuityCode == 1
      then either (Left . InvalidNumericDomain "same_band_continuity") Right (mkUnitInterval 1)
      else Left (UnknownNumericCode "same_band_continuity_code" continuityCode)
  let measurements = Spine.BuildMeasurements (Measured cumulative) (Measured continuity)
  eventCode <- integer "event_type_code" row
  change <- case eventCode of
    8 -> Right (Spine.BuildStarted measurements)
    9 -> do
      level <- required "level" row
      milestone <- either (Left . InvalidNumericDomain "level") Right (mkUnitInterval level)
      Right (Spine.BuildReachedMilestone (Spine.BuildMilestone (Text.pack (show level))) (Spine.BuildMilestoneRatio milestone) measurements)
    10 -> Right (Spine.BuildStopped (Spine.BuildStopReason "producer-stop") measurements)
    code -> Left (UnknownNumericCode "event_type_code" code)
  wallIdentity <- validateDependentWallIdentity wallLocalNo wallCatalog
  let identity = BuildActivityIdentity localNo
      payload = Spine.BuildActivityEvent (buildRefOf identity) (wallRefOf wallIdentity) occurredAt change availability
  pure (BuildActivityOccurrence identity wallIdentity (occurrenceRefFor "build" localNo occurredAt (fromIntegral eventCode)) payload)

attackLanes :: Int -> Either P1IngressError Spine.AttackLaneQualification
attackLanes 1 = Right Spine.TacticalLaneOnly
attackLanes 2 = Right Spine.StructuralLaneOnly
attackLanes 3 = Right Spine.TacticalAndStructuralLanes
attackLanes code = Left (UnknownNumericCode "lane_mask" code)

qualifiedUtisFromRows :: Int64 -> [NumericRow] -> Either P1IngressError [Int]
qualifiedUtisFromRows segmentId rows = do
  decoded <- traverse decodeRow rows
  let ordered = sortOn fst decoded
      ordinals = fmap fst ordered
  unless
    (ordinals == [0 .. length ordinals - 1])
    (Left (InvalidNumericDomain "qualified_uti.ordinal" "must start at zero and be contiguous"))
  pure (fmap snd ordered)
  where
    decodeRow row = do
      owner <- int64 "segment_id" row
      unless
        (owner == segmentId)
        (Left (InvalidNumericDomain "qualified_uti.segment_id" "does not match the segment main row"))
      (,) <$> integer "ordinal" row <*> integer "qualified_uti" row

qualificationHitsFromRows :: AttackFormationMethodSnapshot -> Int64 -> [NumericRow] -> Either P1IngressError [F4QualificationHit]
qualificationHitsFromRows snapshot segmentId rows = do
  decoded <- traverse decodeRow rows
  let ordered = sortOn fst decoded
      ordinals = fmap fst ordered
  unless
    (ordinals == [0 .. length ordinals - 1])
    (Left (InvalidNumericDomain "qualification_hit.ordinal" "must start at zero and be contiguous"))
  pure (fmap snd ordered)
  where
    decodeRow row = do
      owner <- int64 "segment_id" row
      unless
        (owner == segmentId)
        (Left (InvalidNumericDomain "qualification_hit.segment_id" "does not match the segment main row"))
      ordinal <- integer "ordinal" row
      streamOrdinal <- integer "selected_stream_ordinal" row
      familyCode <- integer "qualification_family_code" row
      gradeValue <- integer "grade" row
      _ <- case drop streamOrdinal (selectedF4Streams snapshot) of
        _value : _ -> Right ()
        [] -> Left (InvalidNumericDomain "selected_stream_ordinal" "selected F4 stream ordinal is out of range")
      let family = case familyCode of
            1 -> "tactical"
            2 -> "structural"
            _ -> "family-code-" <> Text.pack (show familyCode)
      pure (ordinal, F4QualificationHit streamOrdinal familyCode family gradeValue)

attackSegmentAvailability :: Int -> Either P1IngressError (AttackSegmentAvailability, Maybe Text)
attackSegmentAvailability 1 = Right (AttackSegmentAvailable, Nothing)
attackSegmentAvailability 2 = Right (AttackSegmentTechnicalTruncated, Just "producer-reported-technical-truncation")
attackSegmentAvailability 3 = Right (AttackSegmentUnavailable, Just "producer-reported-unavailable")
attackSegmentAvailability code = Left (UnknownNumericCode "availability_code" code)

-- | 从逐资格族命中形成公共 AttackSegment 中每条 lane 的实际最高档位。
-- 不从旧的合并 max_grade 反推，也不把未参与或不可用编码成零。
laneGradeObservation ::
  Spine.AttackLaneQualification ->
  AttackSegmentAvailability ->
  Int ->
  [F4QualificationHit] ->
  Either P1IngressError Spine.LaneGradeObservation
laneGradeObservation lanes availability familyCode hits
  | not participates && not (null grades) =
      Left (InvalidNumericDomain "qualification_hits" "lane mask excludes a qualification family carried by the segment")
  | not participates = Right Spine.LaneAbsent
  | availability /= AttackSegmentAvailable = Right Spine.LaneUnavailable
  | null grades =
      Left (InvalidNumericDomain "qualification_hits" "lane mask requires a qualification family missing from the segment")
  | any (<= 0) grades =
      Left (InvalidNumericDomain "qualification_hits" "qualification grade must be positive")
  | otherwise =
      Spine.LaneObserved
        <$> either
          (Left . InvalidNumericDomain "qualification_hits")
          Right
          (Spine.mkPositiveGrade (maximum grades))
  where
    grades =
      [ qualificationGrade hit
        | hit <- hits,
          qualificationFamilyCode hit == familyCode
      ]
    participates = case (lanes, familyCode) of
      (Spine.TacticalLaneOnly, 1) -> True
      (Spine.StructuralLaneOnly, 2) -> True
      (Spine.TacticalAndStructuralLanes, 1) -> True
      (Spine.TacticalAndStructuralLanes, 2) -> True
      _ -> False

decodeAttackSegmentNumericRow :: ProductReceipt -> WallIdentityCatalog -> Text -> NumericRow -> [NumericRow] -> [NumericRow] -> Either P1IngressError AttackSegmentAtWall
decodeAttackSegmentNumericRow receipt wallCatalog resultKey row qualifiedRows qualificationHitRows = do
  unless
    (transportBaseResultKey resultKey == "segment__stream")
    (Left (InvalidResultKey resultKey))
  localNo <- int64 "segment_id" row
  when
    (localNo <= 0)
    (Left (InvalidNumericDomain "segment_id" "must be a positive producer-run local number"))
  attemptLocalNo <- int64 "attack_segment_attempt_local_id" row
  when
    (attemptLocalNo <= 0 || attemptLocalNo /= localNo)
    (Left (InvalidNumericDomain "attack_segment_attempt_local_id" "must be positive and equal to segment_id"))
  wallLocalNo <- int64 "wall_local_no" row
  sideCode <- integer "side_code" row
  side <- wallSide sideCode
  direction <- aggressorDirection sideCode
  start <- integer "start_uti" row
  businessEnd <- integer "business_end_uti" row
  closedAt <- integer "closed_at_uti" row
  timeSpan <- either (Left . InvalidNumericDomain "attack_segment_time_span") Right (Spine.mkAttackSegmentTimeSpan start businessEnd closedAt)
  closeCode <- integer "close_reason_code" row
  lanes <- integer "lane_mask" row >>= attackLanes
  count <- integer "hit_occurrence_count_v0" row >>= either (Left . InvalidNumericDomain "hit_occurrence_count_v0") Right . Spine.mkOccurrenceCount
  qualifiedUtis <- qualifiedUtisFromRows localNo qualifiedRows
  expectedCount <- integer "occurrence_utis_count" row
  unless (expectedCount == length qualifiedUtis) (Left (QualifiedUtiCountMismatch expectedCount (length qualifiedUtis)))
  qualified <- case qualifiedUtis of
    [] -> Left (InvalidNumericDomain "qualified_utis" "complete segment requires at least one qualified UTI")
    first : rest -> either (Left . InvalidNumericDomain "qualified_utis") Right (Spine.mkQualifiedOccurrenceUtis (first :| rest))
  amount <- nonNegative "amount_total_v0" row
  maxGrade <- integer "max_grade" row
  entry <- required "entry_price" row
  exitPrice <- required "exit_price" row
  minPrice <- required "min_price" row
  maxPrice <- required "max_price" row
  load <-
    Spine.AttackSegmentLoad count
      <$> (Spine.Quantity <$> nonNegative "directional_hit_volume_proxy_total_v0" row)
      <*> pure (Measured (Spine.Amount amount))
      <*> (Spine.Quantity <$> nonNegative "vol_tactical_overlap_view" row)
      <*> (Spine.Quantity <$> nonNegative "vol_structural_overlap_view" row)
      <*> (Spine.Quantity <$> nonNegative "largest_directional_hit_volume_proxy_v0" row)
      <*> pure (Measured maxGrade)
  pricePath <-
    Spine.AttackSegmentPricePath
      (Measured (Spine.Price entry))
      (Measured (Spine.Price exitPrice))
      (Measured (Spine.Price minPrice))
      (Measured (Spine.Price maxPrice))
      . Measured
      . Spine.TickDistance
      <$> integer "net_progress_ticks" row
      <*> (Measured . Spine.TickDistance <$> integer "max_retreat_from_best_ticks" row)
  proximity <-
    Spine.AttackSegmentProximity
      <$> (Spine.TickDistance <$> integer "max_dist_deal_to_core_ticks" row)
      <*> (Spine.TickDistance <$> integer "last_dist_deal_to_core_ticks" row)
      <*> (Measured . Spine.TickDistance <$> integer "max_wall_core_shift_ticks" row)
  methodSnapshot <- either (const (Left MissingAttackMethodSnapshot)) Right (attackFormationMethodSnapshotFromReceipt receipt)
  qualificationHits <- qualificationHitsFromRows methodSnapshot localNo qualificationHitRows
  when (null qualificationHits) (Left (InvalidNumericDomain "qualification_hits" "complete segment requires selected F4 qualification evidence"))
  when
    (any (\hit -> qualificationFamilyCode hit /= 1 && qualificationFamilyCode hit /= 2) qualificationHits)
    (Left (InvalidNumericDomain "qualification_hits" "only tactical and structural qualification families may enter a canonical AttackSegment"))
  (availability, unavailableReason) <- integer "availability_code" row >>= attackSegmentAvailability
  tacticalGrade <- laneGradeObservation lanes availability 1 qualificationHits
  structuralGrade <- laneGradeObservation lanes availability 2 qualificationHits
  when
    (maxGrade /= maximum (map qualificationGrade qualificationHits))
    (Left (InvalidNumericDomain "max_grade" "diagnostic max_grade does not equal the maximum preserved lane qualification grade"))
  wallIdentity <- validateDependentWallIdentity wallLocalNo wallCatalog
  let identity = AttackSegmentIdentity localNo
      attemptIdentity = AttackSegmentAttemptIdentity attemptLocalNo
      payload =
        Spine.AttackSegmentAtWall
          (attackSegmentRefOf identity)
          (attackSegmentAttemptRefOf attemptIdentity)
          (instrumentFrom receipt)
          (wallRefOf wallIdentity)
          side
          direction
          timeSpan
          (Spine.AttackSegmentCloseReason ("producer-close-code-" <> Text.pack (show closeCode)))
          lanes
          tacticalGrade
          structuralGrade
          load
          pricePath
          proximity
          (Measured qualified)
          Spine.HalfSecondOccurrenceCountV0
          Spine.PredictedDirectionalHitVolumePerHalfSecondV0
  pure
    ( AttackSegmentAtWall
        identity
        wallIdentity
        (occurrenceRefFor "attack-segment" localNo closedAt 5)
        qualificationHits
        availability
        unavailableReason
        payload
    )

formationAvailability :: Int -> Either P1IngressError Spine.AttackFormationAvailability
formationAvailability 1 = Right Spine.FormationMaterialAvailable
formationAvailability 2 = Right Spine.FormationSourceMissing
formationAvailability 3 = Right Spine.FormationStale
formationAvailability 4 = Right Spine.FormationUnavailableFromCurrentProducer
formationAvailability 5 = Right Spine.FormationOrderUnresolved
formationAvailability 6 = Right Spine.FormationUnavailableFromCurrentProducer
formationAvailability code = Left (UnknownNumericCode "availability_code" code)

formationEvidenceAvailability :: Int -> Either P1IngressError FormationEvidenceAvailability
formationEvidenceAvailability 1 = Right FormationEvidenceAvailable
formationEvidenceAvailability 2 = Right FormationEvidenceMissing
formationEvidenceAvailability 3 = Right FormationEvidenceStale
formationEvidenceAvailability 4 = Right FormationEvidenceSessionInvalid
formationEvidenceAvailability 5 = Right FormationEvidenceUnavailable
formationEvidenceAvailability 6 = Right FormationEvidenceUnavailable
formationEvidenceAvailability code = Left (UnknownNumericCode "availability_code" code)

formationEvidenceKind :: Int -> Int -> Either P1IngressError FormationEvidenceKind
formationEvidenceKind 1 _ = Right AcceptedMaterialEvidence
formationEvidenceKind 2 5 = Right SameUtiOrderUnresolvedEvidence
formationEvidenceKind 2 _ = Right CapabilityUnavailableEvidence
formationEvidenceKind 3 _ = Right OrdinaryGapBreakEvidence
formationEvidenceKind 4 _ = Right ObservedNoAcceptedAttackIntervalEvidence
formationEvidenceKind 5 _ = Right AvailabilityIntervalSummaryEvidence
formationEvidenceKind 6 _ = Right CapabilityUnavailableEvidence
formationEvidenceKind code _ = Left (UnknownNumericCode "body_kind_code" code)

formationReasonText :: Int -> Int -> Int -> Maybe Text
formationReasonText 1 _ _ = Nothing
formationReasonText 2 2 _ = Just "same_uti_order_unresolved"
formationReasonText 2 3 _ = Just "wall_switch_without_formal_barrier_source"
formationReasonText 2 4 _ = Just "side_switch_without_formal_barrier_source"
formationReasonText 3 _ _ = Just "ordinary_gap"
formationReasonText 4 _ _ = Just "observed_no_accepted_attack_interval"
formationReasonText 5 _ 2 = Just "source_missing_interval"
formationReasonText 5 _ 3 = Just "stale_interval"
formationReasonText 5 _ 4 = Just "session_invalid_interval"
formationReasonText 5 _ _ = Just "availability_interval"
formationReasonText 6 6 _ = Just "near_miss_not_observed_current_v0"
formationReasonText 6 7 _ = Just "retreat_trace_unavailable_current_v0"
formationReasonText 6 8 _ = Just "band_shift_trace_unavailable_current_v0"
formationReasonText 6 _ _ = Just "formation_capability_unavailable_current_v0"
formationReasonText _ reasonCode _ = Just ("producer-reason-code-" <> Text.pack (show reasonCode))

formationInterval :: Int -> Int -> NumericRow -> Either P1IngressError (Int, Int)
formationInterval bodyCode occurredAt row = do
  startValue <- optionalInteger "interval_start_uti" row
  endValue <- optionalInteger "interval_end_uti" row
  (start, end) <- case (startValue, endValue) of
    (Just start, Just end) -> Right (start, end)
    (Nothing, Nothing)
      | bodyCode == 4 || bodyCode == 5 || bodyCode == 6 -> Left (MissingNumericField "interval_start_uti/interval_end_uti")
      | otherwise -> Right (occurredAt, occurredAt)
    _ -> Left (MissingNumericField "interval_start_uti/interval_end_uti")
  unless (start <= end) (Left (InvalidNumericDomain "formation_interval" "start_uti must not follow end_uti"))
  unless (occurredAt == end) (Left (InvalidNumericDomain "formation_interval" "occurrence UTI must equal interval end"))
  Right (start, end)

decodeAttackFormationNumericRow :: ProductReceipt -> WallIdentityCatalog -> Text -> NumericRow -> Either P1IngressError AttackFormationMaterialOccurrence
decodeAttackFormationNumericRow receipt wallCatalog resultKey row = do
  (wallLocalNo, directionName) <- relationReferenceFromRow "formation" resultKey row
  direction <- case directionName of
    "bid" -> Right AggressiveSell
    "ask" -> Right AggressiveBuy
    _ -> Left (InvalidResultKey resultKey)
  occurredAt <- integer "uti" row
  availabilityCode <- integer "availability_code" row
  availability <- formationAvailability availabilityCode
  handoffAvailability <- formationEvidenceAvailability availabilityCode
  sourceLocal <- int64 "source_material_local_ref" row
  localNo <- int64 "formation_local_id" row
  attemptLocalNo <- int64 "attack_segment_attempt_local_id" row
  availableAt <- integer "available_at_uti" row
  reasonCode <- integer "reason_code" row
  bodyCode <- integer "body_kind_code" row
  evidenceKind <- formationEvidenceKind bodyCode availabilityCode
  (intervalStart, intervalEnd) <- formationInterval bodyCode occurredAt row
  when
    (availableAt < intervalEnd)
    (Left (InvalidNumericDomain "available_at_uti" "must not precede the business interval end"))
  let attemptRequired =
        bodyCode == 1
          || bodyCode == 3
          || (bodyCode == 2 && (reasonCode == 3 || reasonCode == 4))
  when
    (attemptRequired && attemptLocalNo <= 0)
    (Left (InvalidNumericDomain "attack_segment_attempt_local_id" "this FormationEvidence must name its AttackSegment attempt"))
  when
    (not attemptRequired && attemptLocalNo /= 0)
    (Left (InvalidNumericDomain "attack_segment_attempt_local_id" "this FormationEvidence must not claim an AttackSegment attempt"))
  wallIdentity <- validateDependentWallIdentity wallLocalNo wallCatalog
  let attemptRef =
        if attemptLocalNo > 0
          then Just (attackSegmentAttemptRefOf (AttackSegmentAttemptIdentity attemptLocalNo))
          else Nothing
      sourceRef = SourceMaterialRef ("p1-formation-source:" <> Text.pack (show sourceLocal))
      reasonText = formationReasonText bodyCode reasonCode availabilityCode
      reason = Spine.AttackFormationReason (fromMaybe ("producer-reason-code-" <> Text.pack (show reasonCode)) reasonText)
  body <- case bodyCode of
    1 -> Right (Spine.AcceptedFormationMaterial (Spine.FormationLargeDealSource (LargeDealEventRef ("f4:" <> Text.pack (show sourceLocal)))))
    2 -> Right (Spine.UnresolvedFormationMaterial reason (Just sourceRef))
    3 -> Right (Spine.MethodLocalGapBreak reason (Just sourceRef))
    4 -> Right (Spine.ObservedNoAcceptedAttackInterval (Spine.AttackFormationReason "observed-no-accepted-attack-interval") (Just sourceRef))
    5 -> Right (Spine.ExcludedFormationMaterial reason (Just sourceRef))
    6 -> Right (Spine.ExcludedFormationMaterial reason (Just sourceRef))
    code -> Left (UnknownNumericCode "body_kind_code" code)
  let material =
        Spine.AttackFormationMaterial
          (AttackFormationScopeRef ("attack-formation:" <> Text.pack (show wallLocalNo)))
          (wallRefOf wallIdentity)
          (instrumentFrom receipt)
          direction
          occurredAt
          availability
          body
      ref = occurrenceRefFor "attack-formation" localNo occurredAt (fromIntegral bodyCode)
  pure
    ( AttackFormationMaterialOccurrence
        wallIdentity
        ref
        attemptRef
        evidenceKind
        intervalStart
        intervalEnd
        availableAt
        handoffAvailability
        reasonText
        material
    )

decodeWallBarrierNumericRow :: ProductReceipt -> WallIdentityCatalog -> Text -> NumericRow -> Either P1IngressError WallAttackBarrierOccurrence
decodeWallBarrierNumericRow _receipt wallCatalog resultKey row = do
  (wallLocalNo, directionName) <- relationReferenceFromRow "barrier" resultKey row
  direction <- case directionName of
    "bid" -> Right AggressiveSell
    "ask" -> Right AggressiveBuy
    _ -> Left (InvalidResultKey resultKey)
  localNo <- int64 "barrier_local_id" row
  sourceLocal <- int64 "source_material_local_ref" row
  occurredAt <- integer "uti" row
  kind <-
    integer "barrier_kind_code" row >>= \case
      1 -> Right Spine.WallEndedBarrier
      code -> Left (InvalidNumericDomain "barrier_kind_code" ("current producer has no formal source contract for code " <> Text.pack (show code)))
  wallIdentity <- validateDependentWallIdentity wallLocalNo wallCatalog
  let ref = occurrenceRefFor "wall-attack-barrier" localNo occurredAt 1
      payload =
        Spine.WallAttackBarrier
          (BarrierRef ("barrier:" <> Text.pack (show localNo)))
          (AttackFormationScopeRef ("attack-formation:" <> Text.pack (show wallLocalNo)))
          (wallRefOf wallIdentity)
          direction
          occurredAt
          kind
          (SourceMaterialRef ("p1-barrier-source:" <> Text.pack (show sourceLocal)))
  pure (WallAttackBarrierOccurrence wallIdentity ref payload)

absorbAvailability :: NumericRow -> Either P1IngressError Spine.AbsorbAvailability
absorbAvailability row =
  integer "availability_code" row >>= \case
    1 -> Right Spine.AbsorbAvailable
    2 -> Right Spine.AbsorbSourceMissing
    3 -> Right Spine.AbsorbStale
    5 -> Right Spine.AbsorbCalculationUnavailable
    code -> Left (UnknownNumericCode "availability_code" code)

decodeAbsorbNumericRow :: ProductReceipt -> WallIdentityCatalog -> Text -> NumericRow -> Either P1IngressError AbsorbInteractionOccurrence
decodeAbsorbNumericRow _receipt wallCatalog resultKey row = do
  localNo <- objectLocalNoFromRow "absorb" "track_id" resultKey row
  wallLocalNo <- int64 "wall_local_no" row
  occurredAt <- integer "uti" row
  availability <- absorbAvailability row
  measurements <-
    Spine.AbsorbMeasurements
      <$> (Measured . Spine.Quantity <$> nonNegative "consumed_proxy_cum" row)
      <*> (Measured . Spine.Quantity <$> nonNegative "replenishment_proxy" row)
      <*> (Measured . Spine.TickDistance <$> integer "price_progress_ticks" row)
  eventCode <- integer "event_type_code" row
  (change, occurrenceKind, milestoneLevel, resolvedReason) <- case eventCode of
    11 -> Right (Spine.AbsorbInteractionStarted measurements, AbsorbStartedOccurrence, Nothing, Nothing)
    12 -> do
      level <- required "level" row
      _ <- either (Left . InvalidNumericDomain "level") Right (mkUnitInterval level)
      Right (Spine.AbsorbConsumptionMilestone measurements, AbsorbConsumptionMilestoneOccurrence, Just level, Nothing)
    13 -> do
      resolutionCode <- integer "resolved_type_code" row
      reason <- case resolutionCode of
        1 -> Right "breakthrough"
        2 -> Right "aborted"
        3 -> Right "blocked"
        code -> Left (UnknownNumericCode "resolved_type_code" code)
      Right (Spine.AbsorbInteractionResolved (Spine.AbsorbResolution reason) measurements, AbsorbResolvedOccurrence, Nothing, Just reason)
    code -> Left (UnknownNumericCode "event_type_code" code)
  wallIdentity <- validateDependentWallIdentity wallLocalNo wallCatalog
  let identity = AbsorbInteractionIdentity localNo
      payload = Spine.AbsorbInteractionEvent (absorbRefOf identity) (wallRefOf wallIdentity) occurredAt change availability
  pure
    ( AbsorbInteractionOccurrence
        identity
        wallIdentity
        (occurrenceRefFor "absorb" localNo occurredAt (fromIntegral eventCode))
        occurrenceKind
        milestoneLevel
        resolvedReason
        payload
    )

decodeDirectedLargeDealNumericRow :: ProductReceipt -> Text -> NumericRow -> Either P1IngressError DirectedLargeDealOccurrence
decodeDirectedLargeDealNumericRow receipt resultKey row = do
  localNo <- int64 "producer_local_no" row
  occurredAt <- integer "uti" row
  qualification <- integer "qualification_code" row
  unless (qualification == 1) (Left (InvalidNumericDomain "qualification_code" "quarantine row cannot enter public F4 port"))
  direction <- case head (Text.splitOn "__" resultKey) of
    "buy" -> Right AggressiveBuy
    "sell" -> Right AggressiveSell
    _ -> Left (InvalidResultKey resultKey)
  laneCode <- integer "lane_code" row
  lanes <- attackLanes laneCode
  selectedGrade <- integer "grade" row
  volume <- nonNegative "directional_hit_volume_proxy" row
  amount <- nonNegative "deal_amt" row
  family <- maybe (Left (InvalidNumericDomain "qualification_family" "thin receipt must name the selected family")) Right (receiptBusinessParameterText "qualification_family" receipt)
  familyCode <- integer "qualification_family_code" row
  let expectedFamilyCode
        | family == "tactical" = 1
        | family == "structural" = 2
        | otherwise = 3
  unless (familyCode == expectedFamilyCode && laneCode == expectedFamilyCode) $
    Left (InvalidNumericDomain "qualification_family_code" "row lane/family must match the selected Feature instance")
  let measuredGrade = Measured (Spine.LargeDealLaneGrade (Text.pack (show selectedGrade)))
      unavailableGrade = MeasurementUnavailable "other-qualification-family"
      laneGrades
        | family == "tactical" = Spine.LargeDealLaneQualification lanes measuredGrade unavailableGrade
        | family == "structural" = Spine.LargeDealLaneQualification lanes unavailableGrade measuredGrade
        | otherwise = Spine.LargeDealLaneQualification lanes unavailableGrade unavailableGrade
      ref = occurrenceRefFor "f4" localNo occurredAt (fromIntegral familyCode)
      payload =
        Spine.DirectedLargeDealEvent
          (LargeDealEventRef (unOccurrenceRef ref))
          (instrumentFrom receipt)
          occurredAt
          direction
          laneGrades
          (Spine.Quantity volume)
          (Spine.Amount amount)
          (MethodRef ("f4-method:" <> family))
          Spine.DirectedLargeDealAvailable
  pure (DirectedLargeDealOccurrence localNo ref family selectedGrade payload)

data AttackSegmentTransportKind
  = AttackSegmentMainRow
  | AttackSegmentQualifiedUtiRow
  | AttackSegmentQualificationHitRow
  deriving (Eq, Ord, Show)

attackSegmentTransportKind :: Text -> Maybe AttackSegmentTransportKind
attackSegmentTransportKind resultKey =
  case transportBaseResultKey resultKey of
    "segment__stream" -> Just AttackSegmentMainRow
    "segment_qualified_uti__stream" -> Just AttackSegmentQualifiedUtiRow
    "segment_qualification_hit__stream" -> Just AttackSegmentQualificationHitRow
    _ -> Nothing

type AttackSegmentTransportBucket = ([(Text, NumericRow)], [NumericRow], [NumericRow])

decodeAttackSegmentTransportBatch :: ProductReceipt -> WallIdentityCatalog -> [(Text, NumericRow)] -> [Either P1IngressError AttackSegmentAtWall]
decodeAttackSegmentTransportBatch receipt wallCatalog transportRows =
  case partitionEithers (fmap classify transportRows) of
    (errors@(_ : _), _) -> fmap Left errors
    ([], classified) -> fmap decodeBucket (Map.toAscList (foldr addRow Map.empty classified))
  where
    classify :: (Text, NumericRow) -> Either P1IngressError (Int64, AttackSegmentTransportKind, Text, NumericRow)
    classify (resultKey, row) = do
      kind <- maybe (Left (InvalidResultKey resultKey)) Right (attackSegmentTransportKind resultKey)
      segmentId <- int64 "segment_id" row
      when
        (segmentId <= 0)
        (Left (InvalidNumericDomain "segment_id" "must be a positive producer-run local number"))
      pure (segmentId, kind, resultKey, row)

    addRow :: (Int64, AttackSegmentTransportKind, Text, NumericRow) -> Map Int64 AttackSegmentTransportBucket -> Map Int64 AttackSegmentTransportBucket
    addRow (segmentId, kind, resultKey, row) =
      Map.insertWith mergeBucket segmentId (oneRow kind resultKey row)

    oneRow :: AttackSegmentTransportKind -> Text -> NumericRow -> AttackSegmentTransportBucket
    oneRow AttackSegmentMainRow resultKey row = ([(resultKey, row)], [], [])
    oneRow AttackSegmentQualifiedUtiRow _ row = ([], [row], [])
    oneRow AttackSegmentQualificationHitRow _ row = ([], [], [row])

    mergeBucket :: AttackSegmentTransportBucket -> AttackSegmentTransportBucket -> AttackSegmentTransportBucket
    mergeBucket (newMain, newQualified, newHits) (oldMain, oldQualified, oldHits) =
      (newMain <> oldMain, newQualified <> oldQualified, newHits <> oldHits)

    decodeBucket :: (Int64, AttackSegmentTransportBucket) -> Either P1IngressError AttackSegmentAtWall
    decodeBucket (_segmentId, ([(resultKey, row)], qualifiedRows, qualificationHitRows)) =
      decodeAttackSegmentNumericRow
        receipt
        wallCatalog
        resultKey
        row
        qualifiedRows
        qualificationHitRows
    decodeBucket (segmentId, ([], _, _)) =
      Left
        ( InvalidNumericDomain
            "attack_segment_transport"
            ("segment " <> Text.pack (show segmentId) <> " has detail rows but no main row")
        )
    decodeBucket (segmentId, (_duplicateMainRows, _, _)) =
      Left
        ( InvalidNumericDomain
            "attack_segment_transport"
            ("segment " <> Text.pack (show segmentId) <> " has multiple main rows in one occurrence batch")
        )

decodeAttackSegmentStreamsWithDiagnostics :: ProductReceipt -> WallIdentityCatalog -> GenericFaoResult -> P1DecodedIngress AttackSegmentAtWall
decodeAttackSegmentStreamsWithDiagnostics receipt wallCatalog generic =
  let groups =
        [ (key, fields)
          | (key, fields) <- Map.toList (groupResultKeyFields generic),
            "segment" `Text.isPrefixOf` key
        ]
      streams =
        [ (\row -> [(key, row)]) <$> mergeGenericFaoRows fields
          | (key, fields) <- groups
        ]
      decoded = case streams of
        [] -> never
        _ -> decodeAttackSegmentTransportBatch receipt wallCatalog <$> mergeWith (<>) streams
      accepted = fst . partitionIngressBatch
      rejected = snd . partitionIngressBatch
   in P1DecodedIngress
        { ingressOccurrences = fmapMaybe accepted decoded,
          ingressDiagnostics = fmapMaybe rejected decoded
        }

decodeGroupsWithDiagnostics :: Text -> (Text -> NumericRow -> Either P1IngressError a) -> GenericFaoResult -> P1DecodedIngress a
decodeGroupsWithDiagnostics prefix decoder generic =
  let groups =
        [ (key, fields)
          | (key, fields) <- Map.toList (groupResultKeyFields generic),
            prefix `Text.isPrefixOf` key
        ]
      streams =
        [ (\row -> [decoder key row]) <$> mergeGenericFaoRows fields
          | (key, fields) <- groups
        ]
      decoded = case streams of
        [] -> never
        _ -> mergeWith (<>) streams
      accepted = fst . partitionIngressBatch
      rejected = snd . partitionIngressBatch
   in P1DecodedIngress
        { ingressOccurrences = fmapMaybe accepted decoded,
          ingressDiagnostics = fmapMaybe rejected decoded
        }

decodeGroups :: Text -> (Text -> NumericRow -> Either P1IngressError a) -> GenericFaoResult -> FrpEvent [a]
decodeGroups prefix decoder = ingressOccurrences . decodeGroupsWithDiagnostics prefix decoder

decodePackedRowsWithDiagnostics ::
  (Text -> NumericRow -> Either P1IngressError value) ->
  FrpEvent [(Text, NumericRow)] ->
  P1DecodedIngress value
decodePackedRowsWithDiagnostics decoder rows =
  P1DecodedIngress
    { ingressOccurrences = fmapMaybe (fst . partitionIngressBatch) decoded,
      ingressDiagnostics = fmapMaybe (snd . partitionIngressBatch) decoded
    }
  where
    decoded = fmap (fmap (uncurry decoder)) rows

decodePackedAttackRowsWithDiagnostics ::
  ProductReceipt ->
  WallIdentityCatalog ->
  FrpEvent [(Text, NumericRow)] ->
  P1DecodedIngress AttackSegmentAtWall
decodePackedAttackRowsWithDiagnostics receipt wallCatalog rows =
  P1DecodedIngress
    { ingressOccurrences = fmapMaybe (fst . partitionIngressBatch) decoded,
      ingressDiagnostics = fmapMaybe (snd . partitionIngressBatch) decoded
    }
  where
    decoded = decodeAttackSegmentTransportBatch receipt wallCatalog <$> rows

toWallLifecycleIngress :: ProductReceipt -> GenericFaoResult -> FaoModel (P1DecodedIngress WallLifecycleOccurrence)
toWallLifecycleIngress receipt generic = pure (decodeGroupsWithDiagnostics "wall__" (decodeWallNumericRow receipt) generic)

toWallLifecycleOccurrences :: ProductReceipt -> GenericFaoResult -> FaoModel (FrpEvent [WallLifecycleOccurrence])
toWallLifecycleOccurrences receipt generic = ingressOccurrences <$> toWallLifecycleIngress receipt generic

wallIdentityCatalogFromArtifact :: ProductReceipt -> GenericFaoResult -> Either P1IngressError WallIdentityCatalog
wallIdentityCatalogFromArtifact _wallReceipt generic = do
  localNumbers <- traverse (parseObjectKey "wall") wallKeys
  pure (formWallIdentityCatalog (Set.toList (Set.fromList localNumbers)))
  where
    wallKeys = filter ("wall__" `Text.isPrefixOf`) (Map.keys (groupResultKeyFields generic))

dependentWallContext :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> Either P1IngressError WallIdentityCatalog
dependentWallContext dependent wallReceipt wallGeneric = do
  _ <- validateExactUpstreamReceipt "wall_lifecycle" dependent wallReceipt
  wallIdentityCatalogFromArtifact wallReceipt wallGeneric

loadPackedDependentWallContext :: ProductReceipt -> ProductReceipt -> PyAny -> FaoModel WallIdentityCatalog
loadPackedDependentWallContext dependent wallReceipt wallSource = do
  _ <-
    either
      (error . show)
      pure
      (validateExactUpstreamReceipt "wall_lifecycle" dependent wallReceipt)
  loadWallIdentityCatalogWithReceipt wallReceipt wallSource

loadWallIdentityCatalogFrom :: PyAny -> FaoModel WallIdentityCatalog
loadWallIdentityCatalogFrom source = do
  receipt <- loadProductReceiptFrom source "wall_lifecycle"
  loadWallIdentityCatalogWithReceipt receipt source

toBuildActivityIngress :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (P1DecodedIngress BuildActivityOccurrence)
toBuildActivityIngress receipt wallReceipt generic wallGeneric = do
  catalog <- either (error . show) pure (dependentWallContext receipt wallReceipt wallGeneric)
  pure (decodeGroupsWithDiagnostics "build__" (decodeBuildNumericRow receipt catalog) generic)

toBuildActivityOccurrences :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (FrpEvent [BuildActivityOccurrence])
toBuildActivityOccurrences receipt wallReceipt generic wallGeneric = ingressOccurrences <$> toBuildActivityIngress receipt wallReceipt generic wallGeneric

toAttackSegmentIngress :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (P1DecodedIngress AttackSegmentAtWall)
toAttackSegmentIngress receipt wallReceipt generic wallGeneric = do
  catalog <- either (error . show) pure (dependentWallContext receipt wallReceipt wallGeneric)
  pure (decodeAttackSegmentStreamsWithDiagnostics receipt catalog generic)

toAttackSegmentOccurrences :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (FrpEvent [AttackSegmentAtWall])
toAttackSegmentOccurrences receipt wallReceipt generic wallGeneric = ingressOccurrences <$> toAttackSegmentIngress receipt wallReceipt generic wallGeneric

toFormationEvidenceIngress :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (P1DecodedIngress AttackFormationMaterialOccurrence)
toFormationEvidenceIngress receipt wallReceipt generic wallGeneric = do
  catalog <- either (error . show) pure (dependentWallContext receipt wallReceipt wallGeneric)
  pure (decodeGroupsWithDiagnostics "formation__" (decodeAttackFormationNumericRow receipt catalog) generic)

toFormationEvidenceOccurrences :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (FrpEvent [AttackFormationMaterialOccurrence])
toFormationEvidenceOccurrences receipt wallReceipt generic wallGeneric = ingressOccurrences <$> toFormationEvidenceIngress receipt wallReceipt generic wallGeneric

toWallBarrierIngress :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (P1DecodedIngress WallAttackBarrierOccurrence)
toWallBarrierIngress receipt wallReceipt generic wallGeneric = do
  catalog <- either (error . show) pure (dependentWallContext receipt wallReceipt wallGeneric)
  pure (decodeGroupsWithDiagnostics "barrier__" (decodeWallBarrierNumericRow receipt catalog) generic)

toWallBarrierOccurrences :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (FrpEvent [WallAttackBarrierOccurrence])
toWallBarrierOccurrences receipt wallReceipt generic wallGeneric = ingressOccurrences <$> toWallBarrierIngress receipt wallReceipt generic wallGeneric

toAbsorbInteractionIngress :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (P1DecodedIngress AbsorbInteractionOccurrence)
toAbsorbInteractionIngress receipt wallReceipt generic wallGeneric = do
  catalog <- either (error . show) pure (dependentWallContext receipt wallReceipt wallGeneric)
  pure (decodeGroupsWithDiagnostics "absorb__" (decodeAbsorbNumericRow receipt catalog) generic)

toAbsorbInteractionOccurrences :: ProductReceipt -> ProductReceipt -> GenericFaoResult -> GenericFaoResult -> FaoModel (FrpEvent [AbsorbInteractionOccurrence])
toAbsorbInteractionOccurrences receipt wallReceipt generic wallGeneric = ingressOccurrences <$> toAbsorbInteractionIngress receipt wallReceipt generic wallGeneric

toDirectedLargeDealOccurrences :: ProductReceipt -> GenericFaoResult -> FaoModel (FrpEvent [DirectedLargeDealOccurrence])
toDirectedLargeDealOccurrences receipt generic =
  pure
    ( decodeGroups
        ""
        (decodeDirectedLargeDealNumericRow receipt)
        ( Map.filterWithKey
            (\key _ -> "buy" `Text.isPrefixOf` key || "sell" `Text.isPrefixOf` key)
            generic
        )
    )

validateAttackProductInputs :: AttackSegmentFao -> FormationEvidenceFao -> WallBarrierFao -> FaoModel ()
validateAttackProductInputs segment formation barrier = do
  segmentReceipt <- loadProductReceiptFrom (attackSegmentSource segment) "attack_segment"
  formationReceipt <- loadProductReceiptFrom (formationEvidenceSource formation) "attack_formation_evidence"
  barrierReceipt <- loadProductReceiptFrom (wallBarrierSource barrier) "wall_relation_barrier"
  either
    (error . show)
    pure
    (validateAttackProductReceiptSet segmentReceipt formationReceipt barrierReceipt)

instance Generic2AdtFao WallOccurrenceFao (FrpEvent [WallLifecycleOccurrence]) where
  runFao2Adt f = ingressOccurrences <$> wallOccurrenceIngress f

instance Generic2AdtFao BuildOccurrenceFao (FrpEvent [BuildActivityOccurrence]) where
  runFao2Adt f = ingressOccurrences <$> buildOccurrenceIngress f

instance Generic2AdtFao AttackSegmentFao (FrpEvent [AttackSegmentAtWall]) where
  runFao2Adt f = ingressOccurrences <$> attackSegmentIngress f

instance Generic2AdtFao FormationEvidenceFao (FrpEvent [AttackFormationMaterialOccurrence]) where
  runFao2Adt f = ingressOccurrences <$> formationEvidenceIngress f

instance Generic2AdtFao WallBarrierFao (FrpEvent [WallAttackBarrierOccurrence]) where
  runFao2Adt f = ingressOccurrences <$> wallBarrierIngress f

instance Generic2AdtFao AbsorbOccurrenceFao (FrpEvent [AbsorbInteractionOccurrence]) where
  runFao2Adt f = ingressOccurrences <$> absorbOccurrenceIngress f

instance Generic2AdtFao DirectedLargeDealOccurrenceFao (FrpEvent [DirectedLargeDealOccurrence]) where
  runFao2Adt f = do
    receipt <- loadProductReceiptFrom (directedLargeDealSource f) "directed_large_deal_stream"
    rows <- loadPackedProductRows (directedLargeDealSource f) ["buy", "sell"]
    pure
      ( ingressOccurrences
          (decodePackedRowsWithDiagnostics (decodeDirectedLargeDealNumericRow receipt) rows)
      )

wallOccurrenceEvent :: WallOccurrenceFao -> FaoModel (FrpEvent [WallLifecycleOccurrence])
wallOccurrenceEvent = runFao2Adt

wallOccurrenceIngress :: WallOccurrenceFao -> FaoModel (P1DecodedIngress WallLifecycleOccurrence)
wallOccurrenceIngress f = do
  receipt <- loadProductReceiptFrom (wallOccurrenceSource f) "wall_lifecycle"
  rows <- loadPackedProductRows (wallOccurrenceSource f) ["wall__"]
  pure (decodePackedRowsWithDiagnostics (decodeWallNumericRow receipt) rows)

buildOccurrenceEvent :: BuildOccurrenceFao -> FaoModel (FrpEvent [BuildActivityOccurrence])
buildOccurrenceEvent = runFao2Adt

buildOccurrenceIngress :: BuildOccurrenceFao -> FaoModel (P1DecodedIngress BuildActivityOccurrence)
buildOccurrenceIngress f = snd <$> buildOccurrenceIngressWithCatalog f

buildOccurrenceIngressWithCatalog :: BuildOccurrenceFao -> FaoModel (WallIdentityCatalog, P1DecodedIngress BuildActivityOccurrence)
buildOccurrenceIngressWithCatalog f = do
  receipt <- loadProductReceiptFrom (buildOccurrenceSource f) "build_activity"
  wallReceipt <- loadProductReceiptFrom (buildWallSource f) "wall_lifecycle"
  catalog <- loadPackedDependentWallContext receipt wallReceipt (buildWallSource f)
  rows <- loadPackedProductRows (buildOccurrenceSource f) ["build__"]
  pure (catalog, decodePackedRowsWithDiagnostics (decodeBuildNumericRow receipt catalog) rows)

attackSegmentEvent :: AttackSegmentFao -> FaoModel (FrpEvent [AttackSegmentAtWall])
attackSegmentEvent = runFao2Adt

attackSegmentIngress :: AttackSegmentFao -> FaoModel (P1DecodedIngress AttackSegmentAtWall)
attackSegmentIngress f = do
  receipt <- loadProductReceiptFrom (attackSegmentSource f) "attack_segment"
  wallReceipt <- loadProductReceiptFrom (attackSegmentWallSource f) "wall_lifecycle"
  catalog <- loadPackedDependentWallContext receipt wallReceipt (attackSegmentWallSource f)
  rows <- loadPackedProductRows (attackSegmentSource f) ["segment"]
  pure (decodePackedAttackRowsWithDiagnostics receipt catalog rows)

attackProductIngresses ::
  AttackSegmentFao ->
  FormationEvidenceFao ->
  WallBarrierFao ->
  FaoModel
    ( WallIdentityCatalog,
      P1DecodedIngress AttackSegmentAtWall,
      P1DecodedIngress AttackFormationMaterialOccurrence,
      P1DecodedIngress WallAttackBarrierOccurrence
    )
attackProductIngresses segment formation barrier = do
  segmentReceipt <- loadProductReceiptFrom (attackSegmentSource segment) "attack_segment"
  formationReceipt <- loadProductReceiptFrom (formationEvidenceSource formation) "attack_formation_evidence"
  barrierReceipt <- loadProductReceiptFrom (wallBarrierSource barrier) "wall_relation_barrier"
  either
    (error . show)
    pure
    (validateAttackProductReceiptSet segmentReceipt formationReceipt barrierReceipt)
  segmentWallReceipt <- loadProductReceiptFrom (attackSegmentWallSource segment) "wall_lifecycle"
  formationWallReceipt <- loadProductReceiptFrom (formationEvidenceWallSource formation) "wall_lifecycle"
  barrierWallReceipt <- loadProductReceiptFrom (wallBarrierWallSource barrier) "wall_lifecycle"
  unless
    (segmentWallReceipt == formationWallReceipt && segmentWallReceipt == barrierWallReceipt)
    (error "Attack 三个输入没有指向同一个 exact Wall artifact")
  catalog <-
    loadPackedDependentWallContext segmentReceipt segmentWallReceipt (attackSegmentWallSource segment)
  _ <- either (error . show) pure (validateExactUpstreamReceipt "wall_lifecycle" formationReceipt formationWallReceipt)
  _ <- either (error . show) pure (validateExactUpstreamReceipt "wall_lifecycle" barrierReceipt barrierWallReceipt)
  segmentRows <- loadPackedProductRows (attackSegmentSource segment) ["segment"]
  formationRows <- loadPackedProductRows (formationEvidenceSource formation) ["formation__"]
  barrierRows <- loadPackedProductRows (wallBarrierSource barrier) ["barrier__"]
  pure
    ( catalog,
      decodePackedAttackRowsWithDiagnostics segmentReceipt catalog segmentRows,
      decodePackedRowsWithDiagnostics (decodeAttackFormationNumericRow formationReceipt catalog) formationRows,
      decodePackedRowsWithDiagnostics (decodeWallBarrierNumericRow barrierReceipt catalog) barrierRows
    )

formationEvidenceEvent :: FormationEvidenceFao -> FaoModel (FrpEvent [AttackFormationMaterialOccurrence])
formationEvidenceEvent = runFao2Adt

formationEvidenceIngress :: FormationEvidenceFao -> FaoModel (P1DecodedIngress AttackFormationMaterialOccurrence)
formationEvidenceIngress f = do
  receipt <- loadProductReceiptFrom (formationEvidenceSource f) "attack_formation_evidence"
  wallReceipt <- loadProductReceiptFrom (formationEvidenceWallSource f) "wall_lifecycle"
  catalog <- loadPackedDependentWallContext receipt wallReceipt (formationEvidenceWallSource f)
  rows <- loadPackedProductRows (formationEvidenceSource f) ["formation__"]
  pure (decodePackedRowsWithDiagnostics (decodeAttackFormationNumericRow receipt catalog) rows)

wallBarrierEvent :: WallBarrierFao -> FaoModel (FrpEvent [WallAttackBarrierOccurrence])
wallBarrierEvent = runFao2Adt

wallBarrierIngress :: WallBarrierFao -> FaoModel (P1DecodedIngress WallAttackBarrierOccurrence)
wallBarrierIngress f = do
  receipt <- loadProductReceiptFrom (wallBarrierSource f) "wall_relation_barrier"
  wallReceipt <- loadProductReceiptFrom (wallBarrierWallSource f) "wall_lifecycle"
  catalog <- loadPackedDependentWallContext receipt wallReceipt (wallBarrierWallSource f)
  rows <- loadPackedProductRows (wallBarrierSource f) ["barrier__"]
  pure (decodePackedRowsWithDiagnostics (decodeWallBarrierNumericRow receipt catalog) rows)

absorbOccurrenceEvent :: AbsorbOccurrenceFao -> FaoModel (FrpEvent [AbsorbInteractionOccurrence])
absorbOccurrenceEvent = runFao2Adt

absorbOccurrenceIngress :: AbsorbOccurrenceFao -> FaoModel (P1DecodedIngress AbsorbInteractionOccurrence)
absorbOccurrenceIngress f = snd <$> absorbOccurrenceIngressWithCatalog f

absorbOccurrenceIngressWithCatalog :: AbsorbOccurrenceFao -> FaoModel (WallIdentityCatalog, P1DecodedIngress AbsorbInteractionOccurrence)
absorbOccurrenceIngressWithCatalog f = do
  receipt <- loadProductReceiptFrom (absorbOccurrenceSource f) "absorb_interaction"
  wallReceipt <- loadProductReceiptFrom (absorbWallSource f) "wall_lifecycle"
  catalog <- loadPackedDependentWallContext receipt wallReceipt (absorbWallSource f)
  rows <- loadPackedProductRows (absorbOccurrenceSource f) ["absorb__"]
  pure (catalog, decodePackedRowsWithDiagnostics (decodeAbsorbNumericRow receipt catalog) rows)

directedLargeDealEvent :: DirectedLargeDealOccurrenceFao -> FaoModel (FrpEvent [DirectedLargeDealOccurrence])
directedLargeDealEvent = runFao2Adt
