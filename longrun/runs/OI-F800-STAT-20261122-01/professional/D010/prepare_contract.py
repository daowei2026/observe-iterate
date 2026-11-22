from pathlib import Path
import json

R=Path(__file__).resolve().parent
def save(n,v):(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def identity(prefix):return {k:prefix+'_'+v for k,v in dict(form='idForm',high='idHigh',low='idLow',text='idText').items()}
gm=dict(life=identity('groupReference_referenceLife'),revision=identity('groupReference_referenceRevision'),
    known='groupKnownFrom',original_anchor='groupOriginalAnchor',original_d='groupOriginalDeadline',original_r='groupOriginalRevisionEnd',
    anchor='groupAnchor',d='groupDeadline',r='groupRevisionEnd',basis='groupLocalBasis_name',observation='groupObservation_name',
    coverage='groupCoverageIncomplete',closed='groupClosed')
template=dict(parents=['timestamp','occurrence','record_id','child_id_2'],groups=gm,
    kline={k:k for k in ('open','high','low','close','volume','openUti','closeUti')},
    selected=dict(actual='actual',confirmation='confirmation',known='known',price='price',cprice='confirmation_price',round='round_display',
                  turn='turn_id',source_round='round',t_known='raw_known'),
    raw=dict(actual='posUTI1',price='price1',event_timestamp='timestamp'),
    labels={},participation=dict(table='occurrences_groupFormationParticipation',duty='participationDutyClosed',
        admission='participationAdmissionKnown',handoff='participationHandoffEnd'),
    limits=['当前U为PARTIAL；逐tick材料准入、未成组pair/组合、first blocker、原生coverage区间NOT_EXPOSED。',
            '仅公开/已物化结果的历史位置投影；未发行revision的tick不能补成连续状态。',
            '成员子表不是所有未选转折分母。可选子表空不等于0或失败。'])
save('FIELD_MAP_TEMPLATE.json',{'用途':'D正式绑定时核对的字段模板；当前HTML使用独立合成字段映射。模板不绑定实例/SOF/结果路径/位置。',
 '来源':'D008 PUBLIC_TABLE_SCHEMA与独立读回CSV列名、已接受的上游/scale_turns公开形状。',
 'fields':template,
 '适配说明':[
   'groups以occurrences公开表为源。_name列是已接受读回的枚举名称；若真实reader只有数值码，映射原码并提供已核实labels，不按字段名猜测。',
   'UUID Form=1用无损high/low组合，Form=2保留文本；主组不得Form=0。禁止先读成浮点再转回。',
   'selected需由同参数ScaleTurnCalendar value1/value2原事件轴准备known；不能把几何confirm/T.pointKnownFrom替代selected已知轴。',
   'canonical selected输入可来自合法只读native reader，或已接受D008上游/规范化公开形状。round_display=0/1只是显示偏移；保留原value1/value2或原round字段。',
   '当前26列scale_turns为G已保存的公开投影，不能把其中eligible_*_reference/first_block_screen当成原F材料轨迹；所有额外字段只作原值来源标识，不升格。',
   'raw使用已暴露Rct实际位置/价；不补造未识别市场转折或全分母；其事件timestamp保留。',
   'PUBLIC_TABLE_SCHEMA之外的source P/T/C、known字段须由D给出真实reader映射和来源；C不签正式数据可用。']})
save('INJECTION_CONTRACT.json',{'代码编号版本':'F800-C3-v1','对应C2当前预期版本':'F800-C2-v4',
 'Python代码引用':'display_code/caegraph_display.py','入口':'build_display(*, instance, reader, context, position, fields, caption) -> (Bokeh layout, metadata)',
 '实例注入接口':{'instance':'任意真实外层实例/结果绑定对象；只传给调用方reader。C3没有导入具体Feature。',
     'reader':'reader(instance, position) -> 已物化DataFrame映射。必须只读；不能在本C3接口内触发正式Feature计算/生产。',
     'context':'调用方提供兼容CAEGraph Context的上下文，需具有sof及当前calendar自然TSA；SOF由D绑定。'},
 '位置注入接口':{'必填':['symbols（非空列表）','start','end','calendar'],
     '可选':['width','label_freq','position_id/scale（传递给reader/调用方caption，不改变业务字段）'],
     '边界':'支持日历时间标签或整型UTI，按PlotCtx含结束标签处理。D须正式解释B日期粒度及交易日历边界，不以C2样例日期替代B。',
     '多位置多尺度':'D对每个已批准位置调用同一build_display，传入该位置与其输入映射，组合返回布局；不在C3内挑位置、时间或正式案例。'},
 '字段注入接口':{'groups':'life/revision、known、original_anchor/original_d/original_r、anchor/d/r、basis/observation/coverage/closed，全部由fields.groups映射。identity可为列名或form/high/low/text四列配置。',
     'kline':'fields.kline将实际OHLC/volume/openUti/closeUti映射到标准绘图列；保留DatetimeIndex。NaN不填补。',
     'selected':'fields.selected映射actual/confirmation/known、price/cprice、round数值显示编码及turn等原值；其他原始字段仍保存在__original_json。',
     'raw':'fields.raw至少映射actual/price，全部原始字段仍保存。',
     'parents':'完整组父前缀字段列表，当前版本为timestamp/occurrence/record_id/child_id_2；子表保留所有更深child字段。',
     'labels':'数值basis/observation必须提供同版已核实的名称映射；原数值在原始明细保留。',
     'participation':'指定子表名称及duty/admission/handoff原字段；可以有多条子行，逐行数组保留，不取首条冒充单值。',
     '模板':'FIELD_MAP_TEMPLATE.json，仅形状/字段示例，不是已完成的D绑定。'},
 'reader返回值':{'klines':'{symbol: DatetimeIndex DataFrame}', 'selected':'{symbol: DataFrame（含实际/确认/上游事件已知及原值）}',
     'raw':'{symbol: DataFrame（已暴露Rct）}', 'groups':'DataFrame，父坐标在列或命名MultiIndex；主组父键唯一。',
     'children':'{table_name: DataFrame}，仅本主组occurrences根下子表，完整父前缀及所有child层级，不按时间单独拼接。',
     'metadata':'非group根的definitions/publication/其他公开表及配置/实例/字段/理解引用、可用状态等JSON可序列化原值。D需记录完整来源。'},
 '空值与安全失败':['空groups可以是definitions-only publication，不造输出点；空表必须保留已声明列及类型。',
     '可选子列表空、无participation为NOT_PUBLISHED；不是0、Invalid或失败。',
     '缺字段、主组父键重复、子行孤立、身份缺失/浮点ID、无损UTI类型不合或a/d/r次序冲突直接报错，不自动补齐/合并。'],
 '显示派生':['修订显示行=known和完整父坐标稳定排序后的序号；无业务数值含义，不按UUID排序。',
     '输入known附图纵轴=品种序号+0.15×round，明确标示显示偏移。',
     '区间只在显示层裁剪并作端点插值；原始a/d/r及P/T/C原值和裁剪标记保留；不把携带界限当成逐tick持续状态。',
     'UUID解码只变表示；原字段及64位整数JSON以文本嵌入，浏览器不解析成浮点数。'],
 '预览实例绑定':'PREVIEW_BINDING_v4.json；无真实Feature绑定，合成业务值，日历只读。',
 '是否固化外层实例':'否','是否固化B最终位置':'否','C3是否另生成预期HTML':'否，沿用html/current.html',
 '交付边界':'C3具体代码可运行，但本C不代D正式实例/位置/字段集成，不代E最终核图和正式取数。'})
print('注入合同和当前原生Schema字段模板已形成')
