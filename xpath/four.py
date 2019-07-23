import requests
import os
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
url = 'https://www.aqistudy.cn/historydata/'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)

# # 两次解析
# host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
# all_city_names = []
# # 解析到热门城市
# for li in host_li_list:
#     hot_city_name = li.xpath('./a/text()')[0]
#     all_city_names.append(hot_city_name)
#
# # 解析的是全部城市的名称
# city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
# for li in city_names_list:
#     city_name = li.xpath('./a/text()')[0]
#     all_city_names.append(city_name)
#
# print(all_city_names)
# print(len(all_city_names))

# 一次解析所有城市
# //div[@class="bottom"]/ul/li  热门城市
# //div[@class="bottom"]/ul/div[2]/li/a  热门城市
a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
all_city_names=[]
for a in a_list:
    city_name = a.xpath('./text()')[0]
    all_city_names.append(city_name)
print(all_city_names)
print(len(all_city_names))
