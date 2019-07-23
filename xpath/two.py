import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
url = 'https://bj.58.com/ershoufang/'
page_text = requests.get(url=url, headers=headers).text
# 数据解析
tree = etree.HTML(page_text)
# 存储的是li标签对象
li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
# 文件存储
fp = open('58.txt', 'w', encoding='utf-8')

for li in li_list:
    # 获取a标签文本
    title = li.xpath('./div[2]/h2/a/text()')[0]
    print(title)
    # 追加写入文件
    fp.write(title + "\n")
