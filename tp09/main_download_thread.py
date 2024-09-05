import threading
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time


def download(url,log_file):
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

    thread_list = []
    for file_name in log_files:
        url_file_name = f"{url}{file_name}"
        th = threading.Thread(target=download,args=(url_file_name,file_name))
        th.start()
        thread_list.append(th)


    [t.join() for t in thread_list]


    end = time.perf_counter()
    print(f"{end-start:.3}")


if __name__=='__main__':
    main()
