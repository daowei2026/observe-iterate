{-# LANGUAGE OverloadedStrings #-}
-- DIAGNOSTIC_ONLY: actual be57 library functions; no Feature/engine/store execution.
module Main where
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import qualified Data.Text as T
import Data.Int (Int64)
import Control.Monad (foldM)
import System.Environment (getArgs)
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateKLineInput (klineForwardCoverage)
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateMaterial
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes

split :: String -> [String]
split s=case break (==',') s of (a,[]) -> [a]; (a,_:b) -> a:split b
method=CompleteLinkPriceTurns 600 "CalendarUTITick" 800
objects=["rb","hc","i"]
type St=(MaterialState,M.Map T.Text (Int64,Double))
advance mode (old,previous) line=do
  let (uText:flags)=split line
      at=read uText::Int64; u=fromIntegral at
      valid=zip objects (map (=="1") flags)
      cov o ok=if mode/="actual" && not ok
        then ObjectCoverage o (if mode=="intervention" then CoverageSourceFailure else CoverageInputMissing) Nothing Nothing
        else klineForwardCoverage 600 o (M.lookup o previous) (at,u)
      nextPrev=foldl (\m (o,ok)->if mode/="actual" && not ok then M.delete o m
                  else M.insert o (at,u) m) previous valid
      frame=FormationFrame u at [] [] False [cov o ok | (o,ok)<-valid]
  next<-either (fail . T.unpack) pure (advanceMaterial method S.empty frame old)
  let flag=if materialCoverageIncomplete (currentMaterial next) then "1" else "0"
      from o=maybe "NA" show (coverageFrom (objectCoverage next M.! o))
      condition o=show (coverageCondition (objectCoverage next M.! o))
  putStrLn (concat [mode,",",uText,",",flag,",",from "rb",",",condition "rb"])
  pure (next,nextPrev)
main=do
  args<-getArgs
  input<-readFile (head args)
  putStrLn "mode,uti,domain_coverage_incomplete,rb_coverage_from,rb_condition"
  mapM_ (\mode->foldM (advance mode) (emptyMaterialState objects,M.empty) (tail (lines input)) >> pure ())
    ["actual","intervention","proposed_input_missing_intervention"]
