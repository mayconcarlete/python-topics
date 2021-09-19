import asyncio
import aiohttp


async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            body = await response.json()
            return body

async def coroutine():
    tasks = []
    tasks.append(
        asyncio.create_task(request('https://api.pokemontcg.io/v2/cards?q=name:gardevoir'))
    )
    tasks.append(
        asyncio.create_task(request('https://fakerapi.it/api/v1/addresses?_quantity=1'))
    )
    result = await asyncio.gather(*tasks)
    print(result)

def main():
    asyncio.run(coroutine())

if __name__ == '__main__':
    main()
