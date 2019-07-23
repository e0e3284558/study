# 引入requests请求库
import requests
import json

if __name__ == '__main__':
    # url
    url = 'https://fanyi.baidu.com/sug'
    # 参数
    word = input('输入需要翻译的值')
    data = {
        'kw': word
    }

    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.post(url, data=data)
    print(response.headers)

    dic_obj = response.json()
    fp = open('./' + word + '.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print(word, '保存成功！！')
