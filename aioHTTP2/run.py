

from aiohttp import web
import asyncio
from server.server import main ,start_app
# import counter
import store.tasks as tasks

async def start_async_app():
    await asyncio.gather(*[ main(), start_app() ])



if __name__ == "__main__":    
    tasks.init()
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(start_async_app())
    except KeyboardInterrupt:
        print('\nStopping Application ....')        
        for task in asyncio.all_tasks(loop):
            task.cancel()
        loop.run_until_complete(loop.shutdown_asyncgens())
    except asyncio.CancelledError:
        print("Gather was cancelled")   
    finally:
        print("Application Stopped ....")
        loop.close()