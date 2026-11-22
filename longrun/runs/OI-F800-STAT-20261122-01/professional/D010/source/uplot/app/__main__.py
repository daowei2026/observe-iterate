import sys, os


from aiohttp import web
import bokeh

from .plot import *


app = web.Application()

bokeh_dir = os.path.dirname(bokeh.__file__)
static_dir = os.path.join(bokeh_dir, "server", "static")
app.router.add_static("/static/bokeh/", path=static_dir, name="bokeh")

app.router.add_get(
    "/draw/plot/{feature}/{ablename}",
    lambda req: gen_feature_cae_html(req, cached=True),
)
app.router.add_get(
    "/redraw/plot/{feature}/{ablename}",
    lambda req: gen_feature_cae_html(req, cached=False),
)


http_port = 5080
try:
    if len(sys.argv) > 1:
        http_port = int(sys.argv[1])
except ValueError:
    pass

web.run_app(app, port=http_port)
