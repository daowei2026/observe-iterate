{-# LANGUAGE OverloadedStrings #-}
-- DIAGNOSTIC_ONLY: bounded controls against the unchanged adopted library.
module Main where
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import qualified Data.Text as T
import Control.Monad (foldM,unless)
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateKLineInput (klineForwardCoverage)
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateMaterial
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes
method=CompleteLinkPriceTurns 600 "CalendarUTITick" 800
objects=["rb","hc","i"]
base=1000000
step old at cov=either (error . T.unpack) id
  (advanceMaterial method S.empty (FormationFrame (fromIntegral at) at [] [] False cov) old)
observed prior at=[klineForwardCoverage 600 o prior (at,fromIntegral at) | o<-objects]
flag=materialCoverageIncomplete . currentMaterial
check name expected actual=do
  putStrLn (name++","++show expected++","++show actual++","++show (expected==actual))
  unless (expected==actual) (fail name)
main=do
  putStrLn "control,expected,actual,passed"
  let cold=step (emptyMaterialState objects) base (observed Nothing base)
      ats=[base+600,base+1200..base+480000]
      warmed=foldl (\st at->step st at (observed (Just (at-600,fromIntegral (at-600))) at)) cold ats
      at=base+480600
      failOne condition=step warmed at [if o=="rb" then ObjectCoverage o condition Nothing Nothing
        else klineForwardCoverage 600 o (Just (at-600,fromIntegral (at-600))) (at,fromIntegral at) | o<-objects]
      gapAt=base+481200
      gap=step warmed gapAt (observed (Just (base+480000,fromIntegral (base+480000))) gapAt)
      exempt=step (emptyMaterialState objects) base [ObjectCoverage o CoverageInapplicable Nothing Nothing | o<-objects]
  check "cold_start_is_incomplete" True (flag cold)
  check "801_valid_clock_points_without_turns_are_complete" False (flag warmed)
  check "single_object_source_failure_breaks_fixed_domain" True (flag (failOne CoverageSourceFailure))
  check "single_object_input_missing_breaks_fixed_domain" True (flag (failOne CoverageInputMissing))
  check "single_object_clock_unknown_breaks_fixed_domain" True (flag (failOne CoverageClockUnknown))
  check "true_1200_uti_jump_breaks_600_step_coverage" True (flag gap)
  check "true_gap_restarts_at_current_point" (Just (fromIntegral gapAt)) (coverageFrom (objectCoverage gap M.! "rb"))
  check "explicit_inapplicable_exempts_domain" False (flag exempt)
