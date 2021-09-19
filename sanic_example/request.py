import asyncio
from asyncio.tasks import gather
import aiohttp
from typing import List


# async def request(url: str):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             body = await response.json()
#             return body

# async def coroutine(urls: List[str]):
#     requests = []
#     for url in urls:
#         requests.append(url)
#     response = await asyncio.gather(*requests)
#     return response


# async def multiple_requests(urls: List[str]):

    # body = asyncio.run(coroutine(urls))
    # return body

    # return await asyncio.run(coroutine(urls))

    # return coroutine(urls)
    # return await coroutine(urls)

    # loop = asyncio.get_event_loop()
    # body = loop.run_until_complete(coroutine(urls))
    # return body



# USANDO THREADPOOL

import requests
from concurrent.futures import ThreadPoolExecutor

def get_response(url):
    body = requests.get(url).json()
    return body

def multiple_requests(urls: List[str]):
    with ThreadPoolExecutor(max_workers=10) as pool:
        response_list = list(pool.map(get_response, urls))
        return response_list
