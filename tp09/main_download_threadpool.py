import threading
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import concurrent.futures


def download(url,log_file):
    print(threading.current_thread().name)
    # download url_file_name
    resp = requests.get(url)
    content = resp.text
    # write content to file_name
    with open(log_file,'w') as f:
        f.write(content)

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # all_a = soup.find_all('a')
    all_a = soup.css.select("body > pre > a")
    
    log_files = [a['href'].strip() for a in all_a if "apache_logs" in a["href"]]

    param_urls = []
    param_files = []
    for file_name in log_files:
        url_file_name = f"{url}{file_name}"
        param_urls.append(url_file_name)
        param_files.append(file_name)

    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     executor.map(download,param_urls,param_files)
    try : 
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        executor.map(download,param_urls,param_files)

        executor2 = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        executor2.map(download,param_urls,param_files)
    
    
    finally:    
        executor.shutdown(wait=True)
        executor2.shutdown(wait=True)





    end = time.perf_counter()
    print(f"{end-start:.3}")


if __name__=='__main__':
    main()
