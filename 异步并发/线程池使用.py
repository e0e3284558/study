import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    print(detail_url)
    print(name)
    # 对详情页发起请求
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    # 从详情页解析出视频的地址
    ex = 'srcUrl="(.*?)",vdoUrl'
    video_url = re.findall(ex, detail_page_text)[0]
    print(video_url)
    dic = {
        'name': name,
        'url': video_url
    }
    urls.append(dic)


def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载!')
    data = requests.get(url=url, headers=headers).content
    # 持久化存储操作
    with open(dic['name'], 'wb') as fp:
        fp.write(data)
        print(dic['name'], '下载成功!')


# 使用线程池对视频数据进行请求
pool = Pool(4)
pool.map(get_video_data, urls)

pool.close()
pool.join()
