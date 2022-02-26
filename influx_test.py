import time
import requests
import json

rbc_urls = [
    'https://www.dav-rbc.de/072/185829.php',
    'https://www.dav-rbc.de/072/test1.php',
    'https://www.dav-rbc.de/072/test2.php'
]

result = []
for url in rbc_urls:
    url_result = dict()
    start = time.time()
    t1 = requests.get(url).elapsed.total_seconds()
    t2 = time.time() - start
    url_result['TTFB'] = t1
    url_result['response_time'] = t2
    url_result['url'] = url
    result.append(url_result)

print(json.dumps(result))
    # 'DAVRBC,host=home,method=GET,result=success,server=https://www.dav-rbc.de/072/185829.php,status_code=200 content_length=473244i,http_response_code=200i,response_time=0.212321251,result_code=0i,result_type="success" 1645857733000000000'

