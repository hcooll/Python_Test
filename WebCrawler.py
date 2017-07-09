import requests
import re

url = 'https://www.crowdfunder.com'
params = {
    'q': 'filter',
    'page': '4',
    'template': 'true',
    'random_seed': '195'
}

html = requests.get(url, params).text

# print(html)

a = re.findall('\"card-body\">(.*?)<!-- end .card-image -->', html, re.S)

for each in a:
    print(re.search('\"card-title\">(.*?)</div>', each).group(1))
