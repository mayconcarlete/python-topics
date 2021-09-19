import requests
from concurrent.futures import ThreadPoolExecutor

def get_url(url):
    return requests.get(url)

list_of_urls = ["https://postman-echo.com/get?foo1=bar1&foo2=bar2"]*10

with ThreadPoolExecutor(max_workers=10) as pool:
    response_list = list(pool.map(get_url,list_of_urls))

for response in response_list:
    print(response)
