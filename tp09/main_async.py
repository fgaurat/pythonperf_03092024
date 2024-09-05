import asyncio
import threading
import time


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()

    # a = await add(5,6)
    # print(a)
    # b = await add(5,6)
    # print(b)
    # c = await add(5,6)
    # print(c)
    all = [add(5,6),add(5,6),add(5,6)]

    r = await asyncio.gather(*all)
    end = time.perf_counter()
    print(f"{end-start:.3}")    
if __name__=='__main__':
    #main()

    asyncio.run(main())

