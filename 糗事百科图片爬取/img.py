import requests
import re
import os

if __name__ == '__main__':
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    # 如何爬取图片数据
    url = 'https://www.qiushibaike.com/pic/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    }
    # 使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text

    # 使用聚焦爬虫将页面所有的糗事百科的图片进行解析、提取
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    # print(img_src_list)
    for src in img_src_list:
        # 拼接完整的url
        src = 'https:' + src
        # 请求图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        # 图片路径
        imgPath = './qiutuLibs/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！')

    # content返回的是二进制形式的图片数据
    # text(字符串)  content(二进制)  json(对象)
    # img_data = requests.get(url=url).content

    # with open('./qiutu.jpg', 'wb') as fp:
    #     fp.write(img_data)
