import concurrent.futures
import urllib.request

URLS = [
    'http://www.foxnews.com',
    'http://www.cnn.com',
    'https://edition.cnn.com/',
    'https://www.bbc.co.uk/',
    'https://www.wp.pl',
    'https://www.hbomax.com/pl/pl',
    'http://government.ru/en/department/94/events/'
]

def load_url(url,timeout):
    with urllib.request.urlopen(url,timeout=timeout) as conn:
        return conn.read()
    
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    future_to_url = {executor.submit(load_url,url,60):url
                     for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        
        try:
            data = future.result()
        except Exception as exc:
            print(f"{url} generuje wyjątek: {exc}")
        else:
            print(f"{url} - strona ma roziar: {len(data)} bajtów")