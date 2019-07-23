import requests
import os
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
url = 'http://pic.netbian.com/4kfengjing/'
response = requests.get(url=url, headers=headers)
# 手动设定响应数据的编码格式
# response.encoding = 'utf-8'
page_text = response.text
# 数据解析：src属性值
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
# print(li_list)
if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')
for li in li_list:
    img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    # 乱码解决方案
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    # print(img_name, img_src)
    # 请求图片进行持久化存储
    img_data = requests.get(url=img_src, headers=headers).content

    img_path = 'picLibs/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, '下载成功！！')
