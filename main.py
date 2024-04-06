import aiohttp
import asyncio
import bs4
import html5lib
from bs4 import BeautifulSoup


async def get_epitaph(session, n):
    async with session.get(f'https://memorycode.ru/page/{n}', ssl=False) as resp:
        if resp.status == 200:
            text = await resp.read()
            text = BeautifulSoup(text.decode('utf-8'), 'html5lib').find('div', class_='m-comment__text').text
            if text is not None:
                data.append(text)
                print(text)


async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        await asyncio.gather(*[
            asyncio.ensure_future(get_epitaph(session, item))
            for item in range(10000000, 100000000)
        ])

data = []
# 81481691
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())