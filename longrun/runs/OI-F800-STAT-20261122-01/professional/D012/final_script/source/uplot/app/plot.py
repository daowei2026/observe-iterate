__all__ = [
    "gen_feature_cae_html",
]


import traceback
import os
from aiohttp import web
from bokeh.embed import components
from mquant.frame import eval2
from mquant.apt import mkdirs


async def gen_feature_cae_html(request, cached=True):
    try:
        feature = request.match_info.get("feature")
        ablename = request.match_info.get("ablename")

        plot = eval2(feature)(ablename)(
            **{k: eval(v) for k, v in request.query.items()}
        )

        full_dir = plot.full_dir
        mkdirs(full_dir)
        print(f"保存路径： {full_dir}")
        script_path = os.path.join(full_dir, "plot.script")
        div_path = os.path.join(full_dir, "plot.div")
        if cached and os.path.exists(script_path) and os.path.exists(div_path):
            print("读取已有结果")
            with open(script_path, "r") as f:
                script = f.read()
            with open(div_path, "r") as f:
                div = f.read()
        else:
            print("生成结果并保存")
            script, div = components(plot.layout(ncols=1))
            with open(script_path, "w") as f:
                f.write(script)
            with open(div_path, "w") as f:
                f.write(div)

        # 备注
        description = plot.__doc__

        # Wrap the Bokeh plot with HTML
        html = f"""
        <html>
            <head>
                <script src="/static/bokeh/js/bokeh.min.js"></script>
                <script src="/static/bokeh/js/bokeh-widgets.min.js"></script>
            </head>
            <body>
                <div>{description}</div>
                {div}
                {script}
            </body>
        </html>
        """
        print(f"生成成功...")
        return web.Response(text=html, content_type="text/html")
    except Exception as e:
        print(e)
        traceback.print_exc()
        return web.Response(text=f"生成失败:{e}", status=500)
