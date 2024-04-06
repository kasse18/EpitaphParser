import json

import aiohttp
import asyncio
import pandas as pd
from bs4 import BeautifulSoup


async def get_epitaph(session, n):
    if n == 23116076:
        n = 82804538
    async with session.get(f'https://memorycode.ru/page/{n}', ssl=False) as resp:
        print(n)
        if resp.status == 200:
            text = await resp.read()
            epitaph = BeautifulSoup(text.decode('utf-8'), 'html5lib').find('div', class_='m-comment__text')
            if epitaph is not None:
                print(epitaph.text)
                # text = pd.DataFrame([text]).to_excel('./epitaph.xlsx')
                data.append(epitaph.text)
                # with open('state-data.csv', 'a', newline='') as state_file:
                #     writer = csv.writer(state_file)
                #     writer.writerow([text])
# 82804532
async def main():
    for i in range(45000):
        async with aiohttp.ClientSession(trust_env=True) as session:
            await asyncio.gather(*[
                asyncio.ensure_future(get_epitaph(session, item))
                for item in range(10000000+i*200, 10000000+(i+1)*200)
            ])

data = []

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())

print(data)
pd.DataFrame(data).to_excel('./epitaph.xlsx')
