import asyncio
import random
import time


async def coroutine_task(iteraction):
    process_time = random.randint(1,5)
    print(f'Time: {process_time}')
    await asyncio.sleep(process_time)
    print(f'Iteração {iteraction}, tempo decorrido: {process_time}')

async def corountine():
    tasks = []
    for i in range(10):
        tasks.append(
            asyncio.create_task(coroutine_task(i))
        )
    await asyncio.gather(*tasks)


def main():
    asyncio.run(corountine())


if __name__ == '__main__':
    main()