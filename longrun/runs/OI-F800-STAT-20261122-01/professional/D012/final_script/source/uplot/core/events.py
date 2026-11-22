from bokeh import events
from bokeh.plotting import figure
from bokeh.models import CustomJS

__all__ = ["bind_adjXY_event"]


def bind_adjXY_event(fig: figure, x_offs: int, n: int, kline_sources: list, xy_sources: list = None,std_method="ratio"):
    """
    绑定动态标准化主图Y轴事件
    :param fig: figure
    :param x_offs: x 偏移值
    :param n: 数据长度
    :param kline_sources: K线数据源
    """
    JSCODE = """
            function nanmax(arr){
                arr = arr.filter(item => !isNaN(item) && item != null)
                return arr.length ? Math.max.apply(null, arr) : undefined
            }

            function nanmin(arr){
                arr = arr.filter(item => !isNaN(item) && item != null)
                return arr.length ? Math.min.apply(null, arr) : undefined
            }
            
            function adjXRangeEvent() {
                let start = fig.x_range.start - x_offs;
                let start_x = Math.ceil(start);
                if(start_x < 0) start_x = 0;
                if(start_x >= n) start_x = n - 1;

                let end = fig.x_range.end - x_offs;
                let end_x = Math.ceil(end);
                if(end_x >= n) end_x = n - 1;

                let len = end_x - start_x + 1;
                
                let sym_std = {}                
                let adj_max_y = null;
                let adj_min_y = null;
                for (let i in kline_sources) {
                    let each = kline_sources[i];
                    let source = each.source;
                    let sym = each.sym;
                    let data = source.data;

                    let bl = std_method == "ratio-back" ? data["close"][end_x] : data["open"][start_x];
                
                    for (let j = start_x; j <= end_x; j++){
                        if(isNaN(bl)){
                            if(std_method != "ratio-back"){ // TODO: ratio-back
                                bl = data["open"][j];
                            }
                        }
                        data["o"][j] = data["open"][j] / bl;
                        data["h"][j] = data["high"][j] / bl;
                        data["l"][j] = data["low"][j] / bl;
                        data["c"][j] = data["close"][j] / bl;
                        
                        data["y"][j] = (data["o"][j] + data["c"][j]) / 2;
                    }
                    
                    // 获取当前Y轴的最大最小值
                    const cur_data = data["y"].slice(start_x,end_x);
                    
                    adj_max_y = nanmax([adj_max_y,nanmax(cur_data)]);
                    adj_min_y = nanmin([adj_min_y,nanmin(cur_data)]);
                    
                    sym_std[sym] = bl
                    source.change.emit();
                }

                // K线上的其他图
                if(xy_sources){
                    for (let i in xy_sources) {
                        let each = xy_sources[i];
                        let source = each.source;
                        let sym = each.sym;
                        let data = source.data;
                        let bl = sym_std[sym];
                        
                        ['y','y0','y1'].forEach(function(y,index,self){
                            let ydata = data[y];
                            if(ydata){
                                for (let j = 0; j < ydata.length; j++){
                                    ydata[j] = data[y + '_data'][j] / bl;
                                }
                            }
                        });
                        source.change.emit();
                    }   
                }

                // 当前Y轴的最大最小值,放大缩小
                setTimeout(()=>{ // y_range change may fail if set immediately here
                    const adj_y = (adj_max_y - adj_min_y) * 0.1;
                    fig.y_range.start = adj_min_y - adj_y;
                    fig.y_range.end = adj_max_y + adj_y;
                }, 20);
            }

            const adjXRangeEventSymbol = Symbol.for('adjXRangeEvent');
            clearTimeout(fig[adjXRangeEventSymbol]);
            fig[adjXRangeEventSymbol] = setTimeout(adjXRangeEvent, 50);
        """

    fxr = fig.x_range
    jsh = CustomJS(
        args=dict(
            kline_sources=kline_sources,
            xy_sources=xy_sources,
            x_offs=x_offs,
            n=n,
            fig=fig,
            std_method=std_method
        ),
        code=JSCODE,
    )
    fxr.js_on_change("start", jsh)
    fxr.js_on_change("end", jsh)
