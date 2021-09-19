import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.pokemontcg.io/v2/cards?q=name:gardevoir') as response:
            print(f'Status: {response.status}')
            print(f'Content-type: {response.content_type}')
            print('Printing body...')
            body = await response.text()
            print(body)


if __name__ == '__main__':

    # diferença entre a primeira e a segunda abordagem
    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
