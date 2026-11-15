{-# LANGUAGE OverloadedStrings #-}
module Main where
import Data.Aeson (Value, encode, object, (.=))
import qualified Data.ByteString.Lazy.Char8 as BL
import qualified Data.Text as Text
import Control.Monad (foldM)
import System.Environment (getArgs)
import Frp.Instance.ISL.Eaw.Interface.Common
import qualified Frp.Instance.ISL.Eaw.Interface.PreL0 as Spine
import Frp.Instance.ISL.Eaw.P1.Products
import Frp.Instance.ISL.Eaw.P1.WallLifecycle

-- 复用 existing light-test wallStart 的身份、ref、UTI、band；非自然数据。
identity :: WallIdentity
identity = WallIdentity 999
measuredBand :: Measurement Spine.WallBand
measuredBand = Measured (Spine.WallBand (Spine.Price 99) (Spine.Price 101) (Spine.Price 100))
wallStart :: WallLifecycleOccurrence
wallStart = WallLifecycleOccurrence identity (OccurrenceRef "wall-occurrence-1")
  (Spine.WallLifecycleEvent (wallRefOf identity) (InstrumentSymbol "rb") BidWall 10
    (Spine.WallStarted measuredBand Spine.WallAlive) Spine.WallLifecycleAvailable)
change ref uti value = wallStart {wallOccurrenceRef = OccurrenceRef ref,
  wallOccurrencePayload = Spine.WallLifecycleEvent (wallRefOf identity) (InstrumentSymbol "rb") BidWall uti value Spine.WallLifecycleAvailable}
bandUpdated = change "wall-occurrence-2" 11 (Spine.WallBandUpdated measuredBand Spine.WallAlive)
updateA = change "wall-occurrence-2" 11 (Spine.WallBandUpdated (Measured (Spine.WallBand (Spine.Price 100) (Spine.Price 102) (Spine.Price 101))) Spine.WallAlive)
updateB = change "wall-occurrence-2b" 12 (Spine.WallBandUpdated (Measured (Spine.WallBand (Spine.Price 101) (Spine.Price 103) (Spine.Price 102))) Spine.WallAlive)
ended = change "wall-occurrence-5" 14 (Spine.WallEnded (Spine.WallEndReason "producer-end"))
occValue :: WallLifecycleOccurrence -> Value
occValue o = object ["identity_show" .= show (wallOccurrenceIdentity o),
  "occurrence_ref_show" .= show (wallOccurrenceRef o), "payload_show" .= show (wallOccurrencePayload o),
  "uti_show" .= show (Spine.wallLifecycleOccurredAt (wallOccurrencePayload o)),
  "change_show" .= show (Spine.wallLifecycleChange (wallOccurrencePayload o)), "canonical_typed_show" .= show o]
emit :: Value -> IO ()
emit = BL.putStrLn . encode
stepIO label before inputs = case applyWallOccurrenceBatch before inputs of
  Left err -> do
    emit (object ["firing" .= label,"inputs" .= map occValue inputs,"pre_state_show" .= show before,
       "result" .= ("Left" :: Text.Text),"error_show" .= show err,
       "state_result_available" .= False,"O_result_available" .= False,
       "scope" .= ("pure reducer call; not FRP diagnostic/publication event" :: Text.Text)])
    pure before
  Right (after,os) -> do
    emit (object ["firing" .= label,"inputs" .= map occValue inputs,"pre_state_show" .= show before,
       "result" .= ("Right" :: Text.Text),"post_state_show" .= show after,
       "published_occurrences" .= map occValue os,"published_count" .= length os,
       "state_evidence" .= ("existing derived Show; includes actual wallViews and wallCurrentUpdateBatch; no new accessor" :: Text.Text),
       "scope" .= ("current pure reducer result; not production writer firing or full FRP runtime" :: Text.Text)])
    pure after
main = do
 args <- getArgs
 case args of
  ["normal"] -> do
    emit (object ["kind" .= ("binding" :: Text.Text),"evidence_class" .= ("synthetic engineering controlled current-source reducer" :: Text.Text),
      "object" .= ("rb" :: Text.Text),"calendar_scope" .= ("existing test SHFE-night label only; no calendar runtime" :: Text.Text),
      "UTI_scope" .= ("10,11,12,14 artificial test axis; no market epoch mapping" :: Text.Text),
      "firing_scope" .= ("N1,N2,N3 controlled reducer call ordinal; no wallclock/confirm/known semantics" :: Text.Text)])
    _ <- foldM (\s (l,os) -> stepIO (l::Text.Text) s os) emptyWallLifecycleState [("N1",[wallStart]),("N2",[updateA,updateB]),("N3",[ended])]
    pure ()
  ["scenario-duplicate"] -> do
    s <- stepIO ("CS05.setup"::Text.Text) emptyWallLifecycleState [wallStart]
    emit (object ["existing_test" .= ("P1EndToEndSpec.hs:455-460 cross-firing exact duplicate"::Text.Text),"expected_by_existing_assertion" .= ("Right; sameState==state && null duplicatePublications"::Text.Text)])
    _ <- stepIO ("CS05.duplicate"::Text.Text) s [wallStart]
    pure ()
  ["scenario-after-end"] -> do
    s <- stepIO ("CS06.setup"::Text.Text) emptyWallLifecycleState [wallStart,bandUpdated,ended]
    emit (object ["existing_test" .= ("P1EndToEndSpec.hs:537 after-End update expression; narrowed setup omits Dormant/restore"::Text.Text),"expected_by_existing_assertion" .= ("any Left; original test does not assert exact constructor"::Text.Text)])
    _ <- stepIO ("CS06.afterEndUpdate"::Text.Text) s [bandUpdated {wallOccurrenceRef=OccurrenceRef "wall-occurrence-6"}]
    pure ()
  _ -> fail "expected normal | scenario-duplicate | scenario-after-end"
