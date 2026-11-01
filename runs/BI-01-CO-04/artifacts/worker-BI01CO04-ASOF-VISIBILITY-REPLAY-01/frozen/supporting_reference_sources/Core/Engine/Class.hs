{-# LANGUAGE DefaultSignatures #-}
{-# LANGUAGE DerivingVia #-}
{-# LANGUAGE FlexibleInstances #-}
{-# LANGUAGE GeneralisedNewtypeDeriving #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE UndecidableInstances #-}

-- | Frp 引擎
module Frp.Core.Engine.Class
  ( 
    -- * Reader
    AppConfig (AppConfig),
    env'name,
    env'app_dir,
    env'enable_extra,
    env'mongo'config,
    MongoConfig (..),
    SofConfig (..),
    Sof (..),
    sof'name,
    sof'stk_tlist,
    sof'startDay,
    sof'endDay,
    sof'opt_start_hour,
    sof'opt_end_hour,
    sof'store_dir,
    sof'store_name,
    sof'category,
    sof'dir,
    sof'tlist_dir,
    sof'ori_dir,
    sof'pnv_dir,
    sof'full_period,
    env'ctx,
    ctx'app'config,
    ctx'sof,
    ctx'store'dirs,

    -- * AppModel
    AppModel,
    TisModel,
    runFrpEngine,
    runAppProperty,
    AppModelQuery (..),
  )
where

import Control.Concurrent.MVar
import Control.Lens hiding (List, from, ifoldl', imap, (<.>))
import Control.Monad.Catch
import Control.Monad.Extra
import Control.Monad.Reader
import Control.Monad.Ref
import Control.Monad.ST
import Control.Parallel.Strategies
import Data.Aeson as Aeson
import Data.Align
import Data.ByteString.Lazy.Char8 qualified as BL
import Data.Convertible
import Data.Csv qualified as Csv
import Data.Default
import Data.Dependent.Sum
import Data.IORef
import Data.List qualified as L
import Data.Map.Strict (Map)
import Data.Map.Strict qualified as Map
import Data.Maybe
import Data.Sort
import Data.Text (Text)
import Data.Text qualified as T
import Data.These
import Data.Time hiding (addDays,Day)
import Data.Vector qualified as V
import Data.Vector.Algorithms.Merge qualified as VA
import Data.Vector.Storable qualified as VS
import Data.Vector.Unboxed qualified as VU
import Database.MongoDB qualified as MDB
import Debug.Trace
import Frp.Apt
import Frp.Core.Engine.Base
import GHC.Generics
import Reflex
import Reflex.Host.Class
import System.FilePath

-- import Debug.Trace

data MongoConfig = MongoConfig
  { hostname :: String, -- mongodb 主机名
    secs :: MDB.Secs -- mongodb 连接超时
  }
  deriving (Show, Generic)

-- | 全局配置
data AppConfig = AppConfig
  { -- | test dev prod
    _env'name :: String,
    _env'app_dir :: FilePath,
    -- | 是否启动保存中间事件
    _env'enable_extra :: Bool,
    -- | Mongo 配置
    _env'mongo'config :: Maybe MongoConfig
  }
  deriving (Generic, Show)

makeLenses ''AppConfig

instance Default AppConfig where
  def = AppConfig "dev" "/m3varE/AppData" False Nothing

-- | 针对 store_dir json 数据, 值可能为以下两种类型
data StoreDir = StoreDir FilePath | StoreDirs [FilePath] deriving(Show)

instance FromJSON StoreDir where
  parseJSON v = case v of
    String s -> return $ StoreDir $ T.unpack s
    Array vs -> return $ StoreDirs $ V.toList $ fmap _parse vs
      where
        _parse (String s) = T.unpack s
        _parse _ = error "StoreDir json parse error: Expected a String"
    -- 如果不是上述两种类型，则解析失败
    _ -> fail "StoreDir json parse error: Expected a String or an Array"

instance Convertible StoreDir [FilePath] where 
    safeConvert (StoreDir v) = return [v]
    safeConvert (StoreDirs vs) = return vs

-- | 用于读取 Sof 的 Json 文件配置
data SofFileConfig = SofFileConfig
  { sfc_store_dir :: StoreDir,
    sfc_store_name :: String,
    sfc_opt_start_hour :: Text,
    sfc_opt_end_hour :: Text,
    sfc_sof_category :: String,
    sfc_sof_dir :: FilePath,
    sfc_sof_tlist_dir :: FilePath,
    sfc_ori_dir :: FilePath,
    sfc_pnv_dir :: FilePath
  }
  deriving (Generic, Show)

instance FromJSON SofFileConfig where
  parseJSON =
    genericParseJSON
      defaultOptions
        { fieldLabelModifier = \case
            "sfc_store_dir" -> "store_dir"
            "sfc_store_name" -> "store_name"
            "sfc_opt_start_hour" -> "opt_start_hour"
            "sfc_opt_end_hour" -> "opt_end_hour"
            "sfc_sof_category" -> "sof_category"
            "sfc_sof_dir" -> "sof_dir"
            "sfc_sof_tlist_dir" -> "sof_tlist_dir"
            "sfc_ori_dir" -> "ori_dir"
            "sfc_pnv_dir" -> "pnv_dir"
            s -> error $ "SofFileConfig have no field:" ++ s
        }

-- | Sof参数 与 Python 端同名
data SofConfig = SofConfig
  { -- | 如 TB
    sof_name :: Text,
    stk_tlist :: Text,
    startDay :: Maybe Text,
    endDay :: Maybe Text,
    -- | 数据完整时间周期 或者 特征数据优先查询起止日期
    full_period :: Maybe (Maybe Text,Maybe Text)
  }
  deriving (Generic, Show)

instance Default SofConfig where
  def = SofConfig "TB" "steel" Nothing Nothing Nothing 

-- | 完整的 sof 信息: SofConfig + SofFileConfig
--
-- 使用 Lens 的，字段一般带有 ', 以下名称(' 替换为 _ 后的名称)可能会被其他地方使用
data Sof = Sof
  { _sof'name :: Text,
    _sof'stk_tlist :: Text,
    _sof'startDay :: Maybe Text,
    _sof'endDay :: Maybe Text,
    _sof'store_dir :: [FilePath],
    _sof'store_name :: String,
    _sof'opt_start_hour :: Text,
    _sof'opt_end_hour :: Text,
    _sof'category :: String,
    _sof'dir :: FilePath,
    _sof'tlist_dir :: FilePath,
    _sof'ori_dir :: FilePath,
    _sof'pnv_dir :: FilePath,
    _sof'full_period :: Maybe (Maybe Text,Maybe Text)
  }
  deriving (Generic, Show)

makeLenses ''Sof

-- | 输入 Context
data AppContext = AppContext
  { _ctx'app'config :: AppConfig,
    _ctx'sof :: Sof,
    -- | 配置的 Fao 的 store_dir
    _ctx'store'dirs :: Map.Map Text [FilePath]
  }
  deriving (Generic, Show)

makeLenses ''AppContext


createAppContext :: AppConfig -> SofConfig -> IO AppContext
createAppContext cfg@AppConfig {..} SofConfig {..} = do
  let base_dir = _env'app_dir </> "mquant" </> "config" </> _env'name
  let store_dirs_path = base_dir </> "store_dir.json"
  store_dirs' :: Maybe (Map.Map Text StoreDir) <-
    Aeson.eitherDecodeFileStrict store_dirs_path >>= \case
      Left s -> error $ "parse " ++ store_dirs_path ++ " error:" ++ s
      Right v -> return v
  let store_dirs = fmap2 convert store_dirs'

  let sof_path = base_dir </> "sof" </> T.unpack sof_name <.> "json"
  sofConfig <-
    Aeson.eitherDecodeFileStrict sof_path >>= \case
      Left s -> error $ "parse " ++ sof_path ++ " error:" ++ s
      Right v -> return v

  let sof =
        Sof
          { _sof'name = sof_name,
            _sof'stk_tlist = stk_tlist,
            _sof'startDay = startDay,
            _sof'endDay = endDay,
            _sof'store_dir = convert (sfc_store_dir sofConfig),
            _sof'store_name = sfc_store_name sofConfig,
            _sof'opt_start_hour = sfc_opt_start_hour sofConfig,
            _sof'opt_end_hour = sfc_opt_end_hour sofConfig,
            _sof'category = sfc_sof_category sofConfig,
            _sof'dir = sfc_sof_dir sofConfig,
            _sof'tlist_dir = sfc_sof_tlist_dir sofConfig,
            _sof'ori_dir = sfc_ori_dir sofConfig,
            _sof'pnv_dir = sfc_pnv_dir sofConfig,
            _sof'full_period = full_period
          }
  return
    AppContext
      { _ctx'app'config = cfg,
        _ctx'sof = sof,
        _ctx'store'dirs = fromMaybe Map.empty store_dirs
      }

-- | 历史回测 or 实时
data FrpRunMode = History | RealTime deriving (Show, Ord, Eq)

data OneAskBolck = OneAskBolck
  { one'ask'block :: Map BlkName Symbols,
    one'ask'sym :: Map Sym BlkName
  }
  deriving (Generic)

-- | Env
data AppEnv = AppEnv
  { -- | Context
    _env'ctx :: AppContext,
    -- | 结束事件
    _env'end'event :: FrpEvent (),
    -- | 时间轴事件
    _env'timeline'event :: FrpEvent EventTime,
    -- | 历史结束事件
    _env'history'end'event :: FrpEvent (),
    -- | 实时事件
    _env'realtime'event :: FrpEvent (Map EventName RTTick),
    -- | 回测或者实时运行模式
    _env'run'mode :: FrpRunMode,
    -- | fao 结果缓存,
    _env'fao'result'cache'ref :: IORef GDict,
    -- | 历史数据源
    _env'frp'source'ref :: IORef FrpSource,
    -- | 当前触发时间
    _env'curr'trigger'ts'ref :: IORef Timestamp,
    -- | stk_tlist 品种集
    _env'stk'tlist'symbols'ref :: IORef (Map Text Symbols),
    -- | 固定板块
    _env'fixed'block'ref :: IORef (Maybe (Map BlkName Symbols)),
    -- | 品种所在板块
    _env'ask'block'ref :: IORef (Maybe (Map Text OneAskBolck)),
    _env'block'fixed'hierarchy'ref :: IORef (Maybe (Map BlkName [BlkName])),
    _env'mongo'pipe :: Maybe MDB.Pipe
  }
  deriving (Generic)

makeLenses ''AppEnv

-- | AppModelT  TODO  需要改进 unroll
newtype AppModelT t m a = AppModelT
  { unAppModelT :: ReaderT AppEnv m a
  }
  deriving (Functor, Applicative, Monad, MonadFix, MonadTrans, MonadIO, MonadThrow, MonadCatch, MonadMask, MonadRef, MonadReader AppEnv)

-- | Model
type AppModel = AppModelT FrpEngine (PostBuildT FrpEngine (PerformEventT FrpEngine FrpMonad))

-- | 兼容旧版调用，暂时保留
type TisModel = AppModel

-- | call app model
runAppModelT :: (Monad m) => AppModelT t m a -> AppEnv -> m a
runAppModelT (unAppModelT -> a) = runReaderT a

-------------------
-- AppModelT reflex instance
-------------------

instance (MonadReflexCreateTrigger t m) => MonadReflexCreateTrigger t (AppModelT t m) where
  newEventWithTrigger = lift . newEventWithTrigger
  newFanEventWithTrigger f = lift $ newFanEventWithTrigger f

instance (PerformEvent t m) => PerformEvent t (AppModelT t m) where
  type Performable (AppModelT t m) = AppModelT t (Performable m)
  performEvent_ e = do
    r <- ask
    lift $ performEvent_ $ flip runAppModelT r <$> e
  performEvent e = do
    r <- ask
    lift $ performEvent $ flip runAppModelT r <$> e

instance (TriggerEvent t m) => TriggerEvent t (AppModelT t m) where
  newTriggerEvent = lift newTriggerEvent
  newTriggerEventWithOnComplete = lift newTriggerEventWithOnComplete
  newEventWithLazyTriggerWithOnComplete = lift . newEventWithLazyTriggerWithOnComplete

instance (PostBuild t m) => PostBuild t (AppModelT t m) where
  getPostBuild = lift getPostBuild

instance (MonadSample t m) => MonadSample t (AppModelT t m) where
  sample = lift . sample

instance (MonadHold t m) => MonadHold t (AppModelT t m) where
  hold a0 = lift . hold a0
  holdDyn a0 = lift . holdDyn a0
  holdIncremental a0 = lift . holdIncremental a0
  buildDynamic a0 = lift . buildDynamic a0
  headE = lift . headE

instance (Adjustable t m) => Adjustable t (AppModelT t m) where
  runWithReplace a0 a' = do
    r <- ask
    lift $ runWithReplace (runAppModelT a0 r) $ fmap (`runAppModelT` r) a'
  traverseIntMapWithKeyWithAdjust f dm0 dm' = do
    r <- ask
    lift $ traverseIntMapWithKeyWithAdjust (\k v -> runAppModelT (f k v) r) dm0 dm'
  traverseDMapWithKeyWithAdjust f dm0 dm' = do
    r <- ask
    lift $ traverseDMapWithKeyWithAdjust (\k v -> runAppModelT (f k v) r) dm0 dm'
  traverseDMapWithKeyWithAdjustWithMove f dm0 dm' = do
    r <- ask
    lift $ traverseDMapWithKeyWithAdjustWithMove (\k v -> runAppModelT (f k v) r) dm0 dm'

instance (NotReady t m) => NotReady t (AppModelT r m) where
  notReadyUntil = lift . notReadyUntil
  notReady = lift notReady

-- | 不执行事件，只是用来获取 Fao 属性等
runAppProperty ::
  AppConfig ->
  SofConfig ->
  AppModel a ->
  IO a
runAppProperty acfg scfg model = do
  ctx <- createAppContext acfg scfg
  runSpiderHost $ do  -- 缓存 Fao 结果
    cacheRef <- liftIO $ newIORef def

    sourceRef <- liftIO $ newIORef def

    -- 最新触发时间
    currTriggerTsRef <- liftIO $ newIORef 0

    stk'tlist'symbols'ref1 <- liftIO $ newIORef def
    fixed'block'ref1 <- liftIO $ newIORef Nothing
    ask'block'ref1 <- liftIO $ newIORef Nothing
    block'fixed'hierarchy'ref1 <- liftIO $ newIORef Nothing

    -- 运行 model
    (res, _) <-
      hostPerformEventT $
        flip runPostBuildT never $
          runAppModelT
            model
            AppEnv
              { _env'ctx = ctx,
                -- 结束事件
                _env'end'event = never,
                -- 时间轴事件
                _env'timeline'event = never,
                -- 历史结束事件
                _env'history'end'event = never,
                -- 实时事件
                _env'realtime'event = never,
                _env'run'mode = History,
                _env'fao'result'cache'ref = cacheRef,
                _env'frp'source'ref = sourceRef,
                _env'curr'trigger'ts'ref = currTriggerTsRef,
                -- stk_tlist 品种集
                _env'stk'tlist'symbols'ref = stk'tlist'symbols'ref1,
                -- 固定板块
                _env'fixed'block'ref = fixed'block'ref1,
                -- 品种所在板块
                _env'ask'block'ref = ask'block'ref1,
                _env'block'fixed'hierarchy'ref = block'fixed'hierarchy'ref1,
                _env'mongo'pipe = Nothing
              }
    return res


-- | 运行 Frp 引擎
runFrpEngine ::
  AppConfig ->
  SofConfig ->
  Maybe RealTimeMVar -> -- 实时数据源
  AppModel a ->
  IO ()
runFrpEngine acfg scfg mmvar model = do
  printM "🐸 ===== The Frp Engine e6.2.0.6 is getting ready to start running ===== 🐸 "

  ctx <- createAppContext acfg scfg

  !start <- getZonedTime

  runSpiderHost $ do
    -- 开始事件 即 PostBuild
    (estart, startRef) <- newEventWithTriggerRef

    -- 结束事件
    (eend, endRef) <- newEventWithTriggerRef

    -- 历史结束事件
    (ehisEnd, hisEndRef) <- newEventWithTriggerRef

    -- 主时间轴事件
    (etimeline, timelineRef) <- newEventWithTriggerRef

    -- 实时事件
    (ert, rtRef) <- newEventWithTriggerRef

    -- 缓存 Fao 结果
    cacheRef <- liftIO $ newIORef def

    sourceRef <- liftIO $ newIORef def

    -- Tensor 时期遗留的逻辑，兼容已保存数据
    -- startDay + OPT_HOUR_STR 
    let sof = view ctx'sof ctx
        sdate = textToTimestamp dateFmtPattern <$> joinSpace (view sof'startDay sof) (view sof'opt_start_hour sof)
        edate = textToTimestamp dateFmtPattern <$> joinSpace (view sof'endDay sof) (view sof'opt_end_hour sof)

    -- 最新触发时间
    currTriggerTsRef <- liftIO $ newIORef (0 :: Timestamp)

    stk'tlist'symbols'ref <- liftIO $ newIORef def
    fixed'block'ref <- liftIO $ newIORef Nothing
    ask'block'ref <- liftIO $ newIORef Nothing
    block'fixed'hierarchy'ref <- liftIO $ newIORef Nothing

    -- 连接 MongoDB
    mpipe <- liftIO $ case view env'mongo'config acfg of
      Nothing -> return Nothing
      Just MongoConfig {..} -> do
        pipe <- MDB.connect' secs (MDB.host hostname)
        printM $ "===== 连接 MongoDB " ++ hostname ++ " 成功====="
        return $ Just pipe

    -- 运行 model
    (_, FireCommand fire) <-
      hostPerformEventT $
        flip runPostBuildT estart $
          runAppModelT
            model
            AppEnv
              { _env'ctx = ctx,
                -- 结束事件
                _env'end'event = eend,
                -- 时间轴事件
                _env'timeline'event = etimeline,
                -- 历史结束事件
                _env'history'end'event = ehisEnd,
                -- 实时事件
                _env'realtime'event = ert,
                _env'run'mode = if isJust mmvar then RealTime else History,
                _env'fao'result'cache'ref = cacheRef,
                _env'frp'source'ref = sourceRef,
                _env'curr'trigger'ts'ref = currTriggerTsRef,
                -- stk_tlist 品种集
                _env'stk'tlist'symbols'ref = stk'tlist'symbols'ref,
                -- 固定板块
                _env'fixed'block'ref = fixed'block'ref,
                -- 品种所在板块
                _env'ask'block'ref = ask'block'ref,
                _env'block'fixed'hierarchy'ref = block'fixed'hierarchy'ref,
                _env'mongo'pipe = mpipe
              }

    -- 按事件时间合并分组历史数据
    source <- liftIO $ readIORef sourceRef

    datas <- liftIO $ do
      !start0 <- getZonedTime
      datas <- mergeGroupHistoryData (his_all_source source) (Truncate sdate edate Nothing)
      let !total = sum $ length <$> datas

      !end0 <- getZonedTime
      printM $
        "⏱️ ===== mergeGroupHistoryData cost "
          ++ show (end0 `diffZonedTime` start0)
          ++ ", There are "
          ++ show total
          ++ "("
          ++ (show . V.length $ datas)
          ++ ") events ready to run ====="
      return datas

    -- 清除 his_increased_source
    liftIO $ writeIORef sourceRef (FrpSource (his_all_source source) Map.empty)

    -- 循环历史数据
    dataRef <- liftIO $ newIORef datas
    iRef <- liftIO $ newIORef 0

    let getHisDatas = do
          FrpSource {..} <- readIORef sourceRef
          oldDatas <- readIORef dataRef
          if Map.null his_increased_source
            then return oldDatas
            else do
              i <- readIORef iRef
              !start1 <- getZonedTime
              currTs <- readIORef currTriggerTsRef
              newdatas <- mergeGroupIncreasedHistoryData (V.drop i oldDatas) his_increased_source (Truncate sdate edate (Just currTs))
              let !total1 = sum $ length <$> newdatas

              !end1 <- getZonedTime
              printM $
                "⏱️ ===== mergeGroupIncreasedHistoryData cost "
                  ++ show (end1 `diffZonedTime` start1)
                  ++ ", From "
                  ++ show currTs -- 最新触发时间
                  ++ " There are "
                  ++ show total1
                  ++ "("
                  ++ (show . V.length $ newdatas)
                  ++ ") events ready to run ====="

              -- 重置索引
              writeIORef iRef 0
              writeIORef dataRef newdatas
              -- 清除 his_increased_source
              liftIO $ writeIORef sourceRef (FrpSource his_all_source Map.empty)
              return newdatas

        triggerHis = do
          xs <- getHisDatas
          i <- readIORef iRef
          modifyIORef iRef (+ 1)
          return $ xs V.!? i

    let -- 触发历史数据事件
        loopFireHistory = whenJustM (liftIO triggerHis) fireHistory
        fireHistory vs = do
          vtri <- mapM _findTrigger vs
          tstri <- _findTsTrigger vs
          let tris = catMaybes (tstri : vtri)
          fire tris (return ()) >> loopFireHistory
          where
            _findTrigger :: HistoryTick -> FrpMonad (Maybe (DSum (EventTrigger FrpEngine) Identity))
            _findTrigger a@HistoryTick {..} =
              readRef his_trigger
                >>= mapM
                  ( \tri -> do
                      liftIO $ writeIORef currTriggerTsRef (ts_time . atTickTs $ a)
                      return $ tri :=> Identity a
                  )

            -- 取第一个数据的时间作为主时间轴事件的事件值
            _findTsTrigger (x : _) = readRef timelineRef >>= mapM (\tri -> return $ tri :=> Identity (atTickTs x))
            _findTsTrigger _ = return Nothing

        -- 触发实时数据事件
        fireRealTime = whenJust mmvar $ \mvar -> do
          printM "🔔🔔🔔 ===== 等待接收实时 Tick ===== 🔔🔔🔔"
          let -- 循环获取实时数据
              loopFireRealTime = whenJustM (liftIO $ takeMVar mvar) execRealTime
              execRealTime RealTimeTriggerTick {..} = do
                vtri <-
                  readRef rtRef
                    >>= mapM
                      ( \tri -> do
                          liftIO $ writeIORef currTriggerTsRef (ts_time rt_ts)
                          return $ tri :=> Identity rt_data
                      )
                tstri <- readRef timelineRef >>= mapM (\tri -> return $ tri :=> Identity rt_ts)
                let tris = catMaybes [vtri, tstri]
                fire tris (return ()) >> loopFireRealTime
          loopFireRealTime

        -- 触发一个空的占位事件
        fireEmpty emptyref = whenJustM (readRef emptyref) $ \tri -> void $ fire [tri :=> Identity ()] (return ())

        -- 开始事件特殊处理
        -- 添加 EventTime 0 到主事件轴中
        -- 以便某些使用了 getPostBuild 的事件也可以 wrapTickEvent
        fireStart = do
          vtri <- readRef startRef >>= mapM (\tri -> return $ tri :=> Identity ())
          tstri <- readRef timelineRef >>= mapM (\tri -> return $ tri :=> Identity (def :: EventTime))
          let tris = catMaybes [vtri, tstri]
          fire tris (return ())

        closePipe = liftIO $ forM_ mpipe MDB.close

    -- 依次触发相应事件后输出结果
    -- 开始事件 >> 历史事件 >> 历史结束事件 >> 实时事件 >> 结束事件
    fireStart >> loopFireHistory >> fireEmpty hisEndRef >> fireRealTime >> fireEmpty endRef >> closePipe

  !end <- getZonedTime
  printM $ "⏱️ ===== runFrpEngine cost " ++ show (end `diffZonedTime` start) ++ " ====="

-- | 截取历史数据
data Truncate = Truncate
  { sdate :: Maybe Timestamp,
    edate :: Maybe Timestamp,
    currTs :: Maybe Timestamp -- 当前事件时间, 嵌套事件中触发历史事件截取
  }

mergeGroupIncreasedHistoryData :: V.Vector [HistoryTick] -> FieldMap FrpHistoryData -> Truncate -> IO (V.Vector [HistoryTick])
mergeGroupIncreasedHistoryData !olds !source tr = do
  -- 并行处理新数据
  !news <- mergeGroupHistoryData source tr

  -- 直接在 Vector 层面合并数据
  let !mergedVec = V.concatMap V.fromList (olds V.++ news)
  return $! groupTicksByTime mergedVec

-- | 优化的数据分组函数
groupTicksByTime :: V.Vector HistoryTick -> V.Vector [HistoryTick]
groupTicksByTime !vec = runST $ do
  -- 使用 unboxed vector 存储时间戳以减少内存使用
  let !timestamps = VU.generate (V.length vec) (ts_time . atTickTs . (vec V.!))

  -- 创建索引数组并排序
  idxs <- VU.thaw $ VU.generate (V.length vec) id
  sortWithTimestamps timestamps idxs
  sorted_idxs <- VU.freeze idxs

  -- 按排序后的索引重组数据并分组
  let !sorted = V.backpermute vec (VU.convert sorted_idxs)
  return $! V.fromList $ L.groupBy (\a b -> atTickTs a == atTickTs b) $ V.toList sorted
  where
    -- sortWithTimestamps :: VU.Vector Timestamp -> MU.MVector (PrimState ST) Int -> ST s ()
    sortWithTimestamps !ts !mv = VA.sortBy (\i j -> compare (ts VU.! i) (ts VU.! j)) mv

-- | 按事件时间合并分组历史数据
mergeGroupHistoryData :: FieldMap FrpHistoryData -> Truncate -> IO (V.Vector [HistoryTick])
mergeGroupHistoryData !source Truncate {..} = do
  -- 加载数据
  !xs <- mapM _loadHistoryData (Map.toList source)
  let !rsource = catMaybes xs

  -- 构建和过滤数据
  let !ticks = buildAndFilterTicks rsource
  -- 分组
  return $! groupTicksByTime ticks
  where
    buildAndFilterTicks :: [(EventName, (VS.Vector Timestamp, (Int, Int), FrpEventTriggerRef HistoryTick))] -> V.Vector HistoryTick
    buildAndFilterTicks sources =
      -- 并行处理每个数据源
      V.concat $ parMap rdeepseq processSingleSource sources

    processSingleSource :: (EventName, (VS.Vector Timestamp, (Int, Int), FrpEventTriggerRef HistoryTick)) -> V.Vector HistoryTick
    processSingleSource (!name, (!fts, !back, !trigger)) =
      let !timestamps = VS.convert fts
          !ticks =
            V.force $
              V.imap
                ( \i ts ->
                    HistoryTick name i (EventTime ts HistoryQuoteStatus) trigger
                )
                timestamps
       in filterTicks name back ticks

    filterTicks :: EventName -> (Int, Int) -> V.Vector HistoryTick -> V.Vector HistoryTick
    filterTicks name !back !ticks =
      let !fv =
            case currTs of
              -- 嵌套事件中触发历史事件截取, 过滤掉 <= 最新触发时间的历史数据
              Just _ts ->
                let (!_, !after) = V.partition ((<= _ts) . ts_time . atTickTs) ticks
                 in V.force after
              Nothing -> maybe ticks (filterByStart name ticks back) sdate
       in V.force $ maybe fv (filterByEnd fv) edate

    filterByStart :: EventName -> V.Vector HistoryTick -> (Int, Int) -> Timestamp -> V.Vector HistoryTick
    filterByStart name !vs (n, d) !s =
      if
        -- 不回溯,获取所有大于等于优化开始时间的数据
        -- 这里是假设数据是升序排列的，才能使用 V.dropWhile， 否则需要排序(TODO)
        | n <= 0 && d <= 0 -> V.force $ V.dropWhile ((< s) . ts_time . atTickTs) vs
        -- 同时设置了回溯Bar和Day,获取回溯多的
        | n > 0 && d > 0 ->
            let ndata = _getData _truncateN
                ddata = _getData _truncateD
                nsize = V.length ndata
                dsize = V.length ddata
             in if nsize > dsize then ndata else ddata
        | d > 0 -> _getData _truncateD
        | otherwise -> _getData _truncateN
      where
        -- 通过优化时间分割为两部分
        (!before, !after) = V.partition ((< s) . ts_time . atTickTs) vs
        _getData tr =
          if not (V.null before)
            then V.force $ tr before V.++ after
            else V.force after

        -- 向前取 n 个数据
        _truncateN ds = if cha < 0 then trace msg res else res
          where
            res = V.drop (V.length before - n) ds
            cha = V.length res - n
            msg = "🍋" ++ T.unpack name ++ " 需要回溯 " ++ show n ++ " 个事件，但是只有 " ++ show (n + cha) ++ " 个事件🍋"

        -- 向前取 n 天数据
        _truncateD ds = if s' < fs then trace msg res else res
          where
            s' = addDays (-(abs d)) s
            fs = ts_time . atTickTs $ V.head ds
            res = V.dropWhile ((< s') . ts_time . atTickTs) ds
            msg = "🍋" ++ T.unpack name ++ " 需要回溯到 " ++ show s' ++ ", 但是数据开始时间只到 " ++ show fs ++ "🍋"

    filterByEnd :: V.Vector HistoryTick -> Timestamp -> V.Vector HistoryTick
    filterByEnd !vs !e = V.force $ V.takeWhile (\x -> ts_time (atTickTs x) <= e) vs

-- | 优化的数据加载函数
_loadHistoryData :: (EventName, FrpHistoryData) -> IO (Maybe (EventName, (VS.Vector Timestamp, (Int, Int), FrpEventTriggerRef HistoryTick)))
_loadHistoryData (!name, FrpHistoryData {..}) = do
  !mtrigger <- readRef hisd_trigger_ref
  forM mtrigger $ \_ -> do
    !xdata <- hisd_data_io
    writeRef hisd_data_ref $ Just xdata
    return (name, (atHistoryTs xdata, (hisd_back_number, hisd_back_day), hisd_trigger_ref))

class (Applicative m, Monad m) => AppModelQuery m where
  -- | 事件值通过主时间轴包装为 Tick,没有价格
  --
  -- 只能 wrap 通过 eget equery 等获取的源事件，以及这些源事件通过存函数衍生的的事件
  --
  -- 而通过 performEvent 衍生的则不行，performEvent 的事件发生在源事件后
  wrapTickEvent :: FrpEvent a -> m (FrpEvent (Tick a))
  default wrapTickEvent :: (m ~ f m', MonadTrans f, AppModelQuery m') => FrpEvent a -> m (FrpEvent (Tick a))
  wrapTickEvent = lift . wrapTickEvent

  isRealTimeMode :: m Bool
  default isRealTimeMode :: (m ~ f m', MonadTrans f, AppModelQuery m') => m Bool
  isRealTimeMode = lift isRealTimeMode

  -- | 获取 Fao 结果缓存,不可以乱用
  getFaoResultCacheRef :: m (IORef GDict)
  default getFaoResultCacheRef :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (IORef GDict)
  getFaoResultCacheRef = lift getFaoResultCacheRef

  getFrpSourceRef :: m (IORef FrpSource)
  default getFrpSourceRef :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (IORef FrpSource)
  getFrpSourceRef = lift getFrpSourceRef

  -- | 获取结束事件
  getEndEvent :: m (FrpEvent ())
  default getEndEvent :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (FrpEvent ())
  getEndEvent = lift getEndEvent

  -- | 获取主时间轴事件
  getTimeLineEvent :: m (FrpEvent EventTime)
  default getTimeLineEvent :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (FrpEvent EventTime)
  getTimeLineEvent = lift getTimeLineEvent

  -- | 获取历史结束事件
  getHistoryEndEvent :: m (FrpEvent ())
  default getHistoryEndEvent :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (FrpEvent ())
  getHistoryEndEvent = lift getHistoryEndEvent

  -- | 获取实时事件
  getRealTimeEvent :: m (FrpEvent (Map EventName RTTick))
  default getRealTimeEvent :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (FrpEvent (Map EventName RTTick))
  getRealTimeEvent = lift getRealTimeEvent

  -- | 获取某个 stk_tlist 中的品种集
  loadStkTlistSymbols :: Text -> m Symbols
  default loadStkTlistSymbols :: (m ~ f m', MonadTrans f, AppModelQuery m') => Text -> m Symbols
  loadStkTlistSymbols = lift . loadStkTlistSymbols

  -- | 获取当前品种板块配置，先从环境中获取，如果没有则从 json 文件中读取
  loadAskBlockConfig :: m (Map Text OneAskBolck)
  default loadAskBlockConfig :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (Map Text OneAskBolck)
  loadAskBlockConfig = lift loadAskBlockConfig

  -- | 获取固定板块配置，先从环境中获取，如果没有则从 json 文件中读取
  loadFixedBlockConfig :: m (Map BlkName Symbols)
  default loadFixedBlockConfig :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (Map BlkName Symbols)
  loadFixedBlockConfig = lift loadFixedBlockConfig

  -- | 获取某个品种所在板块名
  askBlkName :: Sym -> Text -> m BlkName
  default askBlkName :: (m ~ f m', MonadTrans f, AppModelQuery m') => Sym -> Text -> m BlkName
  askBlkName sym t = lift $ askBlkName sym t

  -- | 获取某个品种所在板块品种集
  loadAskBlockSymblos :: Sym -> Text -> m Symbols
  default loadAskBlockSymblos :: (m ~ f m', MonadTrans f, AppModelQuery m') => Sym -> Text -> m Symbols
  loadAskBlockSymblos sym t = lift $ loadAskBlockSymblos sym t

  -- | 获取固定板块品种集
  loadFixedBlockSymbols :: BlkName -> m Symbols
  default loadFixedBlockSymbols :: (m ~ f m', MonadTrans f, AppModelQuery m') => BlkName -> m Symbols
  loadFixedBlockSymbols = lift . loadFixedBlockSymbols

  -- | 获取固定板块层级关系
  loadBlockFixedHierarchy :: m (Map BlkName [BlkName])
  default loadBlockFixedHierarchy :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (Map BlkName [BlkName])
  loadBlockFixedHierarchy = lift loadBlockFixedHierarchy

  -- | 获取目标对象名称
  parseTarName :: Target -> m TarName
  default parseTarName :: (m ~ f m', MonadTrans f, AppModelQuery m') => Target -> m TarName
  parseTarName = lift . parseTarName

  -- | 获取当前触发事件(不支持框架以外使用)
  getCurrTriggerTs :: m Timestamp
  default getCurrTriggerTs :: (m ~ f m', MonadTrans f, AppModelQuery m') => m Timestamp
  getCurrTriggerTs = lift getCurrTriggerTs

  getMongoPipe :: m (Maybe MDB.Pipe)
  default getMongoPipe :: (m ~ f m', MonadTrans f, AppModelQuery m') => m (Maybe MDB.Pipe)
  getMongoPipe = lift getMongoPipe

  isMongoDbMode :: m Bool
  default isMongoDbMode :: (m ~ f m', MonadTrans f, AppModelQuery m') => m Bool
  isMongoDbMode = lift isMongoDbMode

data StkSymbol = StkSymbol
  { symbol :: Text,
    exchg :: Text,
    name :: Text
  }
  deriving (Show, Generic)

instance Csv.FromRecord StkSymbol

instance AppModelQuery AppModel where

  isMongoDbMode = isJust <$> getMongoPipe

  getMongoPipe :: AppModel (Maybe MDB.Pipe)
  getMongoPipe = view env'mongo'pipe

  getCurrTriggerTs :: AppModel Timestamp
  getCurrTriggerTs = view env'curr'trigger'ts'ref >>= liftIO . readIORef

  getFaoResultCacheRef :: AppModel (IORef GDict)
  getFaoResultCacheRef = view env'fao'result'cache'ref

  getFrpSourceRef :: AppModel (IORef FrpSource)
  getFrpSourceRef = view env'frp'source'ref

  wrapTickEvent :: FrpEvent a -> AppModel (FrpEvent (Tick a))
  wrapTickEvent e = do
    ets <- getTimeLineEvent
    -- 目标事件发生时肯定有主时间轴事件发生
    let go (These _ts _val) = Just $ Tick _ts _val Nothing
        go (This _ts) = Nothing
        go _ = Nothing -- TODO error "🎃 unsupported event to wrap TimeLineEvent"
    return $ fmapMaybe go $ align ets e

  isRealTimeMode :: AppModel Bool
  isRealTimeMode = view env'run'mode <&> (== RealTime)

  getEndEvent :: AppModel (FrpEvent ())
  getEndEvent = view env'end'event

  -- \| 获取主时间轴事件
  getTimeLineEvent :: AppModel (FrpEvent EventTime)
  getTimeLineEvent = view env'timeline'event

  -- \| 获取历史结束事件
  getHistoryEndEvent :: AppModel (FrpEvent ())
  getHistoryEndEvent = view env'history'end'event

  -- \| 获取实时事件
  getRealTimeEvent :: AppModel (FrpEvent (Map EventName RTTick))
  getRealTimeEvent = view env'realtime'event

  -- \| 获取某个 stk_tlist 中的品种集
  loadStkTlistSymbols :: Text -> AppModel Symbols
  loadStkTlistSymbols name = do
    ref <- view env'stk'tlist'symbols'ref
    ms <- liftIO $ readIORef ref
    case Map.lookup name ms of
      Just syms -> return syms
      Nothing -> do
        dir <- view (env'ctx . ctx'sof . sof'tlist_dir)
        let file_path = dir </> T.unpack name ++ ".csv"
        csvData <- liftIO $ BL.readFile file_path
        let csvRes :: Either String (V.Vector StkSymbol) = Csv.decode Csv.HasHeader csvData
        case csvRes of
          Left err -> error err
          Right vs -> do
            let res = symbol <$> V.toList vs
            liftIO $ writeIORef ref (Map.insert name res ms)
            return res

  -- 获取当前品种板块配置，先从环境中获取，如果没有则从 json 文件中读取
  loadAskBlockConfig :: AppModel (Map Text OneAskBolck)
  loadAskBlockConfig = do
    ref <- view env'ask'block'ref
    ms <- liftIO $ readIORef ref
    case ms of
      Just v -> return v
      Nothing -> do
        dir <- view (env'ctx . ctx'sof . sof'dir)
        let file_path = dir </> "block" </> "ask.json"
        liftIO $
          Aeson.eitherDecodeFileStrict file_path >>= \case
            Left s -> error $ file_path ++ " decode error: " ++ s
            Right jres -> do
              let ori = _parse <$> jres
                  res = Map.map _tran ori
              writeIORef ref (Just res)
              return res
    where
      _parse v =
        case Aeson.fromJSON v of
          Aeson.Error s -> error s
          Aeson.Success (ys :: (Map Text Aeson.Value)) -> _parse2 <$> ys
      _parse2 v =
        case Aeson.fromJSON v of
          Aeson.Error s -> error s
          Aeson.Success (ys :: Symbols) -> ys
      _tran :: Map BlkName Symbols -> OneAskBolck
      _tran xs = OneAskBolck xs ys
        where
          ys = Map.fromList $ Map.foldlWithKey' _fold [] xs
          _fold res blk syms = res ++ fmap (,blk) syms

  -- \| 获取固定板块配置，先从环境中获取，如果没有则从 json 文件中读取
  loadFixedBlockConfig :: AppModel (Map BlkName Symbols)
  loadFixedBlockConfig = do
    ref <- view env'fixed'block'ref
    ms <- liftIO $ readIORef ref
    case ms of
      Just v -> return v
      Nothing -> do
        dir <- view (env'ctx . ctx'sof . sof'dir)
        let file_path = dir </> "block" </> "fixed.json"
        liftIO $
          Aeson.eitherDecodeFileStrict file_path >>= \case
            Left s -> error $ file_path ++ " decode error: " ++ s
            Right jres -> do
              let res = _parse <$> jres
              writeIORef ref (Just res)
              return res
    where
      _parse v =
        case Aeson.fromJSON v of
          Aeson.Error s -> error s
          Aeson.Success (ys :: Symbols) -> ys

  -- | 获取固定板块层级关系
  loadBlockFixedHierarchy :: AppModel (Map BlkName [BlkName]) 
  loadBlockFixedHierarchy = do
    ref <- view env'block'fixed'hierarchy'ref
    ms <- liftIO $ readIORef ref
    case ms of
      Just v -> return v
      Nothing -> do
        dir <- view (env'ctx . ctx'sof . sof'dir)
        let file_path = dir </> "block" </> "fixed_hierarchy.json"
        liftIO $
          Aeson.eitherDecodeFileStrict file_path >>= \case
            Left s -> error $ file_path ++ " decode error: " ++ s
            Right jres -> do
              writeIORef ref (Just jres)
              return jres

  -- \| 获取某个品种所在板块名
  askBlkName :: Sym -> Text -> AppModel BlkName
  askBlkName sym name = do
    ms <- loadAskBlockConfig
    case Map.lookup name ms of
      Nothing -> error $ "品种 " ++ show sym ++ " 没有配置使用板块 " ++ show name
      Just (one'ask'sym -> vs) ->
        case Map.lookup sym vs of
          Nothing -> error $ "品种 " ++ show sym ++ " 没有配置使用板块 " ++ show name
          Just res -> return res

  -- \| 获取某个品种所在板块品种集
  loadAskBlockSymblos :: Sym -> Text -> AppModel Symbols
  loadAskBlockSymblos sym name = do
    blk <- askBlkName sym name
    ms <- loadAskBlockConfig
    case Map.lookup name ms of
      Nothing -> error $ "品种 " ++ show sym ++ " 没有配置使用板块 " ++ show name
      Just (one'ask'block -> vs) ->
        case Map.lookup blk vs of
          Nothing -> error $ "品种 " ++ show sym ++ " 没有配置使用板块 " ++ show name
          Just res -> return res

  -- \| 获取固定板块品种集
  loadFixedBlockSymbols :: BlkName -> AppModel Symbols
  loadFixedBlockSymbols blk = do
    ms <- loadFixedBlockConfig
    case Map.lookup blk ms of
      Nothing -> error $ "没有配置固定板块 " ++ show blk
      Just res -> return res

  -- \| 获取目标对象名称
  parseTarName :: Target -> AppModel TarName
  parseTarName (Symbol sym) = return sym
  parseTarName (AskBlock expr sym) =
    case T.stripPrefix "ask@" expr of
      Nothing -> error $ show expr ++ " is error ask blk expr"
      Just name -> do
        blk <- askBlkName sym name
        return $ expr <> "@" <> blk
  parseTarName (FixedBlock expr) = return expr -- TODO 长度过长时需要与 python 端一致，待处理
  parseTarName (BlockSet blks) = do
    let res = T.intercalate "-" (sort blks)
    if length blks > 8
      then do
        let sha = T.pack $ encodeSha1 (T.unpack res)
        return $ "blks" <> T.pack (show (length blks)) <> "_" <> sha
      else return res
  parseTarName FuncTarget = return "func"
  parseTarName (CalendarTarget AtSelfCalendar t) = parseTarName t
  parseTarName (CalendarTarget c t) = do
    tname <- parseTarName t
    return $ tname <> "." <> convert c
