import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio
import aiohttp 

async def download_aiohttp(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url,log_file = await queue_download.get() # block        
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                content =await resp.text()
                d = {
                    'content' : content,
                    'log_file' : log_file
                }
                queue_save.put_nowait(d)
        
        queue_download.task_done()

async def save(queue_save):    
    while True:
        data = await queue_save.get() # block        
        content = data['content']
        log_file = data['log_file']

        # write content to file_name
        with open(log_file,'w') as f:
            f.write(content)
        queue_save.task_done()


async def main():
    start = time.perf_counter()
    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()
    nb_download_workers = 10
    nb_save_workers = 5


    url = "https://logs.eolem.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # all_a = soup.find_all('a')
    all_a = soup.css.select("body > pre > a")
    
    log_files = [a['href'].strip() for a in all_a if "apache_logs" in a["href"]]


    tasks = []
    for i in range(nb_download_workers):
        task = asyncio.create_task(download_aiohttp(queue_download,queue_save))
        tasks.append(task)

    for i in range(nb_save_workers):
        task = asyncio.create_task(save(queue_save))
        tasks.append(task)

    for log_file in log_files:
        url_file_name = f"{url}{log_file}"
        t = (url_file_name, log_file)
        queue_download.put_nowait(t)

    await queue_download.join()
    await queue_save.join()
    
    [task.cancel() for task in tasks]    

    end = time.perf_counter()
    print(f"{end-start:.3}")

if __name__=='__main__':
    asyncio.run(main())
