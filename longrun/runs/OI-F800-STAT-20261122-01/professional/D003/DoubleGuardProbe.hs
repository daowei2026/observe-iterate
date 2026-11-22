-- DIAGNOSTIC_ONLY. 独立小值算术检查；不导入、不改动、不运行正式Feature。
module Main where
import Text.Printf (printf)
sourceAdjacent :: Double -> Double -> Bool
sourceAdjacent old now = let p=old/600; position=now/600 in position-p==1
integerDiagnosticAdjacent :: Integer -> Integer -> Bool
integerDiagnosticAdjacent old now = now-old==600
main :: IO ()
main=do
  putStrLn "name,old_uti,new_uti,old_position,new_position,position_delta,source_guard,integer_diagnostic_guard"
  mapM_ probe [("normal_before",78642599,78643199),("real_boundary",78643199,78643799),
              ("normal_after",78643799,78644399),("true_gap_control",78643199,78644399)]
  where
    probe (name,old,now)=let oldD=fromInteger old::Double;nowD=fromInteger now::Double
                        in printf "%s,%d,%d,%.17g,%.17g,%.17g,%s,%s\n" name old now
                          (oldD/600) (nowD/600) (nowD/600-oldD/600)
                          (show (sourceAdjacent oldD nowD)) (show (integerDiagnosticAdjacent old now))
