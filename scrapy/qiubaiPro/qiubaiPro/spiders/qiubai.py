# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']

    start_urls = ['https://www.qiushibaike.com/text/']

    # 基于终端指令
    # def parse(self, response):
    #     # 解析作者的名称+段子内容
    #     div_list = response.xpath('//div[@id="content-left"]/div')
    #     all_data = []
    #     for div in div_list:
    #         # 返回为列表，列表元素为selector类型的对象
    #         # extract可以将selector对象中data参数存储字符串提取出来
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #     return all_data

    # 基于管道
    def parse(self, response):
        # 解析作者的名称+段子内容
        div_list = response.xpath('//div[@id="content-left"]/div')
        all_data = []
        for div in div_list:
            # 返回为列表，列表元素为selector类型的对象
            # extract可以将selector对象中data参数存储字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            # 将item提交给管道
            yield item
