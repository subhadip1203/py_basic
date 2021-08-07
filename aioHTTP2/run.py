

from aiohttp import web
import asyncio
from server.server import main ,start_app

async def start_async_app():
    await asyncio.gather(*[ main(), start_app() ])



if __name__ == "__main__":    

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(start_async_app())
    except KeyboardInterrupt:
        print('\nStopping Application ....')
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        print("Application Stopped ....")
        loop.close()