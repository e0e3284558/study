import requests
from lxml import etree
from CodeClass import YDMHttp


# 封装识别验证码图片的函数
def getCodeText(imgPath, codeType):
    # 用户名
    username = 'e0e3284558'

    # 密码
    password = 'asd123'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 8362

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = 'ec7bbe0c8eb2423b7fa1f7afea87ea93'

    # 图片文件
    filename = imgPath

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = codeType

    # 超时时间，秒
    timeout = 15
    result = None

    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login()
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance()
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout)
        print('cid: %s, result: %s' % (cid, result))
    return result


# 创建一个session对象
session = requests.Session()

# 对验证码图片进行捕获和识别
url = 'http://www.renren.com/SysHome.do'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_src = requests.get(url=code_img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
    fp.write(code_img_src)

# 使用云打码提供的示例代码对验证码图片进行识别
result = getCodeText('./code.jpg', 1006)
print(result)

login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019661241704'
data = {
    'email': 'bifei0827@vip.qq.com',
    'icode': result,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '1c1100af8e6307f3753ddc97426996c8fe65764addca321bd813faa5654c7e0c',
    'rkey': '7f68692e5e69afa1ba418b799ec63a0a',
    'f': 'http%3A%2F%2Fwww.renren.com%2F869029531',
}
# 使用session进行post请求发送
response = session.post(url=login_url, headers=headers, data=data)
print(response.status_code)

detail_url = 'http://www.renren.com/869029531/profile'
# 使用携带cookie的session进行get请求的发送
datail_page_text = session.get(url=detail_url, headers=headers).text

with open('bobo.html', 'w', encoding='utf-8') as fp:
    fp.write(datail_page_text)
