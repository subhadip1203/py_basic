
from aiohttp import web
from .server import app

async def start_app():
    host ='localhost'
    port = 8020
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner,host, port)
    await site.start()
    print(f"Serving up app on http://{host}:{port}")