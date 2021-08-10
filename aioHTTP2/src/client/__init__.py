import asyncio
from src.store.tasks import addItem , getItem

async def main():
    while True:
        tokens = getItem()
        print('tokens are : ')
        print(tokens)
        await asyncio.sleep(5)      