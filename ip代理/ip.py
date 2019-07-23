import requests

# 对验证码图片进行捕获和识别
# url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'
url = 'http://200019.ip138.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
result = requests.get(url=url, headers=headers, proxies={"http": '183.146.213.157:80'}).text
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(result)
