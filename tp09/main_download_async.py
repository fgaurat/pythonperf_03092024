import threading
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import concurrent.futures
import asyncio
import httpx 
import aiohttp 


async def download(url,log_file):
    # print(threading.current_thread().name)
    # download url_file_name
    resp = requests.get(url)
    content = resp.text
    # write content to file_name
    with open(log_file,'w') as f:
        f.write(content)

async def download_requests(url,log_file):
    loop = asyncio.get_event_loop()
    resp = await loop.run_in_executor(None, requests.get, url)
    content = resp.text
    # write content to file_name
    with open(log_file,'w') as f:
        f.write(content)

async def download_httpx(url,log_file):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        content = resp.text
        # write content to file_name
        with open(log_file,'w') as f:
            f.write(content)

async def download_aiohttp(url,log_file):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content =await  resp.text()
            # write content to file_name
            with open(log_file,'w') as f:
                f.write(content)

async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # all_a = soup.find_all('a')
    all_a = soup.css.select("body > pre > a")
    
    log_files = [a['href'].strip() for a in all_a if "apache_logs" in a["href"]]

    tasks = []
    for file_name in log_files:
        url_file_name = f"{url}{file_name}"
        tasks.append(download_aiohttp(url_file_name,file_name))

    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"{end-start:.3}")

if __name__=='__main__':
    asyncio.run(main())
