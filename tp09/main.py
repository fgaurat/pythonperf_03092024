import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # all_a = soup.find_all('a')
    all_a = soup.css.select("body > pre > a")
    
    # log_files = []
    # for a in all_a:
    #     if "apache_logs" in a["href"]:
    #         log_files.append(a["href"] )

    log_files = [a['href'].strip() for a in all_a if "apache_logs" in a["href"]]

    pprint(log_files)

    for file_name in log_files:
        url_file_name = f"{url}{file_name}"
        print(url_file_name)
        
        # download url_file_name
        resp = requests.get(url_file_name)
        content = resp.text

        # write content to file_name
        with open(file_name,'w') as f:
            f.write(content)




if __name__=='__main__':
    main()
