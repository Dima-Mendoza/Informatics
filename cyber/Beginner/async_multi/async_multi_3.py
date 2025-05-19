import aiohttp
import asyncio

url_adresses = ['https://example.com/', 'https://google.com/']

async def len_html(url):
    html = await get_html(url)
    print(f"{url} len is {len(html)}")

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_html(url_adr='https://google.com'):
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url_adr)

async def main():
    task1 = asyncio.create_task(get_html(url_adresses[0]))
    task2 = asyncio.create_task(get_html(url_adresses[1]))
    task3 = asyncio.create_task(len_html(url_adresses[1]))
    task4 = asyncio.create_task(len_html(url_adresses[0]))
    await asyncio.gather(task1, task2, task3, task4)


asyncio.run(main())
