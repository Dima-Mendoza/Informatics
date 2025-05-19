import aiohttp
import asyncio

url_adresses = ['https://example.com/', 'https://google.com/']

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        #asyncio.gather()
        html = await fetch(session, 'https://google.com')
        print(html)

asyncio.run(main())
