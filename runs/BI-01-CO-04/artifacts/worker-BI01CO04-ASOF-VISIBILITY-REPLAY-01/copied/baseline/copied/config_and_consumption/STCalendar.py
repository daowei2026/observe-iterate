from ..lib3 import *
import pandas as pd

__all__ = [
  "ScaleTurnCalendar",
  "FiltedScaleTurnCalendar",
]

# 把贴近转折的adt结果转成DataFrame
# 不能在此处合并，否则因为两个df长度不一致，为了填充nan值会强制把int类型转换为float类型
def _scaleTurnValueADT2DF(value, prefix):
    columns = [
        f'{prefix}.x',
        f'{prefix}.y',
        f'{prefix}.xConfirm',
        f'{prefix}.yConfirm',
    ]
    if len(value.ts) == 0:
        # 零 occurrence 是正常业务结果。底层此时是 EmptyDbaStruct，
        # 没有 actual2D/confirm2D 字段；仍应返回合同完整的空表。
        return pd.DataFrame(columns=columns, index=value.ts).astype({
            columns[0]: 'int64',
            columns[1]: 'float64',
            columns[2]: 'int64',
            columns[3]: 'float64',
        })

    dba_value = value.value.root_seq
    return pd.DataFrame({
        columns[0]: dba_value['actual2D']['x'],
        columns[1]: dba_value['actual2D']['y'],
        columns[2]: dba_value['confirm2D']['x'],
        columns[3]: dba_value['confirm2D']['y'],
    }, index=value.ts)


def scaleTurnADT2DF(self):
    df1 = _scaleTurnValueADT2DF(self.value1, 'value1')
    df2 = _scaleTurnValueADT2DF(self.value2, 'value2')
#     dfs = [df1, df2]
#     return pd.concat(dfs, axis=1, join="outer")
    return {"value1":df1,"value2":df2}

class ScaleTurnCalendar(FrpMixIn, AbstractParamFao):
    '''
    Author: zy
    Since : 2025-04-08 16:08
    Desc  : 
        - 指定尺度贴近增益的转折，且支持在指定日历上计算。 
        - 贴近增益, 上一个已确认的贴近转折，与检查点的中间，如果增加1个贴近转折点，从直线段变成折线段，和k线变得更加贴近，与k线贴近程度的增加叫做贴近增益。
        - 当贴近增益在指定尺度上的隶属度大于阈值则被确认为新的贴近转折。
        - 注意是指定尺度的隶属度，而不是大于等于指定尺度的隶属度。比如指定尺度为M,大尺度增益在M的隶属度就偏低，不会被识别出来。
        - 共进行两轮对贴近转折的筛选，两轮结果分别是
        - 第一轮贴近转折, 从头开始过所有转折备选点，直到选出1个贴近增益足够大的备选，就成为第一轮贴近转折。
        - 第二轮贴近转折, 从第一轮贴近转折之后的转折备选点开始过，再选出1个贴近增益足够大的备选。如果无法再选出来，保留第一轮的结果。
        - 转折备选点, 使用最新1个被确认的zig,原因是zig可以覆盖外凸的转折点,且zig只要不太大,对内凹转折点也有一定覆盖.(外凸是波峰波谷,内凹是波峰波谷之间速度变化的点)
        - 检查点, 触发时检查备选点的满足情况.使用最新的zig状态点,业务上表示更新了价格的可能拐头点,则可能提高了增益,需要重新检查,为了减轻延迟,检查点使用更小的转折百分比.
    Params: 
        stCloseGainController: 贴近程度增益控制器
        stMembershipLine: 指定尺度贴近增益的隶属度阈值
        stRnd2ChooseTurn: 第二轮的选择方式
        specTerm: 指定尺度的模糊语义
        falter: 转折的备选点
        fcheck: 检查点
        fisSystem: 控制系统
    Example:
        ZigZag["small"] = lambda:{
            "featIn" : MapKLineOpenData(freq="30m") % ("value.open_uti as uti", "value.close as value"), 
            "retracePct" : 0.5
        }
        ScaleTurnCalendar["mid"] = lambda: {    
            "stCloseGainController": BscCloseGainController()@"test",
            "stMembershipLine": plist([0.3,0.4,0.5,0.6,0.7]),
            "stRnd2ChooseTurn": ChooseMaxExtraPoint(),
            "specTerm": "M",
            "falter": RctZigWithStatus(zig=ZigZag()@"small"),
            "fcheck": RctZigWithStatus(zig=ZigZag()@"small"),
            "fisSystem": T1FisSystem()@"scaleturn_gauss",
        }
    '''
    params = lambda : {
        "stCloseGainController": Nothing,
        "stMembershipLine": 0.5,
        "stRnd2ChooseTurn": Nothing,
        "specTerm": "",
        "falter": Nothing,
        "fcheck": Nothing,
        "fisSystem": Nothing,
    }
    @property
    def tar_type(self) -> TarType:
        return self.falter.tar_type
    
    def to_dfs(self):
        return scaleTurnADT2DF(self)
    
    def to_df(self):
        dfs = self.to_dfs()
        df1 = dfs["value1"]
        df2 = dfs["value2"]

        # 确保两个DataFrame有相同的列名
        df1.columns = ['x', 'y', 'xConfirm', 'yConfirm']
        df2.columns = ['x', 'y', 'xConfirm', 'yConfirm']
        
        # 按行合并两个DataFrame (axis=0)
        df = pd.concat([df1, df2], axis=0, join="outer")

        # 先按时间索引排序，然后对于同一时间点的数据按x值排序
        df = df.sort_values(by=['x'], kind='stable').sort_index(kind='stable')

        return df
class FiltedScaleTurnCalendar(FrpMixIn, AbstractParamFao):
    '''
    Author: zy
    Since : 2025-04-08 16:17
    Desc  : 
        - 过滤后的指定尺度贴近转折
        - 过滤目标是第一轮贴近转折，过滤的逻辑是: 
        - 在上一次确认的贴近转折，与新确认的第二轮贴近转折之间，让新确认第一轮的点作为中间点，再判断一次增益，如果增益过小则滤掉第一轮转折，只保留第二轮转折。
    Params: 
        formTurn: 两轮指定尺度贴近增益的转折
        filtTurn: 过滤两轮的函数
    Example:
        FiltedScaleTurnCalendar["mid"] = lambda:{
            "formTurn": ScaleTurnCalendar()@"mid",
            "filtTurn": FiltScaleTurnByCloseGain()@"mid_large", 
        }
    '''
    params = lambda : {
        "formTurn": ScaleTurnCalendar(),
        "filtTurn": Nothing, 
    }
    @property
    def tar_type(self) -> TarType:
        return self.formTurn.tar_type
    def to_dfs(self):
        return scaleTurnADT2DF(self)
    def to_df(self):
        dfs = self.to_dfs()
        df1 = dfs["value1"]
        df2 = dfs["value2"]
        df = pd.concat([df1,df2], axis=1, join="inner")
        return df
