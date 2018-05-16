# -*- coding: utf-8 -*-
"""
@author: Yi_Zhou
"""
import time
from lxml import etree
import requests

page = 1

fp = open('糗事百科.txt', 'w', encoding = 'UTF-8')

while page < 2:

    header = \
        {'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    url = \
        'https://www.qiushibaike.com/hot/page/' + str(page)
    html = requests.get(url, headers = header).text

    xml = etree.HTML(html)

    content = xml.xpath('//div[@class="content"]/span')

    for i in content:

        fp = open('糗事百科.txt', 'a', encoding = 'UTF-8')

        fp.write(i.text)

    page += 1

    time.sleep(2)

fp.close()

print ('写入完成啦！')


