import asyncio

async def main():
    # Wait for 30 secons => i equals 6
    i = 6
    while i > 0:
        await asyncio.sleep(5)
        print("5 Seconds!")
        i -= 1


if __name__ == "__main__":
    asyncio.run(main())