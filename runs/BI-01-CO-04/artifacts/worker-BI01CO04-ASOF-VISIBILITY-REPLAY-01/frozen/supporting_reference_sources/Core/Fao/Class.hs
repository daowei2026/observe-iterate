{-# LANGUAGE AllowAmbiguousTypes #-}
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE DefaultSignatures #-}
{-# LANGUAGE DerivingVia #-}
{-# LANGUAGE ImplicitParams #-}
{-# LANGUAGE UndecidableInstances #-}

-- | 对应 python 端 Fao
module Frp.Core.Fao.Class
  ( GenericFaoResult,
    GenericFaoResult',
    CalType (..),

    -- * FaoModel
    withSymbol,
    withSymbols,
    withBlock,
    withBlocks,
    withTarget,
    withCalendar,
    currentCalendar,
    currentCalendar',
    currentSymbol,
    currentSymbol',
    currentSymbols,
    CurrTargetEnv,
    curr'target,
    curr'symbol'target,
    curr'block'target,
    curr'calendar'target,
    DumpContext (..),
    withEventDumpEnv,
    curr'dump'context,
    modify'curr'dump'fields,
    curr'dump'fields,
    FaoModel,
    evalFaoModel,
    FaoMeta (..),
    Fao
      ( getParamPath,
        getParamId,
        getFullDir,
        getAllFullDirs,
        getGFullDir,
        getSymbols,
        getTarName,
        getTarNameNoCalendar,
        getTarType,
        getUniqueId,
        getFaoConstr,
        ppname,
        ggjson,
        load,
        dump,
        doImpl,
        runFao,
        runFaoBack,
        runFaoBack',
        FaoResult
      ),
    packEventName,
    HisBack (..),
    HasHisBack,
    getHisBack,

    -- * run
    runFaoProperty,
    runFaoHistory,
    runFaoHistory',
    runFaoRealTime,
    runFaoModelWith,
    runFaoEventModel,
    runFunctionEventModel,
    mergeTarType,
    mergeFaoTarType,

    -- * new event
    newFrpEvent,
    newFrpEvent4Fao,
    newFrpEvent4Fao',
    newBitsFrpEvent,
    newAutoNamedBitsFrpEvent,
    newBitsFrpEvent4Fao,
    newBitsFrpEvent4Fao',
    newAdtFrpEvent,
    newAdtFrpEvent4Fao,
    newAdtFrpEvent4Fao',
    newAdtFrpEvent4His,
    forceLoadSourceEvent,
    forceLoadSourceEvents,
  )
where

import Control.Lens hiding (from, (<.>))
import Control.Monad.Extra
import Control.Monad.IO.Class
import Control.Monad.RWS.Lazy
import Control.Monad.Ref
import Data.Aeson hiding (Object)
import Data.ByteString.Lazy qualified as B
import Data.ByteString.Lazy.Char8 qualified as BL
import Data.Convertible
import Data.Data
import Data.Default
import Data.IORef
import Data.List
import Data.Map.Strict (Map)
import Data.Map.Strict qualified as Map
import Data.Maybe
import Data.Set qualified as Set
import Data.Text (Text)
import Data.Text qualified as T
import Data.UUID (toString,toText)
import Data.UUID.V4
import Database.MongoDB ((=:))
import Database.MongoDB qualified as MDB
import Event.Analytics.EHI
import Foreign hiding (void)
import Frp.Apt
import Frp.Core.Engine
import Frp.Core.Fao.Store.Base
import Frp.DbaStore.Class
import Frp.DbaStore.Internal
import GHC.Generics
import GHC.Types
import Reflex hiding (HList, HNil)
import Reflex.Host.Class
import System.Directory
import System.FilePath

-----------------
-- 通用特征结果，一个字段一个事件
-----------------

type GenericFaoResult = FieldMap (FrpEvent TickDouble)

type GenericFaoResult' = FieldMap (FrpEvent Double)

-- | 唯一ID
type UniqueId = Text

-- | 计算类型
data CalType
  = -- 特征可以设置的类型
    Cal -- 本特征重新计算,不读取,不保存
  | Cache -- 本特征先读取特征数据库,如果没有则重新计算并保存
  | OnlyRead -- 本特征只读
  -- 运行 Fao 时可以设置的类型
  | Gen -- 本特征重新计算并保存
  | AllGen -- 所有特征重新计算并保存
  | AllCal -- 所有特征都重新计算不保存 OnlyRead 除外
  deriving (Eq, Ord, Show, Generic)

instance Convertible Text CalType where
  safeConvert "Cal" = return Cal
  safeConvert "Cache" = return Cache
  safeConvert "OnlyRead" = return OnlyRead
  safeConvert "Gen" = return Gen
  safeConvert "AllGen" = return AllGen
  safeConvert "AllCal" = return AllCal
  safeConvert v = error $ "no support CalType:" ++ show v

isCalType :: CalType -> Bool
isCalType Cal = True
isCalType AllCal = True
isCalType _ = False

-- | 当前环境下的目标对象
data CurrTargetEnv = CurrTargetEnv
  { _curr'target :: Target,
    _curr'symbol'target :: Maybe Target,
    _curr'block'target :: Maybe Target,
    _curr'calendar'target :: Maybe Target,
    _curr'cal'type :: (String, CalType)
  }
  deriving (Show)

instance Default CurrTargetEnv where def = CurrTargetEnv (Symbol "") Nothing Nothing Nothing ("", Cal)

makeLenses ''CurrTargetEnv

data DumpContext = DumpContext
  { dump_unique_id :: UniqueId,
    dump_fao_name :: Text,
    dump_full_dirs :: [FilePath],
    dump_fields :: FieldMap (Text, IO (Int, Maybe Text)) -- 字段类型，保存函数 IO(数据长度，是否有价格)
  }

newtype FaoState = FaoState
  { 
    _curr'store'contexts :: [DumpContext]
  }
  deriving (Generic)

instance Default FaoState where
  def = FaoState []

makeLenses ''FaoState

newtype FaoModelT t m a = FaoModelT
  { unFaoModelT :: RWST CurrTargetEnv () FaoState m a
  }
  deriving (Functor, Applicative, Monad, MonadFix, MonadIO, MonadRef, MonadTrans, MonadReader CurrTargetEnv, MonadState FaoState)

-- | 类似 python 端的 CurrSymbol 环境
--
-- 基于相同参数的 Fao ，在不同目标对象(品种)下结果不一样
type FaoModel = FaoModelT FrpEngine AppModel

evalFaoModel :: (Monad m) => CurrTargetEnv -> FaoState -> FaoModelT t m a -> m a
evalFaoModel r s app = evalRWST (unFaoModelT app) r s <&> fst

evalFaoModel_ :: (Monad m) => CurrTargetEnv -> FaoState -> FaoModelT t m a -> m ()
evalFaoModel_ r s app = void $ evalRWST (unFaoModelT app) r s

instance AppModelQuery FaoModel

-------------------
-- FaoModelT reflex instance
-------------------

instance (MonadReflexCreateTrigger t m) => MonadReflexCreateTrigger t (FaoModelT t m) where
  newEventWithTrigger = lift . newEventWithTrigger
  newFanEventWithTrigger f = lift $ newFanEventWithTrigger f

instance (PerformEvent t m) => PerformEvent t (FaoModelT t m) where
  type Performable (FaoModelT t m) = FaoModelT t (Performable m)
  performEvent_ e = do
    r <- ask
    s <- get
    lift $ performEvent_ $ evalFaoModel r s <$> e
  performEvent e = do
    r <- ask
    s <- get
    lift $ performEvent $ evalFaoModel r s <$> e

instance (TriggerEvent t m) => TriggerEvent t (FaoModelT t m) where
  newTriggerEvent = lift newTriggerEvent
  newTriggerEventWithOnComplete = lift newTriggerEventWithOnComplete
  newEventWithLazyTriggerWithOnComplete = lift . newEventWithLazyTriggerWithOnComplete

instance (PostBuild t m) => PostBuild t (FaoModelT t m) where
  getPostBuild = lift getPostBuild

instance (MonadSample t m) => MonadSample t (FaoModelT t m) where
  sample = lift . sample

instance (MonadHold t m) => MonadHold t (FaoModelT t m) where
  hold a0 = lift . hold a0
  holdDyn a0 = lift . holdDyn a0
  holdIncremental a0 = lift . holdIncremental a0
  buildDynamic a0 = lift . buildDynamic a0
  headE = lift . headE

instance (Adjustable t m) => Adjustable t (FaoModelT t m) where
  runWithReplace a0 a' = do
    r <- ask
    s <- get
    lift $ runWithReplace (evalFaoModel r s a0) $ fmap (evalFaoModel r s) a'
  traverseIntMapWithKeyWithAdjust f dm0 dm' = do
    r <- ask
    s <- get
    lift $ traverseIntMapWithKeyWithAdjust (\k v -> evalFaoModel r s (f k v)) dm0 dm'
  traverseDMapWithKeyWithAdjust f dm0 dm' = do
    r <- ask
    s <- get
    lift $ traverseDMapWithKeyWithAdjust (\k v -> evalFaoModel r s (f k v)) dm0 dm'
  traverseDMapWithKeyWithAdjustWithMove f dm0 dm' = do
    r <- ask
    s <- get
    lift $ traverseDMapWithKeyWithAdjustWithMove (\k v -> evalFaoModel r s (f k v)) dm0 dm'

instance (NotReady t m) => NotReady t (FaoModelT r m) where
  notReadyUntil = lift . notReadyUntil
  notReady = lift notReady

-- | 在某个品种上下文下
withSymbol :: Sym -> FaoModel a -> FaoModel a
withSymbol sym = withTarget (Symbol sym)

-- | 遍历品种集，得到每个品种的 Fao 模型结果
withSymbols :: Symbols -> FaoModel a -> FaoModel (Map Sym a)
withSymbols syms model = do
  res <- forM syms $ \sym -> do
    v <- withSymbol sym model
    return (sym, v)
  return $ Map.fromList res

-- | 在某个板块上下文环境
class WithBlock a where
  withBlock :: a -> FaoModel b -> FaoModel b

class HasTextBlockExpr a where
  atTextBlockExpr :: a -> TextBlockExpr

instance HasTextBlockExpr TextBlockExpr where
  atTextBlockExpr = id

instance HasTextBlockExpr BlockExpr where
  atTextBlockExpr = blk_expr

instance WithBlock TextBlockExpr where
  -- t 板块表达式: 如 ask@default blk@black steel rb|j|i rb&j&i
  withBlock t = withBlock (convert t :: BlockExpr)

instance WithBlock BlockExpr where
  withBlock (AskBlockExpr expr _) = \model -> do
    sym <- currentSymbol
    withTarget (AskBlock expr sym) model
  withBlock (FixedBlockExpr expr _) = withTarget (FixedBlock expr)
  withBlock (StkTlistExpr expr) = withTarget (FixedBlock expr)
  withBlock (SymbolsOrExpr expr _) = withTarget (FixedBlock expr)
  withBlock (SymbolsAndExpr expr _) = withTarget (FixedBlock expr)

-- | 遍历板块集，得到每个板块的 Fao 模型结果
withBlocks :: (WithBlock a, Ord a, HasTextBlockExpr a) => [a] -> FaoModel b -> FaoModel (Map TextBlockExpr b)
withBlocks blks model = do
  res <- forM blks $ \blk -> do
    v <- withBlock blk model
    return (atTextBlockExpr blk, v)
  return $ Map.fromList res

-- 先修改当前目标环境
updateCurrTargetEnv :: CurrTargetEnv -> Target -> CurrTargetEnv
updateCurrTargetEnv curr tar =
  curr
    & curr'target .~ tar
    & curr'symbol'target .~ _parseSymTar tar
    & curr'block'target .~ _parseBlockTar tar -- (if isBlockTarget tar then Just tar else curr ^. curr'block'target)
    & curr'calendar'target .~ (if isJust (maybeCalendarTarget tar) then Just tar else curr ^. curr'calendar'target)
  where
    _parseSymTar t@(Symbol _) = Just t
    _parseSymTar (CalendarTarget _ t) = _parseSymTar t
    _parseSymTar (AskBlock _ sym) = Just $ Symbol sym
    _parseSymTar _ = curr ^. curr'symbol'target

    _parseBlockTar (CalendarTarget _ t) = _parseBlockTar t
    _parseBlockTar b@(AskBlock _ _) = Just b
    _parseBlockTar b@(FixedBlock _) = Just b
    _parseBlockTar b@(BlockSet _) = Just b
    _parseBlockTar _ = curr ^. curr'block'target

-- | 在某个目标对象下
withTarget :: Target -> FaoModel a -> FaoModel a
withTarget tar model = do
  r <- ask
  s <- get
  let r' = updateCurrTargetEnv r tar
  lift $ evalFaoModel r' s model

-- | 在某个日历上下文下
withCalendar :: CalendarName -> FaoModel a -> FaoModel a
withCalendar c m = do
  tar <- view curr'target
  case tar of
    CalendarTarget _ t -> withTarget (CalendarTarget c t) m
    t -> withTarget (CalendarTarget c t) m

-- | 安全的获取当前日历名称
currentCalendar' :: FaoModel (Maybe CalendarName)
currentCalendar' = view curr'calendar'target <&> (>>= maybeCalendarTarget)

-- | 获取当前日历名称
currentCalendar :: FaoModel CalendarName
currentCalendar = do
  msym <- currentCalendar'
  case msym of
    Nothing -> error "No current calendar in context"
    Just c -> return c

-- | 安全的获取当前品种
currentSymbol' :: FaoModel (Maybe Sym)
currentSymbol' = view curr'symbol'target <&> (>>= maybeSymbolTarget)

-- | 获取当前品种
currentSymbol :: FaoModel Sym
currentSymbol = do
  msym <- currentSymbol'
  case msym of
    Nothing -> error "No current symbol in context"
    Just sym -> return sym

-- | 获取当前环境目标对象类型
currentTarType :: FaoModel TarType
currentTarType = view curr'target <&> targetToTarType

-- | 获取当前环境品种集
currentSymbols :: FaoModel Symbols
currentSymbols = currentTarType >>= loadTarTypeSymbols

-- | 通过 TarType 获取品种集
loadTarTypeSymbols :: TarType -> FaoModel Symbols
loadTarTypeSymbols = \case
  -- 单品种, 获取 sof 中 stk_tlist 中的所有品种
  SymbolType -> lift $ view (env'ctx . ctx'sof . sof'stk_tlist) >>= loadStkTlistSymbols
  BlockType (AskBlockExpr _ name) -> do
    sym <- currentSymbol
    loadAskBlockSymblos sym name
  BlockType (FixedBlockExpr _ blk) -> loadFixedBlockSymbols blk
  BlockType (StkTlistExpr expr) -> loadStkTlistSymbols expr
  BlockType (SymbolsOrExpr _ syms) -> return syms
  BlockType (SymbolsAndExpr _ syms) -> return syms
  UnknownBlockType -> do
    mtar <- view curr'block'target
    case mtar of
      Nothing -> error "No current block in context"
      Just tar -> loadTarTypeSymbols $ targetToTarType tar
  BlockSetType (fmap BlockType -> types) -> do
    xs <- mapM loadTarTypeSymbols types
    return . Set.toList . Set.fromList $ concat xs
  RunTimeTarType -> error "RunTimeTarType cannot get symbols"
  FuncTarType -> error "FuncTarType cannot get symbols"
  CalendarTarType t -> loadTarTypeSymbols t

-- | 对应 python 端的 Meta 内部类
class FaoMeta f where
  -- | 特征计算类型, 特征默认 Cache
  propCalType :: f -> CalType
  propCalType = const Cache

  -- | Fao的目标对象类型
  --
  -- 支持通过判断上下文信息(如 currentCalendar)来设置 TarType
  propTarType :: f -> FaoModel TarType

  -- | 文件夹路径是否包含 Sof 起止日期,默认包含
  -- 与 python 端 prop_on_date_range 名称对应
  propOnDateRange :: f -> Bool
  propOnDateRange = const True

-- | 特征对象接口 ,与 python 端同名
class (FaoMeta f) => Fao f where
  -- \| 特征名+参数ID
  --   ppid :: f -> Text
  --   ppid f = ppname f <> T.pack (getParamId f)

  -- ggjson 的 sha1 值
  getParamId :: f -> String
  getParamId = encodeSha1 . BL.unpack . ggjson

  -- 和 python 端一致 将路径分为 8 份
  getParamPath :: f -> String
  getParamPath f =
    let (b1, b2) = splitAt 8 $ getParamId f
     in intersperse '/' b1 <> b2

  -- 根路径
  getStoreDir :: f -> FaoModel FilePath
  getStoreDir f = lift $ do
    -- TODO
    sof <- view (env'ctx . ctx'sof)
    store_dirs <- view (env'ctx . ctx'store'dirs)
    let res = Map.findWithDefault (sof ^. sof'store_dir) (ppname f) store_dirs
    return $ head res

  -- | 通过起止日期创建没有 store_dir 的路径  
  createHeadLessFullDir :: f -> Maybe Text -> Maybe Text -> FaoModel FilePath
  createHeadLessFullDir f mstart mend= do
    sof <- lift $ view (env'ctx . ctx'sof)
    let sof_path = (sof ^. sof'category) </> T.unpack (sof ^. sof'name) </> (sof ^. sof'store_name)
    ename <- lift $ view (env'ctx . ctx'app'config . env'name)

    let cls_name = T.unpack $ ppname f
    tar_name <- getTarName f <&> T.unpack

    -- 是否包含起止日期
    if propOnDateRange f
      then do
        -- Tensor 时期遗留的逻辑，兼容已保存数据
        -- startDay + OPT_HOUR_STR 
        let shour = view sof'opt_start_hour sof 
            ehour = view sof'opt_end_hour sof

        let _parse (Just start) Nothing = Just $ start <> " " <> shour <> "~None"
            _parse Nothing (Just end) = Just $ "None~" <> end <> " " <> ehour
            _parse (Just start) (Just end) = Just $ start <> " " <> shour <> "~" <> end <> " " <> ehour
            _parse _ _ = Nothing

        -- 将日期范围添加到路径中，与 python 端一致
        case _parse mstart mend of
          Nothing -> return $ sof_path </> ename </> cls_name </> getParamPath f </> tar_name
          Just dkey -> return $ sof_path </> ename </> T.unpack dkey </> cls_name </> getParamPath f </> tar_name
      else return $ sof_path </> ename </> cls_name </> getParamPath f </> tar_name

  createFullDir :: f -> Maybe Text -> Maybe Text -> FaoModel FilePath
  createFullDir f mstart mend= do
    store_dir <- getStoreDir f
    param_dir <- createHeadLessFullDir f mstart mend
    return (store_dir </> param_dir)

  -- | 获取优化查询起止日期范围路径  
  getGFullDir :: f -> FaoModel (Maybe FilePath)
  getGFullDir f = do
    -- 是否包含起止日期
    if propOnDateRange f then do
        mperiod <- lift $ view (env'ctx . ctx'sof . sof'full_period)
        case mperiod of 
            Nothing -> return Nothing 
            Just (mstart,mend) -> createFullDir f mstart mend <&> Just
    else return Nothing

  -- 特征当前目标全路径
  getFullDir :: f -> FaoModel FilePath
  getFullDir f = do
    sof <- lift $ view (env'ctx . ctx'sof)
    let mstart = view sof'startDay sof
        mend = view sof'endDay sof
    createFullDir f mstart mend

  -- 特征所有保存路径
  getAllFullDirs :: f -> FaoModel [FilePath]
  getAllFullDirs f = do
    sof <- lift $ view (env'ctx . ctx'sof)
    store_dirs <- lift $ view (env'ctx . ctx'store'dirs)
    let xs = Map.findWithDefault (sof ^. sof'store_dir) (ppname f) store_dirs
    let mstart = view sof'startDay sof
        mend = view sof'endDay sof
    param_dir <- createHeadLessFullDir f mstart mend
    return $ fmap (</> param_dir) xs
    
   -- 包含参数和目标对象的唯一ID
  getUniqueId :: f -> FaoModel UniqueId
  getUniqueId f = do
    sof <- lift $ view (env'ctx . ctx'sof)
    let mstart = view sof'startDay sof
        mend = view sof'endDay sof
    param_dir <- createHeadLessFullDir f mstart mend
    return $ T.pack (encodeSha1 param_dir)

  -- | 根据Fao的目标对象类型获取当前目标对象名称
  getTarName :: f -> FaoModel TarName
  getTarName f = do
    tarType <- getTarType f
    tname <- getTarNameNoCalendar f
    case tarType of
      CalendarTarType t -> do
        mtar <- view curr'calendar'target
        case mtar of
          Nothing -> error "No current calendar in context"
          Just (maybeCalendarTarget -> mcalendar) ->
            case mcalendar of
              Nothing -> error "No current calendar in context"
              Just AtSelfCalendar -> return tname
              Just c -> do
                return $ tname <> "." <> convert c
      _ -> return tname
    
  -- | 根据Fao的目标对象类型获取当前没有日历名称的目标对象名称
  getTarNameNoCalendar :: f -> FaoModel TarName
  getTarNameNoCalendar f = do
    tarType <- getTarType f
    case tarType of
      CalendarTarType t -> go t
      _ -> go tarType
    where
      go = \case
        RunTimeTarType -> do
          tar <- view curr'target
          parseTarName tar
        SymbolType -> do
          mtar <- view curr'symbol'target
          case mtar of
            Nothing -> error "No current symbol in context"
            Just tar@(maybeSymbolTarget -> b) -> if isJust b then parseTarName tar else error "No current symbol in context"
        BlockType (AskBlockExpr expr _) -> do
          mtar <- view curr'symbol'target
          case mtar of
            Nothing -> error "No current symbol in context"
            Just (maybeSymbolTarget -> msym) ->
              case msym of
                Nothing -> error "No current symbol in context"
                Just sym -> parseTarName $ AskBlock expr sym
        UnknownBlockType -> do
          mtar <- view curr'block'target
          case mtar of
            Nothing -> error "No current block in context"
            Just tar@(isBlockTarget -> b) -> if b then parseTarName tar else error "No current block in context"

        -- 固定的
        BlockType expr -> return $ blk_expr expr
        BlockSetType exprs -> parseTarName (BlockSet $ fmap blk_expr exprs)
        FuncTarType -> return "func"
        CalendarTarType _ -> error "CalendarTarType 中不能嵌套 CalendarTarType"

  getFaoConstr :: f -> Text
  default getFaoConstr :: (Typeable f) => f -> Text
  getFaoConstr = typeConstrOf

  -- | 运行特征, 获取当前目标对象结果,历史数据不回溯
  runFao :: (Typeable (FaoResult f)) => f -> FaoModel (FaoResult f)
  runFao = runFaoBack def

  -- | 运行特征,需要显示传入 HisBack
  --
  -- 如果是读取文件的，需要在开始时间点回溯数据
  runFaoBack :: (Typeable (FaoResult f)) => HisBack -> f -> FaoModel (FaoResult f)
  runFaoBack back = do
    let ?hisBack = back
    runFaoBack'

  -- | 运行特征,使用当前上下文的 HisBack
  --
  -- 如在 FaoRable， GMap 内部实现中会使用到
  --
  -- 如果是读取文件的，需要在开始时间点回溯数据
  runFaoBack' :: (Typeable (FaoResult f), HasHisBack) => f -> FaoModel (FaoResult f)
  runFaoBack' f = do
    tarType <- getTarType f
    case tarType of
          -- 固定板块参数类型
          BlockType expr -> withBlock expr $ executeFao f
          _ -> executeFao f

  executeFao :: (Typeable (FaoResult f), HasHisBack) => f -> FaoModel (FaoResult f)
  executeFao f = do
    (glb_fid, glb_type) <- view curr'cal'type
    cacheRef <- getFaoResultCacheRef
    cache <- liftIO $ readRef cacheRef
    uid <- getUniqueId f

    -- Fao 本身可以设置的三种类型
    let cal_type = propCalType f
    -- 加载文件的，缓存key需要加上 HisBack
    let back = getHisBack ?hisBack
    let buid = if cal_type == OnlyRead || cal_type == Cache then T.intercalate "#" [uid, T.pack (show back)] else uid

    case lookupGDict buid cache of
      Just v -> return v
      Nothing -> do
        res <- case cal_type of
          -- 永远读取
          OnlyRead -> do
            full_dir <- getFullDir f
            cfg <- lift $ view (env'ctx . ctx'app'config . env'mongo'config)
            mres <- load f
            case mres of 
                Just v -> return v 
                Nothing -> ifM isMongoDbMode doMongo doFile
                    where doFile = error $ show (getFaoConstr f) ++ " OnlyRead not find result:" ++ full_dir ++ "\n" ++ show (ggjson f)
                          doMongo = error $ show (getFaoConstr f) ++ " OnlyRead not find result:" ++ show cfg ++ "\n" ++ show (ggjson f)
          -- 永远计算
          Cal -> doImpl f
          Cache ->
            case glb_type of
              -- 本特征计算
              Cal ->
                if glb_fid == getParamId f
                  then doImpl f
                  else do
                    mres <- load f
                    maybe doImplAndDump return mres
              -- 本特征重新计算后保存
              Gen ->
                if glb_fid == getParamId f
                  then doImplAndDump
                  else do
                    mres <- load f
                    maybe doImplAndDump return mres
              AllCal -> doImpl f -- 所有特征都计算
              AllGen -> doImplAndDump -- 所有特征重新计算后保存
              _ -> error $ "not support cal_type" ++ show glb_type
          _ -> error $ "Fao propCalType must be Cal or Cache or OnlyRead, cannot be " ++ show cal_type
        liftIO $ writeRef cacheRef $ insertGDict buid res cache
        return res
    where
      doImplAndDump = do
        enable <- lift $ view (env'ctx . ctx'app'config . env'enable_extra)
        res <-
          if not enable
            then doImpl f
            else do
              withEventDumpEnv True f (doImpl f)
        dump f res
        return res

  -- | 获取真实的目标对象类型
  getTarType :: f -> FaoModel TarType
  getTarType f = do
    tartype <- propTarType f
    case tartype of
      RunTimeTarType -> currentTarType
      t -> return t

  -- | 获取当前特征目标类型下的品种集
  getSymbols :: f -> FaoModel Symbols
  getSymbols f = getTarType f >>= loadTarTypeSymbols

  -- | 特征名, 当读写数据时会拼接到路径
  --
  -- 通过如 PyAny 包装后，注意 ppname 一定是使用目标 Fao 的 ppname
  ppname :: f -> Text
  default ppname :: (Typeable f) => f -> Text
  ppname = typeConstrOf

  -- 通用的特征参数 json
  ggjson :: f -> BL.ByteString
  default ggjson :: (ToJSON f) => f -> BL.ByteString
  ggjson = encode

  -- | 特征输出类型
  type FaoResult f :: Type

  -- | 读取结果
  load :: HasHisBack => f -> FaoModel (Maybe (FaoResult f))
  load f@(propCalType -> cal_type) = if isCalType cal_type then return Nothing else error $ show (ppname f) ++ " no impl load"

  -- | 保存结果
  dump :: f -> FaoResult f -> FaoModel ()
  dump f@(propCalType -> cal_type) _ = if isCalType cal_type then return () else error $ show (ppname f) ++ " no impl dump"

  -- | 特征实现, FaoModel 表示某个目标对象下的实现，如某个品种, getTarName 获取目标对象名称
  doImpl :: HasHisBack => f -> FaoModel (FaoResult f)
  doImpl f = error $ show (ppname f) ++ " no impl doImpl"

--------------------
-- dump
--------------------

curr'dump'fields :: FaoModel (FieldMap (Text, IO (Int, Maybe Text)))
curr'dump'fields = do
  ctxs <- use curr'store'contexts
  return . dump_fields $ head ctxs

curr'dump'context :: FaoModel (Maybe DumpContext)
curr'dump'context = do
  ctxs <- use curr'store'contexts
  return $ if null ctxs then Nothing else Just (head ctxs)

modify'curr'dump'fields :: FieldName -> (FDType, IO (Int, Maybe Text)) -> FaoModel ()
modify'curr'dump'fields field v = do
  modify (over curr'store'contexts _uptCtxs)
  where
    _uptCtxs [] = []
    _uptCtxs (x : xs) = _uptCtx x : xs
    _uptCtx ctx@DumpContext {..} = ctx {dump_fields = _upt dump_fields}
    _upt !ms =
      if field == "tis"
        then error "🎃 字段名称不能使用关键字 tis"
        else case Map.lookup field ms of
          Nothing -> ms & at field ?~ v
          Just _ -> error $ "🎃 字段名称 " ++ show field ++ " 已经设置了"

-- | 保存字段信息
withEventDumpEnv :: (Fao f) => Bool -> f -> FaoModel a -> FaoModel a
withEventDumpEnv is_extra f runModel = do
  let fao_name = ppname f
  uid0 <- getUniqueId f
  let uid = if is_extra then "extra" <> uid0 else uid0

  full_dirs0 <- getAllFullDirs f  
  let full_dirs =  
        if is_extra 
        then fmap (</> "extra") full_dirs0
        else full_dirs0

  -- 设置存储路径
  let ctx = DumpContext uid fao_name full_dirs def
  modify (over curr'store'contexts (ctx :)) -- 添加到列表中
  !res <- runModel
  fields <- curr'dump'fields
  bMongoMode <- isMongoDbMode

  sof <- lift $ view (env'ctx . ctx'sof)
  cal_name <- currentCalendar'
  tar_name <- getTarName f

  unless (Map.null fields) $ do
    mpipe <- getMongoPipe
    let _dump = do
          rs <- forM fields $ \(fdtype, fn) -> fn >>= \n -> return (fdtype, n)
          let ps0 = Map.map (snd . snd) rs
              ps1 = catMaybes $ Map.elems ps0
              ps = Map.fromList $ fmap (,"event@f8") ps1
              etypes :: FieldMap Text = Map.union (Map.map fst rs) ps
          if bMongoMode then _dump2mongo rs etypes else _dump2File rs etypes

        _dump2mongo rs etypes = do
          -- 保存该特征相关汇总信息
          -- sof_name startDay endDay calendar fao_name params tar_name fields
          let doc :: MDB.Document
              doc =
                [ "_id" =: uid,
                  "sof_name" =: sof ^. sof'name,
                  "startDay" =: sof ^. sof'startDay,
                  "endDay" =: sof ^. sof'endDay,
                  "calendar" =: cal_name,
                  "fao_name" =: fao_name,
                  "tar_name" =: tar_name,
                  "params" =: (T.pack . BL.unpack) (ggjson f),
                  "fields" =: (T.pack . BL.unpack) (encode etypes),
                  "full_dir" =: head full_dirs
                ]
          case mpipe of 
            Nothing -> error "请配置 MongoDB 连接"
            Just pipe -> do 
                MDB.access pipe MDB.master "fao" $ do
                    wres <- MDB.updateMany "record" [(["_id" =: uid], doc, [MDB.Upsert])]
                    when (MDB.failed wres) $ do
                        liftIO $ printM $ "save result to mongo error:" ++ show wres
                printM $ "📂 save result to mongo[" ++ show uid ++ "] '" ++ "'," ++ show rs

        _dump2File rs etypes = do
          uuid <- nextRandom
          let go full_dir2 = do-- 最后需要保存字段相关信息的 json 文件, 这里都是 event@f8 类型
                let jsonPath = full_dir2 </> "fields.json"
                    tmpPath = jsonPath ++ "!" ++ toString uuid
                B.writeFile tmpPath (encode etypes)
                renamePath tmpPath jsonPath
                printM $ "📂 save result to file '" ++ full_dir2 ++ "'," ++ show rs
          mapM_ go full_dirs

    -- 结束事件触发执行保存函数
    eend <- getHistoryEndEvent
    performEvent_ $ liftIO . const _dump <$> eend

  modify (over curr'store'contexts tail) -- 从列表中移除
  return res

-- | 通过目标对象名称和字段名称获取事件名
packEventName :: (Fao f) => f -> TarName -> FieldName -> EventName
packEventName f tarName field = T.intercalate "#" [ppname f, T.pack (getParamId f), tarName, field]

-- | 运行 Fao 模型
runFaoModelWith :: (Typeable (FaoResult f), Fao f) => Maybe RealTimeMVar -> CalType -> AppConfig -> SofConfig -> Target -> f -> IO ()
runFaoModelWith mmvar calType acfg scfg tar f =
  runFrpEngine acfg scfg mmvar $ do
    let currTar = updateCurrTargetEnv def tar & curr'cal'type .~ (getParamId f, calType)
    evalFaoModel_ currTar def $ runFao f

runFaoProperty :: (Fao f) => AppConfig -> SofConfig -> Target -> f -> (f -> FaoModel a)-> IO a
runFaoProperty acfg scfg tar f go= do 
    runAppProperty acfg scfg $ do
        let currTar = updateCurrTargetEnv def tar & curr'cal'type .~ (getParamId f, Gen)
        evalFaoModel currTar def $ go f

-- | 运行 Fao 历史模型
runFaoHistory' :: (Typeable (FaoResult f), Fao f) => CalType -> AppConfig -> SofConfig -> Target -> f -> IO ()
runFaoHistory' = runFaoModelWith Nothing

-- | 运行 Fao 历史模型, 只重新运行本特征
runFaoHistory :: (Typeable (FaoResult f), Fao f) => AppConfig -> SofConfig -> Target -> f -> IO ()
runFaoHistory = runFaoHistory' Gen

-- | 运行 Fao 实时模型
runFaoRealTime :: (Typeable (FaoResult f), Fao f) => RealTimeMVar -> AppConfig -> SofConfig -> Target -> f -> IO ()
runFaoRealTime mvar = runFaoModelWith (Just mvar) AllGen

-- | 运行 FaoModel 事件, 返回事件值列表
runFaoEventModel :: SofConfig -> Target -> FaoModel (FrpEvent a) -> IO [a]
runFaoEventModel cfg target model = do
  resRef <- liftIO $ newIORef []
  runFrpEngine def cfg Nothing $ do
    let currTar = def & curr'target .~ target
    evalFaoModel currTar def $ do
      e <- model
      let _append a = do
            xs <- readIORef resRef
            writeIORef resRef (a : xs)
      performEvent_ $ liftIO . _append <$> e
  res <- readIORef resRef
  return $ reverse res

-- | 运行 FaoModel 函数事件, 返回事件值列表    
runFunctionEventModel :: FaoModel (FrpEvent a) -> IO [a]
runFunctionEventModel = runFaoEventModel def FuncTarget 


-- 合并目标类型
mergeTarType :: [TarType] -> TarType
mergeTarType tarTypes
  | null tarTypes = error "mergeTarType empty error"
  | length tarTypes == 1 = head tarTypes
  | otherwise =
      let (b, xs) = foldr _process (False, []) tarTypes
          t = _mergeTarType xs
       in if b then CalendarTarType t else t
  where
    _process :: TarType -> (Bool, [TarType]) -> (Bool, [TarType])
    _process (CalendarTarType t) (_, ts) = (True, t : ts)
    _process t (b, ts) = (b, t : ts)

_mergeTarType :: [TarType] -> TarType
_mergeTarType tarTypes
  | SymbolType `elem` tarTypes = SymbolType -- 如果存在 SymbolType
  | allSame tarTypes = head tarTypes -- 如果所有类型相同，返回该类型
  -- 存在未知板块
  | UnknownBlockType `elem` tarTypes = if Map.size askblks > 0 then error "不支持同时存在未知板块和品种所在板块" else UnknownBlockType
  | Map.size askblks == 1 = head $ Map.elems askblks
  | Map.size askblks > 1 = error "不支持多个品种所在板块"
  | otherwise = go -- 如果全是固定板块 FixedBlockType、StkTlistType、SymbolListType、BlockSetType，合并为 BlockSetType
  where
    flattenBlockSet :: TarType -> [BlockExpr]
    flattenBlockSet (BlockSetType ts) = ts
    flattenBlockSet (CalendarTarType _) = error "These cannot be SymbolType in CalendarTarType"
    flattenBlockSet SymbolType = error "These cannot be SymbolType in BlockSetType"
    flattenBlockSet RunTimeTarType = error "These cannot be RunTimeTarType in BlockSetType"
    flattenBlockSet UnknownBlockType = error "These cannot be UnknownBlockType in BlockSetType" -- TODO
    flattenBlockSet (BlockType (AskBlockExpr _ _)) = error "These cannot be AskBlockType in BlockSetType" -- TODO
    flattenBlockSet (BlockType t) = [t]
    flattenBlockSet FuncTarType = []
    go = case res of
      [] -> error "mergeTarType error"
      [x] -> BlockType x
      xs -> BlockSetType xs
      where
        res = Set.toList . Set.fromList $ concatMap flattenBlockSet tarTypes

    -- 判断列表中的所有元素是否相同
    allSame :: (Eq a) => [a] -> Bool
    allSame [] = True
    allSame (x : xs) = all (== x) xs

    -- ask 板块
    askblks = foldl goAskblks Map.empty tarTypes
    goAskblks xs t@(BlockType (AskBlockExpr expr _)) = Map.insert expr t xs
    goAskblks xs _ = xs

-- | 合并 Fao 目标类型
mergeFaoTarType :: (HAllHave Fao xs) => HList xs -> FaoModel TarType
mergeFaoTarType fs = mergeTarType <$> go fs
  where
    go :: (HAllHave Fao xs) => HList xs -> FaoModel [TarType]
    go HNil = return []
    go (x ::: xs) = do
      y <- propTarType x
      ys <- go xs
      return $ y : ys

-- | 特征历史数据回溯
--
-- 相同参数特征的可能被作为上游特征在多个地方调用
-- 且不同地方调用时设置的回溯数可能不一致
-- 如有的回溯10个事件或者Bar，有的回溯5天
-- 这时则回溯最大数据
-- 嵌套事件中不支持回溯 TODO
data HisBack
  = BackNumber Int
  | -- | 回溯 Bar 数或者事件数
    BackDay Int

instance Default HisBack where
  def = BackNumber 0

type HasHisBack = (?hisBack :: HisBack)

-- \| 回溯天数，暂时只支持自然日

getHisBack :: HisBack -> (Int, Int)
getHisBack (BackNumber n) = (n, 0)
getHisBack (BackDay d) = (0, d)

-----------------------------
-- 通过历史数据，自定义 Frp 事件
-----------------------------

-- | 通过历史数据，自定义 Frp 事件
newFrpEvent ::
  forall b a.
  (HasFrpHistoryData a b, HasFrpHistoryTs a, Typeable b, HasHisBack) =>
  -- 唯一事件名称，如果相同则返回定义过的事件
  EventName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  -- 实时 Tick 转换函数
  (RTValue -> b) ->
  AppModel (FrpEvent (Tick b))
newFrpEvent ename back getdata convertRT = do
  sourceRef <- getFrpSourceRef
  FrpSource {..} <- liftIO $ readIORef sourceRef
  let (n, d) = getHisBack ?hisBack
  case Map.lookup ename his_all_source of
    Just FrpHistoryData {..} -> do
      -- 修改回溯数
      let uptInput input =
            input
              { hisd_back_number = max n hisd_back_number,
                hisd_back_day = max d hisd_back_day
              }
          source' = FrpSource (Map.adjust uptInput ename his_all_source) (Map.adjust uptInput ename his_increased_source)
      liftIO $ writeIORef sourceRef source'

      case hisd_event of
        (e :: FrpEvent (Tick b')) ->
          case eqT :: Maybe (b :~: b') of
            Just Refl -> return e
            Nothing -> error $ "newFrpEvent type error: " ++ show ename
    Nothing -> do
      (etri, triRef) <- lift newEventWithTriggerRef

      -- 创建变量，触发的事件才会写入数据
      dataRef :: IORef (Maybe a) <- liftIO $ newIORef Nothing
      let _push HistoryTick {..} =
            readIORef dataRef >>= \case
              Nothing -> error $ show ename ++ " no load history data bug"
              Just a -> do
                let (_ts, _val, _price) = lookupHistoryData a his_data_index
                return $ Tick (convert _ts) _val _price
          ehis = pushAlways (liftIO . _push) etri

          convertRTick RTTick {..} = Tick rt_ts (convertRT rt_value) rt_price
      ert <- getRealTimeEvent <&> fmap convertRTick . fmapMaybe (Map.lookup ename)

      let eres = leftmost [ehis, ert]
          (n0, d0) = getHisBack back
          input =
            FrpHistoryData
              { hisd_data_io = getdata,
                hisd_data_ref = dataRef,
                hisd_trigger_ref = triRef,
                hisd_event = eres,
                hisd_back_number = max n0 n,
                hisd_back_day = max d0 d
              }
      -- 添加历史数据
      let source' = FrpSource (Map.insert ename input his_all_source) (Map.insert ename input his_increased_source)
      liftIO $ writeIORef sourceRef source'
      return eres

-- | 通过历史数据，自定义 Bits 类型的 Frp 惰性的事件
newBitsFrpEvent ::
  (HasFrpHistoryData a b, HasFrpHistoryTs a, DbaField b BitsField, Eq b, Storable b, EdhXchg b, Typeable b, Convertible Double b, HasHisBack) =>
  -- 唯一事件名称，如果相同则返回定义过的事件
  EventName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  AppModel (FrpEvent (Tick b))
newBitsFrpEvent a b c = newFrpEvent a b c $ convertRTDouble ("newBitsFrpEvent " ++ show a ++ " RTTick not RTDouble")

-- | 通过历史数据，自定义 Bits 类型的 Frp 事件,不回溯,自动唯一事件名称
--
-- 不支持实时,一般用于自定义事件数据测试
--
newAutoNamedBitsFrpEvent ::
  (HasFrpHistoryData a b, HasFrpHistoryTs a, DbaField b BitsField, Eq b, Storable b, EdhXchg b, Typeable b, Convertible Double b) =>
  IO a ->
  AppModel (FrpEvent (Tick b))
newAutoNamedBitsFrpEvent hisData = do 
    uuid <- liftIO nextRandom
    let ename = toText uuid
    let ?hisBack = BackNumber 0
    newBitsFrpEvent ename def hisData

-- | 通过历史数据，自定义 Bits 类型的 Frp 事件,不回溯,自动唯一事件名称
--
-- 不支持实时,一般用于自定义事件数据测试
--
-- 不包装 Tick
newAutoNamedBitsFrpEvent' ::
  (HasFrpHistoryData a b, HasFrpHistoryTs a, DbaField b BitsField, Eq b, Storable b, EdhXchg b, Typeable b, Convertible Double b) =>
  IO a ->
  AppModel (FrpEvent b)
newAutoNamedBitsFrpEvent' hisData = newAutoNamedBitsFrpEvent hisData <&> fmap value

-- | 通过历史数据，自定义 Adt 类型的 Frp 惰性的事件
--
-- 不支持实时
newAdtFrpEvent4His ::
  (HasFrpHistoryData a b, HasFrpHistoryTs a, Typeable b, HasHisBack) =>
  -- 唯一事件名称，如果相同则返回定义过的事件
  EventName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  AppModel (FrpEvent (Tick b))
newAdtFrpEvent4His a b c = newFrpEvent a b c $ \_ -> error ("newAdtFrpEvent4His " ++ show a ++ " unsupport realtime")

-- | 通过历史数据，自定义 Adt 类型的 Frp 惰性的事件
newAdtFrpEvent ::
  (HasFrpHistoryData a b, HasFrpHistoryTs a, Typeable b, FromJSON b, HasHisBack) =>
  -- 唯一事件名称，如果相同则返回定义过的事件
  EventName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  AppModel (FrpEvent (Tick b))
newAdtFrpEvent a b c = newFrpEvent a b c $ convertRTJson ("newAdtFrpEvent " ++ show a ++ " RTTick not RTJson")

-- | 通过历史数据，自定义与 Fao 绑定的 Frp 惰性的事件
newFrpEvent4Fao ::
  (Fao f, HasFrpHistoryData a b, HasFrpHistoryTs a, Typeable b, HasHisBack) =>
  f ->
  -- 字段名, 注意同一个 Fao 里面唯一
  FieldName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  -- 实时 Tick 转换函数
  (RTValue -> b) ->
  FaoModel (FrpEvent (Tick b))
newFrpEvent4Fao f fieldname back getData convertRT = do
  tar_name <- getTarName f
  let ename = packEventName f tar_name fieldname
  lift $ newFrpEvent ename back getData convertRT

-- | 通过历史数据，自定义与 Fao 绑定的 Frp 惰性的事件
--
-- 不包装 Tick
newFrpEvent4Fao' ::
  (Fao f, HasFrpHistoryData a b, HasFrpHistoryTs a, Typeable b, HasHisBack) =>
  f ->
  -- 字段名, 注意同一个 Fao 里面唯一
  FieldName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  -- 实时 Tick 转换函数
  (RTValue -> b) ->
  FaoModel (FrpEvent b)
newFrpEvent4Fao' a b c d e = newFrpEvent4Fao a b c d e <&> fmap value

-- | 通过历史数据，自定义与 Fao 绑定的 Frp 惰性的事件
newAdtFrpEvent4Fao ::
  (Fao f, HasFrpHistoryData a b, HasFrpHistoryTs a, Typeable b, FromJSON b, HasHisBack) =>
  f ->
  -- 字段名, 注意同一个 Fao 里面唯一
  FieldName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  FaoModel (FrpEvent (Tick b))
newAdtFrpEvent4Fao a b c d = newFrpEvent4Fao a b c d $ convertRTJson msg
  where
    msg = show (ppname a) ++ " newAdtFrpEvent4Fao " ++ show b ++ " RTTick not RTJson"

-- | 通过历史数据，自定义与 Fao 绑定的 Frp 惰性的事件
--
-- 不包装 Tick
newAdtFrpEvent4Fao' ::
  (Fao f, HasFrpHistoryData a b, HasFrpHistoryTs a, Typeable b, FromJSON b, HasHisBack) =>
  f ->
  -- 字段名, 注意同一个 Fao 里面唯一
  FieldName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  FaoModel (FrpEvent b)
newAdtFrpEvent4Fao' a b c d = newAdtFrpEvent4Fao a b c d <&> fmap value

-- | 通过历史数据，自定义 Bits 类型的 Frp 惰性的事件
newBitsFrpEvent4Fao ::
  (Fao f, HasFrpHistoryData a b, HasFrpHistoryTs a, DbaField b BitsField, Eq b, Storable b, EdhXchg b, Typeable b, Convertible Double b, HasHisBack) =>
  f ->
  -- 字段名, 注意同一个 Fao 里面唯一
  FieldName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  FaoModel (FrpEvent (Tick b))
newBitsFrpEvent4Fao a b c d = newFrpEvent4Fao a b c d $ convertRTDouble msg
  where
    msg = show (ppname a) ++ " newBitsFrpEvent4Fao " ++ show b ++ " RTTick not RTDouble"

-- | 通过历史数据，自定义 Bits 类型的 Frp 惰性的事件
--
-- 不包装 Tick
newBitsFrpEvent4Fao' ::
  (Fao f, HasFrpHistoryData a b, HasFrpHistoryTs a, DbaField b BitsField, Eq b, Storable b, EdhXchg b, Typeable b, Convertible Double b, HasHisBack) =>
  f ->
  -- 字段名, 注意同一个 Fao 里面唯一
  FieldName ->
  -- 默认回溯,如状态型事件默认至少回溯一个事件
  HisBack ->
  -- 获取事件历史数据函数
  IO a ->
  FaoModel (FrpEvent b)
newBitsFrpEvent4Fao' a b c d = newBitsFrpEvent4Fao a b c d <&> fmap value

-- | 强制加载历史数据，如果事件的源头存在
--
-- 必须在构建第一层(最外层)事件网络时调用
--
-- 暂时为了解决在嵌套(内层)事件中,存在自定义事件(如第一次运行 runFao (这些 Fao 的 Caltype = Cache)，或者 调用 newBitsFrpEvent 等)
forceLoadSourceEvent :: (PerformEvent t m, MonadIO (Performable m), MonadHold t m) => Description -> Event t a -> m ()
forceLoadSourceEvent s e = do
  -- 简单触发一次该事件，让触发器知道该事件被使用，从而加载历史数据
  e1 <- headE e
  performEvent_ $ (\_ -> liftIO . printM $ "====force load " ++ show s ++ " source event===") <$> e1

forceLoadSourceEvents :: (PerformEvent t m, MonadIO (Performable m), MonadHold t m) => Description -> [Event t a] -> m ()
forceLoadSourceEvents s es = forceLoadSourceEvent s $ mergeList es
