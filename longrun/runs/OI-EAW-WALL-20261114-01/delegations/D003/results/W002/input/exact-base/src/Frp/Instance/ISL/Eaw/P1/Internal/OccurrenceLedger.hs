{-# LANGUAGE DeriveGeneric #-}

-- | 仅供 P1 DSU 内部使用的 append-only occurrence ledger。
module Frp.Instance.ISL.Eaw.P1.Internal.OccurrenceLedger
  ( OccurrenceLedger,
    AppendDisposition (..),
    emptyOccurrenceLedger,
    appendOccurrence,
  )
where

import Data.Map.Strict (Map)
import Data.Map.Strict qualified as Map
import Data.Text (Text)
import Data.Text qualified as Text
import Frp.Apt (encodeSha1)
import GHC.Generics (Generic)

-- | DSU 的 append-only occurrence 已由正式事件流和 writer 保存；运行态
-- ledger 只承担 exact duplicate／conflicting duplicate 判定，不能再复制
-- 一份完整 payload 历史。
newtype OccurrenceLedger ref = OccurrenceLedger
  { ledgerFingerprintByRef :: Map ref Text
  }
  deriving (Eq, Ord, Show, Generic)

-- | 一条 occurrence 对运行态幂等索引造成的结果。
data AppendDisposition
  = OccurrenceAppended
  | OccurrenceAlreadyPresent
  | OccurrenceRefConflict
  deriving (Eq, Ord, Show, Generic)

-- | 空的运行态幂等索引。
emptyOccurrenceLedger :: OccurrenceLedger ref
emptyOccurrenceLedger = OccurrenceLedger Map.empty

-- | 按 occurrence 引用登记 payload fingerprint。
--
-- 输入依次是业务 occurrence 引用、完整业务 payload 和当前幂等索引；输出
-- 是更新后的紧凑索引以及追加／重复／冲突判定。fingerprint 只用于本次运行
-- 内的幂等判断，不成为业务身份，也不替代正式 writer 中的完整 occurrence。
appendOccurrence :: (Ord ref, Show payload) => ref -> payload -> OccurrenceLedger ref -> (OccurrenceLedger ref, AppendDisposition)
appendOccurrence ref payload ledger =
  case Map.lookup ref (ledgerFingerprintByRef ledger) of
    Nothing ->
      ( ledger
          { ledgerFingerprintByRef = Map.insert ref fingerprint (ledgerFingerprintByRef ledger)
          },
        OccurrenceAppended
      )
    Just existing
      | existing == fingerprint -> (ledger, OccurrenceAlreadyPresent)
      | otherwise -> (ledger, OccurrenceRefConflict)
  where
    fingerprint = Text.pack (encodeSha1 (show payload))
