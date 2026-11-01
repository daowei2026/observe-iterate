from mquant.frame import *
from mquant.tis.frp import *
import numpy as np
import pandas as pd

from mquant.tis.abc.customize import RctOccurFldSeg

__all__ = [
  "ZigZag",
  "ZigStatus",
  "ZigConfirm",
  "HighLowZigZag",
  "RctZigWithStatus",
  "MACDFrp",
  "WaveTurnBack",
  "PrecipitationFundsFeat",
  "TurnoverRateFeat",
  "AMAFrp",
  "AMA",
  "AMAAbsLtFrp",
  "AMAAbsLt",
  "TurtleCapitalRatioFrp",
  "CapitalManagerFrp",
  "FrpTurtleCapitalRatio",
  "FrpCapitalManager",
  "TurtleCapitalRatio",
  "CapitalManager",
  "SpeFrp",
  "SpeGtFrp",
  "SpeGtBlockRatioCurrentContextFrp",
  "SpeGtBlockRatioCurrentContext",
  "HPLtFrp",
  "HPLt",
]

class ZigZagMixIn:
    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type
    
    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        df = pd.DataFrame({
            "swingStatus": dbav1['zigBarSwing']['swingStatus'],
            "swingPrice": dbav1['zigBarSwing']['swingPrice'],
            "swingPoivt": dbav1['zigBarSwing']['swingPoivt'],
            "swingPosUTI": dbav1['zigBarSwing']['swingPosUTI'],
            "lastPrice": dbav1['lastSwing']['lsPrice'],
            "lastPosUTI": dbav1['lastSwing']['lsPosUTI'],
            "lastDirection": dbav1['lastSwing']['lsDirection'],
            "uti": dbav1['zigzagBarUTI'],
        }, index=self.value.ts)
        df["zigUTI"] = np.where(abs(df["swingStatus"]) == 1, df["lastPosUTI"], np.nan)
        df["zigPrice"] = np.where(abs(df["swingStatus"]) == 1, df["lastPrice"], np.nan)
        df["lastUptUTI"] = np.where(abs(df["swingStatus"]) == 2, df["lastPosUTI"], np.nan)
        df["lastUptPrice"] = np.where(abs(df["swingStatus"]) == 2, df["lastPrice"], np.nan)
        return df

class HighLowZigZag(ZigZagMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-05-20 17:56  
    Desc  : 
        - ZigZag 特征, 但是高点用最高价, 低点用最低价
        - 本质逻辑是, SwingHigh, SwingLow计算使用最高价和最低价, 而不是都用收盘价
        - 其他的和已有的ZigZag逻辑完全一致
    '''
    params = lambda : {
        "featIn": Nothing,
        "retracePct": 2,
    }
      
class ZigZag(ZigZagMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-04-03 17:56
    Desc  : 
        - ZigZag 特征
        - 当前bar的swingStatus, 0的时候代表没有有效的swingHigh swingLow, 此时LastSwing为上一个有效SwingHigh或Low的信息.
        - 所谓有效, 说的是, 要么确认上个swingHigh或Low是zig点, 要么更新了上个swingHigh或者Low.
        - 当前bar的绝对值为1, 说明swingHigh或Low是确认zig的点, 此时LastSwing是被确认的实际zig点信息.
        - 当前bar的绝对值为2, 说明swingHigh或Low是更新高点低点的点, 此时LastSwing给的是上一个被更新的高点低点的信息。
        - 注意, bar绝对值为0和2的时候LastSwing不是上一个被确认的实际zig点!
        - 注意, 为了方便画图新增的字段只是根据swingStatus, 把lastPrice和lastPosUTI的信息分别分了两列.
    Params: 
        featIn: 要计算zigzag的特征, 一般是k线收盘价, 要求有uti数据
        retracePct: 反转百分比 
    Fields:
        swingStatus : swingHigh或者Low状态(0无,1确定向上,2修改向上,-1确定向下,-2修改向下)
        swingPrice : 最近一次swingHigh或者Low的价格
        swingPoivt : 最近一次swingHigh或者Low的价格, 带方向
        swingPosUTI : 最近一次swingHigh或者Low的价格的UTI  
        lastPrice : 上一个SwingHigh或者Low点(LastSwing)处价格
        lastPosUTI : 上一个SwingHigh或者Low点(LastSwing)的UTI
        lastDirection : 上一个SwingHigh或者Low点(LastSwing)方向(1向上,-1向下)
        uti : 当前bar的uti
        zigUTI : 为了方便画图新增的字段, 确认转折时, 被确认的转折的uti
        zigPrice : 为了方便画图新增的字段, 确认转折时, 被确认的转折的价格
        lastUptUTI : 为了方便画图新增的字段, 更新swingHigh或Low时, 被更新的swingHigh或Low的uti
        lastUptPrice : 为了方便画图新增的字段, 更新swingHigh或Low时, 被更新的swingHigh或Low的价格
    '''
    params = lambda : {
        "featIn": Nothing,
        "retracePct": 2,
    }
    
class ZigStatus(ZigZagMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-04-03 17:56
    Desc  : 
        - ZigZag 状态点
        - 所谓Zig状态点, 是确认Zig的点(swingStatus绝对值=1), 再加上确认前一个折线段继续延长的点(swingStatus绝对值=2)
        - Zig的状态点中包含了Zig所有的有效信息, 原始的ZigZag中每个bar都有occ, 是不正确的(因为信息冗余), 因此包一个正常的特征出来
    Params: 
        zig: zigzag的特征
    Fields:
        swingStatus : swingHigh或者Low状态(0无,1确定向上,2修改向上,-1确定向下,-2修改向下)
        swingPrice : 最近一次swingHigh或者Low的价格
        swingPoivt : 最近一次swingHigh或者Low的价格, 带方向
        swingPosUTI : 最近一次swingHigh或者Low的价格的UTI  
        lastPrice : 上一个SwingHigh或者Low点(LastSwing)处价格
        lastPosUTI : 上一个SwingHigh或者Low点(LastSwing)的UTI
        lastDirection : 上一个SwingHigh或者Low点(LastSwing)方向(1向上,-1向下)
        uti : 当前bar的uti
        zigUTI : 为了方便画图新增的字段, 确认转折时, 被确认的转折的uti
        zigPrice : 为了方便画图新增的字段, 确认转折时, 被确认的转折的价格
        lastUptUTI : 为了方便画图新增的字段, 更新swingHigh或Low时, 被更新的swingHigh或Low的uti
        lastUptPrice : 为了方便画图新增的字段, 更新swingHigh或Low时, 被更新的swingHigh或Low的价格
    '''
    params = lambda : {
        "zig": ZigZag(),
    }
    @property
    def tar_type(self) -> TarType:
        return self.zig.tar_type
    
class ZigConfirm(ZigZagMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-04-03 17:56
    Desc  : 
        - ZigZag 确认点
        - 是确认Zig的点(swingStatus绝对值=1)
    Params: 
        zig: zigzag的特征
    Fields:
        swingStatus : swingHigh或者Low状态(0无,1确定向上,2修改向上,-1确定向下,-2修改向下)
        swingPrice : 最近一次swingHigh或者Low的价格
        swingPoivt : 最近一次swingHigh或者Low的价格, 带方向
        swingPosUTI : 最近一次swingHigh或者Low的价格的UTI  
        lastPrice : 上一个SwingHigh或者Low点(LastSwing)处价格
        lastPosUTI : 上一个SwingHigh或者Low点(LastSwing)的UTI
        lastDirection : 上一个SwingHigh或者Low点(LastSwing)方向(1向上,-1向下)
        uti : 当前bar的uti
        zigUTI : 为了方便画图新增的字段, 确认转折时, 被确认的转折的uti
        zigPrice : 为了方便画图新增的字段, 确认转折时, 被确认的转折的价格
        lastUptUTI : 为了方便画图新增的字段, 更新swingHigh或Low时, 被更新的swingHigh或Low的uti
        lastUptPrice : 为了方便画图新增的字段, 更新swingHigh或Low时, 被更新的swingHigh或Low的价格
    '''
    params = lambda : {
        "zig": ZigZag(),
    }
    @property
    def tar_type(self) -> TarType:
        return self.zig.tar_type
        
class RctZigWithStatus(FrpMixIn, AbstractParamFao):
    '''
    Author: zy
    Since : 2025-04-08 15:51
    Desc  : 
        - 提供最新状态点和最近第1个zig
        - 规定第一个bar是zig点。与`ZigNLengthPoivt`的区别是，只把状态非0的点看作状态点，因此第一个bar被确认为zig时才出现第一个状态点。
        - 只保留首次更新状态点的bar,没有发生变化的bar就不保留
    Params: 
        zig: ZigZag
    Fields:
        price0: 最新状态点价格
        pivot0: 最新状态点带方向价格
        posUTI0: 最新状态点uti
        price1: 最近第1个zig价格
        pivot1: 最近第1个zig带方向价格
        posUTI1: 最近第1个zig的uti
    '''
    params = lambda : {
        "zig": ZigZag(),
    }

    @property
    def tar_type(self) -> TarType:
        return self.zig.tar_type
    def to_df(self):
        dbav1 = self.value.value.root_seq
        df = pd.DataFrame({
            "price0": dbav1['price0'],
            "pivot0": dbav1['pivot0'],
            "posUTI0": dbav1['posUTI0'],
            "price1": dbav1['price1'],
            "pivot1": dbav1['pivot1'],
            "posUTI1": dbav1['posUTI1'],
        }, index=self.value.ts.values)
        return df


class SpeFrp(FrpMixIn, AbstractParamFao):
    '''
    Author: Codex
    Since : 2026-03-31
    Desc  :
        - Spe FRP wrapper.
        - 输入特征的 close 槽位承载 volume，open 槽位承载 opi，uti 保持原样传递。
    Params:
        featIn: 输入特征，默认 Nothing
        speN_: 有限值窗口长度
    Fields:
        value : Spe 当前值
        volumeAvg : 最近 speN_ 个有限 volume 的均值
        opiAvg : 最近 speN_ 个有限 opi 的均值
        dbgVolumeInput : 当前 bar 的 volume 输入
        dbgOpiInput : 当前 bar 的 opi 输入
    '''
    params = lambda : {
        "featIn": Nothing,
        "speN_": 2,
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type
    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        ts_index = self.value.ts.values if hasattr(self.value.ts, "values") else self.value.ts
        df = pd.DataFrame({
            "value": dbav1["value"],
            "volumeAvg": dbav1["volumeAvg"],
            "opiAvg": dbav1["opiAvg"],
            "dbgVolumeInput": dbav1["dbgVolumeInput"],
            "dbgOpiInput": dbav1["dbgOpiInput"],
        }, index=ts_index)
        return df


class MACDFrp(FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-4-17 17:56
    Desc  : 
        - MACD 特征
    Params: 
        featIn: 要计算MACD的特征, 一般是k线收盘价, 要求有uti数据
        fastLen: 快线指数移动平均周期 
        slowLen: 慢线指数移动平均周期 
        macdLen: 快慢线差值的移动平均周期 
    Fields:
        macdFastEMA : 快线指数移动平均
        macdSlowEMA : 慢线指数移动平均
        macdLineValue : 快线 - 慢线 即 MACD
        macdSignalValue : MACD的指数移动平均, 信号线
        macdHistogram : MACD - 信号线
    '''
    params = lambda : {
        "featIn": Nothing,
        "fastLen": 24,
        "slowLen": 70,
        "macdLen": 10,
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        df = pd.DataFrame({
            "macdFastEMA": dbav1['macdFastEMA'],
            "macdSlowEMA": dbav1['macdSlowEMA'],
            "macdLineValue": dbav1['macdLineValue'],
            "macdSignalValue": dbav1['macdSignalValue'],
            "macdHistogram": dbav1['macdHistogram'],
        }, index=self.value.ts)
        return df

class AMAFrp(FrpAdtDfMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: codex
    Since : 2026-01-23 19:55
    Desc  :
        - AMA pdiff value (ratio * 100 - 100)
    Params:
        featIn: 输入特征(需要包含 value/uti)
        effN: AMA 周期
        freq: 频度
    Fields:
        value : AMA pdiff value
        ratio : AMA ratio (amaVal0 / amaVal1)
        amaVal0 : AMA 当前值
        amaVal1 : AMA 上一值
    '''
    params = lambda : {
        "featIn": Nothing,
        "effN": 10,
        "freq": "1d",
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        ts_index = getattr(self.value.ts, "values", self.value.ts)
        df = pd.DataFrame({
            "value": dbav1['value'],
            "ratio": dbav1['ratio'],
            "amaVal0": dbav1['amaVal0'],
            "amaVal1": dbav1['amaVal1'],
        }, index=ts_index)
        return df


class TurtleCapitalRatioFrp(FrpMixIn, AbstractParamFao):
    '''
    Author: Codex
    Since : 2026-03-31 11:31
    Desc  :
        - 基于 ATR 的乌龟仓位比例。
        - 历史 bar 不足 ATR 窗口时输出 NaN；ATR 为 0 时保持 IEEE Infinity。
    Params:
        featIn: 输入 K 线特征，要求包含 open/high/low/close/uti
        atrN: ATR 计算周期
        riskRatio: 风险比例，按百分比参与计算
    Fields:
        value : 乌龟仓位比例
        dbgClose : 当前收盘价
        dbgATR : 当前 ATR 值
    '''
    params = lambda : {
        "featIn": Nothing,
        "atrN": 20,
        "riskRatio": 1,
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type
    

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        ts_index = getattr(self.value.ts, "values", self.value.ts)
        df = pd.DataFrame({
            "value": dbav1["value"],
            "dbgClose": dbav1["dbgClose"],
            "dbgATR": dbav1["dbgATR"],
        }, index=self.value.ts)
        return df

class WaveTurnBack(FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-4-17 17:56
    Desc  : 
        - 滤波器拐头 特征
    Params: 
        featIn: 要计算拐头的特征, 目前写死是MACD. 可以替换输入为任意滤波器TODO.
    Fields:
        value : 拐头, 1向上, -1向下
    '''
    params = lambda : {
        "featIn": Nothing,
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        return self.to_s1()

class AMAAbsLtFrp(FrpAdtDfMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: codex
    Since : 2026-01-23 19:55
    Desc  :
        - AMA 的 pdiff 值绝对值小于阈值
    Params:
        featIn: 输入特征(需要包含 value/uti)
        effN: AMA 周期
        line: 绝对值阈值
        freq: 频度
    Fields:
        value : 是否满足 abs(amaValue) < line, 1/0
        amaValue : AMA 的 pdiff 值
        absValue : amaValue 的绝对值
        lineValue : 阈值
    '''
    params = lambda : {
        "featIn": Nothing,
        "effN": 10,
        "line": 100,
        "freq": "1d",
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        ts_index = getattr(self.value.ts, "values", self.value.ts)
        df = pd.DataFrame({
            "value": dbav1['value'],
            "amaValue": dbav1['amaValue'],
            "absValue": dbav1['absValue'],
            "lineValue": dbav1['lineValue'],
        }, index=ts_index)
        return df


class CapitalManagerFrp(FrpMixIn, AbstractParamFao):
    '''
    Author: Codex
    Since : 2026-03-31 11:31
    Desc  :
        - 资金管理特征。
        - 先计算 TurtleCapitalRatio，再将 NaN 转为 0，并乘以资金常数得到最终值。
    Params:
        featIn: 输入 K 线特征，要求包含 open/high/low/close/uti
        atrN: ATR 计算周期
        riskRatio: 风险比例，按百分比参与计算
        consVal: 资金常数
    Fields:
        value : 最终资金管理值
        dbgCons : 资金常数
        dbgCapitalManagerRatio : NaN 转 0 后的仓位比例
        dbgRawTurtleCapitalRatio : 原始乌龟仓位比例
        dbgClose : 当前收盘价
        dbgATR : 当前 ATR 值
    '''
    params = lambda : {
        "featIn": Nothing,
        "atrN": 20,
        "riskRatio": 1,
        "consVal": 1,
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type
    

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        df = pd.DataFrame({
            "value": dbav1["value"],
            "dbgCons": dbav1["dbgCons"],
            "dbgCapitalManagerRatio": dbav1["dbgCapitalManagerRatio"],
            "dbgRawTurtleCapitalRatio": dbav1["dbgRawTurtleCapitalRatio"],
            "dbgClose": dbav1["dbgClose"],
            "dbgATR": dbav1["dbgATR"],
        }, index=self.value.ts)
        return df

class PrecipitationFundsFeat(FrpAdtDfMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-07-11 17:56
    Desc  : |
        品种沉淀资金特征
        沉淀资金 = 持仓量 * 最新价(收盘价) * 单位手数 * 保证金比例(固定为10%，是个估计值)
    Params: 
        freq: 频率
    '''
    params = lambda : {
        "freq": "30m",
    }

    @property
    def tar_type(self) -> TarType:
        return CalendarTarType(SymTarType())
    
    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []
    
    def to_df(self):
        event_name = "value"
        fields_map = {
            "value": "unPrecipitationFunds",
        }
        index_depth = 1
        return self._gen_df_from_event(event_name = event_name, fields_map = fields_map, index_depth = index_depth)

class TurnoverRateFeat(FrpAdtDfMixIn, FrpMixIn, AbstractParamFao):
    '''
    Author: cyf
    Since : 2025-07-11 17:56
    Desc  : |
        换手率特征
        换手率 = 成交量 / 持仓量
    Params: 
        freq: 频率
    '''
    params = lambda : {
        "freq": "30m",
    }

    @property
    def tar_type(self) -> TarType:
        return CalendarTarType(SymTarType())
    
    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []
    
    def to_df(self):
        event_name = "value"
        fields_map = {
            "value": "unTurnoverRate",
        }
        index_depth = 1
        return self._gen_df_from_event(event_name = event_name, fields_map = fields_map, index_depth = index_depth)


class SpeGtFrp(FrpMixIn, AbstractParamFao):
    '''
    Author: Codex
    Since : 2026-03-31
    Desc  :
        - SpeGt FRP wrapper.
        - 对上游 Spe 数值做阈值比较，并保留当前 Spe 值与阈值线便于排查。
    Params:
        featIn: 输入特征，默认 Nothing
        speN_: 有限值窗口长度
        line: 阈值线
    Fields:
        value : Spe 是否大于 line 的输出
        speValue : 当前 Spe 数值
        dbgLine : 当前阈值线
    '''
    params = lambda : {
        "featIn": Nothing,
        "speN_": 2,
        "line": 0,
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        ts_index = self.value.ts.values if hasattr(self.value.ts, "values") else self.value.ts
        df = pd.DataFrame({
            "value": dbav1["value"],
            "speValue": dbav1["speValue"],
            "dbgLine": dbav1["dbgLine"],
        }, index=ts_index)
        return df


class SpeGtBlockRatioCurrentContextFrp(BaseBlockFrpFao):
    '''
    Author: Codex
    Since : 2026-05-07
    Desc  :
        - 板块级 SpeGt 当前上下文占比聚合特征。
        - 读取上游单品种 `value` 事件，在当前板块内对有限值做逐 bar 求和。
    Params:
        tar: 输入的单品种 SpeGt 类 FRP 特征，要求其 `value` 事件可被板块聚合
    Fields:
        value : 当前 bar 板块内所有成分品种 `value` 的有限值求和结果
    '''
    params = lambda : {
        "tar": Nothing,
    }

    @property
    def tar_type(self) -> TarType:
        blk = self.blk_expr
        if blk is NoValue:
            return CalendarTarType(UnKnownBlockTarType())

        if not blk:
            raise Exception(f"{self.ppname} blk_expr cannot be None")
        return CalendarTarType(BlockTarType(blk))

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        df = pd.DataFrame({
            "value": dbav1["value"],
        }, index=self.value.ts)
        return df


SpeGtBlockRatioCurrentContext = SpeGtBlockRatioCurrentContextFrp


class HPLtFrp(FrpMixIn, AbstractParamFao):
    '''
    Author: Codex
    Since : 2026-04-07
    Desc  :
        - 横盘阈值比较特征。
        - 直接消费上游 HP 特征的 hpValue，并按 threshold 做小于比较，输出 1/0。
    Params:
        featIn: 输入特征，默认 Nothing
        threshold: 横盘阈值
    Fields:
        value : hpValue < threshold 时为 1，否则为 0
        hpValue : 当前 bar 的横盘值
        threshold : 当前使用的阈值
    '''
    params = lambda : {
        "featIn": Nothing,
        "threshold": 0,
    }

    @property
    def tar_type(self) -> TarType:
        return self.featIn.tar_type

    def doFrpUpSource(self):
        """不去自动运行输入特征"""
        return []

    def to_df(self):
        dbav1 = self.value.value.root_seq
        df = pd.DataFrame({
            "value": dbav1["value"],
            "hpValue": dbav1["hpValue"],
            "threshold": dbav1["threshold"],
        }, index=self.value.ts)
        return df

AMA = AMAFrp
AMAAbsLt = AMAAbsLtFrp
FrpTurtleCapitalRatio = TurtleCapitalRatioFrp
FrpCapitalManager = CapitalManagerFrp
TurtleCapitalRatio = TurtleCapitalRatioFrp
CapitalManager = CapitalManagerFrp
HPLt = HPLtFrp
