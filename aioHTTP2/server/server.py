from aiohttp import web
import asyncio
import random
from state.counter import queue

async def main():
    while True:
        global queue 
        token = await queue.get()
        print('number is '+token)
        await asyncio.sleep(5)        


# server part
async def handle(request):
    global queue 
    token = random.random()
    await queue.put(token)
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

async def start_app():
    host ='localhost'
    port = 8020
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner,host, port)
    await site.start()
    print(f"Serving up app on http://{host}:{port}")
   


