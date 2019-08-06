# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # 允许的域名
    # allowed_domains = ['www.xxx.com']
    # 起始的url列表，该列表中存放的url会被scrapy自动进行发送请求
    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com/']

    # 用于数据解析：response 参数表示的就是请求成功后对应的响应对象
    def parse(self, response):
        print(response)
        # pass
