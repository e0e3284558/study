# 引入requests请求库
import requests
import datetime

if __name__ == '__main__':

    result = []
    cookie = []
    now = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    with open('D://baidu//zhishu.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            result.append(list(line.strip('\n').split(',')))

    with open('D://baidu//cookie.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            cookie = list(line.strip('\n').split(','))

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Cookie": cookie[0]
    }

    for res in result:
        for v in res:
            url = 'http://index.baidu.com/api/SearchApi/index?word={0}&area=0&days=30'.format(v)
            response = requests.get(url=url, headers=headers)
            dic_obj = response.json()
            if (dic_obj['data']):
                value = dic_obj['data']['generalRatio'][0]['wise']['avg']
            else:
                value = '未收录'

            str = '{0}####{1} \n'.format(v, value)
            fo = open("D://baidu//zs-result-{0}.txt".format(now), "ab+")
            str = str.encode('utf-8')
            fo.write(str)
            fo.close()
            print('{0}，搜索量 {1}'.format(v, value))
