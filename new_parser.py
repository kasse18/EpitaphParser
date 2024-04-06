import json
import time

import aiohttp
import asyncio
import pandas as pd
from bs4 import BeautifulSoup


async def get_epitaph(session):
    async with (session.get(f'https://memorycode.ru/api/pages/random-previews', ssl=False) as resp):
        if resp.status == 200:
            text = await resp.json()
            text = text[0]['epitaph']
            if text is not None:
                data.append(text)


async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        await asyncio.gather(*[
            asyncio.ensure_future(get_epitaph(session))
            for item in range(100)
        ])

data = []

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())

print(data)
pd.DataFrame(data).to_excel('./epitaph.xlsx')
