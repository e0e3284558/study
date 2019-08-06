import pymysql
import requests
import os
from lxml import etree
from datetime import datetime, date, timedelta

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="secret",
                       database="query_test", charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义sql
sql = ('SELECT * FROM `myjk`')
# 执行SQL语句
cursor.execute(sql)
result = cursor.fetchall()
# 关闭光标对象
cursor.close()
# 关闭数据库连接
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

for list in result:
    url = list[1]
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    print(url)
    try:
        title = tree.xpath('//*[@id="App"]/div/div[2]/div[1]/div[1]/div[2]/h1/text()')[0]
        # 上线时间
        online_at = tree.xpath('//*[@id="App"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/text()')[2]
        # 收藏数
        collection_num = tree.xpath('//*[@id="App"]/div/div[2]/div[1]/div[1]/div[3]/div/span[2]/span/text()')[0]
        # 阅读数
        read_num = tree.xpath('//*[@id="App"]/div/div[2]/div[1]/div[1]/div[3]/span/span[1]/text()')[0]
        # 推荐数
        recommend_num = 0
        # 评论数
        comment_num = tree.xpath('//*[@id="App"]/div/div[2]/div[1]/div[4]/div[1]/text()')[0]
        # 点赞数
        fabulous_num = tree.xpath('//*[@id="App"]/div/div[2]/div[1]/div[1]/div[3]/div/span[1]/span/text()')[0]
        # 描述
        describe = tree.xpath('//*[@id="App"]/div/div[2]/div[1]/div[2]/div[3]/div/text()')[0]
        # 生成日期
        created_at = date.today().strftime("%Y-%m-%d")

        cursor = conn.cursor()
        sql = "INSERT INTO toutiao_video_info(`toutiao_id`,`toutiao_url`,`toutiao_title`,`online_at`,`collection_num`,`read_num`,`recommend_num`,`comment_num`,`fabulous_num`,`describe`,`created_at`) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')".format(
            list[2], list[1], list[3], online_at, collection_num, read_num, recommend_num, comment_num, fabulous_num,
            describe,
            created_at)
        print(sql)
        # 执行SQL语句
        cursor.execute(sql)
        # 提交事务
        conn.commit()
        cursor.close()
    except LookupError as e:
        str = '{0}####{1} \n'.format(list[1], list[2])
        fo = open("finally.txt", "ab+")
        str = str.encode('utf-8')
        fo.write(str)
        fo.close()

conn.close()
