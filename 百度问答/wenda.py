# 引入requests请求库
import requests
import json
import sys
import os
from lxml import etree

if __name__ == '__main__':

    result = []
    with open('D:\\baidu\\baidukeyword.txt', 'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split(',')))

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    for v in result:
        for it in v:
            url = 'http://m.baidu.com/s?word={0}'.format(it)
            response = requests.get(url=url, headers=headers)
            page_text = response.text
            tree = etree.HTML(page_text)
            li_list = tree.xpath('//*[@class="source-left"]/div')
            if (li_list):
                str = '{0}####{1} {2} \n'.format(it, li_list[0].text, li_list[1].text)
            else:
                str = '{0}####{1} \n'.format(it, '无精选问答')
            fo = open("D:\\baidu\\result.txt", "ab+")
            str = str.encode('utf-8')
            fo.write(str)
            fo.close()
            print(it + '结束')
