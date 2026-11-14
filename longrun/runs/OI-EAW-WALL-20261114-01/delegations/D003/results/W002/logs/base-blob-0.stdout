{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE TypeFamilies #-}

module Frp.Instance.ISL.Eaw.P1.WallLifecycle
  ( WallLifecycleP (..),
    WallLifecycleState,
    WallLifecycleError (..),
    WallLifecycleOutputs (..),
    emptyWallLifecycleState,
    applyWallOccurrenceBatch,
    maintainWallLifecycle,
  )
where

import Control.Monad (foldM)
import Data.Map.Strict (Map)
import Data.Map.Strict qualified as Map
import Frp.Apt (FrpDynamic, FrpEvent)
import Frp.CEP.Class (CEPS (..))
import Frp.Core (FaoModel)
import Frp.Instance.ISL.Eaw.Interface.PreL0 qualified as Spine
import Frp.Instance.ISL.Eaw.P1.Internal.OccurrenceLedger
import Frp.Instance.ISL.Eaw.P1.Products
import GHC.Generics (Generic)
import Reflex (fmapMaybe, foldDyn, holdDyn, updated)

data WallLifecycleError
  = WallOccurrenceRefConflict OccurrenceRef
  | WallStartedTwice WallIdentity
  | WallMustStartPresent WallIdentity
  | WallUpdateBeforeStart WallIdentity
  | WallUpdateAfterEnd WallIdentity
  | WallEndBeforeStart WallIdentity
  | WallBandUpdateChangedPresence WallIdentity WallBusinessState Spine.WallPresence
  | WallInvalidPresenceTransition WallIdentity WallBusinessState Spine.WallPresence
  deriving (Eq, Ord, Show, Generic)

data WallLifecycleState = WallLifecycleState
  { wallLedger :: OccurrenceLedger OccurrenceRef,
    wallViews :: Map WallIdentity WallCurrentView,
    wallCurrentUpdateBatch :: Map WallIdentity WallCurrentView
  }
  deriving (Eq, Ord, Show, Generic)

emptyWallLifecycleState :: WallLifecycleState
emptyWallLifecycleState = WallLifecycleState emptyOccurrenceLedger Map.empty Map.empty

validateWallTransition :: WallIdentity -> Maybe WallCurrentView -> Spine.WallLifecycleChange -> Either WallLifecycleError WallBusinessState
validateWallTransition identity before change = case (before, change) of
  (Nothing, Spine.WallStarted _ Spine.WallAlive) -> Right WallPresent
  (Nothing, Spine.WallStarted _ Spine.WallDormant) -> Left (WallMustStartPresent identity)
  (Nothing, Spine.WallEnded _) -> Left (WallEndBeforeStart identity)
  (Nothing, _) -> Left (WallUpdateBeforeStart identity)
  (Just _, Spine.WallStarted _ _) -> Left (WallStartedTwice identity)
  (Just current, _)
    | wallCurrentState current == WallEndedState -> Left (WallUpdateAfterEnd identity)
  (Just current, Spine.WallBandUpdated _ presence) -> case (wallCurrentState current, presence) of
    (WallPresent, Spine.WallAlive) -> Right WallPresent
    (WallDormantState, Spine.WallDormant) -> Right WallDormantState
    _ -> Left (WallBandUpdateChangedPresence identity (wallCurrentState current) presence)
  (Just current, Spine.WallPresenceChanged _ presence) -> case (wallCurrentState current, presence) of
    (WallPresent, Spine.WallDormant) -> Right WallDormantState
    (WallDormantState, Spine.WallAlive) -> Right WallPresent
    _ -> Left (WallInvalidPresenceTransition identity (wallCurrentState current) presence)
  (Just _, Spine.WallEnded _) -> Right WallEndedState

applyWallOccurrence :: WallLifecycleState -> WallLifecycleOccurrence -> Either WallLifecycleError (WallLifecycleState, Maybe WallLifecycleOccurrence)
applyWallOccurrence state occurrence = do
  let ref = wallOccurrenceRef occurrence
      identity = wallOccurrenceIdentity occurrence
      change = Spine.wallLifecycleChange (wallOccurrencePayload occurrence)
  case appendOccurrence ref occurrence (wallLedger state) of
    (_, OccurrenceRefConflict) -> Left (WallOccurrenceRefConflict ref)
    (_, OccurrenceAlreadyPresent) -> Right (state, Nothing)
    (nextLedger, OccurrenceAppended) -> do
      let before = Map.lookup identity (wallViews state)
      afterState <- validateWallTransition identity before change
      let current = WallCurrentView identity afterState occurrence
          nextViews =
            case afterState of
              WallEndedState -> Map.delete identity (wallViews state)
              _ -> Map.insert identity current (wallViews state)
          next =
            state
              { wallLedger = nextLedger,
                wallViews = nextViews,
                wallCurrentUpdateBatch = Map.insert identity current (wallCurrentUpdateBatch state)
              }
      Right (next, Just occurrence)

applyWallOccurrenceBatch :: WallLifecycleState -> [WallLifecycleOccurrence] -> Either WallLifecycleError (WallLifecycleState, [WallLifecycleOccurrence])
applyWallOccurrenceBatch initial occurrences = do
  -- occurrence_ref 的唯一性由已提交 artifact 保证；运行态只检查当前
  -- firing，不能再永久镜像全年 occurrence fingerprint。
  let firingState = initial {wallLedger = emptyOccurrenceLedger, wallCurrentUpdateBatch = Map.empty}
  (next, publishedReversed) <- foldM step (firingState, []) occurrences
  pure (next, reverse publishedReversed)
  where
    step (state, published) occurrence = do
      (next, accepted) <- applyWallOccurrence state occurrence
      pure (next, maybe published (: published) accepted)

data WallLifecycleOutputs = WallLifecycleOutputs
  { wallLifecycleOccurrences :: FrpEvent [WallLifecycleOccurrence],
    wallLifecycleCurrent :: FrpDynamic (Map WallIdentity WallCurrentView),
    wallLifecycleCurrentUpdates :: FrpEvent [WallCurrentView],
    wallLifecycleDiagnostics :: FrpEvent (P1ProductDiagnostics WallLifecycleError)
  }

data WallTxn = WallTxn
  { wallTxnState :: WallLifecycleState,
    wallTxnResult :: Maybe (Either WallLifecycleError [WallLifecycleOccurrence])
  }

stepWall :: [WallLifecycleOccurrence] -> WallTxn -> WallTxn
stepWall occurrences txn = case applyWallOccurrenceBatch (wallTxnState txn) occurrences of
  Left err -> txn {wallTxnResult = Just (Left err)}
  Right (next, published) -> WallTxn next (Just (Right published))

wallCurrentUpdatesFor :: WallLifecycleState -> [WallCurrentView]
wallCurrentUpdatesFor = Map.elems . wallCurrentUpdateBatch

data WallLifecycleP = WallLifecycleP

instance CEPS WallLifecycleP FaoModel where
  type Input WallLifecycleP = FrpEvent [WallLifecycleOccurrence]
  type Output WallLifecycleP = WallLifecycleOutputs

  processEvents WallLifecycleP input = do
    transactions <- foldDyn stepWall (WallTxn emptyWallLifecycleState Nothing) input
    let outcomes = fmapMaybe wallTxnResult (updated transactions)
        acceptedTransactions =
          fmapMaybe
            (\txn -> case wallTxnResult txn of
                Just (Right published) | not (null published) -> Just (txn, published)
                _ -> Nothing
            )
            (updated transactions)
    current <- holdDyn Map.empty (wallViews . wallTxnState . fst <$> acceptedTransactions)
    pure
      WallLifecycleOutputs
        { wallLifecycleOccurrences = snd <$> acceptedTransactions,
          wallLifecycleCurrent = current,
          wallLifecycleCurrentUpdates =
            (\(txn, _published) -> wallCurrentUpdatesFor (wallTxnState txn))
              <$> acceptedTransactions,
          wallLifecycleDiagnostics =
            (\err -> P1ProductDiagnostics [] [err])
              <$> fmapMaybe (either Just (const Nothing)) outcomes
        }

maintainWallLifecycle :: FrpEvent [WallLifecycleOccurrence] -> FaoModel WallLifecycleOutputs
maintainWallLifecycle = processEvents WallLifecycleP
