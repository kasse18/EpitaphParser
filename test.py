import aiohttp
import asyncio
import pandas as pd
from bs4 import BeautifulSoup


async def get_epitaph(session, n):
    print(n)
    async with session.get(f'https://memorycode.ru/page/{n}', ssl=False) as resp:
        if resp.status == 200:
            text = await resp.read()
            text = BeautifulSoup(text.decode('utf-8'), 'html5lib').find('div', class_='m-comment__text').text
            if text is not None:
                # text = pd.DataFrame([text]).to_excel('./epitaph.xlsx')



                # data.append(text)
                # print(text)
                # with open('state-data.csv', 'a', newline='') as state_file:
                #     writer = csv.writer(state_file)
                #     writer.writerow([text])


# 82804532
async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        await asyncio.gather(*[
            asyncio.ensure_future(get_epitaph(session, item))
            for item in range(81481791, 82804535)
        ])

data = []

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())

print(data)