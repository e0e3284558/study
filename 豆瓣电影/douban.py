import requests
import json

if __name__ == '__main__':
    # 豆瓣获取电影详情的地址
    url = 'https://movie.douban.com/j/chart/top_list'
    # 参数
    param = {
        'type': '11',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '100',
    }
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    }
    # get 请求
    response = requests.get(url=url, params=param, headers=headers)
    # json存储
    list_data = response.json()
    # 写入文件配置
    fp=open('./douban.json','w',encoding='utf-8')
    # json文件写入
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('结束')