# coding = utf-8

import requests
import re
import os
import shutil
import sys

# sys.set

# url = 'https://www.crowdfunder.com'
# params = {
#     'q': 'filter',
#     'page': '4',
#     'template': 'true',
#     'random_seed': '195'
# }
#
# html = requests.get(url, params).text
#
# # print(html)
#
# a = re.findall('\"card-body\">(.*?)<!-- end .card-image -->', html, re.S)
#
# for each in a:
#     print(re.search('\"card-title\">(.*?)</div>', each).group(1))
#
#

# phone = "2004-959-559 # 这是一个国外电话号码"
#
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码是: ", num)
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print("电话号码是 : ", num)

url = 'http://www.jikexueyuan.com/course/?pageNum=1'

with open("jike.txt", 'a', encoding='utf-8') as f:
    for i in range(1, 2):
        url = re.sub('[0-9][0-9]?', str(i), url)
        print(url)
        rep = requests.get(url)
        # print(text)
        text = re.findall('class="lesson-info-h2">(.*?)</div>', rep.text, re.S)

        f.write(text[0])
        f.write('\n')
        f.flush()
    f.close()
