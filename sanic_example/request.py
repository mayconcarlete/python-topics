import asyncio
from asyncio.tasks import gather
import aiohttp
from typing import List


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            body = await response.json()
            print(f'requesting...{url}')
            return body

async def coroutine(urls: List[str]):
    requests = []
    for url in urls:
        requests.append(asyncio.create_task(request(url)))
    response = await asyncio.gather(*requests)
    return response


async def multiple_requests(urls: List[str]):
    response = await coroutine(urls)
    return response
