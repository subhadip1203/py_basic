from aiohttp import web
import asyncio



num_add = 1

async def main():
    while True:
        print('number is '+str(num_add))
        await asyncio.sleep(5)        

async def handle(request):
    global num_add 
    num_add +=1
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
   

async def start_async_app():
    await asyncio.gather(*[
        main(), start_app()
    ])

loop = asyncio.get_event_loop()
runner, site = loop.run_until_complete(start_async_app())
try:
    loop.run_forever()
except KeyboardInterrupt as err:
    loop.run_until_complete(runner.cleanup())